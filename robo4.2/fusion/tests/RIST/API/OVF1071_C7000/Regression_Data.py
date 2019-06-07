from robot.libraries.BuiltIn import BuiltIn

# Credentials
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
oa_credentials = {'username': 'Administrator', 'password': 'hpvse14'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

# Resource types for X-API-Version=800
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV9'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

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
ENC1SHBAY1 = '%s, bay 1' % ENC1    # BL465c Gen8
ENC1SHBAY2 = '%s, bay 2' % ENC1    # BL465c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1    # BL465c Gen8
ENC1SHBAY4 = '%s, bay 4' % ENC1    # BL420c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1    # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1    # BL460c G6
ENC1SHBAY8 = '%s, bay 7' % ENC1    # BL495c G5
ENC1SHBAY14 = '%s, bay 14' % ENC1  # BL460c Gen10
ENC1SHBAY16 = '%s, bay 16' % ENC1  # BL460c Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2    # BL465c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2    # BL465c Gen8
ENC2SHBAY3 = '%s, bay 3' % ENC2    # BL465c Gen8
ENC2SHBAY4 = '%s, bay 4' % ENC2    # BL420c Gen8
ENC2SHBAY5 = '%s, bay 5' % ENC2    # BL460c Gen9
ENC2SHBAY6 = '%s, bay 6' % ENC2    # BL460c G6
ENC2SHBAY7 = '%s, bay 7' % ENC2    # BL2x220c G5
ENC2SHBAY10 = '%s, bay 10' % ENC2  # BL460c Gen10
ENC2SHBAY16 = '%s, bay 16' % ENC2  # BL460c Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3    # BL465c Gen8
ENC3SHBAY2 = '%s, bay 2' % ENC3    # BL465c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3    # BL465c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3    # BL420c Gen8
ENC3SHBAY5 = '%s, bay 5' % ENC3    # BL460c Gen9
ENC3SHBAY7 = '%s, bay 7' % ENC3    # BL660c Gen9
ENC3SHBAY8 = '%s, bay 8' % ENC3    # BL660c Gen8
ENC3SHBAY9 = '%s, bay 9' % ENC3    # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL465c G7
# LIGs and EGs
LIG1_NAME = 'LIG22'
EG1_NAME = 'EG22'
LIG2_NAME = 'LIG23'
EG2_NAME = 'EG23'
LIG3_NAME = 'LIG26'
EG3_NAME = 'EG26'

enclosures_expected = [
    {
        "type": ENCLOSURE_TYPE,
        "name": "wpst22",
        "state": "Configured",

    },
    {
        "type": ENCLOSURE_TYPE,
        "name": "wpst23",
        "state": "Configured",

    },
    {
        "type": ENCLOSURE_TYPE,
        "name": "wpst23",
        "state": "Configured",

    },
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
# volumes
NAME_PREFIX = 'C7000-Reg1-OVF1071-'
VOLUME_NAME_PREFIX = NAME_PREFIX
VOLUME_3PAR1_SHARED = VOLUME_NAME_PREFIX + '3par1-shared'
VOLUME_VSA1_SHARED = VOLUME_NAME_PREFIX + 'vsa1-shared'
VOLUME_VSA2_SHARED = VOLUME_NAME_PREFIX + 'vsa2-shared'
VOLUME_VSA1_PRIV = VOLUME_NAME_PREFIX + 'vsa1-priv'
VOLUME_VSA2_PRIV = VOLUME_NAME_PREFIX + 'vsa2-priv'

storage_systems = [
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': STORESERV1_NAME,
        'family': 'StoreServ',
        "hostname": STORESERV1_HOSTNAME,
        'credentials': {
            'username': 'fusionadm',
            'password': 'hpvse1'
        },
        "deviceSpecificAttributes":
        {
            "discoveredDomains":
            [
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
        'type': STORAGE_SYSTEM_TYPE,
        'name': STOREVIRTUAL1_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL1_HOSTNAME,
        "credentials": {
            "username": "admin",
            "password": 'admin'
        },
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
        'type': STORAGE_SYSTEM_TYPE,
        'name': STOREVIRTUAL2_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL2_HOSTNAME,
        "credentials": {
            "username": "admin",
            "password": 'admin'
        },
        "ports": [
            {
                "name": STOREVIRTUAL2_VIP,
                "expectedNetworkUri": "ETH:network-tunnel",
                "expectedNetworkName": "network-tunnel",
                "mode": "Managed",

            },
        ],

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
        "name": VOLUME_TEMPLATE_3PAR1_POOL1_PRIVATE,
        "description": "",
        "rootTemplateUri": "Volume root template for StoreServ 3.1.3",
        "properties": {
            "name": {
                "title": "Volume name",
                "description": "A volume name between 1 and 100 characters",
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True,
                "meta": {
                    "locked": False}
            },
            "description": {
                "title": "Description",
                "description": "A description for the volume",
                "type": "string",
                "minLength": 0,
                "maxLength": 2000,
                "default": "3Par1 pool1 private",
                "meta": {
                    "locked": False}
            },
            "storagePool": {
                "title": "Storage Pool",
                "description": "A common provisioning group URI reference",
                "type": "string",
                "required": True,
                "format": "x-uri-reference",
                "meta": {
                    "locked": False,
                    "createOnly": True,
                    "semanticType": "device-storage-pool"
                },
                "default": STORESERV1_POOL1

            },
            "size": {
                "title": "Capacity",
                "description": "The capacity of the volume in bytes",
                "type": "integer",
                "required": True,
                "minimum": 1073741824,
                "maximum": 17592186044416,
                "meta": {
                    "locked": False,
                    "semanticType": "capacity"
                },
                "default": 1073741824,

            },
            "isShareable": {
                "title": "Is Shareable",
                "description": "The shareability of the volume",
                "type": "boolean",
                "meta": {
                    "locked": False
                },
                "default": False,

            },
            "provisioningType": {
                "title": "Provisioning Type",
                "description": "The provisioning type for the volume",
                "type": "string",
                "enum": [
                    "Thin",
                    "Full"],
                "meta":{
                    "locked": True,
                    "createOnly": True
                },
                "default": "Thin"
            },
            "snapshotPool": {
                "title": "Snapshot Pool",
                "description": "A URI referenceto the common provisioning group used to create snapshots",
                "type": "string",
                "format": "x-uri-reference",
                "meta": {
                    "locked": True,
                    "semanticType": "device-snapshot-storage-pool"
                },
                "default": STORESERV1_POOL1,
            }

        },

    },
    {
        "name": VOLUME_TEMPLATE_3PAR1_POOL1_SHARED,
        "description": "",
        "rootTemplateUri": "Volume root template for StoreServ 3.1.3",
        "properties": {
            "name": {
                "title": "Volume name",
                "description": "A volume name between 1 and 100 characters",
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True,
                "meta": {
                    "locked": False}
            },
            "description": {
                "title": "Description",
                "description": "A description for the volume",
                "type": "string",
                "minLength": 0,
                "maxLength": 2000,
                "default": "3Par pool1 shared",
                "meta": {
                    "locked": False}
            },
            "storagePool": {
                "title": "Storage Pool",
                "description": "A common provisioning group URI reference",
                "type": "string",
                "required": True,
                "format": "x-uri-reference",
                "meta": {
                    "locked": False,
                    "createOnly": True,
                    "semanticType": "device-storage-pool"
                },
                "default": STORESERV1_POOL1

            },
            "size": {
                "title": "Capacity",
                "description": "The capacity of the volume in bytes",
                "type": "integer",
                "required": True,
                "minimum": 1073741824,
                "maximum": 17592186044416,
                "meta": {
                    "locked": False,
                    "semanticType": "capacity"
                },
                "default": 1073741824,

            },
            "isShareable": {
                "title": "Is Shareable",
                "description": "The shareability of the volume",
                "type": "boolean",
                "meta": {
                    "locked": False
                },
                "default": True,

            },
            "provisioningType": {
                "title": "Provisioning Type",
                "description": "The provisioning type for the volume",
                "type": "string",
                "enum": [
                    "Thin",
                    "Full"],
                "meta":{
                    "locked": True,
                    "createOnly": True
                },
                "default": "Thin"
            },
            "snapshotPool": {
                "title": "Snapshot Pool",
                "description": "A URI referenceto the common provisioning group used to create snapshots",
                "type": "string",
                "format": "x-uri-reference",
                "meta": {
                    "locked": True,
                    "semanticType": "device-snapshot-storage-pool"
                },
                "default": STORESERV1_POOL1,
            }

        },

    },
    {
        "name": VOLUME_TEMPLATE_VSA1_RAID5_PRIVATE,
        "description": "",
        "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
        "properties": {
            "name": {
                "title": "Volume name",
                "description": "A volume name between 1 and 100 characters",
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True,
                "meta": {
                    "locked": False}
            },
            "description": {
                "title": "Description",
                "description": "A description for the volume",
                "type": "string",
                "minLength": 0,
                "maxLength": 2000,
                "default": "VSA1 RAID5 private",
                "meta": {
                    "locked": False}
            },
            "storagePool": {
                "title": "Storage Pool",
                "description": "StoragePoolURI the volume should be added to",
                "type": "string",
                "format": "x-uri-reference",
                "required": True,
                "meta": {
                    "locked": False,
                    "createOnly": True,
                    "semanticType": "device-storage-pool"
                },
                "default": STOREVIRTUAL1_POOL
            },
            "size": {
                "title": "Capacity",
                "description": "Capacity of the volume in bytes",
                "type": "integer",
                "minimum": 4194304,
                "required": True,
                "default": 1073741824,
                "meta": {
                    "locked": False,
                    "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string",
                "enum": [
                    "NetworkRaid0None",
                    "NetworkRaid5SingleParity",
                    "NetworkRaid10Mirror2Way",
                    "NetworkRaid10Mirror3Way",
                    "NetworkRaid10Mirror4Way",
                    "NetworkRaid6DualParity"],
                "default":"NetworkRaid5SingleParity",
                "required":True,
                "meta":{
                    "locked": True,
                    "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type",
                "description": "The provisioning type for the volume",
                "type": "string",
                "enum": [
                    "Thin",
                    "Full"],
                "default":"Thin",
                "meta":{
                    "locked": True,
                    "createOnly": "True",
                    "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization",
                "description": "",
                "type": "boolean",
                "default": True,
                "meta": {
                    "locked": True}
            },
            "isShareable": {
                "title": "Is Shareable",
                "description": "The shareability of the volume",
                "type": "boolean",
                "default": False,
                "meta": {
                    "locked": False}
            }

        },

    },
    {
        "name": VOLUME_TEMPLATE_VSA1_RAID5_SHARED,
        "description": "",
        "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
        "properties": {
            "name": {
                "title": "Volume name",
                "description": "A volume name between 1 and 100 characters",
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True,
                "meta": {
                    "locked": False}
            },
            "description": {
                "title": "Description",
                "description": "A description for the volume",
                "type": "string",
                "minLength": 0,
                "maxLength": 2000,
                "default": "VSA1 RAID5 shared",
                "meta": {
                    "locked": False}
            },
            "storagePool": {
                "title": "Storage Pool",
                "description": "StoragePoolURI the volume should be added to",
                "type": "string",
                "format": "x-uri-reference",
                "required": True,
                "meta": {
                    "locked": False,
                    "createOnly": True,
                    "semanticType": "device-storage-pool"
                },
                "default": STOREVIRTUAL1_POOL
            },
            "size": {
                "title": "Capacity",
                "description": "Capacity of the volume in bytes",
                "type": "integer",
                "minimum": 4194304,
                "required": True,
                "default": 1073741824,
                "meta": {
                    "locked": False,
                    "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string",
                "enum": [
                    "NetworkRaid0None",
                    "NetworkRaid5SingleParity",
                    "NetworkRaid10Mirror2Way",
                    "NetworkRaid10Mirror3Way",
                    "NetworkRaid10Mirror4Way",
                    "NetworkRaid6DualParity"],
                "default":"NetworkRaid5SingleParity",
                "required":True,
                "meta":{
                    "locked": True,
                    "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type",
                "description": "The provisioning type for the volume",
                "type": "string",
                "enum": [
                    "Thin",
                    "Full"],
                "default":"Thin",
                "meta":{
                    "locked": True,
                    "createOnly": "True",
                    "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization",
                "description": "",
                "type": "boolean",
                "default": True,
                "meta": {
                    "locked": True}
            },
            "isShareable": {
                "title": "Is Shareable",
                "description": "The shareability of the volume",
                "type": "boolean",
                "default": True,
                "meta": {
                    "locked": False}
            }

        },

    },
    {
        "name": VOLUME_TEMPLATE_VSA2_RAID0_PRIVATE,
        "description": "",
        "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
        "properties": {
            "name": {
                "title": "Volume name",
                "description": "A volume name between 1 and 100 characters",
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True,
                "meta": {
                    "locked": False}
            },
            "description": {
                "title": "Description",
                "description": "A description for the volume",
                "type": "string",
                "minLength": 0,
                "maxLength": 2000,
                "default": "VSA2 RAID0 private",
                "meta": {
                    "locked": False}
            },
            "storagePool": {
                "title": "Storage Pool",
                "description": "StoragePoolURI the volume should be added to",
                "type": "string",
                "format": "x-uri-reference",
                "required": True,
                "meta": {
                    "locked": False,
                    "createOnly": True,
                    "semanticType": "device-storage-pool"
                },
                "default": STOREVIRTUAL2_POOL
            },
            "size": {
                "title": "Capacity",
                "description": "Capacity of the volume in bytes",
                "type": "integer",
                "minimum": 4194304,
                "required": True,
                "default": 1073741824,
                "meta": {
                    "locked": False,
                    "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string",
                "enum": [
                    "NetworkRaid0None",
                    "NetworkRaid5SingleParity",
                    "NetworkRaid10Mirror2Way",
                    "NetworkRaid10Mirror3Way",
                    "NetworkRaid10Mirror4Way",
                    "NetworkRaid6DualParity"],
                "default":"NetworkRaid0None",
                "required":True,
                "meta":{
                    "locked": True,
                    "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type",
                "description": "The provisioning type for the volume",
                "type": "string",
                "enum": [
                    "Thin",
                    "Full"],
                "default":"Thin",
                "meta":{
                    "locked": True,
                    "createOnly": "True",
                    "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization",
                "description": "",
                "type": "boolean",
                "default": True,
                "meta": {
                    "locked": True}
            },
            "isShareable": {
                "title": "Is Shareable",
                "description": "The shareability of the volume",
                "type": "boolean",
                "default": False,
                "meta": {
                    "locked": False}
            }

        },

    },
    {
        "name": VOLUME_TEMPLATE_VSA2_RAID0_SHARED,
        "description": "",
        "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
        "properties": {
            "name": {
                "title": "Volume name",
                "description": "A volume name between 1 and 100 characters",
                "type": "string",
                "minLength": 1,
                "maxLength": 100,
                "required": True,
                "meta": {
                    "locked": False}
            },
            "description": {
                "title": "Description",
                "description": "A description for the volume",
                "type": "string",
                "minLength": 0,
                "maxLength": 2000,
                "default": "VSA2 RAID0 shared",
                "meta": {
                    "locked": False}
            },
            "storagePool": {
                "title": "Storage Pool",
                "description": "StoragePoolURI the volume should be added to",
                "type": "string",
                "format": "x-uri-reference",
                "required": True,
                "meta": {
                    "locked": False,
                    "createOnly": True,
                    "semanticType": "device-storage-pool"
                },
                "default": STOREVIRTUAL2_POOL
            },
            "size": {
                "title": "Capacity",
                "description": "Capacity of the volume in bytes",
                "type": "integer",
                "minimum": 4194304,
                "required": True,
                "default": 1073741824,
                "meta": {
                    "locked": False,
                    "semanticType": "capacity"}
            },
            "dataProtectionLevel": {
                "title": "Data Protection Level",
                "description": "Indicates the number and configuration of data copies in the Storage Pool",
                "type": "string",
                "enum": [
                    "NetworkRaid0None",
                    "NetworkRaid5SingleParity",
                    "NetworkRaid10Mirror2Way",
                    "NetworkRaid10Mirror3Way",
                    "NetworkRaid10Mirror4Way",
                    "NetworkRaid6DualParity"],
                "default":"NetworkRaid0None",
                "required":True,
                "meta":{
                    "locked": True,
                    "semanticType": "device-dataProtectionLevel"}
            },
            "provisioningType": {
                "title": "Provisioning Type",
                "description": "The provisioning type for the volume",
                "type": "string",
                "enum": [
                    "Thin",
                    "Full"],
                "default":"Thin",
                "meta":{
                    "locked": True,
                    "createOnly": "True",
                    "semanticType": "device-provisioningType"}
            },
            "isAdaptiveOptimizationEnabled": {
                "title": "Adaptive Optimization",
                "description": "",
                "type": "boolean",
                "default": True,
                "meta": {
                    "locked": True}
            },
            "isShareable": {
                "title": "Is Shareable",
                "description": "The shareability of the volume",
                "type": "boolean",
                "default": True,
                "meta": {
                    "locked": False}
            }

        },

    },
]

storage_volumes = [
    {
        "properties": {
            "name": VOLUME_3PAR1_SHARED,
            "storagePool": STORESERV1_POOL1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "isShareable": True,
            "snapshotPool": STORESERV1_POOL1
        },
        "templateUri": 'ROOT',
        "isPermanent": True,

    },
    {
        "properties": {
            "name": VOLUME_VSA1_SHARED,
            "storagePool": STOREVIRTUAL1_POOL,
            "size": 1073741824,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "provisioningType": "Thin",
            "isShareable": True,
            "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": VOLUME_TEMPLATE_VSA1_RAID5_SHARED,
        "isPermanent": True,

    },
    {
        "properties": {
            "name": VOLUME_VSA2_SHARED,
            "storagePool": STOREVIRTUAL2_POOL,
            "size": 1073741824,
            "dataProtectionLevel": "NetworkRaid0None",
            "provisioningType": "Thin",
            "isShareable": True,
            "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": 'ROOT',
        "isPermanent": True,

    },
    {
        "properties": {
            "name": VOLUME_VSA1_PRIV,
            "storagePool": STOREVIRTUAL1_POOL,
            "size": 1073741824,
            "dataProtectionLevel": "NetworkRaid5SingleParity",
            "provisioningType": "Thin",
            "isShareable": False,
            "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": 'ROOT',
        "isPermanent": True,

    },
    {
        "properties": {
            "name": VOLUME_VSA2_PRIV,
            "storagePool": STOREVIRTUAL2_POOL,
            "size": 1073741824,
            "dataProtectionLevel": "NetworkRaid0None",
            "provisioningType": "Thin",
            "isShareable": False,
            "isAdaptiveOptimizationEnabled": True
        },
        "templateUri": VOLUME_TEMPLATE_VSA2_RAID0_SHARED,
        "isPermanent": True,

    },

]

# SHT
SHT1 = 'SH:' + ENC1SHBAY3
SHT2 = 'SH:' + ENC1SHBAY5
SHT3 = 'SH:' + ENC3SHBAY3
SHT4 = 'SH:' + ENC3SHBAY7

# iSCSI connections
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
FIRST_BOOT_TARGET_IP = "192.168.21.71"
INITIATOR_IP_1 = "192.168.22.63"
INITIATOR_IP_2 = "192.168.22.64"

# SPTs and Profiles
SPT_NAME_PREFIX = NAME_PREFIX
PROFILE_NAME_PREFIX = NAME_PREFIX
PROFILE_IQN_PREFIX = "iqn.2015-02.com.hpe:oneview-"
# SPTs
# NTS1 SPT, volumes, and EG
NTS1_SPT1_NAME = SPT_NAME_PREFIX + 'nts1-spt1'
NTS1_SPT2_NAME = SPT_NAME_PREFIX + 'nts1-spt2'
NTS1_SPT3_NAME = SPT_NAME_PREFIX + 'nts1-spt3'
NTS1_SPT4_NAME = SPT_NAME_PREFIX + 'nts1-spt4'
NTS1_SPT5_NAME = SPT_NAME_PREFIX + 'nts1-spt5'
NTS1_SPT6_NAME = SPT_NAME_PREFIX + 'nts1-spt6'
NTS1_SPT7_NAME = SPT_NAME_PREFIX + 'nts1-spt7'
NTS1_SPT8_NAME = SPT_NAME_PREFIX + 'nts1-spt8'
NTS1_SPT9_NAME = SPT_NAME_PREFIX + 'nts1-spt9'
NTS1_SPT10_NAME = SPT_NAME_PREFIX + 'nts1-spt10'
NTS1_SPT11_NAME = SPT_NAME_PREFIX + 'nts1-spt11'
VOLUME_NTS1_VOL_1 = 'nts1-vol1'
VOLUME_NTS1_VOL_2 = 'nts1-vol2'
NTS1_SPT_EG = EG1_NAME
# NTS2 SPT, volumes, and EG
NTS2_SPT = SPT_NAME_PREFIX + 'nts2-spt'
VOLUME_NTS2_VOL_1 = 'nts2-vsa-vol1'
VOLUME_NTS2_VOL_2 = 'nts2-vsa-vol2'
VOLUME_NTS2_VOL_3 = 'nts2-vsa-vol3'
VOLUME_NTS2_VOL_4 = 'nts2-vsa-vol4'
NTS2_SPT_EG = EG1_NAME
# NTS3 SPT, SP, volumes, and EG
NTS3_SPT_NAME = SPT_NAME_PREFIX + 'nts3-spt'
VOLUME_NTS3_VOL_1 = 'nts3-vsa-vol1'
VOLUME_NTS3_VOL_2 = 'nts3-vsa-vol2'
NTS3_SPT_EG = EG1_NAME
NTS3_PROFILE_NAME = PROFILE_NAME_PREFIX + 'nts3-profile'
NTS3_PROFILE_SERVER = ENC1SHBAY3
NTS3_PROFILE_EG = EG1_NAME
NTS3_PROFILE_ENC = ENC1
NTS3_PROFILE_IQN = PROFILE_IQN_PREFIX + NTS3_PROFILE_NAME
# Positive SPT and EG
SPT1_NAME = SPT_NAME_PREFIX + "spt1"
SPT1_EG = EG1_NAME
SPT2_NAME = SPT_NAME_PREFIX + "spt2"
SPT2_EG = EG1_NAME
SPT3_NAME = SPT_NAME_PREFIX + "spt3"
SPT3_EG = EG3_NAME
SPT4_NAME = SPT_NAME_PREFIX + "spt4"
SPT4_EG = EG3_NAME
# PTS1/PTS2/PTS3/PTS4 SPT volumes
VOLUME_SPT2_VSA1_PERM_PRIV = VOLUME_NAME_PREFIX + 'spt2-vsa1-perm-priv'
VOLUME_SPT2_VSA2_PERM_PRIV = VOLUME_NAME_PREFIX + 'spt2-vsa2-perm-priv'
VOLUME_SPT3_3PAR1_EPH_PRIV = VOLUME_NAME_PREFIX + 'spt3-3par1-eph-priv'
VOLUME_SPT3_VSA2_EPH_PRIV = VOLUME_NAME_PREFIX + 'spt3-vsa2-eph-priv'
VOLUME_SPT4_VSA1_EPH_PRIV = VOLUME_NAME_PREFIX + 'spt4-vsa1-eph-priv'
VOLUME_SPT4_VSA2_EPH_PRIV = VOLUME_NAME_PREFIX + 'spt4-vsa2-eph-priv'
# PTS5 SPT volumes
VOLUME_SPT2_VSA1_EPH_PRIV1 = VOLUME_NAME_PREFIX + 'profile2-vsa1-eph-priv1'
VOLUME_SPT2_VSA1_EPH_PRIV2 = VOLUME_NAME_PREFIX + 'profile2-vsa1-eph-priv2'
VOLUME_SPT2_VSA1_EPH_PRIV3 = VOLUME_NAME_PREFIX + 'profile2-vsa1-eph-priv3'
VOLUME_SPT3_3PAR1_EPH_PRIV1 = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv1'
VOLUME_SPT3_3PAR1_EPH_PRIV2 = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv2'
VOLUME_SPT3_3PAR1_EPH_PRIV3 = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv3'
VOLUME_SPT4_VSA2_EPH_PRIV1 = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv1'
VOLUME_SPT4_VSA2_EPH_PRIV2 = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv2'
VOLUME_SPT4_VSA2_EPH_PRIV3 = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv3'
# Profiles
# Profile name and iQN
PROFILE_NAME_PREFIX = NAME_PREFIX
PROFILE_IQN_PREFIX = "iqn.2015-02.com.hpe:oneview-"
SPT1_PROFILE1_NAME = PROFILE_NAME_PREFIX + "spt1-profile1"
SPT1_PROFILE1_IQN = PROFILE_IQN_PREFIX + SPT1_PROFILE1_NAME
SPT2_PROFILE1_NAME = PROFILE_NAME_PREFIX + "spt2-profile1"
SPT2_PROFILE1_IQN = PROFILE_IQN_PREFIX + SPT2_PROFILE1_NAME
SPT3_PROFILE1_NAME = PROFILE_NAME_PREFIX + "spt3-profile1"
SPT3_PROFILE1_IQN = PROFILE_IQN_PREFIX + SPT3_PROFILE1_NAME
SPT4_PROFILE1_NAME = PROFILE_NAME_PREFIX + "spt4-profile1"
SPT4_PROFILE1_IQN = PROFILE_IQN_PREFIX + SPT4_PROFILE1_NAME
# Profile server, EG, and ENC
SPT1_PROFILE1_SERVER = ENC1SHBAY3
SPT1_PROFILE1_EG = EG1_NAME
SPT1_PROFILE1_ENC = ENC1
SPT2_PROFILE1_SERVER = ENC1SHBAY5
SPT2_PROFILE1_EG = EG1_NAME
SPT2_PROFILE1_ENC = ENC1
SPT3_PROFILE1_SERVER = ENC3SHBAY3
SPT3_PROFILE1_EG = EG3_NAME
SPT3_PROFILE1_ENC = ENC3
SPT4_PROFILE1_SERVER = ENC3SHBAY7
SPT4_PROFILE1_EG = EG3_NAME
SPT4_PROFILE1_ENC = ENC3
# PTS3 and PTS4 volumes
VOLUME_PROFILE2_VSA1_PERM_PRIV = VOLUME_NAME_PREFIX + 'profile2-vsa1-perm-priv'
VOLUME_PROFILE2_VSA2_PERM_PRIV = VOLUME_NAME_PREFIX + 'profile2-vsa2-perm-priv'
VOLUME_PROFILE3_3PAR1_EPH_PRIV = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv'
VOLUME_PROFILE3_VSA2_EPH_PRIV = VOLUME_NAME_PREFIX + 'profile3-vsa2-eph-priv'
VOLUME_PROFILE3_3PAR1_PERM_PRIV = VOLUME_NAME_PREFIX + 'profile3-3par1-perm-priv'
VOLUME_PROFILE3_VSA2_PERM_PRIV = VOLUME_NAME_PREFIX + 'profile3-vsa2-perm-priv'
VOLUME_PROFILE4_VSA1_EPH_PRIV = VOLUME_NAME_PREFIX + 'profile4-vsa1-eph-priv'
VOLUME_PROFILE4_VSA2_EPH_PRIV = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv'
# PTS5 profile volumes
VOLUME_PROFILE2_VSA1_EPH_PRIV1 = VOLUME_NAME_PREFIX + 'profile2-vsa1-eph-priv1'
VOLUME_PROFILE2_VSA1_EPH_PRIV2 = VOLUME_NAME_PREFIX + 'profile2-vsa1-eph-priv2'
VOLUME_PROFILE2_VSA1_EPH_PRIV3 = VOLUME_NAME_PREFIX + 'profile2-vsa1-eph-priv3'
VOLUME_PROFILE3_3PAR1_EPH_PRIV1 = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv1'
VOLUME_PROFILE3_3PAR1_EPH_PRIV2 = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv2'
VOLUME_PROFILE3_3PAR1_EPH_PRIV3 = VOLUME_NAME_PREFIX + 'profile3-3par1-eph-priv3'
VOLUME_PROFILE4_VSA2_EPH_PRIV1 = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv1'
VOLUME_PROFILE4_VSA2_EPH_PRIV2 = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv2'
VOLUME_PROFILE4_VSA2_EPH_PRIV3 = VOLUME_NAME_PREFIX + 'profile4-vsa2-eph-priv3'
# Profile complinace and ATAI REGEX
ATAI_REGEX = "REGEX:[a-z,0-9]{8}-[a-z,0-9]{4}-[a-z,0-9]{4}-[a-z,0-9]{4}-[a-z,0-9]{12}"
COMPLIANCE_MISSING_PRIVATE_VOLUME_REGEX = 'REGEX:Create an attachment to a new volume ".*".'
COMPLIANCE_MISSING_SHARED_VOLUME_REGEX = 'REGEX:Create an attachment to an existing volume \{.*\}.'
COMPLIANCE_LUN_TYPE_TO_AUTO_REGEX = "REGEX:Change LUN type of volume attachment id \d* for volume \{.*\} to Auto."
COMPLIANCE_LUN_TYPE_TO_MANUAL_REGEX = "REGEX:Change LUN type of volume attachment id \d* for volume \{.*\} to Manual with LUN value \d*."
COMPLIANCE_LUN_NUMBER_REGEX = 'REGEX:Change LUN of volume attachment id \d* for volume \{.*\} to \d*.'
COMPLIANCE_DISABLE_STORAGE_PATH_REGEX = 'REGEX:Change storage path using connection "\d*" in volume attachment id \d* for volume \{.*\} to enabled.'
COMPLIANCE_ADD_STORAGE_PATH_REGEX = 'REGEX:Add the storage path'
COMPLIANCE_REMOVE_STORAGE_PATH_REGEX = 'REGEX:Remove the storage path'
COMPLIANCE_MISSING_ATAI_MAPPING = 'REGEX:The template volume ".*" is not associated to a volume in the profile. Create an attachment for this volume or associate one of the profile volume attachments to this template volume.'
COMPLIANCE_VOLUME_SIZE = 'REGEX:Attachment id \d* for volume \{.*\} must be at least the capacity of the volume as defined in the server profile template'
COMPLIANCE_VOLUME_PERMANENCE = 'REGEX:does not match the permanent setting in the template.'
COMPLIANCE_VOLUME_DPL = 'REGEX:does not match the data protection level setting in the template.'
COMPLIANCE_SHARED_VOLUME_ADD_ATAI = 'REGEX:The reference to associated template attachment ID [a-z,0-9]{8}-[a-z,0-9]{4}-[a-z,0-9]{4}-[a-z,0-9]{4}-[a-z,0-9]{12} will be added.'

# Profile compliant compliance
spt1_profile1_compliant_compliance = {
    "name": SPT1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
        ]
    }
}
spt2_profile1_compliant_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
        ]
    }
}
spt3_profile1_compliant_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
        ]
    }
}
spt4_profile1_compliant_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
        ]
    }
}
profiles_compliant_compliance = [
    spt1_profile1_compliant_compliance,
    spt2_profile1_compliant_compliance,
    spt3_profile1_compliant_compliance,
    spt4_profile1_compliant_compliance,

]

three_profiles_compliant_compliance = [
    spt2_profile1_compliant_compliance,
    spt3_profile1_compliant_compliance,
    spt4_profile1_compliant_compliance,

]


# Test Sets
# NTS1, create negative SPTs to fail validation
# Bootable volume and non-bootable connection
nts1_negative_spt1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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
nts1_negative_spt2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": "",
                        "firstBootTargetPort": "",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": None,
                        "initiatorName": "",
                        "bootTargetName": "",
                        "bootTargetLun": "",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
        ]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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
            }
        ]
    }
}

# Multiple bootable volumes
nts1_negative_spt3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": "",
                        "firstBootTargetPort": "",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": None,
                        "initiatorName": "",
                        "bootTargetName": "",
                        "bootTargetLun": "",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
        ]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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

            },
            {
                "id": 2,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_2,
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
            }
        ]
    }
}

# Invalid lun=0 for MLPT VSA volume
nts1_negative_spt4 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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

# non-unique LUN number for MLPT VSA volumes
nts1_negative_spt5 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT5_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_2,
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

# Inviad lunType for SLPT VSA volume
nts1_negative_spt6 = {
    "type":
    SERVER_PROFILE_TEMPLATE_TYPE,
    "name":
    NTS1_SPT6_NAME,
    "serverHardwareTypeUri":
    'SHT:' + SHT1,
    "enclosureGroupUri":
    'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType":
    "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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
            }
        ]
    }
}

# Mixed paths for VSA volume, one enabled and the other disabled
nts1_negative_spt7 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT7_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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
            }
        ]
    }
}

# No port configuration
nts1_negative_spt8 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT8_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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
            }
        ]
    }
}

# Attach pre-existing presented private volume
nts1_negative_spt9 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT9_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_PRIV,
            }
        ]
    }
}

# non-unique ATAI
nts1_negative_spt10 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT10_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "1",
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_2,
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
            }
        ]
    }
}

# invalid ATAI
nts1_negative_spt11 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS1_SPT11_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS1_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "-1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS1_VOL_1,
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
            }
        ]
    }
}

nts1_negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Bootable_volume_nonbootable_connection'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_bootable_volumes'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalidate_LUN_MLPT_VSA'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'LUN_not_unique_MLPT_VSA'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_lunType_SLPT_VSA'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Mixed_paths_VSA'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt8.copy(),
        'taskState': 'Error',
        'errorMessage': 'VSA_not_attached_to_network'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt9.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_attach_exist_private_volume'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt10.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_non_unique_ATAI'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': nts1_negative_spt11.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_invalid_ATAI'
    },

]

# NTS2, edit SPT to fail validation
nts2_spt_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# non-bootable connection and bootable volume
nts2_spt_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": True,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# bootable connection and non-bootable volume
nts2_spt_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": "",
                        "firstBootTargetPort": "",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": None,
                        "initiatorName": "",
                        "bootTargetName": "",
                        "bootTargetLun": "",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }

            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# multiple bootable volumes
nts2_spt_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": "",
                    "ipAddress": INITIATOR_IP_1
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": "",
                        "firstBootTargetPort": "",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": None,
                        "initiatorName": "",
                        "bootTargetName": "",
                        "bootTargetLun": "",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": True,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": True,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]

    }
}

# invalid MLPT LUN
nts2_spt_edit4 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# non-unique MLPT LUN
nts2_spt_edit5 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]

    }
}

# invalid SLPT lunType
nts2_spt_edit6 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# mixed paths
nts2_spt_edit7 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# no port configuration
nts2_spt_edit8 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# attach existing priv volume
nts2_spt_edit9 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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

            },
            {
                "associatedTemplateAttachmentId": "4",
                "id": 4,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_PRIV,
            }
        ]
    }
}

# non-unique ATAI
nts2_spt_edit10 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 4,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_4,
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
            }
        ]
    }
}

# invalid ATAI
nts2_spt_edit11 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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

            },
            {
                "associatedTemplateAttachmentId": "-1",
                "id": 4,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_4,
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
            }
        ]
    }
}

# edit existing ATAI
nts2_spt_edit12 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "0",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

# ATAI mismatch storage pool
nts2_spt_edit13 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": NTS2_SPT,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + NTS2_SPT_EG,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_1,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_2,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_NTS2_VOL_3,
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
            }
        ]
    }
}

nts2_spts_create = [
    nts2_spt_create.copy(),
]

nts2_negative_spt_tasks = [
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Bootable_volume_nonbootable_connection'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit2.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_bootable_volumes'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalidate_LUN_MLPT_VSA'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit5.copy(),
        'taskState': 'Error',
        'errorMessage': 'LUN_not_unique_MLPT_VSA'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_lunType_SLPT_VSA'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Mixed_paths_VSA'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit8.copy(),
        'taskState': 'Error',
        'errorMessage': 'VSA_not_attached_to_network'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit9.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_attach_exist_private_volume'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit10.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_non_unique_ATAI'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit11.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_invalid_ATAI'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': nts2_spt_edit12.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_edit_existing_ATAI'
    },
]

# PTS1, Positive, create SPTs and create profiles from SPT. Modify Profiles to cause non-compliance
# PTS1, SPTs
# PTS1 SPT1, SHT1 (BL460c Gen8), shared volumes in 3PAR1 and VSA2, Auto LUN
pts1_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

pts1_spt1_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS1 SPT2, SHT2 (BL460c Gen9), private permanent volume in VSA1 and
# VSA2, Manual LUN
pts1_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

pts1_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

# PTS1 SPT3, SHT3 (BL660c Gen8), private ephemeral volumes in 3Par1 and
# VSA2, Manual LUN and same LUN number
pts1_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

pts1_spt3_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

# PTS1 SPT4, SHT4 (BL660c Gen9), private ephemeral volumes in VSA1 and
# VSA2, Auto LUN
pts1_spt4_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
            "HardDisk"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

pts1_spt4_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings":
    {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

# PTS1, profiles
# PTS1 SPT1 Profile1 on ENC1BAY1 (BL460c Gen8), two shared volumes
pts1_spt1_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
}

pts1_spt1_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS1 SPT1 Profile1 edit1 - LUN type Auto to Manual
pts1_spt1_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]

    }
}

# PTS1 SPT1 Profile1 edit1 - LUN type Auto to Manual
pts1_spt1_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS1 SPT1 Profile1 edit1 - LUN type Auto to Manual
pts1_spt1_profile1_edit1_compliance = {
    "name": SPT1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": [
            COMPLIANCE_LUN_TYPE_TO_AUTO_REGEX,
            COMPLIANCE_LUN_TYPE_TO_AUTO_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS1 SPT1 Profile1 edit4 - Remove one volume
pts1_spt1_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
            }
        ]
    }
}

# PTS1 SPT1 Profile1 edit4 - remove one volume
pts1_spt1_profile1_edit4_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,
            }
        ]
    }
}

# PTS1 SPT1 Profile1 edit4 - remove one volume
pts1_spt1_profile1_edit4_compliance = {
    "name": SPT1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": [
            COMPLIANCE_MISSING_SHARED_VOLUME_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS1 SPT2 Profile1 on ENC1BAY4 (BL460c Gen9), two private permanent volumes
pts1_spt2_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
}

pts1_spt2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit1 - change LUN Number
pts1_spt2_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]

    }
}

# PTS1 SPT2 Profile1 edit1 - change LUN Number
pts1_spt2_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit1 - change LUN Number, disable both storage paths
pts1_spt2_profile1_edit1_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": [
            COMPLIANCE_LUN_NUMBER_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS1 SPT2 Profile1 edit2 - remove ATAI mapping
pts1_spt2_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit2 - Remove ATAI Mapping
pts1_spt2_profile1_edit2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit2 - Remove ATAI Mapping
pts1_spt2_profile1_edit2_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# SPT2 Profile1 edit3 - Add ATAI mapping
pts1_spt2_profile1_edit3 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit3 - Add ATAI Mapping
pts1_spt2_profile1_edit3_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ],
    }
}

# PTS1 SPT2 Profile1 edit4 - Remove one volume
pts1_spt2_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit4 - Remove one volume
pts1_spt2_profile1_edit4_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,
            }
        ]
    }
}

# PTS1 SPT2 Profile1 edit4 - Remove one volume
pts1_spt2_profile1_edit4_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": [
            COMPLIANCE_MISSING_PRIVATE_VOLUME_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS1 SPT2 PROFILE patch2 - after update from template, the missing
# private volume is added back
pts1_spt2_profile1_patch2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
            }
        ]

    }
}

# PTS1 SPT3 Profile1 on ENC1BAY8 (BL660c Gen8)
pts1_spt3_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
}

pts1_spt3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit1 - LUN type Manual to Auto
pts1_spt3_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit1 - LUN type Manual to Auto
pts1_spt3_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit1 - compliance
pts1_spt3_profile1_edit1_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_LUN_TYPE_TO_MANUAL_REGEX,
            COMPLIANCE_LUN_TYPE_TO_MANUAL_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS1 SPT3 Profile1 edit2 - Remove ATAI mapping
pts1_spt3_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit2 - Remove ATAI mapping
pts1_spt3_profile1_edit2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit2 - Remove ATAI Mapping
pts1_spt3_profile1_edit2_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS1 SPT3 Profile1 edit3 - Add ATAI mapping
pts1_spt3_profile1_edit3 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit3 - Add ATAI mapping
pts1_spt3_profile1_edit3_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit4 - Remove one volume
pts1_spt3_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:2',
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts1_spt3_profile1_edit4_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT3 Profile1 edit4 - Remove one volume
pts1_spt3_profile1_edit4_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview":
    {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": [
            COMPLIANCE_MISSING_PRIVATE_VOLUME_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

pts1_spt3_profile1_patch2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode":
    None,
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 3,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 on ENc1Bay7 (BL660c Gen9, UEFI mode)
pts1_spt4_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
}

pts1_spt4_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 edit1 - disable storage paths
pts1_spt4_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": False,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 edit1 - disable storage paths
pts1_spt4_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": False,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts1_spt4_profile1_edit1_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_DISABLE_STORAGE_PATH_REGEX,
            COMPLIANCE_DISABLE_STORAGE_PATH_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS1 SPT4 Profile1 edit2 - Remove ATAI mapping
pts1_spt4_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": None,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 edit2 - Remove ATAI Mapping
pts1_spt4_profile1_edit2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": None,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts1_spt4_profile1_edit2_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates":
        [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS1 SPT4 Profile1 edit3 - Add ATAI mapping
pts1_spt4_profile1_edit3 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 edit3 - Add ATAI Mapping
pts1_spt4_profile1_edit3_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 edit4 - Remove one volume
pts1_spt4_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS1 SPT4 Profile1 edit4 - Remove one volume
pts1_spt4_profile1_edit4_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts1_spt4_profile1_edit4_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates": [
            COMPLIANCE_MISSING_PRIVATE_VOLUME_REGEX],
        "manualUpdates": [
        ]
    }
}

pts1_spt4_profile1_patch2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections":
        [
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
    "boot":
    {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode":
    {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware":
    {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios":
    {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage":
    {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage":
    {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 3,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,
            }
        ]
    }
}

pts1_spts_create = [
    pts1_spt1_create.copy(),
    pts1_spt2_create.copy(),
    pts1_spt3_create.copy(),
    pts1_spt4_create.copy(),
]

pts1_spts_create_expected = [
    pts1_spt1_create_expected,
    pts1_spt2_create_expected,
    pts1_spt3_create_expected,
    pts1_spt4_create_expected,
]

pts1_profiles_create = [
    pts1_spt1_profile1_create.copy(),
    pts1_spt2_profile1_create.copy(),
    pts1_spt3_profile1_create.copy(),
    pts1_spt4_profile1_create.copy(),
]

pts1_profiles_create_expected = [
    pts1_spt1_profile1_create_expected,
    pts1_spt2_profile1_create_expected,
    pts1_spt3_profile1_create_expected,
    pts1_spt4_profile1_create_expected,
]

# PTS1 Profile Edit 1 - Update LUN type, LUN number, disable storage
# paths, remove storage paths
pts1_profiles_edit1 = [
    pts1_spt1_profile1_edit1.copy(),
    pts1_spt2_profile1_edit1.copy(),
    pts1_spt3_profile1_edit1.copy(),
    pts1_spt4_profile1_edit1.copy(),
]

pts1_profiles_edit1_expected = [
    pts1_spt1_profile1_edit1_expected,
    pts1_spt2_profile1_edit1_expected,
    pts1_spt3_profile1_edit1_expected,
    pts1_spt4_profile1_edit1_expected,
]

pts1_profiles_edit1_compliance = [
    pts1_spt1_profile1_edit1_compliance,
    pts1_spt2_profile1_edit1_compliance,
    pts1_spt3_profile1_edit1_compliance,
    pts1_spt4_profile1_edit1_compliance,
]

# PTS1 Profile Edit 2 - Remove ATAI Mapping
pts1_profiles_edit2 = [
    pts1_spt2_profile1_edit2.copy(),
    pts1_spt3_profile1_edit2.copy(),
    pts1_spt4_profile1_edit2.copy(),
]

pts1_profiles_edit2_expected = [
    pts1_spt2_profile1_edit2_expected,
    pts1_spt3_profile1_edit2_expected,
    pts1_spt4_profile1_edit2_expected,
]

pts1_profiles_edit2_compliance = [
    pts1_spt2_profile1_edit2_compliance,
    pts1_spt3_profile1_edit2_compliance,
    pts1_spt4_profile1_edit2_compliance,
]

# PTS1 Profile Edit 3 - Add ATAI Mapping (Manual updates to be compliant)
pts1_profiles_edit3 = [
    pts1_spt2_profile1_edit3.copy(),
    pts1_spt3_profile1_edit3.copy(),
    pts1_spt4_profile1_edit3.copy(),
]

pts1_profiles_edit3_expected = [
    pts1_spt2_profile1_edit3_expected,
    pts1_spt3_profile1_edit3_expected,
    pts1_spt4_profile1_edit3_expected,
]

# PTS1 Profile Edit 4 - Remove one volume
pts1_profiles_edit4 = [
    pts1_spt1_profile1_edit4.copy(),
    pts1_spt2_profile1_edit4.copy(),
    pts1_spt3_profile1_edit4.copy(),
    pts1_spt4_profile1_edit4.copy(),
]

pts1_profiles_edit4_expected = [
    pts1_spt1_profile1_edit4_expected,
    pts1_spt2_profile1_edit4_expected,
    pts1_spt3_profile1_edit4_expected,
    pts1_spt4_profile1_edit4_expected,
]

pts1_profiles_edit4_compliance = [
    pts1_spt1_profile1_edit4_compliance,
    pts1_spt2_profile1_edit4_compliance,
    pts1_spt3_profile1_edit4_compliance,
    pts1_spt4_profile1_edit4_compliance,
]

# PTS1 Profiles Patch - Update from template
pts1_profiles_patch = pts1_profiles_create_expected

pts1_profiles_patch_expected = pts1_profiles_create_expected

# PTS1 Profiles Patch missing volumes - Update from template after remove
# one volume.
pts1_profiles_patch2_expected = [
    pts1_spt1_profile1_create_expected,
    pts1_spt2_profile1_patch2_expected,
    pts1_spt3_profile1_patch2_expected,
    pts1_spt4_profile1_patch2_expected,
]

pts1_new_ephemeral_volumes = [
    {
        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,

    },
    {
        "name": VOLUME_SPT3_VSA2_EPH_PRIV,

    },
    {
        "name": VOLUME_SPT4_VSA1_EPH_PRIV,

    },
    {
        "name": VOLUME_SPT4_VSA2_EPH_PRIV,

    },
]

# PTS2, Positive, create SPTs and create profiles from SPT. Modify SPT to cause non-compliance
# PTS2, SPTs
# PTS2 SPT1, SHT1 (BL460c Gen8), shared volumes in 3PAR1 and VSA2, Auto LUN
pts2_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

pts2_spt1_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS2 SPT1 edit1 - LUN Type Auto to Manual
pts2_spt1_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS2 SPT1 edit1 - update LUN Type Auto to Manual
pts2_spt1_edit1_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS2 SPT1 edit2 - Remove one volume
pts2_spt1_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS2 SPT1 edit3 - Add volume back
pts2_spt1_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}


# PTS2 SPT1 edit2 - remove one volume
pts2_spt1_edit2_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS2 SPT2, SHT2 (BL460c Gen9), private permanent volume in VSA1 and
# VSA2, Manual LUN
pts2_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

pts2_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

# PTS2 SPT2 edit 1 - Update LUN number
pts2_spt2_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

pts2_spt2_edit1_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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


# PTS2 SPT2 edit 2 - remove one volume
pts2_spt2_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

pts2_spt2_edit2_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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


# PTS2 SPT2 edit 3 - Add volume Back
pts2_spt2_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

# PTS2 SPT3, SHT3 (BL660c Gen8), private ephemeral volumes in 3Par1 and
# VSA2, Manual LUN and same LUN number
pts2_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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


pts2_spt3_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

# PTS2 SPT3 edit 1 - LUN type Manual to Auto
pts2_spt3_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

pts2_spt3_edit1_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

# PTS2 SPT3 edit 2 - remove one volume
pts2_spt3_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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
            }
        ]
    }
}

pts2_spt3_edit2_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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
            }
        ]
    }
}


# PTS2 SPT3 edit 3 - Add volume back
pts2_spt3_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": None,
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

# PTS2 SPT4, SHT4 (BL660c Gen9), private ephemeral volumes in VSA1 and
# VSA2, Auto LUN
pts2_spt4_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
            "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None",

                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,

                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }
        ]
    }
}

pts2_spt4_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

# PTS2 SPT4 edit1 - remove storage paths
pts2_spt4_edit1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

pts2_spt4_edit1_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

# PTS2 SPT4 edit2 - remove one volume
pts2_spt4_edit2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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
            }
        ]
    }
}

pts2_spt4_edit2_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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
            }
        ]
    }
}

# PTS2 SPT4 edit3 - Add volume back
pts2_spt4_edit3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": None,
                "id": 2,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

# PTS2 2 Profiles
# PTS2 SPT1 Profile1 on ENC1BAY1 (BL460c Gen8), two shared volumes
pts2_spt1_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
}

pts2_spt1_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS2 SPT1 edit1 - update LUN type, disable one storage path
# PTS2 SPT1 Profile 1 - compliance after SPT1 edit1
pts2_spt1_profile1_edit1_compliance = {
    "name": SPT1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_LUN_TYPE_TO_MANUAL_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS2 SPT1 edit1 - update LUN Type Auto to Manual
# PTS2 SPT1 Profile1 patch1
pts2_spt1_profile1_patch1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

pts2_spt1_profile1_edit3_compliance = {
    "name": SPT1_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_SHARED_VOLUME_ADD_ATAI,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS2 SPT2 Profile1 on ENC1BAY4 (BL460c Gen9), two private permanent volumes
pts2_spt2_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
}

pts2_spt2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS2 SPT2 edit1 - update LUN number
# PTS2 SPT2 Profile 1 - compliance after SPT2 edit1
pts2_spt2_profile1_edit1_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_LUN_NUMBER_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS2 SPT2 edit1 - update LUN number
# PTS2 SPT2 Profile1 patch1
pts2_spt2_profile1_patch1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]

    }
}

# PTS2 SPT2 edit3 - Add the Volume Back
# PTS2 SPT2 Profile - compliance after SPT2 edit3
pts2_spt2_profile1_edit3_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS2 SPT2 Profile1 Edit4 - Associate ATAI
pts2_spt2_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS2 SPT3 Profile1 on ENC1BAY8 (BL660c Gen8)
pts2_spt3_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
}

pts2_spt3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS2 SPT3 edit1 - LUN type Manual to Auto
pts2_spt3_profile1_edit1_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_LUN_TYPE_TO_AUTO_REGEX,
            COMPLIANCE_LUN_TYPE_TO_AUTO_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS2 SPT3 edit1 - LUN Type Manual to Auto
# PTS2 SPT3 profile1 patch1
pts2_spt3_profile1_patch1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS2 SPT3 edit3 - Add the volume back
# PTS2 SPT3 Profile1 - compliance after SPT3 edit3
pts2_spt3_profile1_edit3_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS2 SPT3 Profile1 - Associate ATAI
pts2_spt3_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS2 SPT4 Profile1 on Enc1Bay7 (BL660c Gen9, UEFI mode)
pts2_spt4_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
}

pts2_spt4_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS2 SPT4 edit1 - remove storage paths
# PTS2 SPT2 profile - compliance after SPT4 edit1
pts2_spt4_profile1_edit1_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": True,
        "automaticUpdates":
        [
            COMPLIANCE_REMOVE_STORAGE_PATH_REGEX,
        ],
        "manualUpdates": [
        ]
    }
}

# PTS2 SPT4 edit1 - remove storage paths
# PTS2 SPT4 Profile1 patch1
pts2_spt4_profile1_patch1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS2 SPT4 edit3 - Add the volume back
# PTS2 SPT4 Profile1 - compliance after SPT4 edit3
pts2_spt4_profile1_edit3_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates":
        [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING]
    }
}

# PTS2 SPT4 Profile1 patch2
pts2_spt4_profile1_patch2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": ATAI_REGEX,
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": None,
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS2 SPT4 Profile1 Edit4 - associate ATAT
pts2_spt4_profile1_edit4 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "SPTVAID:1",
                "id": 1,
                "isBootVolume": False,
                "lun": 0,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "SPTVAID:2",
                "id": 2,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_SPT4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts2_spts_create = [
    pts2_spt1_create.copy(),
    pts2_spt2_create.copy(),
    pts2_spt3_create.copy(),
    pts2_spt4_create.copy(),
]

pts2_spts_create_expected = [
    pts2_spt1_create_expected,
    pts2_spt2_create_expected,
    pts2_spt3_create_expected,
    pts2_spt4_create_expected,
]

pts2_spts_edit1 = [
    pts2_spt1_edit1.copy(),
    pts2_spt2_edit1.copy(),
    pts2_spt3_edit1.copy(),
    pts2_spt4_edit1.copy(),
]

pts2_spts_edit1_expected = [
    pts2_spt1_edit1_expected,
    pts2_spt2_edit1_expected,
    pts2_spt3_edit1_expected,
    pts2_spt4_edit1_expected,
]

pts2_spts_edit2 = [
    pts2_spt1_edit2.copy(),
    pts2_spt2_edit2.copy(),
    pts2_spt3_edit2.copy(),
    pts2_spt4_edit2.copy(),
]

pts2_spts_edit2_expected = [
    pts2_spt1_edit2_expected,
    pts2_spt2_edit2_expected,
    pts2_spt3_edit2_expected,
    pts2_spt4_edit2_expected,
]

pts2_spts_edit3 = [
    pts2_spt1_edit3.copy(),
    pts2_spt2_edit3.copy(),
    pts2_spt3_edit3.copy(),
    pts2_spt4_edit3.copy(),
]

pts2_spts_edit3_expected = pts2_spts_edit1_expected

pts2_profiles_create = [
    pts2_spt1_profile1_create.copy(),
    pts2_spt2_profile1_create.copy(),
    pts2_spt3_profile1_create.copy(),
    pts2_spt4_profile1_create.copy(),
]

pts2_profiles_create_expected = [
    pts2_spt1_profile1_create_expected,
    pts2_spt2_profile1_create_expected,
    pts2_spt3_profile1_create_expected,
    pts2_spt4_profile1_create_expected,
]

pts2_profiles_edit1_compliance = [
    pts2_spt1_profile1_edit1_compliance,
    pts2_spt2_profile1_edit1_compliance,
    pts2_spt3_profile1_edit1_compliance,
    pts2_spt4_profile1_edit1_compliance.copy(),
]

pts2_profiles_patch1_expected = [
    pts2_spt1_profile1_patch1_expected,
    pts2_spt2_profile1_patch1_expected,
    pts2_spt3_profile1_patch1_expected,
    pts2_spt4_profile1_patch1_expected,
]

pts2_profiles_edit2_expected = pts2_profiles_patch1_expected

pts2_profiles_edit3_compliance = [
    pts2_spt2_profile1_edit3_compliance,
    pts2_spt3_profile1_edit3_compliance,
    pts2_spt4_profile1_edit3_compliance,
]

pts2_profiles_edit3_expected = pts2_profiles_patch1_expected

pts2_profiles_edit4 = [
    pts2_spt2_profile1_edit4.copy(),
    pts2_spt3_profile1_edit4.copy(),
    pts2_spt4_profile1_edit4.copy(),
]

pts2_profiles_edit4_expected = [
    pts2_spt2_profile1_patch1_expected,
    pts2_spt3_profile1_patch1_expected,
    pts2_spt4_profile1_patch1_expected,
]

pts2_profiles_patch = pts2_profiles_create

pts2_new_permanent_volumes = [
    {
        "name": VOLUME_SPT2_VSA1_PERM_PRIV,

    },
    {
        "name": VOLUME_SPT2_VSA2_PERM_PRIV,

    },
]

# PTS3, Postitive, Create Profiles and SPTs, associate Profiles with SPTs
# PTS3 SPT1, SHT1 (BL460c Gen8), two shared volumes in 3PAR1 and VSA2, Auto LUN
pts3_spt1_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

pts3_spt1_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT1_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT1,
    "enclosureGroupUri": 'EG:' + SPT1_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS3 SPT2, SHT2 (BL460c Gen9), two private permanent volume in VSA1 and
# VSA2, Manual LUN
pts3_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

pts3_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_PERM_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
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

# PTS3 SPT3, SHT3 (BL660c Gen8), private ephemeral volumes in 3Par1 and
# VSA2, Manual LUN and same LUN number
pts3_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

pts3_spt3_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

# PTS3 SPT4, SHT4 (BL660c Gen9), private ephemeral volumes in VSA1 and
# VSA2, Auto LUN
pts3_spt4_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
            "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

pts3_spt4_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

# PTS3 Profiles
# PTS3 SPT1 Profile1 on ENC1BAY1 (BL460c Gen8), three shared volumes
pts3_spt1_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": None,
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
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",

                    },
                ],
                "volume": None,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

pts3_spt1_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS3 SPT1 Profile1 edit1 - associate with SPT
pts3_spt1_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
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
                        "targetSelector": "Auto",

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

pts3_spt1_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT1_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT1_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT1_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT1_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT1_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT1_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "networkUri": "ETH:network-tunnel"
            },
            {
                "id": 6,
                "name": "",
                "state": "Deployed",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel"}
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_3PAR1_SHARED,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_VSA2_SHARED,
            }
        ]
    }
}

# PTS3 SPT2 Profile1 on ENC1BAY4 (BL460c Gen9), two private ephemeral volumes
pts3_spt2_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
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

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
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
            }
        ]
    }

}

pts3_spt2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 11,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS3 SPT2 Profile1 edit1 - associate with SPT
pts3_spt2_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

pts3_spt2_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 11,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS3 SPT2 Profile1 edit1 - associate w SPT
pts3_spt2_profile1_edit1_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS3 SPT4 Profile1 edit2 - map ATAI
pts3_spt2_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

pts3_spt2_profile1_edit2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS3 SPT3 Profile1 on ENC1BAY8 (BL660c Gen8)
pts3_spt3_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE3_3PAR1_EPH_PRIV,
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

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE3_VSA2_EPH_PRIV,
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

pts3_spt3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS3 SPT3 Profile1 edit1 - associate with SPT
pts3_spt3_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts3_spt3_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS3 SPT4 Profile1 on Enc1Bay7 (BL660c Gen9, UEFI mode), four private volumes
pts3_spt4_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 11,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE4_VSA1_EPH_PRIV,
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

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE4_VSA2_EPH_PRIV,
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

pts3_spt4_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 11,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA1_EPH_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS3 SPT4 Profile1 edit1 - associate SPT
pts3_spt4_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA1_EPH_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts3_spt4_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": None,
                "id": 11,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": None,
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS3 SPT4 Profile1 edit1 - associate w SPT
pts3_spt4_profile1_edit1_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS3 SPT4 Profile1 edit2 - map ATAI
pts3_spt4_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts3_spt4_profile1_edit2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "11",
                "id": 11,
                "isBootVolume": False,
                "lun": 0,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA1_EPH_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lunType": "Auto",
                "state": "Attached",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts3_spts_create = [
    pts3_spt1_create.copy(),
    pts3_spt2_create.copy(),
    pts3_spt3_create.copy(),
    pts3_spt4_create.copy(),
]

pts3_spts_create_expected = [
    pts3_spt1_create_expected,
    pts3_spt2_create_expected,
    pts3_spt3_create_expected,
    pts3_spt4_create_expected,
]

pts3_profiles_create = [
    pts3_spt1_profile1_create.copy(),
    pts3_spt2_profile1_create.copy(),
    pts3_spt3_profile1_create.copy(),
    pts3_spt4_profile1_create.copy(),
]

pts3_profiles_create_expected = [
    pts3_spt1_profile1_create_expected,
    pts3_spt2_profile1_create_expected,
    pts3_spt3_profile1_create_expected,
    pts3_spt4_profile1_create_expected,
]

pts3_profiles_edit1 = [
    pts3_spt1_profile1_edit1.copy(),
    pts3_spt2_profile1_edit1.copy(),
    pts3_spt3_profile1_edit1.copy(),
    pts3_spt4_profile1_edit1.copy(),
]

pts3_profiles_edit1_expected = [
    pts3_spt1_profile1_edit1_expected,
    pts3_spt2_profile1_edit1_expected,
    pts3_spt3_profile1_edit1_expected,
    pts3_spt4_profile1_edit1_expected,
]

pts3_profiles_edit1_compliance = [
    spt1_profile1_compliant_compliance,
    pts3_spt2_profile1_edit1_compliance,
    spt3_profile1_compliant_compliance,
    pts3_spt4_profile1_edit1_compliance,
]

pts3_profiles_edit2 = [
    pts3_spt2_profile1_edit2.copy(),
    pts3_spt4_profile1_edit2.copy(),
]

pts3_profiles_edit2_expected = [
    pts3_spt2_profile1_edit2_expected,
    pts3_spt4_profile1_edit2_expected,
]

pts3_new_permanent_volumes = [
    {
        "name": VOLUME_PROFILE2_VSA1_PERM_PRIV
    },
    {
        "name": VOLUME_PROFILE2_VSA2_PERM_PRIV
    },
]

# PTS4, Postitive, Create Profiles and SPTs, associate Profiles with SPTs
# PTS4 SPT2, SHT2 (BL460c Gen9), two private permanent volume in VSA1 and
# VSA2, Manual LUN
pts4_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 2147483648,
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

pts4_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT2_VSA2_PERM_PRIV,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 2147483648,
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

# PTS4 SPT3, SHT3 (BL660c Gen8), private ephemeral volumes in 3Par1 and
# VSA2, Manual LUN and same LUN number
pts4_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

pts4_spt3_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

pts4_spt3_edit = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV,
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

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_SPT3_VSA2_EPH_PRIV,
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

# PTS4 SPT4, SHT4 (BL660c Gen9), private ephemeral volumes in VSA1 and
# VSA2, Manual LUN
pts4_spt4_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
            "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

pts4_spt4_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV,
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

# PTS4 Profiles
# PTS4 SPT2 Profile1 on ENC1BAY4 (BL460c Gen9), two private ephemeral volumes
pts4_spt2_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
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
            }
        ]
    }

}

pts4_spt2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS4 SPT2 Profile1 edit1 - associate with SPT
pts4_spt2_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

pts4_spt2_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS4 SPT2 Profile1 edit1 - associate w SPT
pts4_spt2_profile1_edit1_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_VOLUME_SIZE,
        ]
    }
}

# PTS4 SPT3 Profile1 on ENC1BAY8 (BL660c Gen8)
pts4_spt3_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_PROFILE3_3PAR1_PERM_PRIV,
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

            },
            {
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": VOLUME_PROFILE3_VSA2_PERM_PRIV,
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

pts4_spt3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_PERM_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS4 SPT3 Profile1 edit1 - associate with SPT
pts4_spt3_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_PERM_PRIV,

            },
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_VSA2_PERM_PRIV,
            }
        ]
    }
}

pts4_spt3_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_PERM_PRIV,

            },
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_VSA2_PERM_PRIV,
            }
        ]
    }
}

# PTS4 SPT3 Profile1 edit1 - associate w SPT
pts4_spt3_profile1_edit1_compliance = {
    "name": SPT3_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_VOLUME_PERMANENCE,
            COMPLIANCE_VOLUME_PERMANENCE,
        ]
    }
}

# PTS4 SPT4 Profile1 on Enc1Bay7 (BL660c Gen9, UEFI mode), four private volumes
pts4_spt4_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 21,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE4_VSA2_EPH_PRIV,
                        "description": "",
                        "storagePool": "SPOOL:" + STOREVIRTUAL2_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way"

                    },
                    "templateUri": "ROOT:" + STOREVIRTUAL2_POOL,

                },
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": None,
            }
        ]
    }
}

pts4_spt4_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS4 SPT4 Profile1 edit1 - associate SPT
pts4_spt4_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

pts4_spt4_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "21",
                "id": 21,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV,
            }
        ]
    }
}

# PTS4 SPT4 Profile1 edit1 - associate w SPT
pts4_spt4_profile1_edit1_compliance = {
    "name": SPT4_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_VOLUME_DPL,
        ]
    }
}

pts4_spts_create = [
    pts4_spt2_create.copy(),
    pts4_spt3_create.copy(),
    pts4_spt4_create.copy(),
]

pts4_spts_create_expected = [
    pts4_spt2_create_expected,
    pts4_spt3_create_expected,
    pts4_spt4_create_expected,
]

pts4_profiles_create = [
    pts4_spt2_profile1_create.copy(),
    pts4_spt3_profile1_create.copy(),
    pts4_spt4_profile1_create.copy(),
]

pts4_profiles_create_expected = [
    pts4_spt2_profile1_create_expected,
    pts4_spt3_profile1_create_expected,
    pts4_spt4_profile1_create_expected,
]

pts4_profiles_edit1 = [
    pts4_spt2_profile1_edit1.copy(),
    pts4_spt3_profile1_edit1.copy(),
    pts4_spt4_profile1_edit1.copy(),
]

pts4_profiles_edit1_expected = [
    pts4_spt2_profile1_edit1_expected,
    pts4_spt3_profile1_edit1_expected,
    pts4_spt4_profile1_edit1_expected,
]

pts4_profiles_edit1_compliance = [
    pts4_spt2_profile1_edit1_compliance,
    pts4_spt3_profile1_edit1_compliance,
    pts4_spt4_profile1_edit1_compliance,
]

pts4_volumes_edit = [
    {
        'name': VOLUME_PROFILE2_VSA2_PERM_PRIV,
        "provisionedCapacity": "2147483648"
    },
    {
        'name': VOLUME_PROFILE4_VSA2_EPH_PRIV,
        "deviceSpecificAttributes": {
            "dataProtectionLevel": "NetworkRaid0None"}
    },
]

pts4_spts_edit = [
    pts4_spt3_edit.copy()
]

pts4_new_permanent_volumes = [
    {
        "name": VOLUME_PROFILE2_VSA2_PERM_PRIV
    },
    {
        "name": VOLUME_PROFILE3_3PAR1_PERM_PRIV
    },
    {
        "name": VOLUME_PROFILE3_VSA2_PERM_PRIV
    },
]

# PTS5, Postitive, Create Profiles and SPTs, associate Profiles with SPTs
# PTS5 SPT2, SHT2 (BL460c Gen9), three private ephemeral VSA1 volumes
pts5_spt2_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_EPH_PRIV1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_EPH_PRIV2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_EPH_PRIV3,
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
            }
        ]
    }
}

pts5_spt2_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT2_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT2,
    "enclosureGroupUri": 'EG:' + SPT2_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_EPH_PRIV1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_EPH_PRIV2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT2_VSA1_EPH_PRIV3,
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
            }
        ]
    }
}

# PTS5 SPT3, SHT3 (BL660c Gen8), three private ephemeral StoreServ volumes
pts5_spt3_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV3,
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
            }
        ]
    }
}

pts5_spt3_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT3_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT3,
    "enclosureGroupUri": 'EG:' + SPT3_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT3_3PAR1_EPH_PRIV3,
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
            }
        ]
    }
}

# PTS5 SPT4, SHT4 (BL660c Gen9), three private ephemeral VSA2 volumes
pts5_spt4_create = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 3,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 4,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                }
            },
            {
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
                "ipv4": {
                }
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
            "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV3,
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

pts5_spt4_create_expected = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "name": SPT4_NAME,
    "serverHardwareTypeUri": 'SHT:' + SHT4,
    "enclosureGroupUri": 'EG:' + SPT4_EG,
    "iscsiInitiatorNameType": "UserDefined",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ],
        "manageConnections": True

    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,

    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV1,
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

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV2,
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

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_SPT4_VSA2_EPH_PRIV3,
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

# PTS5 Profiles
# PTS5 SPT2 Profile1 on ENC1BAY4 (BL460c Gen9), three private ephemeral
# VSA1 volumes
pts5_spt2_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE2_VSA1_EPH_PRIV1,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE2_VSA1_EPH_PRIV2,
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

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE2_VSA1_EPH_PRIV3,
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
            }
        ]
    }

}

pts5_spt2_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV3,
            }
        ]
    }
}

# PTS5 SPT2 Profile1 edit1 - associate with SPT
pts5_spt2_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV3,
            }
        ]
    }
}

pts5_spt2_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV3,
            }
        ]
    }
}

# PTS5 SPT2 Profile1 edit1 - associate w SPT
pts5_spt2_profile1_edit1_compliance = {
    "name": SPT2_PROFILE1_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": None,
        "automaticUpdates": [
        ],
        "manualUpdates": [
            COMPLIANCE_MISSING_ATAI_MAPPING,
            COMPLIANCE_MISSING_ATAI_MAPPING,
            COMPLIANCE_MISSING_ATAI_MAPPING,
        ]
    }
}

# PTS5 SPT2 Profile1 edit2 - map ATAI
pts5_spt2_profile1_edit2 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV1,

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV2,

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 3,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV3,
            }
        ]
    }
}

pts5_spt2_profile1_edit2_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT2_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT2_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT2_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT2_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT2_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT2_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "USB",
            "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV1,

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV2,

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 4,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE2_VSA1_EPH_PRIV3,
            }
        ]
    }
}

# PTS5 SPT3 Profile1 on ENC1BAY8 (BL660c Gen8)
pts5_spt3_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE3_3PAR1_EPH_PRIV1,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE3_3PAR1_EPH_PRIV2,
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

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE3_3PAR1_EPH_PRIV3,
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
            }
        ]
    }
}

pts5_spt3_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV3,
            }
        ]
    }
}

# PTS5 SPT3 Profile1 edit1 - associate with SPT
pts5_spt3_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Mezz 1:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
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
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV3,
            }
        ]
    }
}

pts5_spt3_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT3_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT3_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT3_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT3_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT3_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT3_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk",
            "CD",
            "Floppy",
            "USB",
            "PXE"]
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV1,

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV2,

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
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

                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE3_3PAR1_EPH_PRIV3,
            }
        ]
    }
}

# PTS5 SPT4 Profile1 on Enc1Bay7 (BL660c Gen9, UEFI mode),
pts5_spt4_profile1_create = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
                "lun": 1,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE4_VSA2_EPH_PRIV1,
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

            },
            {
                "id": 2,
                "isBootVolume": False,
                "lun": 2,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE4_VSA2_EPH_PRIV2,
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

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                        ]

                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": VOLUME_PROFILE4_VSA2_EPH_PRIV3,
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

pts5_spt4_profile1_create_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV3,
            }
        ]
    }
}

# PTS5 SPT4 Profile1 edit1 - associate SPT
pts5_spt4_profile1_edit1 = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
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
                "id": 5,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",

            },
            {
                "id": 6,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Flb 2:2-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-tunnel",
            }
        ]
    },
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV1,

            },
            {
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV2,

            },
            {
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
                "lunType": "Manual",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 5,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV3,
            }
        ]
    }
}

pts5_spt4_profile1_edit1_expected = {
    "type": SERVER_PROFILE_TYPE,
    "name": SPT4_PROFILE1_NAME,
    "description": None,
    "serverHardwareUri": 'SH:' + SPT4_PROFILE1_SERVER,
    "enclosureGroupUri": 'EG:' + SPT4_PROFILE1_EG,
    "enclosureUri": 'ENC:' + SPT4_PROFILE1_ENC,
    "serverProfileTemplateUri": "SPT:" + SPT4_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "iscsiInitiatorName": SPT4_PROFILE1_IQN,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "affinity": "Bay",
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
    "boot": {
        "manageBoot": False,
        "order": [
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]
    },
    "sanStorage": {
        "hostOSType": "VMware (ESXi)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": "1",
                "id": 1,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV1,

            },
            {
                "associatedTemplateAttachmentId": "2",
                "id": 2,
                "isBootVolume": False,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV2,

            },
            {
                "associatedTemplateAttachmentId": "3",
                "id": 3,
                "isBootVolume": False,
                "lun": 3,
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
                                "tcpPort": "3260"}]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 6,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL2_VIP,
                                "tcpPort": "3260"}]
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL2_NAME,
                "volumeUri": "SVOL:" + VOLUME_PROFILE4_VSA2_EPH_PRIV3,
            }
        ]
    }
}


pts5_spts_create = [
    pts5_spt2_create.copy(),
    pts5_spt3_create.copy(),
    pts5_spt4_create.copy(),
]

pts5_spts_create_expected = [
    pts5_spt2_create_expected,
    pts5_spt3_create_expected,
    pts5_spt4_create_expected,
]

pts5_profiles_create = [
    pts5_spt2_profile1_create.copy(),
    pts5_spt3_profile1_create.copy(),
    pts5_spt4_profile1_create.copy(),
]

pts5_profiles_create_expected = [
    pts5_spt2_profile1_create_expected,
    pts5_spt3_profile1_create_expected,
    pts5_spt4_profile1_create_expected,
]

pts5_profiles_edit1 = [
    pts5_spt2_profile1_edit1.copy(),
    pts5_spt3_profile1_edit1.copy(),
    pts5_spt4_profile1_edit1.copy(),
]

pts5_profiles_edit1_expected = [
    pts5_spt2_profile1_edit1_expected,
    pts5_spt3_profile1_edit1_expected,
    pts5_spt4_profile1_edit1_expected,
]

pts5_profiles_edit1_compliance = [
    pts5_spt2_profile1_edit1_compliance,
    spt3_profile1_compliant_compliance,
    spt4_profile1_compliant_compliance,
]

pts5_profiles_edit2 = [
    pts5_spt2_profile1_edit2.copy(),
]

pts5_profiles_edit2_expected = [
    pts5_spt2_profile1_edit2_expected,
]
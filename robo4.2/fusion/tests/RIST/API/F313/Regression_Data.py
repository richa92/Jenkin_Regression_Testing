admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# EM defaults
EM_NI = 'eth0'             # Default primary NIC.
EM_LOGIN = 'root'             # EM SSH Username
# Fusion defaults

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
# FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC
# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'
# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
# Server Hardware
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

# VSA storages
VSA_cluster = 'VSA_Cluster_173-2'
VSA_cluster2 = 'VSA84_Storage_Pool '
volumeStoragePoolUri1 = "StoragePoolV2:" + VSA_cluster
volumeStorageSystemUri1 = "StorageSystemV3:" + VSA_cluster
volumeStoragePoolUri2 = "StoragePoolV2:" + VSA_cluster2
volumeStorageSystemUri2 = "StorageSystemV3:" + VSA_cluster2


# F313/F1188 VARIBALES
# SAN Manager and managed SANs
BNA_IP = '16.125.65.9'
san_managers = [
    {'connectionInfo': [
        {'name': 'Type', 'value': 'Brocade Network Advisor'},
        {'name': 'Host', 'value': BNA_IP},
        {'name': 'Port', 'value': 5989},
        {'name': 'Username', 'value': 'Administrator'},
        {'name': 'Password', 'value': 'password'},
        {'name': 'UseSsl', 'value': True}]
     },
]
FA_SAN_A = 'wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'
FA_SAN_B = 'wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'

# StoreServ
STORESERV1_NAME = 'wpst3par-7200-7-srv'
STORESERV1_HOSTNAME = 'wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net'
STORESERV1_POOL1 = 'FVT_Tbird_reg1_r1'
STORESERV1_POOL2 = 'FVT_Tbird_reg1_r5'
STORESERV1_POOL3 = 'FVT_Tbird_reg1_r6'

storage_pools = [
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL1, "isManaged": True, },
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL2, "isManaged": True, },
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL3, "isManaged": True, },
]
# StoreVirtual
STOREVIRTUAL1_NAME = 'VSA_Cluster_173-2'
STOREVIRTUAL1_HOSTNAME = '16.71.149.173'
STOREVIRTUAL1_VIP = '192.168.21.71'
STOREVIRTUAL1_POOL = 'VSA_Cluster_173-2'
STOREVIRTUAL2_NAME = 'VSA84_Storage_Pool'
STOREVIRTUAL2_HOSTNAME = '16.71.151.84'
STOREVIRTUAL2_VIP = '16.71.151.84'
STOREVIRTUAL2_POOL = 'VSA84_Storage_Pool'


storage_systems = [
    {'type': 'StorageSystemV4', 'name': STORESERV1_NAME, 'family': 'StoreServ',
     "hostname": STORESERV1_HOSTNAME, 'credentials': {'username': 'fusionadm', 'password': 'hpvse1'},
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
         "managedDomain": "Tbird_Regression_Domain",
     },
     },
    {'type': 'StorageSystemV4', 'name': STOREVIRTUAL1_NAME, "family": "StoreVirtual",
     "hostname": STOREVIRTUAL1_HOSTNAME, "credentials": {"username": "admin", "password": 'admin'},
     "ports": [{
         "name": STOREVIRTUAL1_VIP,
         "expectedNetworkUri": "ETH:network-untagged",
         "expectedNetworkName": "network-untagged",
         "mode": "Managed",
     }, ],
     },
    {'type': 'StorageSystemV4', 'name': STOREVIRTUAL2_NAME, "family": "StoreVirtual",
     "hostname": STOREVIRTUAL2_HOSTNAME, "credentials": {"username": "admin", "password": 'admin'},
     "ports": [{
         "name": STOREVIRTUAL2_VIP,
         "expectedNetworkUri": "ETH:network-tunnel",
                               "expectedNetworkName": "network-tunnel",
                               "mode": "Managed",
     }, ],
     }, ]

slpt_regex = 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:'
mlpt_regex = 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:'

existing_volumes_mlpt = [{"name": "", "deviceVolumeName": "f313-exist-mlpt-shared1", "description": "", "storageSystemUri": STOREVIRTUAL2_NAME, "isShareable": True},
                         {"name": "", "deviceVolumeName": "f313-exist-mlpt-shared2", "description": "", "storageSystemUri": STOREVIRTUAL2_NAME, "isShareable": True},
                         {"name": "", "deviceVolumeName": "f313-exist-mlpt-private1", "description": "", "storageSystemUri": STOREVIRTUAL2_NAME, "isShareable": False},
                         {"name": "", "deviceVolumeName": "f313-exist-mlpt-private2", "description": "", "storageSystemUri": STOREVIRTUAL2_NAME, "isShareable": False}]
existing_volumes_slpt = [{"name": "", "deviceVolumeName": "f313-exist-slpt-shared1", "description": "", "storageSystemUri": STOREVIRTUAL1_NAME, "isShareable": True},
                         {"name": "", "deviceVolumeName": "f313-exist-slpt-shared2", "description": "", "storageSystemUri": STOREVIRTUAL1_NAME, "isShareable": True},
                         {"name": "", "deviceVolumeName": "f313-exist-slpt-private1", "description": "", "storageSystemUri": STOREVIRTUAL1_NAME, "isShareable": False},
                         {"name": "", "deviceVolumeName": "f313-exist-slpt-private1", "description": "", "storageSystemUri": STOREVIRTUAL1_NAME, "isShareable": False}]


NAME_PREFIX = 'Tbird-reg-'
# Storage volumes
VOLUME_NAME_PREFIX = NAME_PREFIX

VOLUME_3PAR_PRIV1 = VOLUME_NAME_PREFIX + '-3par-priv1'
VOLUME_3PAR_PRIV2 = VOLUME_NAME_PREFIX + '-3par-priv2'
VOLUME_3PAR_PRIV3 = VOLUME_NAME_PREFIX + '-3par-priv3'
VOLUME_3PAR_PRIV4 = VOLUME_NAME_PREFIX + '-3par-priv4'
VOLUME_3PAR_PRIV5 = VOLUME_NAME_PREFIX + '-3par-priv5'
VOLUME_3PAR_PRIV6 = VOLUME_NAME_PREFIX + '-3par-priv6'
VOLUME_3PAR_PRIV7 = VOLUME_NAME_PREFIX + '-3par-priv7'
VOLUME_3PAR_PRIV8 = VOLUME_NAME_PREFIX + '-3par-priv8'

VOLUME_3PAR_SHARED1 = VOLUME_NAME_PREFIX + '3par-shared1'
VOLUME_3PAR_SHARED2 = VOLUME_NAME_PREFIX + '3par-shared2'
VOLUME_3PAR_SHARED3 = VOLUME_NAME_PREFIX + '3par-shared3'
VOLUME_3PAR_SHARED4 = VOLUME_NAME_PREFIX + '3par-shared4'
VOLUME_3PAR_SHARED5 = VOLUME_NAME_PREFIX + '3par-shared5'
VOLUME_3PAR_SHARED6 = VOLUME_NAME_PREFIX + '3par-shared6'
VOLUME_3PAR_SHARED7 = VOLUME_NAME_PREFIX + '3par-shared7'
VOLUME_3PAR_SHARED8 = VOLUME_NAME_PREFIX + '3par-shared8'


storage_volumes = [{"properties": {"name": VOLUME_3PAR_PRIV1, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": '3par1-pool1-private', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_PRIV2, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_PRIV3, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": '3par1-pool1-private', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_PRIV4, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    }, {"properties": {"name": VOLUME_3PAR_PRIV5, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                        "templateUri": '3par1-pool1-private', "isPermanent": True,
                        },
                   {"properties": {"name": VOLUME_3PAR_PRIV6, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_PRIV7, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_PRIV8, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": False, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED1, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED2, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED3, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED4, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED5, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED6, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED7, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {"properties": {"name": VOLUME_3PAR_SHARED8, "description": "", "storagePool": STORESERV1_POOL1, "size": 1073741824, "provisioningType": "Thin", "isShareable": True, "snapshotPool": STORESERV1_POOL1},
                    "templateUri": 'ROOT', "isPermanent": True,
                    },
                   {
    "properties": {
        "storagePool": STOREVIRTUAL1_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-slptprivate1"
    },
    "templateUri": "vsa1-raid5-private",
    "isPermanent": False
},
    {
    "properties": {
        "storagePool": STOREVIRTUAL1_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-slptprivate2"
    },
    "templateUri": "vsa1-raid5-private",
    "isPermanent": False
},
    {
    "properties": {
        "storagePool": STOREVIRTUAL1_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-slptshared1"
    },
    "templateUri": "vsa1-raid5-shared",
    "isPermanent": True
}, {
    "properties": {
        "storagePool": STOREVIRTUAL1_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-slptshared2"
    },
    "templateUri": "vsa1-raid5-shared",
    "isPermanent": True
}, {
    "properties": {
        "storagePool": STOREVIRTUAL2_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-mlptshared1"
    },
    "templateUri": "vsa2-raid0-shared",
    "isPermanent": True
},
    {
    "properties": {
        "storagePool": STOREVIRTUAL2_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-mlptshared2"
    },
    "templateUri": "vsa2-raid0-shared",
    "isPermanent": True
},
    {
    "properties": {
        "storagePool": STOREVIRTUAL2_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-mlptprivate1"
    },
    "templateUri": "vsa2-raid0-private",
    "isPermanent": True
},
    {
    "properties": {
        "storagePool": STOREVIRTUAL2_POOL,
        "size": 2147483648,
        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
        "provisioningType": "Full",
        "name": "fvt-exist-mlptprivate2"
    },
    "templateUri": "vsa2-raid0-private",
    "isPermanent": True
},
]

storage_templates = [{"name": "3par1-pool1-private", "description": "",
                      "rootTemplateUri": "Volume root template for StoreServ 3.1.3",
                      "properties": {
                          "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                   "type": "string", "minLength": 1, "maxLength": 100, "required": True,
                                   "meta": {"locked": False}},
                          "description": {"title": "Description", "description": "A description for the volume",
                                          "type": "string", "minLength": 0, "maxLength": 2000, "default": "3Par1 pool1 private",
                                          "meta": {"locked": False}},
                          "storagePool": {"title": "Storage Pool", "description": "A common provisioning group URI reference",
                                          "type": "string", "required": True, "format": "x-uri-reference",
                                          "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                          "default": STORESERV1_POOL1
                                          },
                          "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                                   "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                                   "meta": {"locked": False, "semanticType": "capacity"},
                                   "default": 1073741824, },
                          "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                          "type": "boolean", "meta": {"locked": False},
                                          "default": False, },
                          "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                               "type": "string", "enum": ["Thin", "Full"], "meta":{"locked": True, "createOnly": True},
                                               "default": "Thin"},
                          "snapshotPool": {"title": "Snapshot Pool", "description": "A URI referenceto the common provisioning group used to create snapshots",
                                           "type": "string", "format": "x-uri-reference", "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                           "default": STORESERV1_POOL1, }
                      },
                      },
                     {"name": "3par1-pool1-shared", "description": "",
                      "rootTemplateUri": "Volume root template for StoreServ 3.1.3",
                      "properties": {
                          "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                   "type": "string", "minLength": 1, "maxLength": 100, "required": True,
                                   "meta": {"locked": False}},
                          "description": {"title": "Description", "description": "A description for the volume",
                                          "type": "string", "minLength": 0, "maxLength": 2000, "default": "3Par pool1 shared",
                                          "meta": {"locked": False}},
                          "storagePool": {"title": "Storage Pool", "description": "A common provisioning group URI reference",
                                          "type": "string", "required": True, "format": "x-uri-reference",
                                          "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                          "default": STORESERV1_POOL1
                                          },
                          "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                                   "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                                   "meta": {"locked": False, "semanticType": "capacity"},
                                   "default": 1073741824, },
                          "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                          "type": "boolean", "meta": {"locked": False},
                                          "default": True, },
                          "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                               "type": "string", "enum": ["Thin", "Full"], "meta":{"locked": True, "createOnly": True},
                                               "default": "Thin"},
                          "snapshotPool": {"title": "Snapshot Pool", "description": "A URI referenceto the common provisioning group used to create snapshots",
                                           "type": "string", "format": "x-uri-reference", "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                           "default": STORESERV1_POOL1, }
                      },
                      },
                     {"name": "vsa1-raid5-private",
                      "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
                      "description": "",
                      "properties": {
                          "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                   "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                          "description": {"title": "Description", "description": "A description for the volume",
                                          "type": "string", "minLength": 0, "maxLength": 2000,
                                          "default": "",
                                          "meta": {"locked": False}},
                          "storagePool": {"title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                                          "type": "string", "format": "x-uri-reference", "required": True,
                                          "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                          "default": STOREVIRTUAL1_POOL},
                          "size": {"title": "Capacity", "description": "Capacity of the volume in bytes",
                                   "type": "integer", "minimum": 4194304, "required": True,
                                   "default": 1073741824,
                                   "meta": {"locked": False, "semanticType": "capacity"}},
                          "dataProtectionLevel": {"title": "Data Protection Level", "description": "Indicates the number and configuration of data copies in the Storage Pool",
                                                  "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way", "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way", "NetworkRaid6DualParity"],
                                                  "default":"NetworkRaid5SingleParity",
                                                  "required":True, "meta":{"locked": False, "semanticType": "device-dataProtectionLevel"}},
                          "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                               "type": "string", "enum": ["Thin", "Full"],
                                               "default":"Thin",
                                               "meta":{"locked": False, "createOnly": "True", "semanticType": "device-provisioningType"}},
                          "isAdaptiveOptimizationEnabled": {"title": "Adaptive Optimization", "description": "",
                                                            "type": "boolean", "default": True, "meta": {"locked": False}},
                          "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                          "type": "boolean", "default": False, "meta": {"locked": False}}
                      },
                      },
                     {"name": "vsa1-raid5-shared",
                      "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
                      "description": "",
                      "properties": {
                          "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                   "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                          "description": {"title": "Description", "description": "A description for the volume",
                                          "type": "string", "minLength": 0, "maxLength": 2000,
                                          "default": "",
                                          "meta": {"locked": False}},
                          "storagePool": {"title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                                          "type": "string", "format": "x-uri-reference", "required": True,
                                          "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                          "default": STOREVIRTUAL1_POOL},
                          "size": {"title": "Capacity", "description": "Capacity of the volume in bytes",
                                   "type": "integer", "minimum": 4194304, "required": True,
                                   "default": 1073741824,
                                   "meta": {"locked": False, "semanticType": "capacity"}},
                          "dataProtectionLevel": {"title": "Data Protection Level", "description": "Indicates the number and configuration of data copies in the Storage Pool",
                                                  "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way", "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way", "NetworkRaid6DualParity"],
                                                  "default":"NetworkRaid5SingleParity",
                                                  "required":True, "meta":{"locked": False, "semanticType": "device-dataProtectionLevel"}},
                          "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                               "type": "string", "enum": ["Thin", "Full"],
                                               "default":"Thin",
                                               "meta":{"locked": False, "createOnly": "True", "semanticType": "device-provisioningType"}},
                          "isAdaptiveOptimizationEnabled": {"title": "Adaptive Optimization", "description": "",
                                                            "type": "boolean", "default": True, "meta": {"locked": False}},
                          "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                          "type": "boolean", "default": True, "meta": {"locked": False}}
                      },
                      },
                     {"name": "vsa2-raid0-private",
                      "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
                      "description": "",
                      "properties": {
                          "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                   "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                          "description": {"title": "Description", "description": "A description for the volume",
                                          "type": "string", "minLength": 0, "maxLength": 2000,
                                          "default": "",
                                          "meta": {"locked": False}},
                          "storagePool": {"title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                                          "type": "string", "format": "x-uri-reference", "required": True,
                                          "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                          "default": STOREVIRTUAL2_POOL},
                          "size": {"title": "Capacity", "description": "Capacity of the volume in bytes",
                                   "type": "integer", "minimum": 4194304, "required": True,
                                   "default": 1073741824,
                                   "meta": {"locked": False, "semanticType": "capacity"}},
                          "dataProtectionLevel": {"title": "Data Protection Level", "description": "Indicates the number and configuration of data copies in the Storage Pool",
                                                  "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way", "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way", "NetworkRaid6DualParity"],
                                                  "default":"NetworkRaid0None",
                                                  "required":True, "meta":{"locked": False, "semanticType": "device-dataProtectionLevel"}},
                          "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                               "type": "string", "enum": ["Thin", "Full"],
                                               "default":"Thin",
                                               "meta":{"locked": False, "createOnly": "True", "semanticType": "device-provisioningType"}},
                          "isAdaptiveOptimizationEnabled": {"title": "Adaptive Optimization", "description": "",
                                                            "type": "boolean", "default": True, "meta": {"locked": False}},
                          "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                          "type": "boolean", "default": False, "meta": {"locked": False}}
                      },
                      },
                     {"name": "vsa2-raid0-shared",
                      "rootTemplateUri": "Volume root template for StoreVirtual 1.2",
                      "description": "",
                      "properties": {
                          "name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                   "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                          "description": {"title": "Description", "description": "A description for the volume",
                                          "type": "string", "minLength": 0, "maxLength": 2000,
                                          "default": "",
                                          "meta": {"locked": False}},
                          "storagePool": {"title": "Storage Pool", "description": "StoragePoolURI the volume should be added to",
                                          "type": "string", "format": "x-uri-reference", "required": True,
                                          "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                          "default": STOREVIRTUAL2_POOL},
                          "size": {"title": "Capacity", "description": "Capacity of the volume in bytes",
                                   "type": "integer", "minimum": 4194304, "required": True,
                                   "default": 1073741824,
                                   "meta": {"locked": False, "semanticType": "capacity"}},
                          "dataProtectionLevel": {"title": "Data Protection Level", "description": "Indicates the number and configuration of data copies in the Storage Pool",
                                                  "type": "string", "enum": ["NetworkRaid0None", "NetworkRaid5SingleParity", "NetworkRaid10Mirror2Way", "NetworkRaid10Mirror3Way", "NetworkRaid10Mirror4Way", "NetworkRaid6DualParity"],
                                                  "default":"NetworkRaid0None",
                                                  "required":True, "meta":{"locked": False, "semanticType": "device-dataProtectionLevel"}},
                          "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                               "type": "string", "enum": ["Thin", "Full"],
                                               "default":"Thin",
                                               "meta":{"locked": False, "createOnly": "True", "semanticType": "device-provisioningType"}},
                          "isAdaptiveOptimizationEnabled": {"title": "Adaptive Optimization", "description": "",
                                                            "type": "boolean", "default": True, "meta": {"locked": False}},
                          "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                          "type": "boolean", "default": True, "meta": {"locked": False}}
                      },
                      },
                     ]

# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
FIRST_BOOT_TARGET_IP = STOREVIRTUAL1_VIP
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

# PROFILE1: profile on bay1, Blackbird
PROFILE1_NAME = "tbird9-bay1-profile"
PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol'
PROFILE1_DEFAULT_INITIATOR_NAME = 'iqn.1986-03.com.hp:uefi-i37-cn7446069m'
PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird9-bay1"
PROFILE1_INITIATOR_IP_1 = "192.168.22.51"
PROFILE1_INITIATOR_IP_2 = "192.168.22.56"
PROFILE1_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol_attempt_1"
PROFILE1_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol_attempt_2"
PROFILE1_CHAP_NAME = 'tbird9-bay1'
PROFILE1_MCHAP_NAME = 'tbird9-bay1'

# PROFILE2: profile on bay6, Redbird
PROFILE2_NAME = "tbird9-bay6-profile"
PROFILE2_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol"
PROFILE2_DEFAULT_INITIATOR_NAME = 'iqn.1986-03.com.hp:uefi-i39-cn7540000s'
PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird9-bay6"
PROFILE2_INITIATOR_IP_1 = "192.168.22.52"
PROFILE2_INITIATOR_IP_2 = "192.168.22.57"
PROFILE2_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol_attempt_1"
PROFILE2_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol_attempt_2"
PROFILE2_CHAP_NAME = 'tbird9-bay6'
PROFILE2_MCHAP_NAME = 'tbird9-bay6'

# PROFILE3: bay6 profile move to bay2
PROFILE3_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol"
PROFILE3_DEFAULT_INITIATOR_NAME = 'iqn.1986-03.com.hp:uefi-i37-cn74450748'
PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird9-bay2"
PROFILE3_INITIATOR_IP_1 = "192.168.22.61"
PROFILE3_INITIATOR_IP_2 = "192.168.22.62"
PROFILE3_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol_attempt_1"
PROFILE3_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol_attempt_2"

appliance = {
    "type": "ApplianceNetworkConfiguration",
    "applianceNetworks": [
        {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.210.217", "app1Ipv6Addr": "",
         "app2Ipv4Addr": "16.114.210.218", "app2Ipv6Addr": "",
                         "virtIpv4Addr": "16.114.211.88", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
                         "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": "wpst-tbird-9-oneview.vse.rdlabs.hpecorp.net",
                         "confOneNode": True, "interfaceName": "", "macAddress": None,
                         "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE", "overrideIpv4DhcpDnsServers": False, "ipv4Subnet": "255.255.240.0", "ipv4Gateway": "16.114.208.1", "ipv6Subnet": None, "ipv6Gateway": None,
                         "domainName": "vse.rdlabs.hpecorp.net", "searchDomains": [], "ipv4NameServers":["16.125.25.81", "16.125.25.82"],
                         "ipv6NameServers":["16.125.25.81", "16.125.25.82"], "bondedTo":None, "aliasDisabled":True,
                         "configureRabbitMqSslListener":False, "configurePostgresSslListener":False, "webServerCertificate":None,
                         "webServerCertificateChain":None, "webServerCertificateKey":None}
    ],
    "serverCertificate": {"rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
                          "rabbitMQCertificateKey": None, "postgresCertificate": None,
                          "postgresRootCACertificate": None, "postgresCertificateKey": None}
}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]

licenses = [{'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
            {'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
            {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            {'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'},
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]

enclosures = [
    {"type": "EnclosureV400", "name": ENC1, },
]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC1ICBAY6, },
]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': 'ethernet-networkV300',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': 'ethernet-networkV300',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': 'ethernet-networkV300',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': 'ethernet-networkV300',
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

fc_networks = [
    {'name': 'fa-a', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_A},
    {'name': 'fa-b', 'autoLoginRedistribution': True, 'type': 'fc-networkV300', 'linkStabilityTime': '30', 'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_B},
]

network_sets = [{'name': 'NS1', 'type': 'network-setV300', 'networkUris': ['net100', 'net300'], 'nativeNetworkUri': 'net100'}, ]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
]


uplink_sets = {'us_untagged': {'name': 'us-untagged',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['network-untagged'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          ]
                               },
               'us_tunnel': {'name': 'us-tunnel',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['network-tunnel'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        ]
                             },
               'us_tagged': {'name': 'us-tagged',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['net300', 'net100'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        ]
                             },
               'fa-a': {'name': 'fa-a',
                        'ethernetNetworkType': 'NotApplicable',
                        'networkType': 'FibreChannel',
                        'networkUris': ['fa-a'],
                        'lacpTimer': 'Long',
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'},
                                                   ]
                        },
               'fa-b': {'name': 'fa-b',
                        'ethernetNetworkType': 'NotApplicable',
                        'networkType': 'FibreChannel',
                        'networkUris': ['fa-b'],
                        'lacpTimer': 'Long',
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'},
                                                   ]
                        }
               }


ligs = [
    {'name': LIG_NAME,
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': icmap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'ethernetSettings': None,
     'fcoeSettings': {'fcoeMode': 'FcfNpv'},
     'stackingMode': 'Enclosure',
     'ethernetSettings': None,
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None,
     'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tunnel'].copy(), uplink_sets['us_tagged'].copy(), uplink_sets['fa-a'].copy(), uplink_sets['fa-b'].copy()],
     },
]

egs = [{'name': EG_NAME,
        'type': 'EnclosureGroupV300',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 2,
        'configurationScript': None,
        'interconnectBayMappings':
        [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]


les = [{'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]
# Negative Profiles

# Test set 0, validation errors
# Bootable volume and non-bootable connection
ts0_negative_profile1 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile1', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": True, "lunType": "Manual", "lun": 1,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile1-eph-priv-vsa2", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL2_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL2_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid0None"},
                   ]
                   }
}

# Bootable connection and non-bootable volume
ts0_negative_profile2 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile1', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1, "name": "", "functionType": "iSCSI", "portId": "Auto", "requestedMbps": "2500",
         "networkUri": "ETH:network-untagged", "mac": None, "wwpn": None, "wwnn": None,
         "ipv4": {"ipAddressSource": "UserDefined", "subnetMask": "255.255.192.0", "gateway": "", "ipAddress": "192.168.22.65"},
         "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume",
                  "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "initiatorVlanId": "",
                            "firstBootTargetIp": "", "firstBootTargetPort": "", "secondBootTargetIp": "", "secondBootTargetPort": "",
                            "chapLevel": None, "initiatorName": "", "bootTargetName": "", "bootTargetLun": "",
                            "chapName": "", "chapSecret": None, "mutualChapName": "", "mutualChapSecret": None}
                  }
         }
    ],
    "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Auto", "lun": None,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"boot-volume", "volumeDescription":"", "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL1_POOL,
                        "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL1_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824",
                        "volumeShareable":False, "permanent":True, "dataProtectionLevel":"NetworkRaid0None"}]
                   }
}

# Invalid lun=0 for MLPT VSA volume
ts0_negative_profile3 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile3', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
         "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 0,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile1-eph-priv-vsa2", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL2_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL2_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid0None"},
                   ]
                   }
}

# non-unique LUN number for MLPT VSA volumes
ts0_negative_profile4 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile4', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 1,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile2-eph-priv1-vsa2", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL2_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL2_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid0None"},
                       {"id": 2, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 1,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile2-eph-priv2-vsa2", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL2_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL2_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid0None"},
                   ]
                   }
}

# No port configuration
ts0_negative_profile5 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile5', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Auto", "lun": None,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile4-eph-priv-vsa1", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL1_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL1_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid5SingleParity"},
                   ]
                   }
}
# Inviad LUN for SLPT VSA volume
ts0_negative_profile6 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile6', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 1,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile5-eph-priv-vsa1", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL1_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL1_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid5SingleParity"},
                   ]
                   }
}

# Mixed paths for VSA volume, one enabled and the other disabled
ts0_negative_profile7 = {
    "type": "ServerProfileV7", "name": 'ts0_negative_profile7', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Auto", "lun": None,
                        "storagePaths": [{"isEnabled": False, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile6-eph-priv-vsa1", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL1_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL1_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid5SingleParity"},
                   ]
                   }
}

ts0_negative_profile_tasks = [


    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile1.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'Bootable_volume_nonbootable_connection'},
    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile2.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'SP_Bootable_connection_nonbootable_volume'},
    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile3.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'Invalidate_LUN_MLPT_VSA'},
    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile4.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'LUN_not_unique_MLPT_VSA'},
    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile5.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'No_port_configuration'},
    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile6.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'Invalid_LUN_SLPT_VSA'},
    {
        'keyword': 'Add Server Profile',
        'argument': ts0_negative_profile7.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'Mixed_paths_VSA'}


]

# Test set 1, negative, volume attachment failures
# Unsupported DataProtection level
ts1_negative_profile1 = {
    "type": "ServerProfileV7", "name": 'ts1_negative_profile1', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME,
    "iscsiInitiatorNameType": "AutoGenerated", "iscsiInitiatorName": "",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         },
        {"id": 2,
         "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "functionType": "Ethernet",
         "macType": "Virtual"
         }
    ],
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
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "volumeAttachments": [
                       {"id": 1, "volumeUri": None, "isBootVolume": False, "lunType": "Auto", "lun": None,
                        "storagePaths": [{"isEnabled": True, "connectionId": 1, "targetSelector": "Auto", "targets": []},
                                         {"isEnabled": True, "connectionId": 2, "targetSelector": "Auto", "targets": []}],
                        "volumeName":"neg-profile1-eph-priv-vsa2", "volumeDescription":"",
                        "volumeStoragePoolUri":"SPOOL:" + STOREVIRTUAL2_POOL, "volumeStorageSystemUri":"SSYS:" + STOREVIRTUAL2_NAME,
                        "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                        "permanent":False, "dataProtectionLevel":"NetworkRaid6DualParity"},
                   ]
                   }
}

ts1_ephemeral_volumes = [
    {"name": "neg-profile1-eph-priv-vsa2", },
]

ts1_profiles_delete = [
    ts1_negative_profile1.copy(),
]

ts1_negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': ts1_negative_profile1.copy(),
        'taskState': 'Error',
        'timeout': '600',
        'errorMessage': 'Unsupported_DataProtectionLevel_VSA'},
]


Multiple_LUN_Per_Target = [{
    "type": "ServerProfileV7", "name": 'MLPT-profile', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY5, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1, "name": "Tunnel1", "functionType": "Ethernet", "portId": "Mezz 3:1-a",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "macType": "Virtual"},

        {"id": 2, "name": "Tunnel2",
         "functionType": "Ethernet",
         "portId": "Mezz 3:2-a",
         "wwpnType": "Virtual",
         "requestedMbps": "2500",
         "networkUri": "ETH:network-tunnel",
         "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},

    ],
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
    "sanStorage":{"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                  "volumeAttachments": [{
                      "lunType": "Auto",
                      "isBootVolume": False,
                      "volumeUri": None,
                      "volumeName": "f313-mlpt-shared",
                      "lunType": "Manual",
                      "lun": 1,
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": True,
                      "permanent": True,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },
                      {
                      "isBootVolume": False,
                      "volumeUri": None,
                      "lunType": "Manual",
                      "lun": 2,
                      "volumeName": "f313-mlpt-private1",
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": False,
                      "permanent": False,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },
                      {
                      "isBootVolume": False,
                      "volumeUri": None,
                      "lunType": "Manual",
                      "lun": 3,
                      "volumeName": "f313-mlpt-private2",
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": False,
                      "permanent": False,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },
                      {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV1, "isBootVolume": False, "lunType": "Manual", "lun": 7,
                       "storagePaths": [
                           {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                           {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
                       },
                      {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED1, "isBootVolume": False, "lunType": "Manual", "lun": 8,
                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                                        {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
                       },
                      {"id": 9, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 9,
                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                                        {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
                       "volumeName":'Reg1_3PAR_PERM_PRIV1', "volumeDescription":"",
                       "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
                       "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                       "permanent":True, "dataProtectionLevel":None},
                      {"id": 10, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 10,
                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                                        {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
                       "volumeName":'Reg1_3PAR_EPH_PRIV1', "volumeDescription":"",
                       "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
                       "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                       "permanent":False, "dataProtectionLevel":None}

                  ]
                  }
}]

verify_Multiple_LUN_Per_Target = {
    "type": "ServerProfileV7", "name": 'MLPT-profile', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY5, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1, "name": "Tunnel1", "functionType": "Ethernet", "portId": "Mezz 3:1-a",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "macType": "Virtual"},

        {"id": 2, "name": "Tunnel2",
         "functionType": "Ethernet",
         "portId": "Mezz 3:2-a",
         "wwpnType": "Virtual",
         "requestedMbps": "2500",
         "networkUri": "ETH:network-tunnel",
         "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}}

    ],
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
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "sanSystemCredentials": [
                       {
                          "chapLevel": "MutualChap",
                          "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "chapSource": "AutoGenerated",
                           "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL
                       }
                   ],
                   "volumeAttachments": [{
                       "lunType": "Manual",
                       "isBootVolume": False,
                       "id": 1,
                       "lun": 1,
                       "volumeUri": "SVOL:f313-mlpt-shared",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-shared)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-shared)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {
                       "lunType": "Manual",
                       "isBootVolume": False,
                       "lun": 2,
                       "id": 2,
                       "volumeUri": "SVOL:f313-mlpt-private1",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private1)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private1)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {
                       "lunType": "Manual",
                       "isBootVolume": False,
                       "id": 3,
                       "lun": 3,
                       "volumeUri": "SVOL:f313-mlpt-private2",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private2)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private2)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV1, "isBootVolume": False, "lunType": "Manual", "lun": 7,
                        "storagePaths": [
                            {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                            {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                        },
                       {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED1, "isBootVolume": False, "lunType": "Manual", "lun": 8,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                        },
                       {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV1", "isBootVolume": False, "lunType": "Manual", "lun": 9,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                        },
                       {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV1", "isBootVolume": False, "lunType": "Manual", "lun": 10,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                        }

                   ]
                   }
}


verify_efuse_on = {
    "type": "ServerProfileV7", "name": 'MLPT-profile', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY5, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1, "name": "Tunnel1", "functionType": "Ethernet", "portId": "Mezz 3:1-a",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "macType": "Virtual"},

        {"id": 2, "name": "Tunnel2",
         "functionType": "Ethernet",
         "portId": "Mezz 3:2-a",
         "wwpnType": "Virtual",
         "requestedMbps": "2500",
         "networkUri": "ETH:network-tunnel",
         "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},

    ],
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
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "sanSystemCredentials": [
                       {
                          "chapLevel": "MutualChap",
                          "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "chapSource": "AutoGenerated",
                           "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL
                       }
                   ],
                   "volumeAttachments": [{
                       "lunType": "Manual",
                       "isBootVolume": False,
                       "state": "Reserved",
                       "id": 1,
                       "lun": 1,
                       "volumeUri": "SVOL:f313-mlpt-shared",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-shared)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-shared)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {
                       "lunType": "Manual",
                       "isBootVolume": False,
                       "id": 2,
                       "lun": 2,
                       "state": "Reserved",
                       "volumeUri": "SVOL:f313-mlpt-private1",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private1)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private1)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {
                       "lunType": "Manual",
                       "isBootVolume": False,
                       "id": 3,
                       "lun": 3,
                       "state": "Reserved",
                       "volumeUri": "SVOL:f313-mlpt-private2",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private2)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iiqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:f313-mlpt-private2)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV1, "isBootVolume": False, "lunType": "Manual", "lun": 7,
                        "storagePaths": [
                            {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                            {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                        },
                       {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED1, "isBootVolume": False, "lunType": "Manual", "lun": 8,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                        },
                       {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV1", "isBootVolume": False, "lunType": "Manual", "lun": 9,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                        },
                       {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV1", "isBootVolume": False, "lunType": "Manual", "lun": 10,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                        }

                   ]
                   }
}

ethernet_tunnel = [{
    "type": "ServerProfileV7", "name": 'ethernet_tunnel', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1, "name": "Tunnel1", "functionType": "Ethernet", "portId": "Mezz 3:1-a",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "macType": "Virtual"},

        {"id": 2, "name": "Tunnel2",
         "functionType": "Ethernet",
         "portId": "Mezz 3:2-a",
         "wwpnType": "Virtual",
         "requestedMbps": "2500",
         "networkUri": "ETH:network-tunnel",
         "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},

    ],
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
    "sanStorage":{"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                  "volumeAttachments": [{
                      "lunType": "Auto",
                      "isBootVolume": False,
                      "volumeUri": None,
                      "volumeName": "ethernet_tunnel-shared",
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": True,
                      "permanent": True,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },
                      {
                      "lunType": "Auto",
                      "isBootVolume": False,
                      "volumeUri": None,
                      "volumeName": "ethernet_tunnel-private",
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": False,
                      "permanent": False,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },
                      {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV2, "isBootVolume": False, "lunType": "Manual", "lun": 7,
                       "storagePaths": [
                           {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                           {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
                       },
                      {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED2, "isBootVolume": False, "lunType": "Manual", "lun": 8,
                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                                        {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
                       },
                      {"id": 9, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 9,
                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                                        {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
                       "volumeName":'Reg1_3PAR_PERM_PRIV2', "volumeDescription":"",
                       "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
                       "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                       "permanent":True, "dataProtectionLevel":None},
                      {"id": 10, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 10,
                       "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                                        {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
                       "volumeName":'Reg1_3PAR_EPH_PRIV2', "volumeDescription":"",
                       "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
                       "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
                       "permanent":False, "dataProtectionLevel":None}

                  ]
                  }
}]

verify_ethernet_tunnel = {
    "type": "ServerProfileV7", "name": 'ethernet_tunnel', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY3, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
    "connections": [
        {"id": 1, "name": "Tunnel1", "functionType": "Ethernet", "portId": "Mezz 3:1-a",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-tunnel",
            "macType": "Virtual"},

        {"id": 2, "name": "Tunnel2",
         "functionType": "Ethernet",
         "portId": "Mezz 3:2-a",
         "wwpnType": "Virtual",
         "requestedMbps": "2500",
         "networkUri": "ETH:network-tunnel",
         "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},

    ],
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
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "sanSystemCredentials": [
                       {
                          "chapLevel": "MutualChap",
                          "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "chapSource": "AutoGenerated",
                           "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL
                       }
                   ],
                   "volumeAttachments": [{
                       "lunType": "Auto",
                       "id": 1,
                       "isBootVolume": False,
                       "volumeUri": "SVOL:ethernet_tunnel-shared",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:ethernet-tunnel-shared)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:ethernet-tunnel-shared)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {
                       "lunType": "Auto",
                       "id": 2,
                       "isBootVolume": False,
                       "volumeUri": "SVOL:ethernet_tunnel-private",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_POOL,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:ethernet-tunnel-private)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL2_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:ethernet-tunnel-private)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV2, "isBootVolume": False, "lunType": "Manual", "lun": 7,
                        "storagePaths": [
                            {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                            {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                        },
                       {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED2, "isBootVolume": False, "lunType": "Manual", "lun": 8,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                        },
                       {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV2", "isBootVolume": False, "lunType": "Manual", "lun": 9,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                        },
                       {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV2", "isBootVolume": False, "lunType": "Manual", "lun": 10,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                        }

                   ]
                   }
}

isci_untagged = [{
    "type": "ServerProfileV7", "name": 'isci-untagged', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY7, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
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

    ],
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
    "sanStorage":{"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                  "volumeAttachments": [{
                      "lunType": "Auto",
                      "isBootVolume": False,
                      "volumeUri": None,
                      "volumeName": "isci-untagged-shared",
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": True,
                      "permanent": True,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },
                      {
                      "lunType": "Auto",
                      "isBootVolume": False,
                      "volumeUri": None,
                      "volumeName": "isci-untagged-private",
                      "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                      "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                      "volumeProvisionType": "Thin",
                      "volumeProvisionedCapacityBytes": "2147483648",
                      "volumeShareable": False,
                      "permanent": False,
                      "dataProtectionLevel": "NetworkRaid0None",

                      "storagePaths": [
                          {
                              "isEnabled": True,
                              "connectionId": 1,
                          },
                          {
                              "isEnabled": True,
                              "connectionId": 2,
                          }
                      ]
                  },

                  ]
                  }
}]

verify_isci_untagged = {
    "type": "ServerProfileV7", "name": 'isci-untagged', "description": "",
    "serverHardwareUri": 'SH:' + ENC1SHBAY7, "enclosureGroupUri": 'EG:' + EG_NAME, "enclosureUri": 'ENC:' + ENC1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "affinity": "Bay",
    "hideUnusedFlexNics": True, "osDeploymentSettings": None,
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

    ],
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
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
    "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x)", "manageSanStorage": True,
                   "sanSystemCredentials": [
                       {
                          "chapLevel": "MutualChap",
                          "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "chapSource": "AutoGenerated",
                           "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                           "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME
                       }
                   ],
                   "volumeAttachments": [{
                       "lunType": "Auto",
                       "id": 1,
                       "isBootVolume": False,
                       "volumeUri": "SVOL:isci-untagged-shared",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL1_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:isci-untagged-shared)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL1_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:isci-untagged-shared)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   },
                       {
                       "lunType": "Auto",
                       "id": 2,
                       "isBootVolume": False,
                       "volumeUri": "SVOL:isci-untagged-private",
                       "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                       "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                       "storagePaths": [
                           {
                               "isEnabled": True,
                               "connectionId": 1,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL1_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:isci-untagged-private)",
                                       "tcpPort": "3260"
                                   }]
                           },
                           {
                               "isEnabled": True,
                               "connectionId": 2,
                               "targets": [
                                   {
                                       "ipAddress": STOREVIRTUAL1_VIP,
                                       "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:isci-untagged-private)",
                                       "tcpPort": "3260"
                                   }]
                           }
                       ]
                   }

                   ]
                   }
}

unassigned_profile_new_n_existing_volumes = [{
    "wwnType": "Virtual",
    "serialNumberType": "Physical",
    "serverHardwareTypeUri": "SHT:SY 660 Gen9 1",
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 2,
            "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
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
    "type": "ServerProfileV7",
    "description": "shared volumes",
    "name": "unassigned",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": None,
                "volumeName": "fvt-new-unassigned1",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": False,
                "dataProtectionLevel": "NetworkRaid0None",

                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": None,
                "volumeName": "fvt-new-unassigned2",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": True,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": None,
                "volumeName": "fvt-new-unassigned3",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": False,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV4, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED4, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_PERM_PRIV4', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":True, "dataProtectionLevel":None},
            {"id": 10, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_EPH_PRIV4', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":False, "dataProtectionLevel":None}
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}]

verify_unassigned_profile_new_n_existing_volumes = {
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 2,
            "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:SY 660 Gen9 1",
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
    "type": "ServerProfileV7",
    "description": "shared volumes",
    "name": "unassigned",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "lunType": "Auto",
                "id": 1,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned1",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Reserved',
                'status': 'OK',
                'storagePaths': [{'connectionId': 1, 'isEnabled': True, 'status': 'Unknown', 'targetSelector': 'Auto', 'targets': []},
                                 {'connectionId': 2, 'isEnabled': True, 'status': 'Unknown', 'targetSelector': 'Auto', 'targets': []}],

            },
            {
                "lunType": "Auto",
                "id": 2,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned2",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Reserved',
                'status': 'OK',
                'storagePaths': [{'connectionId': 1, 'isEnabled': True, 'status': 'Unknown', 'targetSelector': 'Auto', 'targets': []},
                                 {'connectionId': 2, 'isEnabled': True, 'status': 'Unknown', 'targetSelector': 'Auto', 'targets': []}]
            },
            {
                "lunType": "Auto",
                "id": 3,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned3",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Reserved',
                'status': 'OK',
                'storagePaths': [{'connectionId': 1, 'isEnabled': True, 'status': 'Unknown', 'targetSelector': 'Auto', 'targets': []},
                                 {'connectionId': 2, 'isEnabled': True, 'status': 'Unknown', 'targetSelector': 'Auto', 'targets': []}]
            },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV4, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED4, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}


assigned_profile_new_n_existing_volumes = [{
    "type": "ServerProfileV7",
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 2,
            "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "enclosureUri": "ENC:" + ENC1,
    "description": "shared volumes",
    "name": "unassigned",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureBay": 6,
    "serverHardwareUri": "SH:" + ENC2SHBAY1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:SY 660 Gen9 1",
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
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1,
                "lunType": "Auto",
                "lun": None,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned1",
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
                    }
                ]
             },
            {"id": 2,
                "lun": None,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned2",
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
                    }
                ]
             },
            {"id": 3,
                "lun": None,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned3",
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
                    }
                ]
             },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV4, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED4, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }

}]

verify_assigned_profile_new_n_existing_volumes = {
    "type": "ServerProfileV7",
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 2,
            "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "enclosureUri": "ENC:" + ENC1,
    "description": "shared volumes",
    "name": "unassigned",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serverHardwareUri": "SH:" + ENC2SHBAY1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "serverHardwareTypeUri": "SHT:SY 660 Gen9 1",

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
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-[a-z,0-9,-]+)",
    "sanStorage": {
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-[a-z,0-9,-]+)",
                "chapSource": "AutoGenerated",
                "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-[a-z,0-9,-]+)",
                "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME
            }
        ],
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1,
                "lunType": "Auto",
                "lun": 0,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned1",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Attached',
                'status': 'OK',
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned1)",
                                        "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned1)",
                                        "tcpPort": "3260"
                            }]
                    }
                ]
             },
            {"id": 2,
                "lun": 0,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned2",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Attached',
                'status': 'OK',
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned2)",
                                        "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned2)",
                                        "tcpPort": "3260"
                            }]
                    }
                ]
             },
            {"id": 3,
                "lun": 0,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned3",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Attached',
                'status': 'OK',
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned3)",
                                        "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned3)",
                                        "tcpPort": "3260"
                            }]
                    }
                ]
             },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV4, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED4, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }

}

move_profile_new_and_existing_volumes = [{
    "type": "ServerProfileV7",
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 2,
            "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "enclosureUri": "ENC:" + ENC1,
    "description": "moved",
    "name": "unassigned",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureBay": 3,
    "serverHardwareUri": "SH:" + ENC3SHBAY1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:SY 480 Gen9 1",
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
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1,
                "lunType": "Auto",
                "lun": None,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned1",
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
                    }
                ]
             },
            {"id": 2,
                "lun": None,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned2",
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
                    }
                ]
             },
            {"id": 3,
                "lun": None,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned3",
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
                    }
                ]
             },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV4, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED4, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }

}]


verify_move_profile_new_and_existing_volumes = {
    "type": "ServerProfileV7",
    "connections": [
        {"id": 1,
            "portId": "Mezz 3:1-a",
            "name": "Untagged-1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 2,
            "portId": "Mezz 3:2-a",
            "name": "Untagged-2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "functionType": "Ethernet",
            "macType": "Virtual"
         },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "enclosureUri": "ENC:" + ENC1,
    "description": "moved",
    "name": "unassigned",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureBay": 3,
    "serverHardwareUri": "SH:" + ENC3SHBAY1,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:SY 480 Gen9 1",

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
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-[a-z,0-9,-]+)",
    "sanStorage": {
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-[a-z,0-9,-]+)",
                "chapSource": "AutoGenerated",
                "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-[a-z,0-9,-]+)",
                "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME
            }
        ],
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1,
                "lunType": "Auto",
                "lun": 0,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned1",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Attached',
                'status': 'OK',
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned11)",
                                        "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned1)",
                                        "tcpPort": "3260"
                            }]
                    }
                ]
             },
            {"id": 2,
                "lun": 0,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned2",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Attached',
                'status': 'OK',
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned2)",
                                        "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned2)",
                                        "tcpPort": "3260"
                            }]
                    }
                ]
             },
            {"id": 3,
                "lun": 0,
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-unassigned3",
                "volumeStoragePoolUri": volumeStoragePoolUri1,
                "volumeStorageSystemUri": volumeStorageSystemUri1,
                'state': 'Attached',
                'status': 'OK',
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned3)",
                                        "tcpPort": "3260"
                            }]
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                        "targets": [
                            {
                                "ipAddress": STOREVIRTUAL1_VIP,
                                "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-unassigned3)",
                                        "tcpPort": "3260"
                            }]
                    }
                ]
             },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV4, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED4, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV4", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }

}

edit_profile = [{
    "connections": [],
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC2SHBAY5,
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "connections": [],
    "type": "ServerProfileV7",
    "description": "edit_profile_new_and_exist_vols",
    "name": "edit_profile_new_and_exist_vols",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []}


}]

edit_profile_new_and_existing_volumes = [{
    "connections": [],
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC2SHBAY5,
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "connections": [
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 1,
            "macType": "Virtual",
            "name": "Tunnel-1",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 2,
            "macType": "Virtual",
            "name": "Tunnel-2",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "type": "ServerProfileV7",
    "description": "shared volumes",
    "name": "edit_profile_new_and_exist_vols",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-slptshared2",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },

            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": None,
                "volumeName": "fvt-new-slptprivate3",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": False,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Manual",
                "lun": "3",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-mlptshared2",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Manual",
                "lun": "4",
                "isBootVolume": False,
                "volumeUri": None,
                "volumeName": "fvt-new-mlptprivate3",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": False,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV5, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED5, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_PERM_PRIV5', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":True, "dataProtectionLevel":None},
            {"id": 10, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_EPH_PRIV5', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":False, "dataProtectionLevel":None}
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}]

verify_edit_profile_new_and_existing_volumes = {
    "connections": [],
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC2SHBAY5,
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "connections": [
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 1,
            "macType": "Virtual",
            "name": "Tunnel-1",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 2,
            "macType": "Virtual",
            "name": "Tunnel-2",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "type": "ServerProfileV7",
    "description": "shared volumes",
    "name": "edit_profile_new_and_exist_vols",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1,
                "lunType": "Auto",
                "lun": "0",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-slptshared2",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
             },

            {"id": 2,
             "lunType": "Auto",
                "lun": "0",
             "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-slptprivate3",
             "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
             "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
             "storagePaths": [
                 {
                        "isEnabled": True,
                        "connectionId": 1,
                 },
                 {
                     "isEnabled": True,
                     "connectionId": 2,
                 }
             ]
             },
            {"id": 3,
                "lunType": "Manual",
                "lun": "3",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-mlptshared2",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
             },
            {
                "id": 4,
                "lunType": "Manual",
                "lun": "4",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-new-mlptprivate3",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV5, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED5, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV5", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV5", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}


new_private_share_sp = [{
    "wwnType": "Virtual",
    "serialNumberType": "Physical",
    "connections": [
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 1,
            "macType": "Virtual",
            "name": "Tunnel-1",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 2,
            "macType": "Virtual",
            "name": "Tunnel-2",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
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
    "type": "ServerProfileV7",
    "enclosureUri": "ENC:" + ENC1,
    "description": "shared volumes",
    "serverHardwareUri": "SH:" + ENC1SHBAY3,
    "name": "new_private_shared_mplt_slpt",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeName": "fvt-new-privateslpt1",
                'volumeUri': None,
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": False,
                "dataProtectionLevel": "NetworkRaid0None",

                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeName": "fvt-new-sharedslpt2",
                'volumeUri': None,
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": True,
                "permanent": True,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Manual",
                "lun": "2",
                "isBootVolume": False,
                'volumeUri': None,
                "volumeName": "fvt-new-privatemlpt1",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": False,
                "permanent": False,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Manual",
                "lun": "3",
                "isBootVolume": False,
                'volumeUri': None,
                "volumeName": "fvt-new-sharedmlpt2",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                "volumeProvisionType": "Thin",
                "volumeProvisionedCapacityBytes": "2147483648",
                "volumeShareable": True,
                "permanent": True,
                "dataProtectionLevel": "NetworkRaid0None",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV6, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED6, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_PERM_PRIV6', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":True, "dataProtectionLevel":None},
            {"id": 10, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_EPH_PRIV6', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":False, "dataProtectionLevel":None}
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}]

verify_new_private_share_sp = {
    "wwnType": "Virtual",
    "serialNumberType": "Physical",
    "connections": [
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 1,
            "macType": "Virtual",
            "name": "Tunnel-1",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 2,
            "macType": "Virtual",
            "name": "Tunnel-2",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
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
    "type": "ServerProfileV7",
    "enclosureUri": "ENC:" + ENC1,
    "description": "shared volumes",
    "serverHardwareUri": "SH:" + ENC1SHBAY3,
    "name": "new_private_shared_mplt_slpt",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1,
                "lunType": "Auto",
                "lun": 0,
                "isBootVolume": False,
                'volumeUri': "SVOL:fvt-new-privateslpt1",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                "storagePaths": [
                    {'connectionId': 1, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto',
                     'targets': [{'ipAddress': STOREVIRTUAL1_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-privateslpt1)', 'tcpPort': '3260'}]},
                    {'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto', 'targets':
                     [{'ipAddress': STOREVIRTUAL1_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-privateslpt1)', 'tcpPort': '3260'}]}]
             },
            {"id": 2,
                "lunType": "Auto",
                "lun": 0,
             "isBootVolume": False,
                'volumeUri': "SVOL:fvt-new-sharedslpt2",
             "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
             "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
             "storagePaths": [
                 {'connectionId': 1, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto',
                  'targets': [{'ipAddress': STOREVIRTUAL1_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-sharedslpt2)', 'tcpPort': '3260'}]},
                 {'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto', 'targets':
                  [{'ipAddress': STOREVIRTUAL1_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-new-sharedslpt2)', 'tcpPort': '3260'}]}]
             },
            {"id": 3,
             "lunType": "Manual",
                "lun": 2,
             "isBootVolume": False,
                'volumeUri': "SVOL:fvt-new-privatemlpt1",
             "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
             "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
             "storagePaths": [
                 {'connectionId': 1, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto',
                  'targets': [{'ipAddress': STOREVIRTUAL2_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-new-privatemlpt1)', 'tcpPort': '3260'}]},
                 {'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto', 'targets':
                  [{'ipAddress': STOREVIRTUAL2_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-new-privatemlpt1)', 'tcpPort': '3260'}]}]
             },
            {"id": 4,
                "lunType": "Manual",
                "lun": 3,
                "isBootVolume": False,
                'volumeUri': "SVOL:fvt-new-sharedmlpt2",
                "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                "storagePaths": [
                    {'connectionId': 1, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto',
                     'targets': [{'ipAddress': STOREVIRTUAL2_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-new-sharedmlpt2)', 'tcpPort': '3260'}]},
                    {'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'targetSelector': 'Auto', 'targets':
                     [{'ipAddress': STOREVIRTUAL2_VIP, 'name': 'REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-new-sharedmlpt2)', 'tcpPort': '3260'}]}]
             },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV6, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED6, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
             },
            {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV6", "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             },
            {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV6", "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
             "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
             }
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}

existing_private_share_sp = [{
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connections": [
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 1,
            "macType": "Virtual",
            "name": "Tunnel-1",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {
            "allocatedMbps": 2500,
            "deploymentStatus": "Deployed",
            "functionType": "Ethernet",
            "id": 2,
            "macType": "Virtual",
            "name": "Tunnel-2",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
        },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
         "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
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
    "type": "ServerProfileV7",
    "enclosureUri": "ENC:" + ENC1,
    "description": "shared volumes",
    "serverHardwareUri": "SH:" + ENC3SHBAY5,
    "enclosureBay": 6,
    "name": "existing_shared_private_mlpt_slpt",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-slptshared1",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Auto",
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-slptprivate1",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Manual",
                "lun": 2,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-mlptshared1",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {
                "lunType": "Manual",
                "lun": 3,
                "isBootVolume": False,
                "volumeUri": "SVOL:fvt-exist-mlptprivate1",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                    }
                ]
            },
            {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV7, "isBootVolume": False, "lunType": "Manual", "lun": 7,
             "storagePaths": [
                 {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED7, "isBootVolume": False, "lunType": "Manual", "lun": 8,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}]
             },
            {"id": 9, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 9,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_PERM_PRIV7', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":True, "dataProtectionLevel":None},
            {"id": 10, "volumeUri": None, "isBootVolume": False, "lunType": "Manual", "lun": 10,
             "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto", "targets": []},
                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto", "targets": []}],
             "volumeName":'Reg1_3PAR_EPH_PRIV7', "volumeDescription":"",
             "volumeStoragePoolUri":"SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri":"SSYS:" + STORESERV1_NAME,
             "volumeProvisionType":"Thin", "volumeProvisionedCapacityBytes":"1073741824", "volumeShareable":False,
             "permanent":False, "dataProtectionLevel":None}
        ],
        "hostOSType": "Windows 2012 / WS2012 R2"
    }
}]
verify_existing_private_share_sp = {

    "affinity": "Bay",
    "bios": {
                "manageBios": False,
                "overriddenSettings": []
    },
    "boot": {
        "manageBoot": False,
        "order": []
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
                "pxeBootPolicy": "Auto"
    },
    "category": "server-profiles",
    "connections": [

                {
                    "allocatedMbps": 2500,
                    "deploymentStatus": "Deployed",
                    "functionType": "Ethernet",
                    "id": 1,
                    "macType": "Virtual",
                    "name": "Tunnel-1",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
                },
        {
                    "allocatedMbps": 2500,
                    "deploymentStatus": "Deployed",
                    "functionType": "Ethernet",
                    "id": 2,
                    "macType": "Virtual",
                    "name": "Tunnel-2",
                    "networkUri": "ETH:network-tunnel",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "wwpnType": "Virtual"
                },
        {"id": 3, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'FC:fa-a',
                    "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
        {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": 'FC:fa-b',
                    "mac": None, "wwpn": None, "wwnn": None, "ipv4": {}},
    ],
    "description": "shared volumes",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": "ENC:" + ENC1,
    "firmware": {
        "forceInstallFirmware": False,
        "manageFirmware": False
    },
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
    "iscsiInitiatorNameType": "AutoGenerated",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "macType": "Virtual",
    "name": "existing_shared_private_mlpt_slpt",
            "sanStorage": {
                "hostOSType": "Windows 2012 / WS2012 R2",
                "manageSanStorage": True,
                "sanSystemCredentials": [
                    {
                        "chapLevel": "MutualChap",
                        "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                        "chapSource": "AutoGenerated",
                        "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                        "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME
                    },
                    {
                        "chapLevel": "MutualChap",
                        "chapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                        "chapSource": "AutoGenerated",
                        "mutualChapName": "REGEX:(iqn\.2015-02\.com\.hpe:oneview-vcg[a-z,0-9]+)",
                        "storageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME
                    }
                ],
                "volumeAttachments": [
                    {
                        "id": 1,
                        "isBootVolume": False,
                        "lun": "0",
                        "lunType": "Auto",
                        "state": "Attached",
                        "status": "OK",
                        "storagePaths": [
                            {
                                "connectionId": 1,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL1_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-exist-slptshared1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            },
                            {
                                "connectionId": 2,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL1_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-exist-slptshared1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            }
                        ],
                        "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                        "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                        "volumeUri": "StorageVolumeV3:fvt-exist-slptshared1"
                    },
                    {
                        "id": 2,
                        "isBootVolume": False,
                        "lun": "0",
                        "lunType": "Auto",
                        "state": "Attached",
                        "status": "OK",
                        "storagePaths": [
                            {
                                "connectionId": 1,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL1_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-exist-slptprivate1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            },
                            {
                                "connectionId": 2,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL1_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa-mg-[a-z,0-9,-]+:\d+:fvt-exist-slptprivate1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            }
                        ],
                        "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL1_POOL,
                        "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL1_NAME,
                        "volumeUri": "StorageVolumeV3:fvt-exist-slptprivate1"
                    },
                    {
                        "id": 3,
                        "isBootVolume": False,
                        "lun": 2,
                        "lunType": "Manual",
                        "state": "Attached",
                        "status": "OK",
                        "storagePaths": [
                            {
                                "connectionId": 1,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL2_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-exist-mlptshared1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            },
                            {
                                "connectionId": 2,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL2_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-exist-mlptshared1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            }
                        ],
                        "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                        "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                        "volumeUri": "StorageVolumeV3:fvt-exist-mlptshared1"
                    },
                    {
                        "id": 4,
                        "isBootVolume": False,
                        "lun": 3,
                        "lunType": "Manual",
                        "state": "Attached",
                        "status": "OK",
                        "storagePaths": [
                            {
                                "connectionId": 1,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL2_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-exist-mlptprivate1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            },
                            {
                                "connectionId": 2,
                                "isEnabled": True,
                                "status": "OK",
                                "targetSelector": "Auto",
                                "targets": [
                                    {
                                        "ipAddress": STOREVIRTUAL2_VIP,
                                        "name": "REGEX:(iqn\.2003-10\.com\.lefthandnetworks:vsa84-mg:\d+:fvt-exist-mlptprivate1)",
                                        "tcpPort": "3260"
                                    }
                                ]
                            }
                        ],
                        "volumeStoragePoolUri": "StoragePoolV2:" + STOREVIRTUAL2_POOL,
                        "volumeStorageSystemUri": "StorageSystemV3:" + STOREVIRTUAL2_NAME,
                        "volumeUri": "StorageVolumeV3:fvt-exist-mlptprivate1"
                    },
                    {"id": 7, "volumeUri": "SVOL:" + VOLUME_3PAR_PRIV7, "isBootVolume": False, "lunType": "Manual", "lun": 7,
                        "storagePaths": [
                            {"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                            {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                     },
                    {"id": 8, "volumeUri": "SVOL:" + VOLUME_3PAR_SHARED7, "isBootVolume": False, "lunType": "Manual", "lun": 8,
                        "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                         {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]
                     },
                    {"id": 9, "volumeUri": "SVOL:Reg1_3PAR_PERM_PRIV7", "isBootVolume": False, "lunType": "Manual", "lun": 9,
                     "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                      {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                     },
                    {"id": 10, "volumeUri": "SVOL:Reg1_3PAR_EPH_PRIV7", "isBootVolume": False, "lunType": "Manual", "lun": 10,
                     "storagePaths": [{"isEnabled": True, "connectionId": 3, "targetSelector": "Auto"},
                                      {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}],
                        "volumeStoragePoolUri": "SPOOL:" + STORESERV1_POOL1, "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
                     }
                ]
    },
    "serialNumberType": "Virtual",
    "serverHardwareUri": "SH:" + ENC3SHBAY5,
    "state": "Normal",
    "status": "OK",
    "type": "ServerProfileV7",
            "wwnType": "Virtual"
}

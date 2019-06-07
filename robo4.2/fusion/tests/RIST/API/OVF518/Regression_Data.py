from copy import deepcopy

# Credentials
admin_credentials = {"userName": "Administrator", "password": "wpsthpvse1"}

# Types
ETHNET_TYPE = "ethernet-networkV4"
FCOENET_TYPE = "fcoe-networkV4"
FCNET_TYPE = "fc-networkV4"
LIG_TYPE = "logical-interconnect-groupV5"
STORSYS_TYPE = "StorageSystemsV4"
SP_TYPE = "ServerProfileV10"
SPT_TYPE = "ServerProfileTemplateV6"
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# PortIds
PORTID_NONE = "None"
PORTID_AUTO = "Auto"

# Networks
NWETH01 = "Eth_01"
NWETH02 = "Eth_02"
NWFCOE01 = "Fcoe_01"
NWFCOE02 = "Fcoe_02"
NWFCFA01 = "FA1"
NWFCFA02 = "FA2"
NWUMFCDA01 = "UmFcDa_01"
NWUMFCDA02 = "UmFcDa_02"
NWUMFCFA01 = "UmFcFa_01"
NWUMFCFA02 = "UmFcFa_02"
NWUMFCFA03 = "UmFcFa_03"
NWUMFCFA04 = "UmFcFa_04"

# Enclosures
ENC1 = "CN754406WB"

# Uplink Sets
LIG01_UPS01 = "ups01_eth"
LIG01_UPS02 = "ups02_eth"
LIG02_UPS01 = "ups01_FC"
LIG03_UPS01 = "ups01_eth"
LIG03_UPS02 = "ups02_eth"
LIG03_UPS03 = "ups03_FC"

# LIG, EG, LE
LIG01 = "lig01"
LIG02 = "lig02"
LIG03 = "lig03"
EG01 = "eg01"
EG02 = "eg02"
EG03 = "eg03"
LE01 = "le01"
EG_live = "EG1"

# Server Hardware Types
SHT01 = "SY 480 Gen9:1:Synergy 3530C 16G HBA:3:HP Synergy 3820C 10/20Gb CNA"
SHT01_HBA_PORT01 = "Mezz 1:1"
SHT01_HBA_PORT02 = "Mezz 1:2"
SHT01_CNA_PORT01 = "Mezz 3:1"
SHT01_CNA_PORT01A = "Mezz 3:1-a"
SHT01_CNA_PORT01B = "Mezz 3:1-b"
SHT01_CNA_PORT02A = "Mezz 3:2-a"
SHT01_CNA_PORT02B = "Mezz 3:2-b"
SHT01_CNA_PORT02 = "Mezz 3:2"

# Server Hardware
BOOTSERVER = "%s, bay 1" % ENC1

# 3par Storage
STORESERV01 = "wpst3par-7200-7-srv"
STORESERV01_NAME = "wpst3par-7200-7-srv"
STORESERV01_HOSTNAME = "wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net"
STORESERV01_STORAGE_POOL = "FVT_Tbird_reg1_r6"
STORESERV01_USER = "3paradm"
STORESERV01_PWD = "3pardata"

# Volumes
SHARED_VOLUME = "ovf518_shared_volume"
PRIVATE_VOLUME = "ovf518_private_volume"

# Other
ONEGB = 1073741824

ethernet_networks = [
    {
        "name": NWETH01,
        "type": ETHNET_TYPE,
        "ethernetNetworkType": "Tagged",
        "vlanId": 151,
        "purpose": "General",
        "smartLink": True,
        "privateNetwork": False
    },
    {
        "name": NWETH02,
        "type": ETHNET_TYPE,
        "ethernetNetworkType": "Tagged",
        "vlanId": 153,
        "purpose": "General",
        "smartLink": True,
        "privateNetwork": False
    }
]

fcoe_networks = [
    {
        "name": NWFCOE01,
        "type": FCOENET_TYPE,
        "vlanId": 3003,
        "managedSanUri": None
    },
    {
        "name": NWFCOE02,
        "type": FCOENET_TYPE,
        "vlanId": 3004,
        "managedSanUri": None
    }
]

fc_networks = [
    {
        "name": NWUMFCDA01,
        "type": FCNET_TYPE,
        "linkStabilityTime": 0,
        "fabricType": "DirectAttach",
        "managedSanUri": None,
        "autoLoginRedistribution": False
    },
    {
        "name": NWUMFCDA02,
        "type": FCNET_TYPE,
        "linkStabilityTime": 0,
        "fabricType": "DirectAttach",
        "managedSanUri": None,
        "autoLoginRedistribution": False
    },
    {
        "name": NWUMFCFA01,
        "type": FCNET_TYPE,
        "linkStabilityTime": 0,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "autoLoginRedistribution": False
    },
    {
        "name": NWUMFCFA02,
        "type": FCNET_TYPE,
        "linkStabilityTime": 0,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "autoLoginRedistribution": False
    },
    {
        "name": NWUMFCFA03,
        "type": FCNET_TYPE,
        "linkStabilityTime": 0,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "autoLoginRedistribution": False
    },
    {
        "name": NWUMFCFA04,
        "type": FCNET_TYPE,
        "linkStabilityTime": 0,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "autoLoginRedistribution": False
    }
]

lig01_uplink_sets = {
    LIG01_UPS01: {
        "name": LIG01_UPS01,
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "networkUris": [NWETH01],
        "mode": "Auto",
        "nativeNetworkUri": None,
        "logicalPortConfigInfos": [
            {"enclosure": "1", "bay": "3", "port": "Q2.1", "speed": "Auto"},
            {"enclosure": "1", "bay": "6", "port": "Q2.1", "speed": "Auto"}
        ]
    },
    LIG01_UPS02: {
        "name": LIG01_UPS02,
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "networkUris": [NWETH02],
        "mode": "Auto",
        "nativeNetworkUri": None,
        "logicalPortConfigInfos": [
            {"enclosure": "1", "bay": "3", "port": "Q2.2", "speed": "Auto"},
            {"enclosure": "1", "bay": "6", "port": "Q2.2", "speed": "Auto"}
        ]
    },
}

lig02_uplink_sets = {
    LIG02_UPS01: {
        "name": LIG02_UPS01,
        "networkType": "FibreChannel",
        "ethernetNetworkType": None,
        "networkUris": [NWFCFA02],
        "mode": "Auto",
        "nativeNetworkUri": None,
        "logicalPortConfigInfos": [
            {"enclosure": "-1", "bay": "1", "port": "1", "speed": "Auto"},
            {"enclosure": "-1", "bay": "1", "port": "2", "speed": "Auto"}
        ]
    },
}

lig03_uplink_sets = {
    LIG03_UPS01: {
        "name": LIG03_UPS01,
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "networkUris": [NWETH01],
        "mode": "Auto",
        "nativeNetworkUri": None,
        "logicalPortConfigInfos": [
            {"enclosure": "1", "bay": "3", "port": "Q2.1", "speed": "Auto"},
            {"enclosure": "1", "bay": "6", "port": "Q2.1", "speed": "Auto"}
        ]
    },
    LIG03_UPS02: {
        "name": LIG03_UPS02,
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "networkUris": [NWETH02],
        "mode": "Auto",
        "nativeNetworkUri": None,
        "logicalPortConfigInfos": [
            {"enclosure": "1", "bay": "3", "port": "Q2.2", "speed": "Auto"},
            {"enclosure": "1", "bay": "6", "port": "Q2.2", "speed": "Auto"}
        ]
    },
    LIG03_UPS03: {
        "name": LIG03_UPS03,
        "networkType": "FibreChannel",
        "ethernetNetworkType": None,
        "networkUris": [NWFCFA02],
        "mode": "Auto",
        "nativeNetworkUri": None,
        "logicalPortConfigInfos": [
            {"enclosure": "1", "bay": "3", "port": "Q3.1", "speed": "Auto"}
        ]
    },
}

ligs = [
    {
        "name": LIG01,
        "type": LIG_TYPE,
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {"bay": 3,
             "enclosure": 1,
             "type": "Virtual Connect SE 40Gb F8 Module for Synergy",
             "enclosureIndex": 1},
            {"bay": 6,
             "enclosure": 1,
             "type": "Virtual Connect SE 40Gb F8 Module for Synergy",
             "enclosureIndex": 1}
        ],
        "enclosureIndexes": [1],
        "interconnectBaySet": 3,
        "redundancyType": "Redundant",
        "uplinkSets": [deepcopy(v) for v in lig01_uplink_sets.itervalues()]
    },
    {
        "name": LIG02,
        "type": LIG_TYPE,
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {'bay': 1,
             'enclosure': -1,
             'type': 'Virtual Connect SE 16Gb FC Module for Synergy',
             'enclosureIndex': -1},
            {'bay': 4,
             'enclosure': -1,
             'type': 'Virtual Connect SE 16Gb FC Module for Synergy',
             'enclosureIndex': -1}
        ],
        "enclosureIndexes": [-1],
        "interconnectBaySet": 1,
        "redundancyType": "Redundant",
        "uplinkSets": [deepcopy(v) for v in lig02_uplink_sets.itervalues()]
    },
    {
        "name": LIG03,
        "type": LIG_TYPE,
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {"bay": 3,
             "enclosure": 1,
             "type": "Virtual Connect SE 40Gb F8 Module for Synergy",
             "enclosureIndex": 1},
            {"bay": 6,
             "enclosure": 1,
             "type": "Virtual Connect SE 40Gb F8 Module for Synergy",
             "enclosureIndex": 1}
        ],
        "enclosureIndexes": [1],
        "interconnectBaySet": 3,
        "redundancyType": "Redundant",
        "uplinkSets": [deepcopy(v) for v in lig03_uplink_sets.itervalues()]
    },
]

egs = [
    {
        "name": EG01,
        "enclosureCount": 1,
        "interconnectBayMappings": [
            {"interconnectBay": 3,
             "logicalInterconnectGroupUri": "LIG:" + LIG01},
            {"interconnectBay": 6,
             "logicalInterconnectGroupUri": "LIG:" + LIG01}
        ],
        "configurationScript": None,
        "ipAddressingMode": "DHCP",
        "ipRangeUris": [],
        "powerMode": "RedundantPowerFeed"
    },
    {
        "name": EG02,
        "enclosureCount": 1,
        "interconnectBayMappings": [
            {"interconnectBay": 1,
             "logicalInterconnectGroupUri": "LIG:" + LIG02},
            {"interconnectBay": 4,
             "logicalInterconnectGroupUri": "LIG:" + LIG02}
        ],
        "configurationScript": None,
        "ipAddressingMode": "DHCP",
        "ipRangeUris": [],
        "powerMode": "RedundantPowerFeed"
    },
    {
        "name": EG03,
        "enclosureCount": 1,
        "interconnectBayMappings": [
            {"interconnectBay": 3,
             "logicalInterconnectGroupUri": "LIG:" + LIG03},
            {"interconnectBay": 6,
             "logicalInterconnectGroupUri": "LIG:" + LIG03}
        ],
        "configurationScript": None,
        "ipAddressingMode": "DHCP",
        "ipRangeUris": [],
        "powerMode": "RedundantPowerFeed"
    },
]

les = [
    {
        "name": LE01,
        "enclosureUris": ["ENC:" + ENC1],
        "enclosureGroupUri": "EG:" + EG01,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False
    }
]

storage_systems = [
    {
        "type": STORSYS_TYPE,
        "name": STORESERV01_NAME,
        "family": "StoreServ",
        "hostname": STORESERV01_HOSTNAME,
        "credentials":
            {"username": STORESERV01_USER, "password": STORESERV01_PWD},
        "deviceSpecificAttributes":
            {"discoveredDomains": None, "managedDomain": "NO DOMAIN"},
        "ports": [
            {"name": "0:0:1",
             "expectedNetworkUri": "FC:" + NWFCFA01,
             "expectedNetworkName": NWFCFA01,
             "mode": "Managed",
             "protocolType": "FC"
             },
            {"name": "0:0:2",
             "expectedNetworkUri": "FC:" + NWFCFA01,
             "expectedNetworkName": NWFCFA01,
             "mode": "Managed",
             "protocolType": "FC"
             },
            {"name": "1:0:1",
             "expectedNetworkUri": "FC:" + NWFCFA02,
             "expectedNetworkName": NWFCFA02,
             "mode": "Managed",
             "protocolType": "FC"
             },
            {"name": "1:0:2",
             "expectedNetworkUri": "FC:" + NWFCFA02,
             "expectedNetworkName": NWFCFA02,
             "mode": "Managed",
             "protocolType": "FC"
             }]
    }
]

storage_pools = [
    {
        "storageSystemUri": STORESERV01_NAME,
        "name": STORESERV01_STORAGE_POOL,
        "isManaged": True,
    }
]

storage_volumes = [
    {
        "properties": {
            "name": SHARED_VOLUME,
            "description": "",
            "storagePool": STORESERV01_STORAGE_POOL,
            "size": ONEGB,
            "provisioningType": "Thin",
            "isShareable": True,
            "snapshotPool": STORESERV01_STORAGE_POOL
        },
        "templateUri": "ROOT",
        "isPermanent": True
    },
    {
        "properties": {
            "name": PRIVATE_VOLUME,
            "description": "",
            "storagePool": STORESERV01_STORAGE_POOL,
            "size": ONEGB,
            "provisioningType": "Thin",
            "isShareable": False,
            "snapshotPool": STORESERV01_STORAGE_POOL
        },
        "templateUri": "ROOT",
        "isPermanent": True
    },
]

# Negative Profile Tests

# Invalid profile - non-VC connection with port Id empty
nonvc_invalid_portid_empty = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_portid_empty",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": None}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with port Id set to None
nonvc_invalid_portid_none = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_portid_none",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": PORTID_NONE}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with port Id set to Auto
nonvc_invalid_portid_auto = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_portid_auto",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": PORTID_AUTO}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with port Id set to a mapped port
nonvc_invalid_portid_mapped = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_portid_mapped",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG02,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with a fibre channel network that is
# direct attach
nonvc_invalid_fc_network = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_fc_network",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCDA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with a CNA or ethernet adapter port
nonvc_invalid_port_type = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_port_type",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_CNA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with connection.boot not null
nonvc_invalid_boot_not_null = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_boot_not_null",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01,
             "boot": {"priority": "NotBootable"}
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid profile - non-VC connection with requestedMbps not null
nonvc_invalid_requestedmbps_not_null = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_invalid_requestedmbps_not_null",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01,
             "requestedMbps": "2500"
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Negative Profile Tasks
negative_profile_invalid_portid_empty_task = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_portid_empty.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORTID_EMPTY"
}

negative_profile_invalid_portid_none_task = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_portid_none.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORTID_NONE"
}

negative_profile_invalid_portid_auto_task = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_portid_auto.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORTID_AUTO"
}

negative_profile_invalid_portid_mapped_task = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_portid_mapped.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_MAPPED_PORT"
}

negative_profile_invalid_fc_network_task = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_fc_network.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_DIRECT_ATTACH"
}

negative_profile_invalid_port_type_task = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_port_type.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORT_TYPE"
}

negative_profile_invalid_boot_not_null = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_boot_not_null.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_BOOT_ATTRIBUTES"
}

negative_profile_invalid_requestedmbps_not_null = {
    "keyword": "Add Server Profile", "argument": nonvc_invalid_requestedmbps_not_null.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_REQUESTED_BANDWIDTH"
}

# Positive profile creation (POST) tests

# Valid profile with a non-VC connection
nonvc_valid_profile = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_valid_profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Valid profile with a non-VC connection and volume attachments
nonvc_valid_profile_with_volume_attachments = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_valid_profile_with_volume_attachments",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True},
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volumeUri": "V:" + SHARED_VOLUME,
             "storagePaths": [
                 {"connectionId": 1,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True}
             ]
             }
        ]
    }
}

# Valid assigned profile with a non-VC connection and volume attachments
nonvc_valid_assigned_profile_with_volume_attachments = {
    "type": SP_TYPE,
    "name": "ovf518-nonvc_valid_assigned_profile_with_volume_attachments",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + BOOTSERVER,
    "affinity": "BayAndServer",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None, "secureBoot": "Unmanaged"},
    "boot": {"order": ["CD", "USB", "HardDisk", "PXE"], "manageBoot": True},
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volumeUri": "V:" + PRIVATE_VOLUME,
             "storagePaths": [
                 {"connectionId": 1,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True}
             ]
             }
        ]
    }
}

# Negative Template Tests

# Invalid template - non-VC connection with port Id empty
template_nonvc_invalid_portid_empty = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_portid_empty",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": None}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid template - non-VC connection with port Id set to Auto
template_nonvc_invalid_portid_auto = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_portid_auto",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": PORTID_AUTO}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid template - non-VC connection with port Id set to a mapped port
template_nonvc_invalid_portid_mapped = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_portid_mapped",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG02,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid template - non-VC connection with a fibre channel network that
# is direct attach
template_nonvc_invalid_fc_network = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_fc_network",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCDA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid template - non-VC connection with a CNA or ethernet adapter port
template_nonvc_invalid_port_type = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_port_type",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_CNA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid template - non-VC connection with connection.boot not null
template_nonvc_invalid_boot_not_null = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_boot_not_null",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01,
             "boot": {"priority": "NotBootable"}
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Invalid template - non-VC connection with requestedMbps not null
template_nonvc_invalid_requestedmbps_not_null = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_invalid_requestedmbps_not_null",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01,
             "requestedMbps": "2500"
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Negative Template Tasks
negative_template_invalid_portid_empty_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_portid_empty.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORTID_EMPTY"
}

negative_template_invalid_portid_auto_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_portid_auto.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORTID_AUTO"
}

negative_template_invalid_portid_mapped_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_portid_mapped.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_MAPPED_PORT"
}

negative_template_invalid_fc_network_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_fc_network.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_DIRECT_ATTACH"
}

negative_template_invalid_port_type_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_port_type.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_PORT_TYPE"
}

negative_template_invalid_boot_not_null_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_boot_not_null.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_BOOT_ATTRIBUTES"
}

negative_template_invalid_requestedmbps_not_null_task = {
    "keyword": "Add Server Profile Template", "argument": template_nonvc_invalid_requestedmbps_not_null.copy(),
    "taskState": "Error", "timeout": "120", "interval": "2",
    "errorMessage": "INVALID_NONVC_REQUESTED_BANDWIDTH"
}

# Positive template tests

# Valid template with a non-VC connection
template_nonvc_valid_profile = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_valid_profile",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# Valid template with a non-VC connection and volume attachments
template_nonvc_valid_profile_with_volume_attachments = {
    "type": SPT_TYPE,
    "name": "ovf518-template_nonvc_valid_profile_with_volume_attachments",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True},
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volume": {
                    "isPermanent": True,
                    "templateUri": "ROOT:" + STORESERV01_STORAGE_POOL,
                    "properties": {
                        "name": "volume-ovf518-template_nonvc_valid_profile_with_volume_attachments",
                                "storagePool": "SP:" + STORESERV01_STORAGE_POOL,
                                "size": ONEGB,
                                "provisioningType": "Thin",
                                "isShareable": False}
                },
             "storagePaths": [
                 {"connectionId": 1, "isEnabled": True, "targetSelector": "Auto", "targets": []}]
             }
        ]
    }
}

# Valid template with a non-VC connection and volume attachments, which will be used to test
# profile creation from a template
template_for_profile_creation = {
    "type": SPT_TYPE,
    "name": "ovf518-template_for_profile_creation",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True},
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volume": {
                    "isPermanent": True,
                    "templateUri": "ROOT:" + STORESERV01_STORAGE_POOL,
                    "properties": {
                        "name": "volume-ovf518-template_for_profile_creation",
                                "storagePool": "SP:" + STORESERV01_STORAGE_POOL,
                                "size": ONEGB,
                                "provisioningType": "Thin",
                                "isShareable": False}
                },
             "storagePaths": [
                 {"connectionId": 1, "isEnabled": True, "targetSelector": "Auto", "targets": []}]
             }
        ]
    }
}

profile_templates = [
    template_for_profile_creation.copy(),
]

create_profile = [{
    "name": "ovf518-template_for_profile_creation-profile",
    "serverProfileTemplateUri": "SPT:" + "ovf518-template_for_profile_creation"
}]

verify_profile_dto = {
    "type": SP_TYPE,
    "name": "ovf518-template_for_profile_creation-profile",
    "templateCompliance": "Compliant",
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {"id": 1, "lunType": "Auto",
             "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
             "state": "Reserved",
             "storagePaths": [{
                 "connectionId": 1,
                 "targetSelector": "Auto",
                 "targets": [],
                 "isEnabled": True}],
             "isBootVolume": False}],
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}


# Positive profile edit (PUT) tests

# Initial unassigned profile with one non-VC connection
profile_with_nonvc_connection = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

profile_with_nonvc_connection_to_delete = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection"
}

# Edit the profile by adding an ethernet connection
profile_with_nonvc_connection_edit_add_connection = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

profile_with_nonvc_connection_edit_add_connection_validator = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    }
}

# Edit the profile by changing the network and port on a connection
profile_with_nonvc_connection_edit_change_connection_params = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_HBA_PORT02},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

profile_with_nonvc_connection_edit_change_connection_params_validator = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_HBA_PORT02},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    }
}

# Edit the profile by removing all connections
profile_with_nonvc_connection_delete_connections = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

profile_with_nonvc_connection_delete_connections_validator = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "connections": []
    }
}

# Edit the profile by adding a volume, VC and non-VC connections, and
# storage paths to both connections
profile_with_nonvc_connection_edit_add_volume_with_storage_paths = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01 non-VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02 VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT01B}
        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volumeUri": "V:" + SHARED_VOLUME,
             "storagePaths": [
                 {"connectionId": 1,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True},
                 {"connectionId": 2,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True}
             ]
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

profile_with_nonvc_connection_edit_add_volume_with_storage_paths_validator = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01 non-VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02 VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT01B}
        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volumeUri": "V:" + SHARED_VOLUME,
             "storagePaths": [
                 {"connectionId": 1,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True},
                 {"connectionId": 2,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True}
             ]
             }
        ]
    }
}

# Edit the profile by deleting one connection
profile_with_nonvc_connection_edit_delete_nonvc_connection = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 2, "name": "cnx02 VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT01B}
        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volumeUri": "V:" + SHARED_VOLUME,
             "storagePaths": [
                 {"connectionId": 2,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True}
             ]
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

profile_with_nonvc_connection_edit_delete_nonvc_connection_validator = {
    "type": SP_TYPE,
    "name": "ovf518-profile_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "connections": [
            {"id": 2, "name": "cnx02 VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT01B}
        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volumeUri": "V:" + SHARED_VOLUME,
             "storagePaths": [
                 {"connectionId": 2,
                  "targets": [],
                     "targetSelector": "Auto",
                     "isEnabled": True}
             ]
             }
        ]
    }
}


# Positive template edit (PUT) tests

# Initial template with one non-VC connection
template_with_nonvc_connection = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

template_with_nonvc_connection_to_delete = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection"
}

# Edit the template by adding an ethernet connection
template_with_nonvc_connection_edit_add_connection = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

template_with_nonvc_connection_edit_add_connection_validator = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    }
}

# Edit the template by changing the network and port on a connection
template_with_nonvc_connection_edit_change_connection_params = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_HBA_PORT02},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

template_with_nonvc_connection_edit_change_connection_params_validator = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_HBA_PORT02},
            {"id": 2, "name": "cnx02", "functionType": "Ethernet",
             "networkUri": "ETH:" + NWETH01,
             "portId": SHT01_CNA_PORT01A,
             "boot": {"priority": "NotBootable"}}
        ]
    }
}

# Edit the template by removing all connections
template_with_nonvc_connection_delete_connections = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": []
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

template_with_nonvc_connection_delete_connections_validator = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "manageConnections": True,
        "connections": []
    }
}

# Edit the template by adding a volume, VC and non-VC connections, and
# storage paths to both connections
template_with_nonvc_connection_edit_add_volume_with_storage_paths = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01 non-VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02 VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT01B}
        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volume": {
                    "isPermanent": True,
                    "templateUri": "ROOT:" + STORESERV01_STORAGE_POOL,
                    "properties": {
                        "name": "volume-ovf518-template_with_nonvc_connection",
                                "storagePool": "SP:" + STORESERV01_STORAGE_POOL,
                                "size": ONEGB,
                                "provisioningType": "Thin",
                                "isShareable": False}
                },
             "storagePaths": [
                 {"connectionId": 1,
                  "isEnabled": True,
                  "targetSelector": "Auto",
                  "targets": []},
                 {"connectionId": 2, "isEnabled": True, "targetSelector": "Auto", "targets": []}]
             }
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

template_with_nonvc_connection_edit_add_volume_with_storage_paths_validator = {
    "type": SPT_TYPE,
    "name": "ovf518-template_with_nonvc_connection",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {"id": 1, "name": "cnx01 non-VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "cnx02 VC", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT01B}
        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [
            {"id": 1, "isBootVolume": False, "lunType": "Auto",
                "volumeStorageSystemUri": "SSYS:" + STORESERV01_NAME,
                "volume": {
                    "isPermanent": True,
                    "templateUri": "ROOT:" + STORESERV01_STORAGE_POOL,
                    "properties": {
                        "name": "volume-ovf518-template_with_nonvc_connection",
                                "storagePool": "SP:" + STORESERV01_STORAGE_POOL,
                                "size": ONEGB,
                                "provisioningType": "Thin",
                                "isShareable": False}
                },
             "storagePaths": [
                 {"connectionId": 1,
                  "isEnabled": True,
                  "targetSelector": "Auto",
                  "targets": []},
                 {"connectionId": 2, "isEnabled": True, "targetSelector": "Auto", "targets": []}]
             }
        ]
    }
}


# Profile edit with compliance

# For creating the profile from template
profile_from_template_with_nonvc_connection = [{
    "name": "ovf518-template_with_nonvc_connection-profile",
    "serverProfileTemplateUri": "SPT:" + "ovf518-template_with_nonvc_connection"
}]

# For validating initial profile creation
profile_from_template_with_nonvc_connection_validator = {
    "type": SP_TYPE,
    "name": "ovf518-template_with_nonvc_connection-profile",
    "serverProfileTemplateUri": "SPT:" + "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Compliant",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT01}
        ]
    }
}

# Change the profile connection portId
profile_from_template_with_nonvc_connection_edit = {
    "type": SP_TYPE,
    "name": "ovf518-template_with_nonvc_connection-profile",
    "serverProfileTemplateUri": "SPT:" + "ovf518-template_with_nonvc_connection",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG03,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "cnx01", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_HBA_PORT02}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

# For testing profile non-compliance after editing the portId
profile_from_template_with_nonvc_connection_edit_non_compliance = {
    "name": "ovf518-template_with_nonvc_connection-profile",
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "isOnlineUpdate": False,
        "automaticUpdates": ["Change port of connection with id 1 on Mezzanine (Mezz) 1:2 to Mezzanine (Mezz) 1:1.", ],
        "manualUpdates": []
    }
}

# For deleting the profile
profile_from_template_with_nonvc_connection_to_delete = {
    "type": SP_TYPE,
    "name": "ovf518-template_with_nonvc_connection-profile"
}

# for OVS51247 CITE: Add missing test cases to non-VC RG test suites
# from the spreadsheet attached to the story
OVS51247_unassigned_T1 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_no_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_edit_unassigned_T1 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_no_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "unmanaged1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "unmanaged2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA02,
             "portId": SHT01_HBA_PORT02}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_with_conn_T2 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_w_mang_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG_live,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "managed1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_CNA_PORT01B},
            {"id": 2, "name": "managed2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT02B}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_edit_with_conn_T2 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_w_mang_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG_live,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "managed1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_CNA_PORT01B},
            {"id": 2, "name": "managed2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT02B},
            {"id": 3, "name": "unmanaged1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 4, "name": "unmanaged2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA02,
             "portId": SHT01_HBA_PORT02}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_add_unassigned_T3 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_w_unman_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "unmanaged1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 2, "name": "unmanaged2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA02,
             "portId": SHT01_HBA_PORT02}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_edit_unassigned_T3 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_w_unman_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG01,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": []
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_with_mang_unmang_conn_T4 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_w_mang_w_unmang_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG_live,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "managed1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_CNA_PORT01B},
            {"id": 2, "name": "managed2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT02B},
            {"id": 3, "name": "unmanaged1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA01,
             "portId": SHT01_HBA_PORT01},
            {"id": 4, "name": "unmanaged2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWUMFCFA02,
             "portId": SHT01_HBA_PORT02}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_edit_mang_unmang_conn_T4 = {
    "type": SP_TYPE,
    "name": "OVF518_OVS51247_unassigned_w_mang_w_unmang_conn",
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareTypeUri": "SHT:" + SHT01,
    "enclosureGroupUri": "EG:" + EG_live,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "managed1", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA01,
             "portId": SHT01_CNA_PORT01B},
            {"id": 2, "name": "managed2", "functionType": "FibreChannel",
             "networkUri": "FC:" + NWFCFA02,
             "portId": SHT01_CNA_PORT02B}
        ]
    },
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "boot": {"order": ["HardDisk"], "manageBoot": True}
}

OVS51247_add_unassigned_w_unman_w_both_T7_8 = [
    {
        "type": SP_TYPE,
        "name": "OVF518_OVS51247_unassigned_unman_conn_T7_8",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareTypeUri": "SHT:" + SHT01,
        "enclosureGroupUri": "EG:" + EG01,
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "connectionSettings": {
            "connections": [
                {"id": 1, "name": "unmanaged1", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA01,
                 "portId": SHT01_HBA_PORT01},
                {"id": 2, "name": "unmanaged2", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA02,
                 "portId": SHT01_HBA_PORT02}
            ]
        },
        "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
        "boot": {"order": ["HardDisk"], "manageBoot": True}
    },
    {
        "type": SP_TYPE,
        "name": "OVF518_OVS51247_unassigned_mang_unmang_conn_T7_8",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareTypeUri": "SHT:" + SHT01,
        "enclosureGroupUri": "EG:" + EG_live,
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "connectionSettings": {
            "connections": [
                {"id": 1, "name": "managed1", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWFCFA01,
                 "portId": SHT01_CNA_PORT01B},
                {"id": 2, "name": "managed2", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWFCFA02,
                 "portId": SHT01_CNA_PORT02B},
                {"id": 3, "name": "unmanaged1", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA01,
                 "portId": SHT01_HBA_PORT01},
                {"id": 4, "name": "unmanaged2", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA02,
                 "portId": SHT01_HBA_PORT02}
            ]
        },
        "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
        "boot": {"order": ["HardDisk"], "manageBoot": True}
    }
]

OVS51247_edit_unassigned_w_unman_w_both_T7_8 = [
    {
        "type": SP_TYPE,
        "name": "OVF518_OVS51247_unassigned_unman_conn_T7_8",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareTypeUri": "SHT:" + SHT01,
        "enclosureGroupUri": "EG:" + EG01,
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "connectionSettings": {
            "connections": [
                {"id": 1, "name": "unmanaged1", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA03,
                 "portId": SHT01_HBA_PORT01},
                {"id": 2, "name": "unmanaged2", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA04,
                 "portId": SHT01_HBA_PORT02}
            ]
        },
        "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
        "boot": {"order": ["HardDisk"], "manageBoot": True}
    },
    {
        "type": SP_TYPE,
        "name": "OVF518_OVS51247_unassigned_mang_unmang_conn_T7_8",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareTypeUri": "SHT:" + SHT01,
        "enclosureGroupUri": "EG:" + EG_live,
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "connectionSettings": {
            "connections": [
                {"id": 1, "name": "managed1", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWFCFA01,
                 "portId": SHT01_CNA_PORT01B},
                {"id": 2, "name": "managed2", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWFCFA02,
                 "portId": SHT01_CNA_PORT02B},
                {"id": 3, "name": "unmanaged1", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA03,
                 "portId": SHT01_HBA_PORT01},
                {"id": 4, "name": "unmanaged2", "functionType": "FibreChannel",
                 "networkUri": "FC:" + NWUMFCFA04,
                 "portId": SHT01_HBA_PORT02}
            ]
        },
        "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
        "boot": {"order": ["HardDisk"], "manageBoot": True}
    }
]

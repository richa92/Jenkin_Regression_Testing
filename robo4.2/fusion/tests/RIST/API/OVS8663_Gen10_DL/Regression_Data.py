admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV9'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# DL
DL120_name = 'FBTilodns'
DL120_IP = '16.114.212.91'
DL160_name = 'ILO7CE701P20F'
DL160_IP = '16.114.212.93'
DL180_name = 'ILO7CE651P1TU'
DL180_IP = '16.114.212.95'
DL360_name = 'ILOCN763807XQ'
DL360_IP = '16.114.212.49'
DL380_name = 'fvtdl43-ilo'
DL380_IP = '16.114.212.43'
# DL580_name = 'ILOCN771702NK'
# DL580_IP = '16.114.212.96'

Gen10_DLs_with_profiles = [DL180_name]
Gen10_DLs_names = [DL120_name, DL160_name, DL180_name, DL360_name, DL380_name]

Gen10_DLs = [
    {'name': DL120_name,
     'hostname': DL120_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
    {'name': DL160_name,
     'hostname': DL160_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
    {'name': DL180_name,
     'hostname': DL180_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
    # TODO, DL49 was sent to Huston to repair, temporary comment this DTOs.
    # {'name': DL360_name,
    #  'hostname': DL360_IP,
    #  'licensingIntent': 'OneViewNoiLO',
    #  'username': 'Administrator',
    #  'password': 'hpvse123',
    #  'force': True,
    #  'configurationState': 'Managed'
    #  },
    {'name': DL380_name,
     'hostname': DL380_IP,
     'licensingIntent': 'OneViewNoiLO',
     'username': 'Administrator',
     'password': 'hpvse123',
     'force': True,
     'configurationState': 'Managed'
     },
    # {'name': DL580_name,
    #  'hostname': DL580_IP,
    #  'licensingIntent': 'OneViewNoiLO',
    #  'username': 'Administrator',
    #  'password': 'hpvse123',
    #  'force': True,
    #  'configurationState': 'Managed'
    #  }
]
licenses = {'licenseType': 'HPE OneView Advanced',
            'license': [{'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'}]}

verify_DL_gen10_servers = [
    {
        "type": SERVER_HARDWARE_TYPE,
        "name": "FBTilodns",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "category": "server-hardware",
        "description": None,
        "formFactor": "1U",
        "licensingIntent": "OneViewNoiLO",
        "locationUri": None,
        "memoryMb": 8192,
        "migrationState": "Unknown",
        "model": "ProLiant DL120 Gen10",
        "mpHostInfo": {
                "mpHostName": "FBTilodns",
                "mpIpAddresses": [
                    {
                        "address": "16.114.212.91",
                        "type": "Static"
                    },
                    {
                        "address": "fe80:0:0:0:9618:82ff:fe18:90a",
                        "type": "LinkLocal"
                    }
                ]
        },
        "mpModel": "iLO5",
        "mpState": "OK",
        "partNumber": "8861879-001",
        "physicalServerHardwareUri": None,
        "portMap": None,
        "position": 0,
        "powerLock": False,
        "processorCoreCount": 4,
        "processorCount": 1,
        "processorSpeedMhz": 2200,
        "processorType": "Genuine Intel(R) CPU 0000%@",
        "refreshState": "NotRefreshing",
        "remoteSupportSettings": {
            "remoteSupportCurrentState": "Unknown",
            "destination": ""
        },
        "serialNumber": "7CE701P28K",
        "serverGroupUri": None,
        "serverHardwareTypeUri": "SHT:" + 'DL120 Gen10',
        "serverProfileUri": None,
        "serverSettings": None,
        "shortModel": "DL120 Gen10",
        "signature": None,
        "supportDataCollectionState": None,
        "supportDataCollectionType": None,
        "supportState": "NotSupported",
        "uidState": "Unsupported",
        "uri": "SH:" + DL120_name,
        "uuid": "31363838-3738-4337-4537-30315032384B",
        "virtualSerialNumber": None,
        "virtualUuid": None
    },
    {
        "type": SERVER_HARDWARE_TYPE,
        "name": DL160_name,
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "category": "server-hardware",
        "description": None,
        "formFactor": "1U",
        "hostOsType": None,
        "licensingIntent": "OneViewNoiLO",
        "locationUri": None,
        "memoryMb": 8192,
        "migrationState": "Unknown",
        "model": "ProLiant DL160 Gen10",
        "mpHostInfo": {
            "mpHostName": DL160_name,
            "mpIpAddresses": [
                {
                    "address": "16.114.212.93",
                    "type": "Static"
                },
                {
                    "address": "fe80:0:0:0:fe15:b4ff:fe97:60d6",
                    "type": "LinkLocal"
                }
            ]
        },
        "mpModel": "iLO5",
        "mpState": "OK",
        "partNumber": "8854836-001",
        "physicalServerHardwareUri": None,
        "portMap": None,
        "position": 0,
        "powerLock": False,
        "processorCoreCount": 14,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Genuine Intel(R) CPU 0000%@",
        "refreshState": "NotRefreshing",
        "remoteSupportSettings": {
            "remoteSupportCurrentState": "Unknown",
            "destination": ""
        },
        "serialNumber": "7CE701P20F",
        "serverGroupUri": None,
        "serverProfileUri": None,
        "serverSettings": None,
        "shortModel": "DL160 Gen10",
        "signature": None,
        "supportDataCollectionState": None,
        "supportDataCollectionType": None,
        "supportState": "NotSupported",
        "uidState": "Unsupported",
        "uri": "SH:" + DL160_name,
        "uuid": "34353838-3338-4337-4537-303150323046",
        "virtualSerialNumber": None,
        "virtualUuid": None
    },
    {
        "type": SERVER_HARDWARE_TYPE,
        "name": DL380_name,
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "category": "server-hardware",
        "description": None,
        "formFactor": "2U",
        "licensingIntent": "OneViewNoiLO",
        "locationUri": None,
        "memoryMb": 8192,
        "migrationState": "Unknown",
        "model": "ProLiant DL380 Gen10",
        "mpHostInfo": {
            "mpHostName": DL380_name,
            "mpIpAddresses": [
                {
                    "address": "16.114.212.43",
                    "type": "Static"
                },
                {
                    "address": "fe80:0:0:0:fe15:b4ff:fe97:37b4",
                    "type": "LinkLocal"
                }
            ]
        },
        "mpModel": "iLO5",
        "mpState": "OK",
        "partNumber": "854354-B21",
        "physicalServerHardwareUri": None,
        "portMap": None,
        "position": 0,
        "powerLock": False,
        "processorCoreCount": 20,
        "processorCount": 1,
        "processorSpeedMhz": 1800,
        "processorType": "Intel(R) Genuine processor",
        "refreshState": "NotRefreshing",
        "serialNumber": "7CE637P0L9",
        "serverGroupUri": None,
        "serverProfileUri": None,
        "serverSettings": None,
        "shortModel": "DL380 Gen10",
        "signature": None,
        "supportDataCollectionState": None,
        "supportDataCollectionType": None,
        "supportState": "NotSupported",
        "uidState": "Unsupported",
        "uri": "SH:" + DL380_name,
        "uuid": "33343538-3435-4337-4536-333750304C39",
        "virtualSerialNumber": None,
        "virtualUuid": None
    },
    {
        "type": SERVER_HARDWARE_TYPE,
        "name": DL180_name,
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "category": "server-hardware",
        "description": None,
        "formFactor": "1U",
        "hostOsType": None,
        "licensingIntent": "OneViewNoiLO",
        "locationUri": None,
        "memoryMb": 65536,
        "migrationState": "Unknown",
        "model": "ProLiant DL180 Gen10",
        "mpHostInfo": {
            "mpHostName": DL180_name,
            "mpIpAddresses": [
                {
                    "address": "16.114.212.95",
                    "type": "Static"
                },
                {
                    "address": "fe80:0:0:0:fe15:b4ff:fe97:61f0",
                    "type": "LinkLocal"
                }
            ]
        },
        "mpModel": "iLO5",
        "mpState": "OK",
        "partNumber": "854837-001",
        "physicalServerHardwareUri": None,
        "portMap": None,
        "position": 0,
        "powerLock": False,
        # "powerState": "On",
        "processorCoreCount": 12,
        "processorCount": 2,
        "processorSpeedMhz": 1800,
        "processorType": "Genuine Intel(R) CPU 0000%@",
        "refreshState": "NotRefreshing",
        "remoteSupportSettings": {
            "remoteSupportCurrentState": "Unknown",
            "destination": ""
        },
        "serialNumber": "7CE651P1TU",
        "serverGroupUri": None,
        "serverProfileUri": None,
        "serverSettings": None,
        "shortModel": "DL180 Gen10",
        "signature": None,
        # "status": "Critical",
        "supportDataCollectionState": None,
        "supportDataCollectionType": None,
        "supportState": "NotSupported",
        "uidState": "Unsupported",
        "uri": "SH:" + DL180_name,
        "uuid": "38343538-3733-4337-4536-353150315455",
        "virtualSerialNumber": None,
        "virtualUuid": None
    },
    # {
    #     "type": SERVER_HARDWARE_TYPE,
    #     "name": DL360_name,
    #     "state": "NoProfileApplied",
    #     "stateReason": "NotApplicable",
    #     "category": "server-hardware",
    #     "description": None,
    #     "formFactor": "1U",
    #     "licensingIntent": "OneViewNoiLO",
    #     "locationUri": None,
    #     "memoryMb": 8192,
    #     "migrationState": "Unknown",
    #     "model": "ProLiant DL360 Gen10",
    #     "mpHostInfo": {
    #         "mpHostName": DL360_name,
    #         "mpIpAddresses": [
    #             {
    #                 "address": "16.114.212.49",
    #                 "type": "Static"
    #             },
    #             {
    #                 "address": "fe80:0:0:0:e207:1bff:fefe:4110",
    #                 "type": "LinkLocal"
    #             }
    #         ]
    #     },
    #     "mpModel": "iLO5",
    #     "mpState": "OK",
    #     "partNumber": "847479-001",
    #     "physicalServerHardwareUri": None,
    #     "portMap": None,
    #     "position": 0,
    #     "powerLock": False,
    #     "processorCoreCount": 14,
    #     "processorCount": 1,
    #     "processorSpeedMhz": 1800,
    #     "processorType": "Intel(R) Genuine processor",
    #     "refreshState": "NotRefreshing",
    #     "remoteSupportSettings": {
    #         "remoteSupportCurrentState": "Unknown",
    #         "destination": ""
    #     },
    #     "serialNumber": "CN763807XQ",
    #     "serverGroupUri": None,
    #     "serverProfileUri": None,
    #     "serverSettings": None,
    #     "shortModel": "DL360 Gen10",
    #     "signature": None,
    # "status": "Critical",
    #     "supportDataCollectionState": None,
    #     "supportDataCollectionType": None,
    #     "supportState": "NotSupported",
    #     "uidState": "Unsupported",
    #     "uri": "SH:" + DL360_name,
    #     "uuid": "34373438-3937-4E43-3736-333830375851",
    #     "virtualSerialNumber": None,
    #     "virtualUuid": None
    # }
]

DL_gen10_profile_templates = [{
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serverProfileDescription": "",
    "serverHardwareTypeUri": "SHT:DL380 Gen10 1",
    "enclosureGroupUri": "",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "DL380 Gen10 1 - SPT",
    "description": "DL380 Gen10 1 - SPT",
    "affinity": None,
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": False},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                 "firmwareInstallType": None, "firmwareActivationType": "Immediate"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL380 Gen10 1 - SPT"}]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [{
            "logicalDrives": [{
                "name": "rd1",
                "raidLevel": "RAID1",
                "bootable": False,
                "numPhysicalDrives": 2,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODId": None
            }],
            "deviceSlot": "Embedded",
            "mode": "Mixed",
            "initialize": True
        }]
    },
    "sanStorage": None,
    "osDeploymentSettings": None
},
    {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serverProfileDescription": "DL120 Gen10 SPT with Raid 0 LS",
    "serverHardwareTypeUri": "SHT:DL120 Gen10 1",
    "enclosureGroupUri": "",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "DL120 Gen10 SPT",
    "description": "DL120 Gen10 SPT",
    "affinity": None,
    "connectionSettings": {"connections": [], "manageConnections": False},
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                 "forceInstallFirmware": False, "firmwareInstallType": None,
                 "firmwareActivationType": "Immediate"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL120"}]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [{
            "logicalDrives": [{
                "name": "rd0",
                "raidLevel": "RAID0",
                "bootable": True,
                "numPhysicalDrives": 1,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODId": None}
            ],
            "deviceSlot": "Embedded",
            "mode": "Mixed",
            "initialize": True}
        ]},
    "sanStorage": None,
    "osDeploymentSettings": None,
    "initialScopeUris": []
},
    {"type": SERVER_PROFILE_TEMPLATE_TYPE,
     "serverProfileDescription": "DL160 SPT with Raid 0 LS",
     "serverHardwareTypeUri": "SHT:DL160 Gen10 1",
     "enclosureGroupUri": "",
     "serialNumberType": "Physical",
     "macType": "Physical",
     "wwnType": "Physical",
     "name": "DL160 SPT",
     "description": "DL160 SPT",
     "affinity": None,
     "connectionSettings": {"connections": [], "manageConnections": False},
     "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
     "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
     "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                  "forceInstallFirmware": False, "firmwareInstallType": None,
                  "firmwareActivationType": "Immediate"},
     "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL120"}]},
     "hideUnusedFlexNics": True,
     "iscsiInitiatorNameType": "AutoGenerated",
     "localStorage": {
         "sasLogicalJBODs": [],
         "controllers": [{
             "logicalDrives": [{
                 "name": "rd0",
                 "raidLevel": "RAID0",
                 "bootable": True,
                 "numPhysicalDrives": 1,
                 "driveTechnology": "SasHdd",
                 "sasLogicalJBODId": None}
             ],
             "deviceSlot": "Embedded",
             "mode": "Mixed",
             "initialize": True}
         ]},
     "sanStorage": None,
     "osDeploymentSettings": None,
     "initialScopeUris": []
     },
    {"type": SERVER_PROFILE_TEMPLATE_TYPE,
     "serverProfileDescription": "DL180 FPT with Raid 0 LS",
     "serverHardwareTypeUri": "SHT:DL180 Gen10 1",
     "enclosureGroupUri": "",
     "serialNumberType": "Physical",
     "macType": "Physical",
     "wwnType": "Physical",
     "name": "DL180 SPT",
     "description": "DL180 SPT",
     "affinity": None,
     "connectionSettings": {"connections": [], "manageConnections": False},
     "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
     "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
     "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                  "forceInstallFirmware": False, "firmwareInstallType": None,
                  "firmwareActivationType": "Immediate"},
     "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL120"}]},
     "hideUnusedFlexNics": True,
     "iscsiInitiatorNameType": "AutoGenerated",
     "localStorage": {
         "sasLogicalJBODs": [],
         "controllers": [{
             "logicalDrives": [{
                 "name": "rd0",
                 "raidLevel": "RAID0",
                 "bootable": True,
                 "numPhysicalDrives": 1,
                 "driveTechnology": "SasHdd",
                 "sasLogicalJBODId": None}
             ],
             "deviceSlot": "Embedded",
             "mode": "Mixed",
             "initialize": True}
         ]},
     "sanStorage": None,
     "osDeploymentSettings": None,
     "initialScopeUris": []
     },
    # {"type": SERVER_PROFILE_TEMPLATE_TYPE,
    #  "serverProfileDescription": "DL360 SPT with Raid 0 LS",
    #  "serverHardwareTypeUri": "SHT:DL360 Gen10 1",
    #  "enclosureGroupUri": "",
    #  "serialNumberType": "Physical",
    #  "macType": "Physical",
    #  "wwnType": "Physical",
    #  "name": "DL360 SPT",
    #  "description": "DL360 SPT",
    #  "affinity": None,
    #  "connectionSettings": {"connections": [], "manageConnections": False},
    #  "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    #  "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    #  "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
    #               "forceInstallFirmware": False, "firmwareInstallType": None,
    #               "firmwareActivationType": "Immediate"},
    #  "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL120"}]},
    #  "hideUnusedFlexNics": True,
    #  "iscsiInitiatorNameType": "AutoGenerated",
    #  "localStorage": {
    #      "sasLogicalJBODs": [],
    #      "controllers": [{
    #          "logicalDrives": [{
    #              "name": "rd0",
    #              "raidLevel": "RAID0",
    #              "bootable": True,
    #              "numPhysicalDrives": 1,
    #              "driveTechnology": "SasHdd",
    #              "sasLogicalJBODId": None}
    #          ],
    #          "deviceSlot": "Embedded",
    #          "mode": "Mixed",
    #          "initialize": True}
    #      ]},
    #  "sanStorage": None,
    #  "osDeploymentSettings": None,
    #  "initialScopeUris": []
    #  }
]

DL_gen10_server_profiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": "SH:" + DL180_name,
        "serverHardwareTypeUri": "SHT:DL180 Gen10 1",
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "DL180 profile",
        "description": "",
        "affinity": None,
        "connectionSettings": {
            "connections": []},
        "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
        "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
        "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                     "firmwareInstallType": None, "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
        "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL180"}]},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {"sasLogicalJBODs": [],
                         "controllers": [{"logicalDrives": [{
                             "name": "rd0",
                             "raidLevel": "RAID0",
                             "bootable": False,
                             "numPhysicalDrives": 1,
                             "driveTechnology": "SataHdd",
                             "sasLogicalJBODId": None,
                             "driveNumber": None}],
                             "deviceSlot": "Embedded",
                             "mode": "Mixed",
                             "initialize": True,
                             "importConfiguration": False}]},
        "sanStorage": None,
        "initialScopeUris": []
    }]

# RIS nodes
create_ris_node_DL180 = {
    "server": DL180_name,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/0/LogicalDrives/1",
    "validate": {
        "CapacityMiB": 476908,
        "Description": "HPE Smart Storage Logical Drive View",
        "Id": "1",
        "InterfaceType": "SATA",
        "LegacyBootPriority": "None",
        "LogicalDriveEncryption": False,
        "LogicalDriveNumber": 1,
        "LogicalDriveType": "Data",
        "MediaType": "HDD",
        "Name": "HpeSmartStorageLogicalDrive",
        "Raid": "0",
        "Status": {"Health": "OK", "State": "Enabled"},
        "StripeSizeBytes": 262144,
    }
}

ris_nodes_create = [create_ris_node_DL180]

edit_DL_gen10_profiles = [{
    "type": SERVER_PROFILE_TYPE,
    "name": "DL180 profile",
    "description": "edited",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + DL180_name,
    "serverHardwareTypeUri": "SHT:DL180 Gen10 1",
    "affinity": None,
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                 "firmwareInstallType": None, "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
    "macType": "Physical",
    "wwnType": "Physical",
    "serialNumberType": "Physical",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {"connections": []},
    "bootMode": {"manageMode": True, "mode": "BIOS", "secureBoot": "Unmanaged"},
    "boot": {"manageBoot": True, "order": ["CD", "USB", "HardDisk", "PXE"]},
    "bios": {"manageBios": True,
             "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL180"}]},
    "localStorage": {"sasLogicalJBODs": [],
                     "controllers": [{"logicalDrives":
                                      [{"name": "new-rd1",
                                        "raidLevel": "RAID1",
                                        "bootable": False,
                                        "numPhysicalDrives": 2,
                                        "driveTechnology": "SataHdd",
                                        "sasLogicalJBODId": None,
                                        "driveNumber": None}],
                                      "deviceSlot": "Embedded",
                                      "mode": "Mixed",
                                      "initialize": True,
                                      "importConfiguration": False}]},
    "sanStorage": None,
    "osDeploymentSettings": None,
    "refreshState": "NotRefreshing"}]

DL_gen10_server_profiles_imported_drives = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": "SH:" + DL180_name,
        "serverHardwareTypeUri": "SHT:DL180 Gen10 1",
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "DL180-importedDrives",
        "description": "",
        "affinity": None,
        "connectionSettings": {"connections": []},
        "boot": {"manageBoot": False},
        "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Unmanaged", "pxeBootPolicy": "Auto"},
        "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, },
        "bios": {"manageBios": False, "overriddenSettings": []},
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {"sasLogicalJBODs": [], "controllers": [
            {
                "logicalDrives": [],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": False,
                "importConfiguration": True
            }]},
        "sanStorage": None,
    }]

# RIS nodes
import_ris_node_DL180 = {
    "server": DL180_name,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/0/LogicalDrives/1",
    "validate": {
        "CapacityMiB": 476908,
        "Description": "HPE Smart Storage Logical Drive View",
        "Id": "1",
        "InterfaceType": "SATA",
        "LegacyBootPriority": "None",
        "LogicalDriveEncryption": False,
        "LogicalDriveNumber": 1,
        "LogicalDriveType": "Data",
        "MediaType": "HDD",
        "Name": "HpeSmartStorageLogicalDrive",
        "Raid": "1",
        "Status": {"Health": "OK", "State": "Enabled"},
        "StripeSizeBytes": 262144,
    }
}

ris_nodes_after_import = [import_ris_node_DL180]

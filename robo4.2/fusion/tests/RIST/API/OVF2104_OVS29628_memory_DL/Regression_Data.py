admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

# Resource types for X-API-Version=1000
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
SERVER_HARDWARE_TYPE = 'server-hardware-10'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# DL
DL120_name = 'WIN-6H9DOGLP0AB'
DL120_IP = '16.114.212.92'
DL160_name = 'fvtdl92-ilo'
DL160_IP = '16.114.212.92'
DL180_name = 'ILO7CE651P1TU'
DL180_IP = '16.114.212.95'
DL360_name = 'ILOCN763807XQ'
DL360_IP = '16.114.212.49'
DL380_name = 'fvtdl43-ilo'
DL380_IP = '16.114.212.43'

Gen10_DLs_with_profiles = [DL160_name]
Gen10_DLs_names = [DL120_name, DL160_name, DL180_name, DL360_name, DL380_name]

ris_node160 = {"server": DL160_name,
               "username": "Administrator",
               "password": "hpvse123",
               "path": "/redfish/v1/Systems/1/Memory/", }
ris_node180 = {"server": DL180_name,
               "username": "Administrator",
               "password": "hpvse123",
               "path": "/redfish/v1/Systems/1/Memory/", }
ris_nodes = [ris_node160, ris_node180]

Gen10_DLs = [{'name': DL160_name,
              'hostname': DL160_IP,
              'licensingIntent': 'OneViewNoiLO',
              'username': 'Administrator',
              'password': 'hpvse123',
              'force': True,
              'configurationState': 'Managed'},
             {'name': DL180_name,
              'hostname': DL180_IP,
              'licensingIntent': 'OneViewNoiLO',
              'username': 'Administrator',
              'password': 'hpvse123',
              'force': True,
              'configurationState': 'Managed'}]

verify_DL_gen10_servers = [
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
]

DL_gen10_profile_templates = [{
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
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
}]

gen10_DL_server_profiles = [{
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
    "connectionSettings": {"connections": []},
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
}, {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": "SH:" + DL160_name,
    "serverHardwareTypeUri": "SHT:DL160 Gen10 1",
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "DL160 profile",
    "description": "",
    "affinity": None,
    "connectionSettings": {"connections": []},
    "boot": {"manageBoot": False},
    "bootMode": {"manageMode": True, "mode": "UEFI", "secureBoot": "Disabled", "pxeBootPolicy": "Auto"},
    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                 "firmwareInstallType": None, "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
    "bios": {"manageBios": True, "overriddenSettings": [{"id": "CustomPostMessage", "value": "DL160"}]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": None,
    "initialScopeUris": []
}]

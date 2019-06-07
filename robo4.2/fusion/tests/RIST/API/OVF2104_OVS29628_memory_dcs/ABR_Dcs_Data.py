admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

# Resource types for X-API-Version=1000
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV5'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

Time_and_Locale = {'type': TIME_AND_LOCALE_TYPE,
                   'locale': 'en_US.UTF-8',
                   'timezone': 'UTC',
                   'ntpServers': [
                       '16.110.135.123'
                   ]
                   }
# Enclosures
ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1
ENC2DEBAY1 = '%s, bay 1' % ENC2
ENC3DEBAY1 = '%s, bay 1' % ENC3

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY11 = '%s, bay 11' % ENC1
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY4 = '%s, bay 4' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2
ENC2SHBAY11 = '%s, bay 11' % ENC2
ENC3SHBAY3 = '%s, bay 3' % ENC3
ENC3SHBAY4 = '%s, bay 4' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3
ENC3SHBAY6 = '%s, bay 6' % ENC3
ENC3SHBAY7 = '%s, bay 7' % ENC3
ENC3SHBAY8 = '%s, bay 8' % ENC3
ENC3SHBAY11 = '%s, bay 11' % ENC3

enclosures = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, },
    {"type": ENCLOSURE_TYPE, "name": ENC2, },
    {"type": ENCLOSURE_TYPE, "name": ENC3, },
]

licenses = [
    {
        'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
]
san_managers = [
    {"connectionInfo": [
        {'name': 'Type',
         'value': 'Brocade Network Advisor'},
        {"name": "Host",
            "displayName": "Host",
            "required": True,
            "value": "16.125.65.9",
            "valueFormat": "IPAddressOrHostname",
            "valueType": "String"},
        {"name": "Port",
            "displayName": "Port",
            "required": True,
            "value": 5989,
            "valueFormat": "None",
            "valueType": "Integer"},
        {"name": "Username",
            "displayName": "Username",
            "required": True,
            "value": "Administrator",
            "valueFormat": "None",
            "valueType": "String"},
        {"name": "Password",
            "displayName": "Password",
            "required": True,
            "value": "password",
            "valueFormat": "SecuritySensitive",
            "valueType": "String"},
        {"name": "UseSsl",
            "displayName": "UseSsl",
            "required": True,
            "value": True,
            "valueFormat": "None",
            "valueType": "Boolean"},
    ], },
]


sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, },
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1, },
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4, },
]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC2ICBAY6, },
]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]
fc_networks = [
    {'name': 'FA1',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': ''},
    {'name': 'FA2',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': ''},
]
network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100'],
                 'nativeNetworkUri': 'net100'},
                ]

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
               'us_tagged': {'name': 'us-tagged',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['net100', 'net300'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
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
               }

ligs = [{'name': LIG_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(), uplink_sets['us_tunnel'].copy(), ],
         }
        ]
sasligs = [{"name": 'SASLIG1',  # Dual SAS switch
            "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'}]}
           ]

egs = [{'name': 'EG1',
        'type': ENCLOSURE_GROUP_TYPE,
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
        [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
         {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
         {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
         ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]

les = [{'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}
       ]

# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3

# Sas Interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

sy660_gen10_backplane_templates = [{
    "type": SERVER_PROFILE_TYPE,
    "serverProfileDescription": "",
    "serverHardwareTypeUri": "SHT:SY 660 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10:4:HPE Smart Array P416ie-m SR G10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "XL-bay6-gen10-condor-backplane-profile-template",
    "description": "XL-bay6-gen10-condor-backplane-profile-template",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [{
            "id": 1,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Auto",
            "requestedMbps": "2500",
            "networkUri": "ETH:net100",
            "requestedVFs": "0",
            "ipv4": {
                "ipAddressSource": None,
                "subnetMask": None,
                "gateway": None
            }
        }, {
            "id": 2,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Auto",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "requestedVFs": "0",
            "ipv4": {
                "ipAddressSource": None,
                "subnetMask": None,
                "gateway": None
            }
        }],
        "manageConnections": True
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
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
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "hideUnusedFlexNics": True,
    "iscsiInitiatorNameType": "AutoGenerated",
    "localStorage": {
        "sasLogicalJBODs": [{
            "id": 1,
            "deviceSlot": "Mezz 1",
            "name": "mezz1-ljb",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd"
        }, {
            "id": 2,
            "deviceSlot": "Mezz 1",
            "name": "external-mezz1-rd0-ld",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd"
        }, {
            "id": 3,
            "deviceSlot": "Mezz 4",
            "name": "external-mezz4-ljb",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd"
        }, {
            "id": 4,
            "deviceSlot": "Mezz 4",
            "name": "external-mezz4-rd0-ld",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd"
        }],
        "controllers": [{
            "logicalDrives": [{
                "name": "internal-ld",
                "raidLevel": "RAID1",
                "bootable": False,
                "numPhysicalDrives": 2,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODId": None
            }, {
                "name": None,
                "raidLevel": "RAID0",
                "bootable": True,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 2
            }],
            "deviceSlot": "Mezz 1",
            "mode": "Mixed",
            "initialize": True
        }, {
            "logicalDrives": [{
                "name": None,
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 4
            }],
            "deviceSlot": "Mezz 4",
            "mode": "Mixed",
            "initialize": False
        }]
    },
    "sanStorage": None,
    "osDeploymentSettings": None
}]

server_profile = [{
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": "SH:" + ENC1 + ", bay 6",
    "serverProfileTemplateUri": "SPT:XL-bay6-gen10-condor-backplane-profile-template",
    "serverHardwareTypeUri": "SHT:SY 660 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10:4:HPE Smart Array P416ie-m SR G10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": ENC1 + ", bay6-gen10-condor-backplane-profile-from-template",
    "description": "With Back plane connections to Mezz1",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [{
            "id": 1,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:net100",
            "requestedVFs": "0",
            "ipv4": {}
        }, {
            "id": 2,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Mezz 3:2-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "requestedVFs": "0",
            "ipv4": {}
        }]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareScheduleDateTime": "",
        "firmwareActivationType": "Immediate"
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [{
            "id": 1,
            "deviceSlot": "Mezz 1",
            "name": "mezz1-ljb",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd",
            "sasLogicalJBODUri": None,
            "status": "Unknown"
        }, {
            "id": 2,
            "deviceSlot": "Mezz 1",
            "name": "external-mezz1-rd0-ld",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd",
            "sasLogicalJBODUri": None,
            "status": "Unknown"
        }, {
            "id": 3,
            "deviceSlot": "Mezz 4",
            "name": "external-mezz4-ljb",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd",
            "sasLogicalJBODUri": None,
            "status": "Unknown"
        }, {
            "id": 4,
            "deviceSlot": "Mezz 4",
            "name": "external-mezz4-rd0-ld",
            "numPhysicalDrives": 1,
            "driveMinSizeGB": 146,
            "driveMaxSizeGB": 146,
            "driveTechnology": "SasHdd",
            "sasLogicalJBODUri": None,
            "status": "Unknown"
        }],
        "controllers": [{
            "logicalDrives": [{
                "name": None,
                "raidLevel": "RAID0",
                "bootable": True,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 2,
                "driveNumber": None
            }, {
                "name": "internal-ld",
                "raidLevel": "RAID1",
                "bootable": False,
                "numPhysicalDrives": 2,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODId": None,
                "driveNumber": None
            }],
            "deviceSlot": "Mezz 1",
            "mode": "Mixed",
            "initialize": True,
            "importConfiguration": False
        }, {
            "logicalDrives": [{
                "name": None,
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 4,
                "driveNumber": None
            }],
            "deviceSlot": "Mezz 4",
            "mode": "Mixed",
            "initialize": False,
            "importConfiguration": False
        }]
    },
    "sanStorage": None
}]

# RIS nodes
create_ris_node_bay6_drive1 = {
    "server": ENC1SHBAY6,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/0/",
    "validate": {
        "BlockSizeBytes": 512,
        "CapacityGB": 240,
        "CapacityLogicalBlocks": 468862128,
        "CapacityMiB": 228936,
        "CarrierApplicationVersion": "11",
        "CarrierAuthenticationStatus": "OK",
        "Description": "HPE Smart Storage Disk Drive View",
        "DiskDriveStatusReasons": ["None"],
        "DiskDriveUse": "Raw",
        "EncryptedDrive": False,
        "FirmwareVersion": {"Current": {"VersionString": "4IWTHPG2"}},
        "Id": "0",
        "InterfaceSpeedMbps": 6000,
        "InterfaceType": "SATA",
        "Location": "3I:2:1",
        "LocationFormat": "ControllerPort:Box:Bay",
        "MediaType": "SSD",
        "Model": "VK0240GEYJQ",
        "Name": "HpeSmartStorageDiskDrive",
        "PowerOnHours": 30,
        "SSDEnduranceUtilizationPercentage": 0,
        "SerialNumber": "BTWA714307K3240AGN",
        "Status": {"Health": "OK", "State": "Enabled"}
    }
}

create_ris_node_bay6_drive2 = {
    "server": ENC1SHBAY6,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/4/",
    "validate": {
        "BlockSizeBytes": 512,
        "CapacityGB": 72,
        "CapacityLogicalBlocks": 143374738,
        "CapacityMiB": 70007,
        "CarrierApplicationVersion": "11",
        "CarrierAuthenticationStatus": "OK",
        "Description": "HPE Smart Storage Disk Drive View",
        "DiskDriveStatusReasons": ["None"],
        "DiskDriveUse": "Data",
        "EncryptedDrive": False,
        "FirmwareVersion": {"Current": {"VersionString": "HPD0"}},
        "Id": "4",
        "InterfaceSpeedMbps": 3000,
        "InterfaceType": "SAS",
        "Location": "4I:1:1",
        "LocationFormat": "ControllerPort:Box:Bay",
        "MediaType": "HDD",
        "Model": "DG072A9BB7",
        "Name": "HpeSmartStorageDiskDrive",
        "PowerOnHours": None,
        "RotationalSpeedRpm": 0,
        "SSDEnduranceUtilizationPercentage": None,
        "SerialNumber": "B365P750TNFR0722",
        "Status": {"Health": "OK", "State": "Enabled"}
    }
}

create_ris_node_bay6_drive3 = {
    "server": ENC1SHBAY6,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/6/",
    "validate": {
        "BlockSizeBytes": 512,
        "CapacityGB": 72,
        "CapacityLogicalBlocks": 143374738,
        "CapacityMiB": 70007,
        "CarrierApplicationVersion": "11",
        "CarrierAuthenticationStatus": "OK",
        "Description": "HPE Smart Storage Disk Drive View",
        "DiskDriveStatusReasons": ["None"],
        "DiskDriveUse": "Data",
        "EncryptedDrive": False,
        "FirmwareVersion": {"Current": {"VersionString": "HPD3"}},
        "Id": "6",
        "InterfaceSpeedMbps": 3000,
        "InterfaceType": "SAS",
        "Location": "4I:1:2",
        "LocationFormat": "ControllerPort:Box:Bay",
        "MediaType": "HDD",
        "Model": "DH072BAAKN",
        "Name": "HpeSmartStorageDiskDrive",
        "PowerOnHours": None,
        "RotationalSpeedRpm": 0,
        "SSDEnduranceUtilizationPercentage": None,
        "SerialNumber": "BV05P8501MP30819",
        "Status": {"Health": "OK", "State": "Enabled"}
    }
}
create_ris_node_bay6_drive4 = {
    "server": ENC1SHBAY6,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/8/",
    "validate": {
        "BlockSizeBytes": 512,
        "CapacityGB": 146,
        "CapacityLogicalBlocks": 286749488,
        "CapacityMiB": 140014,
        "CarrierApplicationVersion": "11",
        "CarrierAuthenticationStatus": "OK",
        "Description": "HPE Smart Storage Disk Drive View",
        "DiskDriveStatusReasons": ["None"],
        "DiskDriveUse": "Raw",
        "EncryptedDrive": False,
        "FirmwareVersion": {"Current": {"VersionString": "HPDD"}},
        "Id": "8",
        "InterfaceSpeedMbps": 6000,
        "InterfaceType": "SAS",
        "Location": "01:1:31",
        "LocationFormat": "ControllerPort:Box:Bay",
        "MediaType": "HDD",
        "Model": "EH0146FARWD",
        "Name": "HpeSmartStorageDiskDrive",
        "PowerOnHours": None,
        "RotationalSpeedRpm": 15000,
        "SSDEnduranceUtilizationPercentage": None,
        "SerialNumber": "PLXSNWHE",
        "Status": {"Health": "OK", "State": "Enabled"}
    }
}
create_ris_node_bay6_drive5 = {
    "server": ENC1SHBAY6,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/redfish/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/9/",
    "validate": {
        "BlockSizeBytes": 512,
        "CapacityGB": 146,
        "CapacityLogicalBlocks": 286749488,
        "CapacityMiB": 140014,
        "CarrierApplicationVersion": "11",
        "CarrierAuthenticationStatus": "OK",
        "Description": "HPE Smart Storage Disk Drive View",
        "DiskDriveStatusReasons": ["None"],
        "DiskDriveUse": "Data",
        "EncryptedDrive": False,
        "FirmwareVersion": {"Current": {"VersionString": "HPD5"}},
        "Id": "9",
        "InterfaceSpeedMbps": 6000,
        "InterfaceType": "SAS",
        "Location": "01:1:32",
        "LocationFormat": "ControllerPort:Box:Bay",
        "MediaType": "HDD",
        "Model": "EH0146FBQDC",
        "Name": "HpeSmartStorageDiskDrive",
        "PowerOnHours": None,
        "RotationalSpeedRpm": 15000,
        "SSDEnduranceUtilizationPercentage": None,
        "SerialNumber": "6XM4E1010000M528K1Q9",
        "Status": {"Health": "OK", "State": "Enabled"}
    }
}

ris_nodes_create = [create_ris_node_bay6_drive1, create_ris_node_bay6_drive2, create_ris_node_bay6_drive3, create_ris_node_bay6_drive4, create_ris_node_bay6_drive5]

edit_profile_add_moreLS = {
    "type": SERVER_PROFILE_TYPE,
    "name": ENC1 + ", bay6-gen10-condor-backplane-profile-from-template",
    "description": "",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC1 + ", bay 6",
    "serverHardwareTypeUri": "SHT:SY 660 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10:4:HPE Smart Array P416ie-m SR G10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC1,
    "enclosureBay": 6,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareScheduleDateTime": "",
        "firmwareActivationType": "Immediate"
    },
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {
        "connections": [{
            "id": 1,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:net100",
            "requestedVFs": "0",
            "ipv4": {},
        }, {
            "id": 2,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Mezz 3:2-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "requestedVFs": "0",
            "ipv4": {},
        }]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Unmanaged"},
    "bios": {"manageBios": False, "overriddenSettings": []},
    "localStorage": {
        "sasLogicalJBODs": [
            {"id": 1,
             "deviceSlot": "Mezz 1",
             "name": "mezz1-ljb",
             "numPhysicalDrives": 1,
             "driveMinSizeGB": 146,
             "driveMaxSizeGB": 146,
             "driveTechnology": "SasHdd",
             "eraseData": False,
             "sasLogicalJBODUri": "SASLJBOD:mezz1-ljb",
             "status": "OK"
             }, {
                "id": 2,
                "deviceSlot": "Mezz 1",
                "name": "external-mezz1-rd0-ld",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "sasLogicalJBODUri": "SASLJBOD:external-mezz1-rd0-ld",
                "status": "OK"
            }, {
                "id": 5,
                "deviceSlot": "Mezz 1",
                "name": "mezz1-extra-ljb",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                # "sasLogicalJBODUri": None
            }, {
                "id": 6,
                "deviceSlot": "Mezz 1",
                "name": "mezz1-extra-external-rd0",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                # "sasLogicalJBODUri": None
            }, {
                "id": 3,
                "deviceSlot": "Mezz 4",
                "name": "external-mezz4-ljb",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "sasLogicalJBODUri": "SASLJBOD:external-mezz4-ljb",
                "status": "OK"
            }, {
                "id": 4,
                "deviceSlot": "Mezz 4",
                "name": "external-mezz4-rd0-ld",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                "sasLogicalJBODUri": "SASLJBOD:external-mezz4-rd0-ld",
                "status": "OK"
            }, {
                "id": 7,
                "deviceSlot": "Mezz 4",
                "name": "mezz4-extra-rd0",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                # "sasLogicalJBODUri": None
            },
            {
                "id": 8,
                "deviceSlot": "Mezz 4",
                "name": "mezz4-extra-ljb",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
                # "sasLogicalJBODUri": None
            }],
        "controllers": [{
            "logicalDrives": [{
                "name": None,
                "raidLevel": "RAID0",
                "bootable": True,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 2,
                "driveNumber": None
            },
                {
                "name": "internal-ld",
                "raidLevel": "RAID1",
                "bootable": False,
                "numPhysicalDrives": 2,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODId": None,
                "driveNumber": None
            },
                {
                "name": None,
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 6,
                "driveNumber": None
            }],
            "deviceSlot": "Mezz 1",
            "mode": "Mixed",
            "initialize": True,
            "importConfiguration": False
        },
            {
            "logicalDrives": [{
                "name": None,
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 4,
                "driveNumber": None
            },
                {
                "name": None,
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": None,
                "driveTechnology": None,
                "sasLogicalJBODId": 7,
                "driveNumber": None
            }],
            "deviceSlot": "Mezz 4",
            "mode": "Mixed",
            "initialize": False,
            "importConfiguration": False}]
    },
    "sanStorage": None,
    "osDeploymentSettings": None,
    "refreshState": "NotRefreshing"
}

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

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
ENC1DEBAY3 = '%s, bay 3' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

ris_node1 = {"server": ENC1SHBAY6,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node2 = {"server": ENC1SHBAY8,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node3 = {"server": ENC2SHBAY6,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node4 = {"server": ENC2SHBAY7,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node5 = {"server": ENC2SHBAY8,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_nodes = [ris_node1, ris_node2, ris_node3, ris_node4, ris_node5]
# ris_nodes_in_profiles = [ris_node3, ris_node5]
ris_nodes_in_profiles = [ris_node2, ris_node3]

enclosures = [
    {"type": "EnclosureV400", "name": ENC1, },
    {"type": "EnclosureV400", "name": ENC2, },
    {"type": "EnclosureV400", "name": ENC3, },
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
     'type': 'ethernet-networkV4',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': 'ethernet-networkV4',
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': 'ethernet-networkV4',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': 'ethernet-networkV4',
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

network_sets = [{'name': 'NS1', 'type': 'network-setV4 ', 'networkUris': ['net100'], 'nativeNetworkUri': 'net100'}, ]

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
                               'logicalPortConfigInfos':
                                   [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                    {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}, ]
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
         'type': 'logical-interconnect-groupV4',
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
         'uplinkSets': [uplink_sets['us_untagged'].copy(),
                        uplink_sets['us_tagged'].copy(), uplink_sets['us_tunnel'].copy(), ],
         }
        ]
sasligs = [{"name": 'SASLIG1',  # Dual SAS switch
            "type": "sas-logical-interconnect-group",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'}]}
           ]

egs = [{'name': 'EG1',
        'type': 'EnclosureGroupV300',
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

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

gen10_server_profiles = [
    {
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:" + ENC1 + ", bay 8",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": ENC1 + ", bay 8-gen10-Harrier with LS and JBODs",
        "description": "",
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
                "ipv4": {},
            }, {
                "id": 2,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:net300",
                "requestedVFs": "0",
                "ipv4": {},
            }]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{
                "id": "CustomPostMessage",
                "value": "Harrier"
            }]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [{
                "id": 1,
                "deviceSlot": "Mezz 1",
                "name": "ljb1",
                "numPhysicalDrives": 1,
                "driveMinSizeGB": 50,
                "driveMaxSizeGB": 500,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODUri": None
            }],
            "controllers": [{
                "logicalDrives": [{
                    "name": "rd0",
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": 1,
                    "driveTechnology": "SasHdd",
                    "sasLogicalJBODId": None,
                    "driveNumber": None
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False
            }]
        },
        "sanStorage": None
    },
    {
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:" + ENC2 + ", bay 6",
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:3:Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": ENC2 + ", bay 6-gen10Fullheight",
        "description": "",
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
                "ipv4": {},
            }, {
                "id": 2,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:net300",
                "requestedVFs": "0",
                "ipv4": {},
            }]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{
                "id": "CustomPostMessage",
                "value": "Harrier"
            }]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {"sasLogicalJBODs": [], "controllers": []},
        "sanStorage": None
    }]

edit_gen10_profile_boot_bios = {
    "type": "ServerProfileV9",
    "name": "CN754406XL, bay 8-gen10-Harrier with LS and JBODs",
    "description": "",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC1 + ", bay 8",
    "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC1,
    "enclosureBay": 8,
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
            "boot": {
                "iscsi": {}
            }
        }, {
            "id": 2,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Mezz 3:2-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "requestedVFs": "0",
            "ipv4": {},
            "boot": {
                "iscsi": {}
            }
        }]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bios": {
        "manageBios": True,
        "overriddenSettings": [{
            "id": "CustomPostMessage",
            "value": "Harrier-edit"
        }]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [{
            "logicalDrives": [{
                "name": "rd0",
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": 1,
                "driveTechnology": "SasHdd",
                "sasLogicalJBODId": None,
                "driveNumber": None,
            }],
            "deviceSlot": "Embedded",
            "mode": "Mixed",
            "initialize": True,
            "importConfiguration": False
        }]
    },
    "sanStorage": None,
    "osDeploymentSettings": None,
    "refreshState": "NotRefreshing",
}

move_profile_from_enc1_XL_Bay8_harrier_to_enc2_R6_Bay8_Harrier = {
    "type": "ServerProfileV9",
    "name": "CN754406XL, bay 8-gen10-Harrier with LS and JBODs",
    "description": "moved to enc2 R6 bay8",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC2 + ", bay 8",
    "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "enclosureUri": 'ENC:' + ENC2,
    "enclosureBay": 8,
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
    "connectionSettings": {
        "connections": [{
            "id": 1,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Auto",
            "requestedMbps": "2500",
            "networkUri": "ETH:net100",
            "requestedVFs": "0",
            "ipv4": {},
            "boot": {
                "priority": "NotBootable",
                "iscsi": {}
            }
        }, {
            "id": 2,
            "name": "",
            "functionType": "Ethernet",
            "portId": "Auto",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "requestedVFs": "0",
            "ipv4": {},
            "boot": {
                "priority": "NotBootable",
                "iscsi": {}
            }
        }]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [{
            "logicalDrives": [{
                "name": "rd0",
                "raidLevel": "RAID0",
                "bootable": False,
                "numPhysicalDrives": 1,
                "driveTechnology": "SataSsd",
                "sasLogicalJBODId": None,
                "driveNumber": None,
            }],
            "deviceSlot": "Embedded",
            "mode": "Mixed",
            "initialize": True,
            "importConfiguration": False
        }]
    },
    "sanStorage": None,
    "osDeploymentSettings": None,
    "refreshState": "NotRefreshing",
}


subresources = {"memory": {
    "type": "SubResourceV1",
    "uri": "/rest/server-hardware/34353736-323130303645/Memory",
    "modified": "2017-12-12T10:15:48.354Z",
    "state": "collected",
    "eTag": "eb1324689w",
    "count": 24,
    "data": [{
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm1",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 1",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
                "Channel": 6,
                "MemoryController": 2,
                "Slot": 1,
                "Socket": 1
        },
        "MemoryMedia": ["DRAM"],
        "MemoryType": "DRAM",
        "Name": "proc1dimm1",
        "Oem": {
                "Hpe": {
                    "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                    "DIMMStatus": "NotPresent",
                    "MinimumVoltageVoltsX10": 0}
        },
        "RankCount": None,
        "Status": {"Health": "OK", "State": "Absent"},
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm2",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 2",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 6,
            "MemoryController": 2,
            "Slot": 2,
            "Socket": 1
        },
        "MemoryMedia": ["DRAM"],
        "MemoryType": "DRAM",
        "Name": "proc1dimm2",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {"Health": "OK", "State": "Absent"},
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm3",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 3",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 5,
            "MemoryController": 2,
            "Slot": 3,
            "Socket": 1
        },
        "MemoryMedia": ["DRAM"],
        "MemoryType": "DRAM",
        "Name": "proc1dimm3",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {"Health": "OK", "State": "Absent"},
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm4",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 4",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 5,
            "MemoryController": 2,
            "Slot": 4,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm4",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm5",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 5",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 4,
            "MemoryController": 2,
            "Slot": 5,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm5",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm6",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 6",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 4,
            "MemoryController": 2,
            "Slot": 6,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm6",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm7",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 7",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 1,
            "MemoryController": 1,
            "Slot": 7,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm7",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm8",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 8",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 1,
            "MemoryController": 1,
            "Slot": 8,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm8",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm9",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 9",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 2,
            "MemoryController": 1,
            "Slot": 9,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm9",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm10",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 10",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 2,
            "MemoryController": 1,
            "Slot": 10,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm10",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm11",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 11",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 3,
            "MemoryController": 1,
            "Slot": 11,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm11",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc1dimm12",
        "BaseModuleType": "RDIMM",
        "BusWidthBits": 72,
        "CapacityMiB": 8192,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 1 DIMM 12",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 3,
            "MemoryController": 1,
            "Slot": 12,
            "Socket": 1
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc1dimm12",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "GoodInUse",
                "MinimumVoltageVoltsX10": 12
            }
        },
        "OperatingSpeedMhz": 2666,
        "RankCount": 1,
        "Status": {
            "Health": "OK",
            "State": "Enabled"
        },
        "VendorID": "44288"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm1",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 1",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 3,
            "MemoryController": 3,
            "Slot": 1,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm1",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm2",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 2",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 3,
            "MemoryController": 3,
            "Slot": 2,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm2",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm3",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 3",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 2,
            "MemoryController": 3,
            "Slot": 3,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm3",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm4",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 4",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 2,
            "MemoryController": 3,
            "Slot": 4,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm4",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm5",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 5",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 1,
            "MemoryController": 3,
            "Slot": 5,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm5",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm6",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 6",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 1,
            "MemoryController": 3,
            "Slot": 6,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm6",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm7",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 7",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 4,
            "MemoryController": 4,
            "Slot": 7,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm7",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm8",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 8",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 4,
            "MemoryController": 4,
            "Slot": 8,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm8",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm9",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 9",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 5,
            "MemoryController": 4,
            "Slot": 9,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm9",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm10",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 10",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 5,
            "MemoryController": 4,
            "Slot": 10,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm10",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm11",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 11",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 6,
            "MemoryController": 4,
            "Slot": 11,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm11",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    }, {
        "@odata.type": "#Memory.v1_1_0.Memory",
        "Id": "proc2dimm12",
        "BusWidthBits": 72,
        "CapacityMiB": 0,
        "DataWidthBits": 64,
        "DeviceLocator": "PROC 2 DIMM 12",
        "ErrorCorrection": "MultiBitECC",
        "MemoryDeviceType": "DDR4",
        "MemoryLocation": {
            "Channel": 6,
            "MemoryController": 4,
            "Slot": 12,
            "Socket": 2
        },
        "MemoryMedia": [
            "DRAM"
        ],
        "MemoryType": "DRAM",
        "Name": "proc2dimm12",
        "Oem": {
            "Hpe": {
                "@odata.type": "#HpeMemoryExt.v2_1_0.HpeMemoryExt",
                "DIMMStatus": "NotPresent",
                "MinimumVoltageVoltsX10": 0
            }
        },
        "RankCount": None,
        "Status": {
            "Health": "OK",
            "State": "Absent"
        },
        "VendorID": "0"
    },

    ]},
    "memoryList": {
    "type": "SubResourceV1",
    "uri": "/rest/server-hardware/34353736-323130303645/MemoryList",
    "modified": "2017-12-12T10:15:48.354Z",
    "state": "collected",
    "count": 2,
    "data": [
            {
                "BoardCpuNumber": 1,
                "BoardNumberOfSockets": 12,
                "BoardOperationalFrequency": 2666,
                "BoardOperationalVoltage": 1200,
                "BoardTotalMemorySize": 8192
            }, {
                "BoardCpuNumber": 2,
                "BoardNumberOfSockets": 12,
                "BoardOperationalFrequency": 2666,
                "BoardOperationalVoltage": 1200,
                "BoardTotalMemorySize": 0
            }]},
    "advancedMemoryProtection": {
    "type": "SubResourceV1",
    "uri": "/rest/server-hardware/34353736-323130303645/AdvancedMemoryProtection",
    "modified": "2017-12-12T10:15:48.354Z",
    "state": "collected",
    "eTag": "eb1324689w",
    "count": 1,
    "data": [{
            "@odata.type": "#HpeAdvancedMemoryProtection.v2_0_0.HpeAdvancedMemoryProtection",
            "AmpModeActive": "AdvancedECC",
            "AmpModeStatus": "AdvancedECC",
            "AmpModeSupported": [
                "AdvancedECC",
                "OnlineSpareRank",
                "IntrasocketMirroring",
                "A3DC"]}]}
}

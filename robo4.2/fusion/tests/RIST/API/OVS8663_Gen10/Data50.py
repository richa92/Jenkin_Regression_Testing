from dto import *
from env_variables import *

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
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

enclosures = [
    {"type": ENCLOSURE_TYPE_400, "name": ENC1, },
    {"type": ENCLOSURE_TYPE_400, "name": ENC2, },
    {"type": ENCLOSURE_TYPE_400, "name": ENC3, },
]

licenses = {
    'licenseType': 'HPE OneView Advanced',
    'license': [{'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'}]}

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
    {
        'name': 'network-tunnel',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 0,
        'subnetUri': None,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tunnel'
    },
    {
        'name': 'network-untagged',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 1,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Untagged'
    },
    {
        'name': 'net100',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 100,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'
    },
    {
        'name': 'net300',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 300,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'
    },
]

network_sets = [{'name': 'NS1', 'type': NETWORK_SET_TYPE, 'networkUris': ['net100'], 'nativeNetworkUri': 'net100'}, ]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': CHLORIDE20, 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': CHLORIDE20, 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': CHLORIDE20, 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': CHLORIDE20, 'enclosureIndex': 3},
]

uplink_sets = {
    'us_untagged': {
        'name': 'us-untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-untagged'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {
                'enclosure': '1', 'bay': '3', 'port': 'Q1.1',
                'speed': 'Auto'
            },
            {
                'enclosure': '2', 'bay': '6', 'port': 'Q1.1',
                'speed': 'Auto'
            },
        ]
    },
    'us_tagged': {
        'name': 'us-tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net100', 'net300'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {
                'enclosure': '1', 'bay': '3', 'port': 'Q2.1',
                'speed': 'Auto'
            },
            {
                'enclosure': '2', 'bay': '6', 'port': 'Q2.1',
                'speed': 'Auto'
            },
        ]
    },
    'us_tunnel': {
        'name': 'us-tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['network-tunnel'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {
                'enclosure': '1', 'bay': '3', 'port': 'Q3.1',
                'speed': 'Auto'
            },
            {
                'enclosure': '2', 'bay': '6', 'port': 'Q3.1',
                'speed': 'Auto'
            },
        ]
    },
}

ligs = [
    {
        'name': LIG_NAME,
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
        'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(),
                       uplink_sets['us_tunnel'].copy(), ],
    }
]
sasligs = [
    {
        "name": 'SASLIG1',  # Dual SAS switch
        "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
        "enclosureType": "SY12000",
        "enclosureIndexes": [1],
        "interconnectBaySet": "1",
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': NATASHA},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': NATASHA}]
    }
]

egs = [
    {
        'name': 'EG1',
        'type': 'EnclosureGroupV300',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
            ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
    }
]

les = [
    {
        'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
    }
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

verify_gen10_servers = [
    {
        "type": SERVER_HARDWARE_10,
        "name": ENC1 + ", bay 6",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "category": "server-hardware",
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 16384,
        "migrationState": "NotApplicable",
        "model": "Synergy 660 Gen10",
        "mpModel": "iLO5",
        "mpState": "OK",
        "partNumber": "854361-001",
        "portMap": {
            "deviceSlots": [
                {
                    "deviceName": "HPE Smart Array P416ie-m SR G10",
                    "deviceNumber": 1,
                    "location": "Mezz",
                    "physicalPorts": [
                        {
                            "interconnectPort": 6,
                            "interconnectUri": "SASIC:" + ENC1 + ", interconnect 1",
                            "mac": None,
                            "physicalInterconnectPort": 6,
                            "physicalInterconnectUri": "SASIC:" + ENC1 + ", interconnect 1",
                            "portNumber": 1,
                            "type": "SAS",
                            "virtualPorts": [],
                        },
                        {
                            "interconnectPort": 6,
                            "interconnectUri": "SASIC:" + ENC1 + ", interconnect 4",
                            "mac": None,
                            "physicalInterconnectPort": 6,
                            "physicalInterconnectUri": "SASIC:" + ENC1 + ", interconnect 4",
                            "portNumber": 2,
                            "type": "SAS",
                            "virtualPorts": [],
                        }
                    ],
                    "slotNumber": 1
                },
                {
                    "deviceName": "",
                    "deviceNumber": 2,
                    "location": "Mezz",
                    "physicalPorts": [],
                    "slotNumber": 2
                },
                {
                    "deviceName": "Synergy 3820C 10/20Gb CNA",
                    "deviceNumber": 3,
                    "location": "Mezz",
                    "physicalPorts": [
                        {
                            "interconnectPort": 6,
                            "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
                            "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                            "physicalInterconnectPort": 6,
                            "physicalInterconnectUri": "IC:" + ENC1 + ", interconnect 3",
                            "portNumber": 1,
                            "type": "Ethernet",
                            "virtualPorts": [
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "a",
                                    "portNumber": 1,
                                },
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "b",
                                    "portNumber": 2,
                                },
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "c",
                                    "portNumber": 3,
                                },
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "d",
                                    "portNumber": 4,
                                }
                            ],
                        },
                        {
                            "interconnectPort": 18,
                            "interconnectUri": "IC:" + ENC2 + ", interconnect 6",
                            "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                            "physicalInterconnectPort": 6,
                            "physicalInterconnectUri": "IC:" + ENC1 + ", interconnect 6",
                            "portNumber": 2,
                            "type": "Ethernet",
                            "virtualPorts": [
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "a",
                                    "portNumber": 1,
                                },
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "b",
                                    "portNumber": 2,
                                },
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "c",
                                    "portNumber": 3,
                                },
                                {
                                    "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                    "portFunction": "d",
                                    "portNumber": 4,
                                }
                            ],
                            "wwn": None
                        }
                    ],
                    "slotNumber": 3
                },
                {
                    "deviceName": "HPE Smart Array P416ie-m SR G10",
                    "deviceNumber": 4,
                    "location": "Mezz",
                    "physicalPorts": [
                        {
                            "interconnectPort": 12,
                            "interconnectUri": "SASIC:" + ENC1 + ", interconnect 1",
                            "mac": None,
                            "physicalInterconnectPort": 12,
                            "physicalInterconnectUri": "SASIC:" + ENC1 + ", interconnect 1",
                            "portNumber": 1,
                            "type": "SAS",
                            "virtualPorts": [],
                            "wwn": "50:01:43:80:40:AA:CC:E0"
                        },
                        {
                            "interconnectPort": 12,
                            "interconnectUri": "SASIC:" + ENC1 + ", interconnect 4",
                            "mac": None,
                            "physicalInterconnectPort": 12,
                            "physicalInterconnectUri": "SASIC:" + ENC1 + ", interconnect 4",
                            "portNumber": 2,
                            "type": "SAS",
                            "virtualPorts": [],
                            "wwn": "50:01:43:80:40:AA:CC:E4"
                        }
                    ],
                    "slotNumber": 4
                },
                {
                    "deviceName": "",
                    "deviceNumber": 5,
                    "location": "Mezz",
                    "physicalPorts": [],
                    "slotNumber": 5
                },
                {
                    "deviceName": "",
                    "deviceNumber": 6,
                    "location": "Mezz",
                    "physicalPorts": [],
                    "slotNumber": 6
                }
            ]
        },
        "position": 6,
        "powerLock": False,
        "processorCoreCount": 18,
        "processorCount": 2,
        "processorSpeedMhz": 2700,
        "processorType": "Intel(R) Xeon(R) Gold 6150 CPU @ 2.70GHz",
        "refreshState": "NotRefreshing",
        "serialNumber": "CN7711000B",
        "serverGroupUri": "EG:" + EG_NAME,
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array \
                         P416ie-m SR G10:4:HPE Smart Array P416ie-m SR G10",
        "serverProfileUri": None,
        "serverSettings": None,
        "shortModel": "SY 660 Gen10",
        "status": "REGEX:(OK|WARNING)",
        "supportDataCollectionState": None,
        "supportDataCollectionType": None,
        "supportState": "NotSupported",
        "uri": "SH:" + ENC1 + ", bay 6",
        "uuid": "33343538-3136-4E43-3737-313130303042",
        "virtualSerialNumber": None,
        "virtualUuid": None
    }
]

gen10_profile_templates = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "XL-bay8-gen10-harrier-profile-template",
        "description": "XL-bay8-gen10-harrier-profile-template",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
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
                }
            ],
            "manageConnections": True
        },
        "boot": None,
        "bootMode": {
            "manageMode": False
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
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "rd1",
                            "raidLevel": "RAID1",
                            "bootable": False,
                            "numPhysicalDrives": 2,
                            "driveTechnology": "SasHdd",
                            "sasLogicalJBODId": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "Mixed",
                    "initialize": True
                }
            ]
        },
        "sanStorage": None,
        "osDeploymentSettings": None
    }
]

gen10_server_profiles = [
    {
        "type": SERVER_PROFILE_TYPE,
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
            "connections": [
                {
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
                }
            ]
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
            "overriddenSettings": [
                {
                    "id": "CustomPostMessage",
                    "value": "Harrier"
                }
            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [
                {
                    "id": 1,
                    "deviceSlot": "Mezz 1",
                    "name": "ljb1",
                    "numPhysicalDrives": 1,
                    "driveMinSizeGB": 50,
                    "driveMaxSizeGB": 500,
                    "driveTechnology": "SasHdd",
                    "sasLogicalJBODUri": None
                }
            ],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "rd0",
                            "raidLevel": "RAID0",
                            "bootable": False,
                            "numPhysicalDrives": 1,
                            "driveTechnology": "SasHdd",
                            "sasLogicalJBODId": None,
                            "driveNumber": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "Mixed",
                    "initialize": True,
                    "importConfiguration": False
                }
            ]
        },
        "sanStorage": None
    }]

edit_gen10_profile_boot_bios = {
    "type": SERVER_PROFILE_TYPE,
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
    "type": SERVER_PROFILE_TYPE,
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

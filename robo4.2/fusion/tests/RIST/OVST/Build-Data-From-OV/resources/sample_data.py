#!/usr/bin/env python


ethnets = [
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net22",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 22
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net23",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 23
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net21",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 21
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net25",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 25
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net15",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 15
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net11",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 11
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net19",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 19
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net13",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 13
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net16",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 16
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net18",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 18
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net17",
        "privateNetwork": False,
        "purpose": "VMMigration",
        "smartLink": False,
        "vlanId": 17
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net24",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 24
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net12",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 12
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net300",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 300
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net14",
        "privateNetwork": False,
        "purpose": "Management",
        "smartLink": False,
        "vlanId": 14
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "net10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 10
    }
]

fcnets = [
    {
        "type": "fc-networkV300",
        "name": "3par-b",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    },
    {
        "type": "fc-networkV300",
        "name": "fa-san-2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN21"
    },
    {
        "type": "fc-networkV300",
        "name": "fa-san-1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "managedSanUri": "FCSan:VSAN20"
    },
    {
        "type": "fc-networkV300",
        "name": "3par-a",
        "fabricType": "DirectAttach",
        "linkStabilityTime": 0,
        "autoLoginRedistribution": False,
        "managedSanUri": None
    }
]

fcoenets = [
]

networkset = [
    {
        "type": "network-setV300",
        "name": "netset2",
        "nativeNetworkUri": "net14",
        "networkUris": [
            "net16",
            "net17",
            "net14",
            "net15"
        ]
    },
    {
        "type": "network-setV300",
        "name": "netset1",
        "nativeNetworkUri": "net10",
        "networkUris": [
            "net10",
            "net12",
            "net11",
            "net13"
        ]
    },
    {
        "type": "network-setV300",
        "name": "netset4",
        "nativeNetworkUri": "net22",
        "networkUris": [
            "net24",
            "net25",
            "net23",
            "net22"
        ]
    },
    {
        "type": "network-setV300",
        "name": "netset3",
        "nativeNetworkUri": "net18",
        "networkUris": [
            "net20",
            "net21",
            "net18",
            "net19"
        ]
    }
]

storagesystems = [
    {
        "name": "ThreePAR-1",
        "family": "StoreServ",
        "hostname": "172.18.11.11",
        "deviceSpecificAttributes": {
            "managedDomain": "TestDomain",
            "managedPools": []
        }
    }
]

storagepools = [
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "FST_CPG2",
        "isManaged": True
    },
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "FST_CPG1",
        "isManaged": True
    },
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "CPG_FC-AO",
        "isManaged": False
    },
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "CPG-SSD",
        "isManaged": False
    },
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "cpg-growth-limit-1TiB",
        "isManaged": False
    },
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "CPG-SSD-AO",
        "isManaged": False
    },
    {
        "storageSystemUri": "ThreePAR-1",
        "name": "cpg_growth-warning-100GiB",
        "isManaged": False
    }
]

storagevolumetemplates = [
    {
        "name": "ova-private-thin",
        "description": "private non-boot volume template",
        "properties": {
            "description": {
                "description": "A description for the volume",
                "title": "Description",
                "default": "",
                "minLength": 0,
                "meta": {
                    "locked": False,
                },
                "maxLength": 2000,
                "type": "string",
            },
            "name": {
                "description": "A volume name between 1 and 100 characters",
                "title": "Volume name",
                "minLength": 1,
                "required": True,
                "meta": {
                    "locked": False,
                },
                "maxLength": 100,
                "type": "string",
            },
            "snapshotPool": {
                "description": "A URI referenceto the common provisioning group used to create snapshots",
                "format": "x-uri-reference",
                "default": "FST_CPG1",
                "title": "FC_wpst16_r1",
                "meta": {
                    "semanticType": "device-snapshot-storage-pool",
                    "locked": True,
                },
                "type": "string",
            },
            "storagePool": {
                "description": "A common provisioning group URI reference",
                "format": "x-uri-reference",
                "default": "FST_CPG1",
                "required": True,
                "meta": {
                    "createOnly": True,
                    "semanticType": "device-storage-pool",
                    "locked": False,
                },
                "title": "Storage Pool",
                "type": "string",
            },
            "provisioningType": {
                "description": "The provisioning type for the volume",
                "title": "Provisioning Type",
                "default": "Thin",
                "enum": [u'Thin', u'Full'],
                "meta": {
                    "createOnly": True,
                    "locked": True,
                },
                "type": "string",
            },
            "isShareable": {
                "default": False,
                "meta": {
                    "locked": False,
                },
                "type": "boolean",
                "description": "The shareability of the volume",
                "title": "Is Shareable",
            },
            "size": {
                "description": "The capacity of the volume in bytes",
                "title": "Capacity",
                "default": 1073741824,
                "required": True,
                "maximum": 17592186044416,
                "minimum": 1073741824,
                "meta": {
                    "semanticType": "capacity",
                    "locked": False,
                },
                "type": "integer",
            },
        }
    }
]

storagevolumes = [
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay2priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ova-private-thin",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay9priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay1priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay3priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "shared volume",
            "isShareable": True,
            "name": "dd-shared",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ova-private-thin",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay10priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ova-private-thin",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay7priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ova-private-thin",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay8priv",
            "provisioningType": "Thin",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        },
    },
    {
        "templateUri": "ROOT",
        "properties": {
            "description": "non-boot private volume",
            "isShareable": False,
            "name": "enc2bay4priv",
            "provisioningType": "Full",
            "size": 5368709120,
            "storagePool": "FST_CPG1"
        }
    }
]

saslig = [
    {
        "name": "dd-Natasha",
        "type": "sas-logical-interconnect-group",
        "enclosureType": "SY12000",
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "bay": 1,
                "enclosure": 1,
                "type": "Synergy 12Gb SAS Connection Module"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 4,
                "type": "Synergy 12Gb SAS Connection Module"
            }

        ],
        "interconnectBaySet": 1,
        "enclosureIndexes": [1]
    }
]

lig = [
    {
        "name": "LIG_DCS_2",
        "type": "logical-interconnect-groupV300",
        "enclosureType": "SY12000",
        "ethernetSettings": {
            "enableFastMacCacheFailover": False,
            "enableIgmpSnooping": True,
            "enableNetworkLoopProtection": False,
            "enablePauseFloodProtection": False,
            "igmpIdleTimeoutInterval": 240,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 15
        },
        "interconnectMapTemplate": [
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 6,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 6,
                "enclosure": 2,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 1,
                "enclosure": 1,
                "bay": 3,
                "type": "Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "enclosureIndex": 3,
                "bay": 6,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 2,
                "bay": 3,
                "enclosure": 2,
                "type": "Synergy 20Gb Interconnect Link Module"
            },
            {
                "enclosureIndex": 3,
                "bay": 3,
                "enclosure": 3,
                "type": "Synergy 20Gb Interconnect Link Module"
            }

        ],
        "interconnectBaySet": 3,
        "redundancyType": "HighlyAvailable",
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 12,
            "sampleInterval": 300
        },
        "snmpConfiguration": {
            "enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": []
        },
        "uplinkSets": [
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "port": "Q1.2",
                        "enclosure": "1",
                        "bay": "3"
                    }
                ],
                "mode": "Auto",
                "name": "lig1-fa-san-1",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "fa-san-1"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "Tagged",
                "lacpTimer": "Short",
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "enclosure": "2",
                        "port": "Q1.1",
                        "bay": "6"
                    },
                    {
                        "speed": "Auto",
                        "bay": "3",
                        "enclosure": "1",
                        "port": "Q1.1"
                    }
                ],
                "mode": "Auto",
                "name": "lig1-enet",
                "nativeNetworkUri": None,
                "networkType": "Ethernet",
                "networkUris": [
                    "net10",
                    "net12",
                    "net13",
                    "net11"
                ],
                "primaryPort": None
            },
            {
                "ethernetNetworkType": "NotApplicable",
                "lacpTimer": None,
                "logicalPortConfigInfos": [
                    {
                        "speed": "Auto",
                        "bay": "3",
                        "enclosure": "1",
                        "port": "Q1:3"
                    }
                ],
                "mode": "Auto",
                "name": "lig1-fa-san-2",
                "nativeNetworkUri": None,
                "networkType": "FibreChannel",
                "networkUris": [
                    "fa-san-2"
                ],
                "primaryPort": None
            }
        ],
        "qosConfiguration": {
            "activeQosConfig": {u'status': None, u'category': u'qos-aggregated-configuration', u'description': None, u'created': None, u'modified': None, u'uri': None, u'configType': u'Passthrough', u'state': None, u'eTag': None, u'downlinkClassificationType': None, u'uplinkClassificationType': None, u'qosTrafficClassifiers': [], u'type': u'QosConfiguration', u'name': None},
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "name": None,
            "type": "qos-aggregated-configuration"
        },
        "enclosureIndexes": [1, 2, 3]
    }
]

encgrp = [
    {
        "name": "ISO-EG",
        "type": "EnclosureGroupV400",
        "enclosureTypeUri": "/rest/enclosure-types/SY12000",
        "stackingMode": "Enclosure",
        "interconnectBayMappingCount": 4,
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "dd-Natasha"
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG_DCS_2"
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "dd-Natasha"
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG_DCS_2"
            }
        ],
        "ipAddressingMode": "External",
        "enclosureCount": 3
    }
]

logicalenclosures = [
    {
        "name": "DCS_LE",
        "enclosureUris": [
            "ENC:0000A66101",
            "ENC:0000A66102",
            "ENC:0000A66103"
        ],
        "enclosureGroupUri": "EG:ISO-EG"
    }
]

spt = [
    {
        "name": "SPT-ENCL1-BAY3",
        "type": "ServerProfileTemplateV3",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SY 660 Gen9 2",
        "enclosureGroupUri": "ISO-EG",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "net10",
                    "boot": {
                        "priority": "NotBootable",
                        "bootVlanId": None,
                    },
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:2-a",
                    "requestedMbps": "2500",
                    "networkUri": "net11",
                    "boot": {
                        "priority": "NotBootable",
                        "bootVlanId": None,
                    },
                },
                {
                    "id": 3,
                    "name": "",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "fa-san-1",
                    "boot": {
                        "priority": "NotBootable",
                        "bootVlanId": None,
                    },
                },
            ]

        },
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk']
        },
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {u'manageSanStorage': False, u'volumeAttachments': []}
    }
]

profiles = [
    {
        "name": "Encl1bay5",
        "type": "ServerProfileV7",
        "serverHardwareUri": "0000A66101, bay 5",
        "enclosureUri": "0000A66101",
        "enclosureGroupUri": "ISO-EG",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "description": "",
        "affinity": "Bay",
        "connections": [
            {
                "allocatedMbps": 2500,
                "functionType": "Ethernet",
                "id": 1,
                "mac": "",
                "macType": "Virtual",
                "maximumMbps": 10000,
                "name": "",
                "portId": "Mezz 3:1-a",
                "requestedMbps": "2500",
                "wwnn": None,
                "wwpn": None,
                "networkUri": "net10",
            },
            {
                "allocatedMbps": 4000,
                "functionType": "FibreChannel",
                "id": 2,
                "mac": "",
                "macType": "Virtual",
                "maximumMbps": 10000,
                "name": "",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "4000",
                "wwnn": "10:00:52:8d:e4:00:00:13",
                "wwpn": "10:00:52:8d:e4:00:00:12",
                "networkUri": "fa-san-1",
            }
        ],
        "boot": {
            "manageBoot": True,
            "order": [u'HardDisk', u'CD', u'USB', u'PXE']
        },
        "bootMode": {
            "pxeBootPolicy": None,
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
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgm74700g",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    "id": 1,
                    "volumeUri": "enc2bay7priv",
                    "isBootVolume": False,
                    "lunType": "Manual",
                    "lun": "1",
                    "storagePaths": [
                        {
                            "isEnabled": True,
                            "connectionId": 2,
                            "targetSelector": "Auto",
                            "targets": [],
                        }
                    ]
                }
            ]
        },
    }
]

encs = [
    {
        "enclosureGroupUri": "ISO-EG",
        "forceInstallFirmware": False,
        "licensingIntent": "NotApplicable"
    },
    {
        "enclosureGroupUri": "ISO-EG",
        "forceInstallFirmware": False,
        "licensingIntent": "NotApplicable"
    },
    {
        "enclosureGroupUri": "ISO-EG",
        "forceInstallFirmware": False,
        "licensingIntent": "NotApplicable"
    }
]

servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 6",
        "partNumber": "740040-001",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201127GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 5",
        "partNumber": "740040-001",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201124GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 660 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 4",
        "partNumber": "777072-001",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 4,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v1.30 08/26/2014",
        "serialNumber": "2M201512GR",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 8",
        "partNumber": "740040-001",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201133GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 12",
        "partNumber": "740040-001",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30",
        "serialNumber": "2M201121GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 11",
        "partNumber": "740040-001",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30",
        "serialNumber": "2M201118GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 7",
        "partNumber": "740040-001",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201130GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 12",
        "partNumber": "740040-001",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201109GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 8",
        "partNumber": "740040-001",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201115GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 11",
        "partNumber": "740040-001",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201106GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 7",
        "partNumber": "740040-001",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201112GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 5",
        "partNumber": "740040-001",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201100GR",
        "shortModel": "SY 480 Gen9",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 6",
        "partNumber": "740040-001",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201103GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 660 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 4",
        "partNumber": "777072-001",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 4,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v1.30 08/26/2014",
        "serialNumber": "2M201505GR",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 660 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66101, bay 3",
        "partNumber": "777072-001",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 4,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v1.30 08/26/2014",
        "serialNumber": "2M201501GR",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 660 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66102, bay 3",
        "partNumber": "777072-001",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 4,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v1.30 08/26/2014",
        "serialNumber": "2M201508GR",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 12",
        "partNumber": "740040-001",
        "position": 12,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201145GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 8",
        "partNumber": "740040-001",
        "position": 8,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201151GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 11",
        "partNumber": "740040-001",
        "position": 11,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201142GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 660 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 3",
        "partNumber": "777072-001",
        "position": 3,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 4,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v1.30 08/26/2014",
        "serialNumber": "2M201515GR",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 5",
        "partNumber": "740040-001",
        "position": 5,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201136GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 7",
        "partNumber": "740040-001",
        "position": 7,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201148GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 480 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 6",
        "partNumber": "740040-001",
        "position": 6,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 2,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I37 v1.30 08/26/2014",
        "serialNumber": "2M201139GR",
        "shortModel": "SY 480 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Critical",
        "type": "server-hardware-7"
    },
    {
        "formFactor": "FullHeight",
        "licensingIntent": "NotApplicable",
        "memoryMb": 4096,
        "model": "HPE Synergy 660 Gen9 Compute Module",
        "mpFirmwareVersion": "2.30 Jul 23 2015",
        "mpModel": "iLO4",
        "name": "0000A66103, bay 4",
        "partNumber": "777072-001",
        "position": 4,
        "powerLock": False,
        "powerState": "Off",
        "processorCoreCount": 4,
        "processorCount": 4,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I39 v1.30 08/26/2014",
        "serialNumber": "2M201519GR",
        "shortModel": "SY 660 Gen9",
        "state": "NoProfileApplied",
        "stateReason": "NotApplicable",
        "status": "Warning",
        "type": "server-hardware-7"
    }
]

default_variables = {
    "ethnets": ethnets,
    "fcnets": fcnets,
    "fcoenets": fcoenets,
    "networkset": networkset,
    "storagesystems": storagesystems,
    "storagepools": storagepools,
    "storagevolumetemplates": storagevolumetemplates,
    "storagevolumes": storagevolumes,
    "saslig": saslig,
    "lig": lig,
    "encgrp": encgrp,
    "logicalenclosures": logicalenclosures,
    "spt": spt,
    "profiles": profiles,
    "encs": encs,
    "servers": servers
}


def get_variables():
    """ Auto-generated function for the variable python file """

    variables = default_variables
    return variables


admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

password = 'wpsthpvse1'

FUSION_IP = '16.114.211.95'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'wpsthpvse1'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
# FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password  DCS
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

ENC_NAME = "CN744502CL"
LIG_NAME = "Tbird10_LIG"
EG_NAME = "Tbird10_EG"
LE_NAME = "Tbird10_LE"

SERVER_NAME = "CN744502CL, bay 1"
PROFILE_NAME = "Tbird10_bay_1_profile"

lig = {
    "enclosureIndexes": [
        1
    ],
    "description": None,
    "telemetryConfiguration": {
        "description": None,
        "sampleCount": 12,
        "enableTelemetry": True,
        "sampleInterval": 300,
        "type": "telemetry-configuration",
        "name": None
    },
    "internalNetworkUris": [],
    "name": "Tbird10_LIG",
    "uplinkSets": [
        {
            "networkUris": [
                "ETH:net100"
            ],
            "ethernetNetworkType": "Tagged",
            "name": "ULS1",
            "lacpTimer": "Short",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "reachability": None,
            "mode": "Auto",
            "networkType": "Ethernet",
            "logicalPortConfigInfos": [
                {
                    "desiredSpeed": "Auto",
                    "logicalLocation": {
                        "locationEntries": [
                            {
                                "type": "Port",
                                "relativeValue": 61
                            },
                            {
                                "type": "Enclosure",
                                "relativeValue": 1
                            },
                            {
                                "type": "Bay",
                                "relativeValue": 3
                            }
                        ]
                    }
                }
            ]
        },
        {
            "networkUris": [
                "ETH:net300"
            ],
            "ethernetNetworkType": "Tagged",
            "name": "ULS2",
            "lacpTimer": "Short",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "reachability": None,
            "mode": "Auto",
            "networkType": "Ethernet",
            "logicalPortConfigInfos": [
                {
                    "desiredSpeed": "Auto",
                    "logicalLocation": {
                        "locationEntries": [
                            {
                                "type": "Port",
                                "relativeValue": 61
                            },
                            {
                                "type": "Enclosure",
                                "relativeValue": 1
                            },
                            {
                                "type": "Bay",
                                "relativeValue": 6
                            }
                        ]
                    }
                }
            ]
        }
    ],
    "redundancyType": "Redundant",
    "enclosureType": "SY12000",
    "fabricUri": "Fabric:DefaultFabric",
    "qosConfiguration": {
        "name": None,
        "type": "qos-aggregated-configuration",
        "inactiveFCoEQosConfig": None,
        "inactiveNonFCoEQosConfig": None,
        "activeQosConfig": {
            "description": None,
            "configType": "Passthrough",
            "downlinkClassificationType": None,
            "uplinkClassificationType": None,
            "qosTrafficClassifiers": [],
            "type": "QosConfiguration",
            "name": None
        },
        "description": None
    },
    "scopeUris": [],
    "type": "logical-interconnect-groupV300",
    "interconnectMapTemplate": {
        "interconnectMapEntryTemplates": [
            {
                "logicalLocation": {
                    "locationEntries": [
                        {
                            "type": "Enclosure",
                            "relativeValue": 1
                        },
                        {
                            "type": "Bay",
                            "relativeValue": 6
                        }
                    ]
                },
                "enclosureIndex": 1,
                "permittedInterconnectTypeUri": "ICTypes:Virtual Connect SE 40Gb F8 Module for Synergy"
            },
            {
                "logicalLocation": {
                    "locationEntries": [
                        {
                            "type": "Enclosure",
                            "relativeValue": 1
                        },
                        {
                            "type": "Bay",
                            "relativeValue": 3
                        }
                    ]
                },
                "enclosureIndex": 1,
                "permittedInterconnectTypeUri": "ICTypes:Virtual Connect SE 40Gb F8 Module for Synergy"
            }
        ]
    },
    "ethernetSettings": {
        "interconnectType": "Ethernet",
        "igmpIdleTimeoutInterval": 260,
        "macRefreshInterval": 5,
        "description": None,
        "enableTaggedLldp": False,
        "enableRichTLV": False,
        "enableNetworkLoopProtection": True,
        "enableFastMacCacheFailover": True,
        "lldpIpv4Address": "",
        "enableIgmpSnooping": False,
        "enablePauseFloodProtection": True,
        "dependentResourceUri": "LIG:Tbird10_LIG",
        "type": "EthernetInterconnectSettingsV201",
        "lldpIpv6Address": "",
        "name": "name2003202772-1470153927401"
    },
    "stackingHealth": None,
    "stackingMode": None,
    "interconnectBaySet": 3,
    "snmpConfiguration": {
        "description": None,
        "readCommunity": "public",
        "enabled": True,
        "systemContact": "",
        "snmpAccess": [],
        "trapDestinations": [],
        "type": "snmp-configuration",
        "name": None
    }
}

eg = {
    "osDeploymentSettings": {
        "deploymentModeSettings": {
            "deploymentNetworkUri": None,
            "deploymentMode": "None"
        },
        "manageOSDeployment": False
    },
    "associatedLogicalInterconnectGroups": [
        "LIG:Tbird10_LIG"
    ],
    "description": None,
    "powerMode": "RedundantPowerFeed",
    "interconnectBayMappings": [
        {
            "logicalInterconnectGroupUri": "LIG:Tbird10_LIG",
            "interconnectBay": 3
        },
        {
            "logicalInterconnectGroupUri": "LIG:Tbird10_LIG",
            "interconnectBay": 6
        }
    ],
    "enclosureCount": 1,
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "type": "EnclosureGroupV300",
    "stackingMode": "Enclosure",
    "name": EG_NAME
}

les = [{'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC_NAME],
        'enclosureGroupUri': "EG:"+EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}
       ]

profile = {
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connections": [
        {
            "requestedVFs": "0",
            "wwnn": None,
            "deploymentStatus": "Deployed",
            "portId": "Mezz 3:1-a",
            "name": "conn1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:net100",
            "interconnectUri": "IC:CN744502CL, interconnect 3",
            "maximumMbps": 10000,
            "functionType": "Ethernet",
            "macType": "Virtual"
        },
        {
            "requestedVFs": "0",
            "wwnn": None,
            "deploymentStatus": "Deployed",
            "portId": "Mezz 3:2-a",
            "name": "conn2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "interconnectUri": "IC:CN744502CL, interconnect 6",
            "maximumMbps": 10000,
            "functionType": "Ethernet",
            "macType": "Virtual"
        }
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "serverHardwareTypeUri": "SHT:SY 480 Gen9 1",
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "firmware": {
        "firmwareBaselineUri": None,
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "boot": {
        "manageBoot": False,
        "order": []
    },
    "hideUnusedFlexNics": True,
    "bootMode": {
        "manageMode": False,
        "pxeBootPolicy": None,
        "mode": None
    },
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "type": "ServerProfileV6",
    "enclosureUri": "ENC:CN744502CL",
    "associatedServer": None,
    "osDeploymentSettings": None,
    "description": "",
    "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgnka005r",
    "templateCompliance": "Unknown",
    "serverHardwareUri": "SH:CN744502CL, bay 1",
    "enclosureBay": 1,
    "name": "Tbird10_bay_1_profile",
    "enclosureGroupUri": "EG:Tbird10_EG",
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }
}

ris_original = {
    "server": SERVER_NAME,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/NetworkAdapters/1",
    "validate": {
            "PhysicalPorts": [{"MacAddress": "34:64:a9:93:68:30"}, {"MacAddress": "34:64:a9:93:68:38"}]
    }
}

PostStateDiscoveryComplete = {
    "server": SERVER_NAME,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1",
    "validate": {
            "Oem": {
                "Hp": {
                    "PostState": "FinishedPost",
                    "DeviceDiscoveryComplete": {
                        "DeviceDiscovery": "vMainDeviceDiscoveryComplete"
                    }
                }
            }
    }
}

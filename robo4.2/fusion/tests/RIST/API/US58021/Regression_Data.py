admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

# Existing Resources from previous test\
ENC1 = "CN754406XL"
ENC2 = "CN754404R6"
ENC3 = "CN754406WB"

LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV6'
SAS_LOGICAL_JBOD_TYPE = 'sas-logical-jbodV4'

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

Bay = "5"

SH = ENC2 + ", bay " + Bay
LIG_Exist = "LIG1"
EG_Exist = "EG1"

# Created "extra" resources
LIG_NAME = "BR_LIG"
EG_NAME = "BR_EG"
SP_NAME = ENC2 + "_BR_bay" + Bay + "_profile"

# Used after backup created
Post_backup_ENC = ENC3
Post_backup_LIG_NAME = "Post_backup_BR_LIG"
Post_backup_EG_NAME = "Post_backup_BR_EG"
Post_backup_SP_NAME = Post_backup_ENC + Bay + "Post_backup_BR_bay__profile"
Post_backup_SH = Post_backup_ENC + ", bay " + Bay

BR_ethernet_networks = [
    {'name': 'BR_Network1',
     'type': 'ethernet-networkV4',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'BR_Network2',
     'type': 'ethernet-networkV4',
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'BR_Network3',
     'type': 'ethernet-networkV4',
     'vlanId': 3,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'BR_Network4',
     'type': 'ethernet-networkV4',
     'vlanId': 4,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
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
     'ethernetNetworkType': 'Tagged'}
]

icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6,
          'enclosure': 1,
          'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
          'enclosureIndex': 1}
         ]

BR_lig = [{
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
    "name": LIG_NAME,
    "uplinkSets": [
        {
            "networkUris": [
                "net100"
            ],
            "ethernetNetworkType": "Tagged",
            "name": "ULS1",
            "lacpTimer": "Short",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "mode": "Auto",
            "networkType": "Ethernet",
            "logicalPortConfigInfos": [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
        },
        {
            "networkUris": [
                "net300"
            ],
            "ethernetNetworkType": "Tagged",
            "name": "ULS2",
            "lacpTimer": "Short",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "mode": "Auto",
            "networkType": "Ethernet",
            "logicalPortConfigInfos": [{'enclosure': '1', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}]
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
    "type": LOGICAL_INTERCONNECT_GROUP_TYPE,
    "interconnectMapTemplate": icmap,
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
        "type": "EthernetInterconnectSettingsV4",
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
        "v3Enabled": True,
        "systemContact": "",
        "snmpAccess": [],
        "trapDestinations": [],
        "type": "snmp-configuration",
        "name": None
    }
}]

BR_lig_validate = {
    "uplinkSets": [
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
                                "relativeValue": 67
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
        },
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
                                "relativeValue": 62
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
        }
    ],
    "stackingHealth": None,
    "interconnectBaySet": 3,
    "snmpConfiguration": {
        "status": None,
        "category": "snmp-configuration",
        "description": None,
        "readCommunity": "public",
        "enabled": True,
        "v3Enabled": True,
        "uri": None,
        "systemContact": "",
        "state": None,
        "snmpAccess": [],
        "trapDestinations": [],
        "type": "snmp-configuration",
        "name": None
    },
    "category": "logical-interconnect-groups",
    "internalNetworkUris": [],
    "state": "Active",
    "qosConfiguration": {
        "status": None,
        "category": "qos-aggregated-configuration",
        "inactiveFCoEQosConfig": None,
        "name": None,
        "activeQosConfig": {
            "status": None,
            "category": "qos-aggregated-configuration",
            "description": None,
            "uri": None,
            "configType": "Passthrough",
            "state": None,
            "downlinkClassificationType": None,
            "uplinkClassificationType": None,
            "qosTrafficClassifiers": [],
            "type": "QosConfiguration",
            "name": None
        },
        "uri": None,
        "state": None,
        "inactiveNonFCoEQosConfig": None,
        "type": "qos-aggregated-configuration",
        "description": None
    },
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
                            "relativeValue": "REGEX:[36]"
                        }
                    ]
                },
                "permittedInterconnectTypeUri": "ICTypes:Virtual Connect SE 40Gb F8 Module for Synergy",
                "enclosureIndex": 1
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
                            "relativeValue": "REGEX:[36]"
                        }
                    ]
                },
                "permittedInterconnectTypeUri": "ICTypes:Virtual Connect SE 40Gb F8 Module for Synergy",
                "enclosureIndex": 1
            }
        ]
    },
    "type": LOGICAL_INTERCONNECT_GROUP_TYPE,
    "status": None,
    "enclosureIndexes": [
        1
    ],
    "description": None,
    "telemetryConfiguration": {
        "status": None,
        "category": "telemetry-configuration",
        "description": None,
        "sampleCount": 12,
        "enableTelemetry": True,
        "uri": None,
        "state": None,
        "sampleInterval": 300,
        "type": "telemetry-configuration",
        "name": None
    },
    "ethernetSettings": {
        "category": None,
        "status": None,
        "igmpIdleTimeoutInterval": 260,
        "macRefreshInterval": 5,
        "description": None,
        "enableTaggedLldp": False,
        "enableRichTLV": False,
        "enableNetworkLoopProtection": True,
        "enableFastMacCacheFailover": True,
        "lldpIpv4Address": "",
        "enableIgmpSnooping": False,
        "state": None,
        "enablePauseFloodProtection": True,
        "dependentResourceUri": "LIG:BR_LIG",
        "interconnectType": "Ethernet",
        "type": "EthernetInterconnectSettingsV4",
        "lldpIpv6Address": ""
    },
    "stackingMode": None,
    "name": "BR_LIG",
    "uri": "LIG:BR_LIG",
    "redundancyType": "Redundant",
    "enclosureType": "SY12000",
    "fabricUri": "Fabric:DefaultFabric"
}

BR_eg = [{
    "osDeploymentSettings": {
        "deploymentModeSettings": {
            "deploymentNetworkUri": None,
            "deploymentMode": "None"
        },
        "manageOSDeployment": False
    },
    "powerMode": "RedundantPowerFeed",
    "interconnectBayMappings": [
        {
            "logicalInterconnectGroupUri": "LIG:" + LIG_NAME,
            "interconnectBay": 3
        },
        {
            "logicalInterconnectGroupUri": "LIG:" + LIG_NAME,
            "interconnectBay": 6
        }
    ],
    "enclosureCount": 1,
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "name": EG_NAME
}]

BR_profile = {
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connectionSettings": {
        "connections": [
            {
                "requestedVFs": "0",
                "portId": "Mezz 3:1-a",
                "name": "conn1",
                "wwpnType": "Virtual",
                "requestedMbps": "2500",
                "networkUri": "ETH:net100",
                "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
                "maximumMbps": 10000,
                "functionType": "Ethernet",
                "macType": "Virtual"
            },
            {
                "requestedVFs": "0",
                "portId": "Mezz 3:2-a",
                "name": "conn2",
                "wwpnType": "Virtual",
                "requestedMbps": "2500",
                "networkUri": "ETH:net300",
                "interconnectUri": "IC:" + ENC2 + ", interconnect 6",
                "maximumMbps": 10000,
                "functionType": "Ethernet",
                "macType": "Virtual"
            }
        ]
    },
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "serverHardwareUri": "SH:" + SH,
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
    "type": "ServerProfileV10",
    "enclosureUri": "ENC:" + ENC2,
    "serverHardwareTypeUri": "SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
    "associatedServer": None,
    "description": "",
    "templateCompliance": "Unknown",
    "enclosureBay": Bay,
    "name": SP_NAME,
    "enclosureGroupUri": "EG:" + EG_Exist,
    "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
    }
}


Post_backup_ethernet_networks = [
    {'name': 'POST_BR_Network111',
     'type': 'ethernet-networkV4',
     'vlanId': 111,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'POST_BR_Network222',
     'type': 'ethernet-networkV4',
     'vlanId': 222,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'POST_BR_Network333',
     'type': 'ethernet-networkV4',
     'vlanId': 333,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'POST_BR_Network444',
     'type': 'ethernet-networkV4',
     'vlanId': 444,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]
icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6,
          'enclosure': 1,
          'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
          'enclosureIndex': 1}
         ]

Post_backup_lig = [{
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
    "name": Post_backup_LIG_NAME,
    "uplinkSets": [
        {
            "networkUris": [
                "net100"
            ],
            "ethernetNetworkType": "Tagged",
            "name": "ULS1",
            "lacpTimer": "Short",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "mode": "Auto",
            "networkType": "Ethernet",
            "logicalPortConfigInfos": [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
        },
        {
            "networkUris": [
                "net300"
            ],
            "ethernetNetworkType": "Tagged",
            "name": "ULS2",
            "lacpTimer": "Short",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "mode": "Auto",
            "networkType": "Ethernet",
            "logicalPortConfigInfos": [{'enclosure': '1', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}]
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
    "type": LOGICAL_INTERCONNECT_GROUP_TYPE,
    "interconnectMapTemplate": icmap,
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
        "dependentResourceUri": "LIG:LIG_NAME",
        "type": "EthernetInterconnectSettingsV4",
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
        "v3Enabled": True,
        "systemContact": "",
        "snmpAccess": [],
        "trapDestinations": [],
        "type": "snmp-configuration",
        "name": None
    }
}]

Post_backup_eg = [{
    "osDeploymentSettings": {
        "deploymentModeSettings": {
            "deploymentNetworkUri": None,
            "deploymentMode": "None"
        },
        "manageOSDeployment": False
    },
    "powerMode": "RedundantPowerFeed",
    "interconnectBayMappings": [
        {
            "logicalInterconnectGroupUri": "LIG:" + LIG_NAME,
            "interconnectBay": 3
        },
        {
            "logicalInterconnectGroupUri": "LIG:" + LIG_NAME,
            "interconnectBay": 6
        }
    ],
    "enclosureCount": 1,
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "name": Post_backup_EG_NAME
}]

Post_backup_profile = {
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connectionSettings": {
        "connections": [
            {
                "requestedVFs": "0",
                "portId": "Mezz 3:1-a",
                "name": "conn1",
                "wwpnType": "Virtual",
                "requestedMbps": "2500",
                "networkUri": "ETH:net100",
                "interconnectUri": "IC:" + Post_backup_ENC + ", interconnect 3",
                "maximumMbps": 10000,
                "functionType": "Ethernet",
                "macType": "Virtual"
            },
            {
                "requestedVFs": "0",
                "portId": "Mezz 3:2-a",
                "name": "conn2",
                "wwpnType": "Virtual",
                "requestedMbps": "2500",
                "networkUri": "ETH:net300",
                "interconnectUri": "IC:" + Post_backup_ENC + ", interconnect 6",
                "maximumMbps": 10000,
                "functionType": "Ethernet",
                "macType": "Virtual"
            }
        ]
    },
    "iscsiInitiatorNameType":
        "AutoGenerated",
    "macType":
        "Virtual",
    "serverHardwareUri":
        "SH:" + Post_backup_SH,
    "bios":
        {
            "overriddenSettings": [],
            "manageBios": False
    },
    "firmware":
        {
            "firmwareBaselineUri": None,
            "manageFirmware": False,
            "forceInstallFirmware": False,
            "firmwareInstallType": None
    },
    "boot":
        {
            "manageBoot": False,
            "order": []
    },
    "hideUnusedFlexNics":
        True,
    "bootMode":
        {
            "manageMode": False,
            "pxeBootPolicy": None,
            "mode": None
    },
    "affinity":
        "Bay",
    "localStorage":
        {
            "controllers": [],
            "sasLogicalJBODs": []
    },
    "type":
        "ServerProfileV10",
    "enclosureUri":
        "ENC:" + Post_backup_ENC,
    "associatedServer":
        None,
    "description":
        "",
    "templateCompliance":
        "Unknown",
    "enclosureBay":
        Bay,
    "name":
        Post_backup_SP_NAME,
    "enclosureGroupUri":
        "EG:" + EG_Exist,
    "sanStorage":
        {
            "manageSanStorage": False,
            "volumeAttachments": []
    }
}

ljb1_name = 'ljb-sas-1'
ljb2_name = 'ljb-sas-2'

SASLI = 'LE1-SASLIG1-1'

ljbs = [{"name": ljb1_name, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
         "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
         "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 1, "minSizeGB": "200",
         "maxSizeGB": "450", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
         "eraseData": False}, ]

Post_backup_ljbs = [{"name": ljb2_name, "type": SAS_LOGICAL_JBOD_TYPE, "description": "",
                     "sasLogicalInterconnectUri": SASLI, "initialScopeUris": [],
                     "driveEnclosureUris": [ENC1DEBAY1], "numPhysicalDrives": 2, "minSizeGB": "100",
                     "maxSizeGB": "146", "driveTechnology": {"deviceInterface": "SAS", "driveMedia": "HDD"},
                     "eraseData": False}, ]

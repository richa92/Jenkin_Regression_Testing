admin_credentials = {'userName': 'Administrator', 'password': 'Wpst@hpvse123#!'}

# Existing Resources from previous test\
ENC1 = "CN754404R9"
ENC2 = "CN754406WS"
ENC3 = "CN754406WB"

Bay = "5"

SH = ENC2 + ", bay " + Bay
LIG_Exist = "LIG1"
EG_Exist = "EG1"

# Created "extra" resources
LIG_NAME = "BR_LIG"
EG_NAME = "BR_EG"

# Used after backup created
Post_backup_ENC = ENC3
Post_backup_LIG_NAME = "Post_backup_BR_LIG"
Post_backup_EG_NAME = "Post_backup_BR_EG"
Post_backup_SH = Post_backup_ENC + ", bay " + Bay

# Ethernet Networks
NET1 = 'net_100'
NET2 = 'net_300'

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
     'ethernetNetworkType': 'Tagged'}
]

icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
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
                NET1
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
                NET2
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
    "type": "logical-interconnect-groupV4",
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
                "ETH:" + NET2
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
                "ETH:" + NET1
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
                            "relativeValue": 6
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
                            "relativeValue": 3
                        }
                    ]
                },
                "permittedInterconnectTypeUri": "ICTypes:Virtual Connect SE 40Gb F8 Module for Synergy",
                "enclosureIndex": 1
            }
        ]
    },
    "type": "logical-interconnect-groupV4",
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
         {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
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
                NET1
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
                NET2
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
    "type": "logical-interconnect-groupV4",
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
            "logicalInterconnectGroupUri": "LIG:" + Post_backup_LIG_NAME,
            "interconnectBay": 3
        },
        {
            "logicalInterconnectGroupUri": "LIG:" + Post_backup_LIG_NAME,
            "interconnectBay": 6
        }
    ],
    "enclosureCount": 1,
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "name": Post_backup_EG_NAME
}]

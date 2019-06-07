
# Some resources can't be POSTed (Tbird Enclosure, Drive-Enclosure, Server blades, etc.
# Thus we can't create an actual data dict.  However Build.robot expects a template thus the
# simple template here.
simple = {
    "name": ""
}

eg = {
    "type": "EnclosureGroupV300",
    "osDeploymentSettings": None,
    "associatedLogicalInterconnectGroups": [""],
    "interconnectBayMappings": [
        {
            "logicalInterconnectGroupUri": "",
            "interconnectBay": 1,
            "enclosureIndex": 1
        }
    ],
    "description": None,
    "powerMode": None,
    "enclosureCount": 1,
    "ipAddressingMode": "",
    "ipRangeUris": [],
    "stackingMode": "",
    "name": "",
}

eth = {
    "ethernetNetworkType": "",
    "description": None,
    "vlanId": 100,
    "fabricUri": "",
    "scopeUris": [],
    "purpose": "",
    "subnetUri": None,
    "connectionTemplateUri": "",
    "privateNetwork": False,
    "type": "",
    "smartLink": False,
    "name": ""
}

fc = {
    "fabricType": "",
    "name": "",
    "autoLoginRedistribution": False,
    "scopeUris": [],
    "managedSanUri": None,
    "linkStabilityTime": 0,
    "connectionTemplateUri": "",
    "type": "",
    "description": None
}

lig = {
    "type": "",
    "description": None,
    "telemetryConfiguration": {
            "description": None,
            "sampleCount": 12,
            "enableTelemetry": True,
            "sampleInterval": 300,
            "type": "",
            "name": None
    },
    "internalNetworkUris": [],
    "uplinkSets": [
        {
            "networkUris": [
                ""
            ],
            "ethernetNetworkType": "",
            "name": "",
            "lacpTimer": "",
            "primaryPort": None,
            "nativeNetworkUri": None,
            "reachability": None,
            "mode": "",
            "networkType": "",
            "logicalPortConfigInfos": [
                    {
                        "desiredSpeed": "",
                        "logicalLocation": {
                            "locationEntries": [
                                {
                                    "type": "",
                                    "relativeValue": 63
                                }
                            ]
                        }
                    }
            ]
        }
    ],
    "name": "",
    "enclosureType": "",
    "fabricUri": "",
    "qosConfiguration": {
            "name": None,
            "type": "",
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "activeQosConfig": {
                "description": None,
                "configType": "",
                "downlinkClassificationType": None,
                "uplinkClassificationType": None,
                "qosTrafficClassifiers": [],
                "type": "",
                "name": None
            },
        "description": None
    },
    "scopeUris": [],
    "interconnectMapTemplate": {
        "interconnectMapEntryTemplates": [
            {
                "logicalDownlinkUri": "",
                "logicalLocation": {
                    "locationEntries": [
                        {
                            "type": "",
                            "relativeValue": 6
                        }
                    ]
                },
                "permittedInterconnectTypeUri": "",
                "enclosureIndex": 3
            }
        ]
    },
    "enclosureIndexes": [
        3
    ],
    "ethernetSettings": {
        "interconnectType": "",
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
        "dependentResourceUri": "",
        "type": "",
        "lldpIpv6Address": "",
        "name": ""
    },
    "redundancyType": "",
    "stackingHealth": None,
    "stackingMode": None,
    "interconnectBaySet": 3,
    "snmpConfiguration": {
        "description": None,
        "readCommunity": "",
        "enabled": True,
        "systemContact": "",
        "snmpAccess": [],
        "trapDestinations": [],
        "type": "",
        "name": None
    }
}

network_sets = {
    "networkUris": ["uri"],
    "nativeNetworkUri": None,
    "description": None,
    "name": ""
}

saslig = {
    "enclosureIndexes": [
        1
    ],
    "description": None,
    "enclosureType": "",
    "interconnectMapTemplate": {
        "interconnectMapEntryTemplates": [
            {
                "logicalLocation": {
                    "locationEntries": [
                        {
                            "type": "",
                            "relativeValue": 4
                        }
                    ]
                },
                "permittedInterconnectTypeUri": "",
                "enclosureIndex": 1
            }
        ]
    },
    "type": "",
    "interconnectBaySet": 1,
    "name": ""
}

user = {
    "userName": "",
    "name": None,
    "roles": [
        ""
    ],
    "description": None,
    "enabled": True,
    "emailAddress": "",
    "fullName": "",
    "officePhone": "",
    "type": "",
    "mobilePhone": ""
}

spt = {
    "hideUnusedFlexNics": True,
    "serverProfileDescription": "",
    "serverHardwareTypeUri": "",
    "description": "",
    "wwnType": "",
    "enclosureGroupUri": "",
    "bootMode": {
        "manageMode": True,
        "pxeBootPolicy": None,
        "mode": ""
    },
    "firmware": {
        "firmwareBaselineUri": None,
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "boot": {
        "manageBoot": True,
        "order": [
            ""
        ]
    },
    "serialNumberType": "",
    "connections": [],
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "affinity": "",
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    },
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "type": "",
    "iscsiInitiatorNameType": "",
    "macType": "",
    "name": ""
}

sp = {
    "wwnType": "",
    "serialNumberType": "",
    "connections": [
        {
            "networkUri": "",
            "requestedVFs": "",
            "portId": "",
            "name": None,
            "functionType": "",
            "requestedMbps": "",
            "boot": {
                "priority": "",
                "iscsi": {
                    "secondBootTargetPort": "",
                    "firstBootTargetPort": "",
                    "bootTargetName": "",
                    "initiatorName": "",
                    "bootTargetLun": "",
                    "secondBootTargetIp": "",
                    "firstBootTargetIp": "",
                    "chapLevel": "",
                    "chapName": "",
                    "initiatorNameSource": ""
                },
                "ethernetBootType": "",
                "bootVolumeSource": ""
            },
            "wwnn": None,
            "connectionStatus": "",
            "connectionState": "",
            "wwpn": None,
            "mac": "",
            "ipv4": {
                "ipAddressSource": "",
                "ipAddress": "",
                "gateway": "",
                "subnetMask": ""
            },
            "deletedNetworkName": None,
            "interconnectUri": "",
            "maximumMbps": 10000,
            "wwpnType": "",
            "macType": ""
        }
    ],
    "refreshState": "",
    "iscsiInitiatorNameType": "",
    "macType": "",
    "serverHardwareTypeUri": "",
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "firmware": {
        "forceInstallFirmware": False,
        "firmwareActivationType": None,
        "firmwareScheduleDateTime": None,
        "firmwareBaselineUri": None,
        "manageFirmware": False,
        "firmwareInstallType": None
    },
    "boot": {
        "manageBoot": True,
        "order": [
            ""
        ]
    },
    "hideUnusedFlexNics": True,
    "bootMode": {
        "pxeBootPolicy": "",
        "manageMode": True,
        "mode": ""
    },
    "affinity": "",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "type": "",
    "enclosureUri": "",
    "associatedServer": None,
    "osDeploymentSettings": None,
    "description": None,
    "serverProfileTemplateUri": "",
    "iscsiInitiatorName": "",
    "templateCompliance": "",
    "serverHardwareUri": "",
    "enclosureBay": 1,
    "name": "",
    "serialNumber": "",
    "enclosureGroupUri": "",
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": [],
        "sanSystemCredentials": []
    }
}


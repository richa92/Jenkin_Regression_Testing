admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

#enclosure_name = "0000A66103"

#drive_enclosure_name = "0000A66103, bay 7"

expected_number_of_DE = 6

enclosures = [{
    "managerBays": [
        {
            "mgmtPortSpeedGbs": "10",
            "devicePresence": "Present",
            "bayPowerState": "Unknown",
            "linkedEnclosure": {
                "serialNumber": "0000A66102",
                "bayNumber": 2
            },
            "linkPortStatus": "OK",
            "fwVersion": "1.00.00",
            "role": "Active",
            "mgmtPortState": "Active",
            "changeState": "None",
            "mgmtPortLinkState": "Linked",
            "status": "OK",
            "uidState": "Off",
            "sparePartNumber": "807963-001",
            "fwBuildDate": "11/12/2014,01:53:01",
            "mgmtPortStatus": "OK",
            "linkPortState": "Linked",
            "model": "HP Synergy Frame Link Module",
            "negotiatedLinkPortSpeedGbs": 1,
            "managerType": "EnclosureManager",
            "linkPortIsolated": False,
            "serialNumber": "0000A66103",
            "linkPortSpeedGbs": "10",
            "negotiatedMgmtPortSpeedGbs": 1,
            "partNumber": "802341-B21",
            "ipAddress": "fe80::2:0:9:5%eth2",
            "bayNumber": 1
        },
        {
            "mgmtPortSpeedGbs": "10",
            "devicePresence": "Present",
            "bayPowerState": "Unknown",
            "linkedEnclosure": {
                "serialNumber": "0000A66101",
                "bayNumber": 1
            },
            "linkPortStatus": "OK",
            "fwVersion": "1.00.00",
            "role": "Standby",
            "mgmtPortState": "Standby",
            "changeState": "None",
            "mgmtPortLinkState": "Unlinked",
            "status": "OK",
            "uidState": "Off",
            "sparePartNumber": "807963-001",
            "fwBuildDate": "11/12/2014,01:53:01",
            "mgmtPortStatus": "OK",
            "linkPortState": "Linked",
            "model": "HP Synergy Frame Link Module",
            "negotiatedLinkPortSpeedGbs": 1,
            "managerType": "EnclosureManager",
            "linkPortIsolated": False,
            "serialNumber": "0000A66103",
            "linkPortSpeedGbs": "10",
            "negotiatedMgmtPortSpeedGbs": 0,
            "partNumber": "802341-B21",
            "ipAddress": "fe80::2:0:9:6%eth2",
            "bayNumber": 2
        }
    ],
    "minimumPowerSuppliesForRedundantPowerFeed": 4,
    "interconnectBayCount": 6,
    "isFwManaged": False,
    "powerAllocatedWatts": 4688,
    "fwBaselineUri": None,
    "uuid": "0000000000A66103",
    "managerBayCount": 2,
    "licensingIntent": "NotApplicable",
    "description": None,
    "powerCapacityBoostWatts": 3500,
    "fwBaselineName": None,
    "powerAvailableWatts": 6352,
    "stateReason": "None",
    "type": "EnclosureV300",
    "interconnectBayWatts": 98,
    "uidState": "On",
    "reconfigurationState": "NotReapplyingConfiguration",
    "applianceBayCount": 2,
    "enclosureTypeUri": "EncTypes:Synergy 12000 Frame",
    "refreshState": "NotRefreshing",
    "enclosureModel": "Synergy 12000 Frame",
    "name": "0000A66103",
    "fanBayCount": 10,
    "enclosureGroupUri": None,
    "powerSupplyBays": [
        {
            "status": "OK",
            "serialNumber": "BD341757XY",
            "changeState": "None",
            "sparePartNumber": "000000-010",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "outputCapacityWatts": 2650,
            "model": "HP Power Supply",
            "devicePresence": "Present",
            "partNumber": "0000008710",
            "bayNumber": 1
        },
        {
            "status": "OK",
            "serialNumber": "BD341767XY",
            "changeState": "None",
            "sparePartNumber": "000000-010",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "outputCapacityWatts": 2650,
            "model": "HP Power Supply",
            "devicePresence": "Present",
            "partNumber": "0000008710",
            "bayNumber": 2
        },
        {
            "status": "OK",
            "serialNumber": "BD341777XY",
            "changeState": "None",
            "sparePartNumber": "000000-010",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "outputCapacityWatts": 2650,
            "model": "HP Power Supply",
            "devicePresence": "Present",
            "partNumber": "0000008710",
            "bayNumber": 3
        },
        {
            "status": "OK",
            "serialNumber": "BD341787XY",
            "changeState": "None",
            "sparePartNumber": "000000-010",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "outputCapacityWatts": 2650,
            "model": "HP Power Supply",
            "devicePresence": "Present",
            "partNumber": "0000008710",
            "bayNumber": 4
        },
        {
            "status": "OK",
            "serialNumber": "BD341797XY",
            "changeState": "None",
            "sparePartNumber": "000000-010",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "outputCapacityWatts": 2650,
            "model": "HP Power Supply",
            "devicePresence": "Present",
            "partNumber": "0000008710",
            "bayNumber": 5
        },
        {
            "status": "OK",
            "serialNumber": "BD341807XY",
            "changeState": "None",
            "sparePartNumber": "000000-010",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "outputCapacityWatts": 2650,
            "model": "HP Power Supply",
            "devicePresence": "Present",
            "partNumber": "0000008710",
            "bayNumber": 6
        }
    ],
    "powerSupplyBayCount": 6,
    "fanBays": [
        {
            "status": "OK",
            "serialNumber": "3C34431020",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 1,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431021",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 2,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431022",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 3,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431023",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 4,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431024",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 5,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431025",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 6,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431026",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 7,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431027",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 8,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431028",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 9,
            "deviceRequired": True
        },
        {
            "status": "OK",
            "serialNumber": "3C34431029",
            "changeState": "None",
            "sparePartNumber": "0256002301",
            "fanBayType": "SY12000FanBay",
            "model": "Fan Module",
            "devicePresence": "Present",
            "partNumber": "0008568710",
            "bayNumber": 10,
            "deviceRequired": True
        }
    ],
    "interconnectBays": [
        {
            "ipv4Setting": None,
            "logicalInterconnectUri": None,
            "interconnectModel": "HPE Synergy 12Gb SAS Connection Module",
            "powerAllocationWatts": 32,
            "bayPowerState": "Unknown",
            "serialNumber": "2M220104SL",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": False,
            "changeState": "None",
            "interconnectUri": "SasIC:0000A66103, interconnect 1",
            "bayNumber": 1
        },
        {
            "ipv4Setting": None,
            "logicalInterconnectUri": None,
            "interconnectModel": None,
            "powerAllocationWatts": None,
            "bayPowerState": "Unknown",
            "serialNumber": None,
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": None,
            "changeState": "None",
            "interconnectUri": None,
            "bayNumber": 2
        },
        {
            "ipv4Setting": None,
            "logicalInterconnectUri": None,
            "interconnectModel": "HP Synergy Interconnect Link Module",
            "powerAllocationWatts": 17,
            "bayPowerState": "Unknown",
            "serialNumber": "0000A55102",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": False,
            "changeState": "None",
            "interconnectUri": "IC:0000A66103, interconnect 3",
            "bayNumber": 3
        },
        {
            "ipv4Setting": None,
            "logicalInterconnectUri": None,
            "interconnectModel": "HPE Synergy 12Gb SAS Connection Module",
            "powerAllocationWatts": 32,
            "bayPowerState": "Unknown",
            "serialNumber": "2M220105SL",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": False,
            "changeState": "None",
            "interconnectUri": "SasIC:0000A66103, interconnect 4",
            "bayNumber": 4
        },
        {
            "ipv4Setting": None,
            "logicalInterconnectUri": None,
            "interconnectModel": None,
            "powerAllocationWatts": None,
            "bayPowerState": "Unknown",
            "serialNumber": None,
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": None,
            "changeState": "None",
            "interconnectUri": None,
            "bayNumber": 5
        },
        {
            "ipv4Setting": None,
            "logicalInterconnectUri": None,
            "interconnectModel": "HP Synergy Interconnect Link Module",
            "powerAllocationWatts": 17,
            "bayPowerState": "Unknown",
            "serialNumber": "0000A55103",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": False,
            "changeState": "None",
            "interconnectUri": "IC:0000A66103, interconnect 6",
            "bayNumber": 6
        }
    ],
    "category": "enclosures",
    "deviceBayWatts": 4000,
    "state": "Monitored",
    "version": "G1",
    "applianceBays": [
        {
            "status": None,
            "sparePartNumber": None,
            "devicePresence": "Absent",
            "partNumber": None,
            "containedRisResources": None,
            "bayPowerState": "Unknown",
            "poweredOn": False,
            "serialNumber": None,
            "originOfCondition": None,
            "enclosureUri": "ENC:0000A66103",
            "model": None,
            "deviceUri": None,
            "bayNumber": 1
        },
        {
            "status": None,
            "sparePartNumber": None,
            "devicePresence": "Absent",
            "partNumber": None,
            "containedRisResources": None,
            "bayPowerState": "Unknown",
            "poweredOn": False,
            "serialNumber": None,
            "originOfCondition": None,
            "enclosureUri": "ENC:0000A66103",
            "model": None,
            "deviceUri": None,
            "bayNumber": 2
        }
    ],
    "status": "OK",
    "forceInstallFirmware": False,
    "minimumPowerSupplies": 2,
    "deviceBayCount": 12,
    "powerMode": "RedundantPowerFeed",
    "fansAndManagementDevicesWatts": 590,
    "serialNumber": "0000A66103",
    "uri": "ENC:0000A66103",
    "enclosureType": "SY12000",
    "powerCapacityWatts": 7950,
    "logicalEnclosureUri": None,
    "partNumber": "000000-010",
    "deviceBays": [
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "DE:0000A66103, bay 1",
            "deviceFormFactor": "SingleHeightDoubleWideStorage",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": False,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "DE:0000A66103, bay 1",
            "bayNumber": 1,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "DE:0000A66103, bay 1",
            "deviceFormFactor": "SingleHeightDoubleWideStorage",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": False,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Subsumed",
            "type": "DeviceBayV300",
            "deviceUri": None,
            "bayNumber": 2,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 3",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 3",
            "bayNumber": 3,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 4",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 4",
            "bayNumber": 4,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 5",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 5",
            "bayNumber": 5,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 6",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 6",
            "bayNumber": 6,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "DE:0000A66103, bay 7",
            "deviceFormFactor": "SingleHeightDoubleWideStorage",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": False,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "DE:0000A66103, bay 7",
            "bayNumber": 7,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "DE:0000A66103, bay 7",
            "deviceFormFactor": "SingleHeightDoubleWideStorage",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": False,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Subsumed",
            "type": "DeviceBayV300",
            "deviceUri": None,
            "bayNumber": 8,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 9",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 9",
            "bayNumber": 9,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 10",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 10",
            "bayNumber": 10,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 11",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 11",
            "bayNumber": 11,
            "deviceBayType": "SY12000DeviceBay"
        },
        {
            "category": "device-bays",
            "coveredByProfile": None,
            "bayPowerState": "Unknown",
            "coveredByDevice": "SH:0000A66103, bay 12",
            "deviceFormFactor": "SingleHeightSingleWide",
            "availableForFullHeightProfile": False,
            "changeState": "None",
            "profileUri": None,
            "availableForHalfHeightProfile": True,
            "ipv4Setting": None,
            "model": None,
            "devicePresence": "Present",
            "type": "DeviceBayV300",
            "deviceUri": "SH:0000A66103, bay 12",
            "bayNumber": 12,
            "deviceBayType": "SY12000DeviceBay"
        }
    ]
}]


drive_enclosures = [{
    "status_code": 200,
    "interconnectBaySet": 1,
    "description": "",
    "category": "drive-enclosures",
    "driveEnclosureTypeUri": "DETypes:HPESynergyD3940StorageModule",
    "firmwareVersion": "0.18",
    "stateReason": "",
    "interconnectUri": None,
    "type": "drive-enclosure",
    "enclosureUri": "ENC:0000A66103",
#    "uidState": "Off",
    "driveBays": [
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 26", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "26"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 36", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "36"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 27", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "27"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 8", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "8"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 29", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "29"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 34", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "34"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 10", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "10"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 32", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "32"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 22", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "22"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 33", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "33"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 31", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "31"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 6", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "6"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 5", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "5"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 19", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "19"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 20", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "20"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 16", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "16"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 7", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "7"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 1", 
            "attachedDeviceWWID": "5001410211D3717F", 
            "drive": {
                "buffered": None, 
                "rotationalRpms": 7200, 
                "firmwareVersion": "HP01", 
                "description": "", 
                "category": "drives", 
                "capacity": "1907729", 
                "temperature": -29, 
                "blockSize": 512, 
                "state": "Enabled", 
                "stateReason": None, 
                "driveType": {
                    "description": "", 
                    "driveMedia": "Unknown", 
                    "category": "drive-types", 
                    "formFactor": None, 
                    "capacity": "1907729", 
                    "name": "SAS Unknown 1907729", 
                    "deviceInterface": "SAS", 
                    "model": "MM2000JEFRC", 
                    "type": "drive-type"
                }, 
                "type": "drive", 
                "status": "OK", 
                "uidState": "Unknown", 
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "Box", 
                            "value": "4"
                        }, 
                        {
                            "type": "SasPort", 
                            "value": "7"
                        }, 
                        {
                            "type": "Bay", 
                            "value": "1"
                        }
                    ]
                }, 
                "refreshState": "NotRefreshing", 
                "linkRateInGbs": 12, 
                "authentic": None, 
                "model": "MM2000JEFRC", 
                "manufacturer": "HPE", 
                "name": "Drive 1", 
                "serialNumber": "S46016790120J4524YPT", 
                "partNumber": None, 
                "wwid": "5000CCA03C6DB120"
            }, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "1"
                    }
                ]
            }, 
            "attachedDeviceInterface": "SAS", 
            "model": "SAS 1907729", 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 35", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "35"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 30", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "30"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 28", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "28"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 23", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "23"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 25", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "25"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 9", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "9"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 21", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "21"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 12", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "12"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 38", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "38"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 14", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "14"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 2", 
            "attachedDeviceWWID": "5001410212D3717F", 
            "drive": {
                "buffered": None, 
                "rotationalRpms": 7200, 
                "firmwareVersion": "HP01", 
                "description": "", 
                "category": "drives", 
                "capacity": "1907729", 
                "temperature": -19, 
                "blockSize": 512, 
                "state": "Enabled", 
                "stateReason": None, 
                "driveType": {
                    "description": "", 
                    "driveMedia": "Unknown", 
                    "category": "drive-types", 
                    "formFactor": None, 
                    "capacity": "1907729", 
                    "name": "SAS Unknown 1907729", 
                    "deviceInterface": "SAS", 
                    "model": "MM2000JEFRC", 
                    "type": "drive-type"
                }, 
                "type": "drive", 
                "status": "OK", 
                "uidState": "Unknown", 
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "Box", 
                            "value": "4"
                        }, 
                        {
                            "type": "SasPort", 
                            "value": "7"
                        }, 
                        {
                            "type": "Bay", 
                            "value": "2"
                        }
                    ]
                }, 
                "refreshState": "NotRefreshing", 
                "linkRateInGbs": 12, 
                "authentic": None, 
                "model": "MM2000JEFRC", 
                "manufacturer": "HPE", 
                "name": "Drive 2", 
                "serialNumber": "S46016790121J4524YPT", 
                "partNumber": None, 
                "wwid": "5000CCA03C6DB121"
            }, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "2"
                    }
                ]
            }, 
            "attachedDeviceInterface": "SAS", 
            "model": "SAS 1907729", 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 11", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "11"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 24", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "24"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 40", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "40"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 17", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "17"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 37", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "37"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 39", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "39"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 4", 
            "attachedDeviceWWID": "5001410214D3717F", 
            "drive": {
                "buffered": None, 
                "rotationalRpms": 7200, 
                "firmwareVersion": "HP01", 
                "description": "", 
                "category": "drives", 
                "capacity": "1907729", 
                "temperature": 11, 
                "blockSize": 512, 
                "state": "Enabled", 
                "stateReason": None, 
                "driveType": {
                    "description": "", 
                    "driveMedia": "Unknown", 
                    "category": "drive-types", 
                    "formFactor": None, 
                    "capacity": "1907729", 
                    "name": "SAS Unknown 1907729", 
                    "deviceInterface": "SAS", 
                    "model": "MM2000JEFRC", 
                    "type": "drive-type"
                }, 
                "type": "drive", 
                "status": "OK", 
                "uidState": "Unknown", 
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "Box", 
                            "value": "4"
                        }, 
                        {
                            "type": "Bay", 
                            "value": "4"
                        }, 
                        {
                            "type": "SasPort", 
                            "value": "7"
                        }
                    ]
                }, 
                "refreshState": "NotRefreshing", 
                "linkRateInGbs": 12, 
                "authentic": None, 
                "model": "MM2000JEFRC", 
                "manufacturer": "HPE", 
                "name": "Drive 4", 
                "serialNumber": "S46016790123J4524YPT", 
                "partNumber": None, 
                "wwid": "5000CCA03C6DB123"
            }, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "4"
                    }
                ]
            }, 
            "attachedDeviceInterface": "SAS", 
            "model": "SAS 1907729", 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 15", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "15"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 13", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "13"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 18", 
            "attachedDeviceWWID": None, 
            "drive": None, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "18"
                    }
                ]
            }, 
            "attachedDeviceInterface": "NODEV", 
            "model": None, 
            "type": "drive-bay", 
            "description": None
        }, 
        {
            "status": None, 
            "category": "drive-bays", 
            "sasLogicalJBODUri": None, 
            "name": "Drive Bay 3", 
            "attachedDeviceWWID": "5001410213D3717F", 
            "drive": {
                "buffered": None, 
                "rotationalRpms": 7200, 
                "firmwareVersion": "HP01", 
                "description": "", 
                "category": "drives", 
                "capacity": "1907729", 
                "temperature": 1, 
                "blockSize": 512, 
                "state": "Enabled", 
                "stateReason": None, 
                "driveType": {
                    "description": "", 
                    "driveMedia": "Unknown", 
                    "category": "drive-types", 
                    "formFactor": None, 
                    "capacity": "1907729", 
                    "name": "SAS Unknown 1907729", 
                    "deviceInterface": "SAS", 
                    "model": "MM2000JEFRC", 
                    "type": "drive-type"
                }, 
                "type": "drive", 
                "status": "OK", 
                "uidState": "Unknown", 
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "Box", 
                            "value": "4"
                        }, 
                        {
                            "type": "SasPort", 
                            "value": "7"
                        }, 
                        {
                            "type": "Bay", 
                            "value": "3"
                        }
                    ]
                }, 
                "refreshState": "NotRefreshing", 
                "linkRateInGbs": 12, 
                "authentic": None, 
                "model": "MM2000JEFRC", 
                "manufacturer": "HPE", 
                "name": "Drive 3", 
                "serialNumber": "S46016790122J4524YPT", 
                "partNumber": None, 
                "wwid": "5000CCA03C6DB122"
            }, 
            "state": "UnConfigured", 
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay", 
                        "value": "3"
                    }
                ]
            }, 
            "attachedDeviceInterface": "SAS", 
            "model": "SAS 1907729", 
            "type": "drive-bay", 
            "description": None
        }
    ],
    "ioAdapterCount": 2,
    "driveBayCount": 40,
    "productName": "Storage Enclosure 5001438031529D6",
    "driveEnclosurePortMap": {
        "type": "DriveEnclosurePortMap",
        "deviceSlots": [
            {
                "physicalPorts": [
                    {
                        "interconnectPortNumber": "7",
                        "physicalInterconnectName": "0000A66103, interconnect 4",
                        "physicalInterconnectPortNumber": "7",
                        "physicalInterconnectUri": "SasIC:0000A66103, interconnect 4",
                        "interconnectName": "0000A66103, interconnect 4",
                        "interconnectUri": "SasIC:0000A66103, interconnect 4",
                        "type": "SAS"
                    },
                    {
                        "interconnectPortNumber": "8",
                        "physicalInterconnectName": "0000A66103, interconnect 4",
                        "physicalInterconnectPortNumber": "8",
                        "physicalInterconnectUri": "SasIC:0000A66103, interconnect 4",
                        "interconnectName": "0000A66103, interconnect 4",
                        "interconnectUri": "SasIC:0000A66103, interconnect 4",
                        "type": "SAS"
                    }
                ],
                "deviceName": None,
                "slotNumber": "1",
                "location": "IO Adapter"
            },
            {
                "physicalPorts": None,
                "deviceName": None,
                "slotNumber": "2",
                "location": "IO Adapter"
            }
        ]
    },
    "refreshState": None,
    "ioAdapters": [
        {
            "description": "",
            "ioAdapterLocation": {
                "locationEntries": [
                    {
                        "type": "Slot",
                        "value": "2"
                    }
                ]
            },
            "partNumber": "755872-001",
            "firmwareVersion": "0.50",
            "manufacturer": "HPE",
            "category": "",
            "name": None,
            "portCount": 2,
            "serialNumber": "50454e5445305111",
            "ports": [],
            "model": "HPE Synergy 12Gb SAS Storage IO Adapter",
            "type": "drive-enclosure-ioadapter",
            "wwid": "5001438031111DBC"
        },
        {
            "description": "",
            "ioAdapterLocation": {
                "locationEntries": [
                    {
                        "type": "Slot",
                        "value": "1"
                    }
                ]
            },
            "partNumber": "755872-001",
            "firmwareVersion": "0.50",
            "manufacturer": "HPE",
            "category": "",
            "name": None,
            "portCount": 2,
            "serialNumber": "50454e5445305110",
            "ports": [
                {
                    "description": None,
                    "portLocation": "7",
                    "portName": "7",
                    "portStatusReason": None,
                    "phyCount": 4,
                    "name": "7",
                    "category": "sas-ports",
                    "containerDeviceUri": "DE:0000A66103, bay 7",
                    "enabled": True,
                    "portIdentifier": "1",
                    "portType": "Downlink",
                    "type": "sas-port"
                },
                {
                    "description": None,
                    "portLocation": "8",
                    "portName": "8",
                    "portStatusReason": None,
                    "phyCount": 4,
                    "name": "8",
                    "category": "sas-ports",
                    "containerDeviceUri": "DE:0000A66103, bay 7",
                    "enabled": True,
                    "portIdentifier": "2",
                    "portType": "Downlink",
                    "type": "sas-port"
                }
            ],
            "model": "HPE Synergy 12Gb SAS Storage IO Adapter",
            "type": "drive-enclosure-ioadapter",
            "wwid": "5001438031110DBC"
        }

    ],
    "partNumber": "755975-001",
    "manufacturer": "HPE",
#    "powerState": "On",
    "name": "0000A66103, bay 7",
    "driveEnclosureLocation": {
        "locationEntries": [
            {
                "type": "Bay",
                "value": "7"
            },
            {
                "type": "Enclosure",
                "value": "ENC:0000A66103"
            }

        ]
    },
    "serialNumber": "SN123105",
    "uri": "DE:0000A66103, bay 7",
    "bay": 7,
    "enclosureName": "0000A66103",
    "model": "HPE Synergy D3940 Storage Module",
    "wwid": "5001438031529D6"
}]
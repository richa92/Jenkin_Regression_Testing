admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

expected_number_of_DE = 1

ENC1 = "CN75120D7B"

enclosures = [{
    "powerSupplyBays": [
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\\d{6}-001",
            "outputCapacityWatts": "RANGE:1325:3975",
            "serialNumber": "REGEX:\w*",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "model": "2650W AC Titanium Hot Plug Power Supply",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 1
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\\d{6}-001",
            "outputCapacityWatts": "RANGE:1325:3975",
            "serialNumber": "REGEX:\w*",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "model": "2650W AC Titanium Hot Plug Power Supply",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 2
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\\d{6}-001",
            "outputCapacityWatts": "RANGE:1325:3975",
            "serialNumber": "REGEX:\w*",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "model": "2650W AC Titanium Hot Plug Power Supply",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 3
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\\d{6}-001",
            "outputCapacityWatts": "RANGE:1325:3975",
            "serialNumber": "REGEX:\w*",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "model": "2650W AC Titanium Hot Plug Power Supply",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 4
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\\d{6}-001",
            "outputCapacityWatts": "RANGE:1325:3975",
            "serialNumber": "REGEX:\w*",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "model": "2650W AC Titanium Hot Plug Power Supply",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 5
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\\d{6}-001",
            "outputCapacityWatts": "RANGE:1325:3975",
            "serialNumber": "REGEX:\w*",
            "powerSupplyBayType": "SY12000PowerSupplyBay",
            "model": "2650W AC Titanium Hot Plug Power Supply",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 6
        }
    ],
    "managerBays": [
        {
            "mgmtPortSpeedGbs": "10",
            "devicePresence": "Present",
            "linkedEnclosure": {
                "serialNumber": "REGEX:\w*",
                "bayNumber": 2
            },
            "mgmtPortNeighbor": {
                "macAddress": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                "description": "REGEX:ProCurve J9022A Switch.*",
                "port": "REGEX:\d"
            },
            "linkPortStatus": "OK",
            "fwVersion": "2.00.00",
            "mgmtPortLinkState": "Linked",
            "status": "OK",
            "sparePartNumber": "807963-001",
            "mgmtPortStatus": "OK",
            "linkPortState": "Linked",
            "partNumber": "REGEX:\d{6}-B21",
            "negotiatedLinkPortSpeedGbs": 10,
            "managerType": "EnclosureManager",
            "serialNumber": "REGEX:\w*",
            "linkPortSpeedGbs": "10",
            "negotiatedMgmtPortSpeedGbs": 1,
            "model": "Synergy Frame Link Module",
            "ipAddress": "REGEX:fe80::([0-9a-fA-F]{4}:){3}[0-9a-fA-F]",
            "bayNumber": 1
        },
        {
            "mgmtPortSpeedGbs": "10",
            "devicePresence": "Present",
            "linkedEnclosure": {
                "serialNumber": "REGEX:\w*",
                "bayNumber": 1
            },
            "mgmtPortNeighbor": None,
            "linkPortStatus": "OK",
            "fwVersion": "2.00.00",
            "mgmtPortLinkState": "Unlinked",
            "status": "OK",
            "sparePartNumber": "807963-001",
            "mgmtPortStatus": "OK",
            "linkPortState": "Linked",
            "partNumber": "REGEX:\d{6}-B21",
            "negotiatedLinkPortSpeedGbs": 10,
            "managerType": "EnclosureManager",
            #            "linkPortIsolated": False,
            "serialNumber": "REGEX:\w*",
            "linkPortSpeedGbs": "10",
            "negotiatedMgmtPortSpeedGbs": 0,
            "model": "Synergy Frame Link Module",
            "ipAddress": "REGEX:fe80::([0-9a-fA-F]{4}:){3}[0-9a-fA-F]",
            "bayNumber": 2
        }
    ],
    "minimumPowerSuppliesForRedundantPowerFeed": 2,
    "interconnectBayCount": 6,
    "isFwManaged": False,
    "fanBays": [
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 1
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 2
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 3
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 4
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 5
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 6
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 7
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 8
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 9
        },
        {
            "status": "OK",
            "sparePartNumber": "REGEX:\d{6}-001",
            "serialNumber": "REGEX:\w*",
            "deviceRequired": True,
            "fanBayType": "SY12000FanBay",
            "model": "Synergy Fan Module",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-001",
            "bayNumber": 10
        }
    ],
    "remoteSupportSettings": {
        "destination": "",
    },
    "powerAllocatedWatts": "RANGE:500:5000",
    "category": "enclosures",
    "reconfigurationState": "NotReapplyingConfiguration",
    "managerBayCount": 2,
    "licensingIntent": "NotApplicable",
    # Blades must be powered on. "deviceBayWatts": "RANGE:100:2000",
    # "powerCapacityBoostWatts": "RANGE:100:600",
    "state": "Monitored",
    "powerAvailableWatts": "RANGE:3255:9763",
    "powerSupplyBayCount": 6,
    "frameLinkModuleDomain": "local",
    "version": "G1",
    "deviceBayCount": 12,
    "interconnectBays": [
        {
            "serialNumber": "REGEX:\w*",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": True,
            "interconnectModel": "Synergy 12Gb SAS Connection Module",
            "interconnectUri": "SasIC:" + ENC1 + ", interconnect 1",
            "bayNumber": 1
        },
        {
            "interconnectBayType": "SY12000InterconnectBay",
            "bayNumber": 2
        },
        {
            "serialNumber": "REGEX:\w*",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": True,
            "interconnectModel": "Virtual Connect SE 40Gb F8 Module for Synergy",
            "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
            "bayNumber": 3
        },
        {
            "serialNumber": "REGEX:\w*",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": True,
            "interconnectModel": "Synergy 12Gb SAS Connection Module",
            "interconnectUri": "SasIC:" + ENC1 + ", interconnect 4",
            "bayNumber": 4
        },
        {
            "interconnectBayType": "SY12000InterconnectBay",
            "bayNumber": 5
        },
        {
            "serialNumber": "REGEX:\w*",
            "interconnectBayType": "SY12000InterconnectBay",
            "serialConsole": False,
            "interconnectModel": "Synergy 20Gb Interconnect Link Module",
            "interconnectUri": "IC:" + ENC1 + ", interconnect 6",
            "bayNumber": 6
        }
    ],
    "type": "EnclosureV400",
    "interconnectBayWatts": "RANGE:151:451",
    "status": "REGEX:(OK|Warning)",
    # "forceInstallFirmware": False,
    "minimumPowerSupplies": 1,
    "applianceBayCount": 2,
    "enclosureTypeUri": "EncTypes:Synergy 12000 Frame",
    "powerMode": "RedundantPowerFeed",
    "applianceBays": [
        {
            "status": "REGEX:(OK|Warning)",
            "sparePartNumber": "REGEX:\d{6}-001",
            "poweredOn": True,
            "serialNumber": "REGEX:\w*",
            "model": "Synergy Composer",
            "devicePresence": "Present",
            "partNumber": "REGEX:\d{6}-B21",
            "bayNumber": 1
        },
        {
            "poweredOn": False,
            "devicePresence": "Absent",
            # Will need to remove if they remove this from api spec
            "bayNumber": 2
        }
    ],
    "fansAndManagementDevicesWatts": "RANGE:500:1500",
    "enclosureModel": "Synergy 12000 Frame",
    "name": ENC1,
    "fanBayCount": 10,
    "serialNumber": ENC1,
    "uri": "ENC:" + ENC1,
    "enclosureType": "SY12000",
    "powerCapacityWatts": "RANGE:3975:11925",
    "supportState": "Disabled",
    "partNumber": "REGEX:\d{6}-010",
    "deviceBays": [
        {
            "type": "DeviceBayV400",
            "bayNumber": 1,
            "devicePresence": "Present",
            "coveredByDevice": "DE:" + ENC1 + ", bay 1",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "SingleHeightDoubleWideStorage",
            "category": "device-bays",
            "serialNumber": "REGEX:\w*"
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 2,
            "devicePresence": "Subsumed",
            "coveredByDevice": "DE:" + ENC1 + ", bay 1",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "SingleHeightDoubleWideStorage",
            "category": "device-bays",
            "serialNumber": "REGEX:\w*"
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 3,
            "devicePresence": "Present",
            "coveredByDevice": "SH:" + ENC1 + ", bay 3",
            "availableForFullHeightDoubleWideProfile": True,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "DoubleHeightDoubleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 4,
            "devicePresence": "Subsumed",
            "coveredByDevice": "SH:" + ENC1 + ", bay 3",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "DoubleHeightDoubleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 5,
            "devicePresence": "Present",
            "coveredByDevice": "SH:" + ENC1 + ", bay 5",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": True,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "DoubleHeightSingleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 6,
            "devicePresence": "Absent",
            "coveredByDevice": None,
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": True,
            "availableForFullHeightProfile": True,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "Empty",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 7,
            "devicePresence": "Present",
            "coveredByDevice": "SH:" + ENC1 + ", bay 7",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": True,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "SingleHeightSingleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 8,
            "devicePresence": "Absent",
            "coveredByDevice": None,
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": True,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "Empty",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 9,
            "devicePresence": "Subsumed",
            "coveredByDevice": "SH:" + ENC1 + ", bay 3",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "DoubleHeightDoubleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 10,
            "devicePresence": "Subsumed",
            "coveredByDevice": "SH:" + ENC1 + ", bay 3",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "DoubleHeightDoubleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 11,
            "devicePresence": "Subsumed",
            "coveredByDevice": "SH:" + ENC1 + ", bay 5",
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": False,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "DoubleHeightSingleWide",
            "category": "device-bays",
        },
        {
            "type": "DeviceBayV400",
            "bayNumber": 12,
            "devicePresence": "Absent",
            "coveredByDevice": None,
            "availableForFullHeightDoubleWideProfile": False,
            "availableForHalfHeightDoubleWideProfile": False,
            "availableForHalfHeightProfile": True,
            "availableForFullHeightProfile": False,
            "deviceBayType": "SY12000DeviceBay",
            "deviceFormFactor": "Empty",
            "category": "device-bays",
        }
    ]
}
]

drive_enclosures = [{
    "category": "drive-enclosures",
    "state": "Monitored",
    "interconnectBaySet": 1,
    "interconnectUri": [
        "SasIC:" + ENC1 + ", interconnect 4",
        "SasIC:" + ENC1 + ", interconnect 1"
    ],
    "type": "drive-enclosure",
    "enclosureUri": "ENC:" + ENC1,
    "status": "REGEX:(OK|Warning)",
    "description": "",
    "driveBays": [
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-1",
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "1"
                    }
                ]
            },
            "attachedDeviceInterface": "NODEV",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-2",
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "2"
                    }
                ]
            },
            "attachedDeviceInterface": "NODEV",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-3",
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "3"
                    }
                ]
            },
            "attachedDeviceInterface": "NODEV",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-4",
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "4"
                    }
                ]
            },
            "attachedDeviceInterface": "NODEV",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-5",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-6",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-7",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-8",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-9",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-10",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-11",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-12",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-13",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-14",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-15",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-16",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-17",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-18",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-19",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-20",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-21",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-22",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-23",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-24",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-25",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-26",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-27",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-28",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-29",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-30",
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
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-31",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:31",
                    "1:1:31"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "31"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 31-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "31"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-32",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:32",
                    "1:1:32"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "32"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 32-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "32"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-33",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:33",
                    "1:1:33"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "33"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 33-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "33"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-34",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:34",
                    "1:1:34"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "34"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 34-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "34"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-35",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:35",
                    "1:1:35"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "35"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 35-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "35"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-36",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:36",
                    "1:1:36"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "36"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 36-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "36"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-37",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:37",
                    "1:1:37"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        },
                        {
                            "type": "Bay",
                            "value": "37"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 37-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "37"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-38",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:38",
                    "1:1:38"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "38"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 38-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "38"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-39",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:39",
                    "1:1:39"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "39"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 39-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "39"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        },
        {
            "category": "drive-bays",
            "name": "REGEX:[0-9A-F]{16}-BayID-40",
            "attachedDeviceWWID": "REGEX:[0-9A-F]{16}",
            "drive": {
                "drivePaths": [
                    "1:4:40",
                    "1:1:40"
                ],
                "rotationalRpms": "RANGE:1500:15050",
                "firmwareVersion": "REGEX:HPD\w",
                "category": "drives",
                "capacity": "146",
                "blockSize": 512,
                "state": "Enabled",
                "deviceInterface": "SAS",
                "type": "drive",
                "status": "OK",
                "description": "",
                "driveMedia": "HDD",
                "driveLocation": {
                    "locationEntries": [
                        {
                            "type": "SasPort",
                            "value": "1"
                        },
                        {
                            "type": "Bay",
                            "value": "40"
                        },
                        {
                            "type": "Box",
                            "value": "REGEX:[14]"
                        }
                    ]
                },
                "linkRateInGbs": 6,
                "authentic": "yes",
                "model": "REGEX:EH0146F(ARWD|BQDC)",
                "name": "REGEX:[0-9A-F]{16}-Bay 40-Drive",
                "serialNumber": "REGEX:\w*",
                "wwid": "REGEX:[0-9A-F]{16}"
            },
            "state": "UnConfigured",
            "driveBayLocation": {
                "locationEntries": [
                    {
                        "type": "Bay",
                        "value": "40"
                    }
                ]
            },
            "attachedDeviceInterface": "SAS",
            "model": "SAS 146",
            "type": "drive-bay",
        }
    ],
    "ioAdapterCount": 2,
    "driveBayCount": 40,
    "productName": "REGEX:Storage Enclosure [0-9A-F]{16}",
    "driveEnclosurePortMap": {
        "type": "DriveEnclosurePortMap",
        "deviceSlots": [
            {
                "physicalPorts": [
                    {
                        "interconnectPortNumber": "1",
                        "physicalInterconnectName": ENC1 + ", interconnect 1",
                        "physicalInterconnectPortNumber": "1",
                        "physicalInterconnectUri": "SasIC:" + ENC1 + ", interconnect 1",
                        "interconnectName": ENC1 + ", interconnect 1",
                        "interconnectUri": "SasIC:" + ENC1 + ", interconnect 1",
                        "type": "SAS"
                    },
                    {
                        "interconnectPortNumber": "2",
                        "physicalInterconnectName": ENC1 + ", interconnect 1",
                        "physicalInterconnectPortNumber": "2",
                        "physicalInterconnectUri": "SasIC:" + ENC1 + ", interconnect 1",
                        "interconnectName": ENC1 + ", interconnect 1",
                        "interconnectUri": "SasIC:" + ENC1 + ", interconnect 1",
                        "type": "SAS"
                    }
                ],
                "slotNumber": "1",
                "location": "IO Adapter"
            },
            {
                "physicalPorts": [
                    {
                        "interconnectPortNumber": "1",
                        "physicalInterconnectName": ENC1 + ", interconnect 4",
                        "physicalInterconnectPortNumber": "1",
                        "physicalInterconnectUri": "SasIC:" + ENC1 + ", interconnect 4",
                        "interconnectName": ENC1 + ", interconnect 4",
                        "interconnectUri": "SasIC:" + ENC1 + ", interconnect 4",
                        "type": "SAS"
                    },
                    {
                        "interconnectPortNumber": "2",
                        "physicalInterconnectName": ENC1 + ", interconnect 4",
                        "physicalInterconnectPortNumber": "2",
                        "physicalInterconnectUri": "SasIC:" + ENC1 + ", interconnect 4",
                        "interconnectName": ENC1 + ", interconnect 4",
                        "interconnectUri": "SasIC:" + ENC1 + ", interconnect 4",
                        "type": "SAS"
                    }
                ],
                "slotNumber": "2",
                "location": "IO Adapter"
            }
        ]
    },
    "ioAdapters": [
        {
            "status": "OK",
            "category": "",
            "redundantIoModule": "Installed",
            "portCount": 2,
            "partNumber": "",
            "serialNumber": "REGEX:\w*",
            "ioAdapterLocation": {
                "locationEntries": [
                    {
                        "type": "Slot",
                        "value": "REGEX:[12]"
                    }
                ]
            },
            "ports": [
                {
                    "status": "OK",
                    "category": "sas-ports",
                    "containerDeviceUri": "DE:" + ENC1 + ", bay 1",
                    "enabled": True,
                    "portIdentifier": "2",
                    "portName": "2",
                    "state": "Linked",
                    "portLocation": "2",
                    "portType": "Downlink",
                    "type": "sas-port",
                    "phyCount": 4,
                    "name": "2"
                },
                {
                    "status": "OK",
                    "category": "sas-ports",
                    "containerDeviceUri": "DE:" + ENC1 + ", bay 1",
                    "enabled": True,
                    "portIdentifier": "1",
                    "portName": "1",
                    "state": "Linked",
                    "portLocation": "1",
                    "portType": "Downlink",
                    "type": "sas-port",
                    "phyCount": 4,
                    "name": "1"
                }
            ],
            "state": "Linked",
            "model": "Synergy D3940 Storage Module IO Adapter",
            "manufacturer": "HPE",
            "type": "drive-enclosure-ioadapter",
            "wwid": "REGEX:[0-9A-F]{16}",
            "description": ""
        },
        {
            "status": "OK",
            "category": "",
            "redundantIoModule": "Installed",
            "portCount": 2,
            "partNumber": "",
            "serialNumber": "REGEX:\w*",
            "ioAdapterLocation": {
                "locationEntries": [
                    {
                        "type": "Slot",
                        "value": "REGEX:[12]"
                    }
                ]
            },
            "ports": [
                {
                    "status": "OK",
                    "category": "sas-ports",
                    "containerDeviceUri": "DE:" + ENC1 + ", bay 1",
                    "enabled": True,
                    "portIdentifier": "1",
                    "portName": "1",
                    "state": "Linked",
                    "portLocation": "1",
                    "portType": "Downlink",
                    "type": "sas-port",
                    "phyCount": 4,
                    "name": "1"
                },
                {
                    "status": "OK",
                    "category": "sas-ports",
                    "containerDeviceUri": "DE:" + ENC1 + ", bay 1",
                    "enabled": True,
                    "portIdentifier": "2",
                    "portName": "2",
                    "state": "Linked",
                    "portLocation": "2",
                    "portType": "Downlink",
                    "type": "sas-port",
                    "phyCount": 4,
                    "name": "2"
                }
            ],
            "state": "Linked",
            "model": "Synergy D3940 Storage Module IO Adapter",
            "manufacturer": "HPE",
            "type": "drive-enclosure-ioadapter",
            "wwid": "REGEX:[0-9A-F]{16}",
            "description": ""
        }
    ],
    "partNumber": "REGEX:\d{6}-B21",
    "manufacturer": "HPE",
    "hardResetState": "Normal",
    "name": ENC1 + ", bay 1",
    "driveEnclosureLocation": {
        "locationEntries": [
            {
                "type": "SasPort",
                "value": "1"
            },
            {
                "type": "Bay",
                "value": "1"
            },
            {
                "type": "Enclosure",
                "value": "ENC:" + ENC1
            }
        ]
    },
    "serialNumber": "REGEX:\w*",
    "uri": "DE:" + ENC1 + ", bay 1",
    "bay": 1,
    "enclosureName": ENC1,
    "model": "Synergy D3940 Storage Module",
    "wwid": "REGEX:[0-9A-F]{16}"
}
]

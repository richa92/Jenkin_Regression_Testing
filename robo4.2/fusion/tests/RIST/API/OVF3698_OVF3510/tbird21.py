admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

# X-API-VERSION = 1000

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Enclosures
ENC1 = 'CN754406WD'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC1

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1

verify_enc = [{"type": "EnclosureV7", "name": ENC1,
               "category": "enclosures",
               "refreshState": "NotRefreshing",
               "enclosureType": "SY12000",
               "uuid": "000000CN754406WD",
               "serialNumber": "CN754406WD",
               "partNumber": "000000-010",
               "licensingIntent": "NotApplicable",
               "deviceBayCount": 12,
               "interconnectBayCount": 6,
               "fanBayCount": 10,
               "powerSupplyBayCount": 6,
               "applianceBays": [
                    {
                    "bayNumber": 1,
                    "model": "Synergy Composer",
                    "devicePresence": "Present",
                    "status": "OK",
                    "serialNumber": "UH4CCP0217",
                    "partNumber": "804353-B21",
                    "sparePartNumber": "807964-001",
                    "bayPowerState": "Unknown",
                    "poweredOn": False
                    },
                    {
                    "bayNumber": 2,
                    "model": "Synergy Composer",
                    "devicePresence": "Present",
                    "status": "OK",
                    "serialNumber": "CN753306YH",
                    "partNumber": "804353-B21",
                    "sparePartNumber": "807964-001",
                    "bayPowerState": "Unknown",
                    "poweredOn": False
                    }
                    ],
               "applianceBayCount": 2}]

verify_servers = [{
    "type": "server-hardware-10",
    "name": "CN754406WD, bay 3",
    "state": "NoProfileApplied",
    "stateReason": "NotApplicable",
    "category": "server-hardware",
    "description": None,
    "formFactor": "HalfHeight",
    "licensingIntent": "NotApplicable",
    "memoryMb": 16384,
    "migrationState": "NotApplicable",
    "model": "Synergy 480 Gen9",
    "mpHostInfo": {
        "mpHostName": "ILOHT57NP0056",
        "mpIpAddresses": [
            {
                "address": "fe80:0:0:0:eeb1:d7ff:fe79:9df7",
                "type": "LinkLocal"
            },
            {
                "address": "16.114.221.44",
                "type": "DHCP"
            }
        ]
    },
    "mpModel": "iLO4",
    "mpState": "OK",
    "partNumber": "754683-001",
    "physicalServerHardwareUri": None,
    "portMap": {
        "deviceSlots": [
            {
                "deviceName": "",
                "deviceNumber": 1,
                "location": "Mezz",
                "physicalPorts": [],
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
                        "interconnectPort": 3,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 3,
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
                        "interconnectPort": 3,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 6",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 3,
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
                                "currentAllocatedVirtualFunctionCount": 64,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "c",
                                "portNumber": 3,
                            },
                            {
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "d",
                                "portNumber": 4,
                            }
                        ],
                    }
                ],
                "slotNumber": 3
            }
        ]
    },
    "position": 3,
    "powerLock": False,
    "powerState": "Off",
    "processorCoreCount": 22,
    "processorCount": 2,
    "processorSpeedMhz": 2200,
    "processorType": "Intel(R) Xeon(R) CPU E5-2699 v4 @ 2.20GHz",
    "refreshState": "NotRefreshing",
    "serialNumber": "HT57NP0056",
    "serverGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
    "serverProfileUri": None,
    "serverSettings": None,
    "shortModel": "SY 480 Gen9",
    "status": "OK",
    "subresources": None,
    "supportDataCollectionState": None,
    "supportDataCollectionType": None,
    "supportState": "NotSupported",
    "uri": "SH:" + ENC1 + ", bay 3",
    "uuid": "36343537-3338-5448-3537-4E5030303536",
},
{
    "type": "server-hardware-10",
    "name": "CN754406WD, bay 4",
    "state": "NoProfileApplied",
    "stateReason": "NotApplicable",
    "category": "server-hardware",
    "description": None,
    "formFactor": "HalfHeight",
    "licensingIntent": "NotApplicable",
    "memoryMb": 16384,
    "migrationState": "NotApplicable",
    "model": "Synergy 480 Gen9",
    "mpHostInfo": {
        "mpHostName": "ILOHT57NP0057",
        "mpIpAddresses": [
            {
                "address": "fe80:0:0:0:eeb1:d7ff:fe79:9d9f",
                "type": "LinkLocal"
            },
            {
                "address": "16.114.221.45",
                "type": "DHCP"
            }
        ]
    },
    "mpModel": "iLO4",
    "mpState": "OK",
    "partNumber": "754683-001",
    "physicalServerHardwareUri": None,
    "portMap": {
        "deviceSlots": [
            {
                "deviceName": "",
                "deviceNumber": 1,
                "location": "Mezz",
                "physicalPorts": [],
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
                        "interconnectPort": 4,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 4,
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
                        "interconnectPort": 4,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 6",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 4,
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
                                "currentAllocatedVirtualFunctionCount": 64,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "c",
                                "portNumber": 3,
                            },
                            {
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "d",
                                "portNumber": 4,
                            }
                        ],
                    }
                ],
                "slotNumber": 3
            }
        ]
    },
    "position": 4,
    "powerLock": False,
    "powerState": "Off",
    "processorCoreCount": 10,
    "processorCount": 2,
    "processorSpeedMhz": 2100,
    "processorType": "Genuine Intel(R) CPU @ 2.10GHz",
    "refreshState": "NotRefreshing",
    "serialNumber": "CN753504M8",
    "serverGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA",
    "serverProfileUri": None,
    "serverSettings": None,
    "shortModel": "SY 480 Gen9",
    "status": "OK",
    "subresources": None,
    "supportDataCollectionState": None,
    "supportDataCollectionType": None,
    "supportState": "NotSupported",
    "uri": "SH:" + ENC1 + ", bay 4",
    "uuid": "36343537-3338-4E43-3735-333530344D38",
},
{
    "type": "server-hardware-10",
    "name": "CN754406WD, bay 6",
    "state": "NoProfileApplied",
    "stateReason": "NotApplicable",
    "category": "server-hardware",
    "description": None,
    "formFactor": "FullHeight",
    "licensingIntent": "NotApplicable",
    "memoryMb": 16384,
    "migrationState": "NotApplicable",
    "model": "Synergy 660 Gen10",
    "mpHostInfo": {
        "mpHostName": "ILOP569NP0003",
        "mpIpAddresses": [
            {
                "address": "fe80:0:0:0:1602:ecff:fe02:519c",
                "type": "LinkLocal"
            },
            {
                "address": "16.114.221.46",
                "type": "DHCP"
            }
        ]
    },
    "mpModel": "iLO5",
    "mpState": "OK",
    "partNumber": "854361-001",
    "physicalServerHardwareUri": None,
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
                    }],
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
                        "interconnectPort":6,
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
                        "interconnectPort": 6,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 6",
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
                                "currentAllocatedVirtualFunctionCount": 64,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "c",
                                "portNumber": 3,
                            },
                            {
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "d",
                                "portNumber": 4,
                            }
                        ],
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
                    }],
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
    "powerState": "Off",
    "processorCoreCount": 20,
    "processorCount": 2,
    "processorSpeedMhz": 1800,
    "processorType": "Intel(R) Genuine processor",
    "refreshState": "NotRefreshing",
    "serialNumber": "P569NP0003",
    "serverGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:SY 660 Gen10:3:Synergy 3820C 10/20Gb CNA:1:HPE Smart Array P416ie-m SR G10:4:HPE Smart Array P416ie-m SR G10",
    "serverProfileUri": None,
    "serverSettings": None,
    "shortModel": "SY 660 Gen10",
    "status": "OK",
    "subresources": None,
    "supportDataCollectionState": None,
    "supportDataCollectionType": None,
    "supportState": "NotSupported",
    "uri": "SH:" + ENC1 + ", bay 6",
    "uuid": "33343538-3136-3550-3639-4E5030303033",
},{
    "type": "server-hardware-10",
    "name": "CN754406WD, bay 7",
    "state": "NoProfileApplied",
    "stateReason": "NotApplicable",
    "category": "server-hardware",
    "description": None,
    "formFactor": "HalfHeight",
    "licensingIntent": "NotApplicable",
    "memoryMb": 8192,
    "migrationState": "NotApplicable",
    "model": "Synergy 480 Gen10",
    "mpHostInfo": {
        "mpHostName": "ILOCN76370178",
        "mpIpAddresses": [
            {
                "address": "fe80:0:0:0:1602:ecff:fe02:f083",
                "type": "LinkLocal"
            },
            {
                "address": "16.114.219.226",
                "type": "DHCP"
            }
        ]
    },
    "mpModel": "iLO5",
    "mpState": "OK",
    "partNumber": "854354-001",
    "physicalServerHardwareUri": None,
    "portMap": {
        "deviceSlots": [
            {
                "deviceName": "",
                "deviceNumber": 1,
                "location": "Mezz",
                "physicalPorts": [],
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
                        "interconnectPort": 7,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 7,
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
                        "interconnectPort": 7,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 6",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 7,
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
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "c",
                                "portNumber": 3,
                            },
                            {
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "d",
                                "portNumber": 4,
                            }
                        ],
                    }
                ],
                "slotNumber": 3
            }
        ]
    },
    "position": 7,
    "powerLock": False,
    "powerState": "Off",
    "processorCoreCount": 14,
    "processorCount": 1,
    "processorSpeedMhz": 1800,
    "processorType": "Intel(R) Genuine processor",
    "refreshState": "NotRefreshing",
    "serialNumber": "CN76370178",
    "serverGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
    "serverProfileUri": None,
    "serverSettings": None,
    "shortModel": "SY 480 Gen10",
    "status": "OK",
    "subresources": None,
    "supportDataCollectionState": None,
    "supportDataCollectionType": None,
    "supportState": "NotSupported",
    "uri": "SH:" + ENC1 + ", bay 7",
    "uuid": "33343538-3435-4E43-3736-333730313738",
},
{
    "type": "server-hardware-10",
    "name": "CN754406WD, bay 8",
    "state": "NoProfileApplied",
    "stateReason": "NotApplicable",
    "category": "server-hardware",
    "description": None,
    "formFactor": "HalfHeight",
    "licensingIntent": "NotApplicable",
    "memoryMb": 8192,
    "migrationState": "NotApplicable",
    "model": "Synergy 480 Gen10",
    "mpHostInfo": {
        "mpHostName": "ILOCN770905XJ",
        "mpIpAddresses": [
            {
                "address": "fe80:0:0:0:32e1:71ff:fe64:100c",
                "type": "LinkLocal"
            },
            {
                "address": "16.114.218.24",
                "type": "DHCP"
            }
        ]
    },
    "mpModel": "iLO5",
    "mpState": "OK",
    "partNumber": "854354-001",
    "physicalServerHardwareUri": None,
    "portMap": {
        "deviceSlots": [
            {
                "deviceName": "",
                "deviceNumber": 1,
                "location": "Mezz",
                "physicalPorts": [],
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
                        "interconnectPort": 8,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 3",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 8,
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
                        "interconnectPort": 8,
                        "interconnectUri": "IC:" + ENC1 + ", interconnect 6",
                        "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                        "physicalInterconnectPort": 8,
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
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "c",
                                "portNumber": 3,
                            },
                            {
                                "currentAllocatedVirtualFunctionCount": 0,
                                "mac": "REGEX:([0-9a-fA-F]{2}:){5}[0-9a-fA-F]",
                                "portFunction": "d",
                                "portNumber": 4,
                            }
                        ],
                    }
                ],
                "slotNumber": 3
            }
        ]
    },
    "position": 8,
    "powerLock": False,
    "powerState": "Off",
    "processorCoreCount": 16,
    "processorCount": 1,
    "processorSpeedMhz": 2100,
    "processorType": "Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz",
    "refreshState": "NotRefreshing",
    "serialNumber": "CN770905XJ",
    "serverGroupUri": "EG:" + EG_NAME,
    "serverHardwareTypeUri": "SHT:SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA",
    "serverProfileUri": None,
    "serverSettings": None,
    "shortModel": "SY 480 Gen10",
    "status": "OK",
    "subresources": None,
    "supportDataCollectionState": None,
    "supportDataCollectionType": None,
    "supportState": "NotSupported",
    "uri": "SH:" + ENC1 + ", bay 8",
    "uuid": "33343538-3435-4E43-3737-30393035584A",
}]

admin_credentials = {'userName': 'administrator', 'password': 'wpsthpvse1'}

users = [
    {'userName': 'backup', 'password': 'backupadmin', 'roles': ['Backup administrator'], 'emailAddress':'backup@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndPermissions'},
    {'userName': 'network', 'password': 'networkadmin', 'roles': ['Network administrator'], 'emailAddress':'network@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'readonly', 'password': 'readonly', 'roles': ['Read only'], 'emailAddress':'readonly@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndPermissions'},
    {'userName': 'server', 'password': 'serveradmin', 'roles': ['Server administrator'], 'emailAddress':'server@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'software', 'password': 'softwareadmin', 'roles': ['Software administrator'], 'emailAddress':'software@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'storage', 'password': 'storageadmin', 'roles': ['Storage administrator'], 'emailAddress':'storage@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
]

# Removed attributes
# *uri
# created
# modified
# temperature
# *etag
# state
# powerState
# stateReason
sas_interconnects = [
    {
        "type": "sas-interconnect",
        "firmwareVersion": "0.8.0.5",
        "partNumber": "755985-B21",
        "model": "Synergy 12Gb SAS Connection Module",
        "interconnectLocation": {
                "locationEntries": [
                    {
                        "value": "fe80::9eb6:54ff:fe90:bbf8",
                        "type": "Ip"
                    },
                    {
                        "value": "443",
                        "type": "Port"
                    },
                    {
                        "value": "/rest/enclosures/000000CN75120D77",
                        "type": "Enclosure"
                    },
                    {
                        "value": "1",
                        "type": "Bay"
                    }
                ]
        },
        "portCount": 12,
        "productName": "Synergy 12Gb SAS Connection Module",
        "interconnectIP": "fe80::9eb6:54ff:fe90:bbf8",
        "enclosureName": "CN75120D77",
        "sasWWN": "5001438034F6EC00",
        "sasPorts": [
            {
                "type": "sas-port",
                "portName": "8",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "8",
                "portLocation": "8",
                "enabled": True,
                "description": None,
                "name": "8",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "9",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "9",
                "portLocation": "9",
                "enabled": True,
                "description": None,
                "name": "9",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "1",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "1",
                "portLocation": "1",
                "enabled": True,
                "description": None,
                "name": "1",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "10",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "10",
                "portLocation": "10",
                "enabled": True,
                "description": None,
                "name": "10",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "11",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "11",
                "portLocation": "11",
                "enabled": True,
                "description": None,
                "name": "11",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "7",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "7",
                "portLocation": "7",
                "enabled": True,
                "description": None,
                "name": "7",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "3",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "3",
                "portLocation": "3",
                "enabled": True,
                "description": None,
                "name": "3",
                "status": "OK",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "6",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "6",
                "portLocation": "6",
                "enabled": True,
                "description": None,
                "name": "6",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "5",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "5",
                "portLocation": "5",
                "enabled": True,
                "description": None,
                "name": "5",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "4",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "4",
                "portLocation": "4",
                "enabled": True,
                "description": None,
                "name": "4",
                "status": "OK",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "2",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "2",
                "portLocation": "2",
                "enabled": True,
                "description": None,
                "name": "2",
                "status": "DISABLED",
                "category": "sas-ports",
            },
            {
                "type": "sas-port",
                "portName": "12",
                "portType": "Downlink",
                "portStatusReason": "None",
                "phyCount": 4,
                "portIdentifier": "12",
                "portLocation": "12",
                "enabled": True,
                "description": None,
                "name": "12",
                "status": "DISABLED",
                "category": "sas-ports",
            }
        ],
        "hardResetState": "Normal",
        "softResetState": "Normal",
        "serialNumber": "TWT546W00S",
        "refreshState": "NotRefreshing",
        "description": None,
        "name": "CN75120D77, interconnect 1",
        "status": "OK",
        "category": "sas-interconnects",
    }
]

drive_enclosures = [
    {
        "type": "drive-enclosure",
        "firmwareVersion": "1.66",
        "partNumber": "",
        "model": "Synergy D3940 Storage Module",
        "manufacturer": "HPE",
        "productName": "Storage Enclosure 5001438031531A00",
        "enclosureName": "CN75120D77",
        "interconnectBaySet": 1,
        "wwid": "5001438031531A00",
        "bay": 3,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "1",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-1",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-2",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-3",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-4",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-5",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-6",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-7",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-8",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-9",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-10",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "11",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-11",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "12",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-12",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "13",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-13",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "14",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-14",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "15",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-15",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "16",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-16",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "17",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-17",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "18",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-18",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "19",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-19",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "20",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-20",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "21",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-21",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "22",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-22",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "23",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-23",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "24",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-24",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "25",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-25",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "26",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-26",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "27",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-27",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "28",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-28",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "29",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-29",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": None,
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "30",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": None,
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "5001438031531A00-BayID-30",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C50089330E61",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD5",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C50089330E61",
                    "drivePaths": [
                        "3:1:31"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "31",
                                "type": "Bay"
                            },
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4LJ8G0000M543MPP4",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 31-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-31",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C50089331411",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C50089331411",
                    "drivePaths": [
                        "3:1:32"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "32",
                                "type": "Bay"
                            },
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4LJ6W0000M543KEC2",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 32-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-32",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C50089336959",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD5",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C50089336959",
                    "drivePaths": [
                        "3:1:33"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "33",
                                "type": "Bay"
                            },
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4LHCA0000M543S4KC",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 33-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-33",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000CCA00B9B8371",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPDD",
                    "model": "EH0146FARWD",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000CCA00B9B8371",
                    "drivePaths": [
                        "3:1:34"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "34",
                                "type": "Bay"
                            },
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15030,
                    "linkRateInGbs": 6,
                    "serialNumber": "PLXSJABE",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 34-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-34",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C5007F6E3C9D",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C5007F6E3C9D",
                    "drivePaths": [
                        "3:1:35"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            },
                            {
                                "value": "35",
                                "type": "Bay"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4EPZG0000M52949JM",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 35-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-35",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C500893340B9",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD5",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C500893340B9",
                    "drivePaths": [
                        "3:1:36"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            },
                            {
                                "value": "36",
                                "type": "Bay"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4LHQR0000M543S4Q8",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 36-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-36",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C5007F5A1E19",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD5",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C5007F5A1E19",
                    "drivePaths": [
                        "3:1:37"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            },
                            {
                                "value": "37",
                                "type": "Bay"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4E0Z50000M528K089",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 37-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-37",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C50089334701",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C50089334701",
                    "drivePaths": [
                        "3:1:38"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "38",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4LHKZ0000M543S57W",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 38-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-38",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C50089328215",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD5",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C50089328215",
                    "drivePaths": [
                        "3:1:39"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "39",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4L2860000M543MP24",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 39-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-39",
                "description": None,
                "status": None,
                "category": "drive-bays",
            },
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                        {
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "attachedDeviceWWID": "5000C500893362DD",
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD5",
                    "model": "EH0146FBQDC",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "wwid": "5000C500893362DD",
                    "drivePaths": [
                        "3:1:40"
                    ],
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "40",
                                "type": "Bay"
                            },
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "blockSize": 512,
                    "authentic": "yes",
                    "rotationalRpms": 15000,
                    "linkRateInGbs": 6,
                    "serialNumber": "6XM4LHBX0000M543KEW3",
                    "capacity": "146",
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "5001438031531A00-Bay 40-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "5001438031531A00-BayID-40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosureLocation": {
            "locationEntries": [
                {
                    "value": "/rest/enclosures/000000CN75120D77",
                    "type": "Enclosure"
                },
                {
                    "value": "3",
                    "type": "Bay"
                },
                {
                    "value": "3",
                    "type": "SasPort"
                }
            ]
        },
        "ioAdapterCount": 1,
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "physicalPorts": [
                        {
                            "interconnectName": "CN75120D77, interconnect 1",
                            "interconnectPortNumber": "3",
                            "physicalInterconnectName": "CN75120D77, interconnect 1",
                            "physicalInterconnectPortNumber": "3",
                            "type": "SAS"
                        },
                        {
                            "interconnectName": "CN75120D77, interconnect 1",
                            "interconnectPortNumber": "4",
                            "physicalInterconnectName": "CN75120D77, interconnect 1",
                            "physicalInterconnectPortNumber": "4",
                            "type": "SAS"
                        }
                    ],
                    "slotNumber": "1",
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "1.66",
                "partNumber": "",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portStatusReason": "None",
                        "portType": "Downlink",
                        "phyCount": 4,
                        "portIdentifier": "1",
                        "portLocation": "1",
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portStatusReason": "None",
                        "portType": "Downlink",
                        "phyCount": 4,
                        "portIdentifier": "2",
                        "portLocation": "2",
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    }
                ],
                "model": "Synergy D3940 Storage Module IO Adapter",
                "manufacturer": "HPE",
                "portCount": 2,
                "wwid": "5001438031531A3C",
                "redundantIoModule": "NotInstalled",
                "ioAdapterLocation": {
                        "locationEntries": [
                            {
                                "value": "1",
                                "type": "Slot"
                            }
                        ]
                },
                "serialNumber": "",
                "description": "",
                "status": "OK",
                "name": None,
                "category": "",
            }
        ],
        "driveBayCount": 40,
        "serialNumber": "CN7452064W",
        "refreshState": "NotRefreshing",
        "description": "",
        "status": "OK",
        "name": "CN75120D77, bay 3",
        "category": "drive-enclosures",
    }
]

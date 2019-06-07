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
# eTag
# powerState
# uidState
# *wwid
# state
# rotationalRpms
# blockSize
drive_enclosures = [
    {
        "type": "drive-enclosure",
        "firmwareVersion": "1.66",
        "partNumber": "",
        "model": "Synergy D3940 Storage Module",
        "enclosureName": "CN754406XL",
        "productName": "Storage Enclosure 500143803152FA00",
        "interconnectBaySet": 1,
        "manufacturer": "HPE",
        "bay": 3,
        "driveBays": [
            {
                "type": "drive-bay",
                "model": "SAS 146",
                "driveBayLocation": {
                    "locationEntries": [
                      {
                          "value": "1",
                          "type": "Bay"
                      }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPDA",
                    "partNumber": None,
                    "model": "EH0146FARWD",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:1",
                        "3:4:1"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "1",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "PLXSJ0YE",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 1-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-1",
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
                            "value": "2",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPDA",
                    "partNumber": None,
                    "model": "EH0146FARWD",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:2",
                        "3:4:2"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "2",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "PLXSRG3E",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 2-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-2",
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
                            "value": "3",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPDA",
                    "partNumber": None,
                    "model": "EH0146FARWD",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:4:3",
                        "3:1:3"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "3",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "PLXST1EE",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 3-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-3",
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
                            "value": "4",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPDA",
                    "partNumber": None,
                    "model": "EH0146FARWD",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:4",
                        "3:4:4"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "4",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "PLXSX5YE",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 4-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-4",
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
                            "value": "5",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPDA",
                    "partNumber": None,
                    "model": "EH0146FARWD",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:5",
                        "3:4:5"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "5",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "PLXSNWHE",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 5-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-5",
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
                            "value": "6",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "partNumber": None,
                    "model": "EH0146FBQDC",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:6",
                        "3:4:6"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "6",
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
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "6XM4LJ230000M543KG4J",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 6-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-6",
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
                            "value": "7",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "partNumber": None,
                    "model": "EH0146FBQDC",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:7",
                        "3:4:7"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "7",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "6XM4EPT50000M52949LQ",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 7-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-7",
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
                            "value": "8",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "partNumber": None,
                    "model": "EH0146FBQDC",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:4:8",
                        "3:1:8"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "8",
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
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "6XM4E1010000M528K1Q9",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 8-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-8",
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
                            "value": "9",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "partNumber": None,
                    "model": "EH0146FBQDC",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:1:9",
                        "3:4:9"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "9",
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
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "6XM4F9YE0000M5286FAT",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 9-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-9",
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
                            "value": "10",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": {
                    "type": "drive",
                    "firmwareVersion": "HPD3",
                    "partNumber": None,
                    "model": "EH0146FBQDC",
                    "formFactor": None,
                    "manufacturer": "HP",
                    "deviceInterface": "SAS",
                    "driveMedia": "HDD",
                    "buffered": None,
                    "drivePaths": [
                        "3:4:10",
                        "3:1:10"
                    ],
                    "authentic": "yes",
                    "driveLocation": {
                        "locationEntries": [
                            {
                                "value": "3",
                                "type": "SasPort"
                            },
                            {
                                "value": "10",
                                "type": "Bay"
                            },
                            {
                                "value": "1",
                                "type": "Box"
                            }
                        ]
                    },
                    "linkRateInGbs": 6,
                    "temperature": None,
                    "serialNumber": "6XM4E2290000M528EJHW",
                    "capacity": "146",
                    "stateReason": None,
                    "refreshState": "NotRefreshing",
                    "description": "",
                    "status": "OK",
                    "name": "500143803152FA00-Bay 10-Drive",
                    "category": "drives",
                },
                "attachedDeviceInterface": "SAS",
                "name": "500143803152FA00-BayID-10",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-11",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-12",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-13",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-14",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-15",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-16",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-17",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-18",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-19",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-20",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-21",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-22",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-23",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-24",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-25",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-26",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-27",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-28",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-29",
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
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-30",
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
                            "value": "31",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-31",
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
                            "value": "32",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-32",
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
                            "value": "33",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-33",
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
                            "value": "34",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-34",
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
                            "value": "35",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-35",
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
                            "value": "36",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-36",
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
                            "value": "37",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-37",
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
                            "value": "38",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-38",
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
                            "value": "39",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-39",
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
                            "value": "40",
                            "type": "Bay"
                        }
                    ]
                },
                "drive": None,
                "attachedDeviceInterface": "NODEV",
                "name": "500143803152FA00-BayID-40",
                "description": None,
                "status": None,
                "category": "drive-bays",
            }
        ],
        "driveEnclosureLocation": {
            "locationEntries": [
                {
                    "value": "3",
                    "type": "SasPort"
                },
                {
                    "value": "3",
                    "type": "Bay"
                },
                {
                    "value": "/rest/enclosures/000000CN754406XL",
                    "type": "Enclosure"
                }
            ]
        },
        "driveEnclosurePortMap": {
            "deviceSlots": [
                {
                    "deviceName": None,
                    "slotNumber": "1",
                    "physicalPorts": [
                        {
                            "interconnectPortNumber": "3",
                            "interconnectName": "CN754406XL, interconnect 1",
                            "physicalInterconnectPortNumber": "3",
                            "physicalInterconnectName": "CN754406XL, interconnect 1",
                            "type": "SAS"
                        },
                        {
                            "interconnectPortNumber": "4",
                            "interconnectName": "CN754406XL, interconnect 1",
                            "physicalInterconnectPortNumber": "4",
                            "physicalInterconnectName": "CN754406XL, interconnect 1",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                },
                {
                    "deviceName": None,
                    "slotNumber": "2",
                    "physicalPorts": [
                        {
                            "interconnectPortNumber": "3",
                            "interconnectName": "CN754406XL, interconnect 4",
                            "physicalInterconnectPortNumber": "3",
                            "physicalInterconnectName": "CN754406XL, interconnect 4",
                            "type": "SAS"
                        },
                        {
                            "interconnectPortNumber": "4",
                            "interconnectName": "CN754406XL, interconnect 4",
                            "physicalInterconnectPortNumber": "4",
                            "physicalInterconnectName": "CN754406XL, interconnect 4",
                            "type": "SAS"
                        }
                    ],
                    "location": "IO Adapter"
                }
            ],
            "type": "DriveEnclosurePortMap"
        },
        "hardResetState": "Normal",
        "driveBayCount": 40,
        "ioAdapters": [
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "1.66",
                "partNumber": "",
                "model": "Synergy D3940 Storage Module IO Adapter",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portLocation": "1",
                        "phyCount": 4,
                        "portIdentifier": "1",
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portLocation": "2",
                        "phyCount": 4,
                        "portIdentifier": "2",
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    }
                ],
                "portCount": 2,
                "manufacturer": "HPE",
                "redundantIoModule": "Installed",
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
            },
            {
                "type": "drive-enclosure-ioadapter",
                "firmwareVersion": "1.66",
                "partNumber": "",
                "model": "Synergy D3940 Storage Module IO Adapter",
                "ports": [
                    {
                        "type": "sas-port",
                        "portName": "1",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portLocation": "1",
                        "phyCount": 4,
                        "portIdentifier": "1",
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "1",
                        "category": "sas-ports",
                    },
                    {
                        "type": "sas-port",
                        "portName": "2",
                        "portType": "Downlink",
                        "portStatusReason": "None",
                        "portLocation": "2",
                        "phyCount": 4,
                        "portIdentifier": "2",
                        "enabled": True,
                        "description": None,
                        "status": "OK",
                        "name": "2",
                        "category": "sas-ports",
                    }
                ],
                "portCount": 2,
                "manufacturer": "HPE",
                "redundantIoModule": "Installed",
                "ioAdapterLocation": {
                    "locationEntries": [
                        {
                            "value": "2",
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
        "ioAdapterCount": 2,
        "temperature": 24,
        "serialNumber": "CN7452061Q",
        "stateReason": None,
        "refreshState": "NotRefreshing",
        "description": "",
        "status": "OK",
        "name": "CN754406XL, bay 3",
        "category": "drive-enclosures",
    }
]

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Enclosures
ENC1 = 'wpst33'

# Server Hardware
SH3 = '%s, bay 3' % ENC1

# Server Hardware Model
SHM1 = 'BL460c Gen8 1'

# Enclosure Group
EG1 = 'EG_SYNERGY'

# Network FC
FCoE = 'FCoENet100'
ETH1 = 'net100'
FC = "FCNet"
FC2 = "FCNet2"


# Create SP with one primary connection, with private volume as boot volume

createProfileP001 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P001",
        "connections": [
            {
                "id": 1,
                "name": "ethernet",
                "functionType": "Ethernet",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }],
        "boot": {
            "order": ["HardDisk","USB"],
            "manageBoot": True
        }
    }
]

createProfileP002 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P002",
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }],
        "boot": {
            "order": ["HardDisk","USB"],
            "manageBoot": True
        }
    }
]

createProfileP003 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P003",
        "connections": [
            {
                "id": 1,
                "name": "iSCSI",
                "functionType": "iSCSI",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }],
        "boot": {
            "order": ["HardDisk","USB"],
            "manageBoot": True
        }
    }
]

createProfileP004 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P004",
        "connections": [
            {
                "id": 1,
                "name": "FCoE",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createProfileP005 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P005",
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": "FC:{}".format(FC)
            }],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

editProfileP005 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_P005",
        "affinity": "Bay",
        "enclosureUri": ENC1,
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "networkUri": None
            }
        ],
        "bootMode": None,
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

createProfileP006 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P006",
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": "FC:{}".format(FC)
            }],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

editProfileP006 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_P006",
        "affinity": "Bay",
        "enclosureUri": ENC1,
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "networkUri": None
            }
        ],
        "bootMode": None,
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

createProfileP007 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P007",
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "networkUri": None
            }
        ],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

editProfileP007 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_P007",
        "affinity": "Bay",
        "enclosureUri": ENC1,
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "Auto",
                "networkUri": "FC:{}".format(FC)
            }],
        "bootMode": None,
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

createProfileP008 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P008",
        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "networkUri": None
            }
        ],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

editProfileP008 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_P008",
        "affinity": "Bay",
        "enclosureUri": ENC1,
        "connections": [
            {
                "id": 1,
                "name": "FCoE",
                "functionType": "FibreChannel",
                "portId": "Mezz 2:1",
                "requestedMbps": "Auto",
                "networkUri": "FC:{}".format(FC)
            }],
        "bootMode": None,
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

createProfileP010 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P010",
        "connections": [
            {
                "id": 1,
                "name": "FCoE",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createProfileP011 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": "",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "name": "OVF564_API_P011",
        "connections": [
            {
                "id": 1,
                "name": "FCoE",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP012 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P012",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "Ethernet",
                    "functionType": "Ethernet",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP013 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P013",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FCoE_1",
                    "functionType": "FibreChannel",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP014 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P014",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "iSCSI_1",
                    "functionType": "iSCSI",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP015 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P015",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FCoE",
                    "functionType": "FibreChannel",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPP015 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverProfileTemplateUri": "SPT:{}".format("OVF564_API_SPT_P015"),
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SP_P015",

        "connections": [
            {
                "id": 1,
                "name": "FCoE",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }
         ],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP016 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P016",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FCoE",
                    "functionType": "FibreChannel",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP017 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P017",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FCoE",
                    "functionType": "FibreChannel",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPP017 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverProfileTemplateUri": "SPT:{}".format("OVF564_API_SPT_P017"),
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SP_P017",
        "connections": [
                {
                    "id": 1,
                    "name": "FCoE",
                    "functionType": "FibreChannel",
                    "portId": "Auto",
                    "requestedMbps" : 2500,
                    "networkUri": "FCOE:{}".format(FCoE)
                }],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP018 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P018",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FC",
                    "functionType": "FibreChannel",
                    "portId": "Mezz 2:1",
                    "networkUri": "FC:{}".format(FC)
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPP018 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverProfileTemplateUri": "SPT:{}".format("OVF564_API_SPT_P018"),
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SP_P018",
        "connections": [
                {
                    "id": 1,
                    "name": "FC",
                    "functionType": "FibreChannel",
                    "portId": "Auto",
                    "networkUri": "FC:{}".format(FC2)
                }
        ],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]


createSPTP019 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P019",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FC",
                    "functionType": "FibreChannel",
                    "portId": "Auto",
                    "networkUri": "FC:{}".format(FC)
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPP019 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverProfileTemplateUri": "SPT:{}".format("OVF564_API_SPT_P019"),
        "serverHardwareUri": SH3,
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SP_P019",

        "connections": [
            {
                "id": 1,
                "name": "FC",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "networkUri": None
            }
        ],
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]

createSPTP020 = [
    {
        "type": "ServerProfileTemplateV3",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "name": "OVF564_API_SPT_P020",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "FCoE",
                    "functionType": "FibreChannel",
                    "portId": "Flb 1:1-b",
                    "networkUri": None
                }
            ],
            "manageConnections": True
        },
        "boot": {
            "order": ["HardDisk", "USB"],
            "manageBoot": True
        }
    }
]


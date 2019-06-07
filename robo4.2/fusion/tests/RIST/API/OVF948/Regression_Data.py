admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
task_states = ['Warning', 'Completed']

FirmwareVersion = 'Gen10Snap1'
# Server Hardware
SHIP = '10.101.101.74'
SHname = 'ILO7CE420PZ2D'

SHM1 = "for ML"
GEN9MLServerManaged = [
     {
        'name': 'ILO7CE420PZ2D',
        'hostname': '10.101.101.74',
        # 'licensingIntent': 'OneViewStandard',
        'licensingIntent': 'OneViewNoiLO',
        'username': 'Administrator',
        'password': 'admin123',
        'force': True,
        'configurationState': 'Managed'
    }
]

# Server profile data


emptyProfile = [
    {
        "type": "ServerProfileV7",
        "name": "Edit_SP",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "connections": [],
        "bootMode": None,
        "boot": {
            "manageBoot": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
    }
]

APIp007createfwProfiles = [
    {

        "type": "ServerProfileV7",
        "serverHardwareUri": SHIP,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "name": "SP-ML-SPP",
        "connections": [],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": FirmwareVersion,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode"
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        }
    }
]

APIp009createbiosProfiles = [
    {

        "type": "ServerProfileV7",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "name": "SP-ML",
        "connections": [],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
         "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "bios": {
            "manageBios": True,
            # "boot": None
        }
    }
]


APIp010createbiosProfiles = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "SP-ML",
        "connections": [

        ],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "CustomPostMessage",
                    "value": "this is test"
                }
            ]
        }

    }

]

APIp011createbootProfiles = [
    {

        "type": "ServerProfileV7",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "name": "SP-ML",
        "connections": [],
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"],
        },
        "bootMode": {
            "manageMode": True,
            "mode":  "BIOS",
        },

        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "bios": {
            "manageBios": True,
            # "boot": None
        }
    }
]

APIp012createLSProfiles = [
    {

        "type": "ServerProfileV7",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "name": "SP-ML",
        "connections": [],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "ML-Volume",
                            "raidLevel": "RAID0",
                            "bootable": False,
                            "numPhysicalDrives": 1,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "driveNumber": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "RAID",
                    "initialize": False,
                    "importConfiguration": True
                }
            ]
        }
    }
]

APIp015editFWProfiles = [
    {
        "type": "ServerProfileV7",
        "name": "Edit_SP",
        "serverHardwareUri": SHIP,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "connections": [],
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": FirmwareVersion,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode"
        },
        "bootMode": None,
        "boot": {
            "manageBoot": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

APIp016editBiosProfiles = [
    {
        "type": "ServerProfileV7",
        "name": "Edit_SP",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "connections": [],
        "bootMode": None,
        "boot": {
            "manageBoot": False
        },
         "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "CustomPostMessage",
                    "value": "this is test for edit"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

APIp017editBootProfiles = [
    {
        "type": "ServerProfileV7",
        "name": "Edit_SP",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "connections": [],
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"],
        },
        "bootMode": {
            "manageMode": True,
            "mode":  "BIOS",
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

APIp018editLSProfiles = [
    {
        "type": "ServerProfileV7",
        "name": "Edit_SP",
        "serverHardwareUri": SHname,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "connections": [],
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"],
        },
        "boot": {
            "manageBoot": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "ML-Volume",
                            "raidLevel": "RAID0",
                            "bootable": False,
                            "numPhysicalDrives": 1,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "driveNumber": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "RAID",
                    "initialize": False,
                    "importConfiguration": True
                }
            ]
        },
        "category": "server-profiles",
        "eTag": ""
    }
]


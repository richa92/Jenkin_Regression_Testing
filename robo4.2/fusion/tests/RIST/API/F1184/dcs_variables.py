admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
model = "C7000"

# Enclosures
ENC1 = 'dcs'
EG1 = 'dcs'

#Update method
HPSUT = "Boot server using"
IP = "HPE Intelligent Provisioning"

# Firmware Bundles
SNAP5SPP = '/rest/firmware-drivers/SPP2016020_2015_1204_63'
SNAP6SPP = '/rest/firmware-drivers/SPPgen9snap6_2016_0202_65'
InvalidSPP = '/rest/firmware-drivers/SPP'
SNAP5BaseLine = '2016.02.0'
SNAP6BaseLine = 'gen9snap6'

# Server Hardware
SH1 = '%s, bay 4' % ENC1
SH2 = '%s, bay 5' % ENC1
SH3 = '%s, bay 6' % ENC1
SH4 = '%s, bay 7' % ENC1

# Server Hardware Model
SHM1 = "BL460C_GEN8"
SHM2 = "BL660C_GEN9"


# Create empty Server profile
emptyProfile = {
    "type": "ServerProfileV6",
    "serverHardwareUri": SH1,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "F1184_EMPTY_SP",
    "connections": [],
    "boot":
        {
            "manageBoot": False
        },
    "bootMode": None
}
# Create SP and update firmware using Gen 9 snap 6 as the baseline and configure local storage 
createProfiles = [
    {
        "type": "ServerProfileV6",
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1184_CREATE_SNAP6_SP_%s" % SH1,
        "connections": [],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": SNAP6SPP,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode"
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "HPSUT-Volume",
                            "raidLevel": "RAID1",
                            "bootable": False,
                            "numPhysicalDrives": 2,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "driveNumber": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "RAID",
                    "initialize": True,
                    "importConfiguration": False
                }
            ]
        }
    }
]
# Edit SP and update firmware using Gen 9 snap 6 as the baseline and configure local storage 
editProfiles = [
    {
        "type": "ServerProfileV6",
        "name": "F1184_EDIT_SNAP6_SP_%s" % SH1,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "affinity": "Bay",
        "connections": [],
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": SNAP6SPP,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode"
        },
        "bootMode": None,
        "boot": {
            "manageBoot": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "HPSUT-Volume",
                            "raidLevel": "RAID1",
                            "bootable": False,
                            "numPhysicalDrives": 2,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "driveNumber": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "RAID",
                    "initialize": True,
                    "importConfiguration": False
                }
            ]
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]
# Create SP update firmware using Gen 9 snap 6 and configure Local Storage and BIOS
createFullProfiles = [
    {
        "type": "ServerProfileV6",
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1184_CREATE_FULL_SP_%s" % SH1,
        "connections": [

        ],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": SNAP6SPP,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode"
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "logicalDrives": [
                        {
                            "name": "HPSUT-Volume",
                            "raidLevel": "RAID1",
                            "bootable": False,
                            "numPhysicalDrives": 2,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "driveNumber": None
                        }
                    ],
                    "deviceSlot": "Embedded",
                    "mode": "RAID",
                    "initialize": True,
                    "importConfiguration": False
                }
            ]
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "23",
                    "value": "1"
                },
                {
                    "id": "85",
                    "value": "2"
                },
                {
                    "id": "177",
                    "value": "1"
                },
                {
                    "id": "108",
                    "value": "Admin Name Text"
                }
            ]
        }
    }
]
# Invalid Raid Level Data For Local Storage
invalidLocalStorage = {
    "sasLogicalJBODs": [],
    "controllers": [
        {
            "logicalDrives": [
                {
                    "name": "HPSUT-Volume",
                    "raidLevel": "RAID11",
                    "bootable": False,
                    "numPhysicalDrives": 2,
                    "driveTechnology": None,
                    "sasLogicalJBODId": None,
                    "driveNumber": None
                }
            ],
            "deviceSlot": "Embedded",
            "mode": "RAID",
            "initialize": True,
            "importConfiguration": False
        }
    ]
}

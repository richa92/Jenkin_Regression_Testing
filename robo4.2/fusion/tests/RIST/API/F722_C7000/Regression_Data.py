admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
model = "C7000"

# Enclosures
ENC1 = 'wpst32'
EG1 = 'GRP-%s' % ENC1

# Update method
HPSUT = "Boot server using"
IP = "HPE Intelligent Provisioning"

# Firmware Bundles
SNAP5SPP = '/rest/firmware-drivers/SPP2016020_2015_1204_63'
SNAP6SPP = '/rest/firmware-drivers/SPP2016100_2016_1015_191'
InvalidSPP = '/rest/firmware-drivers/SPP'
SNAP5BaseLine = '2016.02.0'
SNAP6BaseLine = '2016.10.0'

# Firmware Bundles List
Firmware_Bundles = [
    {
        'SPPFileName': 'SPP2016020.2015_1204.63.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/2016.02.0\ Gen9Snap5/Released/',
        'SPPFileMD5': 'f8eb9835e5698b9daaea4e66eaa964db',
        'FirmwareBundleURI': SNAP5SPP,
    },
    {
        'SPPFileName': 'SPPgen9snap6.2016_0617.118.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
        'SPPFileMD5': 'b9d7e9d34d94d4298e0c9a606f293c72',
        'FirmwareBundleURI': SNAP6SPP
    }
]

# Server Hardware
SH1 = '%s, bay 2' % ENC1
SH2 = '%s, bay 5' % ENC1
SH3 = '%s, bay 6' % ENC1
SH4 = '%s, bay 7' % ENC1

# Server Hardware Model
SHM1 = "BL460C_GEN8"
SHM2 = "BL660C_GEN9"


# Create empty Server profile
emptyProfile = {
    "type": "ServerProfileV7",
    "serverHardwareUri": SH1,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "F722_EMPTY_SP",
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
        "type": "ServerProfileV7",
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F722_CREATE_SNAP6_SP_%s" % SH1,
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
            "controllers": []
        }
    }
]
# Edit SP and update firmware using Gen 9 snap 6 as the baseline and configure local storage
editProfiles = [
    {
        "type": "ServerProfileV7",
        "name": "F722_EDIT_SNAP6_SP_%s" % SH1,
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
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]
# Create SP update firmware using Gen 9 snap 6 and configure Local Storage and BIOS
createFullProfiles = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F722_CREATE_FULL_SP_%s" % SH1,
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
                    "value": "4"
                },
                {
                    "id": "108",
                    "value": "Admin Name Text"
                }
            ]
        }
    }
]
# Validate Firmware Update Result
firmwares = {
    SNAP5SPP: {
        SHM1: [
            {
                "componentName": "HP ProLiant System ROM",
                "componentVersion": "I31 06/01/2015"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.40 Dec 02 2015"
            },
        ],
        SHM2: [
            {
                "componentName": "HP ProLiant System ROM",
                "componentVersion": "I38 10/29/2015"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.40 Dec 02 2015"
            }
        ]
    },
    SNAP6SPP: {
        SHM1: [
            {
                "componentName": "System ROM",
                "componentVersion": "I31 06/01/2015"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.50 Sep 23 2016"
            },
        ],
        SHM2: [
            {
                "componentName": "System ROM",
                "componentVersion": "I38 10/29/2015"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.50 Sep 23 2016"
            }
        ]
    }
}

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
model = "TBird"

# Enclosures
ENC1 = 'CN75440444'
EG_Name = 'EG_SYNERGY'
LE_NAME = 'LE_SYNERGY'


# Firmware Bundles
Snap6SPP = '/rest/firmware-drivers/SPP2016100_2016_1015_191'
OldSnap6SPP = '/rest/firmware-drivers/SPP2016100_2016_1015_191'
InvalidSPP = '/rest/firmware-drivers/SPP'

# Firmware Bundles List
OldSnap6 = [
    {
        'SPPFileName': 'SPP2016100.2016_1015_191',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
        'SPPFileMD5': 'c2e3d4bc2290619041fe0ceeb8364c34',
        'FirmwareBundleURI': OldSnap6SPP
    }
]
Snap6 = [
    {
        'SPPFileName': 'SPP2016100.2016_1015_191',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
        'SPPFileMD5': 'b9d7e9d34d94d4298e0c9a606f293c72',
        'FirmwareBundleURI': Snap6SPP
    }
]

LE_create_update_fw_force = {
    "firmwareBaselineUri":Snap6SPP,
    "forceInstallFirmware":True
}

LE_create_downgrade_fw_force = {
    "firmwareBaselineUri":OldSnap6SPP,
    "forceInstallFirmware":True
}

LE_create_update_fw_noforce = {
    "firmwareBaselineUri":Snap6SPP,
    "forceInstallFirmware":False
}

LE_fw_update_SharedProfile_parallel = {
    "op":"replace",
    "path":"/firmware",
    "firmwareBaselineUri":Snap6SPP,
    "firmwareUpdateOn":"SharedInfrastructureAndServerProfiles",
    "forceInstallFirmware":False,
    "logicalInterconnectUpdateMode":"Parallel",
}

LE_fw_update_SharedProfile_orchestrated = {
    "op":"replace",
    "path":"/firmware",
    "firmwareBaselineUri":Snap6SPP,
    "firmwareUpdateOn":"SharedInfrastructureAndServerProfiles",
    "forceInstallFirmware":False,
    "logicalInterconnectUpdateMode":"Orchestrated"
}

LE_fw_update_SharedProfile_parallel_force = {
    "op":"replace",
    "path":"/firmware",
    "firmwareBaselineUri":OldSnap6SPP,
    "firmwareUpdateOn":"SharedInfrastructureAndServerProfiles",
    "forceInstallFirmware":True,
    "logicalInterconnectUpdateMode":"Parallel"
}

LE_fw_update_SharedProfile_orchestrated_force = {
    "op":"replace",
    "path":"/firmware",
    "firmwareBaselineUri":OldSnap6SPP,
    "firmwareUpdateOn":"SharedInfrastructureAndServerProfiles",
    "forceInstallFirmware":True,
    "logicalInterconnectUpdateMode":"Orchestrated"
}


# Server Hardware
SH1 = '%s, bay 4' % ENC1
SH2 = '%s, bay 6' % ENC1
SH3 = '%s, bay 7' % ENC1

# Server Hardware Model
SHM1 = "SY660_GEN9"
SHM2 = "SY620_Gen9"
SHM3 = "SY480_GEN9"


server_hardwares = [{"serverHardwareUri": SH1, "description": SHM1},
             {"serverHardwareUri": SH2, "description": SHM2},
             {"serverHardwareUri": SH3, "description": SHM3}
             ]

# Validate Firmware Update Result
firmwares = {
    Snap6SPP: {
        SHM1: [
            {
                "componentName": "System ROM",
                "componentVersion": "I39 v2.20 (09/08/2016)"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.50 Sep 23 2016"
            },
            {
                "componentName": "Power Management Controller Firmware",
                "componentVersion": "1.0.9"
            },
            {
                "componentName": "Smart Array P240nr Controller",
                "componentVersion": "4.52"
            },
            {
                "componentName": "Synergy 3820C 10/20Gb CNA",
                "componentVersion": "7.14.79"
            }
        ],
        SHM2: [
            {
                "componentName": "System ROM",
                "componentVersion": "I40 v2.20 (09/08/2016)"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.50 Sep 23 2016"
            },
            {
                "componentName": "Power Management Controller Firmware",
                "componentVersion": "1.0.9"
            },
            {
                "componentName": "Smart HBA H240nr",
                "componentVersion": "4.52"
            },
            {
                "componentName": "Synergy 3820C 10/20Gb CNA",
                "componentVersion": "7.14.79"
            }
        ],
        SHM3: [
            {
                "componentName": "System ROM",
                "componentVersion": "I37 v2.20 (09/14/2016)"
            },
            {
                "componentName": "iLO",
                "componentVersion": "2.50 Sep 23 2016"
            },
            {
                "componentName": "Power Management Controller Firmware",
                "componentVersion": "1.0.9"
            },
            {
                "componentName": "Smart Array P240nr Controller",
                "componentVersion": "4.52"
            },
            {
                "componentName": "Synergy 3820C 10/20Gb CNA",
                "componentVersion": "7.14.79"
            }
        ]
    }
}

EG = [
    {
        'name': 'EG_SYNERGY',
        'type': 'EnclosureGroupV300',
        'enclosureCount': 1,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 1,
        'configurationScript': None,
        'interconnectBayMappings':
        [],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
    }
]
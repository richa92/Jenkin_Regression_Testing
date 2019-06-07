# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
NETWORK_SET_TYPE = 'network-setV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV5'
SERVER_PROFILE_TYPE = 'ServerProfileV9'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Enclosures
ENC1 = 'wpst26'
EG1 = 'GRP-%s' % ENC1

# Update method
HPSUT = "Boot server using"
IP = "Intelligent Provisioning"

# Firmware Bundles
SPP_list = [r'Z:\firmware\SPP\Gen9Snap6\SPP2016100.2016_1015.191.iso',
            r'Z:\firmware\SPP\2016.02.0 Gen9Snap5\Released\SPP2016020.2015_1204.63.iso']

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
        'SPPFileName': 'SPP2016100.2016_1015.191.iso',
        'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/Gen9Snap6/',
        'SPPFileMD5': 'b9d7e9d34d94d4298e0c9a606f293c72',
        'FirmwareBundleURI': SNAP6SPP
    }
]

# Interconnects
ENC1ICBay3 = '%s, interconnect 3' % ENC1
ENC1ICBay6 = '%s, interconnect 6' % ENC1

# Server Hardware
SH1 = '%s, bay 1' % ENC1
SH2 = '%s, bay 3' % ENC1
SH3 = '%s, bay 6' % ENC1
SH4 = '%s, bay 7' % ENC1

# Server Hardware Model
SHM1 = "BL465C_GEN8"
SHM2 = "BL460C_GEN8"


# Create empty Server profile
emptyProfile = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": SH1,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "F1183_EMPTY_SP",
    "connectionSettings": {
        "connections": [],
    },
    "boot": {
        "manageBoot": False
    },
    "bootMode": None
}
# Create SP and update firmware using Gen 9 snap 6 as the baseline and configure BIOS
createdropdownbiosProfiles = [
    {

        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1183_CREATE_SP_BL465c_%s" % SH1,
        "connectionSettings": {
            "connections": [],
        },
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

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "6"
                },
                {
                    "id": "254",
                    "value": "1"
                }
            ]
        }

    }
]

createinputbiosProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH2,
        "description": SHM2,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1183_CREATE_BL460_SP_%s" % SH2,
        "connectionSettings": {
            "connections": [],
        },
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

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "133",
                    "value": "this is test"
                },
                {
                    "id": "100",
                    "value": "test"
                }
            ]
        }

    }

]
# Edit SP and update firmware using Gen 9 snap 6 as the baseline and configure BIOS
editdropdownProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1183_EDIT_BL460_SP_%s" % SH1,
        "connectionSettings": {
            "connections": [],
        },
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

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "6"
                },
                {
                    "id": "254",
                    "value": "1"
                }
            ]
        },
        "category": "server-profiles",
        "eTag": ""
    }
]
editinputProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH2,
        "description": SHM2,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1183_EDIT_BL460_SP_%s" % SH2,
        "connectionSettings": {
            "connections": [],
        },
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

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "133",
                    "value": "this is test by edit SP"
                },
                {
                    "id": "100",
                    "value": "test edit SP"
                }
            ]
        },
        "category": "server-profiles",
        "eTag": ""

    }
]
# create invalid BIOS value SP
createinvalidnbiosProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1183_CREATE_SNAP6_SP_%s" % SH1,
        "connectionSettings": {
            "connections": [],
        },
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

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "177",
                    "value": "5000"
                }
            ]
        }

    }

]
# edit invalid BIOS value SP
editinvalidnbiosProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "F1183_EDIT_SNAP6_SP_%s" % SH1,
        "connectionSettings": {
            "connections": [],
        },
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

        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "177",
                    "value": "5000"
                }
            ]
        },
        "category": "server-profiles",
        "eTag": ""
    }
]

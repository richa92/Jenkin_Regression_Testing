from FusionLibrary.libs.utils.common import get_firmware_bundle
from FusionLibrary.libs.utils.common import get_firmware_version_by_file_name

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
NETWORK_SET_TYPE = 'network-setV5'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV6'
STORAGE_VOLUME_TYPE = 'StorageVolumeV7'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
SCOPE_TYPE = "ScopeV3"
DOMAIN_TYPE = "LoginDomainConfigV600"

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
model = "TBird"

spp_folder = r'Z:\firmware\SPP\SHQA_Regression'
fw_bundle = get_firmware_bundle(spp_folder)
FirmwareVersion = get_firmware_version_by_file_name(fw_bundle)

# Enclosures
ENC1 = 'CN75440444'
EG1 = 'EG_SYNERGY'

# Server Hardware
SH1 = '%s, bay 9' % ENC1
SH2 = '%s, bay 4' % ENC1
# SH3 = '%s, bay 6' % ENC1
SH4 = '%s, bay 7' % ENC1

# Server Hardware Model
SHM1 = "SY480_GEN10"
SHM2 = "SY660_GEN10"

iloUserName = 'Administrator'
iloPasswordDL = 'hpvse123'
iloPassword = 'hpvse123'
Gen10SYIP = '16.114.218.208'
firmwareURI = 'http://wpstwork4.vse.rdlabs.hpecorp.net/firmware/ilo/ilo5/ilo5_115_p16.bin'

Gen10SYServerFW = [
    {
        'server name': SH1,
        'iloIP': Gen10SYIP,
        'iloUserName': iloUserName,
        'iloPassword': iloPasswordDL,
        'firmwareURI': firmwareURI
    }
]

# Create empty Server profile
emptyProfile = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": SH1,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF906_EMPTY_SP",
    "connectionSettings": {"connections": []},
    "boot": {
        "manageBoot": False
    },
    "bootMode": None
}
# Create SP and update firmware using Gen 10 snap 1 as the baseline
createSYProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "OVF906_CREATE_GEN10_SP_%s" % SH1,
        "connectionSettings": {"connections": []},
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
createOnlineSYProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "OVF906_CREATE_GEN10_SP_%s" % SH1,
        "connectionSettings": {"connections": []},
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": FirmwareVersion,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnly",
            "firmwareActivationType": "Immediate",
            "firmwareScheduleDateTime": ""
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        }
    }
]
# Edit SP and update firmware using Gen 9 snap 6 as the baseline and configure local storage
editOnlineBLProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "OVF906_EDIT_GEN10_SP_%s" % SH1,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": FirmwareVersion,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnly",
            "firmwareActivationType": "Immediate",
            "firmwareScheduleDateTime": ""
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
editSYProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "OVF906_EDIT_GEN10_SP_%s" % SH1,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
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

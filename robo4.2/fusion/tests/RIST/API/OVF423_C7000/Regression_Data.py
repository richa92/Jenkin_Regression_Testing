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
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
SCOPE_TYPE = "ScopeV3"
DOMAIN_TYPE = "LoginDomainConfigV600"

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ia_name = 'OVF423IA'
ia_credentials = {'userName': ia_name, 'password': 'wpsthpvse1'}
sa_name = 'OVF423SA'
sa_credentials = {'userName': sa_name, 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
model = "C7000"
ia_users = [{'userName': ia_name, 'password': 'wpsthpvse1', 'fullName': 'OVF5IA', 'permissions': [], 'emailAddress': 'admin@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-555-0003', 'type': USER_AND_PERMISSION_TYPE}]
sa_users = [{'userName': sa_name, 'password': 'wpsthpvse1', 'fullName': 'OVF5SA', 'permissions': [], 'emailAddress': 'admin@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-555-0003', 'type': USER_AND_PERMISSION_TYPE}]

SPT_name = "OVF423_SPT"
SP_name = "OVF423_SP"

# Scopes
ia_user_scopes = ['scope1', 'scope2', 'scope3']
ia_part_scopes = ['scope1', 'scope2']
ia_except_scopes = ['scope4', 'scope5']
ia_scope_scope = 'scope1'
ia_minor_scope = 'scope3'
ia_role_name = "Infrastructure administrator"
sa_role_name = "Server administrator"

FirmwareVersion = '2018.06.0'
invalidSPP = '/rest/firmware-drivers/invalid_uri'
invalidScope = '/rest/scopes/invalid_uri'
ok_status = "OK"
scope_type = "ScopeV3"
scope_name_a = "OVF5_SCOPE_A"
scope_name_b = "OVF5_SCOPE_B"
online_type = "FirmwareAndOSDrivers"
offline_type = "FirmwareOnlyOfflineMode"

invalid_resource_error = "INVALID_RESOURCE"
invalid_scope_error = "INVALID_SCOPE"
not_authorized_error = "ASSOCIATION_FORBIDDEN_BY_SCOPE"
creation_not_authorized_error = "CREATION_NOT_AUTHORIZED_ERROR"
association_error = "ASSOCIATION_FORBIDDEN_BY_SCOPE"

custom_spp_name = 'OVF5_CUSTOM'

Http_repo_with_password = {
    'repositoryName': 'external',
    'repositoryURI': 'https://16.114.220.138/webdav',
    'userName': 'Administrator',
    'password': 'Lsdt4acsl',
    'base64Data': ""
}

# ValidateFirmwares = ["1.7.0.0", "1.0.1.0", "2016.10.0", "2017.07.0"]
ValidateFirmwares = ["2018.06.0"]

ValidateSPP = [
    "Online ROM Flash Component for Linux - HPE Synergy 480 Gen10 (I42) Compute Module ",
    "Online ROM Flash Component for Windows x64 - HPE Synergy 660 Gen10 (I43) Compute Module",
    "Online ROM Flash Component for Linux - HPE ProLiant DL380 Gen10 (U30) Servers",
    "Online ROM Flash Component for Windows x64 - HPE ProLiant BL460c Gen10 (I41) Servers"
]

Scopes = [
    {
        "name": "scope1",
        "description": "",
        "type": scope_type,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope2",
        "description": "",
        "type": scope_type,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope3",
        "description": "",
        "type": scope_type,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope4",
        "description": "",
        "type": scope_type,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope5",
        "description": "",
        "type": scope_type,
        "addedResourceUris": [],
        "removedResourceUris": []
    }
]

CreateScope = {
    "name": "scope",
    "description": "",
    "type": scope_type,
    "addedResourceUris": [],
    "removedResourceUris": []

}

# Enclosures
ENC1 = 'wpst32'
EG1 = 'GRP-%s' % ENC1

# Server Hardware
SH1 = '%s, bay 1' % ENC1
SH2 = '%s, bay 2' % ENC1
SH3 = '%s, bay 3' % ENC1
SH4 = '%s, bay 4' % ENC1
SH5 = '%s, bay 5' % ENC1

# Server Hardware Model
SHM1 = "BL460C_GEN8"
SHM2 = "BL460C_GEN10"

TEMPLATE_SHT = 'BL460c Gen8 2'
# :Flb1:HP FlexFabric 10Gb 2-port 554FLB Adapter:1:HP FlexFabric 10Gb 2-port 554M Adapter:2:HP LPe1205A 8Gb FC HBA for BladeSystem c-Class'

# Create SP and update firmware
server_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": SH3,
    "description": SHM1,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": SP_name,
    "bootMode": None,
    "connectionSettings": {
    },
    "firmware": {
        "manageFirmware": True,
        "firmwareBaselineUri": FirmwareVersion,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"
    }
}

profile_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': SPT_name,
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1,
    "connectionSettings": {
        "manageConnections": False,
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareAndOSDrivers",
        "firmwareActivationType": "Immediate"},
    "initialScopeUris": []
}

empty_profile_template = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': SPT_name,
    'serverHardwareTypeUri': 'SHT:' + TEMPLATE_SHT,
    'enclosureGroupUri': 'EG:%s' % EG1,
    "connectionSettings": {
        "manageConnections": False,
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareAndOSDrivers",
        "firmwareActivationType": "Immediate"},
    "initialScopeUris": []
}

firmware_payload = {
    "manageFirmware": True,
    "firmwareBaselineUri": "/rest/firmware-drivers/SPP2017070_2017_0608_153",
    "forceInstallFirmware": False,
    "firmwareInstallType": "FirmwareAndOSDrivers",
    "firmwareActivationType": "Immediate"
}

empty_firmware_payload = {
    "manageFirmware": False,
    "firmwareBaselineUri": "",
    "forceInstallFirmware": False,
    "firmwareInstallType": "FirmwareAndOSDrivers",
    "firmwareActivationType": "Immediate"
}

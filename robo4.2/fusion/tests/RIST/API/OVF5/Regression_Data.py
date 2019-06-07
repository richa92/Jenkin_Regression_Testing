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
ia_name = 'OVF5IA'
ia_credentials = {'userName': ia_name, 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
task_states = ['Warning', 'Completed']

ia_users = [{'userName': ia_name, 'password': 'wpsthpvse1', 'fullName': 'OVF5IA', 'permissions': [], 'emailAddress': 'admin@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-555-0003', 'type': 'UserAndPermissions'}]
ia_user_scopes = ['scope1', 'scope2', 'scope3']
ia_part_scopes = ['scope1', 'scope2']
ia_except_scopes = ['scope4', 'scope5']
ia_scope_scope = 'scope1'
ia_minor_scope = 'scope3'
ia_role_name = "Infrastructure administrator"

# Firmware Bundles
FirmwareVersion = '2018.06.0'
firmware_version = '2018.06.0'
SPPVersion = firmware_version
# HotFixVersion = '1.0.1.0'
invalidSPP = '/rest/firmware-drivers/invalid_uri'
invalidScope = '/rest/scopes/invalid_uri'
le_name = 'LE_SYNERGY'
ok_status = "OK"
scope_name_a = "OVF5_SCOPE_A"
scope_name_b = "OVF5_SCOPE_B"

invalid_resource_error = "INVALID_RESOURCE"
invalid_scope_error = "INVALID_SCOPE"
not_authorized_error = "NOT_AUTHORIZED_ERROR"
creation_not_authorized_error = "CREATION_NOT_AUTHORIZED_ERROR"
association_error = "ASSOCIATION_FORBIDDEN_BY_SCOPE"

# Upload_SPP_Path = r'Z:\firmware\SPP\Released\2017.04\SPP_2016.04.20170417_for_HPE_Synergy_874800-001.iso'
# Upload_HotFix_Path = r'Z:\firmware\test\cp031117.exe'
# Upload_SPP_Version = '2017.04.0'
# Upload_HotFix_Version = '2016.10.0'
# Upload_Exist_SPP_Path = r'Z:\firmware\SPP\Released\2016.10\871790_001_spp-2016.10.0-SPP2016100.2016_1015.191.iso'
# Upload_Exist_HotFix_Path = r'Z:\firmware\test\cp029396.exe'

custom_spp_name = 'OVF5_CUSTOM'

Http_repo_with_password = {
    'repositoryName': 'external',
    'repositoryURI': 'https://16.114.220.138/webdav',
    'userName': 'Administrator',
    'password': 'Lsdt4acsl',
    'base64Data': ""
}

# ValidateFirmwares = ["2018.06.0", "1.0.1.0", "2017.04.0", "2016.10.0'"]
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
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope2",
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope3",
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope4",
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": "scope5",
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    }
]

CreateScope = {
    "name": "scope",
    "description": "",
    "type": SCOPE_TYPE,
    "addedResourceUris": [],
    "removedResourceUris": []
}

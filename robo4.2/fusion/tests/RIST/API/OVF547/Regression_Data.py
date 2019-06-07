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
SCOPE_TYPE = "ScopeV3"
DOMAIN_TYPE = "LoginDomainConfigV600"

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
server_admin_credentials = {
    'userName': 'ServerAdmin',
    'password': 'wpsthpvse1'}
network_admin_credentials = {
    'userName': 'Networkadmin',
    'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse1-ilo'}
task_states = ['Warning', 'Completed']
aliasName = "16.114.218.204"
# Enclosures
ENC1 = 'wpst32'
le_name = 'wpst32'
EG1 = 'GRP-%s' % ENC1

FirmwareVersion = '2017.07.0'
Gen9FirmwareVersion = '2016.10.0'
custom_spp = 'custom_spp'

# Server Hardware
SH1 = '%s, bay 2' % ENC1
SH2 = '%s, bay 3' % ENC1
SH3 = '%s, bay 4' % ENC1
SH4 = '%s, bay 5' % ENC1

# Server Hardware Model
SHM1 = "BL460C_GEN8"
SHM2 = "BL460C_GEN9"
# repo URI
Http_repo_URI = 'http://16.114.218.204/webdav'
Https_repo_URI = 'https://16.114.218.204/webdav'
SERVER_IP = '16.114.218.204'
ssh_username = 'root'
ssh_password = '123456'
delete_name = 'external_repo'
repository_name = 'external'
internal_name = 'Internal'
edit_repo = "external_repo"
repo_user = 'joanna'
repo_password = "joanna"
ok_status = "OK"
bad_status = "Critical"

# Firmware locations
Expected_locations = ["external"]
expected_edit_locations = ["external_repo"]
external_locations = ["external"]
Unexpected_locations = ["Internal"]
internal_locations = ["Internal"]
both_locations = ["external", "Internal"]
# hpsut_path = 'C:/Users/qiaoya/Downloads/hpsut-1.7.0.0-4.linux.x86_64.rpm'
hpsut_path = 'Z:/firmware/hpsut/hpsut-1.7.0.0-4.linux.x86_64.rpm'
hpsut_version = '1.7.0.0'
smartarray_version = '4.99'
# ams_path = 'C:/Users/qiaoya/Downloads/cp030689.exe'
ams_path = 'Z:/firmware/ams/cp030689.exe'
ams_version = '1.1.0.0'
detect_name = 'Synergy 10Gb Pass-Thru Module'
detect_version = '1.08'
invalid_hotfix = '1.10'
add_multi_error = 'MULTIPLE_REPOSITORY_NOT_SUPPORTED_ERROR'
remove_external_error = 'EXTERNAL_FW_BUNDLE_DELETE_NOT_SUPPORTED_ERROR'

http_pw_commands = ['cp /etc/apache2/sites-available/000-default.conf.passwd /etc/apache2/sites-available/000-default.conf',
                    'service apache2 restart']
http_nopw_commands = ['cp /etc/apache2/sites-available/000-default.conf.withoutpw /etc/apache2/sites-available/000-default.conf',
                      'service apache2 restart']
https_pw_commands = ['cp /etc/apache2/sites-available/default-ssl.conf.passwd /etc/apache2/sites-available/default-ssl.conf',
                     'service apache2 restart']
https_nopw_commands = ['cp /etc/apache2/sites-available/default-ssl.conf.withoutpw /etc/apache2/sites-available/default-ssl.conf',
                       'service apache2 restart']
copy_hotfix_commands = [
    'cp /var/www/hotfix/hp-firmware-icmpt-1.08-1.1.i586.rpm /var/www/webdav/hp-firmware-icmpt-1.08-1.1.i586.rpm']
copy_invalid_hotfix_commands = [
    'cp /var/www/invalidhotfix/hp-firmware-ilo5-1.10-1.1.i386.rpm /var/www/webdav/hp-firmware-ilo5-1.10-1.1.i386.rpm']
copy_invalid_spp_commands = [
    'cp /var/www/SPPGen10s2.iso /var/www/webdav/SPPGen10s2.iso']
remove_hotfix_commands = [
    'rm /var/www/webdav/hp-firmware-icmpt-1.08-1.1.i586.rpm']
remove_invalid_hotfix_commands = [
    'rm /var/www/webdav/hp-firmware-ilo5-1.10-1.1.i386.rpm']
remove_invalid_spp_commands = ['rm /var/www/webdav/SPPGen10s2.iso']


# Firmware Bundles List
ValidateFirmwares = [
    "1.7.0.0",
    "1.0.1.0",
    "10.7.221.0",
    "2016.10.0",
    "2017.07.0",
    "4.99",
    "HPG6"]

# Firmwares Version list
FirmwareVersions = [
    "1.7.0.0",
    "1.0.1.0",
    "10.7.221.0",
    "2016.10.0",
    "2017.07.0",
    "4.99",
    "HPG6"]

# Request Body
Http_repo_with_password = {
    'repositoryName': repository_name,
    'repositoryURI': Http_repo_URI,
    'userName': repo_user,
    'password': repo_password,
    'base64Data': ""
}
Https_repo_with_password = {
    'repositoryName': repository_name,
    'repositoryURI': Https_repo_URI,
    'userName': repo_user,
    'password': repo_password,
    'base64Data': ""
}
Http_repo_without_password = {
    'repositoryName': repository_name,
    'repositoryURI': Http_repo_URI,
    'userName': '',
    'password': '',
    'base64Data': ""
}
Https_repo_without_password = {
    "repositoryName": repository_name,
    "repositoryURI": Https_repo_URI,
    "userName": "",
    "password": "",
    "base64Data": ""
}

createBLProfiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "OVF547_CREATE_SP_%s" % SH1,
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

createBLProfilesWithGen9 = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": SH1,
        "description": SHM1,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": "",
        "enclosureUri": "",
        "name": "OVF547_CREATE_SP_%s" % SH1,
        "connectionSettings": {"connections": []},
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": Gen9FirmwareVersion,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode"
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        }
    }
]

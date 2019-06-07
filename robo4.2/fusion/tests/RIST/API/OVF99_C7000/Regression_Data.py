admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ia_name = 'OVF99IA'
ia_credentials = {'userName': ia_name, 'password': 'wpsthpvse1'}
sa_name = 'OVF99SA'
sa_credentials = {'userName': sa_name, 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
model = "C7000"
ia_users = [{'userName': ia_name, 'password': 'wpsthpvse1', 'fullName': 'OVF99IA', 'permissions': [], 'emailAddress': 'admin@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-555-0003', 'type': 'UserAndPermissions'}]
sa_users = [{'userName': sa_name, 'password': 'wpsthpvse1', 'fullName': 'OVF99SA', 'permissions': [], 'emailAddress': 'admin@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-555-0003', 'type': 'UserAndPermissions'}]

SPT_name = "OVF99_SPT"
SP_name = "OVF99_SP"
sp_param = "?force=ignoreServerHealth"

# Scopes
ia_user_scopes = ['scope1', 'scope2', 'scope3']
ia_part_scopes = ['scope1', 'scope2']
ia_except_scopes = ['scope4', 'scope5']
ia_scope_scope = 'scope1'
ia_minor_scope = 'scope3'
ia_anoher_scope = ['scope2', 'scope3']
ia_role_name = "Infrastructure administrator"
sa_role_name = "Server administrator"

Gen10Firmware = '2017.10.0'
Gen9Firmware = '2016.10.0'
invalidSPP = '/rest/firmware-drivers/invalid_uri'
invalidScope = '/rest/scopes/invalid_uri'
ok_status = "OK"
scope_type = "ScopeV3"
scope_name_a = "OVF99_SCOPE_A"
scope_name_b = "OVF99_SCOPE_B"
online_type = "FirmwareAndOSDrivers"
offline_type = "FirmwareOnlyOfflineMode"

invalid_resource_error = "INVALID_RESOURCE"
invalid_scope_error = "INVALID_SCOPE"
not_authorized_error = "NOT_AUTHORIZED_ERROR"
creation_not_authorized_error = "CREATION_NOT_AUTHORIZED_ERROR"
association_error = "ASSOCIATION_FORBIDDEN_BY_SCOPE"

Http_repo_with_password = {
    'repositoryName': 'external',
    'repositoryURI': 'http://16.114.218.204/webdav',
    'userName': 'joanna',
    'password': 'joanna',
    'base64Data': ""
}

ValidateFirmwares = ["1.7.0.0", "1.0.1.0", "2016.10.0", "2017.07.0", "2017.10.0"]

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

# Enclosures for wpst32
ENC1 = 'wpst32'
EG1 = 'GRP-%s' % ENC1
post_type = 'ServerProfileV9'
spt_type = 'ServerProfileTemplateV5'

# Server Hardware
SH1 = '%s, bay 1' % ENC1
SH2 = '%s, bay 3' % ENC1
SH3 = '%s, bay 5' % ENC1

# Server Hardware Model
SHM1 = "BL460C_GEN8"
SHM3 = "BL460c_GEN9"

TEMPLATE_SHT = 'BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class'
BAY1_SHT_NAME = 'BL460c Gen8:Flb1:HP FlexFabric 10Gb 2-port 554FLB Adapter'
Gen10_SHT_NAME = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'

# Create SP and update firmware
server_profile = {
    "type": post_type,
    "serverHardwareUri": SH3,
    "description": SHM3,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF99_CREATE_scope_SP_%s" % SH3,
    "bootMode": None,
    "connectionSettings": {
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareAndOSDrivers",
        "firmwareActivationType": "Immediate"},
    "initialScopeUris": [],
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

unassigned_server_profile = {
    "type": post_type,
    "serverHardwareUri": None,
    "description": SHM3,
    "serverHardwareTypeUri": "SHT:" + BAY1_SHT_NAME,
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF99_CREATE_scope_SP_%s" % SH1,
    "bootMode": None,
    "connectionSettings": {
    },
    "firmware": {
        "manageFirmware": True,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareAndOSDrivers",
        "firmwareActivationType": "Immediate"},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "category": "server-profiles",
    "eTag": ""
}

profile_template = {
    'type': spt_type,
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

# Create SP and update firmware using Gen 10 snap 1 as the baseline
createBLProfile = {
    "type": post_type,
    "serverHardwareUri": SH3,
    "description": SHM3,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF99_CREATE_scope_SP_%s" % SH3,
    "connectionSettings": {"connections": []},
    "boot": {
        "manageBoot": False
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": True,
        "firmwareBaselineUri": Gen10Firmware,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "initialScopeUris": [],
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

createOnlineBLProfile = {
    "type": post_type,
    "serverHardwareUri": SH3,
    "description": SHM3,
    "serverHardwareTypeUri": "",
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF99_CREATE_scope_SP_%s" % SH3,
    "connectionSettings": {"connections": []},
    "boot": {
        "manageBoot": False
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": True,
        "firmwareBaselineUri": Gen10Firmware,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareAndOSDrivers",
        "firmwareActivationType": "Immediate"},
    "initialScopeUris": [],
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

createBLProfileFromSPT = {
    "type": post_type,
    "serverHardwareUri": SH3,
    "description": SHM3,
    "serverHardwareTypeUri": 'SHT:' + TEMPLATE_SHT,
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF99_CREATE_scope_SP_%s" % SH3,
    "connectionSettings": {"connections": []},
    "boot": {
        "manageBoot": False
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": True,
        "firmwareBaselineUri": Gen10Firmware,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "initialScopeUris": [],
    "serverProfileTemplateUri": "",
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

createBLUnassignProfile = {
    "type": post_type,
    "serverHardwareUri": "",
    "description": SHM3,
    "serverHardwareTypeUri": 'SHT:' + TEMPLATE_SHT,
    "enclosureGroupUri": "",
    "enclosureUri": "",
    "name": "OVF99_CREATE_scope_unassign_SP_%s" % SHM3,
    "connectionSettings": {"connections": []},
    "boot": {
        "manageBoot": False
    },
    "bootMode": None,
    "firmware": {
        "manageFirmware": True,
        "firmwareBaselineUri": Gen10Firmware,
        "forceInstallFirmware": False,
        "firmwareInstallType": "FirmwareOnlyOfflineMode"},
    "initialScopeUris": [],
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    }
}

# Edit SP and update firmware using Gen 9 snap 6 as the baseline and configure local storage
editOnlineBLProfiles = [
    {
        "type": post_type,
        "name": "OVF99_EDIT_GEN10_SP_%s" % SH3,
        "serverHardwareUri": SH3,
        "description": SHM3,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": Gen10Firmware,
            "forceInstallFirmware": False,
            "firmwareInstallType": "FirmwareOnlyOfflineMode",
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

editBLProfiles = [
    {
        "type": post_type,
        "name": "OVF99_EDIT_GEN10_SP_%s" % SH3,
        "serverHardwareUri": SH3,
        "description": SHM3,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "firmware": {
            "manageFirmware": True,
            "firmwareBaselineUri": Gen10Firmware,
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

"""
OVF1086 C7000 HW DHCP initiator
"""
# pylint: disable=E0401,E0602
from dto import *

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

credentials_list = [
    {'userName': 'OVF1166_user', 'password': 'wpsthpvse1'},
    {'userName': 'jerry', 'password': 'cosmos@123', 'authLoginDomain': 'AD_Server'},
    {'userName': 'james', 'password': 'cosmos@123', 'authLoginDomain': 'AD_Server'}
]

CERT_BODY = {
    'members': [
        {
            'type': "CertificateAuthorityInfo",
            'certificateDetails': {
                'base64Data': '',
                'aliasName': '',
                'type': "CertificateDetailV2"
            }
        }
    ],
    'type': "CertificateAuthorityInfoCollection"
}

AD_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQPMm63L7kEbJKQ0QpKb/udzANBgkqhkiG9w0BAQUFADBJ" \
                 "\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow" \
                 "\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xODA1MjUwOTI5NTRaFw0yMzA1\nMjUwOTM5NTNaMEkxEzARBgoJkiaJk" \
                 "/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ" \
                 "\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG" \
                 "\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsi5cFUBbB7yIqshTXWG98bb195qg3qNnvZ" \
                 "\nT6HDldEPryc0Tt5UXbMsI1swvQzDcbgOIGS51/fJlS68Dguu5cV03207grkpFfRl\n8AAyrxeftWW" \
                 "+4x8Hy2sp4WFsEOM3hwKBIYOUhBrzyUZUv3u/nj8bMPJ52UEyvqiT\n/XqgEFlCTdFX3vGMRVowN9jARFfA9AMACby8kGHkt" \
                 "+lsBbC0QEuMWiBd55mqlf3o\nlvbb+EWh1nd+mVfu4ghuVr4ztY1SjyXcs6Ji71LGjidhI2js/Kc/Mu8zqlitf1q2" \
                 "\nPrUobXXAln3Yq99tWLaAx+WgAZ3ZBJYwHHzR3HqPHe52lqun4wIDAQABo4GRMIGO" \
                 "\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH" \
                 "/MB0GA1UdDgQWBBSl4IMWKKfP1EKAPFWvgFReUVq2ozASBgkrBgEEAYI3\nFQEEBQIDAwADMCMGCSsGAQQBgjcVAgQWBBR/wd" \
                 "/nomlY2SxW+cy7T5VoLZMT/zAN\nBgkqhkiG9w0BAQUFAAOCAQEAmLl8cFATJyUZ979i3ZhMcj1WV1QhlP3eU3bsKgkW\nD" \
                 "/n9Q2SbgWSbKw08m8F9KetBEmZdvAmfojcOPAww/xQrxc9gLCfpUhnaUDe4fpcV\nuAnU+S3osPj3CL5W9pIkeaXol" \
                 "/Dnj9BmNbD5OxvxtZbEF8E353ikcytMTKggIT4S\n3Bst+ayI3m1gI4KA9ZKjR4USxZ5TM7E" \
                 "/kJJZNtK0aVniWc7o2WhECw2dUe2ZzufQ\nR+DfY56kTewvTiVAA2w5/+85Ywf/8V1yy4E6Di6h63FN/LUXX2lZKnMftekjjuWz" \
                 "\nzH1KNRrV8HG2hvN8FqkVTAcnWEWyjr7omTLi+0bDhI1BVw==\n-----END CERTIFICATE-----"

AD_cred = {"userName": "Administrator", "password": "Wpsthpvse1234"}

ALIAS_NAME = "AD_Server"

remove_user_headers = {
    'Content-Type': 'application/json',
    'Accept-Language': 'en_US',
    'Accept': 'appliacation/json, */*',
    'X-Api-Version': 500
}

ENC1 = '0000A66101'
SH1 = '%s, bay 5' % ENC1
EG1 = 'EG_SYNERGY'
VOL1 = 'CN75120D7B-FA-Vol2-Full-1GB-R5-Private'
VOL3 = 'CN75120D7B-FA-Vol3-Thin-1GB-R5-Shared'
FC1 = 'FA1'
SHM1 = 'SY 660 Gen9 2'
SPT = 'OVF1166_SPT'
SP1 = 'FVT_Tbird_reg1_r1'
SP2 = 'FVT_Tbird_reg1_r5'
SVT1 = 'CN75120D7B-FA-VT1-Thin-1GB-R5-Private'
SSYS1 = 'wpst3par-7200-7-srv'

directory_profiles = [
    {
        "type": DOMAIN_TYPE,
        "name": "16.125.76.222",
        "credential": {"userName": "wpstuser", "password": "P@ssw0rd"},
        "authProtocol": "LDAP",
        "orgUnits": ["OU=Users", "OU=groups"],
        "userNamingAttribute": "CN",
        "baseDN": "dc=ldapfc,dc=com",
        "authnType": "CREDENTIAL",
        "directoryBindingType": "USER_ACCOUNT",
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": "16.125.76.222",
                "directoryServerCertificateBase64Data": "-----BEGIN "
                                                        "CERTIFICATE-----\nMIIECjCCAvKgAwIBAgIJAO9jxxrDwwEjMA0GCSqGSIb3DQEBCwUAMIGRMQswCQYD\r\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\r\nMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEW\r\nMBQGCgmSJomT8ixkARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTAeFw0x\r\nODA1MjIxNjI0MjBaFw0yODAyMTkxNjI0MjBaMIGRMQswCQYDVQQGEwJVUzETMBEG\r\nA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9I\r\nZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEWMBQGCgmSJomT8ixk\r\nARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTCCASIwDQYJKoZIhvcNAQEB\r\nBQADggEPADCCAQoCggEBAO2qMOGXDpsyb25et7r4ya0R1d5DfB5wo6HipxtyRL2H\r\nkMfvhyHB7izNdxbdUmJW6Zf3FkDB/bTolEjMPgAwFdfMOTk5T5fbF+eUDsHnk3Zz\r\nBBzHQuQ+r6Z+K2Av9P7+pOkOUrkjt28pcFYeYZeYHQ1iUIFb9IVRut0bf+8XDlCU\r\nTgYK2KmzKyPISBas/3KgngjdY1F9zccW/wIBaHou77vM9ozOxdT6qjP+hmMx9WJY\r\nE7gzMQT8+9Gyh0XZzhrKqPFHHj12ztKHlknMDP9kv9esVPIUyD3viBVjdnmpEE+S\r\ny62wuVdGsJhJbyyM2peOTS/LoFW0bcg2Sbr9WWrjNkECAwEAAaNjMGEwHQYDVR0O\r\nBBYEFJgJWnvnI/CINkmuoBpQqYx5jPR5MB8GA1UdIwQYMBaAFJgJWnvnI/CINkmu\r\noBpQqYx5jPR5MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMA0GCSqG\r\nSIb3DQEBCwUAA4IBAQA4HfPrPCmW10uYSL7suwlKLfk+5nRqQU5U5emKi0YAXzuL\r\nIKg7cdjQIZin01Zu6VbXXW8Kx7gof8X98UFXC1fWe0o/z3H5Y/C67we/NkUkhwmz\r\nDZB6SA7HJcslMCPJGIgV2UEyDA/ZN1rmSh5UeX1fzBBgW1NzgTwH8J2IR9j+LRbo\r\n/ujN7sNMUP47XAyjIe8mTMwC7mXOhdYYl432EPunRSNMHdXn2i37lTPoT19fIhDy\r\nN5eDbQAqXtviOHDtHbd1kZM0+RxZY9BDrLu4NpzrSXIWXsk6HKASuUf3i+chXZZ0\r\neDd8PulIMpKtQslgoDJyGnClYn4RxOdMPjwu5Qvn\r\n-----END CERTIFICATE-----",
                "directoryServerSSLPortNumber": "636",
                "directoryServerCertificateStatus": "Yes",
                "serverStatus": "",
            }
        ]
    },
    {
        "type": DOMAIN_TYPE,
        "name": "AD_Server",
        "credential": AD_cred,
        "authProtocol": "AD",
        "orgUnits": [],
        "userNamingAttribute": "",
        "baseDN": "DC=wpstAD,DC=com",
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": "16.125.77.30",
                "directoryServerCertificateBase64Data": AD_CERTIFICATE,
                "directoryServerSSLPortNumber": "636",
                # "validUntil": "2022-07-04T06:57:43.000Z",
                "directoryServerCertificateStatus": "Yes",
                "serverStatus": "true",
                "category": "users"
            }
        ]
    }
]

user_profiles = [
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF1166_user",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF1166_user"
    }
]

group_profiles = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Scope operator",
                    "scopeUri": None
                }
            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    },
    {
        "credentials": AD_cred,
        "group2PermissionPerGroup": {
            "egroup": "Domain Admins",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Scope operator",
                    "scopeUri": None
                },
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    }
]

scope_profiles = [
    {
        "type": SCOPE_TYPE,
        "name": "OVF1166ScopeNoneResource1",
        "description": "Sample Scope description"
    }
]

server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1166_SPT",
        "description": "",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "affinity": "Bay",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "osDeploymentSettings": None,
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bootMode": None,
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "volumeAttachments": [],
            "manageSanStorage": False
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": False,
            "connections": []
        }
    }
]

n001_server_profile = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "OVF1166_n001_sp",
        "description": "",
        "templateCompliance": "Unknown",
        "serverHardwareUri": "SH:{}".format(SH1),
        "enclosureGroupUri": EG1,
        "hideUnusedFlexNics": True,
        "firmware": {
            "reapplyState": "NotApplying",
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": None,
            "firmwareInstallType": None,
            "forceInstallFirmware": False,
            "manageFirmware": False,
            "firmwareBaselineUri": None
        },
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "connectionSettings": {
            "connections": []
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios": {
            "reapplyState": "NotApplying",
            "overriddenSettings": [],
            "manageBios": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying",
            "manageSanStorage": False
        },
        "osDeploymentSettings": None
    }
]

n002_server_profile = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "OVF1166_n002_sp",
        "description": "",
        "serverHardwareUri": None,
        "serverHardwareTypeUri": SHM1,
        "templateCompliance": "Unknown",
        "enclosureGroupUri": EG1,
        "hideUnusedFlexNics": True,
        "firmware": {
            "reapplyState": "NotApplying",
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": None,
            "firmwareInstallType": None,
            "forceInstallFirmware": False,
            "manageFirmware": False,
            "firmwareBaselineUri": None
        },
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC1),
                    "portId": "Auto",
                    "macType": "Virtual",
                    "wwpnType": "Virtual",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ]
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios": {
            "reapplyState": "NotApplying",
            "overriddenSettings": [],
            "manageBios": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying",
            "manageSanStorage": False
        },
        "osDeploymentSettings": None
    }
]

n003_server_profile = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "OVF1166_n003_sp",
        "description": "",
        "serverHardwareUri": None,
        "serverHardwareTypeUri": SHM1,
        "templateCompliance": "Unknown",
        "enclosureGroupUri": EG1,
        "hideUnusedFlexNics": True,
        "firmware": {
            "reapplyState": "NotApplying",
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": None,
            "firmwareInstallType": None,
            "forceInstallFirmware": False,
            "manageFirmware": False,
            "firmwareBaselineUri": None
        },
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "connectionSettings": {
            "connections": []
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios": {
            "reapplyState": "NotApplying",
            "overriddenSettings": [],
            "manageBios": False
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "volumeAttachments": [
                {
                    "volume": None,
                    "isBootVolume": False,
                    "associatedTemplateAttachmentId": None,
                    "storagePaths": [],
                    "state": "Reserved",
                    "volumeUri": "FC:{}".format(VOL3),
                    "lunType": "Auto",
                    "id": 1
                }
            ],
            "manageSanStorage": True
        },
        "osDeploymentSettings": None
    }
]

n004_server_profile = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "OVF1166_n004_sp",
        "description": "",
        "serverProfileTemplateUri": "SPT:{}".format(SPT),
        "serverHardwareUri": None,
        "templateCompliance": "Unknown",
        "enclosureGroupUri": EG1,
        "hideUnusedFlexNics": True,
        "firmware": {
            "reapplyState": "NotApplying",
            "firmwareScheduleDateTime": None,
            "firmwareActivationType": None,
            "firmwareInstallType": None,
            "forceInstallFirmware": False,
            "manageFirmware": False,
            "firmwareBaselineUri": None
        },
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "connectionSettings": {
            "connections": []
        },
        "bootMode": None,
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying",
            "manageSanStorage": False
        },
        "osDeploymentSettings": None
    }
]

n005_server_profile_template = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1166_SPTn005",
        "description": "",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "affinity": "Bay",
        "iscsiInitiatorNameType": "AutoGenerated",
        "osDeploymentSettings": None,
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bootMode": None,
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "volumeAttachments": [],
            "manageSanStorage": False
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC1),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    }
]

n006_server_profile_template = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1166_SPTn006",
        "description": "",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "affinity": "Bay",
        "iscsiInitiatorNameType": "AutoGenerated",
        "osDeploymentSettings": None,
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL3),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": False,
            "connections": []
        }
    }
]

n007_server_profile_template = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1166_SPTn007",
        "description": "",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "affinity": "Bay",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "osDeploymentSettings": None,
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "ROOT:{}".format(SP1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP1),
                            "size": 1073741824,
                            "provisioningType": "Thin",
                            "isShareable": False
                        }
                    },
                    "volumeStorageSystemUri": "SSYS:{}".format(SSYS1)
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": False,
            "connections": []
        }
    }
]

n008_server_profile_template = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1166_SPT4",
        "description": "",
        "serverProfileDescription": "",
        "serverHardwareTypeUri": "SHT:{}".format(SHM1),
        "enclosureGroupUri": "EG:{}".format(EG1),
        "affinity": "Bay",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "osDeploymentSettings": None,
        "firmware": {
            "manageFirmware": False,
            "forceInstallFirmware": False
        },
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv2",
                            "storagePool": "SP:{}".format(SP2),
                            "description": "",
                            "size": 1073741824,
                            "provisioningType": "Thin"
                        }
                    },
                    "volumeStorageSystemUri": "SSYS:{}".format(SSYS1)
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": False,
            "connections": []
        }
    }
]

n009_volume_profile = [
    {
        "properties": {
            "name": "OVF1166_Volume1",
            "description": "volume description",
            "storagePool": SP1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "snapshotPool": SP1,
            "storageSystem": None,
            "isShareable": False
        },
        "templateUri": "ROOT",
        "isPermanent": True
    },
    {
        "properties": {
            "name": "OVF1166_Volume2",
            "description": "volume description",
            "storagePool": SP1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "snapshotPool": SP1,
            "storageSystem": None,
            "isShareable": False
        },
        "templateUri": "ROOT",
        "isPermanent": True
    },
    {
        "properties": {
            "name": "OVF1166_Volume3",
            "description": "volume description",
            "storagePool": SP1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "snapshotPool": SP1,
            "storageSystem": None,
            "isShareable": False
        },
        "templateUri": "ROOT",
        "isPermanent": True
    }
]

n010_volume_profile = [
    {
        "properties": {
            "name": "OVF1166_Volume4",
            "description": "volume description",
            "storagePool": SP1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "isShareable": False,
            "storageSystem": None,
            "snapshotPool": SP1
        },
        "templateUri": SVT1,
        "isPermanent": True
    },
    {
        "properties": {
            "name": "OVF1166_Volume5",
            "description": "volume description",
            "storagePool": SP1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "isShareable": False,
            "storageSystem": None,
            "snapshotPool": SP1
        },
        "templateUri": SVT1,
        "isPermanent": True
    },
    {
        "properties": {
            "name": "OVF1166_Volume6",
            "description": "volume description",
            "storagePool": SP1,
            "size": 1073741824,
            "provisioningType": "Thin",
            "isShareable": False,
            "storageSystem": None,
            "snapshotPool": SP1
        },
        "templateUri": SVT1,
        "isPermanent": True
    }
]

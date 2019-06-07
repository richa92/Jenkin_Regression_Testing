"""OVF1504 for C7000"""
# pylint: disable=E0401,E0602

from dto import *

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

AD_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQPMm63L7kEbJKQ0QpKb/udzANBgkqhkiG9w0BAQUFADBJ\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xODA1MjUwOTI5NTRaFw0yMzA1\nMjUwOTM5NTNaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsi5cFUBbB7yIqshTXWG98bb195qg3qNnvZ\nT6HDldEPryc0Tt5UXbMsI1swvQzDcbgOIGS51/fJlS68Dguu5cV03207grkpFfRl\n8AAyrxeftWW+4x8Hy2sp4WFsEOM3hwKBIYOUhBrzyUZUv3u/nj8bMPJ52UEyvqiT\n/XqgEFlCTdFX3vGMRVowN9jARFfA9AMACby8kGHkt+lsBbC0QEuMWiBd55mqlf3o\nlvbb+EWh1nd+mVfu4ghuVr4ztY1SjyXcs6Ji71LGjidhI2js/Kc/Mu8zqlitf1q2\nPrUobXXAln3Yq99tWLaAx+WgAZ3ZBJYwHHzR3HqPHe52lqun4wIDAQABo4GRMIGO\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBSl4IMWKKfP1EKAPFWvgFReUVq2ozASBgkrBgEEAYI3\nFQEEBQIDAwADMCMGCSsGAQQBgjcVAgQWBBR/wd/nomlY2SxW+cy7T5VoLZMT/zAN\nBgkqhkiG9w0BAQUFAAOCAQEAmLl8cFATJyUZ979i3ZhMcj1WV1QhlP3eU3bsKgkW\nD/n9Q2SbgWSbKw08m8F9KetBEmZdvAmfojcOPAww/xQrxc9gLCfpUhnaUDe4fpcV\nuAnU+S3osPj3CL5W9pIkeaXol/Dnj9BmNbD5OxvxtZbEF8E353ikcytMTKggIT4S\n3Bst+ayI3m1gI4KA9ZKjR4USxZ5TM7E/kJJZNtK0aVniWc7o2WhECw2dUe2ZzufQ\nR+DfY56kTewvTiVAA2w5/+85Ywf/8V1yy4E6Di6h63FN/LUXX2lZKnMftekjjuWz\nzH1KNRrV8HG2hvN8FqkVTAcnWEWyjr7omTLi+0bDhI1BVw==\n-----END CERTIFICATE-----"

LDAP_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIECjCCAvKgAwIBAgIJAO9jxxrDwwEjMA0GCSqGSIb3DQEBCwUAMIGRMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\nMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEW\nMBQGCgmSJomT8ixkARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTAeFw0x\nODA1MjIxNjI0MjBaFw0yODAyMTkxNjI0MjBaMIGRMQswCQYDVQQGEwJVUzETMBEG\nA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9I\nZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEWMBQGCgmSJomT8ixk\nARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTCCASIwDQYJKoZIhvcNAQEB\nBQADggEPADCCAQoCggEBAO2qMOGXDpsyb25et7r4ya0R1d5DfB5wo6HipxtyRL2H\nkMfvhyHB7izNdxbdUmJW6Zf3FkDB/bTolEjMPgAwFdfMOTk5T5fbF+eUDsHnk3Zz\nBBzHQuQ+r6Z+K2Av9P7+pOkOUrkjt28pcFYeYZeYHQ1iUIFb9IVRut0bf+8XDlCU\nTgYK2KmzKyPISBas/3KgngjdY1F9zccW/wIBaHou77vM9ozOxdT6qjP+hmMx9WJY\nE7gzMQT8+9Gyh0XZzhrKqPFHHj12ztKHlknMDP9kv9esVPIUyD3viBVjdnmpEE+S\ny62wuVdGsJhJbyyM2peOTS/LoFW0bcg2Sbr9WWrjNkECAwEAAaNjMGEwHQYDVR0O\nBBYEFJgJWnvnI/CINkmuoBpQqYx5jPR5MB8GA1UdIwQYMBaAFJgJWnvnI/CINkmu\noBpQqYx5jPR5MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMA0GCSqG\nSIb3DQEBCwUAA4IBAQA4HfPrPCmW10uYSL7suwlKLfk+5nRqQU5U5emKi0YAXzuL\nIKg7cdjQIZin01Zu6VbXXW8Kx7gof8X98UFXC1fWe0o/z3H5Y/C67we/NkUkhwmz\nDZB6SA7HJcslMCPJGIgV2UEyDA/ZN1rmSh5UeX1fzBBgW1NzgTwH8J2IR9j+LRbo\n/ujN7sNMUP47XAyjIe8mTMwC7mXOhdYYl432EPunRSNMHdXn2i37lTPoT19fIhDy\nN5eDbQAqXtviOHDtHbd1kZM0+RxZY9BDrLu4NpzrSXIWXsk6HKASuUf3i+chXZZ0\neDd8PulIMpKtQslgoDJyGnClYn4RxOdMPjwu5Qvn\r\n-----END CERTIFICATE-----"

LDAP_IP = "16.125.76.222"
LDAP_cred = {"userName": "wpstuser", "password": "P@ssw0rd"}
LDAP_GRP = "FUSION_NET_ADMIN"
LDAP_GRP_USER = "nat"
LDAP_GRP_USER_PSWD = "networkadmin"
LDAP_BASE_DN = "dc=ldapfc,dc=com"

AD_IP = "16.125.77.30"
AD_cred = {"userName": "james", "password": "cosmos@123"}
AD_GRP = "AD_SVR_ADMIN"
AD_GRP_USER = "adserver"
AD_GRP_USER_PSWD = "Appliance@dmin123"
AD_BASE_DN = "dc=wpstAD,dc=com"

credentials_list = [
    {'userName': 'OVF1504_spa', 'password': 'wpsthpvse1'},
    {
        "userName": LDAP_GRP_USER, "password": LDAP_GRP_USER_PSWD,
        "authLoginDomain": LDAP_IP
    },
    {
        "userName": AD_GRP_USER, "password": AD_GRP_USER_PSWD,
        "authLoginDomain": "AD_Server"
    }
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

AD_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQPMm63L7kEbJKQ0QpKb/udzANBgkqhkiG9w0BAQUFADBJ\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xODA1MjUwOTI5NTRaFw0yMzA1\nMjUwOTM5NTNaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsi5cFUBbB7yIqshTXWG98bb195qg3qNnvZ\nT6HDldEPryc0Tt5UXbMsI1swvQzDcbgOIGS51/fJlS68Dguu5cV03207grkpFfRl\n8AAyrxeftWW+4x8Hy2sp4WFsEOM3hwKBIYOUhBrzyUZUv3u/nj8bMPJ52UEyvqiT\n/XqgEFlCTdFX3vGMRVowN9jARFfA9AMACby8kGHkt+lsBbC0QEuMWiBd55mqlf3o\nlvbb+EWh1nd+mVfu4ghuVr4ztY1SjyXcs6Ji71LGjidhI2js/Kc/Mu8zqlitf1q2\nPrUobXXAln3Yq99tWLaAx+WgAZ3ZBJYwHHzR3HqPHe52lqun4wIDAQABo4GRMIGO\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBSl4IMWKKfP1EKAPFWvgFReUVq2ozASBgkrBgEEAYI3\nFQEEBQIDAwADMCMGCSsGAQQBgjcVAgQWBBR/wd/nomlY2SxW+cy7T5VoLZMT/zAN\nBgkqhkiG9w0BAQUFAAOCAQEAmLl8cFATJyUZ979i3ZhMcj1WV1QhlP3eU3bsKgkW\nD/n9Q2SbgWSbKw08m8F9KetBEmZdvAmfojcOPAww/xQrxc9gLCfpUhnaUDe4fpcV\nuAnU+S3osPj3CL5W9pIkeaXol/Dnj9BmNbD5OxvxtZbEF8E353ikcytMTKggIT4S\n3Bst+ayI3m1gI4KA9ZKjR4USxZ5TM7E/kJJZNtK0aVniWc7o2WhECw2dUe2ZzufQ\nR+DfY56kTewvTiVAA2w5/+85Ywf/8V1yy4E6Di6h63FN/LUXX2lZKnMftekjjuWz\nzH1KNRrV8HG2hvN8FqkVTAcnWEWyjr7omTLi+0bDhI1BVw==\n-----END CERTIFICATE-----"

AD_cred = {"userName": "Administrator", "password": "Wpsthpvse1234"}

ALIAS_NAME = "AD_Server"

remove_user_headers = {
    'Content-Type': 'application/json',
    'Accept-Language': 'en_US',
    'Accept': 'application/json, */*',
    'X-Api-Version': 500
}
# Enclosures wpst23
ENC1 = 'wpst23'
SH1 = '%s, bay 1' % ENC1
EG1 = 'GRP-%s' % ENC1
VOL1 = '{}-FA-Vol2-Full-1GB-R5-Private'.format(ENC1.upper())
VOL3 = '{}-FA-Vol3-Thin-1GB-R5-Shared'.format(ENC1.upper())
VOL4 = '{}-FA-Vol4-Full-1GB-R5-Shared'.format(ENC1.upper())
FC1 = 'FA3'
FC2 = 'FA4'
SHM1 = 'BL420c Gen8 1'
SPT = 'OVF1504_SPT'
SP1 = 'FC_%s_r1' % ENC1
SP2 = 'FC_%s_r5' % ENC1
SVT1 = '{}-FA-VT1-Thin-1GB-R5-Private'.format(ENC1.upper())
SVT2 = '{}-FA-VT3-Thin-1GB-R5-Shared'.format(ENC1.upper())
SSYS1 = 'wpst3par-7200-7-srv'
NS1 = 'Net-Set1'
ETH1 = 'dev100'
INTERCONNECT1 = '{}, interconnect 1'.format(ENC1)
LI1 = '{}-LIG-{}'.format(ENC1, ENC1)
FCOE1 = 'FCoE1'

directory_profiles = [
    {
        "type": DOMAIN_TYPE,
        "name": LDAP_IP,
        "credential": LDAP_cred,
        "authProtocol": "LDAP",
        "orgUnits": [
            "ou=Users",
            "ou=groups"
        ],
        "userNamingAttribute": "UID",
        "baseDN": LDAP_BASE_DN,
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": LDAP_IP,
                "directoryServerCertificateBase64Data": LDAP_CERTIFICATE,
                "directoryServerSSLPortNumber": "636",
                "validUntil": "2027-11-23T08:00:22.000Z",
                "directoryServerCertificateStatus": "Yes",
                "serverStatus": "true",
                "category": "users"
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
        "baseDN": AD_BASE_DN,
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": AD_IP,
                "directoryServerCertificateBase64Data": AD_CERTIFICATE,
                "directoryServerSSLPortNumber": "636",
                "validUntil": "2022-07-04T06:57:43.000Z",
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
        "fullName": "OVF1504_spa",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF1504_spa"
    }
]

group_profiles = [
    {
        "credentials": LDAP_cred,
        "group2PermissionPerGroup": {
            "egroup": LDAP_GRP,
            "loginDomain": LDAP_IP,
            "permissions": [],
            "type": "LoginDomainGroupPermission"
        },
        "type": LOGIN_DOMAIN_GROUP_CRED_TYPE
    },
    {
        "credentials": AD_cred,
        "group2PermissionPerGroup": {
            "egroup": AD_GRP,
            "loginDomain": "AD_Server",
            "permissions": [],
            "type": "LoginDomainGroupPermission"
        },
        "type": LOGIN_DOMAIN_GROUP_CRED_TYPE
    }
]

scope_profile = {
    "type": SCOPE_TYPE,
    "name": "OVF1504Scope",
    "description": "Sample Scope description"
}

p001_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_01",
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
            "manageBoot": True,
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_02",
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
            "manageBoot": True,
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_03",
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
            "manageBoot": True,
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

p017_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_01",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "5",
                    "lunType": "Manual",
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_02",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "3",
                    "lunType": "Manual",
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_03",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "2",
                    "lunType": "Manual",
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

n001_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n001_01",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n001_02",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n001_03",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
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

n006_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_01",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "5",
                    "lunType": "Manual",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_02",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "3",
                    "lunType": "Manual",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_03",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "2",
                    "lunType": "Manual",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
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

n002_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n002_01",
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
            "manageBoot": True,
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n002_02",
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
            "manageBoot": True,
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n002_03",
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
            "manageBoot": True,
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    }
]

n008_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_01",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "5",
                    "lunType": "Manual",
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_02",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "3",
                    "lunType": "Manual",
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_03",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "2",
                    "lunType": "Manual",
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    }
]

n004_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n002_01",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n002_02",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_n002_03",
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
            "manageBoot": True,
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
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    }
]

n009_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_01",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "5",
                    "lunType": "Manual",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_02",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "3",
                    "lunType": "Manual",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p001_03",
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
            "manageBoot": True,
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
            "volumeAttachments": [
                {
                    "id": 1,
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": "2",
                    "lunType": "Manual",
                    "storagePaths": [],
                    "volumeUri": "FC:{}".format(VOL4),
                    "volume": None
                }
            ],
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True
        },
        "category": "server-profile-templates",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "FibreChannel",
                    "networkUri": "FC:{}".format(FC2),
                    "portId": "Auto",
                    "requestedMbps": "2500"
                }
            ]
        }
    }
]

server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT1",
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT2",
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT3",
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

p013_new_users_with_spa_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p013_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            }
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_1"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_2",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_2"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_3",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            },
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_3"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_4",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            },
            {
                "roleName": "Server administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_4"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_5",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_5"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_6",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_6"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_7",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server profile architect",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF1504_p001_user_7"
    }
]

p014_new_group_with_spa_role = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Server profile architect",
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
                    "roleName": "Server profile architect",
                    "scopeUri": None
                }
            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    }
]

p015_new_users_wo_spa_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Read only",
                "scopeUri": None
            }
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_1"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_2",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_2"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_3",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_3"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_4",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_4"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_5",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_5"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_6",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_6"
    },
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF1504_p001_user_7",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_7"
    }
]

p015_assign_users_spa_role = [
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Read only",
            "type": ROLE_NAME_TYPE
        }
    ],
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Backup administrator",
            "type": ROLE_NAME_TYPE
        }
    ],
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Server administrator",
            "type": ROLE_NAME_TYPE
        }
    ],
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Storage administrator",
            "type": ROLE_NAME_TYPE
        }
    ],
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Server firmware operator",
            "type": ROLE_NAME_TYPE
        }
    ],
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Software administrator",
            "type": ROLE_NAME_TYPE
        }
    ],
    [
        {
            "roleName": "Server profile architect",
            "type": ROLE_NAME_TYPE
        },
        {
            "roleName": "Backup administrator",
            "type": ROLE_NAME_TYPE
        }
    ]
]

p016_new_group_wo_spa_role = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": LOGIN_DOMAIN_GROUP_PERMISSION_TYPE
        },
        "type": LOGIN_DOMAIN_GROUP_CRED_TYPE
    },
    {
        "credentials": AD_cred,
        "group2PermissionPerGroup": {
            "egroup": "Domain Admins",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": LOGIN_DOMAIN_GROUP_PERMISSION_TYPE
        },
        "type": LOGIN_DOMAIN_GROUP_CRED_TYPE
    }
]

p016_assign_group_with_spa_role = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Server profile architect",
                    "scopeUri": None
                },
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": LOGIN_DOMAIN_GROUP_PERMISSION_TYPE
        },
        "type": LOGIN_DOMAIN_GROUP_CRED_TYPE
    },
    {
        "credentials": AD_cred,
        "group2PermissionPerGroup": {
            "egroup": "Domain Admins",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Server profile architect",
                    "scopeUri": None
                },
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": LOGIN_DOMAIN_GROUP_PERMISSION_TYPE
        },
        "type": LOGIN_DOMAIN_GROUP_CRED_TYPE
    }
]

p002_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p002_01",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p002_02",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p002_03",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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

p003_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_01",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_02",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_03",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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

p007_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_01",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_02",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_03",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
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

p006_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p002_01",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p002_02",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p002_03",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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

p008_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_01",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_02",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_03",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT1),
                        "properties": {
                            "name": "nv",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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

n010_server_profile_template_profiles = [
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_01",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT2),
                        "properties": {
                            "name": "nv2",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_02",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT2),
                        "properties": {
                            "name": "nv2",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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
    },
    {
        "type": SERVER_PROFILE_TEMPLATE_TYPE,
        "name": "OVF1504_SPT_p003_03",
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
            "manageBoot": True,
            "order": [
                "CD",
                "Floppy",
                "USB",
                "HardDisk",
                "PXE"
            ]
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
                    "associatedTemplateAttachmentId": 'SPTVAID:1',
                    "isBootVolume": False,
                    "lun": None,
                    "lunType": "Auto",
                    "storagePaths": [],
                    "volume": {
                        "isPermanent": True,
                        "templateUri": "SVT:{}".format(SVT2),
                        "properties": {
                            "name": "nv2",
                            "description": "",
                            "storagePool": "SP:{}".format(SP2),
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

enclosure_profile = {
    "op": "replace", "path": "/name", "value": 'NewEnclosure', "name": ENC1
}

fc_profile = [
    {
        'name': FC1,
        'type': FC_NETWORK_TYPE,
        'fabricType': 'FabricAttach',
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True,
        'managedSanUri': None
    }
]

fcoe_profile = [
    {'name': 'fcoe_103', 'type': FCOE_NETWORK_TYPE, 'vlanId': 105}
]

svt_profile = {
    'name': '%s-FA-VT1-Thin-1GB-R5-Private' % ENC1.upper(),
    'description': 'update',
    'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
    'properties': {
        'storageSystem': 'wpst3par-7200-7-srv',
        'name': {
            'title': 'Volume name',
            'description': 'A volume name between 1 and 100 characters',
            'type': 'string',
            'minLength': 1,
            'maxLength': 100,
            'required': True,
            'meta': {'locked': False}
        },
        'description': {
            'title': 'Description',
            'description': 'A description for the volume',
            'type': 'string',
            'minLength': 0,
            'maxLength': 2000,
            'default': '3Par1 pool1 private',
            'meta': {'locked': False}
        },
        'storagePool': {
            'title': 'Storage Pool',
            'description': 'A common provisioning group URI reference',
            'type': 'string',
            'required': True,
            'format': 'x-uri-reference',
            'meta': {
                'locked': False, 'createOnly': True,
                'semanticType': 'device-storage-pool'
            },
            'default': 'FC_%s_r5' % ENC1,
        },
        'size': {
            'title': 'Capacity',
            'description': 'The capacity of the volume in bytes',
            'type': 'integer',
            'required': True,
            'minimum': 1073741824,
            'maximum': 17592186044416,
            'meta': {'locked': False, 'semanticType': 'capacity'},
            'default': 1073741824,
        },
        'isShareable': {
            'title': 'Is Shareable',
            'description': 'The shareability of the volume',
            'type': 'boolean',
            'meta': {'locked': False},
            'default': True,
        },
        'provisioningType': {
            'title': 'Provisioning Type',
            'description': 'The provisioning type for the volume',
            'type': 'string',
            'enum': ['Thin', 'Full'],
            'meta': {'locked': True, 'createOnly': True},
            'default': 'Thin'
        },
        'snapshotPool': {
            'title': 'Snapshot Pool',
            'description': 'A URI referenceto the common provisioning group used to create snapshots',
            'type': 'string',
            'format': 'x-uri-reference',
            'meta': {
                'locked': True, 'semanticType': 'device-snapshot-storage-pool'
            },
            'default': 'FC_%s_r5' % ENC1,
        }
    },
}

sp_profile = {
    "type": SERVER_PROFILE_TYPE,
    "name": "OVF1504_p010_sp",
    "description": "",
    "serverHardwareUri": None,
    "serverHardwareTypeUri": 'SHT:{}'.format(SHM1),
    "templateCompliance": "Unknown",
    "enclosureGroupUri": 'EG:{}'.format(EG1),
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
    "bootMode": None,
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "HardDisk",
            "PXE"
        ],
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
                "volumeUri": "FC:{}".format(VOL1),
                "lunType": "Auto",
                "id": 1
            }
        ],
        "manageSanStorage": True
    },
    "osDeploymentSettings": None
}

sp1_profile = {
    "type": SERVER_PROFILE_TYPE,
    "name": "OVF1504_p010_sp",
    "description": "update this sp",
    "serverHardwareUri": None,
    "serverHardwareTypeUri": 'SHT:{}'.format(SHM1),
    "templateCompliance": "Unknown",
    "enclosureGroupUri": 'EG:{}'.format(EG1),
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
    "bootMode": None,
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "HardDisk",
            "PXE"
        ],
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
                "volumeUri": "FC:{}".format(VOL1),
                "lunType": "Auto",
                "id": 1
            }
        ],
        "manageSanStorage": True
    },
    "osDeploymentSettings": None
}

vol_profile = {'name': VOL3, "isShareable": True}

storage_pool_profile = {
    "storageSystemUri": SSYS1, "name": SP1, "isManaged": False
}

network_set_profiles = [
    {
        'name': 'Net-Set3', 'type': NETWORK_SET_TYPE, 'networkUris': ['dev100'],
        'nativeNetworkUri': None
    },
    {
        'name': 'Net-Set4', 'type': NETWORK_SET_TYPE, 'networkUris': ['dev100'],
        'nativeNetworkUri': None
    },
    {
        'name': 'Net-Set5', 'type': NETWORK_SET_TYPE, 'networkUris': ['dev100'],
        'nativeNetworkUri': None
    }
]

eth_profile = {
    'name': 'dev100', 'type': ETHERNET_NETWORK_TYPE, 'vlanId': 500,
    'purpose': 'General', 'smartLink': False,
    'privateNetwork': False, 'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged'
}

interconnect_dto = {'name': INTERCONNECT1}

lig_profile = [
    {
        'name': 'LIG-%s' % ENC1,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [
            {
                'enclosure': 1, 'enclosureIndex': 1, 'bay': 1,
                'type': 'HP VC FlexFabric 10Gb/24-Port Module'
            },
            {
                'enclosure': 1, 'enclosureIndex': 1, 'bay': 2,
                'type': 'HP VC FlexFabric 10Gb/24-Port Module'
            },
            {
                'enclosure': 1, 'enclosureIndex': 1, 'bay': 3,
                'type': 'HP VC FlexFabric 10Gb/24-Port Module'
            },
            {
                'enclosure': 1, 'enclosureIndex': 1, 'bay': 4,
                'type': 'HP VC FlexFabric 10Gb/24-Port Module'
            },
            {
                'enclosure': 1, 'enclosureIndex': 1, 'bay': 5,
                'type': 'HP VC 8Gb 20-Port FC Module'
            },
            {
                'enclosure': 1, 'enclosureIndex': 1, 'bay': 6,
                'type': 'HP VC 8Gb 20-Port FC Module'
            },
        ],
        'uplinkSets': [],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    }
]

li_profile = {
    "type": "telemetry-configuration",
    "sampleInterval": 300,
    "sampleCount": 12,
    "enableTelemetry": False,
    "description": None,
    "name": LI1,
    "category": "telemetry-configurations"
}

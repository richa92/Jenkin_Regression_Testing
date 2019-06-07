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

p001_credentials_list = [
    {'userName': 'OVF2_p001_user_1', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_2', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_3', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_4', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_5', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_6', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_7', 'password': 'wpsthpvse1'},
    {'userName': 'OVF2_p001_user_8', 'password': 'wpsthpvse1'}
]

p005_credentials_list = [
    {"userName": "nat", "password": "networkadmin", "authLoginDomain": "16.125.76.222"},
    {"userName": 'adserver', 'password': 'Appliance@dmin123', 'authLoginDomain': 'AD_Server'}
]

sht_auth_aciton = {
    "category": "server-hardware-types",
    "action": "Read",
    "associatedResources": [
        {
            "initialScopeUris": None,
            "category": "ethernet-networks",
            "action": "Create, Use"
        }
    ]
}

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

AD_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQAhUzktepPZpKfIgDK6s1uTANBgkqhkiG9w0BAQUFADBJ\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xNDAzMjAxNzA1MjRaFw0yMjEx\nMTUxMDQ2NDVaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnQCjTZuDhuYXYsXyCVZZ0Q06PODw6B/ktN2\nGVyFqG2fkFFJJtj0UUrythnxQoUrYm8xWN3+KrqRBqFOVvx4VcYCLPhc7Q6kxLRB\n9FbjVbyYISkZXoRfwpBCFzHDSSKmSymXJQwmsZ/dzsBzRQ44q8cTc3JR6yqpbJIf\nhpPdeWYBUUjLbxm9o4rV0xzPlkYjMQ7MLmNZir7RRuE5GrW2/6MUYvgabN9qrsbZ\nxG/8TvMeG8AbuHv8jNFRdFv2SkUTmo0UjwRqciK2cBtlQGPoVVDy+7dMiP+VY0jm\neceB8IvLP6U2+hm9BreLlcgcSlLuV+AggvQ8hmXBheHM+BH2ewIDAQABo4GRMIGO\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBRIO04qEVeUVikGs4nLlXBT/1HohDASBgkrBgEEAYI3\nFQEEBQIDAQACMCMGCSsGAQQBgjcVAgQWBBRYZAuy3kMYBotknYU+mkYqd7MOXjAN\nBgkqhkiG9w0BAQUFAAOCAQEAJmm0b51lueHYnO3Nl8/7gn7V1a5PwECH8WkVaz/f\nRoIHxVFA5Rqt7feD9DEnr+ADtHbN2WVHAa7UEKZK5Lg/AeHY8fWweVVDexQoc048\nr2guJTc++DvWcBZ+ug0B4BvO439UWoKsxU6YhtREIA/qCbw9LFVnCudipKLuTnPh\nZzYv3mtfrntgXuKcTFPSgnZJnyQjzX4HBcLSNL3MqzeQ3xTSn075NDYse4iIkpFB\nSN/ePynjWQgB7ExDj2uBFlVq3I0AOMtC5E+O5Hogp+vWIsRU8h1SJUD/i0KEmkiw\nGLxBpwTRwg8C1Cw0uFilq5WcChhJiIqtWKMOA24sbUNiEQ==\n-----END CERTIFICATE-----\n"

AD_cred = {"userName": "james", "password": "cosmos@123"}

ALIAS_NAME = "AD_Server"

remove_user_headers = {
    'Content-Type': 'application/json',
    'Accept-Language': 'en_US',
    'Accept': 'appliacation/json, */*',
    'X-Api-Version': 500
}
sh_modify_body = {
    "name": "New Server Type Name",
    "description": "New Description"
}

directory = [
    {
        "type": "LoginDomainConfigV600",
        "name": "16.125.76.222",
        "credential": {"userName": "wpstuser", "password": "P@ssw0rd"},
        "authProtocol": "LDAP",
        "orgUnits": [
            "ou=Users",
            "ou=groups"
        ],
        "userNamingAttribute": "UID",
        "baseDN": "dc=ldapfc,dc=com",
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": "16.125.76.222",
                "directoryServerCertificateBase64Data": "-----BEGIN CERTIFICATE-----\nMIIECjCCAvKgAwIBAgIJAO9jxxrDwwEjMA0GCSqGSIb3DQEBCwUAMIGRMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\nMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEW\nMBQGCgmSJomT8ixkARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTAeFw0x\nODA1MjIxNjI0MjBaFw0yODAyMTkxNjI0MjBaMIGRMQswCQYDVQQGEwJVUzETMBEG\nA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9I\nZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEWMBQGCgmSJomT8ixk\nARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTCCASIwDQYJKoZIhvcNAQEB\nBQADggEPADCCAQoCggEBAO2qMOGXDpsyb25et7r4ya0R1d5DfB5wo6HipxtyRL2H\nkMfvhyHB7izNdxbdUmJW6Zf3FkDB/bTolEjMPgAwFdfMOTk5T5fbF+eUDsHnk3Zz\nBBzHQuQ+r6Z+K2Av9P7+pOkOUrkjt28pcFYeYZeYHQ1iUIFb9IVRut0bf+8XDlCU\nTgYK2KmzKyPISBas/3KgngjdY1F9zccW/wIBaHou77vM9ozOxdT6qjP+hmMx9WJY\nE7gzMQT8+9Gyh0XZzhrKqPFHHj12ztKHlknMDP9kv9esVPIUyD3viBVjdnmpEE+S\ny62wuVdGsJhJbyyM2peOTS/LoFW0bcg2Sbr9WWrjNkECAwEAAaNjMGEwHQYDVR0O\nBBYEFJgJWnvnI/CINkmuoBpQqYx5jPR5MB8GA1UdIwQYMBaAFJgJWnvnI/CINkmu\noBpQqYx5jPR5MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMA0GCSqG\nSIb3DQEBCwUAA4IBAQA4HfPrPCmW10uYSL7suwlKLfk+5nRqQU5U5emKi0YAXzuL\nIKg7cdjQIZin01Zu6VbXXW8Kx7gof8X98UFXC1fWe0o/z3H5Y/C67we/NkUkhwmz\nDZB6SA7HJcslMCPJGIgV2UEyDA/ZN1rmSh5UeX1fzBBgW1NzgTwH8J2IR9j+LRbo\n/ujN7sNMUP47XAyjIe8mTMwC7mXOhdYYl432EPunRSNMHdXn2i37lTPoT19fIhDy\nN5eDbQAqXtviOHDtHbd1kZM0+RxZY9BDrLu4NpzrSXIWXsk6HKASuUf3i+chXZZ0\neDd8PulIMpKtQslgoDJyGnClYn4RxOdMPjwu5Qvn\r\n-----END CERTIFICATE-----",
                "directoryServerSSLPortNumber": "636",
                "validUntil": "2027-11-23T08:00:22.000Z",
                "directoryServerCertificateStatus": "Yes",
                "serverStatus": "true",
                "category": "users"
            }
        ]
    },
    {
        "type": "LoginDomainConfigV600",
        "name": "AD_Server",
        "credential": AD_cred,
        "authProtocol": "AD",
        "orgUnits": [],
        "userNamingAttribute": "",
        "baseDN": "dc=wpstAD,dc=com",
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": "16.125.77.30",
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

p001_new_scope_with_resources = [
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope1WithLIGResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope2WithLIResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope3WithICMResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope4WithEthnetResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope5WithFCResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope6WithFCOEResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope7NSResources",
        "description": "Sample Scope description"
    },
    {
        "type": SCOPE_TYPE,
        "name": "OVF2Scope8SHResources",
        "description": "Sample Scope description"
    }
]

p001_new_user = [
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_1"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_2",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_2"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_3",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_3"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_4",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_4"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_5",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_5"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_6",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_6"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_7",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_7"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_8",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_8"
    }
]

p003_update_user = [
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "false",
        "fullName": "OVF2_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_1"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_2",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_2"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_3",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_3"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_4",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_4"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_5",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_5"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_6",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_6"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_7",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_7"
    },
    {
        "emailAddress": "admin@hpe.com",
        "enabled": "true",
        "fullName": "OVF2_p001_user_8",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "permissions": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
        "userName": "OVF2_p001_user_8"
    }
]

p009_edit_users_permission = [
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            }
        ]
    }
]

p005_new_group = [
    {
        "credentials": {"userName": "wpstuser", "password": "P@ssw0rd"},
        "group2PermissionPerGroup": {
            "egroup": "FUSION_NET_ADMIN",
            "loginDomain": "16.125.76.222",
            "permissions": [
                {
                    "roleName": "Scope administrator",
                    "scopeUri": None
                },
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                },
                {
                    "roleName": "Scope operator",
                    "scopeUri": None
                },
                {
                    "roleName": "Software administrator",
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
            "egroup": "AD_SVR_ADMIN",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Scope administrator",
                    "scopeUri": None
                },
                {
                    "roleName": "Backup administrator",
                    "scopeUri": None
                },
                {
                    "roleName": "Scope operator",
                    "scopeUri": None
                },
                {
                    "roleName": "Software administrator",
                    "scopeUri": None
                }

            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    }
]

p010_edit_groups_permission = [
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ]
    },
    {
        "sessionID": None,
        "permissionsToActivate": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            }
        ]
    }
]

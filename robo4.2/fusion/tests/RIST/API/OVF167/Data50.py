from dto import *

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

user_credentials_list = [
    {'userName': 'OVF167_p001_user_1', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_2', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_3', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_4', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_5', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_6', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_7', 'password': 'wpsthpvse1'}
]

p003_user_credentials_list = [
    {'userName': 'OVF167_p001_user_1', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_2', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_3', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_5', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_6', 'password': 'wpsthpvse1'},
    {'userName': 'OVF167_p001_user_7', 'password': 'wpsthpvse1'}
]

group_credentials_list = [
    {"userName": "jerry", "password": "cosmos@123", "authLoginDomain": "AD_Server"},
    {"userName": "james", "password": "cosmos@123", "authLoginDomain": "AD_Server"}
]

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

directory = [
    {
        "type": DOMAIN_TYPE,
        "name": "16.125.76.222",
        "credential": {"userName": "wpstuser", "password": "P@ssw0rd"},
        "authProtocol": "LDAP",
        "orgUnits": [
            "OU=Users", "OU=groups"
        ],
        "userNamingAttribute": "CN",
        "baseDN": "dc=ldapfc,dc=com",
        "authnType": "CREDENTIAL",
        "directoryBindingType": "USER_ACCOUNT",
        "directoryServers": [
            {
                "type": "LoginDomainDirectoryServerInfoDto",
                "directoryServerIpAddress": "16.125.76.222",
                "directoryServerCertificateBase64Data": "-----BEGIN CERTIFICATE-----\nMIIECjCCAvKgAwIBAgIJAO9jxxrDwwEjMA0GCSqGSIb3DQEBCwUAMIGRMQswCQYD\r\nVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRv\r\nMRgwFgYDVQQKDA9IZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEW\r\nMBQGCgmSJomT8ixkARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTAeFw0x\r\nODA1MjIxNjI0MjBaFw0yODAyMTkxNjI0MjBaMIGRMQswCQYDVQQGEwJVUzETMBEG\r\nA1UECAwKQ2FsaWZvcm5pYTESMBAGA1UEBwwJUGFsbyBBbHRvMRgwFgYDVQQKDA9I\r\nZXdsZXR0LVBhY2thcmQxEjAQBgNVBAMMCUxEQVBGQy1DQTEWMBQGCgmSJomT8ixk\r\nARkWBmxkYXBmYzETMBEGCgmSJomT8ixkARkWA2NvbTCCASIwDQYJKoZIhvcNAQEB\r\nBQADggEPADCCAQoCggEBAO2qMOGXDpsyb25et7r4ya0R1d5DfB5wo6HipxtyRL2H\r\nkMfvhyHB7izNdxbdUmJW6Zf3FkDB/bTolEjMPgAwFdfMOTk5T5fbF+eUDsHnk3Zz\r\nBBzHQuQ+r6Z+K2Av9P7+pOkOUrkjt28pcFYeYZeYHQ1iUIFb9IVRut0bf+8XDlCU\r\nTgYK2KmzKyPISBas/3KgngjdY1F9zccW/wIBaHou77vM9ozOxdT6qjP+hmMx9WJY\r\nE7gzMQT8+9Gyh0XZzhrKqPFHHj12ztKHlknMDP9kv9esVPIUyD3viBVjdnmpEE+S\r\ny62wuVdGsJhJbyyM2peOTS/LoFW0bcg2Sbr9WWrjNkECAwEAAaNjMGEwHQYDVR0O\r\nBBYEFJgJWnvnI/CINkmuoBpQqYx5jPR5MB8GA1UdIwQYMBaAFJgJWnvnI/CINkmu\r\noBpQqYx5jPR5MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMA0GCSqG\r\nSIb3DQEBCwUAA4IBAQA4HfPrPCmW10uYSL7suwlKLfk+5nRqQU5U5emKi0YAXzuL\r\nIKg7cdjQIZin01Zu6VbXXW8Kx7gof8X98UFXC1fWe0o/z3H5Y/C67we/NkUkhwmz\r\nDZB6SA7HJcslMCPJGIgV2UEyDA/ZN1rmSh5UeX1fzBBgW1NzgTwH8J2IR9j+LRbo\r\n/ujN7sNMUP47XAyjIe8mTMwC7mXOhdYYl432EPunRSNMHdXn2i37lTPoT19fIhDy\r\nN5eDbQAqXtviOHDtHbd1kZM0+RxZY9BDrLu4NpzrSXIWXsk6HKASuUf3i+chXZZ0\r\neDd8PulIMpKtQslgoDJyGnClYn4RxOdMPjwu5Qvn\r\n-----END CERTIFICATE-----",
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
                "directoryServerCertificateStatus": "Yes",
                "serverStatus": "true",
                "category": "users"
            }
        ]
    }
]

p001_new_users_with_so_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope operator",
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
                "roleName": "Scope operator",
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
                "roleName": "Scope operator",
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
                "roleName": "Scope operator",
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
                "roleName": "Scope operator",
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
                "roleName": "Scope operator",
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
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "OVF167_p001_user_7"
    }
]

p001_new_group_with_so_role = [
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

p002_new_users_wo_so_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Read only",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Server administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_7"
    }
]

p002_assign_users_so_role = [
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Read only",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Backup administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Server administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Storage administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Server firmware operator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Software administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope operator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Backup administrator",
            "type": "RoleNameDtoV2"
        }
    ]
]


p002_new_group_wo_so_role = [
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
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    }
]


p002_assign_group_with_so_role = [
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

p003_new_users_with_sa_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_7"
    }
]

p003_new_group_with_sa_role = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Scope administrator",
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
                    "roleName": "Scope administrator",
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

p004_new_users_wo_sa_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Read only",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Server administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_7"
    }
]

p004_assign_users_sa_role = [
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Read only",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Backup administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Server administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Storage administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Server firmware operator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Software administrator",
            "type": "RoleNameDtoV2"
        }
    ],
    [
        {
            "roleName": "Scope administrator",
            "type": "RoleNameDtoV2"
        },
        {
            "roleName": "Backup administrator",
            "type": "RoleNameDtoV2"
        }
    ]
]


p004_new_group_wo_sa_role = [
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
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    }
]


p004_assign_group_with_sa_role = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Scope administrator",
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
                    "roleName": "Scope administrator",
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

p005_scopes = [
    {
        "type": "ScopeV3",
        "name": "OVF167Scope1",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope2",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope3",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope4",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope5",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope6",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope7",
        "description": "Sample Scope description"
    }
]


n003_sa_role_only_user = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope administrator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_3"
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope administrator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_7"
    }
]


n003_sa_role_only_group = [
    {
        "credentials": {"userName": "jerry", "password": "cosmos@123"},
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": "AD_Server",
            "permissions": [
                {
                    "roleName": "Scope administrator",
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
                    "roleName": "Scope administrator",
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


n004_so_role_only_user = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Scope operator",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_3"
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
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Scope operator",
                "scopeUri": None
            },
            {
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_7"
    }
]


n004_so_role_only_group = [
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


p007_edit_body = [
    {
        "type": "ScopeV3",
        "name": "OVF167Scope1",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope2",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope3",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope4",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope5",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope6",
        "description": "Sample Scope description"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope7",
        "description": "Sample Scope description"
    }
]


p011_update_body = [
    {
        "type": "ScopeV3",
        "name": "OVF167Scope1new+",
        "description": "Sample Scope description New1"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope2new+",
        "description": "Sample Scope description New2"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope3new+",
        "description": "Sample Scope description New3"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope4new+",
        "description": "Sample Scope description New4"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope5new+",
        "description": "Sample Scope description New5"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope6new+",
        "description": "Sample Scope description New6"
    },
    {
        "type": "ScopeV3",
        "name": "OVF167Scope7new+",
        "description": "Sample Scope description New7"
    }
]

n009_NonIA_users_wo_scope_role = [
    {
        "emailAddress": "jianl@hpe.com",
        "enabled": "true",
        "fullName": "OVF167_p001_user_1",
        "mobilePhone": "555-2121",
        "officePhone": "555-1212",
        "password": "wpsthpvse1",
        "permissions": [
            {
                "roleName": "Read only",
                "scopeUri": None
            }
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Backup administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Network administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Server administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Storage administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Server firmware operator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
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
                "roleName": "Software administrator",
                "scopeUri": None
            },
        ],
        "type": "UserAndPermissions",
        "userName": "OVF167_p001_user_7"
    }
]

n009_new_group_wo_scope_role = [
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
                    "roleName": "Backup administrator",
                    "scopeUri": None
                }
            ],
            "type": "LoginDomainGroupPermission"
        },
        "type": "LoginDomainGroupCredentials"
    }
]

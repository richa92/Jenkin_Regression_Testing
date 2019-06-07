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

# Add a Group 'GroupJ' to users and Group
p005_credentials_list = [
    {"userName": "jerry", "password": "cosmos@123", "authLoginDomain": "AD_Server"},
    {"userName": 'james', 'password': 'cosmos@123', 'authLoginDomain': 'AD_Server'}
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

AD_CERTIFICATE = "-----BEGIN CERTIFICATE-----\nMIIDrjCCApagAwIBAgIQPMm63L7kEbJKQ0QpKb/udzANBgkqhkiG9w0BAQUFADBJ\nMRMwEQYKCZImiZPyLGQBGRYDY29tMRYwFAYKCZImiZPyLGQBGRYGd3BzdEFEMRow\nGAYDVQQDExF3cHN0QUQtV1BTVC1BRC1DQTAeFw0xODA1MjUwOTI5NTRaFw0yMzA1\nMjUwOTM5NTNaMEkxEzARBgoJkiaJk/IsZAEZFgNjb20xFjAUBgoJkiaJk/IsZAEZ\nFgZ3cHN0QUQxGjAYBgNVBAMTEXdwc3RBRC1XUFNULUFELUNBMIIBIjANBgkqhkiG\n9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsi5cFUBbB7yIqshTXWG98bb195qg3qNnvZ\nT6HDldEPryc0Tt5UXbMsI1swvQzDcbgOIGS51/fJlS68Dguu5cV03207grkpFfRl\n8AAyrxeftWW+4x8Hy2sp4WFsEOM3hwKBIYOUhBrzyUZUv3u/nj8bMPJ52UEyvqiT\n/XqgEFlCTdFX3vGMRVowN9jARFfA9AMACby8kGHkt+lsBbC0QEuMWiBd55mqlf3o\nlvbb+EWh1nd+mVfu4ghuVr4ztY1SjyXcs6Ji71LGjidhI2js/Kc/Mu8zqlitf1q2\nPrUobXXAln3Yq99tWLaAx+WgAZ3ZBJYwHHzR3HqPHe52lqun4wIDAQABo4GRMIGO\nMBMGCSsGAQQBgjcUAgQGHgQAQwBBMA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBSl4IMWKKfP1EKAPFWvgFReUVq2ozASBgkrBgEEAYI3\nFQEEBQIDAwADMCMGCSsGAQQBgjcVAgQWBBR/wd/nomlY2SxW+cy7T5VoLZMT/zAN\nBgkqhkiG9w0BAQUFAAOCAQEAmLl8cFATJyUZ979i3ZhMcj1WV1QhlP3eU3bsKgkW\nD/n9Q2SbgWSbKw08m8F9KetBEmZdvAmfojcOPAww/xQrxc9gLCfpUhnaUDe4fpcV\nuAnU+S3osPj3CL5W9pIkeaXol/Dnj9BmNbD5OxvxtZbEF8E353ikcytMTKggIT4S\n3Bst+ayI3m1gI4KA9ZKjR4USxZ5TM7E/kJJZNtK0aVniWc7o2WhECw2dUe2ZzufQ\nR+DfY56kTewvTiVAA2w5/+85Ywf/8V1yy4E6Di6h63FN/LUXX2lZKnMftekjjuWz\nzH1KNRrV8HG2hvN8FqkVTAcnWEWyjr7omTLi+0bDhI1BVw==\n-----END CERTIFICATE-----\n"

AD_cred = {"userName": "Administrator", "password": "Wpsthpvse1234"}

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
    #     {
    #         "type": "LoginDomainConfigV600",
    #         "name": "16.114.210.116",
    #         "credential": {"userName": "sarah", "password": "serveradmin"},
    #         "authProtocol": "LDAP",
    #         "orgUnits": [
    #             "ou=people"
    #         ],
    #         "userNamingAttribute": "UID",
    #         "baseDN": "dc=shqa,dc=hpe",
    #         "directoryServers": [
    #             {
    #                 "type": "LoginDomainDirectoryServerInfoDto",
    #                 "directoryServerIpAddress": "16.114.210.116",
    #                 "directoryServerCertificateBase64Data": "-----BEGIN CERTIFICATE-----\nMIIFtjCCA56gAwIBAgIJAOHCbbO735g9MA0GCSqGSIb3DQEBDAUAMHMxCzAJBgNV\r\nBAYTAkNOMREwDwYDVQQIDAhTaGFuZ2hhaTERMA8GA1UEBwwIU2hhbmdoYWkxEjAQ\r\nBgNVBAoMCUhQRSBQb2ludDESMBAGA1UECwwJVGVzdC1TSFFBMRYwFAYDVQQDDA0x\r\nNS4xMTQuMTE0LjE3MB4XDTE3MTEyMzA2MTIwM1oXDTI3MTEyMTA2MTIwM1owczEL\r\nMAkGA1UEBhMCQ04xETAPBgNVBAgMCFNoYW5naGFpMREwDwYDVQQHDAhTaGFuZ2hh\r\naTESMBAGA1UECgwJSFBFIFBvaW50MRIwEAYDVQQLDAlUZXN0LVNIUUExFjAUBgNV\r\nBAMMDTE1LjExNC4xMTQuMTcwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoIC\r\nAQC6e1pvUjdFkDg984pFLTW7cq1SBkfPlHlCQbj76QqW5DsZqoQXCtDYJe+QebJI\r\noGquYhAzqNPRXa8DvIJxWXoydWL3dtcR+7srTSTG1sWSCw4bA1AellqZp9wrZIKT\r\nUDc+wdSLOdjOkgtHKAbEmu5+jG+b558w/leuxpRdUKBbUk25rzaZITiicmYpJeMO\r\nk3+4AjMyaTC58uppaMFTIaeJmvgCgofGGs9y4YCRm/ioTIK9429nJumqsur8OXYH\r\nZFBUAhSfq+q8vxwP8UPepuaUoxHFVp3a4zB8YNosL5YfbAbH0zRoMsDE8F/7gulL\r\nasA/G0eKWyUUQhTKdpuTZL+kaIShEbO9pJhvZXQPNITY9pMEzZ86RTE35JcQCvCO\r\n0yIOsEoE3IU5aOwJV8kyB1s+Zmv60wIzMapLogGO/LoOqwOoz4jdBMy1thXHXPte\r\nXunS45hftrgnzzeDvLmezlyoU6oZnfE4ziswZC5qzMoIduLJXcXh1vH9kmpqNvFC\r\nnPj3PiqUhb3fOl1SG2lEzXdaY8QZjGc/STNgIlJ0arBTUmSIVQEDXa6mU3ZdsWqG\r\nmvdJS1X9vhOQXCvnD1/SU1WWRBt5TJbUAuxv7ttIAsnStADZWQID+/dS7Tn59j7J\r\nQA3onD/P4dC1Nsmx0UqnLWVFoLvPYZSNRYbjk6nHns8G7wIDAQABo00wSzAdBgNV\r\nHQ4EFgQUAu2giLguC+m9b8goJjszmzMOyvgwHwYDVR0jBBgwFoAUAu2giLguC+m9\r\nb8goJjszmzMOyvgwCQYDVR0TBAIwADANBgkqhkiG9w0BAQwFAAOCAgEAacUuClr/\r\ntSTE789a0eEJw2KNrGBJhwuvXe8GP+RkSwOEJhyjIwKu73ATokKhCmdW+kq6CnqL\r\nZrUgaMfN9wXuTx5N0Rm8dcQjbfHe2KHLcStDq5SUrfT6G+d08x+rOkYqwuvz6l0o\r\nq/aUmJu5LCWJwaDLLGfAmF55S56nPeKn9KoXYcJBNBvWewZHYsJF72hggkeU3jHx\r\nsmpvzx9frTF4/JlTYlYkAyngc0/SP5Qx43QBAfSUSQRksSo+CjiFk/EebEnwXhfq\r\nS8wFyqIuwdrRaqJflhjdj2SVFPSfnTZkiAA77CkngKoGfptmMl/f1nl184a0m0Iv\r\nr5sMF9Efa5DsidUCJA9K3LxMFN8/xpTBz4qnrkIWuqe1YU9qH8HIWpI9y6zwXqDi\r\n/OqUPERiMfr5rhS0kbPOjH6Wvl6+rkOSO6xc2x1gNkJWA5moLdkwSwbSscvQzjDD\r\nE1qo6mCZZHEnjlLeeKduXQ3eYobGJTk7IJrS7rsXgCnGXEOmJD7sTv15a3El04wD\r\n/wHsqvtSBMRtq3z9ipttVvXn/DMyY/QSxTijbS8igfDqlj0ArYJG6lrUI6skUCfC\r\nEl0fV26jsXGVB/q1M4DK/C5U9yXODx1DXFP7rGhvYQdN/fctU4k5kOGYUNnhDzMY\r\nBUB09813ey8a1YhQRXEJQpeOHx7VALGMA38=\r\n-----END CERTIFICATE-----",
    #                 "directoryServerSSLPortNumber": "636",
    #                 "validUntil": "2027-11-23T08:00:22.000Z",
    #                 "directoryServerCertificateStatus": "Yes",
    #                 "serverStatus": "true",
    #                 "category": "users"
    #             }
    #         ]
    #     },
    {
        "type": "LoginDomainConfigV600",
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
        "credentials": AD_cred,
        "group2PermissionPerGroup": {
            "egroup": "server_group",
            "loginDomain": 'AD_Server',
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
            "egroup": "Domain_Admins",
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
    },
    {
        "credentials": AD_cred,
        "group2PermissionPerGroup": {
            "egroup": "GroupJ",
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

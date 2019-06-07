admin_credentials = {'userName': 'administrator', 'password': 'wpsthpvse1'}

users = [
    {'userName': 'backup', 'password': 'backupadmin', 'roles': ['Backup administrator'], 'emailAddress':'backup@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndPermissions'},
    {'userName': 'network', 'password': 'networkadmin', 'roles': ['Network administrator'], 'emailAddress':'network@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'readonly', 'password': 'readonly', 'roles': ['Read only'], 'emailAddress':'readonly@hp.com', 'officePhone':'970-666-1919', 'mobilePhone':'970-600-1919', 'type': 'UserAndPermissions'},
    {'userName': 'server', 'password': 'serveradmin', 'roles': ['Server administrator'], 'emailAddress':'server@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'software', 'password': 'softwareadmin', 'roles': ['Software administrator'], 'emailAddress':'software@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
    {'userName': 'storage', 'password': 'storageadmin', 'roles': ['Storage administrator'], 'emailAddress':'storage@hp.com', 'officePhone':'970-555-0001', 'mobilePhone':'970-500-0001', 'type': 'UserAndPermissions'},
]

sas_lig = {
    'name': 'SAS LIG',
    "type": "sas-logical-interconnect-group",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": "1",
    'interconnectMapTemplate': [
        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'},
    ],
}

edited_sas_lig = {
    'name': 'SAS LIG',
    "type": "sas-logical-interconnect-group",
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": "1",
    'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'},
                                ],
}

sas_eg = {
    "name": "SAS EG",
            "type": "EnclosureGroupV400",
            "stackingMode": "Enclosure",
            "ipAddressingMode": "External",
            "enclosureCount": 3,
            "interconnectBayMappings": [
                {
                    "enclosureIndex": 1,
                    "interconnectBay": 1,
                    "logicalInterconnectGroupUri": "SASLIG:SAS LIG"
                },
                {
                    "enclosureIndex": 1,
                    "interconnectBay": 4,
                    "logicalInterconnectGroupUri": "SASLIG:SAS LIG"
                }
            ],
}

sas_le = {
    "name": "SAS LE",
    "enclosureGroupUri": "EG:SAS EG",
    "enclosureUris": [
        "ENC:CN754406XL",
        "ENC:CN754404R6",
        "ENC:CN754406WB",
    ],
    "forceInstallFirmware": False
}

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator',
                   'password': 'hpvse123'
                   }

EG_NAME = 'EG1'

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

BOOT_URL1 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/Core-current.iso"
BOOT_URL2 = "https://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/nanolinux64-1.3.iso"
BOOT_URL3 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/Porteus-v3.1-x86_64.iso"
BOOT_URL4 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/TinyCore-current.iso"
BOOT_URL5 = "https://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/CorePlus-current.iso"
BOOT_URL6 = "http://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/nanolinux64-1.3.iso"
BOOT_URL7 = "https://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/Porteus-v3.1-x86_64.iso"
BOOT_URL8 = "http://[2002:107d:4024::107d:4024]/software_distributions/miniLinux/Core-current.iso"

BAD_URL1 = "http://192.168/software_distributions/miniLinux/Core-current.iso"
BAD_URL2 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/"
BAD_URL3 = "http://wpstwork4.vse.rdlabs.hpecorp.net/software_distributions/miniLinux/Core-current.exe"
BAD_URL4 = "https://[2002::107d:4024::O000:107d:4024]/software_distributions/miniLinux/Porteus-v3.1-x86_64.iso"

# PROFILE1 SETTINGS
PROFILE1_NAME = 'Gen10_multiple_boot_url_test_profile1'
PROFILE1_SHT = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'
PROFILE1_SH = ENC2SHBAY7

# PROFILE2 SETTINGS
PROFILE2_NAME = 'Gen10_multiple_boot_url_test_profile2'
PROFILE2_SHT = 'SY 480 Gen10:3:Synergy 3820C 10/20Gb CNA'
PROFILE2_SH = ENC2SHBAY8


# 4 Bootable URLs
four_bootable_urls = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 4 Bootable URLs (edit to different URLs)
four_bootable_urls_edit = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL5
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL6
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL7
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL8
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 3 Bootable URLs
three_bootable_urls = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 2 Bootable URLs
two_bootable_urls = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 1 Bootable URL
only_first_bootable_url = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 2nd Bootable URL
only_second_bootable_url = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 3rd Bootable URL
only_third_bootable_url = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 4th Bootable URL
only_fourth_bootable_url = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE2_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL1
bad_url1 = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BAD_URL1
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL2
bad_url2 = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_2",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BAD_URL2
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL3
bad_url3 = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_3",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BAD_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL4
bad_url4 = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_4",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BAD_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}


# RIS Data

# RIS validation for Four Bootable URLs
ris_four_bootable_urls = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": BOOT_URL3,
            "UrlBootFile4": BOOT_URL4,
        }
    }
}

# RIS validation for Four Bootable URLs after edit
ris_four_bootable_urls_edit = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL5,
            "UrlBootFile2": BOOT_URL6,
            "UrlBootFile3": BOOT_URL7,
            "UrlBootFile4": BOOT_URL8,
        }
    }
}

# RIS validation for three Bootable URLs
ris_three_bootable_urls = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": BOOT_URL3,
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for two Bootable URLs
ris_two_bootable_urls = {
    "server": PROFILE1_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": "",
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for one Bootable URL
ris_only_first_bootable_url = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": BOOT_URL1,
            "UrlBootFile2": "",
            "UrlBootFile3": "",
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for only second Bootable URL
ris_only_second_bootable_url = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": "",
            "UrlBootFile2": BOOT_URL2,
            "UrlBootFile3": "",
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for only third Bootable URL
ris_only_thrid_bootable_url = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": "",
            "UrlBootFile2": "",
            "UrlBootFile3": BOOT_URL3,
            "UrlBootFile4": "",
        },
    }
}

# RIS validation for only fourth Bootable URL
ris_only_fourth_bootable_url = {
    "server": PROFILE2_SH,
    "username": ilo_credentials['username'],
    "password": ilo_credentials['password'],
    "path": "/redfish/v1/Systems/1/bios/settings/",
    "validate": {
        "Attributes": {
            "UrlBootFile": "",
            "UrlBootFile2": "",
            "UrlBootFile3": "",
            "UrlBootFile4": BOOT_URL4,
        },
    }
}

# 4 Bootable URLs template
four_bootable_urls_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 4 Bootable URLs from Template
four_bootable_urls_from_spt = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 4 Bootable URLs (edit to different URLs) template
four_bootable_urls_edit_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL5
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL6
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL7
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL8
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 4 Bootable URLs from Template
four_bootable_urls_from_spt_edit = {
    "type": "ServerProfileV10",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareUri': 'SH:' + PROFILE1_SH,
    'serverProfileTemplateUri': 'SPT:' + PROFILE1_NAME,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL4
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL3
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL1
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": []
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 3 Bootable URLs template
three_bootable_urls_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 2 Bootable URLs template
two_bootable_urls_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL1
            },
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# 1 Bootable URL template
only_first_bootable_url_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BOOT_URL6
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 2nd Bootable URL template
only_second_bootable_url_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BOOT_URL2
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 3rd Bootable URL template
only_third_bootable_url_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Only 4th Bootable URL template
only_fourth_bootable_url_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE2_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BOOT_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Template non-compliance test
# Only 3rd Bootable URL template
template_non_compliance_edit = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": PROFILE1_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BOOT_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL1 template
bad_url1_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile",
                "value": BAD_URL1
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL2 template
bad_url2_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_2",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile2",
                "value": BAD_URL2
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL3 template
bad_url3_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_3",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile3",
                "value": BAD_URL3
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Bad URL4 template
bad_url4_template = {
    "type": "ServerProfileTemplateV6",
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "name": "bad_url_test_4",
    "affinity": "Bay",
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "UrlBootFile4",
                "value": BAD_URL4
            },
        ]
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": False,
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

sp_compliant_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_non_compliant1_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            'REGEX:Change BIOS setting \"Boot from URL 1\" to \"' + BOOT_URL1 + '\".',
            'REGEX:Change BIOS setting \"Boot from URL 2\" to \"' + BOOT_URL2 + '\".',
            'REGEX:Change BIOS setting \"Boot from URL 3\" to \"' + BOOT_URL3 + '\".',
            'REGEX:Change BIOS setting \"Boot from URL 4\" to \"' + BOOT_URL4 + '\".',
        ],
        "manualUpdates": []
    }
}

sp_non_compliant2_profile1 = {
    "name": PROFILE1_NAME,
    "compliance-preview": {
        "type": "ServerProfileCompliancePreviewV1",
        "automaticUpdates": [
            'REGEX:Change BIOS setting \"Boot from URL 1\" to the default value \"\".',
            'REGEX:Change BIOS setting \"Boot from URL 2\" to the default value \"\".',
            'REGEX:Change BIOS setting \"Boot from URL 4\" to the default value \"\".',
        ],
        "manualUpdates": []
    }
}

ts1_create_profiles = [
    four_bootable_urls.copy(),
    only_fourth_bootable_url.copy(),
]

ts1_edit_profiles1 = [
    four_bootable_urls_edit.copy(),
    only_third_bootable_url.copy(),
]

ts1_edit_profiles2 = [
    three_bootable_urls.copy(),
    only_second_bootable_url.copy(),
]

ts1_edit_profiles3 = [
    two_bootable_urls.copy(),
    only_first_bootable_url.copy(),
]

ts1_ris_after_create = [
    ris_four_bootable_urls.copy(),
    ris_only_fourth_bootable_url.copy(),
]

ts1_ris_after_edit1 = [
    ris_four_bootable_urls_edit.copy(),
    ris_only_thrid_bootable_url.copy(),
]

ts1_ris_after_edit2 = [
    ris_three_bootable_urls.copy(),
    ris_only_second_bootable_url.copy(),
]

ts1_ris_after_edit3 = [
    ris_two_bootable_urls.copy(),
    ris_only_first_bootable_url.copy(),
]

negative_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url1.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url2.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url2.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile',
        'argument': bad_url2.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_PROFILE_BOOT_URL'},
]


ts2_create_profiles_template = [
    four_bootable_urls_template.copy(),
    only_fourth_bootable_url_template.copy(),
]

ts2_edit_profiles1_template = [
    four_bootable_urls_edit_template.copy(),
    only_third_bootable_url_template.copy(),
]

ts2_edit_profiles2_template = [
    three_bootable_urls_template.copy(),
    only_second_bootable_url_template.copy(),
]

ts2_edit_profiles3_template = [
    two_bootable_urls_template.copy(),
    only_first_bootable_url_template.copy(),
]

create_sp_from_spt = [
    four_bootable_urls_from_spt.copy(),
]

edit_sp_non_compliant = [
    four_bootable_urls_from_spt_edit.copy(),
]

edit_spt_non_compliant = [
    template_non_compliance_edit.copy(),
]

sp_compliance = [
    sp_compliant_profile1.copy(),
]

sp_non_compliant1 = [
    sp_non_compliant1_profile1.copy(),
]

sp_non_compliant2 = [
    sp_non_compliant2_profile1.copy(),
]

negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url1_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url2_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url2_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': bad_url2_template.copy(),
        'taskState': 'Error',
        'errorMessage': 'INVALID_TEMPLATE_BOOT_URL'},
]

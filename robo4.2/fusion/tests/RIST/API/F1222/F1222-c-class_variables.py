admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
server_credentials = {'userName': 'Serveradmin', 'password': 'wpsthpvse1'}
network_credentials = {'userName': 'Networkadmin', 'password': 'wpsthpvse1'}
storage_credentials = {'userName': 'storageadmin', 'password': 'wpsthpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]

profile_templates = [
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-blade server',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 3',
        'enclosureGroupUri': 'EG:wpst-11-eg1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': 'change-sht-blade server',
        'description': 'change-sht-blade server',
        'affinity': 'Bay',
        'connections': [{
                             'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Flb 1:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:deployment',
            'requestedVFs': 'Auto'
        }
        ],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "HardDisk",
                "USB",
                "CD",
                "PXE"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-blade server to dl server - Virtual Addresses',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 2',
        'enclosureGroupUri': 'EG:wpst-11-eg1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': 'change-sht-blade server to dl server-Virtual',
        'description': 'change-sht-blade server to dl server',
        'affinity': 'Bay',
        'connections': [{
                             'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Flb 1:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:deployment',
            'requestedVFs': 'Auto'
        }
        ],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "67",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-blade server to dl server-Physical Addresses',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 2',
        'enclosureGroupUri': 'EG:wpst-11-eg1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-blade server to dl server-Physical',
        'description': 'change-sht-blade server to dl server',
        'affinity': 'Bay',
        'connections': [{
                             'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Flb 1:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:deployment',
            'requestedVFs': 'Auto'
        }
        ],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "67",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-blade server to dl server-Physical Addresses',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 2',
        'enclosureGroupUri': 'EG:wpst-11-eg1',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-blade server to dl server-Physical2',
        'description': 'change-sht-blade server to dl server',
        'affinity': 'Bay',
        'connections': [{
                             'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Flb 1:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:deployment',
            'requestedVFs': 'Auto'
        }
        ],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "67",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},

    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-and eg',
        'serverHardwareTypeUri': 'SHT:BL660c Gen9 1',
        'enclosureGroupUri': "EG:wpst-11-eg2",
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-and eg',
        'description': 'change-sht-and eg',
        'affinity': 'Bay',
        'connections': [],
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "UsbControl",
                    "value": "UsbEnabled"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change eg',
        'serverHardwareTypeUri': 'SHT:BL660c Gen9 1',
        'enclosureGroupUri': "EG:wpst-11-eg2",
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change eg',
        'description': 'change eg',
        'affinity': 'Bay',
        'connections': [],
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "UsbControl",
                    "value": "UsbEnabled"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},
]


edit_sht_templates = [{
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server',
    'serverHardwareTypeUri': 'SHT:BL660c Gen9 1',
    'enclosureGroupUri': 'EG:wpst-11-eg1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'change-sht-blade server',
    'description': 'change-sht-blade server',
    'affinity': 'Bay',
    'connections': [{
        'id': 1,
        'name': '',
        'functionType': 'Ethernet',
        'portId': 'Flb 1:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:deployment',
        'requestedVFs': 'Auto'
    }
    ],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    }}]

edit_sht_rack_and_blade_templates = [

    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-dl server to bl server',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
        'enclosureGroupUri': 'EG:wpst-11-eg1',
        'affinity': 'Bay',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-blade server to dl server-Physical',
        'description': 'change-sht-dl server to bl server',
        'connections': [],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }}]

edit_eg_templates = [
    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change eg',
        'serverHardwareTypeUri': 'SHT:BL660c Gen9 1',
        'enclosureGroupUri': "EG:wpst-11-eg1",
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change eg',
        'description': 'change eg',
        'affinity': 'Bay',
        'connections': [],
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "UsbControl",
                    "value": "UsbEnabled"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }},

    {
        'type': 'ServerProfileTemplateV2',
        'serverProfileDescription': 'change-sht-and eg',
        'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
        'enclosureGroupUri': "EG:wpst-11-eg1",
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change-sht-and eg',
        'description': 'change-sht-and eg',
        'affinity': 'Bay',
        'connections': [],
        "boot": {
            "manageBoot": True,
            "order": [
                "Floppy",
                "PXE",
                "USB",
                "HardDisk",
                "CD"
            ]
        },

        "bios": {
            "manageBios": True,
            "overriddenSettings": [
                {
                    "id": "64",
                    "value": "1"
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }}
]

auth_test_edit_eg_templates = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
    'enclosureGroupUri': "EG:wpst-11-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

transformation_eg_templates = [{
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 2',
    'enclosureGroupUri': "EG:wpst-11-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },
    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "1"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}]


transformation_edit_eg_templates = [{
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 2',
    'enclosureGroupUri': "EG:wpst-11-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}]

invalid_eg_edit_template = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
    'enclosureGroupUri': "/rest/enclosure-groups/5f275fb2-f74c-4992-a761-54ee58391111",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

invalid_sht_edit_template = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': "/rest/server-hardware-types/5f275fb2-f74c-4992-a761-54ee58391111",
    'enclosureGroupUri': "EG:wpst-11-eg2",
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

invalid_addresses_change_edit_template = {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-and eg',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9 1',
    'enclosureGroupUri': "EG:wpst-11-eg2",
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'change-sht-and eg',
    'description': 'change-sht-and eg',
    'affinity': 'Bay',
    'connections': [],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },

    "bios": {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "64",
                "value": "5"
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

negative_unauth_edit_template = [
    {'keyword': 'Edit Server Profile Template',
     'argument': auth_test_edit_eg_templates.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'AUTHORIZATION'}]

negative_tests_eg_sht_addresses = [

    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_eg_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'INVALID_ENCLOSURE_GROUP'},

    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_sht_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'UNKNOWN_SERVER_TYPE'},
    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_addresses_change_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'FINAL_ATTRIBUTE_CHANGED'}

]


verify_edit_profile_templates = [{'type': 'ServerProfileTemplateV2',
                                  'serverProfileDescription': 'change SHT-rack server',
                                  'serverHardwareTypeUri': 'SHT:DL380p Gen8 1',
                                  'serialNumberType': 'Physical',
                                  'macType': 'Physical',
                                  'wwnType': 'Physical',
                                  'name': 'change_sht-DL',
                                  'description': 'change SHT-rack server',
                                  'connections': [],
                                  "boot": {
                                      "manageBoot": True,
                                      "order": [
                                          "Floppy",
                                          "PXE",
                                          "USB",
                                          "HardDisk",
                                          "CD"
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
                                      "manageSanStorage": False,
                                      "volumeAttachments": []
                                  }}, {
    'type': 'ServerProfileTemplateV2',
    'serverProfileDescription': 'change-sht-blade server',
    'serverHardwareTypeUri': 'SHT:BL465c Gen8 1',
    'enclosureGroupUri': 'EG:mixed-eg1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'change-sht-blade server',
    'description': 'change-sht-blade server',
    'affinity': 'Bay',
    'connections': [{
        'id': 1,
        'name': '',
        'functionType': 'Ethernet',
        'portId': 'Flb 1:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:deployment',
        'requestedVFs': 'Auto'
    }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "Floppy",
            "PXE",
            "USB",
            "HardDisk",
            "CD"
        ]},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}]

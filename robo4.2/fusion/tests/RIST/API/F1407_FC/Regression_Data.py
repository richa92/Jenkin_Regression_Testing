admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Enclosures
ENC2 = 'CN75120D7B'
ENC1 = 'CN75120D77'


# Server Hardware
SH2 = '%s, bay 7' % ENC2
SH1 = '%s, bay 5' % ENC1


# Server Hardware Model
SHM2 = 'SY 480 Gen9 2'
SHM1 = 'SY 660 Gen9 2'


# Enclosure Group
EG1 = 'EG_SYNERGY'

# Network FC
FC1 = 'FA1'
FC2 = 'FA2'

# SAN Volume
VOL1 = '{}-FA-Vol1-Thin-20GB-R5-Private'.format(ENC2.upper())
VOL2 = '{}-FA-Vol2-Full-20GB-R5-Private'.format(ENC2.upper())
VOL3 = '{}-FA-Vol3-Thin-30GB-R5-Shared'.format(ENC2.upper())

vol_orig_size = '21474836480'

vol_modify_size = '42949672960'

# Create SP with one primary connection, with private volume as boot volume
createProfileP01P02P34P35P36 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileN03 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_N03",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": None,
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createsProfileP04P05P07P13P14 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileN06 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_N06",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None
    }
]

createProfileN08 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_N08",
        "connections": [
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]

createProfileN09 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_N09",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL2),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileN10 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP11P12P61 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P11P12P61",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP37 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "affinity": "Bay",
        "serialNumberType" : "Virtual",
        "hideUnusedFlexNics": True,
        "name": "F1407_API_SP_P37",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "macType": "Physical",
                "wwnType": "Physical",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP38 = [
    {
        "type": "ServerProfileV7",
        "affinity": "Bay",
        "serialNumberType" : "Virtual",
        "hideUnusedFlexNics": True,
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP39 = [
    {
        "type": "ServerProfileV7",
        "affinity" : "Bay",
        "serialNumberType" : "Virtual",
        "hideUnusedFlexNics" : True,
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP40 = [
    {
        "type": "ServerProfileV7",
        "affinity" : "Bay",
        "serialNumberType" : "Virtual",
        "hideUnusedFlexNics" : True,
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P40",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "22210002AC01AF55",
                            "lun": "1"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "22210002AC01AF55",
                            "lun": "1"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "20:23:00:02:AC:00:B2:C7",
                               "21:23:00:02:AC:00:B2:C7"
                           ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "20:23:00:02:AC:00:B2:C7",
                               "21:23:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP41 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P41",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00B2C7",
                            "lun": "0"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00B2C7",
                            "lun": "0"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "22:22:00:02:AC:01:AF:55",
                                    "23:22:00:02:AC:01:AF:55"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "23:21:00:02:AC:01:AF:55",
                                    "22:21:00:02:AC:01:AF:55"
                           ]
                       }
                   ]
                }
            ]
        }
    }
]

createProfileP42 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P42",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00B2C7",
                            "lun": "0"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00B2C7",
                            "lun": "0"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "22:22:00:02:AC:01:AF:55",
                                    "23:22:00:02:AC:01:AF:55"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "23:21:00:02:AC:01:AF:55",
                                    "22:21:00:02:AC:01:AF:55"
                           ]
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP43 = [
   {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "F1407_API_SP_P43",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "UserDefined",
                "wwpnType": "UserDefined",
                "mac": "34:64:A9:93:2C:E1",
                "wwnn": "10:00:34:64:a9:93:2c:e1",
                "wwpn": "20:00:34:64:a9:93:2c:e1",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "UserDefined",
                "wwpnType": "UserDefined",
                "mac": "34:64:A9:93:2C:E9",
                "wwnn": "10:00:34:64:a9:93:2c:e9",
                "wwpn": "20:00:34:64:a9:93:2c:e9",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP44 = [
   {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "F1407_API_SP_P44",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Virtual",
                "wwnType": "Virtual",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Virtual",
                "wwnType": "Virtual",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP45 = [
   {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P45",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                        {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileP47 = [
   {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P47",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "4000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


createProfileN71 = [
   {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_N71",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined"
                }
            }
        ],
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },

        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None
    }
]


editProfileN15 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP16 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                        {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP18 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP17 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP58_Pre = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP58 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileN27 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:24:00:02:AC:00:B2:C7",
                               "20:24:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP19 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP20 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL2),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP21_pre = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP21 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP22 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Manual",
                   "lun": "2",
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP23 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileN25 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileN26 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": []
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL3),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP24_pre = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP24 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                },
                {
                   "id": 2,
                   "volumeUri": "FC:{}".format(VOL2),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP30 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "NotBootable"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": False,
            "mode": None
        },
        "boot": {
            "order": [],
            "manageBoot": False
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": False,
            "volumeAttachments": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP28 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP54 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareTypeUri": SHM1,
        "enclosureGroupUri": EG1,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
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
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileN29 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "NotBootable"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileN70 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP49 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics": True,
        "name": "F1407_API_SP_P37",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00B2C7",
                            "lun": "0"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00B2C7",
                            "lun": "0"
                        }
                    ],
                    "bootVolumeSource": "UserDefined"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "20:23:00:02:AC:00:B2:C7",
                               "21:23:00:02:AC:00:B2:C7"
                           ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "20:23:00:02:AC:00:B2:C7",
                               "21:23:00:02:AC:00:B2:C7"
                           ]
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


HeaderP31P33 = {
    'Content-Type': 'application/json',
    'Accept-Language': 'en_US',
    'Accept': 'appliacation/json, */*',
    'X-Api-Version': 200
}


createProfileP31 = [
    {
        "type": "ServerProfileV5",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P31",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        }
    }
]


editProfileN33 = [
    {
        "type": "ServerProfileV5",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P47",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "4000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "priority": "NotBootable"
                }
            }
        ],
        "boot": {
            "manageBoot": False
        },
        "bootMode": None,
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP46 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P45",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "macType": "Physical",
                "wwnType": "Physical",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                        {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP48 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P47",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "4000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
       "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP50 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": False,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]


editProfileP52 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F1407_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag": ""
    }
]


editProfileP51 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics": True,
        "name": "F1407_API_SP_P42",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP55 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "name": "F1407_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP56 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "name": "F1407_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP55P56ViceVersa = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "name": "F1407_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFI"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP57 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "name": "F1407_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": None,
            "manageMode": True,
            "mode": "BIOS"
        },
        "boot": {
            "order": [
                "CD",
                "USB",
                "HardDisk",
                "PXE"
            ],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP57ViceVersa = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "name": "F1407_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editProfileP60 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH2),
        "serverHardwareTypeUri": SHM2,
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC2,
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "name": "F1407_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "P60TestCase1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "P60TestCase2",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FC:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": {
            "pxeBootPolicy": "Auto",
            "manageMode": True,
            "mode": "UEFIOptimized"
        },
        "boot": {
            "order": ["HardDisk"],
            "manageBoot": True
        },
        "bios":{
            "manageBios": False,
            "overriddenSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "sanStorage":{
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                   "id": 1,
                   "volumeUri": "FC:{}".format(VOL1),
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": []
                       }
                   ]
                }
            ]
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "category": "server-profiles",
        "eTag":  ""
    }
]


editVolumeP59 = [
    {
        "type": "StorageVolumeV3",
        "deviceVolumeName": VOL1,
        "provisionType": "Thin",
        "isPermanent": True,
        "shareable": False,
        "provisionedCapacity": "10737418240",
        "raidLevel": "RAID1",
        "deviceType": "FC",
        "refreshState": "NotRefreshing",
        "stateReason": "None",
        "category": "storage-volumes",
        "description": "",
        "eTag": "",
        "uri": "FC:{}".format(VOL1),
        "name": VOL1,
        "state": "Normal"
    }
]


admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Enclosures
ENC1 = 'wpst23'

# Server Hardware
SH1 = '%s, bay 1' % ENC1
SH2 = '%s, bay 2' % ENC1
SH3 = '%s, bay 4' % ENC1
SH4 = '%s, bay 4' % ENC1
SH5 = '%s, bay 5' % ENC1

# Server Hardware Model
SHM12 = 'BL420c Gen8 1'
SHM34 = 'BL420c Gen8 1'
SHM5  = 'BL460c Gen9 1'



# Enclosure Group
EG1 = 'GRP-%s' % ENC1

# Network FC
FC1 = 'FCoE1'
FC2 = 'FCoE2'

# SAN Volume
VOL1 = '{}-FCoE-Vol1-Thin-20GB-R5-Private'.format(ENC1.upper())
VOL2 = '{}-FCoE-Vol3-Thin-30GB-R5-Shared'.format(ENC1.upper())
VOL3 = '{}-FCoE-Vol2-Full-20GB-R5-Private'.format(ENC1.upper())


vol_orig_size = '21474836480'

vol_modify_size = '42949672960'

# Create SP with one primary connection, with private volume as boot volume
createProfileP01P02P34P35P36 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P01P02P34P35P36",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_N03",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


createsProfileP04P05P07P13P14 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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


createProfileN06 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_N06",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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
        "osDeploymentSettings": None
    }
]

createProfileN08 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_N08",
        "connections": [
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_N09",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        }
    }
]


createProfileN10 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_N10",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


createProfileP11P12P61 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P11P12P61",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        }
    }
]


createGen9ProfileP37 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType" : "Virtual",
        "serialNumberType" : "Virtual",
        "wwnType" : "Virtual",
        "hideUnusedFlexNics": True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P37",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
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


createGen9ProfileP38 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
                                ]
                       }
                   ]
                }
            ]
        }
    }
]


createGen9ProfileP39 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
                                ]
                       }
                   ]
                }
            ]
        }
    }
]


createGen9ProfileP40 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity": "Bay",
        "macType": "Virtual",
        "serialNumberType" : "Virtual",
        "wwnType" : "Virtual",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P40",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00C4A7",
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00C4A7",
                            "lun": "0"
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


createGen9ProfileP41 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity": "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P41",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00C4A7",
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00C4A7",
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
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
                                ]
                       }
                   ]
                }
            ]
        }
    }
]

createGen9ProfileP42 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity": "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics": True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P42",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00C4A7",
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00C4A7",
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
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
                                ]
                       }
                   ]
                }
            ]
        }
    }
]


createGen9ProfileP43 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P43",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "macType": "UserDefined",
                "wwpnType": "UserDefined",
                "mac": "86:69:4D:A0:00:B9",
                "wwnn": "10:00:56:ea:e9:40:01:72",
                "wwpn": "10:00:56:ea:e9:40:01:73",
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
                "networkUri": "FCOE:{}".format(FC2),
                "macType": "UserDefined",
                "wwpnType": "UserDefined",
                "mac": "86:69:4D:A0:00:BA",
                "wwnn": "10:00:56:ea:e9:40:01:74",
                "wwpn": "10:00:56:ea:e9:40:01:75",
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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


createGen9ProfileP44 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "affinity": "Bay",
        "macType": "Virtual",
        "serialNumberType" : "Virtual",
        "wwnType": "Virtual",
        "hideUnusedFlexNics": True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P44",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "enclosureGroupUri": EG1,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F221_API_SP_P45",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "macType": "Physical",
                "wwnType": "Physical",
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:2-b",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC2),
                "macType": "Physical",
                "wwnType": "Physical",
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
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
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
                                ]
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P47",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "4000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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


createProfileN71 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P71",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [],
                    "bootVolumeSource": "UserDefined"
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "targets": [],
                    "bootVolumeSource": "UserDefined"
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
        "osDeploymentSettings": None
    }
]


editProfileN15 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [],
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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


editProfileP18 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": None,
        "boot": {
            "order": [
                "HardDisk",
                "CD",
                "Floppy",
                "USB",
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
                }
            }
        ],
        "bootMode": None,
        "boot": {
            "order": [
                "HardDisk",
                "CD",
                "Floppy",
                "USB",
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
                   "volumeUri": "FC:{}".format(VOL2),
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
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
                   "volumeUri": "FC:{}".format(VOL2),
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


editProfileP21_pre = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


editProfileP22 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


editProfileP23 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


editProfileN25 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": []
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


editProfileP24_pre = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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


editProfileP30 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume"
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
        "description": None,
        "serverHardwareTypeUri": 'SHT:{}'.format(SHM5),
        "enclosureGroupUri": EG1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": ENC1,
        "name": "F221_API_SP_P01P02P34P35P36",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
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
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType" : "Virtual",
        "serialNumberType" : "Virtual",
        "wwnType" : "Virtual",
        "hideUnusedFlexNics": True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P37",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "networkUri": "FCOE:{}".format(FC1),
                "boot": {
                    "priority": "Primary",
                    "targets": [
                        {
                            "arrayWwpn": "20230002AC00C4A7",
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "boot": {
                    "priority": "Secondary",
                    "targets": [
                        {
                            "arrayWwpn": "20240002AC00C4A7",
                            "lun": "0"
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
                   "lun": "0",
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "21:23:00:02:AC:00:C4:A7",
                               "20:23:00:02:AC:00:C4:A7"
                           ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                               "20:24:00:02:AC:00:C4:A7",
                               "21:24:00:02:AC:00:C4:A7"
                           ]
                       }
                   ]
                }
            ]
        }
    }
]


HeaderP31P33 = {
    'Content-Type': 'application/json',
    'Accept-Language': 'en_US',
    'Accept': 'appliacation/json, */*',
    'X-Api-Version': 200
}


createGen9ProfileP31 = [
    {
        "type": "ServerProfileV5",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "affinity": "Bay",
        "macType": "Virtual",
        "serialNumberType" : "Virtual",
        "wwnType": "Virtual",
        "hideUnusedFlexNics": True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P31",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P47",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "4000",
                "networkUri": "FCOE:{}".format(FC1),
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
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "enclosureGroupUri": EG1,
        "macType": "Physical",
        "wwnType": "Physical",
        "name": "F221_API_SP_P45",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
                "macType": "Physical",
                "wwnType": "Physical",
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
                "networkUri": "FCOE:{}".format(FC2),
                "macType": "Physical",
                "wwnType": "Physical",
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume"
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
                   "isBootVolume": True,
                   "lunType": "Auto",
                   "lun": None,
                   "storagePaths": [
                       {
                           "isEnabled": True,
                           "connectionId": 1,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
                                ]
                       }
                   ]
                }
            ]
        }
    }
]


editProfileP48 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P47",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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


editProfileP50 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
                }
            }
        ],
        "bootMode": None,
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
        "eTag":  ""
    }
]


editProfileP52 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH3),
        "description": None,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P04P05P07P13P14",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "AdapterBIOS"
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


editProfileP51 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity": "Bay",
        "hideUnusedFlexNics": True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P42",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
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


editProfileP56 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
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


editProfileP55P56ViceVersa = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P38",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
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


editProfileP57 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
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


editProfileP57ViceVersa = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
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


editProfileP60 = [
    {
        "type": "ServerProfileV7",
        "serverHardwareUri": 'SH:{}'.format(SH5),
        "description": None,
        "affinity" : "Bay",
        "macType": "Physical",
        "wwnType": "Physical",
        "hideUnusedFlexNics" : True,
        "serverHardwareTypeUri": "",
        "enclosureGroupUri": EG1,
        "enclosureUri": "",
        "name": "F221_API_SP_P39",
        "connections": [
            {
                "id": 1,
                "name": "P60TestCase1",
                "functionType": "FibreChannel",
                "portId": "Flb 1:1-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC1),
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
                "portId": "Flb 1:2-b",
                "requestedMbps": "8000",
                "networkUri": "FCOE:{}".format(FC2),
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
                           "storageTargets": [
                                    "21:23:00:02:AC:00:C4:A7",
                                    "20:23:00:02:AC:00:C4:A7"
                                ]
                       },
                       {
                           "isEnabled": True,
                           "connectionId": 2,
                           "storageTargetType": "Auto",
                           "storageTargets": [
                                    "21:24:00:02:AC:00:C4:A7",
                                    "20:24:00:02:AC:00:C4:A7"
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


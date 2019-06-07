APPLIANCE_IP = '10.9.2.50'  #OV Appliance IP
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

spp_details = {'spp': 'SPPgen9snap6_2016_0517_107', 'path': 'z:\builds\QA\SPP\Gen9Snap6\SPPgen9snap6.2016_0517.107.iso'}
firmware = {'manageFirmware': False, 'forceInstallFirmware': True, 'uri': '/rest/firmware-drivers/SPPgen9snap6_2016_0517_107', 'firmwareInstallType': 'FirmwareOnlyOfflineMode'}

unassigned_server_profiles = [
                {'type': 'ServerProfileV6', 'serverHardwareUri': '',
                                    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 5', 'enclosureGroupUri': 'EG:ME2-EG1', 'serialNumberType': 'Virtual',
                                    'macType': 'Virtual', 'wwnType': 'Virtual',
                                    'name': 'WR-b2-PrmBP2', 'description': '', 'affinity': 'Bay',
                                    'firmware': {'manageFirmware': firmware['manageFirmware'], 'firmwareBaselineUri': firmware['uri'], 'forceInstallFirmware': firmware['forceInstallFirmware'], 'firmwareInstallType': firmware['firmwareInstallType']},
                                    'bootMode':{'manageMode': True, 'mode': 'UEFI'},
                                    'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '1000', 'networkUri': 'ETH:net1009-a', 'functionType': 'Ethernet'},
                                                    {'id': 2, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '1000', 'networkUri': 'ETH:net1008-a', 'functionType': 'Ethernet'},
                                                    # {'id': 3, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:FCOE-3601', 'functionType': 'FibreChannel'}
                                                     # 'boot': {'priority': 'Primary', 'targets':[{'arrayWwpn':'20120002AC0127C6', 'lun':'2'}], 'bootVolumeSource': 'UserDefined'}, 'macType': 'UserDefined', 'mac': 'F8:16:54:B1:FC:02', 'wwpnType': 'UserDefined', 'wwpn': '10:00:F8:16:54:B1:FC:02', 'wwnn': '20:00:F8:16:54:B1:FC:02'},
                                                    {'id': 4, 'name': 'Mezz 3:2-a', 'portId': 'Mezz 3:2-a', 'requestedMbps': '1000', 'networkUri': 'ETH:net1009-a', 'functionType': 'Ethernet'},
                                                    {'id': 5, 'name': 'Mezz 3:2-c', 'portId': 'Mezz 3:2-c', 'requestedMbps': '1000', 'networkUri': 'ETH:net1008-a', 'functionType': 'Ethernet'},
                                                    # {'id': 6, 'name': 'Mezz 3:2-b', 'portId': 'Mezz 3:2-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:FCOE-3602', 'functionType': 'FibreChannel'}
                                                     # 'boot': {'priority': 'Secondary', 'targets':[{'arrayWwpn':'21120002AC0127C6', 'lun':'2'}], 'bootVolumeSource': 'UserDefined'}, 'macType': 'UserDefined', 'mac': 'F8:16:54:B1:FC:03', 'wwpnType': 'UserDefined', 'wwpn': '10:00:F8:16:54:B1:FC:03', 'wwnn': '20:00:F8:16:54:B1:FC:03'}
                                                    ],
                                          "localStorage": {
                                          "sasLogicalJBODs":
                                            [{"id": 1,"deviceSlot": "Mezz 1","name": "LD1","numPhysicalDrives": 2,"driveMinSizeGB": 50,"driveMaxSizeGB": 500,"driveTechnology": "SasHdd",}],
                                            "controllers": [{"deviceSlot": "Mezz 1","mode": "RAID","initialize": False,"importConfiguration": False,
                                            "logicalDrives":[{"name": None,"raidLevel": "RAID1","bootable": True,"numPhysicalDrives": None,"driveTechnology": None,"sasLogicalJBODId": 1,"driveNumber": None}]}]
                                        },
                                    'bios': {'manageBios': False, 'overriddenSettings': []}},
                {'type': 'ServerProfileV6', 'serverHardwareUri': 'SH:CN754406WR, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Physical',
                    'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WR-b2-PrmBP', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': firmware['manageFirmware'], 'firmwareBaselineUri': firmware['uri'], 'forceInstallFirmware': firmware['forceInstallFirmware'], 'firmwareInstallType': firmware['firmwareInstallType']},
                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '1000', 'networkUri': 'ETH:net1009-a', 'functionType': 'Ethernet'},
                                    {'id': 2, 'name': 'Mezz 3:1-c', 'portId': 'Mezz 3:1-c', 'requestedMbps': '1000', 'networkUri': 'ETH:net1008-a', 'functionType': 'Ethernet'},
                                    # {'id': 3, 'name': 'Mezz 3:1-b', 'portId': 'Mezz 3:1-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:FCOE-3601', 'functionType': 'FibreChannel'}
                                     # 'boot': {'priority': 'Primary', 'targets':[{'arrayWwpn':'20120002AC0127C6', 'lun':'2'}], 'bootVolumeSource': 'UserDefined'}, 'macType': 'UserDefined', 'mac': 'F8:16:54:B1:FC:02', 'wwpnType': 'UserDefined', 'wwpn': '10:00:F8:16:54:B1:FC:02', 'wwnn': '20:00:F8:16:54:B1:FC:02'},
                                    {'id': 4, 'name': 'Mezz 3:2-a', 'portId': 'Mezz 3:2-a', 'requestedMbps': '1000', 'networkUri': 'ETH:net1009-a', 'functionType': 'Ethernet'},
                                    {'id': 5, 'name': 'Mezz 3:2-c', 'portId': 'Mezz 3:2-c', 'requestedMbps': '1000', 'networkUri': 'ETH:net1008-a', 'functionType': 'Ethernet'},
                                    # {'id': 6, 'name': 'Mezz 3:2-b', 'portId': 'Mezz 3:2-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:FCOE-3602', 'functionType': 'FibreChannel'}
                                     # 'boot': {'priority': 'Secondary', 'targets':[{'arrayWwpn':'21120002AC0127C6', 'lun':'2'}], 'bootVolumeSource': 'UserDefined'}, 'macType': 'UserDefined', 'mac': 'F8:16:54:B1:FC:03', 'wwpnType': 'UserDefined', 'wwpn': '10:00:F8:16:54:B1:FC:03', 'wwnn': '20:00:F8:16:54:B1:FC:03'}
                                    ],
                    "localStorage": {"sasLogicalJBODs": [{"id": 1,"deviceSlot": "Mezz 1","name": "LD1","numPhysicalDrives": 2,"driveMinSizeGB": 50,"driveMaxSizeGB": 500,"driveTechnology": "SasHdd",}],
                                       "controllers": [{"logicalDrives":
                                         [{"name": None,"raidLevel": "RAID1","bootable": True,"numPhysicalDrives": None,"driveTechnology": None,"sasLogicalJBODId": 1,"driveNumber": None}],
                                          "deviceSlot": "Mezz 1","mode": "RAID","initialize": False,"importConfiguration": False
                                            }]
                                        },
                    'bios': {'manageBios': False, 'overriddenSettings': []}}
                ]
    #SH:CN754406WR, bay 2
    # "localStorage":{
    # "sasLogicalJBODs":[{"id":1,"deviceSlot":"Mezz 1","name":"LD1","numPhysicalDrives":2,"driveMinSizeGB":50,"driveMaxSizeGB":500,"driveTechnology":"SasHdd","sasLogicalJBODUri":''}],
    # "controllers":[{
    # "logicalDrives":[{"name":'',"raidLevel":"RAID1","bootable":True,"numPhysicalDrives":'',"driveTechnology":'',"sasLogicalJBODId":1,"driveNumber":''}],
    # "deviceSlot":"Mezz 1","mode":"RAID","initialize":False,"importConfiguration":False}]}

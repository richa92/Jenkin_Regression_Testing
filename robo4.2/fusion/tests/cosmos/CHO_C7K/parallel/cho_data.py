
admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

ilo_credentials = {'username': 'Administrator', 'password': 'password'}

server_profile_E1bay3 = {'name': 'ChoR2E1Prof3', 'type': 'ServerProfileV6', 'serverHardwareUri': 'CosmosCHOR2E1, bay 3', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connections': [{'id': 1, 'name': 'Eth1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth1', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': 'CHO3PAR-FA-P1', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:CHO3PAR-FA-P1', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                    'boot':{'priority':'Primary', 'bootVolumeSource':'UserDefined', 'targets':[{'arrayWwpn':'20:21:00:02:AC:01:27:CC', 'lun':'1'}]}},
                                         ],
                                         
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'bios': {'manageBios': False, 'overriddenSettings': []},
                         'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                         'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                          'volumeAttachments': [{'id': 1, 'volumeUri': None, 'volumeName': 'VolCHOR2E1Bay3_Madhav', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1, 'volumeStoragePoolUri': 'SPOOL:Raid5-FC', 'volumeStorageSystemUri':'SSYS:TBRack5-P7200C', 'volumeProvisionType': 'Thin', 'volumeProvisionedCapacityBytes':'53687091200', 'volumeShareable': False, 'permanent': False,
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': []}]}]
                                          }
                         }

expected_server_profile_E1bay3 = {'name': 'ChoR2E1Prof3', 'type': 'ServerProfileV6', 'uri': 'SP:ChoR2E1Prof3', 'serverHardwareUri': 'SH:CosmosCHOR2E1, bay 3', 'enclosureGroupUri': 'EG:CHO_Encg', 'enclosureUri': 'ENC:CosmosCHOR2E1', 'enclosureBay': 3, 'associatedServer': None, 'hideUnusedFlexNics': True, 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Virtual', 'description': '', 'category': 'server-profiles', 'affinity': 'Bay', 'state': 'Normal', 'inProgress': False,
                                  'connections': [{'id': 1, 'name': 'Eth1', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth1', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                                   'boot': {'priority': 'Primary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                                  {'id': 2, 'name': 'CHO3PAR-FA-P1', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P1', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual',      
                                                   }
                                                  ],
                                  'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
                                  'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                  'bios': {'manageBios': False, 'overriddenSettings': []},
                                  'osDeploymentSettings': None,
                                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                  'sanStorage': {'manageSanStorage': True,'hostOSType': 'Windows 2012 / WS2012 R2', 
                                                'volumeAttachments': [{'id': 1, 'isBootVolume': False, 'lun': '1', 'lunType': 'Manual', 'state': 'Attached', 'status': 'OK',
                                                                       'storagePaths': [{'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'storageTargetType': 'Auto', 'storageTargets': ['20:21:00:02:AC:01:27:CC', '21:21:00:02:AC:01:27:CC']}],
                                                                       'volumeStoragePoolUri': 'SPOOL:Raid5-FC', 'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C', 'volumeUri': 'SVOL:VolCHOR2E1Bay3_Madhav'}],
                                                 }
                                  }


edit_server_profile_E1bay3 = {'name': 'ChoR2E1Prof3', 'type': 'ServerProfileV6', 'serverHardwareUri': 'SH:CosmosCHOR2E1, bay 3', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Virtual', 'description': 'Updated Profile', 'affinity': 'Bay',
                              'connections': [{'id': 1, 'name': 'Eth1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth1', 'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                              {'id': 2, 'name': 'CHO3PAR-FA-P1', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:CHO3PAR-FA-P1', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                    'boot':{'priority':'Primary', 'bootVolumeSource':'UserDefined', 'targets':[{'arrayWwpn':'20:21:00:02:AC:01:27:CC', 'lun':'1'}]}},
                                              {'id': 3, 'name': 'Eth2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Eth2', 'boot': {'priority': 'Secondary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                              {'id': 4, 'name': 'CHO3PAR-FA-P2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b', 'requestedMbps': '4000', 'networkUri': 'FCOE:CHO3PAR-FA-P2', 'mac': None, 'wwpn': '', 'wwnn': '',
                                                    'boot':{'priority':'Secondary', 'bootVolumeSource':'UserDefined', 'targets':[{'arrayWwpn':'21:21:00:02:AC:01:27:CC', 'lun':'1'}]}},
                                              ],
                              'boot': {'manageBoot': True, 'order': ['HardDisk']},
                              'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                              'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                              'bios': {'manageBios': False, 'overriddenSettings': []},
                              'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                              'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True, 
                                            'volumeAttachments': [{'id': 1, 'isBootVolume': False, 'lun': '1', 'lunType': 'Manual', 'state': 'Attached', 'status': 'OK',
                                                                       'storagePaths': [{'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'storageTargetType': 'Auto', 'storageTargets': ['20:21:00:02:AC:01:27:CC', '21:21:00:02:AC:01:27:CC']}],
                                                                       'volumeStoragePoolUri': 'SPOOL:Raid5-FC', 'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C', 'volumeUri': 'SVOL:VolCHOR2E1Bay3_Madhav'}],
                                                 }
                              }


expected_edit_server_profile_E1bay3 = {'name': 'ChoR2E1Prof3', 'type': 'ServerProfileV6', 'uri': 'SP:ChoR2E1Prof3', 'serverHardwareUri': 'SH:CosmosCHOR2E1, bay 3', 'enclosureGroupUri': 'EG:CHO_Encg', 'enclosureUri': 'ENC:CosmosCHOR2E1', 'enclosureBay': 3, 'associatedServer': None, 'hideUnusedFlexNics': True, 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Virtual', 'description': 'Updated Profile', 'category': 'server-profiles', 'affinity': 'Bay', 'state': 'Normal', 'inProgress': False,
                                       'connections': [{'id': 1, 'name': 'Eth1', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth1', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                                   'boot': {'priority': 'Primary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                                       {'id': 2, 'name': 'CHO3PAR-FA-P1', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P1', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual'},
                                                       {'id': 3, 'name': 'Eth2', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth2', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 2', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                                   'boot': {'priority': 'Secondary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                                       {'id': 4, 'name': 'CHO3PAR-FA-P2', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:2-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P2', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 2', 'macType': 'Physical', 'wwpnType': 'Virtual'}
                                                  ],
                                       'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
                                       'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': None, 'forceInstallFirmware': False, 'firmwareInstallType': None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                                       'sanStorage': {'manageSanStorage': True,'hostOSType': 'Windows 2012 / WS2012 R2', 
                                                'volumeAttachments': [{'id': 1, 'isBootVolume': False, 'lun': '1', 'lunType': 'Manual', 'state': 'Attached', 'status': 'OK',
                                                                       'storagePaths': [{'connectionId': 2, 'isEnabled': True, 'status': 'OK', 'storageTargetType': 'Auto', 'storageTargets': ['20:21:00:02:AC:01:27:CC', '21:21:00:02:AC:01:27:CC']}],
                                                                       'volumeStoragePoolUri': 'SPOOL:Raid5-FC', 'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C', 'volumeUri': 'SVOL:VolCHOR2E1Bay3_Madhav'}],
                                                 }
                                       }
                                       
move_server_profiles = [{'name': 'ChoR2E1Prof3', 'type': 'ServerProfileV6', 'serverHardwareUri': 'SH:CosmosCHOR2E1, bay 9', 'serverHardwareTypeUri': 'SHT:BL460c Gen9 1', 'enclosureGroupUri':'EG:CHO_Encg', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Virtual', 'description': 'Moved from Gen9 Bay3 to Gen9 bay 9', 'affinity': 'Bay',
                           'connections': [{'id': 1, 'name': 'Eth1', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth1', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                       'boot': {'priority': 'Primary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                           {'id': 2, 'name': 'CHO3PAR-FA-P1', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P1', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual'},
                                           {'id': 3, 'name': 'Eth2', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth2', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 2', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                       'boot': {'priority': 'Secondary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                           {'id': 4, 'name': 'CHO3PAR-FA-P2', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:2-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P2', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 2', 'macType': 'Physical', 'wwpnType': 'Virtual'}
                                      ],
                            'boot': {'manageBoot': True,  'order': ['CD', 'USB', 'HardDisk', 'PXE']},
                            'bootMode':{'manageMode': True, 'mode': 'BIOS'},
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                            'localStorage':{'sasLogicalJBODs': [], 'controllers':[]},
                            'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                          'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:VolCHOR2E1Bay3_Madhav', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1, 'volumeStoragePoolUri': 'SPOOL:Raid5-FC', 'volumeStorageSystemUri':'SSYS:TBRack5-P7200C',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': ['20:21:00:02:AC:01:27:CC', '21:21:00:02:AC:01:27:CC']}]}]
                                          }
                            },
                        {'name': 'ChoR2E1Prof2', 'type': 'ServerProfileV6', 'serverHardwareUri': 'SH:CosmosCHOR2E1, bay 3', 'serverHardwareTypeUri': 'SHT:BL460c Gen9 1', 'enclosureGroupUri':'EG:CHO_Encg', 'serialNumberType': 'Virtual', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Virtual', 'description': 'Moved Back Gen9 Server From Bay9 to bay 3', 'affinity': 'Bay',
                           'connections': [{'id': 1, 'name': 'Eth1', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth1', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                       'boot': {'priority': 'Primary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                           {'id': 2, 'name': 'CHO3PAR-FA-P1', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P1', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 1', 'macType': 'Physical', 'wwpnType': 'Virtual'},
                                           {'id': 3, 'name': 'Eth2', 'functionType': 'Ethernet', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'maximumMbps': 20000, 'networkUri': 'ETH:Eth2', 'allocatedMbps': '2500', 'requestedVFs': 'Auto', 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 2', 'macType': 'Physical', 'wwpnType': 'Virtual', 'wwpn': None, 'wwnn': None,
                                       'boot': {'priority': 'Secondary', 'initiatorNameSource': 'ProfileInitiatorName'}},
                                           {'id': 4, 'name': 'CHO3PAR-FA-P2', 'functionType': 'FibreChannel', 'deploymentStatus': 'Deployed', 'portId': 'Flb 1:2-b', 'requestedMbps': '4000', 'maximumMbps': 20000, 'networkUri': 'FCOE:CHO3PAR-FA-P2', 'allocatedMbps': '4000', 'requestedVFs': None, 'interconnectUri': 'IC:CosmosCHOR2E1, interconnect 2', 'macType': 'Physical', 'wwpnType': 'Virtual'}
                                      ],
                            'boot': {'manageBoot': True,  'order': ['CD', 'USB', 'HardDisk', 'PXE']},
                            'bootMode':{'manageMode': True, 'mode': 'BIOS'},
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                            'bios': {'manageBios': False, 'overriddenSettings': []},
                            'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None,
                            'localStorage':{'sasLogicalJBODs': [], 'controllers':[]},
                            'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                          'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:VolCHOR2E1Bay3_Madhav', 'isBootVolume': False, 'lunType': 'Manual', 'lun': 1, 'volumeStoragePoolUri': 'SPOOL:Raid5-FC', 'volumeStorageSystemUri':'SSYS:TBRack5-P7200C',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 2, 'storageTargetType': 'Auto', 'storageTargets': ['20:21:00:02:AC:01:27:CC', '21:21:00:02:AC:01:27:CC']}]}]
                                          }
                         }]
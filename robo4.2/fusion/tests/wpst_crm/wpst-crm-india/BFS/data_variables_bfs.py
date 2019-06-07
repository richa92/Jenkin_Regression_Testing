
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}


ethernet_networks = [{'name': 'eth_100', 'type': 'ethernet-networkV300', 'vlanId': 100, 'purpose': 'Management',
                      'smartLink': False, 'privateNetwork': False}
                     ]

expected_ethernet_networks = [{'name': 'eth_100', 'type': 'ethernet-networkV300', 'ethernetNetworkType': 'Tagged',
                               'vlanId': 100, 'smartLink': False, 'purpose': 'Management', 'privateNetwork': False,
                               'description': None, 'status': 'OK', 'state': 'Active', 'category': 'ethernet-networks'}
                              ]


fc_networks = [{'name': 'FC_A', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'FC_B', 'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
               ]

expected_fc_networks = [{"type": "fc-networkV300", "fabricType": "FabricAttach", "linkStabilityTime": 30, "managedSanUri": None, "autoLoginRedistribution": True,
                         "name": "FC_A", "state": "Active", "description": None, "status": "OK", "category": "fc-networks"},
                        {"type": "fc-networkV300", "fabricType": "FabricAttach", "linkStabilityTime": 30, "managedSanUri": None, "autoLoginRedistribution": True,
                         "name": "FC_B", "state": "Active", "description": None, "status": "OK", "category": "fc-networks"}
                        ]

fcoe_networks = [{'name': 'FCoE_A201', 'type': 'fcoe-networkV300', 'vlanId': 201, 'managedSanUri': None},
                 {'name': 'FCoE_B200', 'type': 'fcoe-networkV300', 'vlanId': 200, 'managedSanUri': None}
                 ]

expected_fcoe_networks = [{"type": "FCOE", "type": "fcoe-networkV300", "vlanId": 201, "managedSanUri": None, "description": None,
                           "name": "FCoE_A201", "state": "Active", "status": "OK", "category": "fcoe-networks"},
                          {"type": "FCOE", "type": "fcoe-networkV300", "vlanId": 200, "managedSanUri": None, "description": None,
                           "name": "FCoE_B200", "state": "Active", "status": "OK", "category": "fcoe-networks"}]


storage_systems = {"type": "StorageSystemV4", "credentials": {"username": "3paradm", "password": "3pardata"},
                    "name": "3PAR",
                    "hostname": "10.10.3.23",
                    "family":"StoreServ",                                        
                    "deviceSpecificAttributes":
                                            { "managedDomain":"NO DOMAIN"                                              
                                            },                                    
                    "ports": [{"type":"StorageTargetPortV4",
                               "name": "0:1:1",
                               "expectedNetworkUri": "FCOE:FCoE_B200",
                               "expectedNetworkName": "FCoE_B200",
                               "mode": "Managed"},
                              {"type":"StorageTargetPortV4",
                               "name": "0:1:2",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},                                                          
                              {"type":"StorageTargetPortV4",
                               "name": "0:2:1",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                               {"type":"StorageTargetPortV4",
                               "name": "0:2:2",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                               {"type":"StorageTargetPortV4",
                               "name": "1:1:1",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                               {"type":"StorageTargetPortV4",
                               "name": "1:1:2",
                               "expectedNetworkUri": "FCOE:FCoE_A201",
                               "expectedNetworkName": "FCoE_A201",
                               "mode": "Managed"}, 
                               {"type":"StorageTargetPortV4",
                               "name": "1:2:1",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},   
                              {"type":"StorageTargetPortV4",
                               "name": "1:2:2",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                              ]                              
                              
                   }

expected_storage_systems = [{"type": "StorageSystemV4", "credentials": {"username": "3paradm"},
                    "name": "3PAR",
                    "hostname": "10.10.3.23",
                    "family":"StoreServ",                                                          
                    "deviceSpecificAttributes":
                                            { "managedDomain":"NO DOMAIN",
                                             "serialNumber": "1647626"                                             
                                            },                                    
                    "ports": [{"type":"StorageTargetPortV4",
                               "name": "0:1:1",
                               "expectedNetworkUri": "FCOE:FCoE_B200",
                               "expectedNetworkName": "FCoE_B200",
                               "mode": "Managed"},
                              {"type":"StorageTargetPortV4",
                               "name": "0:1:2",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},                                                          
                              {"type":"StorageTargetPortV4",
                               "name": "0:2:1",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                               {"type":"StorageTargetPortV4",
                               "name": "0:2:2",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                               {"type":"StorageTargetPortV4",
                               "name": "1:1:1",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                               {"type":"StorageTargetPortV4",
                               "name": "1:1:2",
                               "expectedNetworkUri": "FCOE:FCoE_A201",
                               "expectedNetworkName": "FCoE_A201",
                               "mode": "Managed"}, 
                               {"type":"StorageTargetPortV4",
                               "name": "1:2:1",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},   
                              {"type":"StorageTargetPortV4",
                               "name": "1:2:2",
                               "expectedNetworkUri": None,
                               "expectedNetworkName": None,
                               "mode": "AutoSelectExpectedSan"},
                              ]                              
                              
                   }
                            ]

storage_pool = {'storageSystemUri': '3PAR', 'name': 'sanboot_1', "isManaged": True}
                 

storage_volumes = [
    {        
        "name": "",
        "description": "",
                       "storageSystemUri": "3PAR",
                       "deviceVolumeName": "FVT_AB_Volume2_Tbird_Windows201",                       
                       "isShareable": False

                       
    },
    {        
        "name": "",
        "description": "",
                       "storageSystemUri": "3PAR",
                       "deviceVolumeName": "FVT_GP_Extra",
                       "isShareable": False
    },
    {     
        "name": "",
        "description": "",
                       "storageSystemUri": "3PAR",
                       "deviceVolumeName": "FVTSharedVolume",
                       "isShareable": True
    },
    {       
        "name": "",
        "description": "",
                       "storageSystemUri": "3PAR",
                       "deviceVolumeName": "FVT_Tbird80_Winodws_2012",
                       "isShareable": False
    }

]


uplink_sets = {'upset_eth': {'name': 'up_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                             'networkUris': ['eth_100'], 'mode': 'Auto', 'nativeNetworkUri': 'eth_100',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'}]},
               'upset_fcoe_a': {'name': 'up_fcoe_a', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                'networkUris': ['FCoE_A201'], 'mode': 'Auto',
                                'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'}]},
               'upset_fcoe_b': {'name': 'up_fcoe_b', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                'networkUris': ['FCoE_B200'], 'mode': 'Auto',
                                'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'}]},
               'upset_fc_a': {'name': 'up_fc_a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                              'networkUris': ['FC_A'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'}]},
               'upset_fc_b': {'name': 'up_fc_b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                              'networkUris': ['FC_B'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'}]}

               }

ligs = {'name': 'LIG_HA',
        'type': 'logical-interconnect-groupV300',
        'enclosureType': 'SY12000',
        "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
        'uplinkSets': [uplink_sets['upset_eth'].copy(),
                       uplink_sets['upset_fcoe_a'].copy(),
                       uplink_sets['upset_fcoe_b'].copy(),
                       uplink_sets['upset_fc_a'].copy(),
                       uplink_sets['upset_fc_b'].copy()
                       ],
        'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
        'internalNetworkUris': [],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'enclosureIndexes': [1, 2],
        'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
        }


enc_groups = {'name': 'EG_HA',
              'type': 'EnclosureGroupV400',
              'enclosureCount': 2,
              'enclosureTypeUri': 'SY12000',
              'stackingMode': 'Enclosure',
              'description': None,
              'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                          {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_HA"},
                                          {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                          {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_HA"}
                                          ],
              'ipAddressingMode': 'External',
              'powerMode': 'RedundantPowerFeed'}

logical_enclosure = {'name': 'LE_HA', 'enclosureUris': ['ENC:CN754404RC', 'ENC:FVTCRMBFS3'], 'enclosureGroupUri': 'EG:EG_HA', 'firmwareBaselineUri': None,
                     'forceInstallFirmware': False}

expected_logical_enclosure = {'type': 'LogicalEnclosureV300', 'name': 'LE_HA', 'status': 'OK', 'enclosureUris': ['ENC:CN754404RC', 'ENC:FVTCRMBFS3'], 'enclosureGroupUri': 'EG:EG_HA'}


server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                    'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'connections': [
                        {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                    ],
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                   'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': 1,
                                                          'isBootVolume': True,
                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            },
                                                                           {'isEnabled': True, 'connectionId': 2,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            }
                                                                           ]}]},
                    'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                    'bios': {'manageBios': False, 'overriddenSettings': []}},

                   {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                    'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'connections': [
                        {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                    ],
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode':{'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                   'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Auto', 'lun': None,
                                                          'isBootVolume': True,
                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            },
                                                                           {'isEnabled': True, 'connectionId': 2,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            }
                                                                           ]}]},
                    'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                    'bios': {'manageBios': False, 'overriddenSettings': []}},

                   {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                    'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'connections': [
                        {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                    ],
                    'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                    'bootMode':{'manageMode': True, 'mode': 'BIOS'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                   'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_TbirdPotash_W2012_BFS_Legac', 'lunType': 'Manual', 'lun': 1,
                                                          'isBootVolume': True,
                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            },
                                                                           {'isEnabled': True, 'connectionId': 2,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            }
                                                                           ]}]},
                    'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                    'bios': {'manageBios': False, 'overriddenSettings': []}},

                   {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                    'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'connections': [
                        {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'macType': 'UserDefined', 'mac': '14:02:EC:C8:83:31', 'wwpnType': 'UserDefined', 'wwnn': '10:00:14:02:ec:c8:83:31', 'wwpn': '20:00:14:02:ec:c8:83:31'},
                        {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                         'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'macType': 'UserDefined', 'mac': '14:02:EC:C8:83:39', 'wwpnType': 'UserDefined', 'wwnn': '10:00:14:02:ec:c8:83:39', 'wwpn': '20:00:14:02:ec:c8:83:39'},
                        {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                    ],
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                   'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': 1,
                                                          'isBootVolume': True,
                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            },
                                                                           {'isEnabled': True, 'connectionId': 2,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                            }
                                                                           ]}]},
                    'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                    'bios': {'manageBios': False, 'overriddenSettings': []}}

                   ]

edit_server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'connections': [
                             {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                         ],
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                                               'isBootVolume': True,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 },
                                                                                {'isEnabled': True, 'connectionId': 2,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 2, 'volumeUri': 'VolName:FVT_GP_Extra', 'lunType': 'Auto', 'lun': None,
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 },
                                                                                {'isEnabled': True, 'connectionId': 2,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 },
                                                                                {'isEnabled': True, 'connectionId': 2,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]}
                                                              ]},
                         'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                         'bios': {'manageBios': False, 'overriddenSettings': []}},

                        {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'connections': [
                             {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                         ],
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                                               'isBootVolume': True,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 },
                                                                                {'isEnabled': True, 'connectionId': 2,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 },
                                                                                {'isEnabled': True, 'connectionId': 2,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]}
                                                              ]},
                         'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                         'bios': {'manageBios': False, 'overriddenSettings': []}},

                        {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'connections': [
                             {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}

                         ],
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                                               'isBootVolume': True,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]}
                                                              ]},
                         'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                         'bios': {'manageBios': False, 'overriddenSettings': []}},

                        {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'connections': [
                             {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}

                         ],
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                                               'isBootVolume': True,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]}
                                                              ]},
                         'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                         'bios': {'manageBios': False, 'overriddenSettings': []}},

                        {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'connections': [
                             {'id': 1, 'name': 'new_conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 3, 'name': 'new_eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}

                         ],
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                                               'isBootVolume': True,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]}
                                                              ]},
                         'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                         'bios': {'manageBios': False, 'overriddenSettings': []}},

                        {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                         'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                         'connections': [
                             {'id': 1, 'name': 'new_conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                             {'id': 3, 'name': 'new_eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}

                         ],
                         'boot': {'manageBoot': True, 'order': ['HardDisk']},
                         'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                        'volumeAttachments': [{'id': 2, 'volumeUri': 'VolName:FVT_Tbird80_Winodws_2012', 'lunType': 'Manual', 'lun': '1',
                                                               'isBootVolume': True,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]},
                                                              {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                               'isBootVolume': False,
                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                 'targetSelector': 'Auto', 'targets': []
                                                                                 }
                                                                                ]}
                                                              ]},
                         'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
                         'bios': {'manageBios': False, 'overriddenSettings': []}}

                        ]

expected_edit_server_profiles = [
    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'name': 'BFS_FCoE_test', 'status': 'OK', 'state': 'Normal',
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                           'isBootVolume': True, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                             'targetSelector': 'Auto'
                                                             },
                                                            {'isEnabled': True, 'connectionId': 2,
                                                             'targetSelector': 'Auto'
                                                             }
                                                            ]},
                                          {'id': 2, 'volumeUri': 'VolName:FVT_GP_Extra', 'lunType': 'Auto',
                                           'isBootVolume': False, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                             'targetSelector': 'Auto'
                                                             },
                                                            {'isEnabled': True, 'connectionId': 2,
                                                             'targetSelector': 'Auto'
                                                             }
                                                            ]},
                                          {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                           'isBootVolume': False, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                             'targetSelector': 'Auto'
                                                             },
                                                            {'isEnabled': True, 'connectionId': 2,
                                                             'targetSelector': 'Auto'
                                                             }
                                                            ]}
                                          ]}
     },

    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'name': 'BFS_FCoE_test', 'status': 'OK', 'state': 'Normal',
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': '1',
                                                                            'isBootVolume': True, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                              'targetSelector': 'Auto'
                                                                                              },
                                                                                             {'isEnabled': True, 'connectionId': 2,
                                                                                              'targetSelector': 'Auto'
                                                                                              }
                                                                                             ]},

                                                                           {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                                            'isBootVolume': False, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                              'targetSelector': 'Auto'
                                                                                              },
                                                                                             {'isEnabled': True, 'connectionId': 2,
                                                                                              'targetSelector': 'Auto'
                                                                                              }
                                                                                             ]}
                                                                           ]}
     },


    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'name': 'BFS_FCoE_test', 'status': 'OK', 'state': 'Normal',
     'connections': [
         {'id': 1, 'name': 'new_conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
         {'id': 3, 'name': 'new_eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}

     ],
     },

    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'name': 'BFS_FCoE_test', 'status': 'OK', 'state': 'Normal',
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 2, 'volumeUri': 'VolName:FVT_Tbird80_Winodws_2012', 'lunType': 'Manual', 'lun': '1',
                                                                            'isBootVolume': True,
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                              'targetSelector': 'Auto', 'targets': []
                                                                                              }
                                                                                             ]},
                                                                           {'id': 3, 'volumeUri': 'VolName:FVTSharedVolume', 'lunType': 'Manual', 'lun': '3',
                                                                            'isBootVolume': False,
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                              'targetSelector': 'Auto', 'targets': []
                                                                                              }
                                                                                             ]}
                                                                           ]},
     }

]
expected_server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'status': 'OK', 'state': 'Normal',
                             'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                             'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                             'firmware': {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'connections': [
                                 {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                 {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                                     'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                 {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                             ],
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': 1,
                                                                   'volumeStoragePoolUri': 'SPOOL:sanboot_1',
                                                                   'volumeStorageSystemUri': 'SSYS:3PAR', 'isBootVolume': True,
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                     'targetSelector': 'Auto'
                                                                                     },
                                                                                    {'isEnabled': True, 'connectionId': 2,
                                                                                     'targetSelector': 'Auto'
                                                                                     }
                                                                                    ]}]},
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'bios': {'manageBios': False, 'overriddenSettings': []}},

                            {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'status': 'OK', 'state': 'Normal',
                             'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                             'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                             'firmware': {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'connections': [
                                 {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                 {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                                  'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                 {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                             ],
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode':{'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto'},
                             'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Auto',
                                                                   'isBootVolume': True, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                     'targetSelector': 'Auto'
                                                                                     },
                                                                                    {'isEnabled': True, 'connectionId': 2,
                                                                                     'targetSelector': 'Auto'
                                                                                     }
                                                                                    ]}]},
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'bios': {'manageBios': False, 'overriddenSettings': []}},

                            {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'status': 'OK', 'state': 'Normal',
                             'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                             'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                             'firmware': {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'connections': [
                                 {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                 {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                                  'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                 {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                             ],
                             'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                             'bootMode':{'manageMode': True, 'mode': 'BIOS'},
                             'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_TbirdPotash_W2012_BFS_Legac', 'lunType': 'Manual', 'lun': 1,
                                                                   'isBootVolume': True, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                     'targetSelector': 'Auto'
                                                                                     },
                                                                                    {'isEnabled': True, 'connectionId': 2,
                                                                                     'targetSelector': 'Auto'
                                                                                     }
                                                                                    ]}]},
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'bios': {'manageBios': False, 'overriddenSettings': []}},

                            {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:FVTCRMBFS3, bay 3', 'status': 'OK', 'state': 'Normal',
                             'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                             'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
                             'firmware': {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'connections': [
                                 {'id': 1, 'name': 'conn1', 'portId': 'Mezz 3:1-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'macType': 'UserDefined', 'mac': '14:02:EC:C8:83:31', 'wwpnType': 'UserDefined', 'wwnn': '10:00:14:02:ec:c8:83:31', 'wwpn': '20:00:14:02:ec:c8:83:31'},
                                 {'id': 2, 'name': 'conn2', 'portId': 'Mezz 3:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
                                  'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'macType': 'UserDefined', 'mac': '14:02:EC:C8:83:39', 'wwpnType': 'UserDefined', 'wwnn': '10:00:14:02:ec:c8:83:39', 'wwpn': '20:00:14:02:ec:c8:83:39'},
                                 {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 3:1-a', 'requestedMbps': '10000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
                             ],
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:FVT_AB_Volume2_Tbird_Windows201', 'lunType': 'Manual', 'lun': 1,
                                                                   'isBootVolume': True, 'volumeStoragePoolUri': 'SPOOL:sanboot_1', 'volumeStorageSystemUri': 'SSYS:3PAR',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                                     'targetSelector': 'Auto'
                                                                                     },
                                                                                    {'isEnabled': True, 'connectionId': 2,
                                                                                     'targetSelector': 'Auto'
                                                                                     }
                                                                                    ]}]},
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'bios': {'manageBios': False, 'overriddenSettings': []}}
                            ]

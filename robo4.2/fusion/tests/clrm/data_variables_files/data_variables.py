# #####################################
admin_credentials = {'userName': 'Administrator', 'password': ''}

# #####################################

# #########PREREQUISITES###############
ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'corp', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '80', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '70', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '21', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '22', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '34', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'untagged_nw', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '33', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '10', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '23', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '24', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '100', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'iSCSI', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV300', 'vlanId': '101', 'purpose': 'ISCSI', "subnetUri": None}
                     ]

fc_networks = [{'fabricType': 'DirectAttach', 'name': 'san_da', 'autoLoginRedistribution': True, 'linkStabilityTime': 30, 'connectionTemplateUri': None, 'type': 'fc-networkV300'},
               {'fabricType': 'FabricAttach', 'name': 'san', 'autoLoginRedistribution': True, 'linkStabilityTime': 30, 'connectionTemplateUri': None, 'type': 'fc-networkV300'}
               ]

network_sets = [{'name': 'netset1', 'type': 'network-setV300', 'networkUris': ['net1', 'corp1'], 'nativeNetworkUri': None},
                {'name': 'netset2', 'type': 'network-setV300', 'networkUris': ['net1', 'corp1', 'production'], 'nativeNetworkUri': None},
                {'name': 'netset3', 'type': 'network-setV300', 'networkUris': ['corp1', 'iSCSI'], 'nativeNetworkUri': None}
                ]

uplink_sets = {'uplink1': {'name': 'upl_corp',
                           'ethernetNetworkType': 'Untagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['corp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]
                           },
               'uplink2': {'name': 'upl_icsp',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['icsp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]
                           },
               'uplink3': {'name': 'upl_san',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkUris': ['san'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'X3', 'speed': 'Auto'}]}
               }

ligs = {'name': 'lig',
        'type': 'logical-interconnect-groupV300',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                    {'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}
                                    ],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink2'].copy(), uplink_sets['uplink3'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net2', 'corp1', 'net1', 'network2', 'untagged_nw', 'tunneled_nw', 'production', 'iSCSI']
        }

enc_groups = {'name': 'enclgrp',
              'type': 'EnclosureGroupV400',
              'enclosureCount': 1,
              'enclosureTypeUri': '/rest/enclosure-types/c7000',
              'stackingMode': 'Enclosure',
              'interconnectBayMappingCount': 2,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
               ],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              }

enclosures = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None},
              {'hostname': "172.18.1.13", 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None}
              ]

storage_systems = [{'family': 'StoreServ', 'name': 'ThreePAR7200-5418', 'hostname': '172.18.11.12', 'credentials': {'username': 'dcs', 'password': 'dcs'}},
                   {"family": "StoreVirtual", "hostname": "172.18.30.2", 'credentials': {'username': 'dcs', 'password': 'dcs'}, 'name': '172.18.30.2'}
                   ]

update_storage_systems = [{'type': 'StorageSystemV4', 'name': 'ThreePAR7200-5418', 'family': 'StoreServ',
                           "hostname": '172.18.11.12', 'credentials': {'username': 'dcs', 'password': 'dcs'},
                           "deviceSpecificAttributes": {"managedDomain": "TestDomain"
                                                        },
                           "ports": [{"expectedNetworkUri": "FC:san",
                                      "expectedNetworkName": "san",
                                      "mode": "Managed"
                                      }, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
                           },
                          {'type': 'StorageSystemV4', 'name': 'Cluster-2', 'family': 'StoreVirtual',
                           "hostname": '172.18.30.2', 'credentials': {'username': 'dcs', 'password': 'dcs'},
                           "ports": [{"name": "172.18.30.2",
                                      "expectedNetworkUri": "ETH:iSCSI",
                                      "expectedNetworkName": "iSCSI",
                                      "mode": "Managed"
                                      }]
                           }
                          ]

storage_pools = [{"storageSystemUri": "ThreePAR7200-5418", "name": "cpg-growth-limit-1TiB", "isManaged": True}
                 ]

storage_volumes = [{"properties": {"name": "svol1", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol2", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol3", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol4", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol5", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol6", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "vsa1", "description": "", "storagePool": "Cluster-2", "size": 1073741824, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'Volume root template for StoreVirtual 1.2', "isPermanent": True},
                   {"properties": {"name": "vsa2", "description": "", "storagePool": "Cluster-2", "size": 1073741824, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'Volume root template for StoreVirtual 1.2', "isPermanent": True},
                   {"properties": {"name": "vsa3", "description": "", "storagePool": "Cluster-2", "size": 1073741824, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'Volume root template for StoreVirtual 1.2', "isPermanent": True},
                   {"properties": {"name": "vsa4", "description": "", "storagePool": "Cluster-2", "size": 1073741824, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'Volume root template for StoreVirtual 1.2', "isPermanent": True},
                   {"properties": {"name": "vsa5", "description": "", "storagePool": "Cluster-2", "size": 1073741824, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'Volume root template for StoreVirtual 1.2', "isPermanent": True},
                   {"properties": {"name": "vsa6", "description": "", "storagePool": "Cluster-2", "size": 1073741824, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'Volume root template for StoreVirtual 1.2', "isPermanent": True}
                   ]

server_profile_templates = [{'name': 'profile_template_gen8_1', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'profile_gen81_san', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san", 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, "volumeName": "san_vol", 'isBootVolume': True, 'lunType': 'Manual', 'lun': 4, 'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}],
                                                                   "volumeStoragePoolUri": "SPOOL:cpg-growth-limit-1TiB",
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR7200-5418",
                                                                   "volumeProvisionType": "Thin",
                                                                   "volumeProvisionedCapacityBytes": "10737418240",
                                                                   "volumeShareable": False,
                                                                   "permanent": False}
                                                                  ]
                                            }
                             },

                            {'name': 'profile_template_gen8_1_1', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_03_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_untagged', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:untagged_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'profile_nomgmt', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_04_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_tunneled', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:tunneled_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'dvSwitch_05_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'Cluster_43_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp'},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp'},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production'},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production'}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, "volumeName": "nvol1", 'isBootVolume': True, 'lunType': 'Manual', 'lun': 2, 'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}],
                                                                   "volumeStoragePoolUri": "SPOOL:cpg-growth-limit-1TiB",
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR7200-5418",
                                                                   "volumeProvisionType": "Thin",
                                                                   "volumeProvisionedCapacityBytes": "10737418240",
                                                                   "volumeShareable": False,
                                                                   "permanent": False}]
                                            }
                             },

                            {'name': 'dvSwitch_07_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'Cluster_177_178_179', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto",
                                                                                     'isEnabled': 'true',
                                                                                     'connectionId': 3
                                                                                     }
                                                                                    ],
                                                                   'id': 1,
                                                                   'volumeUri': 'SVOL:svol3'}]}
                             },

                            {'name': 'Cluster_180_181_182_SPT', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_netset1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_netset2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto",
                                                                                     'isEnabled': 'true',
                                                                                     'connectionId': 3
                                                                                     }
                                                                                    ],
                                                                   'id': 1,
                                                                   'volumeUri': 'SVOL:svol6'
                                                                   },
                                                                  {'lunType': 'Auto',
                                                                   'storagePaths': [{"targetSelector": "Auto",
                                                                                     'isEnabled': 'true',
                                                                                     'connectionId': 3
                                                                                     }
                                                                                    ],
                                                                   'id': 2,
                                                                   'volumeUri': 'SVOL:svol1'
                                                                   }
                                                                  ]
                                            }
                             },

                            {'name': 'vSwitch_01_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'dvSwitch_01_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_02_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'dvSwitch_02_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'profile_template_vsa', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 6, "name": "iscsi_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:iSCSI'}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             },

                            {'name': 'SPT_vsa_multi_iSCSI', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "iscsi_conn1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:iSCSI"},
                                                                    {"id": 5, "name": "iscsi_conn2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:iSCSI"},
                                                                    {"id": 6, "name": "iscsi_conn3", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:iSCSI'}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             },

                            {'name': 'SPT_vsa_netset_iSCSI', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "netset3_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "NS:netset3"}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}
                             }
                            ]

# ####################################
ipv4_subnet = [{'type': 'Subnet',
                'networkId': '15.146.152.0',
                'subnetmask': '255.255.248.0',
                'gateway': '15.146.152.1',
                'dnsServers': ['16.110.135.51',
                               '16.110.135.52'],
                'domain': 'hpe.com'},
               {'type': 'Subnet',
                'networkId': '172.18.0.0',
                'subnetmask': '255.255.248.0',
                'gateway': '172.18.0.1',
                'dnsServers': ['16.110.135.51', '16.110.135.51'],
                'domain': 'hpe.com'
                }
               ]

ipv4_ranges = [{'type': 'Range', 'name': 'IPV4', 'startAddress': '15.146.152.2', 'endAddress': '15.146.152.99', 'subnetUri': '15.146.152.0'},
               {'type': 'Range', 'name': 'IPV4_iSCSI', 'startAddress': '172.18.0.11', 'endAddress': '172.18.0.99', 'subnetUri': '172.18.0.0'}
               ]

subnet_association = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'subnetUri': '15.146.152.0'},
                      {'network type': 'ethernet-networkV300', 'name': 'iSCSI', 'subnetUri': '172.18.0.0'}
                      ]

# #####################################
deployment_managers = [{'username': 'dcs', 'password': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

# #####################################
update_deployment_managers = [{'name': '172.18.9.1', 'port': '444'}]

# #####################################
expected_deployment_managers = [{'username': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

# #####################################
vcenter = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443'}]

# #####################################
update_vcenter = [{'type': 'HypervisorManager', 'name': '172.18.13.11', 'username': 'dcs', 'password': 'dcs', 'port': '443', 'version': '5.1.0', 'virtualSwitchType': 'Distributed', 'multiNicVMotion': 'false', 'distributedSwitchUsage': 'GeneralNetworks', 'distributedSwitchVersion': '5.1.0', 'hypervisor_type': 'Vmware'}]

# #####################################  Hypervisor Cluster Profile ##########################################
cluster_10 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_10', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}
              ]

cluster_10_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_10', 'new_name': 'Cluster_10_updated'}]

cluster_30 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_30', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 8', 'Encl1, bay 11'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

vSwitch_01 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_01', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_01_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 12'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_03 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_03', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_03_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 13'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_04 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_04', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 14'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

dvSwitch_01 = [{'type': 'HypervisorClusterProfile', 'name': 'dvSwitch_01', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_01_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 15'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

cluster_113_v4 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v4', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 16'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

cluster_113_v4_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v4', 'server_hardware': ['Encl1, bay 12']}
                         ]

Cluster_113_v5 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v5', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 13'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

Cluster_113_v5_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v5',
                          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                          'server_hardware': ['Encl2, bay 14']}
                         ]

Cluster_113_v6 = [{'type': 'HypervisorClusterProfile', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 15'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

Cluster_113_v6_update = [{'type': 'HypervisorClusterProfile', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '172.18.13.11',
                          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                          'server_hardware': ['Encl2, bay 12']}
                         ]

Cluster_113_v1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v1', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3', 'Encl1, bay 4'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

Cluster_113_v1_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v1', 'HostProfileUris': ['Encl1, bay 3']}
                         ]

Cluster_113_v2 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v2', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

Cluster_113_v2_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v2', 'HostProfileUris': ['Encl1, bay 5']}
                         ]

Cluster_113_v3 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v3', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 7', 'Encl1, bay 8'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

Cluster_113_v3_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_113_v3', 'HostProfileUris': ['Encl1, bay 7']}
                         ]

Cluster_1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_1', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'IPV4', 'network': 'corp'}
             ]

Cluster_3 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_3', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_28 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_28', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 7'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

Cluster_22 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_22', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'}, 'server_hardware': ['Encl1, bay 4'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

Cluster_26 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_26', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_nomgmt', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp'}
              ]

Cluster_27 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_27', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 4'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_31 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_31', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

cluster_31_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_31', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6']}
                     ]

Cluster_11 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_11', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}
              ]

cluster_11_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_11', 'path': 'Invalid_DC/host'}
                     ]

Host_07 = [{'type': 'HypervisorClusterProfile', 'name': 'Host_07', 'path': 'DC1', 'vcenter': '172.18.13.11',
            'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
            'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
            'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 16'],
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
           ]

Host_07_update = [{'type': 'HypervisorClusterProfile', 'name': 'Host_07', 'hhp_settings': {'hhp_name': 'Host_07', 'host_name': 'new_host'}}]

Cluster_129 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_129', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}
               ]

Cluster_133 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true',
                                     'haEnabled': 'false'}}
               ]

Cluster_133_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_133',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false',
                                            'haEnabled': 'true'}}
                      ]

SM_09 = [{'type': 'HypervisorClusterProfile', 'name': 'SM_09', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 12'],
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
         ]

Cluster_43 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_43', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'Cluster_43_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 8'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
               'shared_volume': [{'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}
              ]

cluster_128 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_128', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 12'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_134 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_134', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 12'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_135 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_135', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 12'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_136 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_136', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 12'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_18 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_18', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 7'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_107 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_107', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_108 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_108_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'HostProfileUris': ['Encl1, bay 3'],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

Cluster_109 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_109_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

Cluster_29 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_29_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '172.18.13.11',
                      'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',
                      'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                      'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                     ]

Hosts_04 = [{'type': 'HypervisorClusterProfile', 'name': 'Hosts_04', 'path': 'DC1', 'vcenter': '172.18.13.11',
             'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
             'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
             'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
             'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
            ]

Cluster_177 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_177', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_177_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_177', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'], 'HostProfileUris': ['Encl1, bay 3']}
                      ]

cluster_178 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_178', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

cluster_178_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_178', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'], 'HostProfileUris': ['Encl1, bay 3']}
                      ]

cluster_179 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_179', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

cluster_179_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_179', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'],
                       'HostProfileUris': ['Encl1, bay 3']}
                      ]

Cluster_21 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_21', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 12'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_21_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_21', 'hhp_settings': {'power_state': 'Off'}}
                     ]

cluster_130 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_130', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false',
                                     'haEnabled': 'false'}}
               ]

cluster_131 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_131', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true',
                                     'haEnabled': 'true'}}
               ]

cluster_132 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_132', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

cluster_133 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}
               ]

cluster_133_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'false'}}
                      ]

cluster_14 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_14', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 7'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_14_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_14', 'profile_name': 'profile_template_gen8_1_1'}
                     ]

cluster_16 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_16', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'NULL', 'network': 'corp', 'server_hardware': ["NULL"],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_180 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_180', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}, {'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_180_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_180', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'],
                       'HostProfileUris': ['Encl1, bay 3']}
                      ]

cluster_181 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_181', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}, {'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_181_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_181', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'],
                       'HostProfileUris': ['Encl1, bay 3']}
                      ]

cluster_182 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_182', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 3'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'svol1', 'volumeFileSystemType': 'VMFS'},
                                  {'name': 'svol6', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_182_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_182', 'server_hardware': ['Encl1, bay 5', 'Encl1, bay 6'],
                       'HostProfileUris': ['Encl1, bay 3']}
                      ]

cluster_183 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_183', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]
cluster_183_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_183', 'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false'}}]

cluster_183_update1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_183', 'server_hardware': ['Encl1, bay 4']}]

cluster_15 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_15', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl1, bay 7'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_15_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_15',
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
                     ]

Host_06 = [{'type': 'HypervisorClusterProfile', 'name': 'Host_06', 'path': 'DC1', 'vcenter': '172.18.13.11',
            'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 13'],
            'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
           ]

Host_06_update = [{'type': 'HypervisorClusterProfile', 'name': 'Host_06', 'hhp_settings': {'redeploy': 'true'}}
                  ]

Cluster_91 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_91', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_91_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_91', 'deployment_uri': '/rest/os-deployment-build-plans/780001'}
                     ]

Cluster_92 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_92', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 11'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_92_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_92', 'deployment_uri': '/rest/os-deployment-build-plans/780001'}
                     ]

Cluster_2 = [{'type': '', 'name': 'Cluster_2', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_34 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_34', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 8'],
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_36 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_36', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_36_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_36', 'server_hardware': ['NONE']}
                     ]

Cluster_37 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_37', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_37_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_37', 'profile_name': 'Non-existingProfile', 'server_hardware': ['Encl1, bay 11']}
                     ]

Cluster_38 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_38', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_38_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_38', 'server_hardware': ['Encl1, bay 11'], 'deployment_uri': '/rest/os-deployment-build-plans/80000123456'}
                     ]

Cluster_39 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_39', 'path': 'DC1', 'vcenter': '172.18.13.00',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 8'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]
Cluster_4 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_4', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 8'],
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'NULL', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]
Cluster_40 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_40', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 8'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'NonStandard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_41 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_41', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'hypervisor_type': 'Vmware', 'deployment_uri': '/rest/os-deployment-build-plans/800001',
               'server_password': 'iso*help', 'ip_pool': 'IPV4', 'network': 'corp'}
              ]

Cluster_42 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_42', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'server_password': 'iso*help', 'ip_pool': 'IPV4', 'network': 'corp'}
              ]

Cluster_5 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_5', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['NULL'],
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'IPV4', 'network': 'corp'}
             ]

Cluster_50 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_50', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 7'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001_11', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp'}
              ]

Cluster_12 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp'}
              ]

Cluster_12_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '172.18.13.11',
                      'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
                      'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                      'ip_pool': 'IPV4', 'network': 'corp'}
                     ]

Cluster_173 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_173', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp'}
               ]

Cluster_184 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp'}
               ]

Cluster_184_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184_new',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp'}
                      ]

Cluster_193 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_193', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'network': 'corp'}
               ]

Cluster_6 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_6', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard_1', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_9 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_9', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'ip_pool': 'IPV4', 'network': 'corp'}
             ]

cluster_88 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_88', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'None', 'haEnabled': 'NULL'}}
              ]

cluster_89 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_89', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks_1', 'distributed_switch_version': '5.1.0'}}
              ]

cluster_17 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_17', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen8111', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

Cluster_140 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_140', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 14'],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_140_update_1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_140_update_2 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_140_update_3 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_141 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_141', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 15'],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_141_update_1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_141_update_2 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'InMaintenance'}}
                        ]

Cluster_141_update_3 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

Cluster_141_update_4 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_142 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_142', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 15'],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_142_update_1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_142_update_2 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_142_update_3 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

Cluster_143 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_143', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 15'],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_143_update_1 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_143_update_2 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_143_update_3 = [{
                        'type': 'HypervisorClusterProfile', 'name': 'Cluster_143',
                        'hhp_settings': {'power_state': 'InMaintenance'}}
                        ]

Cluster_143_update_4 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

vCenter_1 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
             ]

vCenter_1_update = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
                     'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
                     'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                    ]

vCenter_38 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
              ]

vCenter_10 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
              ]

vCenter_10_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_10', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_2 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.1211', 'port': '443', 'version': '5.1.0'}
             ]

vCenter_3 = [{'username': 'dcs1234', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
             ]

vCenter_4 = [{'username': 'dcs', 'password': 'dcs123', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
             ]

vCenter_5 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '', 'port': '443', 'version': '5.1.0'}
             ]

vCenter_46 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager_012', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
              ]

vCenter_34_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_34', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 3'],
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_35_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 3'],
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_35_cluster_update = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '172.18.13.11',
                              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'HostProfileUris': ['Encl1, bay 3'],
                              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                              'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                             ]

vCenter_36_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_36_cluster_update = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '172.18.13.11',
                              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['Encl1, bay 3'],
                              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                              'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                             ]

vCenter_37_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_37', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_38 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}
              ]

vCenter_38_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'vCenter_38', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'ip_pool': 'IPV4', 'network': 'corp'}
                      ]

vCenter_6 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
              'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '', 'distributedSwitchUsage': 'GeneralNetworks',
              'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
             ]

vCenter_14 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
              ]

vCenter_14_update = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
                      'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
                      'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                     ]

vCenter_16 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}
              ]

vCenter_17 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}
              ]

ICSP_14_cluster = [{'type': 'HypervisorClusterProfile', 'name': 'ICSP_14_cluster', 'path': 'DC1', 'vcenter': '172.18.13.11',
                    'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                    'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                    'ip_pool': 'IPV4', 'network': 'corp'}
                   ]

ICSPAltair_4 = [{'username': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}
                ]

ICSPAltair_3 = [{'username': 'wronguser', 'password': 'wrongpassword', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}
                ]

ICSPAltair_2 = [{'username': 'dcs', 'password': 'dcs', 'type': 'DeploymentManager', 'name': 'wrong_name', 'port': '443'}
                ]

cluster_103 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_103', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 8'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'true'}}
               ]

cluster_104 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_104', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 13'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

cluster_106 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_106', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 12'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

cluster_105 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_105', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp', 'server_hardware': ['Encl2, bay 11'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

vSwitch_08 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_08', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_08_update = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_08', 'server_hardware': ['Encl2, bay 7']}
                     ]

vSwitch_09 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_09', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_09_update = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_09', 'server_hardware': ['Encl2, bay 8']}
                     ]

dvSwitch_05 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_05', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

dvSwitch_05_update = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_05', 'server_hardware': ['Encl2, bay 4']}
                      ]

dvSwitch_06 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_06', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

dvSwitch_06_update = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_06', 'server_hardware': ['Encl2, bay 4']}
                      ]

vSwitch_02 = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_02', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_02_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_02_update = [{'type': 'HypervisorClusterProfile', 'name': 'vSwitch_02', 'server_hardware': ['Encl2, bay 5']}
                     ]

dvSwitch_02 = [{'type': 'HypervisorClusterProfile', 'name': 'dvSwitch_02', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

dvSwitch_02_update = [{'type': 'HypervisorClusterProfile', 'name': 'dvSwitch_02', 'server_hardware': ['Encl2, bay 6']}
                      ]

dvSwitch_07 = [{'type': 'HypervisorClusterProfile', 'name': 'dvSwitch_07', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

dvSwitch_07_update = [{'type': 'HypervisorClusterProfile', 'name': 'dvSwitch_07', 'server_hardware': ['Encl2, bay 11']}
                      ]

cls46_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_cls46'},
                    {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_cls46'}
                    ]

cls46_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_cls46'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_cls46'}
                    ]

Cluster_vc_46 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_46 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_46', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp_cls46', 'server_hardware': ['Encl1, bay 5']}
              ]

cls47_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_cls47'},
                    {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_cls47'}
                    ]

cls47_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_cls47'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_cls47'}
                    ]

# As per test case vCenter version should be 5.5.0  Due to limitation in DCS Oneview build(supporting only 5.1.0), Registering vCenter of version 5.1.0
Cluster_vc_47 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_47 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_47', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp_cls47', 'server_hardware': ['Encl1, bay 4']}
              ]

cls48_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_cls48'},
                    {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_cls48'}
                    ]

cls48_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_cls48'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_cls48'}
                    ]

Cluster_vc_48 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_48 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_48', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp_cls48', 'server_hardware': ['Encl1, bay 8']}
              ]

cls49_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_cls49'},
                    {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_cls49'}
                    ]

cls49_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_cls49'},
                    {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_cls49'}
                    ]

Cluster_vc_49 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_49 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_49', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'ip_pool': 'IPV4', 'network': 'corp_cls49'}
              ]

Cluster_49_update = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_49', 'server_hardware': ['Encl1, bay 6']}
                     ]

cls111_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_cls111'},
                     {'network type': 'ethernet-networkV300', 'name': 'net1', 'new_name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV300', 'name': 'corp1', 'new_name': 'corp1_cls111'}
                     ]

cls111_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_cls111'},
                     {'network type': 'ethernet-networkV300', 'new_name': 'net1', 'name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV300', 'new_name': 'corp1', 'name': 'corp1_cls111'}
                     ]

Cluster_vc_111 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManager', 'name': '172.18.13.11', 'version': '5.1.0',
                   'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                   'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                  ]

Cluster_111 = [{'type': 'HypervisorClusterProfile', 'name': 'Cluster_111', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'ip_pool': 'IPV4', 'network': 'corp_cls111', 'server_hardware': ['Encl2, bay 13'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'},
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'true', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'}}
               ]

sm06_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_sm06'},
                   {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_sm06'}
                   ]

sm06_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_sm06'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_sm06'}
                   ]

SM_06 = [{'type': 'HypervisorClusterProfile', 'name': 'SM_06', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'ip_pool': 'IPV4', 'network': 'corp_sm06',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.0'}}
         ]

sm07_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_sm07'},
                   {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_sm07'}
                   ]

sm07_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_sm07'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_sm07'}
                   ]

SM_07 = [{'type': 'HypervisorClusterProfile', 'name': 'SM_07', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'ip_pool': 'IPV4', 'network': 'corp_sm07',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.1.0'}}
         ]

sm08_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_sm08'},
                   {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_sm08'}
                   ]

sm08_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_sm08'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_sm08'}
                   ]

SM_08 = [{'type': 'HypervisorClusterProfile', 'name': 'SM_08', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'ip_pool': 'IPV4', 'network': 'corp_sm08',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.0.0'}}
         ]

sm10_net_edit_1 = [{'network type': 'ethernet-networkV300', 'name': 'corp', 'new_name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV300', 'name': 'icsp', 'new_name': 'icsp_sm10'},
                   {'network type': 'ethernet-networkV300', 'name': 'production', 'new_name': 'production_sm10'}
                   ]

sm10_net_edit_2 = [{'network type': 'ethernet-networkV300', 'new_name': 'corp', 'name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'icsp', 'name': 'icsp_sm10'},
                   {'network type': 'ethernet-networkV300', 'new_name': 'production', 'name': 'production_sm10'}
                   ]

SM_10 = [{'type': 'HypervisorClusterProfile', 'name': 'SM_10', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'ip_pool': 'IPV4', 'network': 'corp_sm10',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.5.0'}}
         ]

# iSCSI_Vol_2 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_2', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                 }
#                ]
#
# iSCSI_Vol_2_update = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_2', 'server_hardware': ['Encl1, bay 4']}
#                       ]
#
# iSCSI_Vol_4 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_4', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}
#                 }
#                ]
#
# iSCSI_Vol_4_update = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_4', 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]}
#                       ]
#
# iSCSI_Vol_5 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_5', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                 }
#                ]
#
# iSCSI_Vol_5_update = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_5', 'shared_volume': [{'name': 'vsa1', 'requestedCapacity': 10000000}]}
#                       ]
#
# iSCSI_Vol_6 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_6', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                 }
#                ]
#
# iSCSI_Vol_6_update = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_6', 'del_shared_volume': ['vsa1']}
#                       ]
#
# iSCSI_Vol_7 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_7', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3', 'Encl1, bay 4'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                 }
#                ]
#
# iSCSI_Vol_7_update = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_7', 'HostProfileUris': ['Encl1, bay 3']}
#                       ]
#
# iSCSI_Vol_8 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_8', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3', 'Encl1, bay 4'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                 }
#                ]
#
# iSCSI_Vol_8_update = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_8', 'HostProfileUris': ['Encl1, bay 3', 'Encl1, bay 4']}
#                       ]
#
# iSCSI_Vol_9 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_9', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                 'server_hardware': ['Encl1, bay 3'],
#                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                 }
#                ]
#
# iSCSI_Vol_18 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_18', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                  'profile_name': 'SPT_vsa_multi_iSCSI', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                  'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                  'server_hardware': ['Encl1, bay 3'],
#                  'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                       'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                  'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                  }
#                 ]
#
# iSCSI_Vol_21 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_21', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                  'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                  'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                  'server_hardware': ['Encl1, bay 3'],
#                  'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                       'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                  'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                  }
#                 ]
#
# iSCSI_Vol_22 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_22', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                  'profile_name': 'SPT_vsa_netset_iSCSI', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                  'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                  'server_hardware': ['Encl1, bay 3'],
#                  'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                       'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                  'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                  }
#                 ]
#
# iSCSI_Vol_23 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_23', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                  'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                  'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                  'server_hardware': ['Encl1, bay 3'],
#                  'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
#                  'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                  }
#                 ]
#
# iSCSI_Vol_24 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_24', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                  'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                  'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                  'server_hardware': ['Encl1, bay 3'],
#                  'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                       'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
#                  'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                  }
#                 ]
#
# iSCSI_Vol_25 = [{'type': 'HypervisorClusterProfile', 'name': 'iSCSI_Vol_25', 'path': 'DC1', 'vcenter': '172.18.13.11',
#                  'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware', 'ip_pool': 'IPV4', 'network': 'corp',
#                  'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
#                  'server_hardware': ['Encl1, bay 3'],
#                  'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
#                                       'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
#                  'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
#                  }
#                 ]

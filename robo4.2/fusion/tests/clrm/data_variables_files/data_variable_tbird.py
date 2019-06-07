# #####################################s
admin_credentials = {'userName': 'Administrator', 'password': ''}

# #####################################

# #########PREREQUISITES###############
ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'mgmt_net', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '80', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '21', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '22', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '34', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'untagged_nw', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '33', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '10', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '23', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '24', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '101', 'purpose': 'General'}
                     ]

fc_networks = [{'fabricType': 'DirectAttach', 'name': 'san_da', 'autoLoginRedistribution': True, 'linkStabilityTime': 30, 'connectionTemplateUri': None, 'type': 'fc-networkV4'},
               {'fabricType': 'FabricAttach', 'name': 'san', 'autoLoginRedistribution': True, 'linkStabilityTime': 30, 'connectionTemplateUri': None, 'type': 'fc-networkV4'}
               ]

network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1'], 'nativeNetworkUri': 'net1'},
                {'name': 'netset2', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1', 'production'], 'nativeNetworkUri': 'net1'}]

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
        'SGH537YCESosureType': 'C7000',
        'interconnectMapTemplate': [{'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'SGH537YCESosureIndex': 1},
                                    {'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'SGH537YCESosureIndex': 1}
                                    ],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink2'].copy(), uplink_sets['uplink3'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net2', 'corp1', 'net1', 'network2', 'untagged_nw', 'tunneled_nw', 'production']
        }

enc_groups = {'name': 'EG',
              'type': 'SGH537YCESosureGroupV400',
              'SGH537YCESosureCount': 1,
              'SGH537YCESosureTypeUri': '/rest/SGH537YCESosure-types/c7000',
              'stackingMode': 'SGH537YCESosure',
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

enclosures = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:EG', 'force': True, 'licensingIntent': 'OneViewNoiLO'},
              {'hostname': "172.18.1.13", 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:EG', 'force': True, 'licensingIntent': 'OneViewNoiLO'}
              ]

storage_systems = [{'family': 'StoreServ', 'name': 'ThreePAR7200-5252', 'hostname': '172.18.11.12', 'credentials': {'username': 'dcs', 'password': 'dcs'}}
                   ]

update_storage_systems = [{'type': 'StorageSystemV4', 'name': 'ThreePAR7200-5252', 'family': 'StoreServ',
                           "hostname": '172.18.11.12', 'credentials': {'username': 'dcs', 'password': 'dcs'},
                           "deviceSpecificAttributes": {"managedDomain": "TestDomain"
                                                        },
                           "ports": [{"expectedNetworkUri": "FC:san",
                                      "expectedNetworkName": "san",
                                      "mode": "Managed"
                                      }, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
                           }
                          ]

storage_pools = [{"storageSystemUri": "ThreePAR7200-5252", "name": "cpg-growth-limit-1TiB", "isManaged": True}
                 ]

storage_volumes = [{"properties": {"name": "svol1", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol2", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol3", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol4", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol5", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol6", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True}
                   ]

server_profile_templates = [{"name": "profile_template_gen9_1", "type": "ServerProfileTemplateV3", "serverProfileDescription": "", "serverHardwareTypeUri": "SHT:SY 480 Gen9 1", "enclosureGroupUri": "EG:EG", "serialNumberType": "Virtual", "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                            'connectionSettings': {'manageConnections': True,
                                                   "connections": [{"id": 1, "name": "corp_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "ETH:corp"},
                                                                   {"id": 2, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                   {"id": 3, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "ETH:ft_net"}
                                                                   ]},
                             "boot": {"manageBoot": True, "order": ["HardDisk"]},
                             "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False, "firmwareInstallType": None},
                             "bios": {"manageBios": False, "overriddenSettings": []},
                             "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                             "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": False, "volumeAttachments": []}
                             },
                            {'name': 'profile_gen91_san', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "ETH:ft_net"}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": False, "volumeAttachments": []},
                             },

                            {'name': 'profile_template_gen9_1_1', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_ft', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_03_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_untagged', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:untagged_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'profile_nomgmt', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_tunnel', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:tunneled_nw', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_04_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'netset2_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_tunneled', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:tunneled_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_netset2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'dvSwitch_05_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'netset2_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_tunneled', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:tunneled_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_netset2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'Cluster_43_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_ft', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },
                            {'name': 'dvSwitch_07_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },
                            {'name': 'Cluster_177_178_179', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'Cluster_180_181_182_SPT', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_netset2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_01_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_corp', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'dvSwitch_01_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_corp', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_netset2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'vSwitch_02_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },

                            {'name': 'dvSwitch_02_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             },
                            {'name': 'vSwitch_06_SP', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '2 management network ', 'serverHardwareTypeUri': 'SHT:SY 660 Gen9 1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_mgmt', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_corp', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Mezz 6:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['HardDisk']},
                             'bootMode': {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                             }
                            ]

# ####################################
ipv4_subnet = [{'type': 'Subnet',
                'networkId': '15.146.152.0',
                'subnetmask': '255.255.248.0',
                'gateway': '15.146.152.1',
                'dnsServers': ['16.110.135.51',
                               '16.110.135.52'],
                'domain': 'hpe.com'}
               ]

ipv4_ranges = [{'type': 'Range', 'name': 'IPV4', 'startAddress': '15.146.152.2', 'endAddress': '15.146.152.99', 'subnetUri': ''}]

# #####################################
deployment_managers = [{'username': 'Administrator', 'password': 'Admin123', 'type': 'DeploymentManager', 'name': '15.212.171.100', 'port': '443'}]

# #####################################
update_deployment_managers = [{'name': '15.212.171.100', 'port': '444'}]

# #####################################
expected_deployment_managers = [{'username': 'Administrator', 'type': 'DeploymentManager', 'name': '15.212.171.100', 'port': '443'}]

# #####################################
vcenter = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443'}]

# #####################################
update_vcenter = [{'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'port': '443', 'version': '6.0.0', 'virtualSwitchType': 'Distributed', 'multiNicVMotion': 'false', 'distributedSwitchUsage': 'GeneralNetworks', 'distributedSwitchVersion': '5.1.0', 'hypervisor_type': 'Vmware'}]

# #####################################  Hypervisor Cluster Profile ##########################################

os_deployment_plan = '/rest/os-deployment-plans/03e5120d-152e-44d8-8db9-759ce1d85e35'
Cluster_10 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_10', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
              ]

cluster_10_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_10', 'new_name': 'Cluster_10_updated'}]

cluster_30 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_30', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 3',
                                   'SGH537YCES, bay 4'],
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                   'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

vSwitch_01 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_01', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'vSwitch_01_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 1'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]
vSwitch_03 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_03', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'vSwitch_03_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 1'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_04', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 1'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

dvSwitch_01 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_01', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'dvSwitch_01_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 1'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

cluster_113_v4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v4', 'path': 'DC1', 'vcenter': '15.212.172.200',
                   'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                   'server_hardware': ['SGH537YCES, bay 4'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

cluster_113_v4_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v4', 'server_hardware': ['SGH537YCES, bay 9']}
                         ]

Cluster_113_v5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v5', 'path': 'DC1', 'vcenter': '15.212.172.200',
                   'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                   'server_hardware': ['SGH537YCES, bay 6'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

Cluster_113_v5_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v5',
                          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                          'server_hardware': ['SGH537YCES, bay 9']}
                         ]

Cluster_113_v6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '15.212.172.200',
                   'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                   'server_hardware': ['SGH537YCES, bay 4'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

Cluster_113_v6_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '15.212.172.200',
                          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                          'server_hardware': ['SGH537YCES, bay 9']}
                         ]

Cluster_113_v1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v1', 'path': 'DC1', 'vcenter': '15.212.172.200',
                   'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 3'],
                   'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

Cluster_113_v1_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v1', 'HostProfileUris': ['SGH537YCES, bay 3']}
                         ]

Cluster_113_v2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v2', 'path': 'DC1', 'vcenter': '15.212.172.200',
                   'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                   'server_hardware': ['SGH537YCES, bay 6'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
                  ]

Cluster_113_v2_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v2', 'HostProfileUris': ['SGH537YCES, bay 6']}
                         ]

Cluster_113_v3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v3', 'path': 'DC1', 'vcenter': '15.212.172.200',
                   'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                   'server_hardware': ['SGH537YCES, bay 9'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

Cluster_113_v3_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v3', 'HostProfileUris': ['SGH537YCES, bay 9']}
                         ]

Cluster_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_1', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'
              }
             ]

Cluster_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_3', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
              'server_hardware': ['SGH537YCES, bay 4'],
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_28 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_28', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 3'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

Cluster_22 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_22', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'}, 'server_hardware': ['SGH537YCES, bay 6'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

Cluster_26 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_26', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_nomgmt', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
              ]

Cluster_27 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_27', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 6'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_31 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_31', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

cluster_31_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_31', 'server_hardware': ['SGH537YCES, bay 4', 'SGH537YCES, bay 6']}
                     ]

Cluster_11 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_11', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
              ]

cluster_11_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_11', 'path': 'Invalid_DC/host'}
                     ]

Host_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_07', 'path': 'DC1', 'vcenter': '15.212.172.200',
            'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
            'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
            'server_hardware': ['SGH537YCES, bay 9'],
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
           ]

Host_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_07', 'hhp_settings': {'hhp_name': 'Host_07', 'host_name': 'new_host'}}]

Cluster_129 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_129', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}
               ]

Cluster_133 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true',
                                     'haEnabled': 'false'}}
               ]

Cluster_133_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false',
                                            'haEnabled': 'true'}}
                      ]

SM_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_09', 'path': 'DC1', 'vcenter': '15.212.172.200',
          'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
          'server_hardware': ['SGH537YCES, bay 3'],
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
         ]

Cluster_43 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_43', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'Cluster_43_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 10'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
               }]

cluster_128 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_128', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_134 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_134', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_135 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_135', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 6'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_136 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_136', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_18 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_18', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 3'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_107 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_107', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_108 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_108_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'HostProfileUris': ['SGH537YCES, bay 6'],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

Cluster_109 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_109_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'server_hardware': ['SGH537YCES, bay 3'],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

Cluster_29 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 4'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_29_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '15.212.172.200',
                      'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
                      'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                      'server_hardware': ['SGH537YCES, bay 3'],
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                     ]

Hosts_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Hosts_04', 'path': 'DC1', 'vcenter': '15.212.172.200',
             'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
             'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
             'server_hardware': ['SGH537YCES, bay 3'],
             'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
            ]

Cluster_177 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_177', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 3'],
                ''' 'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}], '''
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_177_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_177', 'server_hardware': ['SGH537YCES, bay 4'], 'HostProfileUris': ['SGH537YCES, bay 3']}
                      ]

cluster_178 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_178', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                ''' 'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],'''
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

cluster_178_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_178', 'server_hardware': ['SGH537YCES, bay 6'], 'HostProfileUris': ['SGH537YCES, bay 4']}
                      ]

cluster_179 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_179', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 6'],
                ''' 'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],'''
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

cluster_179_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_179', 'server_hardware': ['SGH537YCES, bay 9'],
                       'HostProfileUris': ['SGH537YCES, bay 6']}
                      ]

Cluster_21 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_21', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 4'],
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_21_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_21', 'hhp_settings': {'power_state': 'Off'}}
                     ]

cluster_130 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_130', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false',
                                     'haEnabled': 'false'}}
               ]

cluster_131 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_131', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true',
                                     'haEnabled': 'true'}}
               ]

cluster_132 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_132', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

cluster_133 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}
               ]

cluster_133_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'false'}}
                      ]

cluster_14 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_14', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 6'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_14_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_14', 'profile_name': 'profile_template_gen9_1_1'}
                     ]

cluster_16 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_16', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ["NULL"],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_180 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_180', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
                }
               ]

cluster_180_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_180', 'server_hardware': ['SGH537YCES, bay 6'],
                       'HostProfileUris': ['SGH537YCES, bay 4']}
                      ]

cluster_181 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_181', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 3'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}
                }
               ]

cluster_181_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_181', 'server_hardware': ['SGH537YCES, bay 4'],
                       'HostProfileUris': ['SGH537YCES, bay 3']}
                      ]

cluster_182 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_182', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 6'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}
                }
               ]

cluster_182_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_182', 'server_hardware': ['SGH537YCES, bay 6'],
                       'HostProfileUris': ['SGH537YCES, bay 6']}
                      ]

cluster_183 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]
cluster_183_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false'}}]

cluster_183_update1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'server_hardware': ['SGH537YCES, bay 3']}]

cluster_15 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_15', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 4'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_15_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_15',
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
                     ]

Host_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_06', 'path': 'DC1', 'vcenter': '15.212.172.200',
            'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 6'],
            'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
           ]

Host_06_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_06', 'hhp_settings': {'redeploy': 'true'}}
                  ]

Cluster_91 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_91', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_91_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_91', 'deployment_uri': '/rest/os-deployment-build-plans/780001'}
                     ]

Cluster_92 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_92', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 6'],
               'deployment_uri': '/rest/os-deployment-plans/37352aa5-7d24-4655-aad5-a8d65cd36ee6', 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_92_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_92', 'deployment_uri': '/rest/os-deployment-plans/37352aa5-7d24-4655-aad5-a8d65cd36ee6'}
                     ]

Cluster_2 = [{'type': '', 'name': 'Cluster_2', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_34 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_34', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 9'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_36 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_36', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_36_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_36', 'server_hardware': ['NONE']}
                     ]

Cluster_37 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_37', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_37_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_37', 'profile_name': 'Non-existingProfile', 'server_hardware': ['SGH537YCES, bay 9']}
                     ]

Cluster_38 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_38', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_38_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_38', 'server_hardware': ['SGH537YCES, bay9'], 'deployment_uri': '/rest/os-deployment-build-plans/80000123456'}
                     ]

Cluster_39 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_39', 'path': 'DC1', 'vcenter': '172.18.13.00',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 3'],
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]
Cluster_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_4', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 4'],
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]
Cluster_40 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_40', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 6'],
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'NonStandard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_41 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_41', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
               'server_password': 'hpVSE123#'}
              ]

Cluster_42 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_42', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'server_password': 'hpVSE123#'}
              ]

Cluster_5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_5', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['NULL'],
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
             ]

Cluster_50 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_50', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 6'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001_11', 'server_password': 'hpVSE123#'}
              ]

Cluster_12 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
              ]

Cluster_12_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '15.212.172.200',
                      'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                      'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
                     ]

Cluster_173 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_173', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
               ]

Cluster_184 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
               ]

Cluster_184_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184_new',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       }
                      ]

Cluster_193 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_193', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
               ]

Cluster_6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_6', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard_1', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_9 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_9', 'path': 'DC1', 'vcenter': '15.212.172.200',
              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'
              }
             ]

cluster_88 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_88', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'None', 'haEnabled': 'NULL'}}
              ]

cluster_89 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_89', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks_1', 'distributed_switch_version': '5.1.0'}}
              ]

cluster_17 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_17', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_gen911', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}
              ]

Cluster_140 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 9'],
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_140_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_140_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_140_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_141 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 3'],
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_141_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_141_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'InMaintenance'}}
                        ]

Cluster_141_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

Cluster_141_update_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_142 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 4'],
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_142_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_142_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_142_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

Cluster_143 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 9'],
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_143_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_143_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_143_update_3 = [{
                        'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143',
                        'hhp_settings': {'power_state': 'InMaintenance'}}
                        ]

Cluster_143_update_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

vCenter_1 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0'}
             ]

vCenter_1_update = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0',
                     'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
                     'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                    ]

vCenter_38 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0'}
              ]

vCenter_10 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0'}
              ]

vCenter_10_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_10', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_2 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '172.18.13.1211', 'port': '443', 'version': '6.0.0'}
             ]


vCenter_3 = [{'username': 'dcs1234', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.173.50', 'port': '443', 'version': '6.0.0'}
             ]

vCenter_4 = [{'username': 'administrator@vsphere.local', 'password': 'dcs123', 'type': 'HypervisorManagerV2', 'name': '15.212.173.50', 'port': '443', 'version': '6.0.0'}
             ]

vCenter_5 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '', 'port': '443', 'version': '6.0.0'}
             ]

vCenter_46 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2_012', 'name': '15.212.173.50', 'port': '443', 'version': '6.0.0'}
              ]

vCenter_34_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_34', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 6'],
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_35_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 9'],
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_35_cluster_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '15.212.172.200',
                              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'HostProfileUris': ['SGH537YCES, bay 3'],
                              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                             ]

vCenter_36_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_36_cluster_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '15.212.172.200',
                              'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['SGH537YCES, bay 4'],
                              'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                             ]

vCenter_37_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_37', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_38 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0'}
              ]

vCenter_38_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_38', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
                      ]

vCenter_6 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0',
              'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '', 'distributedSwitchUsage': 'GeneralNetworks',
              'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
             ]

vCenter_14 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
              ]

vCenter_14_update = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0',
                      'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
                      'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                     ]

vCenter_16 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'port': '443', 'version': '6.0.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}
              ]

vCenter_17 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}
              ]

ICSP_14_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'ICSP_14_cluster', 'path': 'DC1', 'vcenter': '15.212.172.200',
                    'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                    'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
                   ]

ICSPAltair_4 = [{'username': 'Administrator', 'type': 'DeploymentManager', 'name': '15.212.171.100', 'port': '443'}
                ]

ICSPAltair_3 = [{'username': 'wronguser', 'password': 'wrongpassword', 'type': 'DeploymentManager', 'name': '15.212.171.100', 'port': '443'}
                ]

ICSPAltair_2 = [{'username': 'Administrator', 'password': 'password', 'type': 'DeploymentManager', 'name': 'wrong_name', 'port': '443'}
                ]

cluster_103 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_103', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'true'}}
               ]

Cluster_104 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_104', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

Cluster_106 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_106', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 6'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

Cluster_105 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_105', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

vSwitch_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_08', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_08_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_08', 'server_hardware': ['SGH537YCES, bay 1']}
                     ]

vSwitch_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_09', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_09_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_09', 'server_hardware': ['SGH537YCES, bay 1']}
                     ]

dvSwitch_05 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_05', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

dvSwitch_05_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_05', 'server_hardware': ['SGH537YCES, bay 1']}
                      ]

dvSwitch_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_06', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}
               ]

dvSwitch_06_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_06', 'server_hardware': ['SGH537YCES, bay 1']}
                      ]

vSwitch_02 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_02', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'vSwitch_02_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_02_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_02', 'server_hardware': ['SGH537YCES, bay 10']}
                     ]

dvSwitch_02 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_02', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

dvSwitch_02_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_02', 'server_hardware': ['SGH537YCES, bay 10']}
                      ]
dvSwitch_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_07', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

dvSwitch_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_07', 'server_hardware': ['SGH537YCES, bay 1']}
                      ]

cls46_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls46'}
                    ]

cls46_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls46'}
                    ]

Cluster_vc_46 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'version': '6.0.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_46 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_46', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 4']}
              ]

cls47_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls47'}
                    ]

cls47_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls47'}
                    ]

# As per test case vCenter version should be 5.5.0  Due to limitation in DCS Oneview build(supporting only 5.1.0), Registering vCenter of version 5.1.0
Cluster_vc_47 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@3123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'version': '6.0.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_47 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_47', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 9']}
              ]

cls48_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls48'}
                    ]

cls48_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls48'}
                    ]

Cluster_vc_48 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'version': '6.0.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_48 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_48', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 6']}
              ]

cls49_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls49'}
                    ]

cls49_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls49'}
                    ]

Cluster_vc_49 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'version': '6.0.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_49 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_49', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#'}
              ]

Cluster_49_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_49', 'server_hardware': ['SGH537YCES, bay 9']}
                     ]

cls111_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'net1', 'new_name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'corp1', 'new_name': 'corp1_cls111'}
                     ]

cls111_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'net1', 'name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'corp1', 'name': 'corp1_cls111'}
                     ]

Cluster_vc_111 = [{'username': 'administrator@vsphere.local', 'password': 'Orion!@#123', 'type': 'HypervisorManagerV2', 'name': '15.212.172.200', 'version': '6.0.0',
                   'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                   'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                  ]

Cluster_111 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_111', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 1'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'},
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'true', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'}}
               ]

sm06_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm06'}
                   ]

sm06_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm06'}
                   ]

SM_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_06', 'path': 'DC1', 'vcenter': '15.212.172.200',
          'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.0'}}
         ]

sm07_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm07'}
                   ]

sm07_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm07'}
                   ]

SM_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_07', 'path': 'DC1', 'vcenter': '15.212.172.200',
          'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.1.0'}}
         ]

sm08_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm08'}
                   ]

sm08_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm08'}
                   ]

SM_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_08', 'path': 'DC1', 'vcenter': '15.212.172.200',
          'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.0.0'}}
         ]

sm10_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm10'}
                   ]

sm10_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm10'}
                   ]

SM_10 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_10', 'path': 'DC1', 'vcenter': '15.212.172.200',
          'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.5.0'}}
         ]
'''*************************  New set of cluster *********************************'''
Cluster_13 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_13', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true',
                                    'drsEnabled': 'true', 'haEnabled': 'false'}}]

Cluster_13_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_13',
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true',
                                           'drsEnabled': 'false', 'haEnabled': 'true'}}]

cluster_44 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_44', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 3'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_45 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_45', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 3'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
               }]

vSwitch_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_07', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'vSwitch_01_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_07', 'server_hardware': ['SGH537YCES, bay 1']}]

Cluster_114 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_114', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 6'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_115 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_115', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_gen91_san', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
                }
               ]

cluster_116 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_116', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 3'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
                }
               ]

dvSwitch_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_04', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

dvSwitch_04_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_04', 'server_hardware': ['SGH537YCES, bay 9']}
                      ]

dvSwitch_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_08', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

dvSwitch_08_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_08', 'server_hardware': ['SGH537YCES, bay 9']}
                      ]

dvSwitch_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_09', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'server_hardware': ['SGH537YCES, bay 4'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

dvSwitch_09_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_09', 'server_hardware': ['SGH537YCES, bay 6']}]

cluster_186 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_186', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'mgmtIp_SettingsOverride': {'netmask': '255.255.252.0', 'gateway': '15.212.168.1',
                                            'primaryDns': 'null', 'secondaryDns': 'null'},
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
                }
               ]
cluster_186_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_186',
                       'server_hardware': ['SGH537YCES, bay 4'], 'mgmt_ip':['15.212.171.201']
                       }]

cluster_187 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_187', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_187_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_187', 'path': 'DC1', 'vcenter': '15.212.172.200',
                       'mgmtIp_SettingsOverride': {'netmask': '255.255.252.0', 'gateway': '15.212.168.1',
                                                   'primaryDns': 'null', 'secondaryDns': 'null'},
                       'server_hardware': ['SGH537YCES, bay 4', 'SGH537YCES, bay 6'], 'mgmt_ip':['15.212.171.202', '15.212.171.203']}]

cluster_188 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_188', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'mgmtIp_SettingsOverride': {'netmask': '255.255.252.0', 'gateway': '15.212.168.1',
                                            'primaryDns': '16.110.135.51', 'secondaryDns': '16.110.135.52'},
                'server_hardware': ['SGH537YCES, bay 3'], 'mgmt_ip':['15.212.171.201'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}
                }]

cluster_189 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_189', 'path': 'DC1', 'vcenter': '15.212.172.200',
                'profile_name': 'profile_template_gen9_1_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                'mgmtIp_SettingsOverride': {'netmask': '205.255.252.0', 'gateway': '15.212.168.12',
                                            'primaryDns': '16.110.135.59', 'secondaryDns': '16.110.135.58'},
                'server_hardware': ['SGH537YCES, bay 3'], 'mgmt_ip': ['15.212.171.201'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}
                }
               ]
vSwitch_05 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_05', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'profile_nomgmt', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 10'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

vSwitch_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_06', 'path': 'DC1', 'vcenter': '15.212.172.200',
               'profile_name': 'vSwitch_06_SP', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
               'server_hardware': ['SGH537YCES, bay 1'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

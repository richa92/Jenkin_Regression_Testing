# #####################################
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

# #####################################

# #########PREREQUISITES###############
ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '100', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'mgmt_net', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1060', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1002', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1061', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1062', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1063', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'UnTagged', 'name': 'untagged_nw', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1065', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1066', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1067', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production', 'connectionTemplateUri': None, 'privateNetwork': 'false',
                      'type': 'ethernet-networkV4', 'vlanId': '1066', 'purpose': 'General'}
                     ]

fc_networks = [{'fabricType': 'DirectAttach', 'name': 'san_da', 'autoLoginRedistribution': True, 'linkStabilityTime': 30, 'connectionTemplateUri': None, 'type': 'fc-networkV4'},
               {'fabricType': 'FabricAttach', 'name': 'san', 'autoLoginRedistribution': True, 'linkStabilityTime': 30, 'connectionTemplateUri': None, 'type': 'fc-networkV4'}
               ]

network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1'], 'nativeNetworkUri': 'net1'},
                {'name': 'netset2', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1', 'production'], 'nativeNetworkUri': 'net1'}]

dvs_delete = ['corp__VDS', 'icsp__VDS', 'production__VDS', 'netset2_VDS', 'network2_VDS', 'mgmt_net__VDS', 'net1__VDS', 'tunneled_nw__VDS', 'untagged_nw__VDS',
              'corp1__VDS', 'ft_net__VDS', 'ft_net2__VDS', 'san_da__VDS', 'san__VDS', 'netset1__VDS']

data_center = 'DC1'

uplink_sets = {'uplink1': {'name': 'upl_corp_icsp',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['corp', 'icsp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]
                           },
               'uplink2': {'name': 'upl_san',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkUris': ['san'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]}
               }

ligs = {'name': 'lig',
        'type': 'logical-interconnect-groupV300',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                    {'enclosure': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}
                                    ],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink2'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net2', 'corp1', 'net1', 'network2', 'untagged_nw', 'tunneled_nw', 'production', 'mgmt_net']
        }

enc_groups = {'name': 'enclgrp',
              'enclosureCount': 1,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig'}],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"
              }

enclosures = [{'hostname': '10.0.0.5', 'username': 'Administrator', 'password': 'puls@rwpst1', 'enclosureGroupUri': 'EG:enclgrp',
               'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None}]

storage_systems = [{'family': 'StoreServ', 'name': 'pulsarwpst3par1-srv', 'hostname': '16.125.64.102', 'credentials': {'username': '3paradm', 'password': '3pardata'}}
                   ]

update_storage_systems = [{'type': 'StorageSystemV4', 'name': 'pulsarwpst3par1-srv', 'family': 'StoreServ',
                           "hostname": '16.125.64.102', 'credentials': {'username': '3paradm', 'password': '3pardata'},
                           "deviceSpecificAttributes": {"managedDomain": "Pulsar_Wpst"
                                                        },
                           "ports": [{}, {}, {},
                                     {"expectedNetworkUri": "FC:san",
                                      "expectedNetworkName": "san",
                                      "mode": "Managed"
                                      }, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
                           }
                          ]

storage_pools = [{"name": "orionwpstR0", "storageSystemUri": "pulsarwpst3par1-srv", "isManaged": True}
                 ]

storage_volumes = [{"properties": {"name": "svol1", "description": "", "storagePool": "orionwpstR0", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "orionwpstR0"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol2", "description": "", "storagePool": "orionwpstR0", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "orionwpstR0"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol3", "description": "", "storagePool": "orionwpstR0", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "orionwpstR0"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol4", "description": "", "storagePool": "orionwpstR0", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "orionwpstR0"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol5", "description": "", "storagePool": "orionwpstR0", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "orionwpstR0"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol6", "description": "", "storagePool": "orionwpstR0", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "orionwpstR0"}, "templateUri": "ROOT", "isPermanent": True}
                   ]

server_profile_templates = [{'name': 'profile_template_gen8_1', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san",
                                                                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "gen_8_1_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'profile_gen81_san', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "FC:san", 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "san_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}
                                                                  ]}},

                            {'name': 'profile_template_gen8_1_1', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "gen_8_1_1_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'vSwitch_03_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1, "volume": {"properties":
                                                                                       {"name": "vs3_vol",
                                                                                        "size": 11811160064,
                                                                                        "provisioningType": "Thin",
                                                                                        "isShareable": False,
                                                                                        "storagePool": "SP:orionwpstR0"},
                                                                                       "isPermanent": False,
                                                                                       "templateUri": 'ROOT:orionwpstR0'},
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'profile_nomgmt', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "p_nomgmnt_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'vSwitch_04_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_tunneled', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:tunneled_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "vs4_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 5, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'dvSwitch_05_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "vs5_vol",
                                                                           "size": 10737418240,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'Cluster_43_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "cls43",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]
                                            }
                             },

                            {'name': 'dvSwitch_07_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "dvs7_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'Cluster_177_178_179', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}
                                                                    ]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [
                                                {'id': 1,
                                                 "volume": {
                                                     "properties": {
                                                         "name": "cls177_vol",
                                                         "size": 11811160064,
                                                         "provisioningType": "Thin",
                                                         "isShareable": False,
                                                         "storagePool": "SP:orionwpstR0"},
                                                     "isPermanent": False,
                                                     "templateUri": 'ROOT:orionwpstR0'
                                                 },
                                                 "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                 'isBootVolume': True,
                                                 'lunType': 'Auto',
                                                 'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                 },
                                                {'id': 2,
                                                 "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                 'isBootVolume': False,
                                                 'lunType': 'Auto',
                                                 "volumeUri": "v:svol3",
                                                 'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                 }]}
                             },

                            {'name': 'Cluster_180_181_182_SPT', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_netset1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_netset2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'NS:netset2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': False,
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol6",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   },
                                                                  {'id': 2,
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': False,
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol3",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   },
                                                                  {'id': 3,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "cls180_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }
                                                                  ]
                                            }
                             },

                            {'name': 'vSwitch_01_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_ft1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:ft_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "vs1_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 5, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'dvSwitch_01_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "dvs1_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'vSwitch_02_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "vs2_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },

                            {'name': 'dvSwitch_02_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "dvs2_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             },
                            {'name': 'vSwitch_06_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '2 management network ', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_mgmt', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:mgmt_net', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_ft2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:ft_net2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {'id': 6, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 7, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "vs6_vol",
                                                                           "size": 11811160064,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:orionwpstR0"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:orionwpstR0'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:pulsarwpst3par1-srv",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 5, 'targetSelector': 'Auto', 'targets': []}]
                                                                   }]}
                             }
                            ]
#####################################
ipv4_subnet = [{'type': 'Subnet',
                'networkId': '10.0.0.0',
                'subnetmask': '255.255.0.0',
                'gateway': '10.0.1.6',
                'dnsServers': ['10.0.1.2'],
                'domain': 'ind.hpe.com'}
               ]

ipv4_ranges = [{'type': 'Range', 'name': 'IPV4', 'startAddress': '10.0.100.190', 'endAddress': '10.0.100.200', 'subnetUri': '10.0.0.0'}]

subnet_association = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'subnetUri': '10.0.0.0'}]
# #####################################
deployment_managers = [{'username': 'Administrator', 'password': 'password', 'type': 'DeploymentManager', 'name': '10.0.100.139', 'port': '443'}]

# #####################################
update_deployment_managers = [{'name': '10.0.100.139', 'port': '444'}]

# #####################################
expected_deployment_managers = [{'username': 'Administrator', 'type': 'DeploymentManager', 'name': '10.0.100.139', 'port': '443'}]

# #####################################
vCenter_password = 'Orion!123'
vcenter = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443'}]

# #####################################
update_vcenter = [{'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'username': 'administrator@vsphere.local', 'password': vCenter_password,
                   'port': '443', 'version': '6.5.0', 'virtualSwitchType': 'Distributed', 'multiNicVMotion': 'false', 'distributedSwitchUsage': 'GeneralNetworks',
                   'distributedSwitchVersion': '6.0.0', 'hypervisor_type': 'Vmware'}]

# #####################################  Hypervisor Cluster Profile ##########################################
os_plan = '/rest/os-deployment-build-plans/1590001'
new_os_plan = '/rest/os-deployment-build-plans/1570001'


Cluster_10 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_10', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help'}
              ]

cluster_10_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_10', 'new_name': 'Cluster_10_updated'}]

cluster_30 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_30', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
               'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
               'server_hardware': ['pulsarwpst-enc5, bay 12', 'pulsarwpst-enc5, bay 1'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
              ]

vSwitch_01 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_01', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'vSwitch_01_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 2'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]
vSwitch_03 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_03', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'vSwitch_03_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 13'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_04', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 8'],
               'shared_volume': [{'name': 'svol2', 'volumeFileSystemType': 'VMFS'}],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

dvSwitch_01 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_01', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'dvSwitch_01_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 10'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
               ]

cluster_113_v4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v4', 'path': 'DC1', 'vcenter': '10.0.100.160',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                   'deployment_uri': os_plan, 'server_password': 'iso*help',
                   'server_hardware': ['pulsarwpst-enc5, bay 9'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
                  ]

cluster_113_v4_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v4', 'server_hardware': ['pulsarwpst-enc5, bay 12']}
                         ]

Cluster_113_v5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v5', 'path': 'DC1', 'vcenter': '10.0.100.160',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                   'deployment_uri': os_plan, 'server_password': 'iso*help',
                   'server_hardware': ['pulsarwpst-enc5, bay 6'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}
                  ]

Cluster_113_v5_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v5',
                          'deployment_uri': os_plan, 'server_password': 'iso*help',
                          'server_hardware': ['pulsarwpst-enc5, bay 1']}
                         ]

Cluster_113_v6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '10.0.100.160',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                   'deployment_uri': os_plan, 'server_password': 'iso*help',
                   'server_hardware': ['pulsarwpst-enc5, bay 2'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

Cluster_113_v6_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '10.0.100.160',
                          'deployment_uri': os_plan, 'server_password': 'iso*help',
                          'server_hardware': ['pulsarwpst-enc5, bay 9']}
                         ]

Cluster_113_v1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v1', 'path': 'DC1', 'vcenter': '10.0.100.160',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 12', 'pulsarwpst-enc5, bay 6'],
                   'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
                  ]

Cluster_113_v1_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v1', 'HostProfileUris': ['pulsarwpst-enc5, bay 12']}
                         ]

Cluster_113_v2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v2', 'path': 'DC1', 'vcenter': '10.0.100.160',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                   'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}
                  ]

Cluster_113_v2_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v2', 'HostProfileUris': ['pulsarwpst-enc5, bay 2']}
                         ]

Cluster_113_v3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v3', 'path': 'DC1', 'vcenter': '10.0.100.160',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                   'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                   'server_hardware': ['pulsarwpst-enc5, bay 9', 'pulsarwpst-enc5, bay 12'],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

Cluster_113_v3_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v3', 'HostProfileUris': ['pulsarwpst-enc5, bay 9']}
                         ]

Cluster_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_1', 'path': 'DC1', 'vcenter': '10.0.100.160',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
              'deployment_uri': os_plan, 'server_password': 'iso*help'
              }
             ]

Cluster_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_3', 'path': 'DC1', 'vcenter': '10.0.100.160',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
              'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
              'server_hardware': ['pulsarwpst-enc5, bay 14'],
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_28 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_28', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 16'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
              ]

Cluster_22 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_22', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'}, 'server_hardware': ['pulsarwpst-enc5, bay 8'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
              ]

Cluster_26 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_26', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_nomgmt', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help'}
              ]

Cluster_27 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_27', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 6'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_31 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_31', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
              ]

cluster_31_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_31', 'server_hardware': ['pulsarwpst-enc5, bay 13', 'pulsarwpst-enc5, bay 8']}
                     ]

Cluster_11 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_11', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help'}
              ]

cluster_11_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_11', 'path': 'Invalid_DC/host'}
                     ]

Host_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_07', 'path': 'DC1', 'vcenter': '10.0.100.160',
            'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
            'deployment_uri': os_plan, 'server_password': 'iso*help',
            'server_hardware': ['pulsarwpst-enc5, bay 16'],
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
           ]

Host_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_07', 'hhp_settings': {'hhp_name': 'Host_07', 'host_name': 'new_host'}}]

Cluster_129 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_129', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}
               ]

Cluster_133 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'true',
                                     'haEnabled': 'false'}}
               ]

Cluster_133_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'false',
                                            'haEnabled': 'true'}}
                      ]

SM_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_09', 'path': 'DC1', 'vcenter': '10.0.100.160',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
          'deployment_uri': os_plan, 'server_password': 'iso*help',
          'server_hardware': ['pulsarwpst-enc5, bay 14'],
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}
         ]

Cluster_43 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_43', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'Cluster_43_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 10'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
               'shared_volume': [{'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}
              ]

cluster_128 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_128', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 10'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_134 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_134', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 12'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_135 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_135', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 6'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_136 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_136', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 1'],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_18 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_18', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 2'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_107 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_107', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 10'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_108 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 14'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_108_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help',
                       'HostProfileUris': ['pulsarwpst-enc5, bay 10'],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

Cluster_109 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_109_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help',
                       'server_hardware': ['pulsarwpst-enc5, bay 16'],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

Cluster_29 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_29_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '10.0.100.160',
                      'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',
                      'deployment_uri': os_plan, 'server_password': 'iso*help',
                      'server_hardware': ['pulsarwpst-enc5, bay 12'],
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                     ]

Hosts_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Hosts_04', 'path': 'DC1', 'vcenter': '10.0.100.160',
             'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
             'deployment_uri': os_plan, 'server_password': 'iso*help',
             'server_hardware': ['pulsarwpst-enc5, bay 9'],
             'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
            ]


Cluster_177 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_177', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 12'],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_177_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_177', 'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                       'HostProfileUris': ['pulsarwpst-enc5, bay 12']}
                      ]

cls178_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls178'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls178'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls178'}
                     ]

cls178_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls178'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls178'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls178'}
                     ]
cluster_178 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_178', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
               ]

cluster_178_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_178', 'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                       'HostProfileUris': ['pulsarwpst-enc5, bay 9']}
                      ]

cls179_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls179'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls179'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls179'}
                     ]

cls179_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls179'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls179'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls179'}
                     ]
cluster_179 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_179', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}
               ]

cluster_179_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_179', 'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                       'HostProfileUris': ['pulsarwpst-enc5, bay 9']}
                      ]

Cluster_21 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_21', 'path': 'DC1', 'vcenter': '10.0.100.160', 'deployment_manager_type': 'ICSP',
               'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 12'],
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_21_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_21', 'hhp_settings': {'power_state': 'Off'}}
                     ]

cluster_130 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_130', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'false',
                                     'haEnabled': 'false'}}
               ]

cluster_131 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_131', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'true',
                                     'haEnabled': 'true'}}
               ]

cluster_132 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_132', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

cluster_133 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}
               ]

cluster_133_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'false', 'haEnabled': 'false'}}
                      ]

cluster_14 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_14', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 14'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_14_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_14', 'profile_name': 'profile_template_gen8_1_1'}
                     ]

cluster_16 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_16', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ["NULL"],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_180 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_180', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}, {'name': 'svol3', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_180_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_180', 'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                       'HostProfileUris': ['pulsarwpst-enc5, bay 9']}
                      ]

cls181_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls181'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls181'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls181'}
                     ]

cls181_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls181'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls181'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls181'}
                     ]
cluster_181 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_181', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}, {'name': 'svol3', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_181_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_181', 'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                       'HostProfileUris': ['pulsarwpst-enc5, bay 9']}
                      ]

cls182_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls182'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls182'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls182'}
                     ]

cls182_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls182'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls182'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls182'}
                     ]
cluster_182 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_182', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'},
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'},
                                  {'name': 'svol6', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_182_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_182', 'server_hardware': ['pulsarwpst-enc5, bay 1', 'pulsarwpst-enc5, bay 2'],
                       'HostProfileUris': ['pulsarwpst-enc5, bay 9']}
                      ]

cluster_183 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]
cluster_183_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false'}}]

cluster_183_update1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'server_hardware': ['pulsarwpst-enc5, bay 12']}]

cluster_15 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_15', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 6'],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

cluster_15_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_15',
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                           'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
                     ]

Host_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_06', 'path': 'DC1', 'vcenter': '10.0.100.160',
            'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 12'],
            'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
           ]

Host_06_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_06', 'hhp_settings': {'redeploy': 'true'}}
                  ]

Cluster_91 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_91', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_91_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_91', 'deployment_uri': new_os_plan}
                     ]

Cluster_92 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_92', 'path': 'DC1', 'vcenter': '10.0.100.160', 'deployment_manager_type': 'ICSP',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 6'],
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_92_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_92', 'deployment_uri': os_plan}
                     ]

Cluster_2 = [{'type': '', 'name': 'Cluster_2', 'path': 'DC1', 'vcenter': '10.0.100.160',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
              'deployment_uri': os_plan, 'server_password': 'iso*help',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_34 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_34', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 13'], 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_36 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_36', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_36_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_36', 'server_hardware': ['NONE']}
                     ]

Cluster_37 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_37', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_37_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_37', 'profile_name': 'Non-existingProfile', 'server_hardware': ['pulsarwpst-enc5, bay 8']}
                     ]

Cluster_38 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_38', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_38_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_38', 'server_hardware': ['pulsarwpst-enc5, bay 13'], 'deployment_uri': '/rest/os-deployment-build-plans/80000123456'}
                     ]

Cluster_39 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_39', 'path': 'DC1', 'vcenter': '172.18.13.00',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 8'],
               'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]
Cluster_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_4', 'path': 'DC1', 'vcenter': '10.0.100.160', 'deployment_manager_type': 'ICSP',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 12'],
              'deployment_uri': os_plan, 'server_password': 'iso*help', 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
             ]
Cluster_40 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_40', 'path': 'DC1', 'vcenter': '10.0.100.160', 'deployment_manager_type': 'ICSP',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 6'],
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'NonStandard', 'multi_nic_vmotion': 'true'}}
              ]

Cluster_41 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_41', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'hypervisor_type': 'Vmware', 'deployment_uri': os_plan, 'deployment_manager_type': 'ICSP',
               'server_password': 'iso*help'}
              ]

Cluster_42 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_42', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'server_password': 'iso*help'}
              ]

Cluster_5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_5', 'path': 'DC1', 'vcenter': '10.0.100.160', 'deployment_manager_type': 'ICSP',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['NULL'],
              'deployment_uri': os_plan, 'server_password': 'iso*help'}
             ]

Cluster_50 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_50', 'path': 'DC1', 'vcenter': '10.0.100.160', 'deployment_manager_type': 'ICSP',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 1'],
               'deployment_uri': '/rest/os-deployment-build-plans/800001_11', 'server_password': 'iso*help'}
              ]

Cluster_12 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help'}
              ]

Cluster_12_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '10.0.100.160',
                      'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                      'deployment_uri': os_plan, 'server_password': 'iso*help'}
                     ]

Cluster_173 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_173', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help'}
               ]

Cluster_184 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help'}
               ]

Cluster_184_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184_new', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help',
                       }
                      ]

Cluster_193 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_193', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help'}
               ]

Cluster_6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_6', 'path': 'DC1', 'vcenter': '10.0.100.160',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
              'deployment_uri': os_plan, 'server_password': 'iso*help',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard_1', 'multi_nic_vmotion': 'true'}}
             ]

Cluster_9 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_9', 'path': 'DC1', 'vcenter': '10.0.100.160',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
              'deployment_uri': os_plan, 'server_password': 'iso*help'
              }
             ]

cluster_88 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_88', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'None', 'haEnabled': 'NULL'}}
              ]

cluster_89 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_89', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                    'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks_1', 'distributed_switch_version': '6.0.0'}}
              ]

cluster_17 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_17', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_gen8111', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                    'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
              ]

Cluster_140 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 2'],
                'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_140_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_140_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_140_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_141 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
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

Cluster_142 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 10'],
                'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_142_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_142_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}
                        ]

Cluster_142_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

Cluster_143 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 13'],
                'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

Cluster_143_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_143_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}
                        ]

Cluster_143_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'InMaintenance'}}
                        ]

Cluster_143_update_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'ExitMaintenance'}}
                        ]

vCenter_1 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443'}
             ]

vCenter_1_update = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0',
                     'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
                     'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                    ]

vCenter_38 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0'}
              ]

vCenter_10 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0'}
              ]

vCenter_10_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_10', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_2 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '172.18.13.1211', 'port': '443', 'version': '6.5.0'}
             ]


vCenter_3 = [{'username': 'dcs1234', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '15.212.173.50', 'port': '443', 'version': '6.5.0'}
             ]

vCenter_4 = [{'username': 'administrator@vsphere.local', 'password': 'dcs123', 'type': 'HypervisorManagerV2', 'name': '15.212.173.50', 'port': '443', 'version': '6.5.0'}
             ]

vCenter_5 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '', 'port': '443', 'version': '6.5.0'}
             ]

vCenter_46 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2_012', 'name': '15.212.173.50', 'port': '443', 'version': '6.5.0'}
              ]

vCenter_34_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_34', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 12'],
                       'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_35_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 6'],
                       'deployment_uri': os_plan, 'server_password': 'iso*help', 'deployment_manager_type': 'ICSP',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_35_cluster_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '10.0.100.160',
                              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'HostProfileUris': ['pulsarwpst-enc5, bay 1'],
                              'deployment_uri': os_plan, 'server_password': 'iso*help',
                              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                             ]

vCenter_36_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_36_cluster_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '10.0.100.160',
                              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': ['pulsarwpst-enc5, bay 2'],
                              'deployment_uri': os_plan, 'server_password': 'iso*help',
                              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                             ]

vCenter_37_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_37', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                      ]

vCenter_38 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0'}
              ]

vCenter_38_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_38', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                       'deployment_uri': os_plan, 'server_password': 'iso*help'}
                      ]

vCenter_6 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0',
              'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '', 'distributedSwitchUsage': 'GeneralNetworks',
              'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
             ]

vCenter_14 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
              ]

vCenter_14_update = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0',
                      'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
                      'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                     ]

vCenter_16 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'port': '443', 'version': '6.5.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}
              ]

vCenter_17 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}
              ]

ICSP_14_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'ICSP_14_cluster', 'path': 'DC1', 'vcenter': '10.0.100.160',
                    'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                    'deployment_uri': os_plan, 'server_password': 'iso*help'}
                   ]

ICSPAltair_4 = [{'username': 'Administrator', 'type': 'DeploymentManager', 'name': '10.0.100.139', 'port': '443'}
                ]

ICSPAltair_3 = [{'username': 'wronguser', 'password': 'wrongpassword', 'type': 'DeploymentManager', 'name': '10.0.100.139', 'port': '443'}
                ]

ICSPAltair_2 = [{'username': 'Administrator', 'password': 'password', 'type': 'DeploymentManager', 'name': 'wrong_name', 'port': '443'}
                ]

cluster_103 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_103', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 12'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'true'}}
               ]

Cluster_104 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_104', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

Cluster_106 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_106', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 6'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

Cluster_105 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_105', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 12'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}
               ]

vSwitch_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_08', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_08_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_08', 'server_hardware': ['pulsarwpst-enc5, bay 9']}
                     ]

vSwitch_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_09', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_09_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_09', 'server_hardware': ['pulsarwpst-enc5, bay 2']}
                     ]

dvSwitch_05 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_05', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
               ]

dvSwitch_05_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_05', 'server_hardware': ['pulsarwpst-enc5, bay 1']}
                      ]

clsdvs6_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_clsdvs6'},
                      {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_clsdvs6'},
                      {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_clsdvs6'}
                      ]

clsdvs6_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_clsdvs6'},
                      {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_clsdvs6'},
                      {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_clsdvs6'}
                      ]

dvSwitch_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_06', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}
               ]

dvSwitch_06_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_06', 'server_hardware': ['pulsarwpst-enc5, bay 6']}
                      ]

vSwitch_02 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_02', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'vSwitch_02_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
              ]

vSwitch_02_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_02', 'server_hardware': ['pulsarwpst-enc5, bay 12']}
                     ]

dvSwitch_02 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_02', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

dvSwitch_02_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_02', 'server_hardware': ['pulsarwpst-enc5, bay 9']}
                      ]
clsdvs7_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_clsdvs7'}
                      ]

clsdvs7_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_clsdvs7'}
                      ]
dvSwitch_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_07', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}
               ]

dvSwitch_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_07', 'server_hardware': ['pulsarwpst-enc5, bay 1']}
                      ]

cls46_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls46'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls46'}
                    ]

cls46_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls46'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls46'}
                    ]

Cluster_vc_46 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'version': '6.5.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_46 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_46', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 2']}
              ]

cls47_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls47'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls47'}
                    ]

cls47_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls47'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls47'}
                    ]

# As per test case vCenter version should be 5.5.0  Due to limitation in DCS Oneview build(supporting only 5.1.0), Registering vCenter of version 5.1.0
Cluster_vc_47 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'version': '6.5.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.5.0', 'distributedSwitchUsage': 'AllNetworks', 'deployment_manager_type': 'ICSP',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_47 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_47', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 12']}
              ]

cls48_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls48'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls48'}
                    ]

cls48_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls48'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls48'}
                    ]

Cluster_vc_48 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'version': '6.5.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'AllNetworks', 'deployment_manager_type': 'ICSP',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_48 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_48', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 9']}
              ]

cls49_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls49'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls49'}
                    ]

cls49_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls49'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls49'}
                    ]

Cluster_vc_49 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'version': '6.5.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'AllNetworks', 'deployment_manager_type': 'ICSP',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                 ]

Cluster_49 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_49', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help'}
              ]

Cluster_49_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_49', 'server_hardware': ['pulsarwpst-enc5, bay 6']}
                     ]

cls111_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'net1', 'new_name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'corp1', 'new_name': 'corp1_cls111'}
                     ]

cls111_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'net1', 'name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'corp1', 'name': 'corp1_cls111'}
                     ]

Cluster_vc_111 = [{'username': 'administrator@vsphere.local', 'password': vCenter_password, 'type': 'HypervisorManagerV2', 'name': '10.0.100.160', 'version': '6.5.0',
                   'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '6.0.0', 'distributedSwitchUsage': 'AllNetworks', 'deployment_manager_type': 'ICSP',
                   'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}
                  ]

Cluster_111 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_111', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 10'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'},
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'true', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'}}
               ]

sm06_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm06'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm06'}
                   ]

sm06_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm06'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm06'}
                   ]

SM_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_06', 'path': 'DC1', 'vcenter': '10.0.100.160',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
          'deployment_uri': os_plan, 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.0'}}
         ]

sm07_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm07'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm07'}
                   ]

sm07_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm07'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm07'}
                   ]

SM_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_07', 'path': 'DC1', 'vcenter': '10.0.100.160',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
          'deployment_uri': os_plan, 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.1.0'}}
         ]

sm08_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm08'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm08'}
                   ]

sm08_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm08'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm08'}
                   ]

SM_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_08', 'path': 'DC1', 'vcenter': '10.0.100.160',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
          'deployment_uri': os_plan, 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.0.0'}}
         ]

sm10_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm10'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm10'}
                   ]

sm10_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm10'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm10'}
                   ]

SM_10 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_10', 'path': 'DC1', 'vcenter': '10.0.100.160',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
          'deployment_uri': os_plan, 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.5.0'}}
         ]
'''*************************  New set of cluster *********************************'''
Cluster_13 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_13', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true',
                                    'drsEnabled': 'true', 'haEnabled': 'false'}}]

Cluster_13_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_13',
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true',
                                           'drsEnabled': 'false', 'haEnabled': 'true'}}]

cluster_44 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_44', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 9'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
               'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'},
                                 {'name': 'svol6', 'volumeFileSystemType': 'VMFS'}]}]

cluster_45 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_45', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 9'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
               'shared_volume': [{'name': 'invalid_svol', 'volumeFileSystemType': 'VMFS'},
                                 {'name': 'svol6', 'volumeFileSystemType': 'VMFS'}]}]

vSwitch_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_07', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'vSwitch_01_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_07', 'server_hardware': ['pulsarwpst-enc5, bay 2']}]


Cluster_114 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_114', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 1'],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]


cluster_115 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_115', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 14'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}]}
               ]

cluster_116 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_116', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 9'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'shared_volume': [{'name': 'svol7', 'pool_name': 'cpg-growth-limit-1TiB123', 'provisionType': 'Thin', 'volumeFileSystemType': 'VMFS'}]}
               ]

dvSwitch_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_04', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 16'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}]

dvSwitch_04_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_04', 'server_hardware': ['pulsarwpst-enc5, bay 6']}
                      ]

dvSwitch_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_08', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 13'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}}
               ]

dvSwitch_08_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_08', 'server_hardware': ['pulsarwpst-enc5, bay 6']}
                      ]

dvSwitch_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_09', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'server_hardware': ['pulsarwpst-enc5, bay 12'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}
               ]

dvSwitch_09_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_09', 'server_hardware': ['pulsarwpst-enc5, bay 12']}
                      ]

cluster_186 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_186', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'mgmtIp_SettingsOverride': {'netmask': '255.255.252.0', 'gateway': '15.212.168.1',
                                            'primaryDns': 'null', 'secondaryDns': 'null'},
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
                }
               ]
cluster_186_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_186',
                       'server_hardware': ['pulsarwpst-enc5, bay 12'], 'mgmt_ip':['15.212.171.201']
                       }]
cluster_187 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_187', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}
                }
               ]
cluster_187_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_187', 'path': 'DC1', 'vcenter': '10.0.100.160',
                       'mgmtIp_SettingsOverride': {'netmask': '255.255.252.0', 'gateway': '15.212.168.1',
                                                   'primaryDns': 'null', 'secondaryDns': 'null'},
                       'server_hardware': ['pulsarwpst-enc5, bay 12', 'pulsarwpst-enc5, bay 6'], 'mgmt_ip': ['15.212.171.202', '15.212.171.203'],
                       }
                      ]
cluster_188 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_188', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'mgmtIp_SettingsOverride': {'netmask': '255.255.252.0', 'gateway': '15.212.168.1',
                                            'primaryDns': '16.110.135.51', 'secondaryDns': '16.110.135.52'},
                'server_hardware': ['pulsarwpst-enc5, bay 8'], 'mgmt_ip':['15.212.171.201'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}
                }
               ]

cluster_189 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_189', 'path': 'DC1', 'vcenter': '10.0.100.160',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
                'deployment_uri': os_plan, 'server_password': 'iso*help',
                'mgmtIp_SettingsOverride': {'netmask': '205.255.252.0', 'gateway': '15.212.168.12',
                                            'primaryDns': '16.110.135.59', 'secondaryDns': '16.110.135.58'},
                'server_hardware': ['pulsarwpst-enc5, bay 9'], 'mgmt_ip':['15.212.171.201'],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '6.0.0'}
                }
               ]
vSwitch_05 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_05', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'profile_nomgmt', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 12'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '6.0.0'}}]

vSwitch_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_06', 'path': 'DC1', 'vcenter': '10.0.100.160',
               'profile_name': 'vSwitch_06_SP', 'hypervisor_type': 'Vmware', 'deployment_manager_type': 'ICSP',
               'deployment_uri': os_plan, 'server_password': 'iso*help',
               'server_hardware': ['pulsarwpst-enc5, bay 12'],
               'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

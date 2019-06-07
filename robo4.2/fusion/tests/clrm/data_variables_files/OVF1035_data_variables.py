# #####################################
admin_credentials = {'userName': 'Administrator', 'password': 'vsbqa*help'}

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

OVF1035_API_1 = [{'name': 'OVF1035_API_1', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                  'connectionSettings': {'manageConnections': False,
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
                  }
                 ]

OVF1035_API_2 = [{'name': 'OVF1035_API_2', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
                  }
                 ]

OVF1035_02 = [{'name': 'OVF1035_02', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False,
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
               }
              ]

OVF1035_02_SP = [{'name': 'OVF1035_02_SP', 'serverHardwareUri': 'Encl2, bay 3', 'enclosureGroupUri': 'EG:enclgrp', "type": "ServerProfileV7",
                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                  ],
                  'serverProfileTemplateUri': 'SPT:OVF1035_02'
                  }
                 ]

OVF1035_03 = [{'name': 'OVF1035_03', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
               }
              ]

OVF1035_03_update1 = [{'name': 'OVF1035_03', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': False},
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                       }
                      ]

OVF1035_03_SP = [{'name': 'OVF1035_03_SP', 'serverHardwareUri': 'Encl2, bay 4', 'enclosureGroupUri': 'EG:enclgrp', "type": "ServerProfileV7", 'serverProfileTemplateUri': 'SPT:OVF1035_03',
                  'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                  {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'},
                                  {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500", "networkUri": "FC:san"},
                                  {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"},
                                  {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": "ETH:production"}
                                  ]
                  }
                 ]

OVF1035_04 = [{'name': 'OVF1035_04', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
               }
              ]

OVF1035_04_update1 = [{'name': 'OVF1035_04', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
                       }
                      ]

OVF1035_04_SP = [{'name': 'OVF1035_04_SP', 'serverHardwareUri': 'Encl2, bay 4', 'enclosureGroupUri': 'EG:enclgrp', "type": "ServerProfileV7", 'serverProfileTemplateUri': 'SPT:OVF1035_04',
                  'connections': []
                  }
                 ]

OVF1035_05 = [{'name': 'OVF1035_05', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
               }
              ]

OVF1035_05_update1 = [{'name': 'OVF1035_05', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
                       }
                      ]

OVF1035_06 = [{'name': 'OVF1035_06', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
               }
              ]

OVF1035_07 = [{'name': 'OVF1035_07', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
               }
              ]

OVF1035_07_update1 = [{'name': 'OVF1035_07', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': False},
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                       }
                      ]

OVF1035_08 = [{'name': 'OVF1035_08', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': False},
               'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
               'bootMode': None,
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
               }
              ]

OVF1035_08_update1 = [{'name': 'OVF1035_08', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
                       }
                      ]

OVF1035_09 = [{'name': 'OVF1035_09', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
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
               }
              ]

OVF1035_09_update1 = [{'name': 'OVF1035_09', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'manageConnections': False},
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bootMode': None,
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}
                       }
                      ]

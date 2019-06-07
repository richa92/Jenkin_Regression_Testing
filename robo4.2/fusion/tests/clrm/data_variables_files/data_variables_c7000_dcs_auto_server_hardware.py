# #####################################
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

# #####################################

# #########PREREQUISITES###############
ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'corp', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '80', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '70', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '21', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '22', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '34', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'untagged_nw', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '33', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '10', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '23', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '24', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '100', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'iSCSI', 'connectionTemplateUri': None,
                      'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '101', 'purpose': 'ISCSI', "subnetUri": None}]

fc_networks = [{'fabricType': 'DirectAttach', 'name': 'san_da', 'autoLoginRedistribution': True, 'linkStabilityTime': 30,
                'connectionTemplateUri': None, 'type': 'fc-networkV4'},
               {'fabricType': 'FabricAttach', 'name': 'san', 'autoLoginRedistribution': True, 'linkStabilityTime': 30,
                'connectionTemplateUri': None, 'type': 'fc-networkV4'}]

network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1'], 'nativeNetworkUri': 'net1'},
                {'name': 'netset2', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1', 'production'], 'nativeNetworkUri': 'net1'},
                {'name': 'netset3', 'type': 'network-setV4', 'networkUris': ['corp1', 'iSCSI'], 'nativeNetworkUri': None}]

uplink_sets = {'uplink1': {'name': 'upl_corp',
                           'ethernetNetworkType': 'Untagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['corp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]},
               'uplink2': {'name': 'upl_icsp',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['icsp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]},
               'uplink3': {'name': 'upl_san',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkUris': ['san'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'X3', 'speed': 'Auto'}]}}

ligs = {'name': 'lig',
        'type': 'logical-interconnect-groupV300',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                    {'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink2'].copy(), uplink_sets['uplink3'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net2', 'corp1', 'net1', 'network2', 'untagged_nw', 'tunneled_nw', 'production']}

enc_groups = {'name': 'enclgrp',
              'enclosureCount': 1,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig'}],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"}

enclosures = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None},
              {'hostname': "172.18.1.13", 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None}]

storage_systems = [{'family': 'StoreServ', 'name': 'ThreePAR-1', 'hostname': '172.18.11.11', 'credentials': {'username': 'dcs', 'password': 'dcs'}}]

update_storage_systems = [{'type': 'StorageSystemV4',
                           'credentials': {'hostname': '172.18.11.11',
                                           'username': 'dcs',
                                           'password': 'dcs'},
                           'family': 'StoreServ',
                           'name': 'ThreePAR-1',
                           "deviceSpecificAttributes": {'managedDomain': 'TestDomain'},
                           'ports': [{}, {}, {},
                                     {"expectedNetworkUri": "FC:san",
                                      "expectedNetworkName": "san",
                                      "expectedSanUri": "FC:san",
                                      "mode": "Managed",
                                      "name": "0:1:1"},
                                     {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]}]

storage_pools = [{"storageSystemUri": "ThreePAR-1", "name": "cpg-growth-limit-1TiB", "isManaged": True}]

storage_volumes = [{"properties": {"name": "svol1", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol2", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol3", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol4", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol5", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "svol6", "description": "", "storagePool": "cpg-growth-limit-1TiB", "size": 11000000000, "provisioningType": "Thin", "isShareable": True,
                                   "snapshotPool": "cpg-growth-limit-1TiB"}, "templateUri": "ROOT", "isPermanent": True}]

server_profile_templates = [{'name': 'profile_template_gen8_1', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual',
                             'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:icsp',
                                                                     'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:corp',
                                                                     'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                     'requestedMbps': '2500', 'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

                            {'name': 'profile_gen81_san', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
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
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "san_vol",
                                                                           "size": 10737418240,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}},

                            {'name': 'profile_template_gen8_1_1', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

                            {'name': 'vSwitch_03_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:icsp',
                                                                     'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:corp',
                                                                     'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_untagged', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:untagged_nw', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri':
                                                                     'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri':
                                                                     'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

                            {'name': 'profile_nomgmt', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

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
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
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
                                                                           "name": "nvol2",
                                                                           "size": 10737418240,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 5, 'targetSelector': 'Auto', 'targets': []}]}]}},

                            {'name': 'dvSwitch_05_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

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
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': 'FirmwareOnly'},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                             'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                            'volumeAttachments': [{'id': 1,
                                                                   "volume": {
                                                                       "properties": {
                                                                           "name": "nvol1",
                                                                           "size": 10737418240,
                                                                           "provisioningType": "Thin",
                                                                           "isShareable": False,
                                                                           "storagePool": "SP:cpg-growth-limit-1TiB"
                                                                       },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:cpg-growth-limit-1TiB'
                                                                   },
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                   'isBootVolume': True,
                                                                   'lunType': 'Auto',
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}},

                            {'name': 'dvSwitch_07_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

                            {'name': 'Cluster_177_178_179', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
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
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                   'isBootVolume': False,
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol3",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}},

                            {'name': 'Cluster_180_181_182_SPT', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'FC:san', 'boot': {'priority': 'NotBootable'}},
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
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                   'isBootVolume': False,
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol6",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]},
                                                                  {'id': 2,
                                                                   "volumeStorageSystemUri": "SSYS:ThreePAR-1",
                                                                   'isBootVolume': False,
                                                                   'lunType': 'Auto',
                                                                   "volumeUri": "v:svol1",
                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto', 'targets': []}]}]}},

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
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},
                            {'name': 'dvSwitch_01_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_vm1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_vm2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:network2', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

                            {'name': 'vSwitch_02_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
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
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},

                            {'name': 'dvSwitch_02_SP', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'icsp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:icsp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:corp', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': 'conn_netset', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 4, 'name': 'conn_prod1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 5, 'name': 'conn_prod2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                     'networkUri': 'ETH:production', 'boot': {'priority': 'NotBootable'}}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None},
                            {'name': 'profile_template_vsa', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "conn_prod1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"},
                                                                    {"id": 5, "name": "conn_prod2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:production"},
                                                                    {"id": 6, "name": "iscsi_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:iSCSI'}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, 'volumeAttachments': []}},
                            {'name': 'SPT_vsa_multi_iSCSI', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "iscsi_conn1", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:iSCSI"},
                                                                    {"id": 5, "name": "iscsi_conn2", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "ETH:iSCSI"},
                                                                    {"id": 6, "name": "iscsi_conn3", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:iSCSI'}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                                                                        'volumeAttachments': []}},

                            {'name': 'SPT_vsa_netset_iSCSI', 'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1',
                             'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": 'ETH:corp'},
                                                                    {"id": 3, "name": "san_conn", "functionType": "FibreChannel", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "FC:san"},
                                                                    {"id": 4, "name": "netset3_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                                                                     "networkUri": "NS:netset2"}]},
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                                                                        'volumeAttachments': []}}
                            ]

# ####################################
ipv4_subnet = [{'type': 'Subnet',
                'networkId': '10.0.0.0',
                'subnetmask': '255.255.0.0',
                'gateway': '10.0.1.6',
                'dnsServers': ['10.0.1.2'],
                'domain': 'ind.hpe.com'}
               ]
ipv4_subnet_local = [{'type': 'Subnet',
                      'networkId': '15.146.152.0',
                      'subnetmask': '255.255.248.0',
                      'gateway': '15.146.152.1',
                      'dnsServers': ['16.110.135.51',
                                     '16.110.135.52'],
                      'domain': 'hpe.com'}
                     ]
ipv4_ranges = [{'type': 'Range', 'name': 'IPV4', 'startAddress': '10.0.100.190', 'endAddress': '10.0.100.200', 'subnetUri': '10.0.0.0'}]

ipv4_ranges_local = [{'type': 'Range', 'name': 'IPV4', 'startAddress': '15.146.152.2', 'endAddress': '15.146.152.99', 'subnetUri': '15.146.152.0'}]

subnet_association = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'subnetUri': '10.0.0.0'}]

subnet_association_local = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'subnetUri': '15.146.152.0'}]
# #####################################
deployment_managers = [{'username': 'dcs', 'password': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

# #####################################
update_deployment_managers = [{'name': '172.18.9.1', 'port': '444'}]

# #####################################
expected_deployment_managers = [{'username': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

# #####################################
vcenter = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443'}]

# #####################################
update_vcenter = [{'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'username': 'dcs', 'password': 'dcs', 'port': '443',
                   'version': '5.1.0', 'virtualSwitchType': 'Distributed', 'multiNicVMotion': 'false', 'distributedSwitchUsage':
                   'GeneralNetworks', 'distributedSwitchVersion': '5.1.0', 'hypervisor_type': 'Vmware'}]

######################################
cluster_10 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_10', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

cluster_10_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_10', 'new_name': 'Cluster_10_updated'}]

cluster_30 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_30', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [2],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

vSwitch_01 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_01', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_01_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_03 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_03', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_03_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_04', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_04_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

dvSwitch_01 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_01', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_01_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

cluster_113_v4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v4', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'server_hardware': [1],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

cluster_113_v4_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v4', 'server_hardware': [1]}]

Cluster_113_v5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v5', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'server_hardware': [1],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_113_v5_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v5',
                          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                          'server_hardware': [1]}]

Cluster_113_v6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'server_hardware': [1],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_113_v6_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'cluster_113_v6', 'path': 'DC1', 'vcenter': '172.18.13.11',
                          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                          'server_hardware': [1]}]

Cluster_113_v1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v1', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [2],
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_113_v1_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v1', 'HostProfileUris': [1]}]

Cluster_113_v2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v2', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'server_hardware': [2],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                        'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_113_v2_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v2', 'HostProfileUris': [1]}]

Cluster_113_v3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v3', 'path': 'DC1', 'vcenter': '172.18.13.11',
                   'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                   'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'server_hardware': [2],
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_113_v3_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_113_v3', 'HostProfileUris': [1]}]

Cluster_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_1', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

Cluster_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_3', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'server_hardware': [1],
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_28 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_28', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_22 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_22', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'}, 'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_26 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_26', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_nomgmt', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

Cluster_27 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_27', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_31 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_31', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                    'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

cluster_31_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_31', 'server_hardware': [2]}]

Cluster_11 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_11', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

cluster_11_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_11', 'path': 'Invalid_DC/host'}]

Host_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_07', 'path': 'DC1', 'vcenter': '172.18.13.11',
            'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
            'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
            'server_hardware': [1],
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Host_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_07', 'hhp_settings': {'hhp_name': 'Host_07', 'host_name': 'new_host'}}]

Cluster_129 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_129', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}]

Cluster_133 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true',
                                     'haEnabled': 'false'}}]

Cluster_133_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false',
                                            'haEnabled': 'true'}}]

SM_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_09', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'server_hardware': [1],
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_43 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_43', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'Cluster_43_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
               'shared_volume': [{'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}]

cluster_128 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_128', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_134 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_134', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_135 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_135', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_136 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_136', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_18 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_18', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_107 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_107', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_108 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_108_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_108', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'HostProfileUris': [1],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_109 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_109_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_109', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'server_hardware': [1],
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_29 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_29_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_29', 'path': 'DC1', 'vcenter': '172.18.13.11',
                      'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                      'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                      'server_hardware': [1],
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Hosts_04 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Hosts_04', 'path': 'DC1', 'vcenter': '172.18.13.11',
             'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
             'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
             'server_hardware': [1],
             'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_177 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_177', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_177_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_177', 'server_hardware': [2], 'HostProfileUris': [1]}]

cls178_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls178'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls178'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls178'}]

cls178_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls178'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls178'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls178'}]

cluster_178 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_178', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

cluster_178_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_178', 'server_hardware': [2], 'HostProfileUris': [1]}]

cls179_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls179'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls179'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls179'}]

cls179_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls179'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls179'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls179'}]

cluster_179 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_179', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_177_178_179', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'shared_volume': [{'name': 'svol3', 'volumeFileSystemType': 'VMFS'}],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

cluster_179_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_179', 'server_hardware': [2],
                       'HostProfileUris': [1]}]

Cluster_21 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_21', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_21_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_21', 'hhp_settings': {'power_state': 'Off'}}]

cluster_130 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_130', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false',
                                     'haEnabled': 'false'}}]

cluster_131 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_131', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true',
                                     'haEnabled': 'true'}}]

cluster_132 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_132', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}]

cluster_133 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'true', 'haEnabled': 'false'}}]

cluster_133_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_133', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                            'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'false'}}]

cluster_14 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_14', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_14_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_14', 'profile_name': 'profile_template_gen8_1_1'}]

cluster_16 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_16', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [None],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_180 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_180', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}, {'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}]

cluster_180_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_180', 'server_hardware': [2],
                       'HostProfileUris': [1]}]

cls181_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls181'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls181'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls181'}]

cls181_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls181'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls181'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls181'}]

cluster_181 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_181', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'svol6', 'volumeFileSystemType': 'VMFS'}, {'name': 'svol1', 'volumeFileSystemType': 'VMFS'}]}]

cluster_181_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_181', 'server_hardware': [2],
                       'HostProfileUris': [1]}]

cls182_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls182'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls182'},
                     {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls182'}]

cls182_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls182'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls182'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls182'}]

cluster_182 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_182', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'Cluster_180_181_182_SPT', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'svol1', 'volumeFileSystemType': 'VMFS'},
                                  {'name': 'svol6', 'volumeFileSystemType': 'VMFS'}]}]

cluster_182_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_182', 'server_hardware': [2],
                       'HostProfileUris': [1]}]

cluster_183 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_183_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false'}}]

cluster_183_update1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_183', 'server_hardware': [1]}]

cluster_15 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_15', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1],
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

cluster_15_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_15',
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                           'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

Host_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_06', 'path': 'DC1', 'vcenter': '172.18.13.11',
            'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
            'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
            'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Host_06_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Host_06', 'hhp_settings': {'redeploy': 'true'}}]

Cluster_91 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_91', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_91_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_91', 'deployment_uri': '/rest/os-deployment-build-plans/780001'}]

Cluster_92 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_92', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen81_san', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_92_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_92', 'deployment_uri': '/rest/os-deployment-build-plans/780001'}]

Cluster_2 = [{'type': '', 'name': 'Cluster_2', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_34 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_34', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'hypervisor_type': 'Vmware', 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_36 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_36', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_36_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_36', 'server_hardware': [None]}]

Cluster_37 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_37', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_37_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_37', 'profile_name': 'Non-existingProfile', 'server_hardware': [1]}]

Cluster_38 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_38', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_38_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_38', 'server_hardware': [1], 'deployment_uri': '/rest/os-deployment-build-plans/80000123456'}]

Cluster_39 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_39', 'path': 'DC1', 'vcenter': '172.18.13.00',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_4', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_40 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_40', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'NonStandard', 'multi_nic_vmotion': 'true'}}]

Cluster_41 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_41', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'hypervisor_type': 'Vmware', 'deployment_uri': '/rest/os-deployment-build-plans/800001',  # 'deployment_manager_type': 'ICSP',
               'server_password': 'iso*help'}]

Cluster_42 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_42', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'server_password': 'iso*help'}]

Cluster_5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_5', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [None],  # 'deployment_manager_type': 'ICSP',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

Cluster_50 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_50', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001_11', 'server_password': 'iso*help'}]

Cluster_12 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

Cluster_12_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_12', 'path': 'DC1', 'vcenter': '172.18.13.11',
                      'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                      'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'
                      }]

Cluster_173 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_173', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'}]

Cluster_184 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'
                }]

Cluster_184_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_184', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'hostprefix': 'cls184_new',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'
                       }]

Cluster_193 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_193', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                }]

Cluster_6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_6', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard_1', 'multi_nic_vmotion': 'true'}}]

Cluster_9 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_9', 'path': 'DC1', 'vcenter': '172.18.13.11',
              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'
              }]

cluster_88 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_88', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks',
                                    'distributed_switch_version': '5.1.0', 'drsEnabled': 'None', 'haEnabled': 'NULL'}}]

cluster_89 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_89', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                    'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'AllNetworks_1', 'distributed_switch_version': '5.1.0'}}]

cluster_17 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_17', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_gen8111', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                    'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}}]

Cluster_140 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_140_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}]

Cluster_140_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'Off'}}]

Cluster_140_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_140', 'hhp_settings': {'power_state': 'On'}}]

Cluster_141 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_141_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'On'}}]

Cluster_141_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'InMaintenance'}}]

Cluster_141_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'ExitMaintenance'}}]

Cluster_141_update_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_141', 'hhp_settings': {'power_state': 'Off'}}]

Cluster_142 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_142_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}]

Cluster_142_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'On'}}]

Cluster_142_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_142', 'hhp_settings': {'power_state': 'ExitMaintenance'}}]

Cluster_143 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

Cluster_143_update_1 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}]

Cluster_143_update_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'Off'}}]

Cluster_143_update_3 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'InMaintenance'}}]

Cluster_143_update_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_143', 'hhp_settings': {'power_state': 'ExitMaintenance'}}]

vCenter_1 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_1_update = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
                     'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
                     'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

vCenter_38 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_10 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_10_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_10', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_2 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.1211', 'port': '443', 'version': '5.1.0'}]

vCenter_3 = [{'username': 'dcs1234', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_4 = [{'username': 'dcs', 'password': 'dcs123', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_5 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '', 'port': '443', 'version': '5.1.0'}]

vCenter_46 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2_012', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_34_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_34', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_35_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',  # 'deployment_manager_type': 'ICSP',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_35_cluster_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_35', 'path': 'DC1', 'vcenter': '172.18.13.11',
                              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'HostProfileUris': [1],
                              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_36_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_36_cluster_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_36', 'path': 'DC1', 'vcenter': '172.18.13.11',
                              'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware', 'server_hardware': [1],
                              'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                              'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_37_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_37', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vCenter_38 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0'}]

vCenter_38_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'vCenter_38', 'path': 'DC1', 'vcenter': '172.18.13.11',
                       'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                       'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                       }]

vCenter_6 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
              'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '', 'distributedSwitchUsage': 'GeneralNetworks',
              'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

vCenter_14 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

vCenter_14_update = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
                      'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'GeneralNetworks',
                      'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

vCenter_16 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', 'version': '5.1.0',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}]

vCenter_17 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11',
               'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'GeneralNetworks',
               'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true'}]

ICSP_14_cluster = [{'type': 'HypervisorClusterProfileV2', 'name': 'ICSP_14_cluster', 'path': 'DC1', 'vcenter': '172.18.13.11',
                    'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                    'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'
                    }]

ICSPAltair_4 = [{'username': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

ICSPAltair_3 = [{'username': 'wronguser', 'password': 'wrongpassword', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

ICSPAltair_2 = [{'username': 'dcs', 'password': 'dcs', 'type': 'DeploymentManager', 'name': 'wrong_name', 'port': '443'}]

cluster_103 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_103', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'true'}}]

cluster_104 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_104', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'true'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}]

cluster_106 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_106', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}]

cluster_105 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_105', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'false', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'},
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'}}]

vSwitch_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_08', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_08_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_08', 'server_hardware': [1]}]

vSwitch_09 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_09', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_09_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_09', 'server_hardware': [1]}]

dvSwitch_05 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_05', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

dvSwitch_05_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_05', 'server_hardware': [1]}]

dvSwitch_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_06', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'}}]

dvSwitch_06_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_06', 'server_hardware': [1]}]

vSwitch_02 = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_02', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'vSwitch_02_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

vSwitch_02_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'vSwitch_02', 'server_hardware': [1]}]

dvSwitch_02 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_02', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}]

dvSwitch_02_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_02', 'server_hardware': [1]}]

clsdvs7_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_clsdvs7'}]

clsdvs7_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_clsdvs7'},
                      {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_clsdvs7'}]

dvSwitch_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_07', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_05_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0', 'drsEnabled': 'false', 'haEnabled': 'true'}}]

dvSwitch_07_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'dvSwitch_07', 'server_hardware': [1]}]

cls46_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls46'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls46'}]

cls46_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls46'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls46'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls46'}]

Cluster_vc_46 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.0.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

Cluster_46 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_46', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1]}]

cls47_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls47'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls47'}]

cls47_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls47'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls47'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls47'}]

# As per test case vCenter version should be 5.5.0  Due to limitation in DCS Oneview build(supporting only 5.1.0), Registering vCenter of version 5.1.0
Cluster_vc_47 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

Cluster_47 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_47', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1]}]

cls48_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls48'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls48'}]

cls48_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls48'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls48'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls48'}]

Cluster_vc_48 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

Cluster_48 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_48', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
               'server_hardware': [1]}]

cls49_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls49'},
                    {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_cls49'}]

cls49_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls49'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls49'},
                    {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_cls49'}]

Cluster_vc_49 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'version': '5.1.0',
                  'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                  'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

Cluster_49 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_49', 'path': 'DC1', 'vcenter': '172.18.13.11',
               'profile_name': 'profile_template_gen8_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
               'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help'
               }]

Cluster_49_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_49', 'server_hardware': [1]}]

cls111_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'net1', 'new_name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV4', 'name': 'corp1', 'new_name': 'corp1_cls111'}]

cls111_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'net1', 'name': 'net1_cls111'},
                     {'network type': 'ethernet-networkV4', 'new_name': 'corp1', 'name': 'corp1_cls111'}]

Cluster_vc_111 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'version': '5.1.0',
                   'virtualSwitchType': 'Distributed', 'distributedSwitchVersion': '5.1.0', 'distributedSwitchUsage': 'AllNetworks',
                   'hypervisor_type': 'Vmware', 'multiNicVMotion': 'false'}]

Cluster_111 = [{'type': 'HypervisorClusterProfileV2', 'name': 'Cluster_111', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'dvSwitch_02_SP', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                'hostConfigPolicy_settings': {'leaveHostInMaintenance': 'false', 'useHostnameToRegister': 'false', 'useHostPrefixAsHostname': 'false'},
                'virtualSwitchConfigPolicy': {'customVirtualSwitches': 'true', 'configurePortGroups': 'false', 'manageVirtualSwitches': 'false'}}]

sm06_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm06'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm06'}]

sm06_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm06'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm06'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm06'}]

SM_06 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_06', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.0'}}]

sm07_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm07'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm07'}]

sm07_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm07'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm07'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm07'}]

SM_07 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_07', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '4.1.0'}}]

sm08_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm08'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm08'}]

sm08_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm08'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm08'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm08'}]

SM_08 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_08', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.0.0'}}]

sm10_net_edit_1 = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'new_name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV4', 'name': 'icsp', 'new_name': 'icsp_sm10'},
                   {'network type': 'ethernet-networkV4', 'name': 'production', 'new_name': 'production_sm10'}]

sm10_net_edit_2 = [{'network type': 'ethernet-networkV4', 'new_name': 'corp', 'name': 'corp_sm10'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'icsp', 'name': 'icsp_sm10'},
                   {'network type': 'ethernet-networkV4', 'new_name': 'production', 'name': 'production_sm10'}]

SM_10 = [{'type': 'HypervisorClusterProfileV2', 'name': 'SM_10', 'path': 'DC1', 'vcenter': '172.18.13.11',
          'profile_name': 'profile_template_gen8_1_1', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
          'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                               'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.5.0'}}]

"""
ISCSI cluster profiles
"""

iSCSI_Vol_2 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_2', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                }]

iSCSI_Vol_2_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_2', 'server_hardware': [1]}]

iSCSI_Vol_4 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_4', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'}
                }]

iSCSI_Vol_4_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_4', 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]}]

iSCSI_Vol_5 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_5', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                }]

iSCSI_Vol_5_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_5', 'shared_volume': [{'name': 'vsa1', 'requestedCapacity': 10000000}]}]

iSCSI_Vol_6 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_6', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]}]

iSCSI_Vol_6_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_6', 'del_shared_volume': ['vsa1']}]

iSCSI_Vol_7 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_7', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [2],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                }]

iSCSI_Vol_7_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_7', 'HostProfileUris': [1]}]

iSCSI_Vol_8 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_8', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [2],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                }]

iSCSI_Vol_8_update = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_8', 'HostProfileUris': [2]}]

iSCSI_Vol_9 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_9', 'path': 'DC1', 'vcenter': '172.18.13.11',
                'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                'server_hardware': [1],
                'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                     'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                }]

iSCSI_Vol_18 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_18', 'path': 'DC1', 'vcenter': '172.18.13.11',
                 'profile_name': 'SPT_vsa_multi_iSCSI', 'hypervisor_type': 'Vmware',  # 'deployment_manager_type': 'ICSP',
                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                 'server_hardware': [1],
                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                 }]

iSCSI_Vol_21 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_21', 'path': 'DC1', 'vcenter': '172.18.13.11',
                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',
                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                 }]

iSCSI_Vol_22 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_22', 'path': 'DC1', 'vcenter': '172.18.13.11',
                 'profile_name': 'SPT_vsa_netset_iSCSI', 'hypervisor_type': 'Vmware',
                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                 }]

iSCSI_Vol_23 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_23', 'path': 'DC1', 'vcenter': '172.18.13.11',
                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',
                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                 }]

iSCSI_Vol_24 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_24', 'path': 'DC1', 'vcenter': '172.18.13.11',
                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',
                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                      'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': '5.1.0'},
                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                 }]

iSCSI_Vol_25 = [{'type': 'HypervisorClusterProfileV2', 'name': 'iSCSI_Vol_25', 'path': 'DC1', 'vcenter': '172.18.13.11',
                 'profile_name': 'profile_template_vsa', 'hypervisor_type': 'Vmware',
                 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                 'server_hardware': [1],  # 'deployment_manager_type': 'ICSP',
                 'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                      'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': '5.1.0'},
                 'shared_volume': [{'name': 'vsa1', 'volumeFileSystemType': 'VMFS'}]
                 }]

"""
SPT SBAC prereq  data variable file
"""
# #####################################
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

# #####################################

# #########PREREQUISITES###############
ethernet_networks_EG1 = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'corp_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'purpose': 'Management'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '71', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '22', 'purpose': 'VMMigration'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '33', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '35', 'purpose': 'VMMigration'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '11', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '24', 'purpose': 'FaultTolerance'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '101', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '38', 'purpose': 'FaultTolerance'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net_3', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '103', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'untagged_nw_1', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '104', 'purpose': 'General'}]

ethernet_networks_EG2 = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'corp_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'purpose': 'Management'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '72', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '32', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '36', 'purpose': 'VMMigration'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '12', 'purpose': 'General'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '20', 'purpose': 'VMMigration'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '25', 'purpose': 'FaultTolerance'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '39', 'purpose': 'FaultTolerance'},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '102', 'purpose': 'General', "subnetUri": None},
                         {'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'untagged_nw_2', 'connectionTemplateUri': None,
                          'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '105', 'purpose': 'General'}]

ethernet_networks_shared = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'corp', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'purpose': 'Management'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '70', 'purpose': 'General'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'network2', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '37', 'purpose': 'VMMigration'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'net1', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '21', 'purpose': 'VMMigration'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tunnel', 'name': 'tunneled_nw', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '34', 'purpose': 'General'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'corp1', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '10', 'purpose': 'General'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '23', 'purpose': 'FaultTolerance'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'ft_net2', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '40', 'purpose': 'FaultTolerance'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'production', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '100', 'purpose': 'General'},
                            {'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'untagged_nw', 'connectionTemplateUri': None,
                             'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '106', 'purpose': 'General'}]

fc_networks_EG1 = [{'fabricType': 'FabricAttach', 'name': 'san_1', 'autoLoginRedistribution': True, 'linkStabilityTime': 30,
                    'connectionTemplateUri': None, 'type': 'fc-networkV4'}]

fc_networks_EG2 = [{'fabricType': 'FabricAttach', 'name': 'san_2', 'autoLoginRedistribution': True, 'linkStabilityTime': 30,
                   'connectionTemplateUri': None, 'type': 'fc-networkV4'}]

fc_networks_shared = [{'fabricType': 'FabricAttach', 'name': 'san', 'autoLoginRedistribution': True, 'linkStabilityTime': 30,
                       'connectionTemplateUri': None, 'type': 'fc-networkV4'}]

network_sets_EG1 = [{'name': 'netset1_1', 'type': 'network-setV4', 'networkUris': ['net1_1', 'corp1_1'], 'nativeNetworkUri': 'net1_1'},
                    {'name': 'netset2_1', 'type': 'network-setV4', 'networkUris': ['net1_1', 'corp1_1', 'production_1'], 'nativeNetworkUri': 'net1_1'}]

network_sets_EG2 = [{'name': 'netset1_2', 'type': 'network-setV4', 'networkUris': ['net1_2', 'corp1_2'], 'nativeNetworkUri': 'net1_2'},
                    {'name': 'netset2_2', 'type': 'network-setV4', 'networkUris': ['net1_2', 'corp1_2', 'production_2'], 'nativeNetworkUri': 'net1_2'}]

network_sets_shared = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1'], 'nativeNetworkUri': 'net1'},
                       {'name': 'netset2', 'type': 'network-setV4', 'networkUris': ['net1', 'corp1', 'production'], 'nativeNetworkUri': 'net1'}]

uplink_sets1 = {'uplink0': {'name': 'upl_corp',
                            'ethernetNetworkType': 'Untagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['corp'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]},
                'uplink1': {'name': 'upl_corp1',
                            'ethernetNetworkType': 'Untagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['corp_1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.3', 'speed': 'Auto'}]},
                'uplink2': {'name': 'upl_icsp',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['icsp', 'icsp_1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                'uplink3': {'name': 'upl_san',
                            'networkType': 'FibreChannel',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkUris': ['san'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'lacpTimer': 'Long',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
                'uplink4': {'name': 'upl_san1',
                            'networkType': 'FibreChannel',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkUris': ['san_1'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'lacpTimer': 'Long',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'}]}}

uplink_sets2 = {'uplink0': {'name': 'upl_corp',
                            'ethernetNetworkType': 'Untagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['corp'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]},
                'uplink1': {'name': 'upl_corp2',
                            'ethernetNetworkType': 'Untagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['corp_2'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.3', 'speed': 'Auto'}]},
                'uplink2': {'name': 'upl_icsp',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['icsp', 'icsp_2'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                'uplink3': {'name': 'upl_san',
                            'networkType': 'FibreChannel',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkUris': ['san'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'lacpTimer': 'Long',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
                'uplink4': {'name': 'upl_san1',
                            'networkType': 'FibreChannel',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkUris': ['san_2'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'lacpTimer': 'Long',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'}]}}


lig1 = {'name': 'lig',
        'type': 'logical-interconnect-groupV5',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                    {'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}],
        'uplinkSets': [uplink_sets1['uplink0'].copy(), uplink_sets1['uplink1'].copy(), uplink_sets1['uplink2'].copy(), uplink_sets1['uplink3'].copy(), uplink_sets1['uplink4'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net_1', 'corp1', 'net1', 'tunneled_nw', 'production', 'ft_net2', 'ft_net2_1'
                                'corp1_1', 'net1_1', 'tunneled_nw_1', 'production_1', 'untagged_nw', 'untagged_nw_1']
        }


lig2 = {'name': 'lig2',
        'type': 'logical-interconnect-groupV5',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'enclosure': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                    {'enclosure': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}],
        'uplinkSets': [uplink_sets2['uplink0'].copy(), uplink_sets2['uplink1'].copy(), uplink_sets2['uplink2'].copy(), uplink_sets2['uplink3'].copy(), uplink_sets2['uplink4'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net_2', 'corp1', 'net1', 'tunneled_nw', 'production', 'ft_net2', 'ft_net2_2'
                                'corp1_2', 'net1_2', 'tunneled_nw_2', 'production_2', 'untagged_nw', 'untagged_nw_2']}


enc_group1 = {'name': 'enclgrp',
              'enclosureCount': 1,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig'}],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"}

enc_group2 = {'name': 'enclgrp1',
              'enclosureCount': 1,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig2'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig2'}],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"}

enclosures = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None},
              {'hostname': "172.18.1.13", 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp2', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None}]

storage_systems = [{'family': 'StoreServ', 'name': 'ThreePAR-1', 'hostname': '172.18.11.11', 'credentials': {'username': 'dcs', 'password': 'dcs'}}]

update_storage_systems = [{'type': 'StorageSystemV4',
                           'credentials': {'hostname': '172.18.11.11',
                                           'username': 'dcs',
                                           'password': 'dcs'},
                           'family': 'StoreServ',
                           'name': 'ThreePAR-1',
                           "deviceSpecificAttributes": {'managedDomain': 'TestDomain'},
                           'ports': [
                                     {"expectedNetworkUri": "FC:san",
                                      "expectedNetworkName": "san",
                                      "mode": "Managed",
                                      "name": "0:1:1"},
                                     {"expectedNetworkUri": "FC:san_1",
                                      "expectedNetworkName": "san_1",
                                      "mode": "Managed",
                                      "name": "0:1:2"},
                                     {"expectedNetworkUri": "FC:san_2",
                                      "expectedNetworkName": "san_2",
                                      "mode": "Managed",
                                      "name": "1:1:1"}]}]

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

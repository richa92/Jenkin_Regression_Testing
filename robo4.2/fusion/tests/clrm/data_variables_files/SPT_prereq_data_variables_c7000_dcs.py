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
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]},
               'uplink2': {'name': 'upl_icsp',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['icsp'],
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
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]}}

ligs = {'name': 'lig',
        'type': 'logical-interconnect-groupV5',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink2'].copy(), uplink_sets['uplink3'].copy()],
        'internalNetworkUris': ['ft_net', 'ft_net2', 'corp1', 'net1', 'network2', 'tunneled_nw', 'production', 'untagged_nw'],
        "snmpConfiguration":
        {
            "type": "snmp-configuration",
            "readCommunity": "Public",
            "systemContact": "",
            "enabled": True,
            "category": "snmp-configuration",
            "v3Enabled": False
        }
        }

enc_groups = {'name': 'enclgrp',
              'enclosureCount': 1,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig'}],
              'ipAddressingMode': "External",
              'ipRangeUris': [],
              'powerMode': "RedundantPowerFeed"}

enc_group1 = {'name': 'enclgrp1',
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
                           'ports': [
                                     {"expectedNetworkUri": "FC:san",
                                      "expectedNetworkName": "san",
                                      "mode": "Managed",
                                      "name": "0:1:1"}]}]

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

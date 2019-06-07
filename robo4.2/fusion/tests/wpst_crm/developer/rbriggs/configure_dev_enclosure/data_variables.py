def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
#FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': '15.199.x.x',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'ipv4Subnet': '255.255.240.0',
                   'ipv4Gateway': '15.199.224.1',
                   'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
                   'app1Ipv4Addr': '15.199.229.200',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'cic-rb.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

licenses = [{'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
            {'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}]

ethernet_networks = [{'name': 'IC',
                      'type': 'ethernet-networkV300',
                      'vlanId': 1001,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'Untagged',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Tunnel',
                      'type': 'ethernet-networkV3',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'}]

ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 1, 'end': 102, 'name': None, 'type': 'ethernet-networkV3',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False,
                    'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'},
                   {'prefix': 'net_', 'suffix': '', 'start': 200, 'end': 250, 'name': None,
                    'type': 'ethernet-networkV3',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False,
                    'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'}]

fc_networks = [{'name': 'SAN-A', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-B', 'type': 'fc-networkV2', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

network_sets = [{'name': 'NS_23', 'type': 'network-set', 'networkUris': ['net_23'], 'nativeNetworkUri': 'net_23'},
                {'name': 'NS_24', 'type': 'network-set', 'networkUris': ['net_24'], 'nativeNetworkUri': 'net_24'},
                {'name': 'NS_46', 'type': 'network-set', 'networkUris': ['net_46'], 'nativeNetworkUri': 'net_46'},
                {'name': 'NS_47', 'type': 'network-set', 'networkUris': ['net_47'], 'nativeNetworkUri': 'net_47'}]

network_set_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 22, 'name': 'VlanTrunk1', 'type': 'network-set',
                       'networkUris': None, 'nativeNetworkUri': 'net_2'},
                      {'prefix': 'net_', 'suffix': '', 'start': 25, 'end': 45, 'name': 'VlanTrunk2', 'type': 'network-set',
                       'networkUris': None, 'nativeNetworkUri': 'net_25'},
                      {'prefix': 'net_', 'suffix': '', 'start': 50, 'end': 70, 'name': 'VlanTrunk3', 'type': 'network-set',
                       'networkUris': None, 'nativeNetworkUri': 'net_50'},
                      {'prefix': 'net_', 'suffix': '', 'start': 75, 'end': 95, 'name': 'VlanTrunk4', 'type': 'network-set',
                       'networkUris': None, 'nativeNetworkUri': 'net_75'},
                      {'prefix': 'net_', 'suffix': '', 'start': 201, 'end': 210, 'name': 'VlanTrunk5', 'type': 'network-set',
                       'networkUris': None, 'nativeNetworkUri': 'net_201'}]

fcoe_networks = []

fcoe_ranges = [{'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1032},
               {'prefix': 'fcoe-', 'suffix': 'b', 'start': 1001, 'end': 1032},
               {'prefix': 'fcoe-', 'suffix': 'c', 'start': 1001, 'end': 1032},
               {'prefix': 'fcoe-', 'suffix': 'd', 'start': 1001, 'end': 1032}]

enc_groups = [{'name': 'EG',
               'type': 'EnclosureGroupV200',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [{'hostname': '15.199.229.1', 'username': 'Administrator', 'password': 'hpvse1', 'enclosureGroupUri': 'EG:EG',
         'force': False, 'licensingIntent': 'OneViewNoiLO'}]

uplink_sets = {'IC': {'name': 'IC',
                      'ethernetNetworkType': 'Tagged',
                      'networkType': 'Ethernet',
                      'networkUris': ['IC'],
                      'nativeNetworkUri': None,
                      'mode': 'Auto',
                      'logicalPortConfigInfos': [{'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                 {'bay': '2', 'port': 'X4', 'speed': 'Auto'}]},
               'Tunnel1': {'name': 'Tunnel1',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel1'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'},
                                                      {'bay': '2', 'port': 'X7', 'speed': 'Auto'}]},
               'Untagged': {'name': 'Untagged',
                            'ethernetNetworkType': 'Untagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['Untagged'],
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'lacpTimer': 'Long',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X8', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X8', 'speed': 'Auto'}]},
               'SAN-A': {'name': 'SAN-A',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-A'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'SAN-B': {'name': 'SAN-B',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-B'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe1': {'name': 'BigPipe1',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(2, 50) + make_range_list(201, 210),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
               'BigPipe2': {'name': 'BigPipe2',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(51, 102),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
               'bad': {'name': 'badUS',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(51, 102),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
               }

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     ],
         'uplinkSets': [uplink_sets['bad']],
         """
         'uplinkSets': [uplink_sets['IC'],
                        uplink_sets['Tunnel1'],
                        uplink_sets['Untagged'],
                        uplink_sets['SAN-A'],
                        uplink_sets['SAN-B'],
                        uplink_sets['BigPipe1'],
                        uplink_sets['BigPipe2']],
         """
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        ]

badlig = { "enclosureIndexes": None, "enclosureType": "C7000", "ethernetSettings": None, "interconnectBaySet": None, "interconnectMapTemplate": { "interconnectMapEntryTemplates": [ { "enclosureIndex": 1, "logicalLocation": { "locationEntries": [ { "relativeValue": 1, "type": "Bay" }, { "relativeValue": 1, "type": "Enclosure" } ] }, "permittedInterconnectTypeUri": "/rest/interconnect-types/7e6d3be1-d738-4fb3-8d6a-9ab8c8167b4e" }, { "enclosureIndex": 1, "logicalLocation": { "locationEntries": [ { "relativeValue": 2, "type": "Bay" }, { "relativeValue": 1, "type": "Enclosure" } ] }, "permittedInterconnectTypeUri": "/rest/interconnect-types/7e6d3be1-d738-4fb3-8d6a-9ab8c8167b4e" } ] }, "internalNetworkUris": None, "name": "LIG1", "qosConfiguration": None, "redundancyType": None, "snmpConfiguration": None, "stackingMode": None, "state": "Active", "telemetryConfiguration": None, "type": "logical-interconnect-groupV300", "uplinkSets": [ { "ethernetNetworkType": "Tagged", "lacpTimer": "Short", "logicalPortConfigInfos": [ { "desiredSpeed": "Auto", "logicalLocation": { "locationEntries": [ { "relativeValue": 1, "type": "Enclosure" }, { "relativeValue": 5, "type": "Bay" }, { "relativeValue": "22", "type": "Port" } ] } }, { "desiredSpeed": "Auto", "logicalLocation": { "locationEntries": [ { "relativeValue": 1, "type": "Enclosure" }, { "relativeValue": 6, "type": "Bay" }, { "relativeValue": "22", "type": "Port" } ] } } ], "mode": "Auto", "name": "badUS", "nativeNetworkUri": None, "networkType": "Ethernet", "networkUris": [], "primaryPort": None } ] }
telemetry = {'enableTelemetry': True, 'sampleInterval': 400, 'sampleCount': 20}

trapDestinations = [{'trapSeverities': ['Major'],
                     'enetTrapCategories': ['Other'],
                     'fcTrapCategories': ['Other'],
                     'vcmTrapCategories': ['Legacy'],
                     'trapFormat': 'SNMPv1',
                     'trapDestination': '192.168.99.99',
                     'communityString': 'public'}]

snmp = {'snmpAccess': ['192.168.1.0/24'],
        'trapDestinations': trapDestinations}

enet = {'enableFastMacCacheFailover': False}

ranges = [{'name': 'CMAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': '12:11:11:00:00:00', 'endAddress': '12:11:11:0F:FF:FF', 'enabled': True},
          {'name': 'CWWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '10:00:1C:11:00:00:00:00', 'endAddress': '10:00:1C:11:00:0F:FF:FF', 'enabled': True},
          {'name': 'CSN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCU1110000', 'endAddress': 'VCU1110ZZZ', 'enabled': True},
          {"name": "172", "type": "Range", "startAddress": "172.0.0.2", "endAddress": "172.0.0.10", "rangeCategory": "CUSTOM", "subnet": {"networkId": "172.0.0.0", "domain": "test.domain.hp.com", "subnetmask": "255.255.255.0", "gateway": "172.0.0.1", "dnsServers": []}}
          ]

server_profiles = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay1-BL460cGen8-BFS', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '20010002AC003D7E', 'lun': '02'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Virtual',
                    'name': 'Bay2-BL460cGen8-w2012', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:IC',
                                     'boot': {'priority': 'Primary'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'NotBootable'}, 'mactype': 'UserDefined', 'wwpnType': 'UserDefined', 'mac': '12:11:11:00:00:00', 'wwpn': '10:00:1C:11:00:00:00:01', 'wwnn': '10:00:1C:11:00:00:00:00'},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-B',
                                     'boot': {'priority': 'NotBootable'}, 'mactype': 'UserDefined', 'wwpnType': 'UserDefined', 'mac': '12:11:11:00:00:01', 'wwpn': '10:00:1C:11:00:00:00:03', 'wwnn': '10:00:1C:11:00:00:00:02'},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk2',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d',
                                     'requestedMbps': '2500', 'networkUri': 'NS:NS_23',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d',
                                     'requestedMbps': '2500', 'networkUri': 'NS:NS_23',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay3-BL465cGen8-esxi55', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-B',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 4',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay4-BL460cGen8-vCenter', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 9',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay9-BL465cGen8-esxi1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-B',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 10',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay10-BL465cGen8-esxi2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-B',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay11-BL460cGen9-esxi6.0a', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI'},
                    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-B',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PAAR63-EN1, bay 12',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PAAR63-EN1', 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Bay11-BL460cGen9-esxi6.0b', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI'},
                    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'FC:SAN-B',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}

                   ]
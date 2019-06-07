def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

lig1_ethernetsettings = {'type': 'EthernetInterconnectSettingsV3', 'enableRichTLV': True, 'interconnectType': 'Ethernet'}

li_set1_f702 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": True, "enableTaggedLldp": True}
li_set1 = {"type": "EthernetInterconnectSettingsV4", "enableTaggedLldp": True, "lldpIpAddressMode": "IPV4"}
li_set2 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": False, "enableTaggedLldp": True}
li_set3 = {"type": "EthernetInterconnectSettingsV4", "enableTaggedLldp": False, "lldpIpAddressMode": "IPV4"}
li_set4 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": False, "enableTaggedLldp": False}

li_set5 = {"type": "EthernetInterconnectSettingsV4", "enableTaggedLldp": True, "lldpIpAddressMode": "IPV6"}
li_set6 = {"type": "EthernetInterconnectSettingsV4", "enableTaggedLldp": False, "lldpIpAddressMode": "IPV6"}

li_set7 = {"type": "EthernetInterconnectSettingsV4", "enableTaggedLldp": True, "lldpIpAddressMode": "BOTH_IPV4_IPV6"}
li_set8 = {"type": "EthernetInterconnectSettingsV4", "enableTaggedLldp": False, "lldpIpAddressMode": "BOTH_IPV4_IPV6"}

apic_admin_credentials = {"aaaUser": {
    "attributes": {
        "name": "admin", "pwd": "password"}}}

apic_ip = ['10.10.0.203', '10.10.5.16']

li_spp_downgrade = {'command': 'UPDATE', 'sppUri': '/rest/firmware-drivers/SPP2014090_2014_0710_89', 'force': True}

li_spp_upgrade = {'command': 'UPDATE', 'sppUri': '/rest/firmware-drivers/SPP2015090_2015_0825_54', 'force': False}

les_tbird = [{'name': 'LE',
              # 'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66103'],
              'enclosureUris': ['ENC:IRTQI6MH9D'],  # REAL
              'enclosureGroupUri': 'EG:EGLldp',
              'firmwareBaselineUri': None,
              'forceInstallFirmware': False
              }]

downlink_enable = {'interconnectName': 'EM1FFFF500, interconnect 3', 'enabled': True,
                   'portName': 'd4',
                   'type': 'port',
                   }

downlink_disable = {'interconnectName': 'EM1FFFF500, interconnect 3', 'enabled': False,
                    'portName': 'd4',
                    'type': 'port',
                    }

les_tbird_ME = [{'name': 'LE',
                 'enclosureUris': ['ENC:IRTQI6MH9D', 'ENC:EM1FFFF600'],  # REAL
                 'enclosureGroupUri': 'EG:EGLldp',
                 'firmwareBaselineUri': None,
                 'forceInstallFirmware': False
                 }]


les_tbird_Multi_LIG = [{'name': 'LE',
                        'enclosureUris': ['ENC:IRTQI6MH9D', 'ENC:EM1FFFF600'],  # REAL
                        'enclosureGroupUri': 'EG:EGLldp',
                        'firmwareBaselineUri': None,
                        'forceInstallFirmware': False
                        }]

subnet = [{'type': 'Subnet',
           'gateway': '15.212.137.1',
           'networkId': '15.212.137.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'hpe.com'}]

ipv4ranges_old = [{'type': 'Range',
                   'startAddress': '15.212.137.12',
                   'endAddress': '15.212.137.14',
                   'name': 'Test',
                   'subnetUri': ' '}]

ipv4ranges = [{'type': 'Range',
               'startAddress': '15.212.137.17',
               'endAddress': '15.212.137.22',
               'name': 'Test',
               'subnetUri': ' '}]


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

licenses = [{'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
            {'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
            ]

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM', 'startAddress': 'AA:AA:AA:00:00:00', 'endAddress': 'AA:AA:AA:00:00:80', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM', 'startAddress': '2A:AA:AA:AA:AA:AA:AA:AA', 'endAddress': '2A:AA:AA:AA:AA:AA:AB:29', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM', 'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

ethernet_networks1_201 = [{'name': 'eth-100',
                           'type': 'ethernet-networkV3',
                           'vlanId': 100,
                           'purpose': 'General',
                           'smartLink': True,
                           'privateNetwork': False,
                           'connectionTemplateUri': None,
                           'ethernetNetworkType': 'Tunnel'},
                          {'name': 'eth-101',
                           'type': 'ethernet-networkV3',
                           'vlanId': 101,
                           'purpose': 'General',
                           'smartLink': True,
                           'privateNetwork': False,
                           'connectionTemplateUri': None,
                           'ethernetNetworkType': 'Tunnel'},
                          ]

ethernet_networks1 = [{'name': 'eth-101',
                       'type': 'ethernet-networkV300',
                       'vlanId': 100,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},

                      ]
ethernet_networks = [{'name': 'eth-100',
                      'type': 'ethernet-networkV3',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-101',
                      'type': 'ethernet-networkV3',
                      'vlanId': 101,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-102',
                      'type': 'ethernet-networkV3',
                      'vlanId': 102,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-a',
                      'type': 'ethernet-networkV3',
                      'vlanId': 200,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-b',
                      'type': 'ethernet-networkV3',
                      'vlanId': 201,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-c',
                      'type': 'ethernet-networkV3',
                      'vlanId': 202,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-d',
                      'type': 'ethernet-networkV3',
                      'vlanId': 203,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'network-e',
                      'type': 'ethernet-networkV3',
                      'vlanId': 204,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},

                     ]

network_sets = [{'name': 'netset1', 'type': 'network-set', 'networkUris': ['network-a'], 'nativeNetworkUri': None}]

fcoe_networks = {'fcoe-1': {'name': 'fcoe-1', 'type': 'fcoe-network', 'vlanId': 1},
                 'fcoe-100': {'name': 'fcoe-100', 'type': 'fcoe-network', 'vlanId': 100},
                 'fcoe-2000': {'name': 'fcoe-2000', 'type': 'fcoe-network', 'vlanId': 2000},
                 'fcoe-100b': {'name': 'fcoe-100b', 'type': 'fcoe-network', 'vlanId': 100},
                 'fcnetwork-a': {'name': 'fcnetwork-a', 'type': 'fcoe-network', 'vlanId': 209},
                 'network-a': {'name': 'network-a', 'type': 'fcoe-network', 'vlanId': 210},
                 'network-b': {'name': 'network-b', 'type': 'fcoe-network', 'vlanId': 211},
                 'no-vlanId': {'name': 'no-vlanId', 'type': 'fcoe-network'},
                 'fcoe-4095': {'name': 'fcoe-4095', 'type': 'fcoe-network', 'vlanId': 4095}}

fcoe_ranges = {'fcoe-range32a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1032},
               'fcoe-range32b': {'prefix': 'fcoe-', 'suffix': 'b', 'start': 1001, 'end': 1032},
               'fcoe-range32c': {'prefix': 'fcoe-', 'suffix': 'c', 'start': 1001, 'end': 1032},
               'fcoe-range32d': {'prefix': 'fcoe-', 'suffix': 'd', 'start': 1001, 'end': 1032},
               'fcoe-range33': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1033},
               'fcoe-range30a': {'prefix': 'fcoe-', 'suffix': 'a', 'start': 1001, 'end': 1030},
               'fcoe-range128': {'prefix': 'fcoe-', 'suffix': '', 'start': 1001, 'end': 1128},
               'fcoe-range-delete-20': {'prefix': 'fcoe-', 'suffix': '', 'start': 1109, 'end': 1128}
               }

fc_networks = [{'type': 'fc-networkV2',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'fcnetwork-a',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]
enc_group_201 = {'name': 'EGLldp',
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
                     {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}


enc_group_tbird = [{'name': 'EGLldp',
                    'type': 'EnclosureGroupV300',
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'interconnectBayMappingCount': 2,
                    'configurationScript': None,
                    'powerMode': 'RedundantPowerFeed',
                    'ipAddressingMode': 'IpPool',
                    'enclosureCount': 1,
                    'ipRangeUris': '',
                    'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG2'}
                     ]}]


enc_group_tbird_ME = [{'name': 'EGLldp',
                       'type': 'EnclosureGroupV300',
                       'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                       'stackingMode': 'Enclosure',
                       'interconnectBayMappingCount': 2,
                       'configurationScript': None,
                       'powerMode': 'RedundantPowerFeed',
                       'ipAddressingMode': 'IpPool',
                       'enclosureCount': 2,
                       'ipRangeUris': '',
                       'interconnectBayMappings':
                       [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                           {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
                        ]}]


enc_group_tbird_Multi_LIG = [{'name': 'EGLldp',
                              'type': 'EnclosureGroupV300',
                              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                              'stackingMode': 'Enclosure',
                              'interconnectBayMappingCount': 2,
                              'configurationScript': None,
                              'powerMode': 'RedundantPowerFeed',
                              'ipAddressingMode': 'IpPool',
                              'enclosureCount': 2,
                              'ipRangeUris': '',
                              'interconnectBayMappings':
                              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                                  {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                  {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                  {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}

                               ]}]

enc_group_02 = {'name': 'EGLldp',
                'type': 'EnclosureGroupV200',
                'enclosureTypeUri': '/rest/enclosure-types/c7000',
                'stackingMode': 'Enclosure',
                'interconnectBayMappingCount': 8,
                'configurationScript': None,
                'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}


encDCS = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:EGLldp', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]
encREAL1 = [{'hostname': '10.10.0.2', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EGLldp', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]
encREAL = [{'hostname': '10.10.0.26', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EGLldp', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]

encs = encREAL

ENC1 = 'WPST-PABA58-EN1'
LE = 'WPST-PABA58-EN1'
LIG1 = 'LIG'
LIG2 = 'LIG1'


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
               'app1Ipv4Addr': '15.199.229.190',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'f100.usa.hp.com',
               'confOneNode': True,
               'domainName': 'usa.hp.com',
               'aliasDisabled': True,
               }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

uplink_sets_f702 = {'us1': {'name': 'us1',
                            'ethernetNetworkType': 'Tunnel',
                            'networkType': 'Ethernet',
                            'networkUris': ['eth-100'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                       ]},
                    'us2': {'name': 'us2',
                            'ethernetNetworkType': 'Tunnel',
                            'networkType': 'Ethernet',
                            'networkUris': ['eth-101'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                       ]},
                    'us3': {'name': 'us3',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X4', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                       {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
                    'us33': {'name': 'us-33-exceeds-32',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': make_range_list(**fcoe_ranges['fcoe-range33']),
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '4', 'port': 'X2', 'speed': 'Auto'},
                                                        {'bay': '4', 'port': 'X3', 'speed': 'Auto'},
                                                        {'bay': '4', 'port': 'X4', 'speed': 'Auto'}]},
                    'us1-b': {'name': 'us1-b-removed X10, 30 networks',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list(**fcoe_ranges['fcoe-range30a']),
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X7', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X8', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X9', 'speed': 'Auto'}]},

                    'us1-c': {'name': 'us-3-exceeds-32max',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': ['fcoe-1001', 'fcoe-1002', 'fcoe-1003'],
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X10', 'speed': 'Auto'}]},
                    'us1-d': {'name': 'us1',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list(**fcoe_ranges['fcoe-range32a']),
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                         {'bay': '1', 'port': 'X4', 'speed': 'Auto'}]},
                    'us1-eth': {'name': 'us1-eth',
                                'ethernetNetworkType': 'Tagged',
                                'networkType': 'Ethernet',
                                'networkUris': ['network-d'],
                                'primaryPort': None,
                                'nativeNetworkUri': None,
                                'mode': 'Auto',
                                'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                           {'bay': '1', 'port': 'X6', 'speed': 'Auto'}]},
                    'us2-d': {'name': 'us2',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list(**fcoe_ranges['fcoe-range32b']),
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '3', 'port': 'X2', 'speed': 'Auto'}]},
                    'us2-fc': {'name': 'us2-fc',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'FibreChannel',
                               'networkUris': ['fcnetwork-a'],
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                          {'bay': '3', 'port': 'X4', 'speed': 'Auto'}]},
                    'us3-d': {'name': 'us3',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                         {'bay': '5', 'port': 'X4', 'speed': 'Auto'}]},
                    'us3-eth': {'name': 'us3-eth',
                                'ethernetNetworkType': 'Tagged',
                                'networkType': 'Ethernet',
                                'networkUris': ['network-e'],
                                'primaryPort': None,
                                'nativeNetworkUri': None,
                                'mode': 'Auto',
                                'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                           {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                           {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                           {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
                    'us3-2ics': {'name': 'us2-ics',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['fcoe-100'],
                                 'primaryPort': None,
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                            {'bay': '6', 'port': 'X5', 'speed': 'Auto'}]},
                    'unsupported-ics': {'name': 'unsupported-ics',
                                        'ethernetNetworkType': 'Tagged',
                                        'networkType': 'Ethernet',
                                        'networkUris': ['fcoe-100'],
                                        'primaryPort': None,
                                        'nativeNetworkUri': None,
                                        'mode': 'Auto',
                                        'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
                    'unsupported-ics2': {'name': 'unsupported-ics2',
                                         'ethernetNetworkType': 'Tagged',
                                         'networkType': 'Ethernet',
                                         'networkUris': ['fcoe-100'],
                                         'primaryPort': None,
                                         'nativeNetworkUri': None,
                                         'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'bay': '1', 'port': '1', 'speed': 'Auto'}]},
                    'duplicate-vlan': {'name': 'duplicate-vlan',
                                       'ethernetNetworkType': 'Tagged',
                                       'networkType': 'Ethernet',
                                       'networkUris': ['eth-100', 'fcoe-100'],
                                       'primaryPort': None,
                                       'nativeNetworkUri': None,
                                       'mode': 'Auto',
                                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
                    'BFS': {'name': 'BFS',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['eth-102', 'fcoe-1002'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
                    'BFS-fcoe': {'name': 'BFS-fcoe',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['fcoe-1002'],
                                 'primaryPort': None,
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
                    }


uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-200'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               'us3': {'name': 'us3',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X4', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                  {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
               'us33': {'name': 'us-33-exceeds-32',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': make_range_list(**fcoe_ranges['fcoe-range33']),
                        'primaryPort': None,
                        'nativeNetworkUri': None,
                        'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                   {'bay': '4', 'port': 'X2', 'speed': 'Auto'},
                                                   {'bay': '4', 'port': 'X3', 'speed': 'Auto'},
                                                   {'bay': '4', 'port': 'X4', 'speed': 'Auto'}]},
               'us1-b': {'name': 'us1-b-removed X10, 30 networks',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range30a']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X7', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X8', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X9', 'speed': 'Auto'}]},

               'us1-c': {'name': 'us-3-exceeds-32max',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['fcoe-1001', 'fcoe-1002', 'fcoe-1003'],
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X10', 'speed': 'Auto'}]},
               'us1-d': {'name': 'us1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range32a']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X4', 'speed': 'Auto'}]},
               'us1-eth': {'name': 'us1-eth',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['network-d'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                      {'bay': '1', 'port': 'X6', 'speed': 'Auto'}]},
               'us2-d': {'name': 'us2',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range32b']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X2', 'speed': 'Auto'}]},
               'us2-fc': {'name': 'us2-fc',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'FibreChannel',
                          'networkUris': ['fcnetwork-a'],
                          'primaryPort': None,
                          'nativeNetworkUri': None,
                          'mode': 'Auto',
                          'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                     {'bay': '3', 'port': 'X4', 'speed': 'Auto'}]},
               'us3-d': {'name': 'us3',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                         'primaryPort': None,
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                    {'bay': '5', 'port': 'X4', 'speed': 'Auto'}]},
               'us3-eth': {'name': 'us3-eth',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['network-e'],
                           'primaryPort': None,
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
               'us3-2ics': {'name': 'us2-ics',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['fcoe-100'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                       {'bay': '6', 'port': 'X5', 'speed': 'Auto'}]},
               'unsupported-ics': {'name': 'unsupported-ics',
                                   'ethernetNetworkType': 'Tagged',
                                   'networkType': 'Ethernet',
                                   'networkUris': ['fcoe-100'],
                                   'primaryPort': None,
                                   'nativeNetworkUri': None,
                                   'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
               'unsupported-ics2': {'name': 'unsupported-ics2',
                                    'ethernetNetworkType': 'Tagged',
                                    'networkType': 'Ethernet',
                                    'networkUris': ['fcoe-100'],
                                    'primaryPort': None,
                                    'nativeNetworkUri': None,
                                    'mode': 'Auto',
                                    'logicalPortConfigInfos': [{'bay': '1', 'port': '1', 'speed': 'Auto'}]},
               'duplicate-vlan': {'name': 'duplicate-vlan',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['eth-100', 'fcoe-100'],
                                  'primaryPort': None,
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
               'BFS': {'name': 'BFS',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-102', 'fcoe-1002'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'BFS-fcoe': {'name': 'BFS-fcoe',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': ['fcoe-1002'],
                            'primaryPort': None,
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               }

uplink_sets_tbird = {'us1': {'name': 'Uplinkset1',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['eth-101'],
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},

                                                        {'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},


                                                        ]},


                     'us1_ME': {'name': 'Uplinkset1',
                                'ethernetNetworkType': 'Tunnel',
                                'networkType': 'Ethernet',
                                'networkUris': ['eth-101'],
                                'primaryPort': None,
                                'nativeNetworkUri': None,
                                'mode': 'Auto',
                                'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q5.1', 'speed': 'Auto'},
                                                           {'bay': '6', 'enclosure': '2', 'port': 'Q5.1', 'speed': 'Auto'}

                                                           ]},

                     'us1_ME_Multi_LIG': {'name': 'Uplinkset1',
                                          'ethernetNetworkType': 'Tunnel',
                                          'networkType': 'Ethernet',
                                          'networkUris': ['eth-101'],
                                          'primaryPort': None,
                                          'nativeNetworkUri': None,
                                          'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q5.1', 'speed': 'Auto'},
                                                                     {'bay': '6', 'enclosure': '2', 'port': 'Q5.1', 'speed': 'Auto'}

                                                                     ]},

                     'us1_ME_Multi_LIG1': {'name': 'Uplinkset2',
                                           'ethernetNetworkType': 'Tunnel',
                                           'networkType': 'Ethernet',
                                           'networkUris': ['eth-101'],
                                           'primaryPort': None,
                                           'nativeNetworkUri': None,
                                           'mode': 'Auto',
                                           'logicalPortConfigInfos': [{'bay': '2', 'enclosure': '1', 'port': 'Q5.1', 'speed': 'Auto'},
                                                                      {'bay': '5', 'enclosure': '2', 'port': 'Q5.1', 'speed': 'Auto'}

                                                                      ]},


                     'us1_ME_LIG1': {'name': 'Us1',
                                     'ethernetNetworkType': 'Tunnel',
                                     'networkType': 'Ethernet',
                                     'networkUris': ['eth-101'],
                                     'primaryPort': None,
                                     'nativeNetworkUri': None,
                                     'mode': 'Auto',
                                     'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q5.1', 'speed': 'Auto'}
                                                                ]},


                     'us1_ME_LIG2': {'name': 'Us2',
                                     'ethernetNetworkType': 'Tunnel',
                                     'networkType': 'Ethernet',
                                     'networkUris': ['eth-101'],
                                     'primaryPort': None,
                                     'nativeNetworkUri': None,
                                     'mode': 'Auto',
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '2', 'port': 'Q5.1', 'speed': 'Auto'}
                                                                ]},

                     'us1_SE_Multi_LIG': {'name': 'Uplinkset1',
                                          'ethernetNetworkType': 'Tunnel',
                                          'networkType': 'Ethernet',
                                          'networkUris': ['eth-101'],
                                          'primaryPort': None,
                                          'nativeNetworkUri': None,
                                          'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q5.1', 'speed': 'Auto'},
                                                                     {'bay': '6', 'enclosure': '1', 'port': 'Q5.1', 'speed': 'Auto'}

                                                                     ]},



                     'us2': {'name': 'us2',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['eth-101'],
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                        ]},
                     'us3': {'name': 'us3',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X4', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                        {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
                     'us33': {'name': 'us-33-exceeds-32',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': make_range_list(**fcoe_ranges['fcoe-range33']),
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                         {'bay': '4', 'port': 'X2', 'speed': 'Auto'},
                                                         {'bay': '4', 'port': 'X3', 'speed': 'Auto'},
                                                         {'bay': '4', 'port': 'X4', 'speed': 'Auto'}]},
                     'us1-b': {'name': 'us1-b-removed X10, 30 networks',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': make_range_list(**fcoe_ranges['fcoe-range30a']),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X4', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X7', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X8', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X9', 'speed': 'Auto'}]},

                     'us1-c': {'name': 'us-3-exceeds-32max',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['fcoe-1001', 'fcoe-1002', 'fcoe-1003'],
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X10', 'speed': 'Auto'}]},
                     'us1-d': {'name': 'us1',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': make_range_list(**fcoe_ranges['fcoe-range32a']),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X3', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'X4', 'speed': 'Auto'}]},
                     'us1-eth': {'name': 'us1-eth',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['network-d'],
                                 'primaryPort': None,
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                            {'bay': '1', 'port': 'X6', 'speed': 'Auto'}]},
                     'us2-d': {'name': 'us2',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': make_range_list(**fcoe_ranges['fcoe-range32b']),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '3', 'port': 'X2', 'speed': 'Auto'}]},
                     'us2-fc': {'name': 'us2-fc',
                                'ethernetNetworkType': 'Tagged',
                                'networkType': 'FibreChannel',
                                'networkUris': ['fcnetwork-a'],
                                'primaryPort': None,
                                'nativeNetworkUri': None,
                                'mode': 'Auto',
                                'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                                           {'bay': '3', 'port': 'X4', 'speed': 'Auto'}]},
                     'us3-d': {'name': 'us3',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': make_range_list(**fcoe_ranges['fcoe-range32c']),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                          {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                          {'bay': '5', 'port': 'X3', 'speed': 'Auto'},
                                                          {'bay': '5', 'port': 'X4', 'speed': 'Auto'}]},
                     'us3-eth': {'name': 'us3-eth',
                                 'ethernetNetworkType': 'Tagged',
                                 'networkType': 'Ethernet',
                                 'networkUris': ['network-e'],
                                 'primaryPort': None,
                                 'nativeNetworkUri': None,
                                 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                            {'bay': '5', 'port': 'X6', 'speed': 'Auto'},
                                                            {'bay': '5', 'port': 'X7', 'speed': 'Auto'},
                                                            {'bay': '5', 'port': 'X8', 'speed': 'Auto'}]},
                     'us3-2ics': {'name': 'us2-ics',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['fcoe-100'],
                                  'primaryPort': None,
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '5', 'port': 'X5', 'speed': 'Auto'},
                                                             {'bay': '6', 'port': 'X5', 'speed': 'Auto'}]},
                     'unsupported-ics': {'name': 'unsupported-ics',
                                         'ethernetNetworkType': 'Tagged',
                                         'networkType': 'Ethernet',
                                         'networkUris': ['fcoe-100'],
                                         'primaryPort': None,
                                         'nativeNetworkUri': None,
                                         'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
                     'unsupported-ics2': {'name': 'unsupported-ics2',
                                          'ethernetNetworkType': 'Tagged',
                                          'networkType': 'Ethernet',
                                          'networkUris': ['fcoe-100'],
                                          'primaryPort': None,
                                          'nativeNetworkUri': None,
                                          'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'bay': '1', 'port': '1', 'speed': 'Auto'}]},
                     'duplicate-vlan': {'name': 'duplicate-vlan',
                                        'ethernetNetworkType': 'Tagged',
                                        'networkType': 'Ethernet',
                                        'networkUris': ['eth-100', 'fcoe-100'],
                                        'primaryPort': None,
                                        'nativeNetworkUri': None,
                                        'mode': 'Auto',
                                        'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
                     'BFS': {'name': 'BFS',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['eth-102', 'fcoe-1002'],
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
                     'BFS-fcoe': {'name': 'BFS-fcoe',
                                  'ethernetNetworkType': 'Tagged',
                                  'networkType': 'Ethernet',
                                  'networkUris': ['fcoe-1002'],
                                  'primaryPort': None,
                                  'nativeNetworkUri': None,
                                  'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
                     }
icmap_02 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric-20/40 F8 Module'},

            ]
icmap_F702 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},

              ]

icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
         ]

icmap_ME = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
            {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
            {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
            ]

icmap_ME_LIG1 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                 {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
                 ]

icmap_ME_LIG2 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
                 {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                 ]


icmap_ME_Multi_LIG = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 3, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'}
]


icmap_ME_Multi_LIG1 = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 2, 'type': 'Synergy 20Gb Interconnect Link Module'},
    {'enclosure': 2, 'enclosureIndex': 2, 'bay': 5, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'}
]

icmap_SE_Multi_LIG = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
]


icmap2 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10 Enet Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10 Enet Module'}]

icmap3 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC 8Gb 20-Port FC Module'}]

icmap4 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10 Enet Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10 Enet Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
          {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
          ]

ligs_201 = {'lig1':
            {'name': 'LIG1',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': icmap,
             'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None},

            'ligTT':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
             'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None},

            'ligFT':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
             'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None},

            'ligTF':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None},

            'ligFF':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None}
            }


ligs = {'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligTTT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligFT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligTF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligFF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},


        'ligF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureIndexes': [1],
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'interconnectBaySet': 3,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'redundancyType': 'Redundant',
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureIndexes': [1],
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'interconnectBaySet': 3,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'redundancyType': 'Redundant',
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}

        }

ligs_tbird = {'lig1':
              {'name': 'LIG2',
               'type': 'logical-interconnect-groupV300',
               'enclosureType': 'SY12000',
               'interconnectMapTemplate': icmap,
               'uplinkSets': [uplink_sets_tbird['us1']],
               # 'uplinkSets': [],
               'interconnectBaySet': 3,
               'redundancyType': 'Redundant',
               'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
               'state': 'Active',
               'telemetryConfiguration': None,
               'snmpConfiguration': None}
              }


ligs_tbird_ME_1 = {'lig1':
                   {'name': 'LIG1',
                    'type': 'logical-interconnect-groupV300',
                    'enclosureType': 'SY12000',
                    'enclosureIndexes': [1, 2],
                    'interconnectMapTemplate': icmap_ME,
                    'uplinkSets': [uplink_sets_tbird['us1_ME']],
                    # 'uplinkSets': [],
                    'interconnectBaySet': 3,
                    'redundancyType': 'HighlyAvailable',
                    'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': None}
                   }

ligs_tbird_ME_LIG = {'lig1':
                     {'name': 'LIG',
                      'type': 'logical-interconnect-groupV300',
                      'enclosureType': 'SY12000',
                      'enclosureIndexes': [1, 2],
                      'interconnectMapTemplate': icmap_ME_LIG1,
                      'uplinkSets': [uplink_sets_tbird['us1_ME_LIG1']],
                      # 'uplinkSets': [],
                      'interconnectBaySet': 3,
                      'redundancyType': 'NonRedundantASide',
                      'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                      'state': 'Active',
                      'telemetryConfiguration': None,
                      'snmpConfiguration': None},

                     'lig2':
                     {'name': 'LIG_4',
                      'type': 'logical-interconnect-groupV300',
                      'enclosureType': 'SY12000',
                      'enclosureIndexes': [1, 2],
                      'interconnectMapTemplate': icmap_ME_LIG2,
                      'uplinkSets': [uplink_sets_tbird['us1_ME_LIG2']],
                      # 'uplinkSets': [],
                      'interconnectBaySet': 3,
                      'redundancyType': 'NonRedundantBSide',
                      'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                      'state': 'Active',
                      'telemetryConfiguration': None,
                      'snmpConfiguration': None}
                     }


ligs_tbird_ME_Multi_LIG = {'lig1':
                           {'name': 'LIG',
                            'type': 'logical-interconnect-groupV4',
                            'enclosureType': 'SY12000',
                            'enclosureIndexes': [1],
                            'interconnectMapTemplate': icmap_SE_Multi_LIG,
                            'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG']],
                            # 'uplinkSets': [],
                            'interconnectBaySet': 3,
                            'redundancyType': 'HighlyAvailable',
                            'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None},

                           'lig2':
                           {'name': 'LIG1',
                            'type': 'logical-interconnect-groupV300',
                            'enclosureType': 'SY12000',
                            'enclosureIndexes': [1, 2],
                            'interconnectMapTemplate': icmap_ME_Multi_LIG1,
                            'uplinkSets': [uplink_sets_tbird['us1_ME_Multi_LIG1']],
                            # 'uplinkSets': [],
                            'interconnectBaySet': 2,
                            'redundancyType': 'HighlyAvailable',
                            'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None}
                           }

enc_group_tbird_SE_Multi_LIG = [{'name': 'EGLldp',
                                 # 'type': 'EnclosureGroupV7',
                                 # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                 # 'stackingMode': 'Enclosure',
                                 'configurationScript': None,
                                 'powerMode': 'RedundantPowerFeed',
                                 'ipAddressingMode': 'IpPool',
                                 'enclosureCount': 1,
                                 # 'enclosureType':'TClass',
                                 'ipRangeUris': '',
                                 'interconnectBayMappings':
                                 [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}
                                  ]}]

subnet = [{'type': 'Subnet',
           'gateway': '192.168.144.1',
           'networkId': '192.168.144.0',
           'subnetmask': '255.255.248.0',
           'dnsServers': [],
           'domain': 'hpe.com'}]

ipv4ranges = [{'type': 'Range',
               'startAddress': '192.168.144.67',
               'endAddress': '192.168.144.70',
               'name': 'Test',
               'subnetUri': ' '}]

ipv4ranges1 = [{'type': 'Range',
                'startAddress': '192.168.144.81',
                'endAddress': '192.168.144.82',
                'name': 'Test1',
                'subnetUri': ' '}]

ligs_tbird_SE_Multi_LIG = {'lig1':
                           {'name': 'LIG',
                            'type': 'logical-interconnect-groupV4',
                            'enclosureType': 'SY12000',
                            'enclosureIndexes': [1],
                            'interconnectMapTemplate': icmap_SE_Multi_LIG,
                            'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG']],
                            # 'uplinkSets': [],
                            'interconnectBaySet': 3,
                            'redundancyType': 'Redundant',
                            'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableNetworkLoopProtection': True, 'igmpIdleTimeoutInterval': 260, 'enableIgmpSnooping': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                            'state': 'Active',
                            'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 300},
                            'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'enabled': True, 'category': 'snmp-configuration'}}}


enc_group_tbird_SE_dhcp = [{'name': 'EGLldp',
                            'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'}],
                            'ipAddressingMode': 'DHCP',
                            'ipRangeUris': [], 'enclosureCount':1,
                            'powerMode':'RedundantPowerFeed', 'ambientTemperatureMode':'Standard'
                            }]

les_tbird_SE_Multi_LIG = [{'name': 'LE',
                           'enclosureUris': ['ENC:EM1FFFF500'],  # REAL
                           'enclosureGroupUri': 'EG:EGLldp',
                           'firmwareBaselineUri': None,
                           'forceInstallFirmware': False
                           }]

server_profiles_tbird_Multi_LIG = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'EM1FFFF500, bay 4', 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:EM1FFFF500', 'enclosureGroupUri': 'EG:EGLldp',
                                    'name': 'Sp_APIC_ENC1_BAY4', 'description': '', 'affinity': 'Bay', 'boot': {'manageBoot': False},
                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 3:1-a',
                                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 3:2-a',
                                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''}]}]
edit_ligs_tbird_ME_LIG = {'ligTT':
                          {'name': 'LIG',
                           'type': 'logical-interconnect-groupV300',
                           'enclosureType': 'SY12000',
                           'interconnectMapTemplate': icmap,
                           'uplinkSets': [uplink_sets_tbird['us1']],
                           'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligF':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV3',
                              'enclosureIndexes': [1, 2],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_ME_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_ME_Multi_LIG'].copy()],
                              'redundancyType': 'HighlyAvailable',
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligT':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV3',
                              'enclosureIndexes': [1, 2],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_ME_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_ME_Multi_LIG'].copy()],
                              'redundancyType': 'HighlyAvailable',
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None}
                          }

edit_ligs_tbird_ME_LIG1 = {'ligTT':
                           {'name': 'LIG',
                            'type': 'logical-interconnect-groupV300',
                            'enclosureType': 'SY12000',
                            'interconnectMapTemplate': icmap,
                            'uplinkSets': [uplink_sets_tbird['us1']],
                            'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                               'state': 'Active',
                               'telemetryConfiguration': None,
                               'snmpConfiguration': None},

                           'ligF':
                           {'name': 'LIG1',
                               'type': 'logical-interconnect-groupV3',
                               'enclosureIndexes': [1, 2],
                               'enclosureType': 'SY12000',
                               'interconnectMapTemplate': icmap_ME_Multi_LIG1,
                               'interconnectBaySet': 2,
                               'uplinkSets': [uplink_sets_tbird['us1_ME_Multi_LIG1'].copy()],
                               'redundancyType': 'HighlyAvailable',
                               'stackingMode': 'Enclosure',
                               'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                               'state': 'Active',
                               'telemetryConfiguration': None,
                               'snmpConfiguration': None},

                           'ligT':
                           {'name': 'LIG1',
                               'type': 'logical-interconnect-groupV3',
                               'enclosureIndexes': [1, 2],
                               'enclosureType': 'SY12000',
                               'interconnectMapTemplate': icmap_ME_Multi_LIG1,
                               'interconnectBaySet': 2,
                               'uplinkSets': [uplink_sets_tbird['us1_ME_Multi_LIG1'].copy()],
                               'redundancyType': 'HighlyAvailable',
                               'stackingMode': 'Enclosure',
                               'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                               'state': 'Active',
                               'telemetryConfiguration': None,
                               'snmpConfiguration': None}
                           }

ligs_tbird_ME = {'ligTT':
                 {'name': 'LIG',
                  'type': 'logical-interconnect-groupV300',
                  'enclosureType': 'SY12000',
                  'interconnectMapTemplate': icmap,
                  'uplinkSets': [uplink_sets_tbird['us1']],
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None},

                 'ligF':
                 {'name': 'LIG1',
                     'type': 'logical-interconnect-groupV3',
                  'enclosureIndexes': [1, 2],
                     'enclosureType': 'SY12000',
                     'interconnectMapTemplate': icmap_ME,
                     'interconnectBaySet': 3,
                     'uplinkSets': [uplink_sets_tbird['us1_ME'].copy()],
                     'redundancyType': 'HighlyAvailable',
                     'stackingMode': 'Enclosure',
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                     'state': 'Active',
                     'telemetryConfiguration': None,
                     'snmpConfiguration': None},

                 'ligT':
                 {'name': 'LIG1',
                     'type': 'logical-interconnect-groupV3',
                     'enclosureIndexes': [1, 2],
                     'enclosureType': 'SY12000',
                     'interconnectMapTemplate': icmap_ME,
                     'interconnectBaySet': 3,
                     'uplinkSets': [uplink_sets_tbird['us1_ME'].copy()],
                     'redundancyType': 'HighlyAvailable',
                     'stackingMode': 'Enclosure',
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                     'state': 'Active',
                     'telemetryConfiguration': None,
                     'snmpConfiguration': None}
                 }


ligs_f702 = {'lig1':
             {'name': 'LIG1',
              'type': 'logical-interconnect-groupV3',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': icmap,
              'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': None,
              'snmpConfiguration': None},

             'ligTT':
             {'name': 'LIG1',
                 'type': 'logical-interconnect-groupV3',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': icmap,
                 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                 'stackingMode': 'Enclosure',
              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},

             'ligFT':
             {'name': 'LIG1',
                 'type': 'logical-interconnect-groupV3',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': icmap,
                 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                 'stackingMode': 'Enclosure',
              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},

             'ligTF':
             {'name': 'LIG1',
                 'type': 'logical-interconnect-groupV3',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': icmap,
                 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None},

             'ligFF':
             {'name': 'LIG1',
                 'type': 'logical-interconnect-groupV3',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': icmap,
                 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': None}


             }
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

"""
profile1 = {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PABA58-EN1, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PABA58-EN1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WPST-PABA58-EN1_Bay1-BFS', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-102', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]}

profile2 = {'type': 'ServerProfileV5', 'serverHardwareUri': 'WPST-PABA58-EN1, bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:WPST-PABA58-EN1', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'WPST-PABA58-EN1_Bay2', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-102', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                   ]}

server_profiles = [profile1.copy(), profile2.copy()]

"""
server_profiles_201 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                        'boot': {'manageBoot': False},
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]},
                       ]

server_profiles = [{'type': 'ServerProfileV6', 'serverHardwareUri': 'CN754404RC, bay 4',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:CN754404RC', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]


server_profiles_tbird_1 = {'type': 'ServerProfileV6', 'serverHardwareUri': 'IRTQI6MH9D, bay 2',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:IRTQI6MH9D', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                           'boot': {'manageBoot': False},
                           'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},

                                           ]}


server_profiles_tbird = [{'type': 'ServerProfileV6', 'serverHardwareUri': 'IRTQI6MH9D, bay 4', 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:IRTQI6MH9D', 'enclosureGroupUri': 'EG:EGLldp',
                          'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay', 'boot': {'manageBoot': False},
                          'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 3:1-a',
                                           'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 3:2-a',
                                           'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''}]}]


server_profiles_tbird_Multi_LIG1 = [{'type': 'ServerProfileV6', 'serverHardwareUri': 'IRTQI6MH9D, bay 11', 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:IRTQI6MH9D', 'enclosureGroupUri': 'EG:EGLldp',
                                     'name': 'Sp_APIC_ENC1_BAY11', 'description': '', 'affinity': 'Bay', 'boot': {'manageBoot': False},
                                     'connections': [{'id': 1, 'name': '3', 'functionType': 'Ethernet', 'portId': 'mezz 2:1-a',
                                                      'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''},
                                                     {'id': 2, 'name': '4', 'functionType': 'Ethernet', 'portId': 'mezz 2:2-a',
                                                      'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''}]}]


server_profiles_8pf = [{'type': 'ServerProfileV6', 'serverHardwareUri': 'SGH433MX0L, bay 9',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH433MX0L', 'enclosureGroupUri': 'EG:EG_new', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'Sp_8PF', 'description': '', 'affinity': 'Bay',
                        'boot': {'manageBoot': False},
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-g', 'requestedMbps': '2500', 'networkUri': 'ETH:net_101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-h', 'requestedMbps': '2500', 'networkUri': 'ETH:net_102', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]},
                       ]

server_profiles1 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC2', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     ]},

                    ]


edit_ligs_tbird_SE_LIG = {'ligTT':
                          {'name': 'LIG',
                           'type': 'logical-interconnect-groupV300',
                           'enclosureType': 'SY12000',
                           'interconnectMapTemplate': icmap,
                           'uplinkSets': [uplink_sets_tbird['us1']],
                           'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligF':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureIndexes': [1],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_SE_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG'].copy()],
                              'redundancyType': 'Redundant',
                              'stackingMode': 'Enclosure',
                           'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet', 'lldpIpAddressMode': 'IPV4'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligT':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureIndexes': [1],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_SE_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG'].copy()],
                              'redundancyType': 'Redundant',
                              'stackingMode': 'Enclosure',
                           'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet', 'lldpIpAddressMode': 'IPV4'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligTboth':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureIndexes': [1],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_SE_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG'].copy()],
                              'redundancyType': 'Redundant',
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet', 'lldpIpAddressMode': 'BOTH_IPV4_IPV6'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligFboth':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureIndexes': [1],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_SE_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG'].copy()],
                              'redundancyType': 'Redundant',
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet', 'lldpIpAddressMode': 'BOTH_IPV4_IPV6'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligTipv6':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureIndexes': [1],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_SE_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG'].copy()],
                              'redundancyType': 'Redundant',
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': True, 'interconnectType': 'Ethernet', 'lldpIpAddressMode': 'IPV6'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},

                          'ligFipv6':
                          {'name': 'LIG',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureIndexes': [1],
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': icmap_SE_Multi_LIG,
                              'interconnectBaySet': 3,
                              'uplinkSets': [uplink_sets_tbird['us1_SE_Multi_LIG'].copy()],
                              'redundancyType': 'Redundant',
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'enableTaggedLldp': False, 'interconnectType': 'Ethernet', 'lldpIpAddressMode': 'IPV6'},
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None},
                          }

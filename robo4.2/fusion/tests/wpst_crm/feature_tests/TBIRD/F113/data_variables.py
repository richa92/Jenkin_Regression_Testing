def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


FUSION_USERNAME = 'Administrator'  # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'  # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password
# FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
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
                   'hostname': 'f113-rb.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'],
                 'locale': 'en_US.UTF-8'}

ranges = [{'name': 'CI-FIT-01-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': 'A2:11:11:00:00:00', 'endAddress': 'A2:11:11:0F:FF:FF', 'enabled': True},
          {'name': 'CI-FIT-01-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '21:11:11:11:00:00:00:00', 'endAddress': '21:11:11:11:00:0F:FF:FF', 'enabled': True},
          {'name': 'CI-FIT-01-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUBBB0000', 'endAddress': 'VCUBBB0ZZZ', 'enabled': True}]

users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'}
]

licenses = [{
    'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
    {
        'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
]

ethernet_networks = [{'name': 'RDP',
                      'type': 'ethernet-networkV4',
                      'vlanId': 1001,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'IC',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'Tunnel1',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     {'name': 'Tunnel2',
                      'type': 'ethernet-networkV4',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     ]

ethernet_ranges = [{'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 50, 'name': None, 'type': 'ethernet-networkV4',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False,
                    'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'},
                   {'prefix': 'net_', 'suffix': '', 'start': 51, 'end': 102, 'name': None, 'type': 'ethernet-networkV4',
                    'vlanId': None, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False,
                    'connectionTemplateUri': None,
                    'ethernetNetworkType': 'Tagged'}]

network_sets = [{'name': 'NS_23', 'type': 'network-setV4', 'networkUris': ['net_23'], 'nativeNetworkUri': None},
                {'name': 'NS_24', 'type': 'network-setV4', 'networkUris': ['net_24'], 'nativeNetworkUri': None},
                {'name': 'NS_46', 'type': 'network-setV4', 'networkUris': ['net_46'], 'nativeNetworkUri': None},
                {'name': 'NS_47', 'type': 'network-setV4', 'networkUris': ['net_47'], 'nativeNetworkUri': None},
                {'name': 'NS_96', 'type': 'network-setV4', 'networkUris': ['net_96'], 'nativeNetworkUri': None},
                {'name': 'NS_97', 'type': 'network-setV4', 'networkUris': ['net_97'], 'nativeNetworkUri': None},
                {'name': 'NS_98', 'type': 'network-setV4', 'networkUris': ['net_98'], 'nativeNetworkUri': None},
                {'name': 'NS_99', 'type': 'network-setV4', 'networkUris': ['net_99'], 'nativeNetworkUri': None}]

network_set_ranges = [
    {'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 22, 'name': 'VlanTrunk1', 'type': 'network-setV4',
     'networkUris': None, 'nativeNetworkUri': None},
    {'prefix': 'net_', 'suffix': '', 'start': 25, 'end': 45, 'name': 'VlanTrunk2', 'type': 'network-setV4',
     'networkUris': None, 'nativeNetworkUri': 'net_25'},
    {'prefix': 'net_', 'suffix': '', 'start': 50, 'end': 70, 'name': 'VlanTrunk3', 'type': 'network-setV4',
     'networkUris': None, 'nativeNetworkUri': 'net_50'},
    {'prefix': 'net_', 'suffix': '', 'start': 75, 'end': 95, 'name': 'VlanTrunk4', 'type': 'network-setV4',
     'networkUris': None, 'nativeNetworkUri': 'net_75'}
]

fc_networks = [{'name': 'SAN-1-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-2-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-3-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-4-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-5-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'name': 'SAN-6-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               ]

fcoe_networks = [{'name': 'fcoe-100', 'type': 'fcoe-network', 'vlanId': 100},
                 {'name': 'fcoe-101', 'type': 'fcoe-network', 'vlanId': 101},
                 ]

fcoe_ranges = [{'prefix': 'fcoe-', 'suffix': '', 'start': 1000, 'end': 1255}]

enc_groups = [{'name': 'TClass-EG',
               'enclosureCount': 1,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-Tbird'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External"}
              ]

enc_groupsA = [{'name': 'BAD-EG-Missing-stuff',
                'enclosureCount': 1,
                'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
                'ipAddressingMode': "External",
                },
               {'name': 'TClass-EG',
                'enclosureCount': 2,
                'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-Tbird'},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-Tbird'}],
                'ipAddressingMode': "Externally",
                },
               ]

encs = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24',
         'force': False, 'licensingIntent': 'OneViewNoiLO'}]

les = [{'name': 'LE',
        # 'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66103'],
        'enclosureUris': ['ENC:00HPMP4F18'],  # REAL
        'enclosureGroupUri': 'EG:TClass-EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

uplink_sets = {'RDP': {'name': 'RDP',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['RDP'],
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                  {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}]},
               'IC': {'name': 'IC',
                      'ethernetNetworkType': 'Untagged',
                      'networkType': 'Ethernet',
                      'networkUris': ['IC'],
                      'nativeNetworkUri': None,
                      'mode': 'Auto',
                      'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                 {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}]},
               'Tunnel1': {'name': 'Tunnel1',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': ['Tunnel1'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}]},
               'Tunnel2': {'name': 'Tunnel2',
                           'ethernetNetworkType': 'Tunnel',
                           'networkType': 'Ethernet',
                           'networkUris': make_range_list(
                               {'start': 1, 'end': 10, 'prefix': 'net_', 'suffix': ''}) + make_range_list(
                               {'start': 101, 'end': 110, 'prefix': 'net_', 'suffix': ''}),
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
               'Q1-Q6': {'name': 'Q1-Q6 ',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['fcoe-1001'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'lacpTimer': 'Long',
                         'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                    {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                                    {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                    {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'},
                                                    {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
                                                    {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
                                                    ]},
               'Q1.1-Q6.4': {'name': 'Q1.1-Q6.4',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['Tunnel1'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q1.2', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q1.3', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q1.4', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2.2', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2.3', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q2.4', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q3.2', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q3.3', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q3.4', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q4.2', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q4.3', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q4.4', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q5.2', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q5.3', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q5.4', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q6.2', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q6.3', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '3', 'port': 'Q6.4', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1.2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1.3', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q1.4', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.3', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.4', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.3', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.4', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q4.2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q4.3', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q4.4', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q5.2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q5.3', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q5.4', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q6.2', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q6.3', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q6.4', 'speed': 'Auto'},
                                                        ]},

               'SAN-1-A': {'name': 'SAN-1-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-1-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '1', 'port': 'X7', 'speed': 'Auto'}]},
               'SAN-2-B': {'name': 'SAN-2-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-2-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '2', 'port': 'X7', 'speed': 'Auto'}]},
               'SAN-3-A': {'name': 'SAN-3-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-3-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '3', 'port': '2', 'speed': 'Auto'}]},
               'SAN-4-B': {'name': 'SAN-4-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-4-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '4', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '4', 'port': '2', 'speed': 'Auto'}]},
               'SAN-5-A': {'name': 'SAN-5-A',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-5-A'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '5', 'port': '2', 'speed': 'Auto'}]},
               'SAN-6-B': {'name': 'SAN-6-B',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': ['SAN-6-B'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'},
                                                      {'bay': '6', 'port': '2', 'speed': 'Auto'}]},
               'BigPipe1': {'name': 'BigPipe1',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(ethernet_ranges[0]),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'BigPipe2': {'name': 'BigPipe2',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            'networkUris': make_range_list(ethernet_ranges[1]),
                            'nativeNetworkUri': None,
                            'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                       {'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},

               }

icmap = [{'bay': 3, 'enclosure': 1, 'type': 'VC SE 40Gb F8 Module', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 2, 'type': 'VC SE 40Gb F8 Module', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 1, 'type': 'HP Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'HP Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
         ]

ligs = [{'name': 'LIG-Tbird',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'SY12000',
         # 'interconnectMapTemplate': icmap,
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'VC SE 40Gb F8 Module', 'enclosureIndex': 1}],
         # new
         'enclosureIndexes': [1],
         # 'enclosureIndexes': [1, 2],
         # 'interconnectBaySet': 2,
         'interconnectBaySet': 3,
         # 'redundancyType': 'HighlyAvailable',
         'redundancyType': 'NonRedundantASide',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         # end new
         # 'uplinkSets': [],
         'uplinkSets': [uplink_sets['Q1-Q6'].copy()],
         #    uplink_sets['RDP'].copy(),
         #               uplink_sets['IC'].copy(),
         #               uplink_sets['Tunnel1'].copy()],
         #               uplink_sets['Tunnel2'].copy(),
         #               uplink_sets['SAN-1-A'].copy(),
         #               uplink_sets['SAN-2-B'].copy(),
         #               uplink_sets['SAN-3-A'].copy(),
         #               uplink_sets['SAN-4-B'].copy(),
         #               uplink_sets['SAN-5-A'].copy(),
         #               uplink_sets['SAN-6-B'].copy(),
         #               uplink_sets['BigPipe1'].copy(),
         #               uplink_sets['BigPipe2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]

fcoe_settings = {"fcoeMode": "FcfNpv"}
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

server_profiles = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'Encl1, bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:Encl1',
                    'enclosureGroupUri': 'EG:FFF8-8FC20-8FC24', 'serialNumberType': 'Virtual', 'macType': 'Virtual',
                    'wwnType': 'Virtual',
                    'name': 'Encl1_Bay1-BL465cGen8', 'description': '', 'affinity': 'Bay',
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:RDP',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'Primary'},
                                     'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_96',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_96',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-c',
                                     'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-d',
                                     'requestedMbps': '2500', 'networkUri': 'NS:NS_23',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-d',
                                     'requestedMbps': '2500', 'networkUri': 'NS:NS_23',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                     'requestedMbps': '8000', 'networkUri': 'FC:SAN-3-A',
                                     'boot': {'priority': 'NotBootable'}},
                                    {'id': 10, 'name': '10', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2',
                                     'requestedMbps': '8000', 'networkUri': 'FC:SAN-4-B',
                                     'boot': {'priority': 'NotBootable'}},
                                    {'id': 11, 'name': '11', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1',
                                     'requestedMbps': '8000', 'networkUri': 'FC:SAN-5-A',
                                     'boot': {'priority': 'Primary',
                                              'targets': [{'arrayWwpn': '21110002ac00364c', 'lun': '0'}]}, 'mac': None,
                                     'wwpn': '', 'wwnn': ''},
                                    {'id': 12, 'name': '12', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2',
                                     'requestedMbps': '8000', 'networkUri': 'FC:SAN-6-B',
                                     'boot': {'priority': 'Secondary',
                                              'targets': [{'arrayWwpn': '20110002ac00364c', 'lun': '0'}]}, 'mac': None,
                                     'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

########################################

true = True
false = False
rc = {'200': 200, '201': 201, '202': 202, '400': 400, '401': 401, '403': 403, '412': 412, '500': 500}

########################################
"""
default_variables = {'admin_credentials': admin_credentials,
                     'appliance': appliance,
                     'encs': encs,
                     'enc_groups': enc_groups,
                     'ethernet_networks': ethernet_networks,
                     'ethernet_ranges': ethernet_ranges,
                     'fc_networks': fc_networks,
                     'fcoe_networks': fcoe_networks,
                     'fcoe_ranges': fcoe_ranges,
                     'les': les,
                     'licenses': licenses,
                     'ligs': ligs,
                     'network_sets': network_sets,
                     'network_set_ranges': network_set_ranges,
                     'ranges': ranges,
                     'rc': rc,
                     'server_profiles': server_profiles,
                     'uplink_sets': uplink_sets,
                     'users': users,
                     'timeandlocale': timeandlocale,
                     'true': true, 'false': false,
                     'vcenter': vcenter}


def get_variables():

    variables = default_variables
    return variables
"""

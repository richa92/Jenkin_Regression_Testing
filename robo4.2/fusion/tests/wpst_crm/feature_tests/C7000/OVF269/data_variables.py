def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'
ENC1 = 'FVT-PAAW63-EN2'
LIG1 = 'MIXED_TAA_SS'
EG1 = 'EG'
LE1 = ENC1
US1 = 'TAA_CONVERGED'
US2 = 'BIGPIPE'

OA1_HOST = '15.245.129.56'
OA1_USER = 'Administrator'
OA1_PASS = 'wpsthpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

encs = [{'hostname': OA1_HOST, 'username': OA1_USER, 'password': OA1_PASS, 'enclosureGroupUri': 'EG:EG', 'force': False,
         'licensingIntent': 'OneViewNoiLO'}]

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'LIT',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'OVF269.hpecorp.net',
                   'confOneNode': True,
                   'domainName': 'hpecorp.net',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
     'permissions': [{'roleName': 'Server administrator'}],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
     'permissions': [{'roleName': 'Backup administrator'}],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge',
     'permissions': [{'roleName': 'Read only'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]
licenses = [{
    'key': 'YCDC D9MA H9PQ KHX2 V7B5 HWWB Y9JL KMPL TA2E PDRA DXAU 2CSM GHTG L762 HUK7 GB5M KJVT D5KM EFRW DS5R TXXK 6Q22 AK2P 3EW2 AJQ4 HU5V TZZH AB6X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542007 HPOV-NFR1 HP_OneView_16_Seat_NFR 75YYJJECU46C"_3DWNY-6B2KD-D8Z6S-6YR4B-K8GDW'},
    {
        'key': '9CTC B9MA H9PA GHWY V7B5 HWWB Y9JL KMPL 3ASE NGRE DXAU 2CSM GHTG L762 FN83 EARE KJVT D5KM EFRW DS5R 3XPK 4T22 AK2P 3EW2 AJA6 XUNV TZZX MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542185 HPOV-NFR1 HP_OneView_16_Seat_NFR JJT5JJEC9DC5"_3JNBT-28349-3DJ6L-TBRPP-PDLNR'},
    {
        'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'}
]

e1 = [{'name': n,
       'type': 'ethernet-networkV4',
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(2, 1000)]

e2 = [{'name': n,
       'type': 'ethernet-networkV4',
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(2000, 3000)]

ethernet_networks = e1 + e2

network_sets = [{'name': 'VlanTrunk1',
                 'type': 'network-setV4',
                 'networkUris': rlist(2, 163),
                 'nativeNetworkUri': None},
                ]

fcoe_networks = [{'name': n,
                  'type': 'fcoe-networkV4',
                  'vlanId': int(n[5:])} for n in rlist(1001, 1033, 'fcoe_')]

fc_networks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'fcnetwork-a',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

enc_groups = [{'name': EG1,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}
              ]

ligs = {LIG1: {'name': LIG1,
               'type': 'logical-interconnect-groupV4',
               'enclosureType': 'C7000',
               'interconnectMapTemplate': [
                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
               ],
               'uplinkSets': [{'name': US1,
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': rlist(1001, 1032, 'fcoe_') + rlist(2001, 2200),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q4.1', 'speed': 'Auto'},
                                                          {'bay': '1', 'port': 'Q4.2', 'speed': 'Auto'},
                                                          ]},
                              {'name': US2,
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': rlist(2, 801),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [
                                   {'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'},
                                   {'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'},
                                   {'bay': '1', 'port': 'Q1.3', 'speed': 'Auto'},
                                   {'bay': '1', 'port': 'Q1.4', 'speed': 'Auto'},
                                   {'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'},
                                   {'bay': '2', 'port': 'Q1.2', 'speed': 'Auto'},
                                   {'bay': '2', 'port': 'Q1.3', 'speed': 'Auto'},
                                   {'bay': '2', 'port': 'Q1.4', 'speed': 'Auto'},

                               ]},
                              ],

               'stackingMode': 'Enclosure',
               'ethernetSettings': None,
               'state': 'Active',
               'telemetryConfiguration': None,
               'snmpConfiguration': None},
        }

li_uplink_sets = {US1: {'name': US1,
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': rlist(2001, 2100),  # reduced the number of ethernet networks
                        'fcNetworkUris': [],
                        'fcoeNetworkUris': rlist(1001, 1032, 'fcoe_'),
                        'lacpTimer': 'Short',
                        'logicalInterconnectUri': None,
                        'primaryPortLocation': None,
                        'manualLoginRedistributionState': 'NotSupported',
                        'connectionMode': 'Auto',
                        'nativeNetworkUri': None,
                        'portConfigInfos': [{'enclosure': ENC1, 'bay': '1', 'port': 'Q4.1', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '1', 'port': 'Q4.2', 'desiredSpeed': 'Auto'},
                                            ]},
                  US2: {'name': US2,
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': rlist(2, 801),
                        'fcNetworkUris': [],
                        'fcoeNetworkUris': [],
                        'lacpTimer': 'Short',
                        'logicalInterconnectUri': None,
                        'primaryPortLocation': None,
                        'manualLoginRedistributionState': 'NotSupported',
                        'connectionMode': 'Auto',
                        'nativeNetworkUri': None,  # Added Q2:1 below
                        'portConfigInfos': [{'enclosure': ENC1, 'bay': '1', 'port': 'Q2.1', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '1', 'port': 'Q1.1', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '1', 'port': 'Q1.2', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '1', 'port': 'Q1.3', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '1', 'port': 'Q1.4', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '2', 'port': 'Q2.1', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '2', 'port': 'Q1.1', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '2', 'port': 'Q1.2', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '2', 'port': 'Q1.3', 'desiredSpeed': 'Auto'},
                                            {'enclosure': ENC1, 'bay': '2', 'port': 'Q1.4', 'desiredSpeed': 'Auto'}
                                            ]},
                  }

"""
0 = Windows
1 = RHEL 6.7
2 = ESXI 6
"""

server_profiles = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG1,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

def rlist(start, end, step=1, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1, step):
        rlist.append('%s%s%s' % (prefix, str(x), suffix))
    return rlist


SSH_PASS = 'hpvse1'
interface = 'bond0'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': '00:BB:58:00:00:00', 'endAddress': '00:BB:58:00:00:7F', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '21:11:BB:58:00:00:00:00', 'endAddress': '21:11:BB:58:00:00:00:7F', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'vLAN101',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'ipv4Subnet': '255.255.240.0',
                   'ipv4Gateway': '15.199.224.1',
                   'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
                   'virtIpv4Addr': '15.199.232.97',
                   'app1Ipv4Addr': '15.199.232.98',
                   'app2Ipv4Addr': '15.199.232.99',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'BB58-2ENCS.us.rdlabs.hpecorp.net',
                   'confOneNode': True,
                   'domainName': 'us.rdlabs.hpecorp.net',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hp.net'],
                 'locale': 'en_US.UTF-8'}

EG = 'EG'
EG2 = 'EG-IBS2-IBS3'
EG3 = 'EG3'
ENC1 = 'CN75016BG8'
ENC2 = 'CN750202SK'
ENC1_BAY1_IP = '192.169.0.101'
ENC1_BAY1_IP_B = '192.169.0.102'
ENC1_BAY1 = '%s, bay 1' % ENC1
ENC1_BAY3_IP = '192.169.0.103'
ENC1_BAY3 = '%s, bay 3' % ENC1
ENC2_BAY6_IP = '192.169.0.216'
ENC2_BAY6 = '%s, bay 6' % ENC2

GW_IP = '192.169.0.1'

SERVERS = [ENC1_BAY1, ENC1_BAY3, ENC2_BAY6]

LE = 'LE'

LIG1 = 'IBS3-HA'
LIG2 = 'IBS2-HA'

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
                'key': 'YCDC D9MA H9PQ KHX2 V7B5 HWWB Y9JL KMPL TA2E PDRA DXAU 2CSM GHTG L762 HUK7 GB5M KJVT D5KM EFRW DS5R TXXK 6Q22 AK2P 3EW2 AJQ4 HU5V TZZH AB6X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542007 HPOV-NFR1 HP_OneView_16_Seat_NFR 75YYJJECU46C"_3DWNY-6B2KD-D8Z6S-6YR4B-K8GDW'},
            {
                'key': '9CTC B9MA H9PA GHWY V7B5 HWWB Y9JL KMPL 3ASE NGRE DXAU 2CSM GHTG L762 FN83 EARE KJVT D5KM EFRW DS5R 3XPK 4T22 AK2P 3EW2 AJA6 XUNV TZZX MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEC 3F9V JQY5 "423542185 HPOV-NFR1 HP_OneView_16_Seat_NFR JJT5JJEC9DC5"_3JNBT-28349-3DJ6L-TBRPP-PDLNR'},
            {
                'key': '9B3C A99A H9P9 GHUZ U7B5 HWW5 Y9JL KMPL 5AWA 8CBE DXAU 2CSM GHTG L762 7NGZ GDV4 KJVT D5KM EFRW DS5R 5XP8 4XK2 GNSL 9F82 7JKT QVXB XZKH ABB4 NV2C LHXU KN7U 5NA6 BKRK 35QB D8UW R42A X3BN LQ6M 5V9A PM6Q 4MN9 9GGS EZU7 GEMX VUJW CDB5 JVRX 8HEN 2J98 ACPB "TKOPREN HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR ATJUJJEDAT2Y"'}
            ]

ethernet_ranges = [
    {'prefix': 'net_', 'suffix': '', 'start': 2, 'end': 1000, 'name': None, 'type': 'ethernet-networkV300',
     'vlanId': None, 'purpose': 'General', 'smartLink': False, 'privateNetwork': False, 'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    ]

network_sets = [
    {'name': 'VlanTrunk', 'type': 'network-setV300', 'networkUris': rlist(2, 163, suffix=''), 'nativeNetworkUri': None},
    {'name': 'VlanTrunk3', 'type': 'network-setV300', 'networkUris': rlist(300, 461, suffix=''),
     'nativeNetworkUri': None}
    ]

fcoe_ranges = [{'prefix': 'fcoe_', 'suffix': '', 'start': 1001, 'end': 1256}
               ]

enc_groups = [{'name': EG,
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               },
              {'name': EG2,
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG1},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               },
              ]

les = [{'name': LE,
        'enclosureUris': ['ENC:%s' % ENC1, 'ENC:%s' % ENC2],
        'enclosureGroupUri': 'EG:%s' % EG,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       ]

uplink_sets = {'FCoE-A': {'name': 'FCoE-A',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': rlist(1000, 1064, 2, 'fcoe_'),
                          'primaryPort': None,
                          'nativeNetworkUri': None,
                          'mode': 'Auto',
                          'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                                     ]},
               'FCoE-B': {'name': 'FCoE-B',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': rlist(1001, 1063, 2, 'fcoe_'),
                          'primaryPort': None,
                          'nativeNetworkUri': None,
                          'mode': 'Auto',
                          'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                                     ]},
               'Bigpipe': {'name': 'Bigpipe',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': rlist(2, 998),
                           'primaryPort': None,
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
                                                      {'enclosure': '1', 'bay': '3', 'port': 'Q5.2', 'speed': 'Auto'},
                                                      {'enclosure': '1', 'bay': '3', 'port': 'Q5.3', 'speed': 'Auto'},
                                                      {'enclosure': '1', 'bay': '3', 'port': 'Q5.4', 'speed': 'Auto'},
                                                      {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
                                                      {'enclosure': '2', 'bay': '6', 'port': 'Q5.2', 'speed': 'Auto'},
                                                      {'enclosure': '2', 'bay': '6', 'port': 'Q5.3', 'speed': 'Auto'},
                                                      {'enclosure': '2', 'bay': '6', 'port': 'Q5.4', 'speed': 'Auto'},
                                                      ]},
               }

ligs = [{'name': 'IBS2-HA',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [
             {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
             {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
             {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
             {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
             ],
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': 'IBS3-HA',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [
             {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
             {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
             {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
             {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
             ],
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'uplinkSets': [uplink_sets['FCoE-A'], uplink_sets['FCoE-B'], uplink_sets['Bigpipe']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]

"""
Maps sever profile to encl, bay.  First column: server profile name. Second column: Enclosure, bay #
"""
server_profile_to_bay_map = {'%sbay1' % ENC1: '%s, bay 1' % ENC1,
                             '%sbay2' % ENC1: '%s, bay 2' % ENC1,
                             '%sbay3' % ENC1: '%s, bay 3' % ENC1,
                             '%sbay1' % ENC2: '%s, bay 1' % ENC2,
                             '%sbay2' % ENC2: '%s, bay 2' % ENC2,
                             '%sbay6' % ENC2: '%s, bay 6' % ENC2
                             }


def make_server_profile_dict(name, mezz=3, serverHardwareUri=None, serverHardwareTypeUri=None, enclosureUri=None,
                             enclosureGroupUri=None):
    connections = [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-a' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-a' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:1-b' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:2-b' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1003',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-c' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:net_103',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-c' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:net_103',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-d' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-d' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk3',
                    'boot': {'priority': 'NotBootable'}},
                   ]

    return {'type': 'ServerProfileV6',
            'serverHardwareUri': serverHardwareUri,
            'serverHardwareTypeUri': serverHardwareTypeUri,
            'enclosureUri': enclosureUri,
            'enclosureGroupUri': enclosureGroupUri,
            'serialNumberType': 'Virtual',
            'macType': 'Virtual',
            'wwnType': 'Virtual',
            'name': name,
            'description': '',
            'affinity': 'Bay',
            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
            'boot': {'manageBoot': True, 'order': ['HardDisk']},
            'connections': connections}


def build_profiles(profiles):
    return [make_server_profile_dict(*p) for p in profiles]


def enc_profiles(enc, eg='EG', count=13):
    return [['%s profile%s' % (enc, N), '%s, bay %s' % (enc, N), '', 'ENC:%s' % enc, 'EG:%s' % eg] for N in
            xrange(1, count)]


profiles = [['%sbay1' % ENC1, 3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
            ['%sbay2' % ENC1, 3, None, 'SY 480 Gen9 2', None, 'EG:%s' % EG],
            ['%sbay3' % ENC1, 6, None, 'SY 620 Gen9 1', None, 'EG:%s' % EG],
            ['%sbay1' % ENC2, 3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
            ['%sbay2' % ENC2, 3, None, 'SY 480 Gen9 3', None, 'EG:%s' % EG],
            ['%sbay6' % ENC2, 3, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG]
            ]

server_profiles_nohw = build_profiles(profiles)
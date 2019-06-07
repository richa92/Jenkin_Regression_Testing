from copy import deepcopy


def rlist(start, end, prefix='net_', suffix='', step=1):
    l = []
    for x in xrange(start, end + 1, step):
        l.append('%s%s%s' % (prefix, str(x), suffix))
    return l


SSH_PASS = 'hpvse1'
interface = 'bond0'

TOR = {'aside_bagg': {'name': 'Bridge-Aggregation350', 'ports': ['25', '27', '29', '31']},
       'bside_bagg': {'name': 'Bridge-Aggregation650', 'ports': ['17', '19', '21', '23']},
       'ipv4': '15.245.128.95',
       'user': 'Administrator',
       'pass': 'wpsthpvse1',
       'cfg_file': 'ovf266_smartlink.cfg'
       }

EG1 = 'EG-HA'
EG2 = 'EG-AB'

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

PING_LIST_1 = [ENC1_BAY1_IP, ENC1_BAY3_IP, ENC2_BAY6_IP]
PING_LIST_2 = [ENC1_BAY1_IP_B, ENC2_BAY6_IP]
PING_LIST_3 = [ENC1_BAY1_IP, GW_IP]

SERVERS = [ENC1_BAY1, ENC1_BAY3, ENC2_BAY6]

LE1 = 'LE-AB'

LIG1 = 'LIG-HA'
LIG2 = 'LIG-ASIDE'
LIG3 = 'LIG-BSIDE'

ENCS = [ENC1, ENC2]

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': '00:BB:58:00:00:00', 'endAddress': '00:BB:58:00:00:7F', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '21:11:BB:58:00:00:00:00', 'endAddress': '21:11:BB:58:00:00:00:7F', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'LIT',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'ipv4Subnet': '255.255.248.0',
                   'ipv4Gateway': '15.245.128.1',
                   'ipv4NameServers': ['16.110.135.51', '16.110.135.52'],
                   'virtIpv4Addr': '15.245.131.206',
                   'app1Ipv4Addr': '15.245.131.207',
                   'app2Ipv4Addr': '15.245.131.208',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'ovf266.api.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hp.net'],
                 'locale': 'en_US.UTF-8'}

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

nets = {'net_2001': {'name': 'net_2001',
                     'type': 'ethernet-networkV300',
                     'purpose': 'General',
                     'smartLink': True,
                     'privateNetwork': False,
                     'connectionTemplateUri': None,
                     'ethernetNetworkType': 'Tagged',
                     'vlanId': 2001},
        'untagged': {'name': 'net_untagged',
                     'type': 'ethernet-networkV300',
                     'purpose': 'General',
                     'smartLink': True,
                     'privateNetwork': False,
                     'connectionTemplateUri': None,
                     'ethernetNetworkType': 'Untagged'},
        'tunnel': {'name': 'net_tunnel',
                   'type': 'ethernet-networkV300',
                   'purpose': 'General',
                   'smartLink': True,
                   'privateNetwork': False,
                   'connectionTemplateUri': None,
                   'ethernetNetworkType': 'Tunnel'},
        'net_2000_enable': {'name': 'net_2000',
                            'type': 'ethernet-networkV300',
                            'purpose': 'General',
                            'smartLink': True,
                            'privateNetwork': False,
                            'connectionTemplateUri': None,
                            'ethernetNetworkType': 'Tagged',
                            'vlanId': 2000},
        'net_2000_disable': {'name': 'net_2000',
                             'type': 'ethernet-networkV300',
                             'purpose': 'General',
                             'smartLink': False,
                             'privateNetwork': False,
                             'connectionTemplateUri': None,
                             'ethernetNetworkType': 'Tagged',
                             'vlanId': 2000},
        'fcoe': {'name': 'error-no-fcoe-smartlink',
                 'type': 'fcoe-networkV4',
                 'smartLink': True,
                 'vlanId': 4000},
        'fc': {'name': 'error-no-fc-smartlink',
               'type': 'fc-networkV300',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'smartLink': True,
               'fabricType': 'FabricAttach'}
        }

e1 = [{'name': 'tunnelnetwork1',
       'type': 'ethernet-networkV300',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'tunnelnetwork2',
       'type': 'ethernet-networkV300',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'untaggednetwork1',
       'type': 'ethernet-networkV300',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'},
      {'name': 'untaggednetwork2',
       'type': 'ethernet-networkV300',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'},
      {'name': 'net_a',
       'type': 'ethernet-networkV300',
       'vlanId': 2100,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged'},
      {'name': 'net_b',
       'type': 'ethernet-networkV300',
       'vlanId': 2101,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged'},
      {'name': 'net_c',
       'type': 'ethernet-networkV300',
       'vlanId': 2102,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged'},
      {'name': 'net_d',
       'type': 'ethernet-networkV300',
       'vlanId': 2103,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged'}
      ]

e2 = [{'name': n,
       'type': 'ethernet-networkV300',
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(1, 1000)]

ethernet_networks = e1 + e2

network_sets = [{'name': 'NetSet1', 'type': 'network-setV300', 'networkUris': rlist(100, 161),
                 'nativeNetworkUri': None},
                {'name': 'NetSet2', 'type': 'network-setV300', 'networkUris': rlist(200, 261),
                 'nativeNetworkUri': None},
                {'name': 'NetSet3', 'type': 'network-setV300', 'networkUris': rlist(300, 361),
                 'nativeNetworkUri': None},
                {'name': 'NetSet4', 'type': 'network-setV300', 'networkUris': rlist(400, 461),
                 'nativeNetworkUri': None},
                {'name': 'NetSet5', 'type': 'network-setV300', 'networkUris': rlist(500, 561),
                 'nativeNetworkUri': None},
                {'name': 'NetSet6', 'type': 'network-setV300', 'networkUris': rlist(600, 661),
                 'nativeNetworkUri': None},
                {'name': 'NetSet7', 'type': 'network-setV300', 'networkUris': rlist(700, 761),
                 'nativeNetworkUri': None},
                {'name': 'NetSet8', 'type': 'network-setV300', 'networkUris': rlist(800, 861),
                 'nativeNetworkUri': None},
                {'name': 'NetSet-AD', 'type': 'network-setV300', 'networkUris': ['net_a', 'net_d'],
                 'nativeNetworkUri': None},
                {'name': 'NetSet-ABC', 'type': 'network-setV300', 'networkUris': ['net_a', 'net_b', 'net_c'],
                 'nativeNetworkUri': None}

                ]

fcoe_networks = [{'name': n,
                  'type': 'fcoe-networkV4',
                  'vlanId': int(n[5:])} for n in rlist(1001, 1256, 'fcoe_')]

fc_networks = [{'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': '%s' % n,
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'} for n in rlist(1, 6, 'fc_fa_')]

ha_uplink_sets = {'FCoE-A': {'name': 'FCoE-A',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': rlist(1000, 1064, 'fcoe_', step=2),
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                                        ]},
                  'FCoE-B': {'name': 'FCoE-B',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': rlist(1001, 1063, 'fcoe_', step=2),
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                                        ]},
                  'Bigpipe': {'name': 'BigpipeAB',
                              'ethernetNetworkType': 'Tagged',
                              'networkType': 'Ethernet',
                              'networkUris': rlist(1, 1000),
                              'primaryPort': None,
                              'nativeNetworkUri': None,
                              'mode': 'Auto',
                              'logicalPortConfigInfos': [
                                  {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
                                  {'enclosure': '1', 'bay': '3', 'port': 'Q5.2', 'speed': 'Auto'},
                                  {'enclosure': '1', 'bay': '3', 'port': 'Q5.3', 'speed': 'Auto'},
                                  {'enclosure': '1', 'bay': '3', 'port': 'Q5.4', 'speed': 'Auto'},
                                  {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
                                  {'enclosure': '2', 'bay': '6', 'port': 'Q5.2', 'speed': 'Auto'},
                                  {'enclosure': '2', 'bay': '6', 'port': 'Q5.3', 'speed': 'Auto'},
                                  {'enclosure': '2', 'bay': '6', 'port': 'Q5.4', 'speed': 'Auto'},
                              ]},
                  }

aside_uplink_sets = {
    'FCoE-A': {'name': 'FCoE-A',
               'ethernetNetworkType': 'Tagged',
               'networkType': 'Ethernet',
               'networkUris': ['fcoe_1002'],
               'primaryPort': None,
               'nativeNetworkUri': None,
               'mode': 'Auto',
               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                          ]},
    'Bigpipe-A': {'name': 'Bigpipe-A',
                  'ethernetNetworkType': 'Tagged',
                  'networkType': 'Ethernet',
                  'networkUris': rlist(1, 1000),
                  'primaryPort': None,
                  'nativeNetworkUri': None,
                  'mode': 'Auto',
                  'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
                                             {'enclosure': '1', 'bay': '3', 'port': 'Q5.2', 'speed': 'Auto'},
                                             {'enclosure': '1', 'bay': '3', 'port': 'Q5.3', 'speed': 'Auto'},
                                             {'enclosure': '1', 'bay': '3', 'port': 'Q5.4', 'speed': 'Auto'}
                                             ]}
}

bside_uplink_sets = {
    'FCoE-B': {'name': 'FCoE-B',
               'ethernetNetworkType': 'Tagged',
               'networkType': 'Ethernet',
               'networkUris': ['fcoe_1003'],
               'primaryPort': None,
               'nativeNetworkUri': None,
               'mode': 'Auto',
               'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                          ]},
    'Bigpipe-B': {'name': 'Bigpipe-B',
                  'ethernetNetworkType': 'Tagged',
                  'networkType': 'Ethernet',
                  'networkUris': rlist(1, 1000),
                  'primaryPort': None,
                  'nativeNetworkUri': None,
                  'mode': 'Auto',
                  'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
                                             {'enclosure': '2', 'bay': '6', 'port': 'Q5.2', 'speed': 'Auto'},
                                             {'enclosure': '2', 'bay': '6', 'port': 'Q5.3', 'speed': 'Auto'},
                                             {'enclosure': '2', 'bay': '6', 'port': 'Q5.4', 'speed': 'Auto'}
                                             ]}
}

aside_uplink_sets2 = {
    'US1': {'name': 'US1',
            'ethernetNetworkType': 'Tagged',
            'networkType': 'Ethernet',
            'networkUris': rlist(2100, 2101),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
                                       {'enclosure': '1', 'bay': '3', 'port': 'Q5.2', 'speed': 'Auto'}
                                       ]},
    'US2': {'name': 'US2',
            'ethernetNetworkType': 'Tagged',
            'networkType': 'Ethernet',
            'networkUris': rlist(2102, 2103),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5.3', 'speed': 'Auto'},
                                       {'enclosure': '1', 'bay': '3', 'port': 'Q5.4', 'speed': 'Auto'}
                                       ]}

}

bside_uplink_sets2 = {
    'US1': {'name': 'US1',
            'ethernetNetworkType': 'Tagged',
            'networkType': 'Ethernet',
            'networkUris': rlist(2100, 2101),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
                                       {'enclosure': '2', 'bay': '6', 'port': 'Q5.2', 'speed': 'Auto'}
                                       ]},
    'US2': {'name': 'US2',
            'ethernetNetworkType': 'Tagged',
            'networkType': 'Ethernet',
            'networkUris': rlist(2102, 2103),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q5.3', 'speed': 'Auto'},
                                       {'enclosure': '2', 'bay': '6', 'port': 'Q5.4', 'speed': 'Auto'}
                                       ]}

}

ligs = {
    LIG1: {'name': LIG1,
           'type': 'logical-interconnect-groupV400',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'enclosureIndex': 1},
               {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
               {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
               {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'enclosureIndex': 2},
           ],
           'enclosureIndexes': [1, 2],
           'interconnectBaySet': 3,
           'redundancyType': 'HighlyAvailable',
           'uplinkSets': [deepcopy(v) for v in ha_uplink_sets.itervalues()]
           },
    LIG2: {'name': LIG2,
           'type': 'logical-interconnect-groupV400',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
               {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}],
           'enclosureIndexes': [1, 2],
           'interconnectBaySet': 3,
           'redundancyType': 'NonRedundantASide',
           'uplinkSets': [deepcopy(v) for v in aside_uplink_sets.itervalues()]
           },
    LIG3: {'name': LIG3,
           'type': 'logical-interconnect-groupV400',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
               {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1}],
           'enclosureIndexes': [1, 2],
           'interconnectBaySet': 3,
           'redundancyType': 'NonRedundantBSide',
           'uplinkSets': [deepcopy(v) for v in bside_uplink_sets.itervalues()]
           }
}

enc_groups = {EG1: {'name': EG1,
                    'type': 'EnclosureGroupV400',
                    'enclosureCount': 2,
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'interconnectBayMappingCount': 6,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    },
              EG2: {'name': EG2,
                    'type': 'EnclosureGroupV400',
                    'enclosureCount': 2,
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'interconnectBayMappingCount': 6,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG3},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    },
              }

les = {LE1: {'name': LE1,
             'enclosureUris': ['ENC:%s' % ENC1, 'ENC:%s' % ENC2],
             'enclosureGroupUri': 'EG:%s' % EG2,
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }
       }

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
                    'requestedMbps': '2500', 'networkUri': 'NS:NetSet3',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-d' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'NS:NetSet3',
                    'boot': {'priority': 'NotBootable'}},
                   ]

    return {'type': 'ServerProfileV7',
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


profiles = [['%sbay1' % ENC1, 3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG2],
            ['%sbay2' % ENC1, 3, None, 'SY 480 Gen9 2', None, 'EG:%s' % EG2],
            ['%sbay3' % ENC1, 6, None, 'SY 620 Gen9 1', None, 'EG:%s' % EG2],
            ['%sbay1' % ENC2, 3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG2],
            ['%sbay2' % ENC2, 3, None, 'SY 480 Gen9 3', None, 'EG:%s' % EG2],
            ['%sbay6' % ENC2, 3, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG2]
            ]

server_profiles_nohw = build_profiles(profiles)

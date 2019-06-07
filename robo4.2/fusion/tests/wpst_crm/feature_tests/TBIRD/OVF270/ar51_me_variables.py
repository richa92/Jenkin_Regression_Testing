def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'
interface = 'bond0'
FUSION_USERNAME = 'Administrator'  # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'  # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password
FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

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
                   'virtIpv4Addr': '15.245.131.12',
                   'app1Ipv4Addr': '15.245.131.13',
                   'app2Ipv4Addr': '15.245.131.14',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'ovf270.hpecorp.net',
                   'confOneNode': True,
                   'domainName': 'hpecorp.net',
                   'aliasDisabled': True,
                   }],
             }

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hp.net'],
                 'locale': 'en_US.UTF-8'}

EG1 = 'EG'

ENC1 = 'CN754406W7'
ENC2 = 'CN7544044C'
ENC3 = 'CN754406WT'

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

LE1 = 'LE'

LIG1 = 'IBS2_HA_MIXED_TAA_POTASH_CL20'
LIG2 = 'IBS3_HA_MIXED_TAA_POTASH_CL10'

US1 = 'TAA_CONVERGED'
US2 = 'BIGPIPE'

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
               'enclosureCount': 3,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG2}],
               'ipAddressingMode': "External",
               },
              ]

les = {LE1: {'name': LE1,
             'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
             'enclosureGroupUri': 'EG:EG',
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }
       }

ligs = {LIG1: {'name': LIG1,
               'type': 'logical-interconnect-groupV4',
               'enclosureType': 'SY12000',
               'interconnectMapTemplate': [
                   {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                    'enclosureIndex': 1},
                   {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                    'enclosureIndex': 2},
                   {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                   {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                   {'bay': 2, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                   {'bay': 5, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
               ],
               'enclosureIndexes': [1, 2, 3],
               'interconnectBaySet': 2,
               'redundancyType': 'HighlyAvailable',
               'fcoeSettings': {'fcoeMode': 'FcfNpv'},
               'uplinkSets': [{'name': "%s%s" % (LIG1, US1),
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': rlist(1001, 1032, 'fcoe_') + rlist(2001, 3000),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
                                                          ]},
                              {'name': "%s%s" % (LIG1, US2),
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': rlist(2, 998),
                               'primaryPort': None,
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'logicalPortConfigInfos': [
                                   {'enclosure': '1', 'bay': '2', 'port': 'Q5.1', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '2', 'port': 'Q5.2', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '2', 'port': 'Q5.3', 'speed': 'Auto'},
                                   {'enclosure': '1', 'bay': '2', 'port': 'Q5.4', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '5', 'port': 'Q5.1', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '5', 'port': 'Q5.2', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '5', 'port': 'Q5.3', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '5', 'port': 'Q5.4', 'speed': 'Auto'},
                              ]},
                              ]
               },
        LIG2:
            {'name': LIG2,
             'type': 'logical-interconnect-groupV4',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': [
                 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                  'enclosureIndex': 1},
                 {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                  'enclosureIndex': 2},
                 {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module',
                  'enclosureIndex': 1},
                 {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module',
                  'enclosureIndex': 2},
                 {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module',
                  'enclosureIndex': 3},
                 {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module',
                  'enclosureIndex': 3},
             ],
             'enclosureIndexes': [1, 2, 3],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'fcoeSettings': {'fcoeMode': 'FcfNpv'},
             'uplinkSets': [{'name': "%s%s" % (LIG2, US1),
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': rlist(1001, 1032, 'fcoe_') + rlist(2001, 3000),
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [
                                 {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
             ]},
                 {'name': "%s%s" % (LIG2, US2),
                  'ethernetNetworkType': 'Tagged',
                  'networkType': 'Ethernet',
                  'networkUris': rlist(2, 998),
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

             ],

             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None}
        }

li_uplink_sets = {"%s%s" % (LIG2, US1): {'name': "%s%s" % (LIG2, US1),
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
                                         'portConfigInfos': [
                                             {'enclosure': ENC1, 'bay': '3', 'port': 'Q6', 'desiredSpeed': 'Auto'},
]},
    "%s%s" % (LIG2, US2): {'name': "%s%s" % (LIG2, US2),
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': rlist(2, 998),
                           'fcNetworkUris': [],
                           'fcoeNetworkUris': [],
                           'lacpTimer': 'Short',
                           'logicalInterconnectUri': None,
                           'primaryPortLocation': None,
                           'manualLoginRedistributionState': 'NotSupported',
                           'connectionMode': 'Auto',
                           'nativeNetworkUri': None,  # Added Q1:1 below
                           'portConfigInfos': [
                                             {'enclosure': ENC1, 'bay': '3', 'port': 'Q1:1', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC1, 'bay': '3', 'port': 'Q5:1', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC1, 'bay': '3', 'port': 'Q5:2', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC1, 'bay': '3', 'port': 'Q5:3', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC1, 'bay': '3', 'port': 'Q5:4', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC2, 'bay': '6', 'port': 'Q1:1', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC2, 'bay': '6', 'port': 'Q5:1', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC2, 'bay': '6', 'port': 'Q5:2', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC2, 'bay': '6', 'port': 'Q5:3', 'desiredSpeed': 'Auto'},
                                             {'enclosure': ENC2, 'bay': '6', 'port': 'Q5:4', 'desiredSpeed': 'Auto'}
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
                    'name': ENC1 + '_Bay1-BFS', 'description': 'Blackbird! rhel6.7 - Aside', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    # 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                    #         'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '1'}]}, 'mac': None,
                                    # 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 4',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG1,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay4', 'description': 'Firebird! - esxi 6 - Aside', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},

                                    # 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                    #         'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None,
                                    # 'wwpn': '', 'wwnn': ''},
                                    ]},
                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 8',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG1,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC2 + '_Bay8', 'description': 'Redbird! esxi 6 - Aside', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},

                                    # 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                    #          'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None,
                                    # 'wwpn': '', 'wwnn': ''},
                                    ]},

                   ]

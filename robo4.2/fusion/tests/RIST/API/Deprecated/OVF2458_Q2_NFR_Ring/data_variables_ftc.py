from copy import deepcopy
import json


def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_USER = 'root'
SSH_PASS = 'Wpst@hpvse123#!'
interface = 'bond0'


EG1 = '3enc'
LE1 = 'LE1'

LIG1 = 'IBS1'
LIG2 = 'IBS2'
LIG3 = 'IBS3'

ENC1 = 'CN754404R9'
ENC2 = 'CN754406WS'
ENC3 = 'MXQ7100868'

ENCS = [ENC1, ENC2, ENC3]

admin_credentials = {'userName': 'Administrator', 'password': 'Wpst@hpvse123#!'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': '',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.240.0',
               'ipv4Gateway': '16.114.208.1',
               'ipv4NameServers': ['16.125.25.81', '16.125.25.82'],
               'virtIpv4Addr': '16.114.208.62',
               'app1Ipv4Addr': '16.114.208.60',
               'app2Ipv4Addr': '16.114.208.61',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': 'daisy.vse.rdlabs.hpecorp.net',
               'confOneNode': True,
               'domainName': 'vse.rdlabs.hpecorp.net',
               'aliasDisabled': True,
               }],
             }

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hp.net'],
                 'locale': 'en_US.UTF-8'}


racks = [{"name": "R4", "serialNumber": "", "uHeight": "48", "rackMounts": [
    {"location": "CenterFront", "mountUri": "ENC:%s" % ENC3, "relativeOrder": 0, "topUSlot": 18,
     "uHeight": 10},
    {"location": "CenterFront", "mountUri": "ENC:%s" % ENC2, "relativeOrder": 0, "topUSlot": 28,
     "uHeight": 10},
    {"location": "CenterFront", "mountUri": "ENC:%s" % ENC1, "relativeOrder": 0, "topUSlot": 38,
     "uHeight": 10}], "thermalLimit": "", "height": 2223, "width": 600, "depth": 1000}]

###
# Virtual Addressing
# MAC-3 mezz * 8 subports * 12 blades * 5 frames = 1440
# WWN-3 mezz * 8 subports * 12 blades * 5 frames = 1440
###

ranges = [{'name': 'N19-40-R4-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': '00:AA:04:00:00:00', 'endAddress': '00:AA:04:00:05:9F', 'enabled': True},
          {'name': 'N19-40-R4-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '21:11:AA:04:00:00:00:00', 'endAddress': '21:11:AA:04:00:00:05:9F', 'enabled': True},
          {'name': 'N19-40-R4-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUR400000', 'endAddress': 'VCUR40003J', 'enabled': True}]

users = [
    {'userName': 'lori', 'password': 'hpvse123', 'fullName': 'Lori Winter', 'roles': ['Infrastructure administrator'],
     'emailAddress': 'lori.winter@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'russell', 'password': 'hpvse123', 'fullName': 'Russell Briggs', 'roles': ['Infrastructure administrator'],
     'emailAddress': 'rbriggs@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'ron', 'password': 'hpvse123', 'fullName': 'Ron Soto',
     'roles': ['Infrastructure administrator'],
     'emailAddress': 'ron.soto@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'guthrey', 'password': 'hpvse123', 'fullName': 'Guthrey Coy',
     'roles': ['Infrastructure administrator'],
     'emailAddress': 'guthrey.coy@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'fvtftc', 'password': 'fvtftchpvse123', 'fullName': 'Ron Soto and Team',
     'roles': ['Infrastructure administrator'],
     'emailAddress': 'ron.soto@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
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
     'type': 'UserAndRoles'},
    {'userName': 'ES', 'password': 'EShpvse123', 'fullName': 'Engineering Services',
     'roles': ['Infrastructure administrator'],
     'emailAddress': 'esrequests@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
]

e1 = [{'name': 'tunnelnetwork1',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'tunnelnetwork2',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'untaggednetwork1',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'},
      {'name': 'untaggednetwork2',
       'type': 'ethernet-networkV4',
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'}
      ]

e2 = [{'name': n,
       'type': 'ethernet-networkV4',
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(1, 2000)]

ethernet_networks = e1 + e2

network_sets = [{'name': 'NetSet1', 'type': 'network-setV4', 'networkUris': rlist(100, 161),
                 'nativeNetworkUri': None},
                {'name': 'NetSet2', 'type': 'network-setV4', 'networkUris': rlist(200, 261),
                 'nativeNetworkUri': None},
                {'name': 'NetSet3', 'type': 'network-setV4', 'networkUris': rlist(300, 361),
                 'nativeNetworkUri': None},
                {'name': 'NetSet4', 'type': 'network-setV4', 'networkUris': rlist(400, 461),
                 'nativeNetworkUri': None},
                {'name': 'NetSet5', 'type': 'network-setV4', 'networkUris': rlist(500, 561),
                 'nativeNetworkUri': None},
                {'name': 'NetSet6', 'type': 'network-setV4', 'networkUris': rlist(600, 661),
                 'nativeNetworkUri': None},
                {'name': 'NetSet7', 'type': 'network-setV4', 'networkUris': rlist(700, 761),
                 'nativeNetworkUri': None},
                {'name': 'NetSet8', 'type': 'network-setV4', 'networkUris': rlist(800, 861),
                 'nativeNetworkUri': None},
                ]

fcoe_networks = [{'name': n,
                  'type': 'fcoe-networkV4',
                  'vlanId': int(n[5:])} for n in rlist(3001, 3256, 'fcoe_')]

fc1 = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'fc_fa_1',
                'connectionTemplateUri': None,
                'managedSanUri': 'FCSan:Daisy_Q2_NFR_VF_100-10:00:c4:f5:7c:46:b5:25',
                'fabricType': 'FabricAttach'}]

fc2 = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'fc_fa_2',
                'connectionTemplateUri': None,
                'managedSanUri': 'FCSan:Daisy_Q2_NFR_VF_128-10:00:c4:f5:7c:46:b5:24',
                'fabricType': 'FabricAttach'}]

fc3_6 = [{'type': 'fc-networkV4',
          'linkStabilityTime': 30,
          'autoLoginRedistribution': True,
          'name': '%s' % n,
          'connectionTemplateUri': None,
          'managedSanUri': None,
          'fabricType': 'FabricAttach'} for n in rlist(3, 6, 'fc_fa_')]

fc_networks = fc1 + fc2 + fc3_6

potash_us = {

    'bay3-fcoe3002': {
        'name': 'bay3-fcoe3002',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe_3002'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.4', 'speed': 'Auto'}
        ]
    },
    'bay6-fcoe3004': {
        'name': 'bay6-fcoe3004',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe_3004'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.4', 'speed': 'Auto'}
        ]
    },
    'bay3-tunnel4xC-us': {
        'name': 'bay3-tunnel4xC-us',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['tunnelnetwork1'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.3', 'speed': 'Auto'}
        ]
    },
    'bay3-untagged4xC-us': {
        'name': 'bay3-untagged4xC-us',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['untaggednetwork1'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}
        ]
    },
    'bay3-enet4x10-us': {
        'name': 'bay3-enet4x10-us',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(900, 999),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.2', 'speed': 'Auto'}
        ]
    },
    'MLAG222-ENET-4x10': {
        'name': 'MLAG222-ENET-4x10',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(100, 461),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.4', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.4', 'speed': 'Auto'},
        ]
    },
    'MLAG666-ENET-40': {
        'name': 'MLAG666-ENET-40',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(500, 861),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
        ]
    },
}

carbon_US = [{'name': '%s-FC-2' % LIG2,
              'ethernetNetworkType': 'NotApplicable',
              'networkType': 'FibreChannel',
              'networkUris': ['fc_fa_1'],
              'nativeNetworkUri': None,
              'mode': 'Auto',
              'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '2', 'port': '1', 'speed': 'Auto'},
                                         {'enclosure': '-1', 'bay': '2', 'port': '3', 'speed': 'Auto'},
                                         {'enclosure': '-1', 'bay': '2', 'port': '4',
                                          'speed': 'Auto'}]},
             {'name': '%s-FC-5' % LIG2,
              'ethernetNetworkType': 'NotApplicable',
              'networkType': 'FibreChannel',
              'networkUris': ['fc_fa_2'],
              'nativeNetworkUri': None,
              'mode': 'Auto',
              'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '5', 'port': '1', 'speed': 'Auto'},
                                         {'enclosure': '-1', 'bay': '5', 'port': '3', 'speed': 'Auto'},
                                         {'enclosure': '-1', 'bay': '5', 'port': '4',
                                          'speed': 'Auto'}]},
             ]

###
# LIGs
###

sas_ligs = {LIG1: {'name': LIG1,
                   'type': 'sas-logical-interconnect-groupV2',
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                   ],
                   'enclosureIndexes': [1],
                   'interconnectBaySet': 1,
                   },
            }

ligs = {
    LIG2: {'name': LIG2,
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 2, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy',
                'enclosureIndex': -1},
               {'bay': 5, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy',
                'enclosureIndex': -1},
           ],
           'enclosureIndexes': [-1],
           'interconnectBaySet': 2,
           'redundancyType': 'Redundant',
           'uplinkSets': deepcopy(carbon_US),
           },
    LIG3: {'name': LIG3,
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [
               {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'enclosureIndex': 1},
               {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
               {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
               {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'enclosureIndex': 2},
               {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
               {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
           ],
           'enclosureIndexes': [1, 2, 3],
           'interconnectBaySet': 3,
           'redundancyType': 'HighlyAvailable',
           'uplinkSets': [deepcopy(v) for v in potash_us.itervalues()]
           }
}

enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 3,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    }
              }

les = {LE1: {'name': LE1,
             'enclosureUris': ['ENC:%s' % ENC1, 'ENC:%s' % ENC2, 'ENC:%s' % ENC3],
             'enclosureGroupUri': 'EG:%s' % EG1,
             'firmwareBaselineUri': None,
             'forceInstallFirmware': False
             }
       }

"""
Server Profile Templates
"""
sht_480_1 = 'SY 480 Gen9 1'
sht_660_1 = 'SY 660 Gen9 1'

conns = [{'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1',
          'requestedMbps': 'Auto',
          'networkUri': 'FC:fc_fa_1', 'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 2, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:2',
          'requestedMbps': 'Auto',
          'networkUri': 'FC:fc_fa_2', 'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
          'networkUri': 'NS:NetSet1', 'requestedVFs': '0',
          'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
          'networkUri': 'NS:NetSet1', 'requestedVFs': '0',
          'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 5, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
          'requestedMbps': '2500',
          'networkUri': 'FCOE:fcoe_3002', 'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 6, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
          'requestedMbps': '2500',
          'networkUri': 'FCOE:fcoe_3004', 'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 7, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
          'networkUri': 'NS:NetSet2', 'requestedVFs': '0',
          'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 8, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
          'networkUri': 'NS:NetSet2', 'requestedVFs': '0',
          'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 9, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
          'networkUri': 'NS:NetSet3', 'requestedVFs': '0',
          'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}},
         {'id': 10, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
          'requestedMbps': '2500',
          'networkUri': 'NS:NetSet3', 'requestedVFs': '0',
          'ipv4': {},
          'boot': {'priority': 'NotBootable', 'iscsi': {}}}
         ]

spts = {'480_1': {'type': 'ServerProfileTemplateV4', 'serverProfileDescription': 'Profile created from 480_1 SPT',
                  'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
                  'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                  'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '480_1', 'description': 'Profile created from 480_1 SPT', 'affinity': 'Bay',
                  'connectionSettings': {'connections': deepcopy(conns), 'manageConnections': True},
                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                  'boot': {'manageBoot': True, 'order': ['HardDisk']},
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                               'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
                  'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True,
                  'iscsiInitiatorNameType': 'AutoGenerated',
                  'localStorage': {'controllers': [{'deviceSlot': 'Mezz 1', 'initialize': False, 'mode': 'RAID',
                                                    'logicalDrives': [
                                                        {'name': None, 'bootable': False, 'raidLevel': 'RAID5',
                                                         'sasLogicalJBODId': 1, 'driveTechnology': None,
                                                         'numPhysicalDrives': None}]}],
                                   'sasLogicalJBODs': [{'deviceSlot': 'Mezz 1',
                                                        'driveMinSizeGB': 146,
                                                        'name': 'RAID 5, 4 Drives',
                                                        'driveMaxSizeGB': 300,
                                                        'driveTechnology': 'SasHdd',
                                                        'numPhysicalDrives': 4,
                                                        'id': 1}]},
                  'sanStorage': None},
        '660_1': {'type': 'ServerProfileTemplateV4', 'serverProfileDescription': 'Profile created from 660_1 SPT',
                  'serverHardwareTypeUri': 'SHT:%s' % sht_660_1,
                  'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                  'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '660_1', 'description': 'Profile created from 660_1 SPT', 'affinity': 'Bay',
                  'connectionSettings': {'connections': deepcopy(conns), 'manageConnections': True},
                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                  'boot': {'manageBoot': True, 'order': ['HardDisk']},
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                               'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
                  'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True,
                  'iscsiInitiatorNameType': 'AutoGenerated',
                  'localStorage': {'controllers': [{'deviceSlot': 'Mezz 1', 'initialize': False, 'mode': 'RAID',
                                                    'logicalDrives': [
                                                        {'name': None, 'bootable': False, 'raidLevel': 'RAID5',
                                                         'sasLogicalJBODId': 1, 'driveTechnology': None,
                                                         'numPhysicalDrives': None}]}],
                                   'sasLogicalJBODs': [{'deviceSlot': 'Mezz 1',
                                                        'driveMinSizeGB': 146,
                                                        'name': 'RAID 5, 8 Drives',
                                                        'driveMaxSizeGB': 300,
                                                        'driveTechnology': 'SasHdd',
                                                        'numPhysicalDrives': 8,
                                                        'id': 1}]},
                  'sanStorage': None},
        }

"""
Used to create a dict of profile names to create
from the profile templates
"""
bays_480 = [3, 4, 7, 8, 9, 10]
bays_660 = [5, 6]

sp1 = {'%s_BAY_%i_480_1' % (e, i): '480_1' for i in bays_480 for e in ENCS}
sp2 = {'%s_BAY_%i_660_1' % (e, i): '660_1' for i in bays_660 for e in ENCS}
sp_from_spts = dict(sp1)
sp_from_spts.update(sp2)

"""
Used to assign the profiles to physical hardware enc-bay
"""
sp2bm1 = {'%s_BAY_%i_480_1' % (e, i): '%s, bay %i' % (e, i) for i in bays_480 for e in ENCS}
sp2bm2 = {'%s_BAY_%i_660_1' % (e, i): '%s, bay %i' % (e, i) for i in bays_660 for e in ENCS}
server_profile_to_bay_map = dict(sp2bm1)
server_profile_to_bay_map.update(sp2bm2)

# StRM
# StoreServ
STORESERV1_NAME = 'wpst3par-mini1-srv'
STORESERV1_HOSTNAME = 'wpst3par-mini1-srv.vse.rdlabs.hpecorp.net'
STORESERV1_POOL1 = 'FC_r1'
STORESERV1_POOL2 = 'FC_r5'


san_managers = [
    {"connectionInfo": [
        {'name': 'Type',
         'value': 'Brocade Network Advisor'},
        {"name": "Host",
            "displayName": "Host",
            "required": True,
            "value": "16.114.220.71",
            "valueFormat": "IPAddressOrHostname",
            "valueType": "String"},
        {"name": "Port",
            "displayName": "Port",
            "required": True,
            "value": 5989,
            "valueFormat": "None",
            "valueType": "Integer"},
        {"name": "Username",
            "displayName": "Username",
            "required": True,
            "value": "Administrator",
            "valueFormat": "None",
            "valueType": "String"},
        {"name": "Password",
            "displayName": "Password",
            "required": True,
            "value": "Wpsthpvse123",
            "valueFormat": "SecuritySensitive",
            "valueType": "String"},
        {"name": "UseSsl",
            "displayName": "UseSsl",
            "required": True,
            "value": True,
            "valueFormat": "None",
            "valueType": "Boolean"},
    ], },
]

storage_systems = [
    {'type': 'StorageSystemV4',
     'name': STORESERV1_NAME,
     'family': 'StoreServ',
     "hostname": STORESERV1_HOSTNAME,
     'credentials': {'username': '3paradm', 'password': '3pardata'},
     "deviceSpecificAttributes":
         {
             "discoveredDomains": ["NO DOMAIN"],
             "managedDomain": "NO DOMAIN",
     },
     }
]

storage_pools = [
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL1, "isManaged": True},
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL2, "isManaged": True}
]

#
# Create ${existing_volumes}
#

print_pretty = False

enc_short = [ENC1[-2:], ENC2[-2:], ENC3[-2:]]
volnames_private_r1 = ['FC_r1_Private_%s_Bay%s' % (e, b) for e in enc_short for b in bays_480]
volnames_private_r5 = ['FC_r5_Private_%s_Bay%s' % (e, b) for e in enc_short for b in bays_660]

SHARED = [20, 25, 30, 35, 40]
volnames_shared = ['FC_r%s_Shared_%sGb' % (p, s) for p in [1, 5] for s in SHARED]

all_volume_names = volnames_private_r1 + volnames_private_r5 + volnames_shared

vol_template = {
    "storageSystemUri": STORESERV1_NAME,
    "name": "name",
    "deviceVolumeName": "name",
    "isShareable": False,
}

existing_volumes = []

for volname in all_volume_names:
    this_vol = deepcopy(vol_template)
    if "Shared" in volname:
        isShareable = True
    else:
        isShareable = False

    this_vol['name'] = volname
    this_vol['deviceVolumeName'] = volname
    this_vol['isShareable'] = isShareable

    existing_volumes.append(this_vol)

if print_pretty:
    pretty_existing = json.dumps(existing_volumes, indent=4)
    print pretty_existing
#
#  End create ${existing_volumes}
#

#
# Create sanStorage['volumeAttachments']
#

host_types = {
    "480_1": "Windows 2012 / WS2012 R2",
    "660_1": "VMware (ESXi)"
}
pools = [STORESERV1_POOL1, STORESERV1_POOL2]
bays = bays_480 + bays_660
one_gb = 1073741824

# storage system targets.  Used for Validation not assigned by OneView at this time
storage_targets = ["20:12:00:02:AC:00:AF:0A", "21:12:00:02:AC:00:AF:0A", "20:11:00:02:AC:00:AF:0A", "21:11:00:02:AC:00:AF:0A"]
STORAGE_TARGETS_REGEXP = "2(0|1):1(1|2):00:02:AC:00:AF:0A"

attach_template = {
    "isBootVolume": False,

    "storagePaths": [
        {
            "targets": [],
            "targetSelector": "Auto",
            "connectionId": 1,
            "isEnabled": True,
        },
        {
            "targets": [],
            "targetSelector": "Auto",
            "connectionId": 2,
            "isEnabled": True,
        }
    ],
    # can't have both volumeName and volumeUri;  name and bytes for new vol, uri for existing.  Delete appropriately below.
    "volumeName": "",
    "volumeProvisionedCapacityBytes": "",
    "volumeUri": "",
    "volumeStorageSystemUri": "SSYS:" + STORESERV1_NAME,
    "volumeStoragePoolUri": "",
    "lunType": "Auto",
    "id": 0  # increment 1..n
}

profile_sanStorage = {}
volume_attachments = []
id = 0
for e in ENCS:
    enc_full_name = e
    e = e[-2:]
    for b in bays:
        if b in bays_660:
            t = '660_1'
        else:
            t = '480_1'

        for p in pools:
            for s in SHARED:
                shared_name = "%s_Shared_%sGb" % (p, s)
                # print shared_name, id
                id += 1
                this_shared = deepcopy(attach_template)
                map(this_shared.pop, ['volumeName', 'volumeProvisionedCapacityBytes'])
                this_shared['volumeUri'] = 'SVOL:' + shared_name
                this_shared['id'] = id
                this_shared['volumeStoragePoolUri'] = 'SPOOL:' + shared_name[:5]
                volume_attachments.append(this_shared)
                # print this_shared

        ov_create_name = "%s_Bay%s_OV_Created_vol" % (e, b)
        # print ov_create_name, id
        id += 1
        this_create = deepcopy(attach_template)
        this_create.pop('volumeUri')
        this_create['volumeStoragePoolUri'] = 'SPOOL:' + STORESERV1_POOL2
        this_create['volumeName'] = ov_create_name
        this_create['id'] = id
        this_create['permanent'] = False
        this_create['volumeProvisionedCapacityBytes'] = str(one_gb * b)
        this_create['volumeProvisionType'] = 'Thin'
        this_create['volumeShareable'] = False
        volume_attachments.append(this_create)

        if b in bays_660:
            private_name = "%s_Private_%s_Bay%s" % (STORESERV1_POOL2, e, b)
        else:
            private_name = "%s_Private_%s_Bay%s" % (STORESERV1_POOL1, e, b)
        # print private_name, id, '\n'
        id += 1
        this_private = deepcopy(attach_template)
        map(this_private.pop, ['volumeName', 'volumeProvisionedCapacityBytes'])
        this_private['volumeUri'] = 'SVOL:' + private_name
        this_private['id'] = id
        this_private['volumeStoragePoolUri'] = 'SPOOL:' + private_name[:5]
        volume_attachments.append(this_private)

        # print 'Profile: %s_Bay_%s_%s' % (enc_full_name, b, t)
        # print volume_attachments

        os_type = host_types[t]
        san_storage = {
            "sanStorage": {"manageSanStorage": True,
                           "hostOSType": os_type,
                           "volumeAttachments": volume_attachments}}
        profile_sanStorage["%s_BAY_%s_%s" % (enc_full_name, b, t)] = san_storage

        volume_attachments = []
        id = 0

if print_pretty:
    pretty_sanStorage = json.dumps(profile_sanStorage, indent=4)
    print pretty_sanStorage

# not used for Daisy, just used for development pythonHelperFunctions.py
ron_sanStorage = {
    "RonProfile": {
        "sanStorage": {"manageSanStorage": True,
                       "hostOSType": "Windows 2012 / WS2012 R2",
                       "volumeAttachments": [{"id": 1,
                                              "volumeUri": "SVOL:RonVol",
                                              "lunType": "Auto",
                                              "lun": None,
                                              "storagePaths": [{"isEnabled": True,
                                                                "connectionId": 1,
                                                                "targetSelector": "Auto",
                                                                "targets": []},
                                                               {"isEnabled": True,
                                                                "connectionId": 2,
                                                                "targetSelector": "Auto",
                                                                "targets": []}],
                                              "volumeStoragePoolUri": "SPOOL:FVT_Tbird_reg1_r1"},
                                             {"id": 2,
                                              "volumeUri": None,
                                              "isBootVolume": False,
                                              "lunType": "Auto",
                                              "lun": None,
                                              "storagePaths": [{"isEnabled": True,
                                                                "connectionId": 1,
                                                                "targetSelector": "Auto",
                                                                "targets": []},
                                                               {"isEnabled": True,
                                                                "connectionId": 2,
                                                                "targetSelector": "Auto",
                                                                "targets": []}],
                                              "volumeName":"RonTestVol2",
                                              "volumeDescription":"",
                                              "volumeStorageSystemUri": "SSYS:wpst3par-7200-7-srv",
                                              "volumeProvisionType":"Thin",
                                              "volumeProvisionedCapacityBytes":"1073741824",
                                              "volumeShareable":False,
                                              "permanent":False,
                                              "dataProtectionLevel":None,
                                              "volumeStoragePoolUri": "SPOOL:FVT_Tbird_reg1_r1"}]}}}
#
# end create volumeAttachments
#

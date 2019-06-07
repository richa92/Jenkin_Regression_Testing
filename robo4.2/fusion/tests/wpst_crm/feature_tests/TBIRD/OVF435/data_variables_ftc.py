from copy import deepcopy


def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'
interface = 'bond0'


EG1 = '3enc'
LE1 = 'LE1'

LIG1 = 'IBS1'
LIG2 = 'IBS2'
LIG3 = 'IBS3'

ENC1 = 'CN754404R9'
ENC2 = 'CN754406WS'
#ENC3 = 'CN754406WD'
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
    {"location": "CenterFront", "mountUri": "/rest/enclosures/000000%s" % ENC3, "relativeOrder": 0, "topUSlot": 18,
     "uHeight": 10},
    {"location": "CenterFront", "mountUri": "/rest/enclosures/000000%s" % ENC2, "relativeOrder": 0, "topUSlot": 28,
     "uHeight": 10},
    {"location": "CenterFront", "mountUri": "/rest/enclosures/000000%s" % ENC1, "relativeOrder": 0, "topUSlot": 38,
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
    {'userName': 'kelly', 'password': 'hpvse123', 'fullName': 'Kelly Rollins', 'roles': ['Infrastructure administrator'],
     'emailAddress': 'kelly.rollins@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'clay', 'password': 'hpvse123', 'fullName': 'Clay Graves', 'roles': ['Infrastructure administrator'],
     'emailAddress': 'clayton.graves@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'lori', 'password': 'hpvse123', 'fullName': 'Lori Winter', 'roles': ['Infrastructure administrator'],
     'emailAddress': 'lori.winter@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'russell', 'password': 'hpvse123', 'fullName': 'Russell Briggs', 'roles': ['Infrastructure administrator'],
     'emailAddress': 'rbriggs@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'jeff', 'password': 'hpvse123', 'fullName': 'Jeff Watson',
     'roles': ['Infrastructure administrator'],
     'emailAddress': 'jeff.watson@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndRoles'},
    {'userName': 'patrick', 'password': 'hpvse123', 'fullName': 'Patrick Shapard',
     'roles': ['Infrastructure administrator'],
     'emailAddress': 'patrick.shapard@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
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
     'type': 'UserAndRoles'}
]

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
       'ethernetNetworkType': 'Untagged'}
      ]

e2 = [{'name': n,
       'type': 'ethernet-networkV300',
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(1, 2000)]

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
                ]

fcoe_networks = [{'name': n,
                  'type': 'fcoe-networkV300',
                  'vlanId': int(n[5:])} for n in rlist(3001, 3256, 'fcoe_')]

fc_networks = [{'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': '%s' % n,
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'} for n in rlist(1, 6, 'fc_fa_')]

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
                   'type': 'sas-logical-interconnect-group',
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
    LIG2:  {'name': LIG2,
            'type': 'logical-interconnect-groupV300',
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
           'type': 'logical-interconnect-groupV300',
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
                    'type': 'EnclosureGroupV400',
                    'enclosureCount': 3,
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'interconnectBayMappingCount': 6,
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


LE_SupportDump_Payload = {"encrypt": True, "errorCode": "MyDump16", "excludeApplianceDump": False}

"""
Server Profile Templates
"""
# TODO: will need to change these SHT types!

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

spts = {'480_1': {'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                  'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
                  'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                  'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '480_1', 'description': '', 'affinity': 'Bay',
                  'connectionSettings': {'connections': deepcopy(conns), 'manageConnections': True},
                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                  'boot': {'manageBoot': True, 'order': ['HardDisk']},
                  #'boot': {'manageBoot': True, 'order': ['USB', 'CD', 'HardDisk', 'PXE']},
                  #'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                               'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
                  'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True,
                  'iscsiInitiatorNameType': 'AutoGenerated', 'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                  'sanStorage': None},
        '660_1': {'type': 'ServerProfileTemplateV3', 'serverProfileDescription': '',
                  'serverHardwareTypeUri': 'SHT:%s' % sht_660_1,
                  'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                  'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '660_1', 'description': '', 'affinity': 'Bay',
                  'connectionSettings': {'connections': deepcopy(conns), 'manageConnections': True},
                  #'boot': {'manageBoot': True, 'order': ['USB', 'CD', 'HardDisk', 'PXE']},
                  #'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                  'boot': {'manageBoot': True, 'order': ['HardDisk']},
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                               'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
                  'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True,
                  'iscsiInitiatorNameType': 'AutoGenerated', 'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
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
sp2bm1 = {'480_1_%s_BAY_%i' % (e, i): '%s, bay %i' % (e, i) for i in bays_480 for e in ENCS}
#sp2bm2 = {'660_1_%s_BAY_%i' % (e, i): '%s, bay %i' % (e, i) for i in bays_660 for e in ENCS}
server_profile_to_bay_map = dict(sp2bm1)
#server_profile_to_bay_map.update(sp2bm2)

pass

"""
ufg_ligs = [
    {'name': 'Enc3-LIG3',
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc3bay3ICMMap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [deepcopy(uplink_set['bay3-fcoe1002-us']),
                    deepcopy(uplink_set['bay6-fcoe1003-us']),
                    deepcopy(uplink_set['bay3-tunnel4xC-us']),
                    deepcopy(uplink_set['bay3-untagged4xC-us']),
#                    deepcopy(uplink_set['bay3-enet4x-us']),
                    deepcopy(uplink_set['mlag1-enet4x-us']),
                    deepcopy(uplink_set['mlag3-enetQ-us'])
                    ],
     },
     {'name': 'Enc3-LIG3',
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc3bay3ICMMap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [deepcopy(uplink_set['bay3-fcoe1002-us']),
                    deepcopy(uplink_set['bay3-tunnel4xC-us']),
                    deepcopy(uplink_set['bay3-untagged4xC-us']),
 #                   deepcopy(uplink_set['bay3-enet4x-us']),
                    deepcopy(uplink_set['us_enet_crm']),
                    deepcopy(uplink_set['mlag3-enetQ-us'])
                    ],
     },
     {'name': 'Enc3-LIG3',
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc3bay3ICMMap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [deepcopy(uplink_set['bay3-fcoe1002-us']),
                    deepcopy(uplink_set['bay6-fcoe1003-us']),
                    deepcopy(uplink_set['bay3-tunnel4xC-us']),
                    deepcopy(uplink_set['bay3-untagged4xC-us']),
                    deepcopy(uplink_set['bay3-enet4x-us']),
                    deepcopy(uplink_set['us_enet_crm']),
                    deepcopy(uplink_set['mlag3-enetQ-us'])
                    ],
     }
]

"""




"""
Maps sever profile to encl, bay.  First column: server profile name. Second column: Enclosure, bay #



# Server assignment
# Enclosure 1: (bay 1-2: Big bird; bay 5/11: Red Bird; bay 3-4,6-10,12: BlackBird)
# Enclosure 2: (bay 1-2: Big bird; bay 5/11, 6/12: Red Bird; bay 3-4,7-10: BlackBird)
# Enclosure 3: (bay 1-2: Big bird; bay 6/12: Red Bird; bay 3-5,7-11: BlackBird)


server_profile_to_bay_map = {
#    '%s_sp_bay1' % ENC1: '%s, bay 1' % ENC1,
#                             '%s_sp_bay3' % ENC1: '%s, bay 3' % ENC1,
#                             '%s_sp_bay4' % ENC1: '%s, bay 4' % ENC1,
#                             '%s_sp_bay5' % ENC1: '%s, bay 5' % ENC1,
#                             '%s_sp_bay6' % ENC1: '%s, bay 6' % ENC1,
#                            '%s_sp_bay7' % ENC1: '%s, bay 7' % ENC1,
                            '%s_sp_bay8' % ENC1: '%s, bay 8' % ENC1,
#                             '%s_sp_bay9' % ENC1: '%s, bay 9' % ENC1,
#                             '%s_sp_bay10' % ENC1: '%s, bay 10' % ENC1,
#                             '%s_sp_bay12' % ENC1: '%s, bay 12' % ENC1,
#                             '%s_sp_bay1' % ENC2: '%s, bay 1' % ENC2,
#                             '%s_sp_bay3' % ENC2: '%s, bay 3' % ENC2,
#                             '%s_sp_bay4' % ENC2: '%s, bay 4' % ENC2,
#                             '%s_sp_bay5' % ENC2: '%s, bay 5' % ENC2,
#                             '%s_sp_bay6' % ENC2: '%s, bay 6' % ENC2,
#                             '%s_sp_bay7' % ENC2: '%s, bay 7' % ENC2,
                             '%s_sp_bay8' % ENC2: '%s, bay 8' % ENC2,
#                             '%s_sp_bay9' % ENC2: '%s, bay 9' % ENC2,
#                             '%s_sp_bay10' % ENC2: '%s, bay 10' % ENC2,
#                             '%s_sp_bay1' % ENC3: '%s, bay 1' % ENC3,
#                             '%s_sp_bay3' % ENC3: '%s, bay 3' % ENC3,
#                             '%s_sp_bay4' % ENC3: '%s, bay 4' % ENC3,
#                             '%s_sp_bay5' % ENC3: '%s, bay 5' % ENC3,
#                             '%s_sp_bay6' % ENC3: '%s, bay 6' % ENC3,
#                             '%s_sp_bay7' % ENC3: '%s, bay 7' % ENC3,
#                             '%s_sp_bay8' % ENC3: '%s, bay 8' % ENC3,
                             '%s_sp_bay9' % ENC3: '%s, bay 9' % ENC3,
#                            '%s_sp_bay10' % ENC3: '%s, bay 10' % ENC3,
#                             '%s_sp_bay11' % ENC3: '%s, bay 11' % ENC3
                             }

# Mezz 3 connections [Ethernet]
# Mezz 3:1-a	net_401
# Mezz 3:2-a    net_403
# Mezz 3:1-b	fcoenetwork1002
# Mezz 3:2-b
# Mezz 3:1-c	tunnelnetwork1
# Mezz 3:2-c	net_402
# Mezz 3:1-d	untaggednetwork1
# Mezz 3:2-d	VlanTrunk1

potash_connection = [{'id': 31, 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                      'boot': {'priority': 'NotBootable'}},
                     #                     {'id': 32, 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-a',
                     #                      'requestedMbps': '2500', 'networkUri': 'ETH:net_403',
                     #                      'boot': {'priority': 'NotBootable'}},
                     {'id': 33, 'functionType': 'FibreChannel', 'portId': 'Mezz %s:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                      'boot': {'priority': 'NotBootable'}},
                     #                     {'id': 35, 'functionType': 'Ethernet', 'portId': 'Mezz%s:1-c',
                     #                      'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnetwork1',
                     #                      'boot': {'priority': 'NotBootable'}},
                     {'id': 36, 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-c',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_402',
                      'boot': {'priority': 'NotBootable'}},
                     #                     {'id': 37, 'functionType': 'Ethernet', 'portId': 'Mezz%s:1-d',
                     #                      'requestedMbps': '2500', 'networkUri': 'ETH:untaggednetwork1',
                     #                      'boot': {'priority': 'NotBootable'}},
                     {'id': 38, 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-d',
                      'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1',
                      'boot': {'priority': 'NotBootable'}},

                     ]

# Mezz 2 connections [FC connections]
carbon_connection = [{'id': 21, 'functionType': 'FC', 'portId': 'Mezz %s:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FC:FA_FCnetwork1',
                      'boot': {'priority': 'NotBootable'}},
                     {'id': 22, 'functionType': 'FC', 'portId': 'Mezz %s:2-b',
                      'requestedMbps': '2500', 'networkUri': 'FC:FA_FCnetwork2',
                      'boot': {'priority': 'NotBootable'}},
]


# Mezz 1 connections [FC connections]
natasha_connection = [{'id': 11, 'functionType': 'FC', 'portId': 'Mezz %s:1-a',
                       'requestedMbps': '2500', 'networkUri': 'FC:FA_FCnetwork',
                       'boot': {'priority': 'NotBootable'}},
                      ]


# Server profile connection definitions
def make_connections_list(connections, mezz='3'):
    connections = deepcopy(connections)
    for connection in connections:
        connection['portId'] = connection['portId'] % mezz
    return connections


# #1 for Mezz1
conn = make_connections_list(potash_connection)
conn1 = make_connections_list(natasha_connection, mezz='1')
conn2 = make_connections_list(carbon_connection, mezz='2')
conn3 = make_connections_list(potash_connection, mezz='3')
conn4 = make_connections_list(natasha_connection, mezz='4')
conn5 = make_connections_list(carbon_connection, mezz='5')
conn6 = make_connections_list(potash_connection, mezz='6')


def make_server_profile_dict2(name, connections, serverHardwareUri=None, serverHardwareTypeUri=None, enclosureUri=None,
                             enclosureGroupUri=None):

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
    return [make_server_profile_dict2(*p) for p in profiles]

# Profiles for hardware
#             Profile Name,        Mezz,    , SHT           ,     , Enc group

# conn1 + Conn2 +... + Conn6
#    ['%s_sp_bay1' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
#    ['%s_sp_bay1' % ENC1, conn2 + conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],

add_multi_conn_server_profiles = [
#    ['%s_sp_bay1' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    # ['%s_sp_bay3' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay4' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay5' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay6' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay7' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    ['%s_sp_bay8' % ENC1, conn3, None, 'SY 480 Gen9 6', None, 'EG:%s' % EG1],
    #            ['%s_sp_bay9' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay10' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay12' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay1' % ENC2, conn3, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bayconn3' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay4' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay5' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay6' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay7' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    ['%s_sp_bay8' % ENC2, conn3, None, 'SY 480 Gen9 7', None, 'EG:%s' % EG1],
    #            ['%s_sp_bay9' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay10' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay12' % ENC2, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay1' % ENC3, conn3, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay3' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay4' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay5' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay6' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay7' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
#    ['%s_sp_bay8' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    ['%s_sp_bay9' % ENC3, conn3, None, 'SY 480 Gen9 2', None, 'EG:%s' % EG1],
    #            ['%s_sp_bay10' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay11' % ENC3, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG]
]

# add IBS2 connections
# conn1 + Conn2 +... + Conn6
#    ['%s_sp_bay1' % ENC1, conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
#    ['%s_sp_bay1' % ENC1, conn2 + conn3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],

edit_multi_conn_server_profiles = [
#    ['%s_sp_bay1' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    # ['%s_sp_bay3' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay4' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay5' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay6' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay7' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    ['%s_sp_bay8' % ENC1, conn3+conn2, None, 'SY 480 Gen9 6', None, 'EG:%s' % EG1],
    #            ['%s_sp_bay9' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay10' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay12' % ENC1, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay1' % ENC2, conn3+conn2, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bayconn3+conn2' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay4' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay5' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay6' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay7' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    ['%s_sp_bay8' % ENC2, conn3+conn2, None, 'SY 480 Gen9 7', None, 'EG:%s' % EG1],
    #            ['%s_sp_bay9' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay10' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay12' % ENC2, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay1' % ENC3, conn3+conn2, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay3' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay4' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay5' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay6' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay7' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
#    ['%s_sp_bay8' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    ['%s_sp_bay9' % ENC3, conn3+conn2, None, 'SY 480 Gen9 2', None, 'EG:%s' % EG1],
    #            ['%s_sp_bay10' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
    #            ['%s_sp_bay11' % ENC3, conn3+conn2, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG]
]

add_server_profiles = build_profiles(add_multi_conn_server_profiles)

edit_server_profiles = build_profiles(edit_multi_conn_server_profiles)

# old data - delete after testing
#
# def make_server_profile_dict(name, mezz=3, serverHardwareUri=None, serverHardwareTypeUri=None, enclosureUri=None,
#                              enclosureGroupUri=None):
#     connections = [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-a' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'ETH:untaggednetwork1',
#                     'boot': {'priority': 'NotBootable'}},
#                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-a' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
#                     'boot': {'priority': 'NotBootable'}},
#                    {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:1-b' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1002',
#                     'boot': {'priority': 'NotBootable'}},
# #                   {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:2-b' % mezz,
# #                    'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1003',
# #                    'boot': {'priority': 'NotBootable'}},
#                    {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-c' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnetwork1',
#                     'boot': {'priority': 'NotBootable'}},
#                    {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-c' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'ETH:net_402',
#                     'boot': {'priority': 'NotBootable'}},
#                    {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-d' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
#                     'boot': {'priority': 'NotBootable'}},
#                    {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-d' % mezz,
#                     'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
#                     'boot': {'priority': 'NotBootable'}},
#                    ]
#
#     return {'type': 'ServerProfileV7',
#             'serverHardwareUri': serverHardwareUri,
#             'serverHardwareTypeUri': serverHardwareTypeUri,
#             'enclosureUri': enclosureUri,
#             'enclosureGroupUri': enclosureGroupUri,
#             'serialNumberType': 'Virtual',
#             'macType': 'Virtual',
#             'wwnType': 'Virtual',
#             'name': name,
#             'description': '',
#             'affinity': 'Bay',
#             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
#             'boot': {'manageBoot': True, 'order': ['HardDisk']},
#             'connections': connections}
#
#

# def enc_profiles(enc, eg='EG', count=13):
#     return [['%s profile%s' % (enc, N), '%s, bay %s' % (enc, N), '', 'ENC:%s' % enc, 'EG:%s' % eg] for N in
#             xrange(1, count)]

"""



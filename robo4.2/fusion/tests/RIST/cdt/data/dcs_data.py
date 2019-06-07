from copy import deepcopy
import json

from common_data import *


def rlist(start, end, prefix='Net_', suffix='', step=1):
    return ['%s%s%s' % (prefix, str(x), suffix)
            for x in xrange(start, end + 1, step)]


def us(**kwargs):
    return {'name': kwargs.get('name', None),
            'ethernetNetworkType': kwargs.get('ethernetNetworkType', 'Tagged'),
            'networkType': 'Ethernet',
            'networkUris': kwargs.get('networkUris', None),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': kwargs.get('logicalPortConfigInfos', None)}


def lig(**kwargs):
    return {'name': kwargs.get('name', None),
            'type': kwargs.get('type', 'logical-interconnect-groupV5'),
            'enclosureType': kwargs.get('enclosureType', 'SY12000'),
            'interconnectMapTemplate': kwargs.get('interconnectMapTemplate', None),
            'enclosureIndexes': kwargs.get('enclosureIndexes', [1]),
            'interconnectBaySet': kwargs.get('interconnectBaySet', 3),
            'redundancyType': kwargs.get('redundancyType', 'HighlyAvailable'),
            'uplinkSets': kwargs.get('uplinkSets', []),
            'internalNetworkUris': kwargs.get('internalNetworkUris', None),
            }


uplink_sets = {'Q6': us(name='Tagged 1-100',
                        networkUris=rlist(1, 100),
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q6', 'speed': 'Auto'}]),

               'Q4': us(name='Tunnel',
                        networkUris=['tunnel_1'],
                        ethernetNetworkType='Tunnel',
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q4', 'speed': 'Auto'}]),
               'Q1': us(name='Untagged',
                        networkUris=['untagged_1'],
                        ethernetNetworkType='Untagged',
                        logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                 'port': 'Q1', 'speed': 'Auto'}]),
               'BigPipe': us(name='BigPipe',
                             networkUris=rlist(101, 3966),
                             logicalPortConfigInfos=[{'enclosure': '1', 'bay': '3',
                                                      'port': p,
                                                      'speed': 'Auto'}
                                                     for p in sorted(['Q%i.%i' % (n, i)
                                                                      for i in range(1, 5)
                                                                      for n in (3, 5)])])
               }

# APPLIANCE_IP = ''

# ssh_server_ip = '15.114.112.61'  # Used in appliance_certificates1.txt

SSH_USER = 'root'
SSH_PASS = 'hpvse1'
interface = 'bond0'
one_gb = 1073741824

EG1 = '3enc'
LE1 = 'LE1'

LIG1 = 'SASLIG1'
LIG2 = 'CarbonLIG1'
LIG3 = 'PotashLIG'
LIG4 = 'SASLIG2'
LIG5 = 'SASLIG3'
LIG6 = 'CarbonLIG2'
LIG7 = 'CarbonLIG3'

ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'

ENCS = [ENC1, ENC2, ENC3]

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

appliance = {'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': '',
               'activeNode': '1',
               'unconfigure': False,
               'ipv4Type': 'STATIC',
               'ipv4Subnet': '255.255.240.0',
               'ipv4Gateway': '16.125.64.1',
               'ipv4NameServers': ['16.125.24.19', '16.125.24.20'],
               'virtIpv4Addr': '16.125.69.189',
               'app1Ipv4Addr': '16.125.69.189',
               'app2Ipv4Addr': '',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': '',
               'confOneNode': True,
               'domainName': 'vse.rdlabs.hpecorp.net',
               'aliasDisabled': True,
               }],
             }

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hpecorp.net'],
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
    {
        'userName': 'lori',
        'password': 'hpvse123',
        'fullName': 'LoriWinter',
        "permissions": [{
            "roleName": "Infrastructure administrator"
        }],
        'emailAddress': 'lori.winter@hpe.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'russell',
        'password': 'hpvse123',
        'fullName': 'RussellBriggs',
        "permissions": [{
            "roleName": "Infrastructure administrator"
        }],
        'emailAddress': 'rbriggs@hpe.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'ron',
        'password': 'hpvse123',
        'fullName': 'RonSoto',
        "permissions": [{
            "roleName": "Infrastructure administrator"
        }],
        'emailAddress': 'ron.soto@hpe.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'ramya',
        'password': 'hpvse123',
        'fullName': 'RamyaParasuram',
        "permissions": [{
            "roleName": "Infrastructure administrator"
        }],
        'emailAddress': 'ramya@hpe.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'Serveradmin',
        'password': 'Serveradmin',
        'fullName': 'Serveradmin',
        "permissions": [{
            "roleName": "Server administrator"
        }],
        'emailAddress': 'sarah@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'Networkadmin',
        'password': 'Networkadmin',
        'fullName': 'Networkadmin',
        "permissions": [{"roleName": "Network administrator"}],
        'emailAddress': 'nat@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'Backupadmin',
        'password': 'Backupadmin',
        'fullName': 'Backupadmin',
        "permissions": [{"roleName": "Backup administrator"}],
        'emailAddress': 'backup@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'Noprivledge',
        'password': 'Noprivledge',
        'fullName': 'Noprivledge',
        "permissions": [{"roleName": "Read only"}],
        'emailAddress': 'rheid@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
    {
        'userName': 'ES',
        'password': 'EShpvse123',
        'fullName': 'EngineeringServices',
        "permissions": [{"roleName": "Infrastructure administrator"}],
        'emailAddress': 'esrequests@hpe.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'
    },
]

e1 = [{'name': 'Tunnel1',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'Tunnel2',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tunnel'},
      {'name': 'Untagged1',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': None,
       'purpose': 'General',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Untagged'},
      {'name': 'iSCSI_2101',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': 2101,
       'purpose': 'ISCSI',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged'},
      {'name': 'iSCSI_2102',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': 2102,
       'purpose': 'ISCSI',
       'smartLink': True,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged'}
      ]

e2 = [{'name': n,
       'type': ETHERNET_NETWORK_TYPE,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(100, 2100)]

ethernet_networks = e1 + e2

network_sets = [{'name': 'NetSet1', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(101, 161),
                 'nativeNetworkUri': None},
                {'name': 'NetSet2', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(162, 222),
                 'nativeNetworkUri': None},
                {'name': 'NetSet3', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(223, 283),
                 'nativeNetworkUri': None},
                {'name': 'NetSet4', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(284, 344),
                 'nativeNetworkUri': None},
                {'name': 'NetSet5', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(345, 405),
                 'nativeNetworkUri': None},
                {'name': 'NetSet6', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(406, 466),
                 'nativeNetworkUri': None},
                {'name': 'NetSet7', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(467, 527),
                 'nativeNetworkUri': None},
                {'name': 'NetSet8', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(528, 588),
                 'nativeNetworkUri': None},
                ]

fcoe_networks = [
    {'name': 'FCOE-SideA-3201',
     'managedSanUri': 'FCSan:VSAN3201',
     'type': FCOE_NETWORK_TYPE,
     'vlanId': 3201},
    {'name': 'FCOE-SideB-3202',
     'managedSanUri': 'FCSan:VSAN3202',
     'type': FCOE_NETWORK_TYPE,
     'vlanId': 3202},
    {'name': 'FCOE-SideA-3301',
     'managedSanUri': 'FCSan:VSAN3301',
     'type': FCOE_NETWORK_TYPE,
     'vlanId': 3301},
    {'name': 'FCOE-SideB-3302',
     'managedSanUri': 'FCSan:VSAN3302',
     'type': FCOE_NETWORK_TYPE,
     'vlanId': 3302},
]

fc1 = [{'type': FC_NETWORK_TYPE,
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True,
        'name': 'FC-SAN-A',
        'connectionTemplateUri': None,
        'managedSanUri': 'FCSan:switch1-SAN-A-10:00:c4:f5:7c:46:b5:24',
        'fabricType': 'FabricAttach'}]

fc2 = [{'type': FC_NETWORK_TYPE,
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True,
        'name': 'FC-SAN-B',
        'connectionTemplateUri': None,
        'managedSanUri': 'FCSan:switch2-SAN-B-10:00:c4:f5:7c:60:7d:55',
        'fabricType': 'FabricAttach'}]

fc_networks = fc1 + fc2

potash_us = {

    'FCOE-SideA': {
        'name': 'FCOE-SideA',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['FCOE-SideA-3201'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.4', 'speed': 'Auto'}
        ]
    },
    'FCOE-SideB': {
        'name': 'FCOE-SideB',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['FCOE-SideB-3202'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.4', 'speed': 'Auto'}
        ]
    },
    'Ethernet-Tunnel': {
        'name': 'Ethernet-Tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['Tunnel1'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.3', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6.3', 'speed': 'Auto'}
        ]
    },
    'Ethernet-Untagged': {
        'name': 'Ethernet-Untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['Untagged1'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6.2', 'speed': 'Auto'}
        ]
    },
    'Ethernet-Tagged': {
        'name': 'Ethernet-Tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(0100, 2100) + ['iSCSI_2101'  'iSCSI_2102'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'}
        ]
    },
    'iSCSI': {
        'name': 'iSCSI',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['iSCSI_283'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}
        ]
    },
    # 'MLAG222-ENET-4x10': {
    #     'name': 'MLAG222-ENET-4x10',
    #     'ethernetNetworkType': 'Tagged',
    #     'networkType': 'Ethernet',
    #     'networkUris': rlist(100, 461),
    #     'mode': 'Auto',
    #     'nativeNetworkUri': None,
    #     'logicalPortConfigInfos': [
    #         {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
    #         {'enclosure': '1', 'bay': '3', 'port': 'Q2.2', 'speed': 'Auto'},
    #         {'enclosure': '1', 'bay': '3', 'port': 'Q2.3', 'speed': 'Auto'},
    #         {'enclosure': '1', 'bay': '3', 'port': 'Q2.4', 'speed': 'Auto'},
    #         {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
    #         {'enclosure': '2', 'bay': '6', 'port': 'Q2.2', 'speed': 'Auto'},
    #         {'enclosure': '2', 'bay': '6', 'port': 'Q2.3', 'speed': 'Auto'},
    #         {'enclosure': '2', 'bay': '6', 'port': 'Q2.4', 'speed': 'Auto'},
    #     ]
    # },
    # 'MLAG666-ENET-40': {
    #     'name': 'MLAG666-ENET-40',
    #     'ethernetNetworkType': 'Tagged',
    #     'networkType': 'Ethernet',
    #     'networkUris': rlist(500, 861),
    #     'mode': 'Auto',
    #     'nativeNetworkUri': None,
    #     'logicalPortConfigInfos': [
    #         {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
    #         {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
    #     ]
    # },
}

carbon_US = [{'name': 'SAN-A',
              'ethernetNetworkType': 'NotApplicable',
              'networkType': 'FibreChannel',
              'networkUris': ['FC-SAN-A'],
              'nativeNetworkUri': None,
              'mode': 'Auto',
              'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '2', 'port': '3', 'speed': 'Auto'},
                                         {'enclosure': '-1', 'bay': '2', 'port': '4', 'speed': 'Auto'}]},
             {'name': 'SAN-B',
              'ethernetNetworkType': 'NotApplicable',
              'networkType': 'FibreChannel',
              'networkUris': ['FC-SAN-B'],
              'nativeNetworkUri': None,
              'mode': 'Auto',
              'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '5', 'port': '3', 'speed': 'Auto'},
                                         {'enclosure': '-1', 'bay': '5', 'port': '4', 'speed': 'Auto'}]},
             ]

###
# LIGs
###

sas_ligs = {LIG1: {'name': LIG1,
                   'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1, 'type': NATASHA, 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1, 'type': NATASHA, 'enclosureIndex': 1},
                   ],
                   'enclosureIndexes': [1],
                   'interconnectBaySet': 1,
                   },
            LIG4: {'name': LIG4,
                   'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1, 'type': NATASHA, 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1, 'type': NATASHA, 'enclosureIndex': 1},
                   ],
                   'enclosureIndexes': [1],
                   'interconnectBaySet': 1,
                   },
            LIG5: {'name': LIG5,
                   'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1, 'type': NATASHA, 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1, 'type': NATASHA, 'enclosureIndex': 1},
                   ],
                   'enclosureIndexes': [1],
                   'interconnectBaySet': 1,
                   },
            }

ligs = {LIG2: lig(name=LIG2,
                  interconnectMapTemplate=[{'bay': 2, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1},
                                           {'bay': 5, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1}],
                  enclosureIndexes=[-1],
                  interconnectBaySet=2,
                  redundancyType='Redundant',
                  uplinkSets=deepcopy(carbon_US)),
        LIG6: lig(name=LIG6,
                  interconnectMapTemplate=[{'bay': 2, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1},
                                           {'bay': 5, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1}],
                  enclosureIndexes=[-1],
                  interconnectBaySet=2,
                  redundancyType='Redundant',
                  uplinkSets=deepcopy(carbon_US)),
        LIG7: lig(name=LIG7,
                  interconnectMapTemplate=[{'bay': 2, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1},
                                           {'bay': 5, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1}],
                  enclosureIndexes=[-1],
                  interconnectBaySet=2,
                  redundancyType='Redundant',
                  uplinkSets=deepcopy(carbon_US)),
        LIG3: lig(name=LIG3,
                  interconnectMapTemplate=[{'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
                                           {'bay': 6, 'enclosure': 1, 'type': CL20, 'enclosureIndex': 1},
                                           {'bay': 3, 'enclosure': 2, 'type': CL20, 'enclosureIndex': 2},
                                           {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
                                           {'bay': 3, 'enclosure': 3, 'type': CL20, 'enclosureIndex': 3},
                                           {'bay': 6, 'enclosure': 3, 'type': CL20, 'enclosureIndex': 3}
                                           ],
                  enclosureIndexes=[1, 2, 3],
                  uplinkSets=[deepcopy(v) for v in potash_us.itervalues()])}


enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 3,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 1},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG4, 'enclosureIndex': 2},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG5, 'enclosureIndex': 3},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG6, 'enclosureIndex': 2},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG7, 'enclosureIndex': 3},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 1},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG4, 'enclosureIndex': 2},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG5, 'enclosureIndex': 3},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG6, 'enclosureIndex': 2},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG7, 'enclosureIndex': 3},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    }
              }

les = [{'name': LE1,
        'enclosureUris': ['ENC:%s' % ENC1, 'ENC:%s' % ENC2, 'ENC:%s' % ENC3],
        'enclosureGroupUri': 'EG:%s' % EG1,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       ]

"""
Server Profile Templates
"""
sht_480_1 = 'SY 480 Gen9 1'
sht_660_1 = 'SY 660 Gen9 1'

conns_SPT_480_2 = [{"id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto",
                    "networkUri": "FC:FC-SAN-A", "lagName": None, "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto",
                    "networkUri": "FC:FC-SAN-B", "lagName": None, "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 3, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet5", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 4, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet6", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet7", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet8", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 7, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet5", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 8, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet6", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 9, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet7", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   {"id": 10, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500",
                    "networkUri": "NS:NetSet8", "lagName": None, "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable",
                             "iscsi": {}}},
                   ]

spts = {'SPT_480_2': {'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 480 Gen9 1',
                      'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
                      'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                      'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'SPT_480_2_1',
                      'description': 'Server Profile Template created from SY 480 Gen9 1', 'affinity': 'Bay',
                      'connectionSettings': {'connections': deepcopy(conns_SPT_480_2), 'manageConnections': True},
                      'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
                      'boot': {'manageBoot': True, 'order': ['HardDisk']},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                                   'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'controllers': [{'deviceSlot': 'Embedded', 'initialize': True, 'mode': 'RAID',
                                                        'logicalDrives': [{'name': "ld2", 'bootable': True, 'raidLevel': 'RAID5',
                                                                           'sasLogicalJBODId': None, 'driveTechnology': "SasHdd", 'numPhysicalDrives': 3}]}],
                                       'sasLogicalJBODs': []},
                      'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                     'volumeAttachments': [{'id': 1,
                                                            "volume": {"properties": {"name": "vol1",
                                                                                      "size": 11811160064,
                                                                                      "provisioningType": "Thin",
                                                                                      "isShareable": False,
                                                                                      "storagePool": "SP:FC_r5"
                                                                                      },
                                                                       "isPermanent": False,
                                                                       "templateUri": 'ROOT:FC_r5'},
                                                            "volumeStorageSystemUri": "SSYS:wpst3par-mini1-srv",
                                                            'isBootVolume': True,
                                                            'lunType': 'Auto',
                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []}]
                                                            }]}},
        #    '660_1': {'type': 'ServerProfileTemplateV5', 'serverProfileDescription': 'Profile created from 660_1 SPT',
        #          'serverHardwareTypeUri': 'SHT:%s' % sht_660_1,
        #          'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        #          'macType': 'Virtual', 'wwnType': 'Virtual', 'name': '660_1',
        #          'description': 'Profile created from 660_1 SPT', 'affinity': 'Bay',
        #          'connectionSettings': {'connections': deepcopy(conns), 'manageConnections': True},
        #          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
        #          'boot': {'manageBoot': True, 'order': ['HardDisk']},
        #          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
        #                       'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        #          'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True,
        #          'iscsiInitiatorNameType': 'AutoGenerated',
        #          'localStorage': {'controllers': [{'deviceSlot': 'Mezz 1', 'initialize': False, 'mode': 'RAID',
        #                                            'logicalDrives': [
        #                                                {'name': None, 'bootable': False, 'raidLevel': 'RAID5',
        #                                                 'sasLogicalJBODId': 1, 'driveTechnology': None,
        #                                                 'numPhysicalDrives': None}]}],
        #                           'sasLogicalJBODs': [{'deviceSlot': 'Mezz 1',
        #                                                'driveMinSizeGB': 146,
        #                                                'name': 'RAID 5, 8 Drives',
        #                                                'driveMaxSizeGB': 300,
        #                                                'driveTechnology': 'SasHdd',
        #                                                'numPhysicalDrives': 8,
        #                                                'id': 1}]},
        #          'sanStorage': None},
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

brocade_network_advisor = {
    "connectionInfo": [
        {'name': 'Type',
            'value': 'Brocade Network Advisor'},
        {"name": "Host",
            "displayName": "Host",
            "required": True,
            "value": "16.114.218.248",
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
            "value": "hpvse123",
            "valueFormat": "SecuritySensitive",
            "valueType": "String"},
        {"name": "UseSsl",
            "displayName": "UseSsl",
            "required": True,
            "value": True,
            "valueFormat": "None",
            "valueType": "Boolean"},
    ],
}

HP_5900_san_manager = {
    "connectionInfo": [
        {'name': 'Type',
         'value': 'HPE'},
        {"name": "Host",
         "value": "16.125.33.205"},
        {"name": "SnmpPort",
         "value": 161},
        {"name": "SnmpUserName",
         "value": "defaultUser"},
        {"name": "SnmpAuthLevel",
         "value": "AUTHPRIV"},
        {"name": "SnmpAuthProtocol",
         "value": "MD5"},
        {"name": "SnmpAuthString",
         "value": "authPass123"},
        {"name": "SnmpPrivProtocol",
         "value": "AES128"},
        {"name": "SnmpPrivString",
         "value": "privPass123"},
    ],
}

san_managers = [
    brocade_network_advisor,
    HP_5900_san_manager,
]

storage_systems = [
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STORESERV1_NAME,
     'family': 'StoreServ',
     "hostname": STORESERV1_HOSTNAME,
     'credentials': {'username': '3paradm', 'password': '3pardata'},
     "deviceSpecificAttributes":
         {"discoveredDomains": ["NO DOMAIN"], "managedDomain": "NO DOMAIN"},
     },
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STOREVIRTUAL_NAME,
     'family': 'StoreVirtual',
     "hostname": STOREVIRTUAL_HOSTNAME,
     'credentials': {'username': 'admin', 'password': 'hpvse123'},
     "ports": [
         {"actualNetworkUri": 'ETH:iSCSI_283'}
     ]
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

# storage system targets.  Used for Validation not assigned by OneView at this time
storage_targets = ["20:12:00:02:AC:00:AF:0A",
                   "21:12:00:02:AC:00:AF:0A",
                   "20:11:00:02:AC:00:AF:0A",
                   "21:11:00:02:AC:00:AF:0A"]

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

#
# end create volumeAttachments
#

cert_body_example = {
    "members": [{
        "type": "CertificateAuthorityInfo",
        "certificateDetails": {"base64Data": "", "type": "CertificateDetailV2", "aliasName": ""}
    }],
    "type": "CertificateAuthorityInfoCollection"
}

UPLINK_SET_TYPE = 'uplink-setV4'
US_name = 'fc_uplink'
LI_name = '%s-%s' % (LE1, LIG3)
FC_name = 'FC-SAN-A'

newLicenses = {'licenseType': 'Synergy 8Gb FC Upgrade',
               'license': [{'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
                           {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}],
               'invalidLicense': [{'key': 'YYYY D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]
               }

fc_uplinkset = {
    "type": UPLINK_SET_TYPE,
    "name": US_name,
    "portConfigInfos": [
        {"desiredSpeed": "Auto",
         "location": {"locationEntries": [
             {"value": "Q3:1", "type": "Port"},
             {"value": 3, "type": "Bay"},
             {"value": "ENC:%s" % ENC1, "type": "Enclosure"}]
         }
         }
    ],
    "networkType": "FibreChannel",
    "primaryPortLocation": None,
    "reachability": None,
    "manualLoginRedistributionState": "Supported",
    "logicalInterconnectUri": "EG:%s" % LI_name,
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "networkUris": [],
    "fcNetworkUris": ["FC:%s" % FC_name],
    "fcoeNetworkUris": []
}

storage_volume_templates = [{"name": "boot-private-thin",
                             "description": "",
                             "rootTemplateUri": "SVT:boot-private-thin",
                             "description": "private boot volume template",
                             "properties": {"name": {"title": "Volume name",
                                                     "description": "A volume name between 1 and 100 characters",
                                                     "type": "string",
                                                     "minLength": 1,
                                                     "maxLength": 100,
                                                     "required": True,
                                                     "meta": {"locked": False}
                                                     },
                                            "description": {"title": "Description",
                                                            "description": "A description for the volume",
                                                            "type": "string",
                                                            "minLength": 0,
                                                            "maxLength": 2000,
                                                            "default": "",
                                                            "meta": {"locked": False}
                                                            },
                                            "storagePool": {"title": "Storage Pool",
                                                            "description": "A common provisioning group URI reference",
                                                            "type": "string",
                                                            "required": True,
                                                            "format": "x-uri-reference",
                                                            "meta": {"locked": False,
                                                                     "createOnly": True,
                                                                     "semanticType": "device-storage-pool"},
                                                            "default": "FC_r1"
                                                            },
                                            "size": {"title": "Capacity",
                                                     "description": "The capacity of the volume in bytes",
                                                     "type": "integer",
                                                     "required": True,
                                                     "minimum": 1073741824,
                                                     "maximum": 17592186044416,
                                                     "meta": {"locked": False,
                                                              "semanticType": "capacity"},
                                                     "default": one_gb * 100,
                                                     },
                                            "isShareable": {"title": "Is Shareable",
                                                            "description": "The shareability of the volume",
                                                            "type": "boolean",
                                                            "meta": {"locked": False},
                                                            "default": False,
                                                            },
                                            "provisioningType": {"title": "Provisioning Type",
                                                                 "description": "The provisioning type for the volume",
                                                                 "type": "string",
                                                                 "enum": ["Thin", "Full"],
                                                                 "meta": {"locked": True,
                                                                          "createOnly": True},
                                                                 "default": "Thin"
                                                                 },
                                            "snapshotPool": {"title": "Snapshot Pool",
                                                             "description": "A URI reference to the common provisioning group used to create snapshots",
                                                             "type": "string",
                                                             "format": "x-uri-reference",
                                                             "meta": {"locked": True,
                                                                      "semanticType": "device-snapshot-storage-pool"},
                                                             "default": "FC_r1"
                                                             }
                                            }
                             },
                            {"name": "shared-thin",
                             "description": "",
                             "rootTemplateUri": "SVT:shared-thin",
                             "description": "shared thin volume template",
                             "properties": {"name": {"title": "Volume name",
                                                     "description": "A volume name between 1 and 100 characters",
                                                     "type": "string",
                                                     "minLength": 1,
                                                     "maxLength": 100,
                                                     "required": True,
                                                     "meta": {"locked": False}
                                                     },
                                            "description": {"title": "Description",
                                                            "description": "A description for the volume",
                                                            "type": "string",
                                                            "minLength": 0,
                                                            "maxLength": 2000,
                                                            "default": "",
                                                            "meta": {"locked": False}
                                                            },
                                            "storagePool": {"title": "Storage Pool",
                                                            "description": "A common provisioning group URI reference",
                                                            "type": "string",
                                                            "required": True,
                                                            "format": "x-uri-reference",
                                                            "meta": {"locked": False,
                                                                     "createOnly": True,
                                                                     "semanticType": "device-storage-pool"},
                                                            "default": "FC_r5"
                                                            },
                                            "size": {"title": "Capacity",
                                                     "description": "The capacity of the volume in bytes",
                                                     "type": "integer",
                                                     "required": True,
                                                     "minimum": 1073741824,
                                                     "maximum": 17592186044416,
                                                     "meta": {"locked": False,
                                                              "semanticType": "capacity"},
                                                     "default": one_gb * 50,
                                                     },
                                            "isShareable": {"title": "Is Shareable",
                                                            "description": "The shareability of the volume",
                                                            "type": "boolean",
                                                            "meta": {"locked": False},
                                                            "default": True,
                                                            },
                                            "provisioningType": {"title": "Provisioning Type",
                                                                 "description": "The provisioning type for the volume",
                                                                 "type": "string",
                                                                 "enum": ["Thin", "Full"],
                                                                 "meta": {"locked": True,
                                                                          "createOnly": True},
                                                                 "default": "Thin"
                                                                 },
                                            "snapshotPool": {"title": "Snapshot Pool",
                                                             "description": "A URI reference to the common provisioning group used to create snapshots",
                                                             "type": "string",
                                                             "format": "x-uri-reference",
                                                             "meta": {"locked": True,
                                                                      "semanticType": "device-snapshot-storage-pool"},
                                                             "default": "FC_r5"
                                                             }
                                            }
                             },
                            {'name': 'private-thick',
                             'description': '',
                             'rootTemplateUri': 'SVT:private-thick',
                             'description': 'private thick volume template',
                             'properties': {'name': {'title': 'Volume name',
                                                     'description': 'A volume name between 1 and 100 characters',
                                                     'type': 'string',
                                                     'minLength': 1,
                                                     'maxLength': 100,
                                                     'required': True,
                                                     'meta': {'locked': False}
                                                     },
                                            'description': {'title': 'Description',
                                                            'description': 'A description for the volume',
                                                            'type': 'string',
                                                            'minLength': 0,
                                                            'maxLength': 2000,
                                                            'default': '',
                                                            'meta': {'locked': False}
                                                            },
                                            'storagePool': {'title': 'Storage Pool',
                                                            'description': 'A common provisioning group URI reference',
                                                            'type': 'string',
                                                            'required': True,
                                                            'format': 'x-uri-reference',
                                                            'meta': {'locked': False,
                                                                     'createOnly': True,
                                                                     'semanticType': 'device-storage-pool'},
                                                            'default': 'FC_r5'
                                                            },
                                            'size': {'title': 'Capacity',
                                                     'description': 'The capacity of the volume in bytes',
                                                     'type': 'integer',
                                                     'required': True,
                                                     'minimum': 1073741824,
                                                     'maximum': 17592186044416,
                                                     'meta': {'locked': False,
                                                              'semanticType': 'capacity'},
                                                     'default': one_gb * 50,
                                                     },
                                            'isShareable': {'title': 'Is Shareable',
                                                            'description': 'The shareability of the volume',
                                                            'type': 'boolean',
                                                            'meta': {'locked': False},
                                                            'default': False,
                                                            },
                                            'provisioningType': {'title': 'Provisioning Type',
                                                                 'description': 'The provisioning type for the volume',
                                                                 'type': 'string',
                                                                 'enum': ['Thin', 'Full'],
                                                                 'meta': {'locked': True,
                                                                          'createOnly': True},
                                                                 'default': 'Full'
                                                                 },
                                            'snapshotPool': {'title': 'Snapshot Pool',
                                                             'description': 'A URI reference to the common provisioning group used to create snapshots',
                                                             'type': 'string',
                                                             'format': 'x-uri-reference',
                                                             'meta': {'locked': True,
                                                                      'semanticType': 'device-snapshot-storage-pool'},
                                                             'default': 'FC_r5'
                                                             }
                                            }
                             }
                            ]

expected_storage_volume_templates = [{"category": "storage-volume-templates",
                                      "name": "boot-private-thin",
                                      "status": "OK",
                                      "state": "Configured",
                                      "type": "StorageVolumeTemplateV6",
                                      "uri": "SVT:boot-private-thin",
                                      "properties": {"name": {"title": "Volume name",
                                                              "description": "A volume name between 1 and 100 characters",
                                                              "type": "string",
                                                              "minLength": 1,
                                                              "maxLength": 100,
                                                              "required": True,
                                                              "meta": {"locked": False}
                                                              },
                                                     "description": {"title": "Description",
                                                                     "description": "A description for the volume",
                                                                     "type": "string",
                                                                     "minLength": 0,
                                                                     "maxLength": 2000,
                                                                     "default": "",
                                                                     "meta": {"locked": False}
                                                                     },
                                                     "storagePool": {"title": "Storage Pool",
                                                                     "description": "A common provisioning group URI reference",
                                                                     "type": "string",
                                                                     "required": True,
                                                                     "format": "x-uri-reference",
                                                                     "meta": {"locked": False,
                                                                              "createOnly": True,
                                                                              "semanticType": "device-storage-pool"},
                                                                     "default": "SPOOL:FC_r1"
                                                                     },
                                                     "size": {"title": "Capacity",
                                                              "description": "The capacity of the volume in bytes",
                                                              "type": "integer",
                                                              "required": True,
                                                              "minimum": 1073741824,
                                                              "maximum": 70368744177664,
                                                              "meta": {"locked": False,
                                                                       "semanticType": "capacity"},
                                                              "default": one_gb * 100,
                                                              },
                                                     "isShareable": {"title": "Is Shareable",
                                                                     "description": "The shareability of the volume",
                                                                     "type": "boolean",
                                                                     "meta": {"locked": False},
                                                                     "default": False,
                                                                     },
                                                     "provisioningType": {"title": "Provisioning Type",
                                                                          "description": "The provisioning type for the volume",
                                                                          "type": "string",
                                                                          "enum": ["Thin", "Full"],
                                                                          "meta": {"locked": True,
                                                                                   "createOnly": True},
                                                                          "default": "Thin"
                                                                          },
                                                     "snapshotPool": {"title": "Snapshot Pool",
                                                                      "description": "A URI reference to the common provisioning group used to create snapshots",
                                                                      "type": "string",
                                                                      "format": "x-uri-reference",
                                                                      "meta": {"locked": True,
                                                                               "semanticType": "device-snapshot-storage-pool"},
                                                                      "default": "SPOOL:FC_r1"
                                                                      }
                                                     }
                                      },
                                     {'category': 'storage-volume-templates',
                                      'name': 'shared-thin',
                                      'status': 'OK',
                                      'state': 'Configured',
                                      'type': 'StorageVolumeTemplateV6',
                                      'uri': 'SVT:shared-thin',
                                      'properties': {'name': {'title': 'Volume name',
                                                              'description': 'A volume name between 1 and 100 characters',
                                                              'type': 'string',
                                                              'minLength': 1,
                                                              'maxLength': 100,
                                                              'required': True,
                                                              'meta': {'locked': False}
                                                              },
                                                     'description': {'title': 'Description',
                                                                     'description': 'A description for the volume',
                                                                     'type': 'string',
                                                                     'minLength': 0,
                                                                     'maxLength': 2000,
                                                                     'default': '',
                                                                     'meta': {'locked': False}
                                                                     },
                                                     'storagePool': {'title': 'Storage Pool',
                                                                     'description': 'A common provisioning group URI reference',
                                                                     'type': 'string',
                                                                     'required': True,
                                                                     'format': 'x-uri-reference',
                                                                     'meta': {'locked': False,
                                                                              'createOnly': True,
                                                                              'semanticType': 'device-storage-pool'},
                                                                     'default': 'SPOOL:FC_r5'
                                                                     },
                                                     'size': {'title': 'Capacity',
                                                              'description': 'The capacity of the volume in bytes',
                                                              'type': 'integer',
                                                              'required': True,
                                                              'minimum': 1073741824,
                                                              'maximum': 70368744177664,
                                                              'meta': {'locked': False,
                                                                       'semanticType': 'capacity'},
                                                              'default': one_gb * 50,
                                                              },
                                                     'isShareable': {'title': 'Is Shareable',
                                                                     'description': 'The shareability of the volume',
                                                                     'type': 'boolean',
                                                                     'meta': {'locked': False},
                                                                     'default': True,
                                                                     },
                                                     'provisioningType': {'title': 'Provisioning Type',
                                                                          'description': 'The provisioning type for the volume',
                                                                          'type': 'string',
                                                                          'enum': ['Thin', 'Full'],
                                                                          'meta': {'locked': True,
                                                                                   'createOnly': True},
                                                                          'default': 'Thin'
                                                                          },
                                                     'snapshotPool': {'title': 'Snapshot Pool',
                                                                      'description': 'A URI reference to the common provisioning group used to create snapshots',
                                                                      'type': 'string',
                                                                      'format': 'x-uri-reference',
                                                                      'meta': {'locked': True,
                                                                               'semanticType': 'device-snapshot-storage-pool'},
                                                                      'default': 'SPOOL:FC_r5'
                                                                      }
                                                     }
                                      },
                                     {'category': 'storage-volume-templates',
                                      'name': 'private-thick',
                                      'status': 'OK',
                                      'state': 'Configured',
                                      'type': 'StorageVolumeTemplateV6',
                                      'uri': 'SVT:private-thick',
                                      'properties': {'name': {'title': 'Volume name',
                                                              'description': 'A volume name between 1 and 100 characters',
                                                              'type': 'string',
                                                              'minLength': 1,
                                                              'maxLength': 100,
                                                              'required': True,
                                                              'meta': {'locked': False}
                                                              },
                                                     'description': {'title': 'Description',
                                                                     'description': 'A description for the volume',
                                                                     'type': 'string',
                                                                     'minLength': 0,
                                                                     'maxLength': 2000,
                                                                     'default': '',
                                                                     'meta': {'locked': False}
                                                                     },
                                                     'storagePool': {'title': 'Storage Pool',
                                                                     'description': 'A common provisioning group URI reference',
                                                                     'type': 'string',
                                                                     'required': True,
                                                                     'format': 'x-uri-reference',
                                                                     'meta': {'locked': False,
                                                                              'createOnly': True,
                                                                              'semanticType': 'device-storage-pool'},
                                                                     'default': 'SPOOL:FC_r5'
                                                                     },
                                                     'size': {'title': 'Capacity',
                                                              'description': 'The capacity of the volume in bytes',
                                                              'type': 'integer',
                                                              'required': True,
                                                              'minimum': 1073741824,
                                                              'maximum': 70368744177664,
                                                              'meta': {'locked': False,
                                                                       'semanticType': 'capacity'},
                                                              'default': one_gb * 50,
                                                              },
                                                     'isShareable': {'title': 'Is Shareable',
                                                                     'description': 'The shareability of the volume',
                                                                     'type': 'boolean',
                                                                     'meta': {'locked': False},
                                                                     'default': False,
                                                                     },
                                                     'provisioningType': {'title': 'Provisioning Type',
                                                                          'description': 'The provisioning type for the volume',
                                                                          'type': 'string',
                                                                          'enum': ['Thin', 'Full'],
                                                                          'meta': {'locked': True,
                                                                                   'createOnly': True},
                                                                          'default': 'Full'
                                                                          },
                                                     'snapshotPool': {'title': 'Snapshot Pool',
                                                                      'description': 'A URI reference to the common provisioning group used to create snapshots',
                                                                      'type': 'string',
                                                                      'format': 'x-uri-reference',
                                                                      'meta': {'locked': True,
                                                                               'semanticType': 'device-snapshot-storage-pool'},
                                                                      'default': 'SPOOL:FC_r5'
                                                                      }
                                                     }
                                      }
                                     ]

health_desired = {'enclosures': 'OK',
                  'les': 'OK',
                  'servers': 'OK',
                  'drive_enclosures': 'OK',
                  'interconnects': 'OK',
                  'sas_interconnects': 'OK',
                  'lis': 'OK',
                  'sas_lis': 'OK',
                  'san_managers': 'OK',
                  'storage_systems': 'OK',
                  'storage_volumes': 'OK',
                  'server_profiles': 'OK'
                  }

state_desired = {'enclosures': 'Configured',
                 'les': 'Consistent',
                 'servers': 'ProfileApplied',
                 'drive_enclosures': 'Configured',
                 'interconnects': 'Configured',
                 'sas_interconnects': 'Configured',
                 'lis': 'Unknown',
                 'sas_lis': 'Redundant',
                 'san_managers': 'Managed',
                 'storage_systems': 'Managed',
                 'storage_volumes': 'Managed',
                 'server_profiles': 'Normal'
                 }

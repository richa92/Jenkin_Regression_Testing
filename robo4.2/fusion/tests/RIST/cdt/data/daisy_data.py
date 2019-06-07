"""Data file for Performance Test - Daisy."""
from copy import deepcopy
import json

from common_data import *


def rlist(start, end, prefix='Net_', suffix='', step=1):
    """Creates and returns the list with prefix and suffix added to range of values from start to end."""
    return ['%s%s%s' % (prefix, str(x), suffix)
            for x in xrange(start, end + 1, step)]


def us(**kwargs):
    """ Creates and returns uplink set dto dict with data populated from kwargs."""
    return {'name': kwargs.get('name', None),
            'ethernetNetworkType': kwargs.get('ethernetNetworkType', 'Tagged'),
            'networkType': 'Ethernet',
            'networkUris': kwargs.get('networkUris', None),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': kwargs.get('logicalPortConfigInfos', None)}


def lig(**kwargs):
    """Creates and returns lig dto from kwargs."""
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

APPLIANCE_IP = '16.114.208.62'  # daisy-ov.vse.rdlabs.hpecorp.net
HOSTNAME = 'daisy-ov.vse.rdlabs.hpecorp.net'
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'
FUSION_PROMPT = 'root'
FUSION_TIMEOUT = 35
ssh_server_ip = '15.114.112.61'  # Used in appliance_certificates1.txt

SSH_USER = 'root'
SSH_PASS = 'hpvse1'
interface = 'bond0'
one_gb = 1073741824

NUVO_VOL = '/home/testNuvo/daisy:/client_mnt'

EG1 = '3enc'
LE1 = 'LE1'

LIG1 = 'SASLIG1'
LIG2 = 'CarbonLIG1'
LIG3 = 'PotashLIG'
LIG4 = 'SASLIG2'
LIG5 = 'SASLIG3'
LIG6 = 'CarbonLIG2'
LIG7 = 'CarbonLIG3'

ENC1 = 'CN754404R9'
ENC2 = 'CN754406WS'
ENC3 = 'MXQ7100868'

ENCS = [ENC1, ENC2, ENC3]

bays_480 = [3, 4, 7, 8, 9, 10]
bays_660 = [5, 6]


LI = {'name': 'LE1-PotashLIG'}

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

OVF5956_APPMETRICS = ['node_exporter', 'pgbouncer_exporter', 'postgres_exporter', 'oneview_log_count_exporter', 'apache_exporter', 'oneview_task_exporter', 'jetty_app_metrics']

appliance = {'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
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
               'hostname': HOSTNAME,
               'confOneNode': True,
               'domainName': 'vse.rdlabs.hpecorp.net',
               'aliasDisabled': True,
               }],
             }

CIM_HOSTS = {"active": "16.114.208.60",
             "standby": "16.114.208.61"
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
      {'name': 'iSCSI_283',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': 283,
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
       'vlanId': int(n[4:])} for n in rlist(100, 282)]

e3 = [{'name': n,
       'type': ETHERNET_NETWORK_TYPE,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(284, 2100)]

ethernet_networks = e1 + e2 + e3

network_sets = [{'name': 'NetSet1', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(101, 161),
                 'nativeNetworkUri': None},
                {'name': 'NetSet2', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(162, 222),
                 'nativeNetworkUri': None},
                {'name': 'NetSet3', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(223, 282),
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
        'networkUris': rlist(100, 282) + rlist(284, 2100),
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
}


Ethernet_Tagged_new = {
    'name': 'Ethernet-Tagged', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
    'networkUris': ['Net_2200'],
    'mode': 'Auto',
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
        {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'}
    ]
}

network_sets_update_add = [{'name': 'NetSet4', 'add_networkUris': ['Net_2200']}]

Net_2200 = [{
    "name": "Net_2200",
    "type": "ETHERNET_NETWORK_TYPE",
    "vlanId": 2200,
    "connectionTemplateUri": None,
    "privateNetwork": False,
    "smartLink": True,
    "purpose": "General",
    "ethernetNetworkType": "Tagged"
}
]

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

PotashLIG = ligs['PotashLIG']

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

# StRM
# StoreServ
STORESERV_NAME = 'wpst3par-mini1-srv'
STORESERV_HOSTNAME = 'wpst3par-mini1-srv.vse.rdlabs.hpecorp.net'
STORESERV_POOL1 = 'FC_r1'
STORESERV_POOL2 = 'FC_r5'

"""
Server Profile Templates
"""
sht_480_1 = 'SY 480 Gen9 1'
sht_480_2 = 'SY 480 Gen10 1'
sht_660_1 = 'SY 660 Gen9 1'
sht_660_2 = 'SY 660 Gen10 1'

sp_conns_1 = [{"id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-A", "lagName": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-B", "lagName": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 3, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 4, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "NS:NetSet6", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet7", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet8", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 7, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 8, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "NS:NetSet6", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 9, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet7", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 10, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet8", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              ]

sp_conns_2 = [
    {"id": 1, "name": "FC-SAN-A", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-A", "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 2, "name": "FC-SAN-B", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-B", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 3, "name": "MGMT_INTERFACE_NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 4, "name": "MGMT_INTERFACE_REDUNDANT_NET_100", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 5, "name": "NETSET_5", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "NS:NetSet5", "lagName": None, },
    {"id": 6, "name": "NETSET_5_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "NS:NetSet5", "lagName": None, },
    {"id": 7, "name": "NETSET_6", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet6", "lagName": None, },
    {"id": 8, "name": "NETSET_6_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet6", "lagName": None, },
    {"id": 9, "name": "NETSET_7", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet7", "lagName": None, },
    {"id": 10, "name": "NETSET_7_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet7", "lagName": None, },
]

sp_conns_3 = [
    {"id": 1, "name": "MGMT_INTERFACE_NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 2, "name": "NET_400", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "ETH:Net_400", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
]

sp_conns_4 = [
    {"id": 1, "name": "MGMT_INTERFACE_NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 2, "name": "FCOE_SideA_conn", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "FCOE:FCOE-SideA-3201", "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 3, "name": "Untagged1_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "ETH:Untagged1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 4, "name": "NetSet1_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 5, "name": "MGMT_INTERFACE_NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 6, "name": "FCOE_SideB_conn", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "FCOE:FCOE-SideB-3202", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 7, "name": "Untagged1_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "ETH:Untagged1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 8, "name": "NetSet1_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
]

sp_conns_5 = [
    {"id": 1, "name": "FC-SAN-A", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-A", "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 2, "name": "FC-SAN-B", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-B", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 3, "name": "MGMT_INTERFACE_NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 4, "name": "NetSet3_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 5, "name": "NetSet4_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet4", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 6, "name": "NetSet5_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet5", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 7, "name": "MGMT_INTERFACE_NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 8, "name": "NetSet3_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 9, "name": "NetSet4_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet4", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 10, "name": "NetSet5_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet5", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
]

sp_conns_6 = [
    {"id": 1, "name": "MGMT_INTERFACE_NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 2, "name": "FCOE_SideA_conn", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "FCOE:FCOE-SideA-3201", "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 3, "name": "NetSet8_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet8", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 4, "name": "NetSet1_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 5, "name": "MGMT_INTERFACE_NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, },
    {"id": 6, "name": "FCOE_SideB_conn", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "FCOE:FCOE-SideB-3202", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
    {"id": 7, "name": "NetSet8_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet8", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 8, "name": "NetSet1_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
]

sp_conns_7 = [{"id": 1, "name": "Net_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 2, "name": "NetSet2_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 3, "name": "NetSet3_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 4, "name": "NetSet4_conn", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet4", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 5, "name": "Net_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 6, "name": "NetSet2_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 7, "name": "NetSet3_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 8, "name": "NetSet4_conn_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet4", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
              ]

spts = {'SPT_480_1': {'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 480 Gen9 1',
                      'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
                      'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                      'macType': 'Physical', 'wwnType': 'Physical', 'name': 'BB_SPT1',
                      'description': 'Server Profile Template created from SY 480 Gen10 1', 'affinity': 'Bay',
                      'connectionSettings': {'connections': deepcopy(sp_conns_7), 'manageConnections': True},
                      'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
                      'boot': {'manageBoot': True, 'order': ['HardDisk']},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                                   'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'localStorage': {'controllers': [{"logicalDrives": [{"name": None,
                                                                           "raidLevel": "RAID0",
                                                                           "bootable": True,
                                                                           "numPhysicalDrives": None,
                                                                           "driveTechnology": None,
                                                                           "sasLogicalJBODId": 1,
                                                                           "accelerator": "Unmanaged",
                                                                           "numSpareDrives": None
                                                                           }],
                                                        "deviceSlot": "Mezz 1",
                                                        "mode": "Mixed",
                                                        "initialize": False
                                                        }],
                                       'sasLogicalJBODs': [{"id": 1,
                                                            "deviceSlot": "Mezz 1",
                                                            "name": "jbod1",
                                                            "numPhysicalDrives": 20,
                                                            "driveMinSizeGB": 146,
                                                            "driveMaxSizeGB": 300,
                                                            "driveTechnology": "SasHdd",
                                                            "eraseData": False}
                                                           ]},
                      }, }
#         'SPT_660_3': {'type': 'ServerProfileTemplateV5', 'serverProfileDescription': 'Server profile for SY 660 Gen9 1',
#                       'serverHardwareTypeUri': 'SHT:%s' % sht_660_1,
#                       'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
#                       'macType': 'Physical', 'wwnType': 'Physical', 'name': 'SPT_660_3',
#                       'description': 'Server Profile Template created from SY 660 Gen9 1', 'affinity': 'Bay',
#                       'connectionSettings': {'connections': deepcopy(sp_conns_7), 'manageConnections': True},
#                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
#                       'boot': {'manageBoot': True, 'order': ['HardDisk']},
#                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
#                                    'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
#                       'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
#                       'iscsiInitiatorNameType': 'AutoGenerated',
#                       'localStorage': {'controllers': [{"logicalDrives": [{"name": None,
#                                                                            "raidLevel": "RAID5",
#                                                                            "bootable": True,
#                                                                            "numPhysicalDrives": None,
#                                                                            "driveTechnology": None,
#                                                                            "sasLogicalJBODId": 1,
#                                                                            "accelerator": "Unmanaged"},
#                                                                           {"name": None,
#                                                                            "raidLevel": "RAID1",
#                                                                            "bootable": False,
#                                                                            "numPhysicalDrives": None,
#                                                                            "driveTechnology": None,
#                                                                            "sasLogicalJBODId": 2,
#                                                                            "accelerator": "Unmanaged"}],
#                                                         "deviceSlot": "Mezz 1",
#                                                         "mode": "RAID",
#                                                         "initialize": False
#                                                         }],
#                                        'sasLogicalJBODs': [{"id": 1,
#                                                             "deviceSlot": "Mezz 1",
#                                                             "name": "ld_660_3_1",
#                                                             "numPhysicalDrives": 3,
#                                                             "driveMinSizeGB": 300,
#                                                             "driveMaxSizeGB": 300,
#                                                             "driveTechnology": "SasHdd",
#                                                             "eraseData": False},
#                                                            {"id": 2,
#                                                             "deviceSlot": "Mezz 1",
#                                                             "name": "ld_660_3_2",
#                                                             "numPhysicalDrives": 2,
#                                                             "driveMinSizeGB": 300,
#                                                             "driveMaxSizeGB": 300,
#                                                             "driveTechnology": "SasHdd",
#                                                             "eraseData": False
#                                                             }]},
#                       },
#         }

"""
Used to create a dict of profile names to create
from the profile templates
"""
# sp_from_spts = dict(
#     {'P2_480_1' % (ENC1, 3): 'SPT_480_1',
#      'P6_660_3' % (ENC2, 5): 'SPT_660_3'
#      }
# )

"""
Used to assign the unassigned profiles to physical hardware enc-bay
"""
# unassigned_sp_to_bay_map = dict(
#     {'P2_480_1' % (ENC1, 3): '%s, bay %i' % (ENC1, 3),
#      'P6_660_3' % (ENC2, 5): '%s, bay %i' % (ENC2, 5)
#      }
# )

"""
Used to power off blades when creating assigned profiles.
This is the initial assignment for each profiles to sever bay.
Profiles may be reassigned to new bays at run time.
"""
# Profile 1  CN754404R9, Bay 7
# Profile 2  CN754404R9, Bay 3
# Profile 3  CN754404R9, Bay 4
# Profile 4  CN754404R9, Bay 8
# Profile 5  CN754406WS, Bay 3
# Profile 6  CN754406WS, Bay 5
# Profile 7  MXQ7100868, Bay 6
# Profile 8  MXQ7100868, Bay 3
# Profile 9  MXQ7100868, Bay 4
# Profile 10  CN754406WS, Bay 7
# Profile 11  CN754406WS, Bay 8
# Profile 12  CN754406WS, Bay 9
# Profile 13  CN754404R9, Bay 5
# Profile 14  CN754406WS, Bay 4
# Profile 15  CN754404R9, Bay 6
# Profile 16  CN754404R9, Bay 9
# Profile 17  CN754404R9, Bay 10
# Profile 18  CN754406WS, Bay 10
# Profile 19  MXQ7100868, Bay 5
# Profile 20  MXQ7100868, Bay 9
# Profile 21  MXQ7100868, Bay 10
# Profile 22  CN754406WS, Bay 6
# Profile 23  MXQ7100868, Bay 7
# Profile 24  MXQ7100868, Bay 8

assigned_sp_to_bay_map = dict(
    {
        'P1_480_MID:Baseline_Gen9': '%s, bay %i' % (ENC1, 7),
        'P2_480_MID:Bigbird_Gen9': '%s, bay %i' % (ENC1, 3),
        'P3_480_MID:BootFromSD_Gen9': '%s, bay %i' % (ENC1, 4),
        'P4_480_MID:BFSCarbon_Gen9': '%s, bay %i' % (ENC1, 8),
        'P5_480_MID:BootFromSD_Gen10': '%s, bay %i' % (ENC3, 11),
        'P6_480_MID:Bigbird_Gen10': '%s, bay %i' % (ENC2, 11),
        'P7_480_MID:BFSCarbon_Gen10': '%s, bay %i' % (ENC3, 6),
        'P8_480_MID:LocalDrive_Gen10': '%s, bay %i' % (ENC3, 3),
        'P9_480_MID:LocalDrive_Gen10': '%s, bay %i' % (ENC3, 4),
        'P10_480_MID:Bigbird_Gen10': '%s, bay %i' % (ENC2, 8),
        'P11_480_MID:Bigbird_Gen10': '%s, bay %i' % (ENC2, 7),
        'P12_480_MID:Bigbird_Gen10': '%s, bay %i' % (ENC2, 9),
        'P13_660_MID:LocalDrive_Gen9': '%s, bay %i' % (ENC1, 5),
        'P14_480_MID:LocalDrive_Gen10': '%s, bay %i' % (ENC3, 12),
        'P15_660_MID:BFSCarbon_Gen9': '%s, bay %i' % (ENC1, 6),
        'P16_480_MID:BFSFCoE_Gen9': '%s, bay %i' % (ENC1, 9),
        'P17_480_MID:BFSCarbon_Gen9': '%s, bay %i' % (ENC1, 10),
        'P18_480_MID:Bigbird_Gen10': '%s, bay %i' % (ENC2, 10),
        'P19_480_MID:BFSFCoE_Gen10': '%s, bay %i' % (ENC3, 5),
        'P20_480_MID:BFSFCoE_Gen10': '%s, bay %i' % (ENC3, 9),
        'P21_480_MID:BFSFCoE_Gen10': '%s, bay %i' % (ENC3, 10),
        'P22_480_MID:Bigbird_Gen10': '%s, bay %i' % (ENC2, 12),
        'P23_480_MID:BFSISCSI_Gen10': '%s, bay %i' % (ENC3, 7),
        'P24_480_MID:BFSISCSI_Gen10': '%s, bay %i' % (ENC3, 8),
    }
)

assigned_sps = [
    {  # Profile 1 : Encl 1, Bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P1_480_MID:Baseline_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 7),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
        'enclosureGroupUri': 'EG:3enc',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_3),
        },
        'boot': {
            'manageBoot': True,
            'order': [
                'HardDisk'
            ]
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'pxeBootPolicy': 'Auto'
        },
    },  # Profile 1  CN754404R9, Bay 7`

    {  # Profile 2 : Encl 1, bay 3 Added newly
        'type': SERVER_PROFILE_TYPE,
        'name': 'P2_480_MID:Bigbird_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 3),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Virtual',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P2',
                'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_conns_7),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'boot': {
            'manageBoot': True,
            'order': ['HardDisk']
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings":
                [{"id": "IntelPerfMonitoring", "value": "Enabled"}]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [{"name": None,
                                                "raidLevel": "RAID1",
                                                "bootable": True,
                                                "numPhysicalDrives": None,
                                                "driveTechnology": None,
                                                "sasLogicalJBODId": 1,
                                                "accelerator": "Unmanaged"},
                                               {"name": None,
                                                "raidLevel": "RAID0",
                                                "bootable": False,
                                                "numPhysicalDrives": None,
                                                "driveTechnology": None,
                                                "sasLogicalJBODId": 2,
                                                "accelerator": "Unmanaged"}],
                             "deviceSlot": "Mezz 1",
                             "mode": "RAID",
                             "initialize": False
                             }],
            'sasLogicalJBODs': [{"id": 1,
                                 "deviceSlot": "Mezz 1",
                                 "name": "jbod1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False},
                                {"id": 2,
                                 "deviceSlot": "Mezz 1",
                                 "name": "jbod2",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False
                                 }]},

    },  # Profile 2  CN754404R9, Bay 3

    {  # Profile 3 : Encl 1, Bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P3_480_MID:BootFromSD_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 4),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Virtual',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile Template created from SY 480 Gen9 1',
        'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_1)},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto',
                     'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['SD']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        # TODO: Import logical storage instead of creating a new one.
        'localStorage': {'controllers': [],
                         'sasLogicalJBODs': []},
        'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                       'volumeAttachments': [{'id': 1,
                                              "volumeUri": "SVOL:P3_data_volume",
                                              'lunType': 'Auto',
                                              "lun": None,
                                              # "bootVolumePriority": "NotBootable",
                                              'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                'targetSelector': 'Auto', 'targets': []},
                                                               {'isEnabled': True, 'connectionId': 2,
                                                                'targetSelector': 'Auto', 'targets': []}]
                                              }]}
    },  # Profile 3  CN754404R9, Bay 4

    {  # Profile 4 : Encl 1, Bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P4_480_MID:BFSCarbon_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 8),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_2),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P4_boot_volume',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': 'VolName:P4_data_volume',
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["CD", "USB", "HardDisk", "PXE"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'BIOS',
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 4  CN754404R9, Bay 8

    {  # Profile 5 : Encl 3, bay 11
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 11),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'P5_480_MID:BootFromSD_Gen10',
        'description': 'Server Profile Template created from SY 480 Gen10 1',
        'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_1)},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['SD']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {'controllers': [],
                         'sasLogicalJBODs': []},
        'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                       'volumeAttachments': [{'id': 1,
                                              "volumeUri": "SVOL:SPT_480_7_data_volume",
                                              'lunType': 'Auto',
                                              "lun": None,
                                              # "bootVolumePriority": "NotBootable",
                                              'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                'targetSelector': 'Auto', 'targets': []},
                                                               {'isEnabled': True, 'connectionId': 2,
                                                                'targetSelector': 'Auto', 'targets': []}]
                                              }]}
    },  # Profile 5  CN754406WS, Bay 3

    {  # Profile 6 : Encl 2, bay 11 Added newly
        'type': SERVER_PROFILE_TYPE,
        'name': 'P6_480_MID:Bigbird_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 11),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': 'Server Profile P6',
        'affinity': 'Bay',
        'bios': {
            'manageBios': True,
            "overriddenSettings":
                [{"id": "IntelPerfMonitoring", "value": "Enabled"}]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
    },  # Profile 6  CN754406WS, Bay 5

    {  # Profile 7 : Encl 3, Bay 6
        'type': SERVER_PROFILE_TYPE,
        'name': 'P7_480_MID:BFSCarbon_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 6),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_2),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P7_boot_volume',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': 'VolName:P7_data_volume',
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 7  MXQ7100868, Bay 6

    {  # Profile 8 : Encl 3, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P8_480_MID:LocalDrive_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 3),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P8',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_conns_7),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'BIOS',
            'secureBoot': 'Unmanaged'
        },
        'boot': {
            'manageBoot': True,
            'order': ['HardDisk']
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None,
            'firmwareActivationType': 'Immediate'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings":
                [{"id": "IntelPerfMonitoring", "value": "Enabled"}]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{'deviceSlot': 'Embedded', 'initialize': False, 'mode': 'Mixed',
                             'logicalDrives': [], "importConfiguration": True},
                            {"logicalDrives": [{"name": None,
                                                "raidLevel": "RAID0",
                                                "bootable": False,
                                                "numPhysicalDrives": None,
                                                "driveTechnology": None,
                                                "sasLogicalJBODId": 1,
                                                "accelerator": "Unmanaged"}],
                             "deviceSlot": "Mezz 1",
                             "mode": "Mixed",
                             "initialize": False
                             }],
            'sasLogicalJBODs': [{"id": 1,
                                 "deviceSlot": "Mezz 1",
                                 "name": "jbod1",
                                 "numPhysicalDrives": 1,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False
                                 }]},
    },  # Profile 8  MXQ7100868, Bay 3

    {  # Profile 9 : Encl 3, Bay 4
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 4),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical', 'wwnType': 'Physical', 'name': 'P9_480_MID:LocalDrive_Gen10',
        'description': 'Server Profile created from SY 480 Gen9 1', 'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_1)},
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto',
                     'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {'controllers': [{'deviceSlot': 'Embedded', 'initialize': False, 'mode': 'Mixed',
                                          'logicalDrives': [], "importConfiguration": True}],
                         'sasLogicalJBODs': []},
        'sanStorage': {'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                       'volumeAttachments': [{'id': 1,
                                              "volumeUri": "SVOL:P9_data_volume",
                                              'lunType': 'Auto',
                                              "lun": None,
                                              'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                'targetSelector': 'Auto', 'targets': []},
                                                               {'isEnabled': True, 'connectionId': 2,
                                                                'targetSelector': 'Auto', 'targets': []}]
                                              }]}
    },  # Profile 9  MXQ7100868, Bay 4

    {  # Profile 10 : Encl 2, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P10_480_MID:Bigbird_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 8),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': 'Server Profile P10',
        'affinity': 'Bay',
        'bios': {'manageBios': True,
                 "overriddenSettings":
                     [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
    },  # Profile 10  CN754406WS, Bay 7

    {  # Profile 11 : Encl 2, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P11_480_MID:Bigbird_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 7),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': 'Server Profile P11',
        'affinity': 'Bay',
        'bios': {
            'manageBios': True,
            "overriddenSettings":
                [{"id": "IntelPerfMonitoring", "value": "Enabled"}]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
    },  # Profile 11  CN754406WS, Bay 8

    {  # Profile 12 : Encl 2, Bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P12_480_MID:Bigbird_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 9),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': '',
        'affinity': 'Bay',
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 12  CN754406WS, Bay 9

    {  # Profile 13 : Encl 1, Bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P13_660_MID:LocalDrive_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 5),
        'serverHardwareTypeUri': 'SHT:%s' % sht_660_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': [

                {"id": 1, "name": "NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 2, "name": "NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {
                    "id": 3,
                    "name": "iSCSI_283",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    # "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume",},
                    # "ipv4":{"ipAddressSource":"UserDefined","subnetMask":"255.255.240.0","gateway":"16.114.208.1","ipAddress":"16.114.217.150"},
                },
                {
                    "id": 4,
                    "name": "iSCSI_283_REDUNDANT",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    # "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume",},
                    # "ipv4":{"ipAddressSource":"UserDefined","subnetMask":"255.255.240.0","gateway":"16.114.208.1","ipAddress":"16.114.217.151"},
                },

                {"id": 5, "name": "NETSET2", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 6, "name": "NETSET2_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 7, "name": "NETSET3", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 8, "name": "NETSET3_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},

            ],
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 3,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                    "volume": {
                        "properties": {
                            "name": "P13_data_volume",
                            "description": "",
                            "size": 1073741824,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "dataProtectionLevel": "NetworkRaid0None",
                            "storagePool": "SP:" + STOREVIRTUAL_NAME
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STOREVIRTUAL_NAME,
                    },
                },
            ],
            "sanSystemCredentials": [
                {
                    "storageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                    "chapLevel": "None"
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 13  CN754404R9, Bay 5

    {  # Profile 14 : Encl 3, Bay 12
        'type': SERVER_PROFILE_TYPE,
        'name': 'P14_480_MID:LocalDrive_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 12),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': [

                {"id": 1, "name": "NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 2, "name": "NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},

                {
                    "id": 3,
                    "name": "iSCSI_283",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    # "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume",},
                    # "ipv4":{"ipAddressSource":"UserDefined","subnetMask":"255.255.240.0","gateway":"16.114.208.1","ipAddress":"16.114.217.153"},
                },
                {
                    "id": 4,
                    "name": "iSCSI_283_REDUNDANT",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    # "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume",},
                    # "ipv4":{"ipAddressSource":"UserDefined","subnetMask":"255.255.240.0","gateway":"16.114.208.1","ipAddress":"16.114.217.154"},
                },

                {"id": 5, "name": "NETSET2", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 6, "name": "NETSET2_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},

                {"id": 7, "name": "NETSET3", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 8, "name": "NETSET3_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},

            ],
        },
        "localStorage": {'controllers': [{'deviceSlot': 'Embedded', 'initialize': False, 'mode': 'Mixed',
                                          'logicalDrives': [], "importConfiguration": True}],
                         'sasLogicalJBODs': []},
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 3,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                    "volume": {
                        "properties": {
                            "name": "P14_data_volume",
                            "description": "",
                            "size": 1073741824,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "dataProtectionLevel": "NetworkRaid0None",
                            "storagePool": "SP:" + STOREVIRTUAL_NAME
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STOREVIRTUAL_NAME,
                    },
                },
            ],
            "sanSystemCredentials": [
                {
                    "storageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                    "chapLevel": "None"
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 14  CN754406WS, Bay 4

    {  # Profile 15 : Encl 1, Bay 6
        'type': SERVER_PROFILE_TYPE,
        'name': 'P15_660_MID:BFSCarbon_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 6),
        'serverHardwareTypeUri': 'SHT:%s' % sht_660_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_2),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "Primary",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P15_boot_volume",
                            "description": "",
                            "size": 1073741824 * 50,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': 'VolName:P15_data_volume',
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 15  CN754404R9, Bay 6

    {  # Profile 16  CN754404R9, Bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P16_480_MID:BFSFCoE_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 9),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_4),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "Primary",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P16_boot_volume",
                            "description": "",
                            "size": 1073741824 * 30,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': 'VolName:P16_data_volume',
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 16  CN754404R9, Bay 9

    {  # Profile 17  CN754404R9, Bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P17_480_MID:BFSCarbon_Gen9',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 10),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_1,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_5),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P17_boot_volume',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': 'VolName:P17_data_volume',
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 1,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 17  CN754404R9, Bay 10

    {  # Profile 18  CN754406WS, Bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P18_480_MID:Bigbird_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 10),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': '',
        'affinity': 'Bay',
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 18  CN754406WS, Bay 10

    {  # Profile 19  MXQ7100868, Bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P19_480_MID:BFSFCoE_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 5),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_6),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P19_boot_volume',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': 'VolName:P19_data_volume',
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 19  MXQ7100868, Bay 5

    {  # Profile 20  MXQ7100868, Bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P20_480_MID:BFSFCoE_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 9),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_4),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "Primary",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P20_boot_volume",
                            "description": "",
                            "size": 1073741824 * 30,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P20_data_volume",
                            "description": "",
                            "size": 1073741824 * 1,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'BIOS',
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 20  MXQ7100868, Bay 9

    {  # Profile 21  MXQ7100868, Bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P21_480_MID:BFSFCoE_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 10),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_conns_4),
        },
        "sanStorage": {
            "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P21_boot_volume",
                            "description": "",
                            "size": 1073741824 * 30,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },
                {
                    'id': 2,
                    "bootVolumePriority": "NotBootable",
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 2,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 6,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P21_data_volume",
                            "description": "",
                            "size": 1073741824 * 1,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },
            ]
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'pxeBootPolicy': 'Auto',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 21  MXQ7100868, Bay 10

    {  # Profile 22 : Encl 2, Bay 12
        'type': SERVER_PROFILE_TYPE,
        'name': 'P22_480_MID:Bigbird_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 12),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': '',
        'affinity': 'Bay',
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
    },  # Profile 22 : CN754406WS, Bay 6

    {  # Profile 23 : Encl 3, Bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P23_480_MID:BFSISCSI_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 7),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': [
                {"id": 1, "name": "NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 2, "name": "NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {
                    "id": 3,
                    "name": "iSCSI_283",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", },
                    "ipv4": {"ipAddressSource": "UserDefined", "subnetMask": "255.255.240.0", "gateway": "16.114.208.1", "ipAddress": "16.114.217.158"},
                },
                {
                    "id": 4,
                    "name": "iSCSI_283_REDUNDANT",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", },
                    "ipv4": {"ipAddressSource": "UserDefined", "subnetMask": "255.255.240.0", "gateway": "16.114.208.1", "ipAddress": "16.114.217.159"},
                },
                {"id": 5, "name": "NETSET2", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 6, "name": "NETSET2_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 7, "name": "NETSET3", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 8, "name": "NETSET3_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            ],
        },
        "sanStorage": {"hostOSType": "Windows Server 2016",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 3,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P23_iscsi_boot_volume",
                                                                        "description": "",
                                                                        "size": one_gb * 50,
                                                                        "provisioningType": "Thin",
                                                                        "isShareable": False,
                                                                        "dataProtectionLevel": "NetworkRaid0None",
                                                                        "storagePool": "SP:" + STOREVIRTUAL_NAME
                                                                        },
                                                         "isPermanent": False,
                                                         "templateUri": 'ROOT:' + STOREVIRTUAL_NAME,
                                                         },
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 3,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P23_iscsi_data_volume",
                                                                        "description": "",
                                                                        "size": one_gb,
                                                                        "provisioningType": "Thin",
                                                                        "isShareable": False,
                                                                        "dataProtectionLevel": "NetworkRaid0None",
                                                                        "storagePool": "SP:" + STOREVIRTUAL_NAME
                                                                        },
                                                         "isPermanent": False,
                                                         "templateUri": 'ROOT:' + STOREVIRTUAL_NAME,
                                                         },
                                              }],
                       "sanSystemCredentials": [{"storageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                                 "chapLevel": "None"
                                                 },
                                                ]
                       },
        'boot': {'manageBoot': True,
                 "order": ["HardDisk"],
                 },
        'bootMode': {'manageMode': True,
                     'mode': 'BIOS'
                     },
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]
                 },
    },  # Profile 23 : MXQ7100868, Bay 7

    {  # Profile 24 : Encl 3, Bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P24_480_MID:BFSISCSI_Gen10',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 8),
        'serverHardwareTypeUri': 'SHT:%s' % sht_480_2,
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': '',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': [
                {"id": 1, "name": "NET_100", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 2, "name": "NET_100_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {
                    "id": 3,
                    "name": "iSCSI_283",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", },
                    "ipv4": {"ipAddressSource": "UserDefined", "subnetMask": "255.255.240.0", "gateway": "16.114.208.1", "ipAddress": "16.114.217.161"},
                },
                {
                    "id": 4,
                    "name": "iSCSI_283_REDUNDANT",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:iSCSI_283",
                    "lagName": None,
                    "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", },
                    "ipv4": {"ipAddressSource": "UserDefined", "subnetMask": "255.255.240.0", "gateway": "16.114.208.1", "ipAddress": "16.114.217.162"},
                },
                {"id": 5, "name": "NETSET2", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 6, "name": "NETSET2_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:NetSet2", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 7, "name": "NETSET3", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                {"id": 8, "name": "NETSET3_REDUNDANT", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet3", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            ],
        },
        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': "SVOL:P24_boot_volume_iscsi",
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 3,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               {'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 3,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P24_iscsi_data_volume",
                                                                        "description": "",
                                                                        "size": one_gb,
                                                                        "provisioningType": "Thin",
                                                                        "isShareable": False,
                                                                        "dataProtectionLevel": "NetworkRaid0None",
                                                                        "storagePool": "SP:" + STOREVIRTUAL_NAME
                                                                        },
                                                         "isPermanent": False,
                                                         "templateUri": 'ROOT:' + STOREVIRTUAL_NAME,
                                                         },
                                              }],
                       "sanSystemCredentials": [{"storageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                                 "chapLevel": "None"
                                                 },
                                                ]
                       },
        'boot': {'manageBoot': True,
                 "order": ["HardDisk"],
                 },
        'bootMode': {'manageMode': True,
                     'mode': 'UEFIOptimized',
                     'pxeBootPolicy': 'Auto',
                     'secureBoot': 'Unmanaged'
                     },
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}
                                        ]
                 },
    },  # Profile 24 : MXQ7100868, Bay 8
]

# Generic SPP used for Edit SP and other few tests
SPP_WEB_URL = 'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/SPP/Daisy'

# Used for downloading the perl-Module-Pluggable RPM needed in Cent OS 7.x. Key is Cent OS version, Value is url to download RPM
RPM_WEB_URL = {'7': 'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/RPM/Pluggable/centos/7'}
# Name of the server hosting dev mode package needed for RM performance measurement. Dictionary with Key=OV major version and value is host name
dev_pack_host = {'4': 'ci-artifacts02.vse.rdlabs.hpecorp.net', '5': 'ci-artifacts04.vse.rdlabs.hpecorp.net'}

edit_server_profiles_baseline_spp = [
    'P1_480_MID:Baseline_Gen9',
    'P4_480_MID:BFSCarbon_Gen9',
    'P15_660_MID:BFSCarbon_Gen9'
]

firmware_and_os_drivers_mode = dict(
    {
        "manageFirmware": True,
        "forceInstallFirmware": True,
        "firmwareInstallType": "FirmwareAndOSDrivers",
    }
)

edit_server_profiles_BIOS = [
    'P4_480_MID:BFSCarbon_Gen9',
    'P15_660_MID:BFSCarbon_Gen9'
]

edit_server_profiles_Connections = [
    'P4_480_MID:BFSCarbon_Gen9',
    'P15_660_MID:BFSCarbon_Gen9'
]

firmware_only_offline_mode = dict(
    {
        "manageFirmware": True,
        "forceInstallFirmware": True,
        "firmwareInstallType": "FirmwareOnlyOfflineMode",
        # firmwareBaselineUri will be added in payload generation keyword
    }
)

BIOS_settings_add = dict(
    {
        "manageBios": True,
        "overriddenSettings": [
            {
                "id": "CustomPostMessage",
                "value": "test"
            }
        ]
    }
)

P16_edit_SP_volumes_1 = {"sanStorage": {"volumeAttachments": [{'id': int(n),
                                                               'volumeUri': None,
                                                               "lunType": "Auto",
                                                               "lun": None,
                                                               'storagePaths': [{'isEnabled': True,
                                                                                 'connectionId': 2,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []},
                                                                                {'isEnabled': True,
                                                                                 'connectionId': 6,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []
                                                                                 }, ],
                                                               "bootVolumePriority": "NotBootable",
                                                               "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                                                               "volume": {"properties": {"name": n,
                                                                                         "description": "",
                                                                                         "size": 268435456,
                                                                                         "provisioningType": "Thin",
                                                                                         "isShareable": False,
                                                                                         "storagePool": "SP:" + STORESERV_POOL1,
                                                                                         "templateVersion": "2.0",
                                                                                         "isDeduplicated": False,
                                                                                         "isCompressed": False},
                                                                          "templateUri": 'ROOT:' + STORESERV_POOL1,
                                                                          "isPermanent": False,
                                                                          "initialScopeUris": None
                                                                          }} for n in rlist(3, 3, prefix="")]}}

P16_edit_SP_volumes_2 = {"sanStorage": {"volumeAttachments": [{'id': int(n),
                                                               'volumeUri': None,
                                                               "lunType": "Auto",
                                                               "lun": None,
                                                               'storagePaths': [{'isEnabled': True,
                                                                                 'connectionId': 2,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []},
                                                                                {'isEnabled': True,
                                                                                 'connectionId': 6,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []
                                                                                 }, ],
                                                               "bootVolumePriority": "NotBootable",
                                                               "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                                                               "volume": {"properties": {"name": n,
                                                                                         "description": "",
                                                                                         "size": 268435456,
                                                                                         "provisioningType": "Thin",
                                                                                         "isShareable": False,
                                                                                         "storagePool": "SP:" + STORESERV_POOL1,
                                                                                         "templateVersion": "2.0",
                                                                                         "isDeduplicated": False,
                                                                                         "isCompressed": False},
                                                                          "templateUri": 'ROOT:' + STORESERV_POOL1,
                                                                          "isPermanent": False,
                                                                          "initialScopeUris": None
                                                                          }} for n in rlist(4, 94, prefix="")]}}

P16_edit_SP_volumes_3 = {"sanStorage": {"volumeAttachments": [{'id': int(n),
                                                               'volumeUri': None,
                                                               "lunType": "Auto",
                                                               "lun": None,
                                                               'storagePaths': [{'isEnabled': True,
                                                                                 'connectionId': 2,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []},
                                                                                {'isEnabled': True,
                                                                                 'connectionId': 6,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []
                                                                                 }, ],
                                                               "bootVolumePriority": "NotBootable",
                                                               "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                                                               "volume": {"properties": {"name": n,
                                                                                         "description": "",
                                                                                         "size": 268435456,
                                                                                         "provisioningType": "Thin",
                                                                                         "isShareable": False,
                                                                                         "storagePool": "SP:" + STORESERV_POOL1,
                                                                                         "templateVersion": "2.0",
                                                                                         "isDeduplicated": False,
                                                                                         "isCompressed": False},
                                                                          "templateUri": 'ROOT:' + STORESERV_POOL1,
                                                                          "isPermanent": False,
                                                                          "initialScopeUris": None
                                                                          }} for n in rlist(95, 95, prefix="")]}}

P15_edit_SP_volumes_1 = {"sanStorage": {"volumeAttachments": [{'id': int(n),
                                                               'volumeUri': None,
                                                               "lunType": "Auto",
                                                               "lun": None,
                                                               'storagePaths': [{'isEnabled': True,
                                                                                 'connectionId': 1,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []},
                                                                                {'isEnabled': True,
                                                                                 'connectionId': 2,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []
                                                                                 }, ],
                                                               "bootVolumePriority": "NotBootable",
                                                               "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                                                               "volume": {"properties": {"name": n,
                                                                                         "description": "",
                                                                                         "size": 268435456,
                                                                                         "provisioningType": "Thin",
                                                                                         "isShareable": False,
                                                                                         "storagePool": "SP:" + STORESERV_POOL2,
                                                                                         "templateVersion": "2.0",
                                                                                         "isDeduplicated": False,
                                                                                         "isCompressed": False},
                                                                          "templateUri": 'ROOT:' + STORESERV_POOL2,
                                                                          "isPermanent": False,
                                                                          "initialScopeUris": None
                                                                          }} for n in rlist(96, 96, prefix="")]}}

P15_edit_SP_volumes_2 = {"sanStorage": {"volumeAttachments": [{'id': int(n),
                                                               'volumeUri': None,
                                                               "lunType": "Auto",
                                                               "lun": None,
                                                               'storagePaths': [{'isEnabled': True,
                                                                                 'connectionId': 1,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []},
                                                                                {'isEnabled': True,
                                                                                 'connectionId': 2,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []
                                                                                 }, ],
                                                               "bootVolumePriority": "NotBootable",
                                                               "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                                                               "volume": {"properties": {"name": n,
                                                                                         "description": "",
                                                                                         "size": 268435456,
                                                                                         "provisioningType": "Thin",
                                                                                         "isShareable": False,
                                                                                         "storagePool": "SP:" + STORESERV_POOL2,
                                                                                         "templateVersion": "2.0",
                                                                                         "isDeduplicated": False,
                                                                                         "isCompressed": False},
                                                                          "templateUri": 'ROOT:' + STORESERV_POOL2,
                                                                          "isPermanent": False,
                                                                          "initialScopeUris": None
                                                                          }} for n in rlist(97, 187, prefix="")]}}

P15_edit_SP_volumes_3 = {"sanStorage": {"volumeAttachments": [{'id': int(n),
                                                               'volumeUri': None,
                                                               "lunType": "Auto",
                                                               "lun": None,
                                                               'storagePaths': [{'isEnabled': True,
                                                                                 'connectionId': 1,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []},
                                                                                {'isEnabled': True,
                                                                                 'connectionId': 2,
                                                                                 'targetSelector': 'Auto',
                                                                                 'targets': []
                                                                                 }, ],
                                                               "bootVolumePriority": "NotBootable",
                                                               "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                                                               "volume": {"properties": {"name": n,
                                                                                         "description": "",
                                                                                         "size": 268435456,
                                                                                         "provisioningType": "Thin",
                                                                                         "isShareable": False,
                                                                                         "storagePool": "SP:" + STORESERV_POOL2,
                                                                                         "templateVersion": "2.0",
                                                                                         "isDeduplicated": False,
                                                                                         "isCompressed": False},
                                                                          "templateUri": 'ROOT:' + STORESERV_POOL2,
                                                                          "isPermanent": False,
                                                                          "initialScopeUris": None
                                                                          }} for n in rlist(188, 188, prefix="")]}}

P8_edit_SP_volumes_1 = {'controllers': [{"logicalDrives": [[{"name": None,
                                                             "raidLevel": "RAID0",
                                                             "bootable": False,
                                                             "numPhysicalDrives": None,
                                                             "driveTechnology": None,
                                                             "sasLogicalJBODId": int(n),
                                                             "accelerator": "Unmanaged"}for n in rlist(2, 2, prefix="")]],
                                         }],
                        'sasLogicalJBODs': [[{"id": int(n),
                                              "deviceSlot": "Mezz 1",
                                              "name": n,
                                              "numPhysicalDrives": 1,
                                              "driveMinSizeGB": 146,
                                              "driveMaxSizeGB": 300,
                                              "driveTechnology": "SasHdd",
                                              "eraseData": False}for n in rlist(2, 2, prefix="")]]}

P8_edit_SP_volumes_2 = {'controllers': [{"logicalDrives": [[{"name": None,
                                                             "raidLevel": "RAID0",
                                                             "bootable": False,
                                                             "numPhysicalDrives": None,
                                                             "driveTechnology": None,
                                                             "sasLogicalJBODId": int(n),
                                                             "accelerator": "Unmanaged"}for n in rlist(3, 39, prefix="")]],
                                         }],
                        'sasLogicalJBODs': [[{"id": int(n),
                                              "deviceSlot": "Mezz 1",
                                              "name": n,
                                              "numPhysicalDrives": 1,
                                              "driveMinSizeGB": 146,
                                              "driveMaxSizeGB": 300,
                                              "driveTechnology": "SasHdd",
                                              "eraseData": False}for n in rlist(3, 39, prefix="")]]}

P8_edit_SP_volumes_3 = {'controllers': [{"logicalDrives": [[{"name": None,
                                                             "raidLevel": "RAID0",
                                                             "bootable": False,
                                                             "numPhysicalDrives": None,
                                                             "driveTechnology": None,
                                                             "sasLogicalJBODId": int(n),
                                                             "accelerator": "Unmanaged"}for n in rlist(40, 40, prefix="")]],
                                         }],
                        'sasLogicalJBODs': [[{"id": int(n),
                                              "deviceSlot": "Mezz 1",
                                              "name": n,
                                              "numPhysicalDrives": 1,
                                              "driveMinSizeGB": 146,
                                              "driveMaxSizeGB": 300,
                                              "driveTechnology": "SasHdd",
                                              "eraseData": False}for n in rlist(40, 40, prefix="")]]}

edit_server_profiles_san_volumes = [
    ['P16_480_MID:BFSFCoE_Gen9', P16_edit_SP_volumes_1, P16_edit_SP_volumes_2, P16_edit_SP_volumes_3],
    ['P15_660_MID:BFSCarbon_Gen9', P15_edit_SP_volumes_1, P15_edit_SP_volumes_2, P15_edit_SP_volumes_3],
]

edit_server_profiles_local_volumes = [
    ['P8_480_MID:LocalDrive_Gen10', P8_edit_SP_volumes_1, P8_edit_SP_volumes_2, P8_edit_SP_volumes_3],
]

recreate_sp_list = []


def fetch_sp_body(specific_sp, sp_list):
    """Finds and adds matching server profile from data file to the sp_list."""
    for sp in assigned_sps:
        if str(sp['name']) == specific_sp:
            sp_list.append(sp)


Delete_recreate_sp = ['P6_480_MID:Bigbird_Gen10', 'P10_480_MID:Bigbird_Gen10', 'P11_480_MID:Bigbird_Gen10', 'P12_480_MID:Bigbird_Gen10', 'P18_480_MID:Bigbird_Gen10', 'P22_480_MID:Bigbird_Gen10', 'P6_480_MID:Bigbird_Gen10', 'P10_480_MID:Bigbird_Gen10', 'P11_480_MID:Bigbird_Gen10', 'P12_480_MID:Bigbird_Gen10', 'P18_480_MID:Bigbird_Gen10', 'P22_480_MID:Bigbird_Gen10']
for sp_name in Delete_recreate_sp:
    fetch_sp_body(sp_name, recreate_sp_list)

recreate_static_sp_list = []

SP_rotation_exclude_list = ['P3_480_MID:BootFromSD_Gen9', 'P5_480_MID:BootFromSD_Gen10']
for sp_name in SP_rotation_exclude_list:
    fetch_sp_body(sp_name, recreate_static_sp_list)

brocade_network_advisor = {
    "connectionInfo": [
        {'name': 'Type',
            'value': 'Brocade Network Advisor'},
        {"name": "Host",
            "displayName": "Host",
            "required": True,
            "value": "16.114.217.194",
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
     'name': STORESERV_NAME,
     'family': 'StoreServ',
     "hostname": STORESERV_HOSTNAME,
     'credentials': {'username': '3paradm', 'password': '3pardata'},
     "deviceSpecificAttributes":
         {
             "discoveredDomains": ["NO DOMAIN"],
             "managedDomain": "NO DOMAIN",
     },
     },
    {'type': STORAGE_SYSTEM_TYPE,
     'name': STOREVIRTUAL_NAME,
     'family': 'StoreVirtual',
     "hostname": STOREVIRTUAL_HOSTNAME,
     'credentials': {'username': 'admin', 'password': 'hpvse123'},
     "ports":
         [{
             "name": STOREVIRTUAL_HOSTNAME,
             "expectedNetworkUri": "ETH:iSCSI_283",
             "protocolType": "iSCSI",
             "mode": "Managed"
         }],
     },
]

storage_pools = [
    {"storageSystemUri": STORESERV_NAME, "name": STORESERV_POOL1, "isManaged": True},
    {"storageSystemUri": STORESERV_NAME, "name": STORESERV_POOL2, "isManaged": True}
]

"""
New storage volumes to be created
"""

storage_volumes = []

"""
Existing storage volumes to be added
"""

print_pretty = True

all_volume_names = [
    "SPT_480_7_data_volume",
    "P3_data_volume",
    "P4_boot_volume",
    "P4_data_volume",
    "P7_boot_volume",
    "P7_data_volume",
    "P9_data_volume",
    "P12_boot_volume",
    "P12_data_volume",
    "P15_data_volume",
    "P16_data_volume",
    "P17_boot_volume",
    "P17_data_volume",
    "P18_boot_volume",
    "P18_data_volume",
    "P19_boot_volume",
    "P19_data_volume",
    "P24_boot_volume_iscsi",
]

vol_template = {
    "storageSystemUri": STORESERV_NAME,
    "name": "name",
    "deviceVolumeName": "name",
    "isShareable": True,
}

vol_template_iscsi = {
    "storageSystemUri": STOREVIRTUAL_NAME,
    "name": "name",
    "deviceVolumeName": "name",
    "isShareable": True,
}

existing_volumes = []

for volname in all_volume_names:
    if "boot" in volname or "BOOT" in volname:
        isShareable = False
    else:
        isShareable = True

    if "iscsi" in volname or "ISCSI" in volname:
        this_vol = deepcopy(vol_template_iscsi)
    else:
        this_vol = deepcopy(vol_template)
    this_vol['name'] = volname
    this_vol['deviceVolumeName'] = volname
    this_vol['isShareable'] = isShareable

    existing_volumes.append(this_vol)

if print_pretty:
    pretty_existing = json.dumps(existing_volumes, indent=4)
    print pretty_existing

#
# Create sanStorage['volumeAttachments']
#
#
# host_types = {
#     "480_1": "Windows 2012 / WS2012 R2",
#     "660_1": "VMware (ESXi)"
# }
# pools = [STORESERV_POOL1, STORESERV_POOL2]
# bays = bays_480 + bays_660
#
# storage system targets.  Used for Validation not assigned by OneView at this time
# storage_targets = ["20:12:00:02:AC:00:AF:0A",
#                    "21:12:00:02:AC:00:AF:0A",
#                    "20:11:00:02:AC:00:AF:0A",
#                    "21:11:00:02:AC:00:AF:0A"]
#
# STORAGE_TARGETS_REGEXP = "2(0|1):1(1|2):00:02:AC:00:AF:0A"
#
# attach_template = {
#     "isBootVolume": False,
#
#     "storagePaths": [
#         {
#             "targets": [],
#             "targetSelector": "Auto",
#             "connectionId": 1,
#             "isEnabled": True,
#         },
#         {
#             "targets": [],
#             "targetSelector": "Auto",
#             "connectionId": 2,
#             "isEnabled": True,
#         }
#     ],
# can't have both volumeName and volumeUri;  name and bytes for new vol, uri for existing.  Delete appropriately below.
#     "volumeName": "",
#     "volumeProvisionedCapacityBytes": "",
#     "volumeUri": "",
#     "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
#     "volumeStoragePoolUri": "",
#     "lunType": "Auto",
# "id": 0  # increment 1..n
# }
#
# profile_sanStorage = {}
# volume_attachments = []
# id = 0
# for e in ENCS:
#     enc_full_name = e
#     e = e[-2:]
#     for b in bays:
#         if b in bays_660:
#             t = '660_1'
#         else:
#             t = '480_1'
#
#         for p in pools:
#             for s in SHARED:
#                 shared_name = "%s_Shared_%sGb" % (p, s)
# print shared_name, id
#                 id += 1
#                 this_shared = deepcopy(attach_template)
#                 map(this_shared.pop, ['volumeName', 'volumeProvisionedCapacityBytes'])
#                 this_shared['volumeUri'] = 'SVOL:' + shared_name
#                 this_shared['id'] = id
#                 this_shared['volumeStoragePoolUri'] = 'SPOOL:' + shared_name[:5]
#                 volume_attachments.append(this_shared)
# print this_shared
#
#         ov_create_name = "%s_Bay%s_OV_Created_vol" % (e, b)
# print ov_create_name, id
#         id += 1
#         this_create = deepcopy(attach_template)
#         this_create.pop('volumeUri')
#         this_create['volumeStoragePoolUri'] = 'SPOOL:' + STORESERV_POOL2
#         this_create['volumeName'] = ov_create_name
#         this_create['id'] = id
#         this_create['permanent'] = False
#         this_create['volumeProvisionedCapacityBytes'] = str(one_gb * b)
#         this_create['volumeProvisionType'] = 'Thin'
#         this_create['volumeShareable'] = False
#         volume_attachments.append(this_create)
#
#         if b in bays_660:
#             private_name = "%s_Private_%s_Bay%s" % (STORESERV_POOL2, e, b)
#         else:
#             private_name = "%s_Private_%s_Bay%s" % (STORESERV_POOL1, e, b)
# print private_name, id, '\n'
#         id += 1
#         this_private = deepcopy(attach_template)
#         map(this_private.pop, ['volumeName', 'volumeProvisionedCapacityBytes'])
#         this_private['volumeUri'] = 'SVOL:' + private_name
#         this_private['id'] = id
#         this_private['volumeStoragePoolUri'] = 'SPOOL:' + private_name[:5]
#         volume_attachments.append(this_private)
#
# print 'Profile: %s_Bay_%s_%s' % (enc_full_name, b, t)
# print volume_attachments
#
#         os_type = host_types[t]
#         san_storage = {
#             "sanStorage": {"manageSanStorage": True,
#                            "hostOSType": os_type,
#                            "volumeAttachments": volume_attachments}}
#         profile_sanStorage["%s_BAY_%s_%s" % (enc_full_name, b, t)] = san_storage
#
#         volume_attachments = []
#         id = 0
#
# if print_pretty:
#     pretty_sanStorage = json.dumps(profile_sanStorage, indent=4)
#     print pretty_sanStorage

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

# Added for FLT
ENCLOSURES_MGRBays = [{'MXQ7100868': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC2},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC1},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'mgmtPortNeighbor': None,
                                       'status': 'OK'}, ]},
                      {'CN754406WS': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC1},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC3},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'CN754404R9': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC3},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC2},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]}

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

remotesupport_edit = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                      {'op': 'replace', 'path': '/configuration/companyName', 'value': 'HPE'},
                      {'op': 'replace', 'path': '/configuration/marketingOptIn', 'value': True},
                      {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True},
                      {'op': 'add', 'path': '/sites/default',
                       'value': {'name': 'DEFAULT SITE', 'streetAddress1': 'Compaq Center Dr', 'streetAddress2': '', 'city': 'Houston', 'provinceState': 'TX',
                                 'postalCode': '', 'timeZone': 'US/Central', 'countryCode': 'US', 'type': 'Site', 'default': True}},
                      {'op': 'add', 'path': '/contacts',
                       'value': {'contactKey': 'default', 'firstName': 'FFF', 'lastName': 'LLL', 'email': 'fff.ll@hpe.com', 'primaryPhone': '8884442222',
                                 'alternatePhone': '', 'notes': '', 'language': 'en', 'default': True, 'type': 'Contact'}}]

remotesupport_enable = [{'op': 'replace', 'path': '/configuration/enableRemoteSupport', 'value': True},
                        {"op": "replace", "path": "/configuration/autoEnableDevices", "value": True}]
proxy_servers = [
    {"type": "ProxyServerV2",
     "server": "web-proxy.houston.hpecorp.net",
     "port": "8080",
     "username": None,
     "password": None,
     "credUri": None,
     "communicationProtocol": "HTTP"}
]

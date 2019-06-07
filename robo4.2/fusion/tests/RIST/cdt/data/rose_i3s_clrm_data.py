"""Data file for Rose"""
from copy import deepcopy
import os
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


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ov_appliances = ['fe80::1602:ecff:fe45:bc90', 'fe80::1602:ecff:fe45:9cf0']
i3s_appliances = ['fe80::32e1:71ff:fe68:c70', 'fe80::32e1:71ff:fe68:cbf8']
i3s_hardware = ['MXQ71700GN, bay 1', 'MXQ71700GP, bay 2']
enclosures_count = '3'
OV_ACTIVE = 'fe80::1602:ecff:fe45:9cf0'
I3S_Build = 'http://15.119.160.65/tbird-i3s/master/DDImage/SSH/Latest'
OV_Build = 'http://ci-artifacts04.vse.rdlabs.hpecorp.net/Fusion/rel/5.00/DDImage/Composer-SSH/Latest'
platform = os.name
if platform == 'nt':
    path = 'c:/Goldenimage'
else:
    path = '/root/Goldenimage'
GI_LIST = [
    'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/OS%20Images/ImageStreamer/ESX 6.5 U2 image.zip']
THREADNUM = 3
filename = 'ESXi-6.5.0-U1-2017-08-03.zip'
artifact_bundle_locations = ['http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/OS%20Images/artifact_bundles/HPE-ESXi-2018-12-02-v5.0.zip',
                             'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/OS%20Images/artifact_bundles/HPE-ESXi-6.7-2018-11-27-v5.0.zip']

subnets = [{'type': 'Subnet', 'gateway': '10.30.0.1',
            'networkId': '10.30.0.0', 'subnetmask': '255.255.0.0',
            'dnsServers': [], 'domain': None},
           {'type': 'Subnet', 'gateway': '16.114.208.1',
            'networkId': '16.114.208.0', 'subnetmask': '255.255.240.0',
               'dnsServers': None, 'domain': None},
           {'type': 'Subnet', 'gateway': '10.126.0.1',
            'networkId': '10.126.0.0', 'subnetmask': '255.255.255.0',
               'dnsServers': None, 'domain': None},
           {'type': 'Subnet', 'gateway': '10.100.0.1',
            'networkId': '10.100.0.0', 'subnetmask': '255.255.255.0',
               'dnsServers': ['10.100.0.2', '10.100.0.3', '10.100.0.4'], 'domain': 'cdt.lab.fc'}, ]

ranges = [{'type': 'Range', 'networkId': '10.30.0.0',
           "startStopFragments": [{'startAddress': '10.30.0.2', 'endAddress': '10.30.0.151'}],
           'name': 'i3s-deploy', 'subnetUri': ' '},
          {'type': 'Range', 'networkId': '16.114.208.0',
           "startStopFragments": [{'startAddress': '16.114.217.163', 'endAddress': '16.114.217.168'}],
           'name': 'i3s-mgmt', 'subnetUri': ' '},
          {'type': 'Range', 'networkId': '10.126.0.0',
           "startStopFragments": [{'startAddress': '10.126.0.2', 'endAddress': '10.126.0.151'}],
                   'name': 'clrm-vmotion', 'subnetUri': ' '},
          {'type': 'Range', 'networkId': '10.100.0.0',
           "startStopFragments": [{'startAddress': '10.100.0.5', 'endAddress': '10.100.0.50'}],
           'name': 'clrm-mgmt', 'subnetUri': ' '}]

networks = [{'vlanId': '3010', 'networkId': '10.30.0.0',
             'ethernetNetworkType': 'Tagged', 'subnetUri': '',
             'purpose': 'General', 'name': 'Net_3010',
             'smartLink': False, 'privateNetwork': False,
             'connectionTemplateUri': None, 'type': ETHERNET_NETWORK_TYPE},
            {'vlanId': '283', 'networkId': '16.114.208.0',
             'ethernetNetworkType': 'Tagged', 'subnetUri': '',
             'purpose': 'Management', 'name': 'Net_283',
             'smartLink': False, 'privateNetwork': False,
             'connectionTemplateUri': None, 'type': ETHERNET_NETWORK_TYPE},
            {'vlanId': '126', 'networkId': '10.126.0.0',
                'ethernetNetworkType': 'Tagged', 'subnetUri': '',
                'purpose': 'VMMigration', 'name': 'CLRM-VMotion',
                'smartLink': False, 'privateNetwork': False,
                'connectionTemplateUri': None, 'type': ETHERNET_NETWORK_TYPE},
            {'vlanId': '100', 'networkId': '10.100.0.0',
                'ethernetNetworkType': 'Tagged', 'subnetUri': '',
                'purpose': 'Management', 'name': 'CLRM-Mgmt',
                'smartLink': False, 'privateNetwork': False,
                'connectionTemplateUri': None, 'type': ETHERNET_NETWORK_TYPE}]
# ##### ROSE DATA ######
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

APPLIANCE_IP = '16.114.217.122'  # Rose-ov.vse.rdlabs.hpecorp.net
HOSTNAME = 'rose-ov.vse.rdlabs.hpecorp.net'
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'
FUSION_PROMPT = 'root'
FUSION_TIMEOUT = 35
SSH_USER = 'root'
SSH_PASS = 'Wpst@hpvse123#!'
interface = 'bond0'
one_gb = 1073741824

NUVO_IP = '16.114.220.181'
NUVO_VOL = '/home/testNuvo/rose:/client_mnt'
NUVO_REIMAGE_FILE = 'hub.docker.hpecorp.net/rist/ovreimage:latest'
restore_timeout = '150m'
restore_poll_interval = '5m'
NUVO_SSH_USERNAME = 'root'
NUVO_SSH_PASSWORD = 'hpvse123'
NUVO_PROMPT = 'root'
NUVO_TIMEOUT = 35

EG1 = '3enc'
LE1 = 'LE1'

LIG1 = 'SASLIG1'
LIG2 = 'CarbonLIG1'
LIG3 = 'PotashLIG'
LIG4 = 'SASLIG2'
LIG5 = 'SASLIG3'
LIG6 = 'CarbonLIG2'
LIG7 = 'CarbonLIG3'

ENC1 = 'MXQ71700GQ'
ENC2 = 'MXQ71700GP'
ENC3 = 'MXQ71700GN'

ENCS = [ENC1, ENC2, ENC3]

bays_480 = [3, 4, 7, 8, 9, 10]
bays_660 = [5, 6]


LI = {'name': 'LE1-PotashLIG'}

sp_name = 'P10_480'

sp_name_update = [{'name': 'P10_480'}]

# Added for effuse tests
POTASH_LI = 'LE1-PotashLIG'
CARBON_LI = 'LE1-CarbonLIG1-1'
NATASHA_LIs = ['LE1-SASLIG1-1']
CL20 = 'Synergy 20Gb Interconnect Link Module'
CL10 = 'Synergy 10Gb Interconnect Link Module'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'

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
               'virtIpv4Addr': '16.114.217.122',
               'app1Ipv4Addr': '16.114.217.127',
               'app2Ipv4Addr': '16.114.217.126',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': HOSTNAME,
               'confOneNode': True,
               'domainName': 'vse.rdlabs.hpecorp.net',
               'aliasDisabled': True,
               }],
             }

CIM_HOSTS = {"active": "16.114.217.126",
             "standby": "16.114.217.127"
             }

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
      ]

e2 = [{'name': n,
       'type': ETHERNET_NETWORK_TYPE,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(101, 125)]

e3 = [{'name': n,
       'type': ETHERNET_NETWORK_TYPE,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(127, 282)]

e4 = [{'name': n,
       'type': ETHERNET_NETWORK_TYPE,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(284, 800)]

ethernet_networks = e1 + e2 + e3 + e4

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
        'networkUris': ['FCOE-SideA-3301'],
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
        'networkUris': ['FCOE-SideB-3302'],
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
        'networkUris': ['CLRM-Mgmt'] + ['CLRM-VMotion'] + rlist(101, 125) + rlist(127, 282) + rlist(284, 800),
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
        'networkUris': ['Net_283'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q3.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q3.2', 'speed': 'Auto'}
        ]
    },
    'Deployment': {
        'name': 'Deployment',
        'ethernetNetworkType': 'ImageStreamer',
        'networkType': 'Ethernet',
        'networkUris': ['Net_3010'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.2', 'speed': 'Auto'}
        ]
    }
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

POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
CL20 = 'Synergy 20Gb Interconnect Link Module'
CARBON = 'Virtual Connect SE 16Gb FC Module for Synergy'
NATASHA = 'Synergy 12Gb SAS Connection Module'

sas_ligs = {LIG1: {'name': LIG1,
                   'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1,
                           'type': NATASHA, 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1,
                           'type': NATASHA, 'enclosureIndex': 1},
                   ],
                   'enclosureIndexes': [1],
                   'interconnectBaySet': 1,
                   },
            LIG4: {'name': LIG4,
                   'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1,
                           'type': NATASHA, 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1,
                           'type': NATASHA, 'enclosureIndex': 1},
                   ],
                   'enclosureIndexes': [1],
                   'interconnectBaySet': 1,
                   },
            LIG5: {'name': LIG5,
                   'type': SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                   'enclosureType': 'SY12000',
                   'interconnectMapTemplate': [
                       {'bay': 1, 'enclosure': 1,
                           'type': NATASHA, 'enclosureIndex': 1},
                       {'bay': 4, 'enclosure': 1,
                           'type': NATASHA, 'enclosureIndex': 1},
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
                                           {'bay': 6, 'enclosure': 1,
                                               'type': CL20, 'enclosureIndex': 1},
                                           {'bay': 3, 'enclosure': 2,
                                               'type': CL20, 'enclosureIndex': 2},
                                           {'bay': 6, 'enclosure': 2,
                                               'type': POTASH, 'enclosureIndex': 2},
                                           {'bay': 3, 'enclosure': 3,
                                               'type': CL20, 'enclosureIndex': 3},
                                           {'bay': 6, 'enclosure': 3,
                                               'type': CL20, 'enclosureIndex': 3}
                                           ],
                  enclosureIndexes=[1, 2, 3],
                  uplinkSets=[deepcopy(v) for v in potash_us.itervalues()])}

PotashLIG = ligs['PotashLIG']

enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 3,
                    'configurationScript': None,
                    'osDeploymentSettings': {'manageOSDeployment': True,
                                             'deploymentModeSettings': {'deploymentMode': 'Internal', 'deploymentNetworkUri': None}},
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 1},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri':
                             'SASLIG:%s' % LIG4, 'enclosureIndex': 2},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri':
                             'SASLIG:%s' % LIG5, 'enclosureIndex': 3},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri':
                             'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri':
                             'LIG:%s' % LIG6, 'enclosureIndex': 2},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri':
                             'LIG:%s' % LIG7, 'enclosureIndex': 3},
                         {'interconnectBay': 3,
                             'logicalInterconnectGroupUri': 'LIG:%s' % LIG3},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri':
                             'SASLIG:%s' % LIG1, 'enclosureIndex': 1},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri':
                             'SASLIG:%s' % LIG4, 'enclosureIndex': 2},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri':
                             'SASLIG:%s' % LIG5, 'enclosureIndex': 3},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri':
                             'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri':
                             'LIG:%s' % LIG6, 'enclosureIndex': 2},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri':
                             'LIG:%s' % LIG7, 'enclosureIndex': 3},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3}],
                    'ipAddressingMode': "External",
                    'ambientTemperatureMode': 'Standard',
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

UPLINK_SET_TYPE = 'uplink-setV4'
US_name = 'fc_uplink'
LI_name = '%s-%s' % (LE1, LIG3)
FC_name = 'FC-SAN-A'

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

osdeploymentserver = {'name': 'I3S', 'description': 'os deployment server',
                      'applianceUri': 'MXQ71700GN, appliance 1', 'mgmtNetworkUri': ['Net_283'],
                      'deplManagersType': 'Image Streamer'}

goldenimage = [
    {'name': 'ESXi 6.5 U2', 'description': 'valid_goldenimage', 'file': "valid_file", 'location': 'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/OS%20Images/ImageStreamer/ESX 6.5 U2 image.zip'}]

planscript = {"type": "PlanScript", "description": "valid deploy planscript",
              "name": "planscript_1", "hpProvided": "false", "planType": "deploy",
              "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"}

buildplan = {"type": "OeBuildPlanV5",
             "customAttributes": [{"constraints": "{}",
                                   "description": "To enable ssh", "name": "SSH",
                                   "value": "enabled", "type": "string"}],
             "buildStep": [{"planScriptUri": "planscript_1",
                            "serialNumber": "1", "parameters": "1"}],
             "hpProvided": False, "oeBuildPlanType": "deploy",
             "description": "Buildplan", "name": "buildplan_1"}

deploymentplan = [
    {"type": "OEDeploymentPlanV5",
     "name": "Deploy ESXi 6.5 U2",
     "description": "",
     "goldenImageURI": "ESXi 6.5 U2",
     "oeBuildPlanURI": "HPE - ESXi - deploy with multiple management NIC HA config-autobackup- 2018-07-31",
     "ostype": "ESXi",
     "hpProvided": "false",
     "customAttributes": [
         {"name": "SSH", "value": "enabled",
          "type": "option", "description": "",
          "editable": True, "visible": True,
          "constraints": "{\"options\":[\"enabled\",\"disabled\"]}"},
         {"name": "ManagementNIC",
          "value": None, "type": "nic",
          "description": "", "editable": True,
          "visible": True,
          "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":true,\"ipv4disable\":false,\"parameters\":[\"dns1\",\"dns2\",\"gateway\",\"ipaddress\",\"mac\",\"netmask\",\"vlanid\"]}"},
         {"name": "ManagementNIC2",
          "value": None, "type": "nic",
          "description": "", "editable": True,
          "visible": True,
          "constraints": "{\"ipv4static\":true,\"ipv4dhcp\":false,\"ipv4disable\":false,\"parameters\":[\"mac\",\"vlanid\"]}"},
         {"name": "Password",
          "value": "", "type": "password",
          "description": "Password value must meet password complexity and minimum length requirements defined for ESXi 5.x, ESXi 6.x appropriately.",
          "editable": True, "visible": True,
          "constraints": "{\"options\":[\"\"]}"},
         {"name": "DomainName",
          "value": "", "type": "fqdn",
          "description": "", "editable": True,
          "visible": True, "constraints": "{\"helpText\":\"\"}"},
         {"name": "Hostname", "value": "",
          "type": "hostname", "description": "",
          "editable": True, "visible": True,
          "constraints": "{\"helpText\":\"\"}"}]}]

artifactbundle_extracts = [
    {'name': 'HPE-ESXi-2018-12-02-v5.0'}, {'name': 'HPE-ESXi-6.7-2018-11-27-v5.0'}]

Hypervisor_manager = [{'username': 'administrator@vsphere.local', 'password': 'CDT-hpvse123', 'type': 'HypervisorManagerV2', 'name': '16.114.220.87', 'port': '443',
                       'version': '6.5.0', 'virtualSwitchType': 'Standard', 'distributedSwitchVersion': '4.0', 'distributedSwitchUsage': '0',
                       'hypervisor_type': 'Vmware', 'multiNicVMotion': 'true', "drsEnabled": 'true', "haEnabled": 'true'}]

CERTIFICATE = {
    "certificateDetails": [{
        "aliasName": "Vcenter",
        "base64Data": "",
        "type": "CertificateDetailV2"
    }],
    "type": "CertificateInfoV2"
}

CLUSTER_PATH = "CLRM-CDT-DC-1"
HYPERV_MGR = Hypervisor_manager[0]['name']
osDeploymentPlan = deploymentplan[0]['name']

STORESERV_NAME = 'rose-3par-srv'
STORESERV_HOSTNAME = 'rose-3par-srv.vse.rdlabs.hpecorp.net'
STORESERV_POOL1 = 'FC_r1'
STORESERV_POOL2 = 'FC_r5'

# StoreVirtual
STOREVIRTUAL_NAME = 'cdt-cluster'
STOREVIRTUAL_HOSTNAME = '16.114.217.140'

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
             "name": "16.114.217.140",
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

storage_volumes = []

print_pretty = True

all_volume_names = [
    "clrm_shared_volume-1",
    "clrm_shared_volume-2",
    "clrm_shared_volume-3",
    "clrm_shared_volume-4",
    "clrm_shared_volume-5",
    "clrm_shared_volume-6",
]


existing_volumes = []
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

customAttribute = {"hostname": "{enclosure}{profile}",
                   "domain": "cdt.lab.fc",
                   "password": "hpvse123"}

sp_conns_clrm_1 = [{"id": 1, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-A", "lagName": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 2, "name": "", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-B", "lagName": None, "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 3, "name": "Deployment Network A", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_3010", "requestedVFs": "Auto", "ipv4": {"ipAddressSource": "SubnetPool"}, "boot": {"bootVolumeSource": "UserDefined", "priority": "Primary", "ethernetBootType": "iSCSI", "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None, "secondBootTargetIp": "", "secondBootTargetPort": ""}}},
                   {"id": 7, "name": "Deployment Network B", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_3010", "requestedVFs": "Auto", "ipv4": {"ipAddressSource": "SubnetPool"}, "boot": {"bootVolumeSource": "UserDefined", "priority": "Secondary", "ethernetBootType": "iSCSI", "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None, "secondBootTargetIp": "", "secondBootTargetPort": ""}}},
                   {"id": 4, "name": "MGMT A", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "ETH:CLRM-Mgmt", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 5, "name": "VMotion A", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "ETH:CLRM-VMotion", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 6, "name": "VMGuest-A", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "ETH:Net_110", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 8, "name": "MGMT B", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "ETH:CLRM-Mgmt", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 9, "name": "VMotion B", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "ETH:CLRM-VMotion", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 10, "name": "VMGuest-B", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "ETH:Net_110", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   ]

sp_conns_clrm_2 = [{"id": 1, "name": "Deployment Network A", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_3010", "requestedVFs": "Auto", "ipv4": {"ipAddressSource": "SubnetPool"}, "boot": {"bootVolumeSource": "UserDefined", "priority": "Primary", "ethernetBootType": "iSCSI", "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None, "secondBootTargetIp": "", "secondBootTargetPort": ""}}},
                   {"id": 2, "name": "Deployment Network B", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_3010", "requestedVFs": "Auto", "ipv4": {"ipAddressSource": "SubnetPool"}, "boot": {"bootVolumeSource": "UserDefined", "priority": "Secondary", "ethernetBootType": "iSCSI", "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None, "secondBootTargetIp": "", "secondBootTargetPort": ""}}},
                   {"id": 3, "name": "MGMT A", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "ETH:CLRM-Mgmt", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 5, "name": "VMotion A", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "ETH:CLRM-VMotion", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 7, "name": "VMGuest-A", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:NetSet1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 4, "name": "MGMT B", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "ETH:CLRM-Mgmt", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 6, "name": "VMotion B", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "ETH:CLRM-VMotion", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 8, "name": "VMGuest-B", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:NetSet1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   ]

sp_conns_clrm_3 = [{"id": 1, "name": "Deployment Network A", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:Net_3010", "requestedVFs": "Auto", "ipv4": {"ipAddressSource": "SubnetPool"}, "boot": {"bootVolumeSource": "UserDefined", "priority": "Primary", "ethernetBootType": "iSCSI", "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None, "secondBootTargetIp": "", "secondBootTargetPort": ""}}},
                   {"id": 2, "name": "Deployment Network B", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_3010", "requestedVFs": "Auto", "ipv4": {"ipAddressSource": "SubnetPool"}, "boot": {"bootVolumeSource": "UserDefined", "priority": "Secondary", "ethernetBootType": "iSCSI", "iscsi": {"initiatorNameSource": "ProfileInitiatorName", "firstBootTargetIp": None, "secondBootTargetIp": "", "secondBootTargetPort": ""}}},
                   {"id": 3, "name": "MGMT A", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "ETH:CLRM-Mgmt", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 5, "name": "VMotion A", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "ETH:CLRM-VMotion", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 7, "name": "VMGuest-A", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "ETH:Tunnel1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 4, "name": "MGMT B", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "ETH:CLRM-Mgmt", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 6, "name": "VMotion B", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "ETH:CLRM-VMotion", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 8, "name": "VMGuest-B", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "ETH:Tunnel1", "lagName": None, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                   ]

sy_480_gen10 = {
    "Synergy 480 Gen10": {
        "adapters": [
            {
                "model": "HPE Smart Array P416ie-m SR G10",
                "location": "Mezz",
                "slot": 1,
                "deviceType": "SAS"
            },
            {
                "model": "Synergy 3830C 16G FC HBA",
                "location": "Mezz",
                "slot": 2,
                "deviceType": "FibreChannel"
            },
            {
                "model": "Synergy 3820C 10/20Gb CNA",
                "location": "Mezz",
                "slot": 3,
                "deviceType": "Ethernet"
            },

        ]
    }
}

sy_480_gen9a = {
    "Synergy 480 Gen9": {
        "adapters": [
            {
                "model": "Smart Array P542D Controller",
                "location": "Mezz",
                "slot": 1,
                "deviceType": "SAS"
            },
            {
                "model": "Synergy 3830C 16G FC HBA",
                "location": "Mezz",
                "slot": 2,
                "deviceType": "FibreChannel"
            },
            {
                "model": "Synergy 3820C 10/20Gb CNA",
                "location": "Mezz",
                "slot": 3,
                "deviceType": "Ethernet"
            },

        ]
    }
}

sy_480_gen9b = {
    "Synergy 480 Gen9": {
        "adapters": [
            {
                "model": "Smart Array P542D Controller",
                "location": "Mezz",
                "slot": 1,
                "deviceType": "SAS"
            },
            {
                "model": "Synergy 3820C 10/20Gb CNA",
                "location": "Mezz",
                "slot": 3,
                "deviceType": "Ethernet"
            },

        ]
    }
}

sy_660_gen9 = {
    "Synergy 660 Gen9": {
        "adapters": [
            {
                "model": "Smart Array P542D Controller",
                "location": "Mezz",
                "slot": 1,
                "deviceType": "SAS"
            },
            {
                "model": "Synergy 3830C 16G FC HBA",
                "location": "Mezz",
                "slot": 2,
                "deviceType": "FibreChannel"
            },
            {
                "model": "Synergy 3820C 10/20Gb CNA",
                "location": "Mezz",
                "slot": 3,
                "deviceType": "Ethernet"
            },

        ]
    }
}

hyperv_spts = [
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 480 Gen10',
        'serverHardwareTypeUri': sy_480_gen10,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical', 'wwnType': 'Physical', 'name': 'CLRM-SPT-Gen10',
        'description': 'Server Profile Template created from SY 480 Gen10', 'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_clrm_1), 'manageConnections': True, "complianceControl": "Checked"},
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {'controllers': [],
                         'sasLogicalJBODs': []},

        "osDeploymentSettings": {"osDeploymentPlanUri": osDeploymentPlan, "complianceControl": "Checked",
                                 "osCustomAttributes": [{"name": "DomainName", "value": customAttribute["domain"], "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                                        {"name": "Hostname", "value": customAttribute["hostname"], "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                                        {"name": "ManagementNIC.connectionid", "value": "4"},
                                                        {"name": "ManagementNIC.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC.vlanid", "value": "0"},
                                                        {"name": "ManagementNIC2.connectionid", "value": "8"},
                                                        {"name": "ManagementNIC2.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC2.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC2.vlanid", "value": "0"},
                                                        {"name": "Password", "value": customAttribute["password"]},
                                                        {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]
                                 },

        'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, "complianceControl": "CheckedMinimum",
                       'volumeAttachments': [{"id": vol_id,
                                              "volumeUri": "SVOL:clrm_shared_volume-%i" % vol_id,
                                              "lunType": "Auto",
                                              "lun": None,
                                              "bootVolumePriority": "NotBootable",
                                              "storagePaths": [{'isEnabled': True, 'connectionId': 1,
                                                                'targetSelector': 'Auto', 'targets': []},
                                                               {'isEnabled': True, 'connectionId': 2,
                                                                'targetSelector': 'Auto', 'targets': []}]
                                              } for vol_id in range(1, 6)],
                       },
    },
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 660 Gen9 ',
        'serverHardwareTypeUri': sy_660_gen9,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical', 'wwnType': 'Physical', 'name': 'CLRM-SPT-Gen9-660',
        'description': 'Server Profile Template created from SY 660 Gen9', 'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_clrm_1), 'manageConnections': True, "complianceControl": "Checked"},
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {'controllers': [],
                         'sasLogicalJBODs': []},

        "osDeploymentSettings": {"osDeploymentPlanUri": osDeploymentPlan, "complianceControl": "Checked",
                                 "osCustomAttributes": [{"name": "DomainName", "value": customAttribute["domain"], "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                                        {"name": "Hostname", "value": customAttribute["hostname"], "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                                        {"name": "ManagementNIC.connectionid", "value": "4"},
                                                        {"name": "ManagementNIC.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC.vlanid", "value": "0"},
                                                        {"name": "ManagementNIC2.connectionid", "value": "8"},
                                                        {"name": "ManagementNIC2.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC2.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC2.vlanid", "value": "0"},
                                                        {"name": "Password", "value": customAttribute["password"]},
                                                        {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]
                                 },

        'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True, "complianceControl": "CheckedMinimum",
                       'volumeAttachments': [{"id": v_id,
                                              "volumeUri": "SVOL:clrm_shared_volume-%i" % v_id,
                                              "lunType": "Auto",
                                              "lun": None,
                                              "bootVolumePriority": "NotBootable",
                                              "storagePaths": [{'isEnabled': True, 'connectionId': 1,
                                                                'targetSelector': 'Auto', 'targets': []},
                                                               {'isEnabled': True, 'connectionId': 2,
                                                                'targetSelector': 'Auto', 'targets': []}]
                                              } for v_id in range(1, 6)],
                       },
    },
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 480 Gen9',
        'serverHardwareTypeUri': sy_480_gen9b,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical', 'wwnType': 'Physical', 'name': 'CLRM-SPT-Gen9-480',
        'description': 'Server Profile Template created from SY 480 Gen9', 'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_clrm_3), 'manageConnections': True, "complianceControl": "Checked"},
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {'controllers': [],
                         'sasLogicalJBODs': []},

        "osDeploymentSettings": {"osDeploymentPlanUri": osDeploymentPlan, "complianceControl": "Checked",
                                 "osCustomAttributes": [{"name": "DomainName", "value": customAttribute["domain"], "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                                        {"name": "Hostname", "value": customAttribute["hostname"], "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                                        {"name": "ManagementNIC.connectionid", "value": "3"},
                                                        {"name": "ManagementNIC.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC.vlanid", "value": "0"},
                                                        {"name": "ManagementNIC2.connectionid", "value": "4"},
                                                        {"name": "ManagementNIC2.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC2.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC2.vlanid", "value": "0"},
                                                        {"name": "Password", "value": customAttribute["password"]},
                                                        {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]
                                 },

    },
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 480 Gen9',
        'serverHardwareTypeUri': sy_480_gen9b,
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
        'macType': 'Physical', 'wwnType': 'Physical', 'name': 'CLRM-SPT-Gen9-480-JBOD',
        'description': 'Server Profile Template created from SY 480 Gen9 ', 'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_conns_clrm_2), 'manageConnections': True, "complianceControl": "Checked"},
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True, "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]}, 'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            "complianceControl": "Checked",
            'controllers': [{"logicalDrives": [{"name": None,
                                                "raidLevel": "RAID0",
                                                "bootable": False,
                                                "numPhysicalDrives": None,
                                                "driveTechnology": None,
                                                "sasLogicalJBODId": 1,
                                                "accelerator": "Unmanaged"}],
                             "deviceSlot": "Mezz 1",
                             "mode": "RAID",
                             "initialize": False
                             }],
            'sasLogicalJBODs': [{"id": 1,
                                 "deviceSlot": "Mezz 1",
                                 "name": "Datastore",
                                 "numPhysicalDrives": 1,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "persistent": False,
                                 "eraseData": True}, ]
        },
        "osDeploymentSettings": {"osDeploymentPlanUri": osDeploymentPlan, "complianceControl": "Checked",
                                 "osCustomAttributes": [{"name": "DomainName", "value": customAttribute["domain"], "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                                        {"name": "Hostname", "value": customAttribute["hostname"], "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                                        {"name": "ManagementNIC.connectionid", "value": "3"},
                                                        {"name": "ManagementNIC.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC.vlanid", "value": "0"},
                                                        {"name": "ManagementNIC2.connectionid", "value": "4"},
                                                        {"name": "ManagementNIC2.networkuri", "value": "ETH:" + "CLRM-Mgmt"},
                                                        {"name": "ManagementNIC2.constraint", "value": "auto"},
                                                        {"name": "ManagementNIC2.vlanid", "value": "0"},
                                                        {"name": "Password", "value": customAttribute["password"]},
                                                        {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]
                                 },

    }

]

hyperv_cluster_profiles = [
    {
        "type": "HypervisorClusterProfileV3",
        "description": "",
        "name": "Standard-CLRM-SPT-Gen10",
        "hypervisorManagerUri": 'HM:%s' % HYPERV_MGR,
        "path": CLUSTER_PATH,
        "initialScopeUris": [

        ],
        "hypervisorType": "Vmware",
        "hypervisorClusterSettings": {
            "type": "Vmware",
            "drsEnabled": True,
            "haEnabled": True,
            "multiNicVMotion": True,
            "virtualSwitchType": "Standard"
        },
        "hypervisorHostProfileTemplate": {
            "serverProfileTemplateUri": 'SPT:CLRM-SPT-Gen10',
            "deploymentPlan": {
                "serverPassword": "hpvse123",
                "deploymentCustomArgs": [

                ]
            },
            "hostprefix": "CP-Gen10-Std",
            "hostConfigPolicy": {
                "leaveHostInMaintenance": False,
                "useHostnameToRegister": False
            },
            "virtualSwitchConfigPolicy": {
                "manageVirtualSwitches": True,
                "configurePortGroups": True
            }
        },
        "sharedStorageVolumes": [
            {"name": "clrm_shared_volume-1", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-2", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-3", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-4", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-5", "volumeFileSystemType": "Unmanaged"}

        ],
        "addHostRequests": [
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 3)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 4)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 6)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 7)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 8)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 10)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 11)},
            {"serverHardwareUri": '%s, bay %i' % (ENC3, 12)},
        ]
    },
    {
        "type": "HypervisorClusterProfileV3",
        "description": "",
        "name": "Distributed-CLRM-SPT-Gen10",
        "hypervisorManagerUri": 'HM:%s' % HYPERV_MGR,
        "path": CLUSTER_PATH,
        "initialScopeUris": [

        ],
        "hypervisorType": "Vmware",
        "hypervisorClusterSettings": {
            "type": "Vmware",
            "drsEnabled": True,
            "haEnabled": True,
            "multiNicVMotion": True,
            "virtualSwitchType": "Distributed",
            "distributedSwitchVersion": "6.0.0",
            "distributedSwitchUsage": "GeneralNetworks"
        },
        "hypervisorHostProfileTemplate": {
            "serverProfileTemplateUri": 'SPT:CLRM-SPT-Gen10',
            "deploymentPlan": {
                "serverPassword": "hpvse123",
                "deploymentCustomArgs": [

                ]
            },
            "hostprefix": "CP-Gen10-Distributed",
            "hostConfigPolicy": {
                "leaveHostInMaintenance": False,
                "useHostnameToRegister": False
            },
            "virtualSwitchConfigPolicy": {
                "manageVirtualSwitches": True,
                "configurePortGroups": True
            }
        },
        "sharedStorageVolumes": [
            {"name": "clrm_shared_volume-1", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-2", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-3", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-4", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-5", "volumeFileSystemType": "Unmanaged"}

        ],
        "addHostRequests": [
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 3)},
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 4)},
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 7)},
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 8)},
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 9)},
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 10)},
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 11)},

        ]
    },
    {
        "type": "HypervisorClusterProfileV3",
        "description": "",
        "name": "Standard-CLRM-SPT-Gen9-480-Local",
        "hypervisorManagerUri": 'HM:%s' % HYPERV_MGR,
        "path": CLUSTER_PATH,
        "initialScopeUris": [

        ],
        "hypervisorType": "Vmware",
        "hypervisorClusterSettings": {
            "type": "Vmware",
            "drsEnabled": True,
            "haEnabled": True,
            "multiNicVMotion": True,
            "virtualSwitchType": "Standard"
        },
        "hypervisorHostProfileTemplate": {
            "serverProfileTemplateUri": 'SPT:CLRM-SPT-Gen9-480',
            "deploymentPlan": {
                "serverPassword": "hpvse123",
                "deploymentCustomArgs": [

                ]
            },
            "hostprefix": "CP-Gen9-480-Std",
            "hostConfigPolicy": {
                "leaveHostInMaintenance": False,
                "useHostnameToRegister": False
            },
            "virtualSwitchConfigPolicy": {
                "manageVirtualSwitches": True,
                "configurePortGroups": True
            }
        },
        "addHostRequests": [
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 7)},
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 8)},
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 9)}

        ]
    },
    {
        "type": "HypervisorClusterProfileV3",
        "description": "",
        "name": "Standard-CLRM-SPT-Gen9-480-JBOD",
        "hypervisorManagerUri": 'HM:%s' % HYPERV_MGR,
        "path": CLUSTER_PATH,
        "initialScopeUris": [

        ],
        "hypervisorType": "Vmware",
        "hypervisorClusterSettings": {
            "type": "Vmware",
            "drsEnabled": True,
            "haEnabled": True,
            "multiNicVMotion": True,
            "virtualSwitchType": "Standard"
        },
        "hypervisorHostProfileTemplate": {
            "serverProfileTemplateUri": 'SPT:CLRM-SPT-Gen9-480-JBOD',
            "deploymentPlan": {
                "serverPassword": "hpvse123",
                "deploymentCustomArgs": [

                ]
            },
            "hostprefix": "CP-Gen9-480-Std-JBOD",
            "hostConfigPolicy": {
                "leaveHostInMaintenance": False,
                "useHostnameToRegister": False
            },
            "virtualSwitchConfigPolicy": {
                "manageVirtualSwitches": True,
                "configurePortGroups": True
            }
        },
        "addHostRequests": [
            {"serverHardwareUri": '%s, bay %i' % (ENC2, 5)},
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 3)},
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 4)}
        ]
    },
    {
        "type": "HypervisorClusterProfileV3",
        "description": "",
        "name": "Standard-CLRM-SPT-Gen9-660",
        "hypervisorManagerUri": 'HM:%s' % HYPERV_MGR,
        "path": CLUSTER_PATH,
        "initialScopeUris": [

        ],
        "hypervisorType": "Vmware",
        "hypervisorClusterSettings": {
            "type": "Vmware",
            "drsEnabled": True,
            "haEnabled": True,
            "multiNicVMotion": True,
            "virtualSwitchType": "Standard"
        },
        "hypervisorHostProfileTemplate": {
            "serverProfileTemplateUri": 'SPT:CLRM-SPT-Gen9-660',
            "deploymentPlan": {
                "serverPassword": "hpvse123",
                "deploymentCustomArgs": [

                ]
            },
            "hostprefix": "CP-Gen9-660-Std",
            "hostConfigPolicy": {
                "leaveHostInMaintenance": True,
                "useHostnameToRegister": True
            },
            "virtualSwitchConfigPolicy": {
                "manageVirtualSwitches": True,
                "configurePortGroups": True
            }
        },
        "sharedStorageVolumes": [
            {"name": "clrm_shared_volume-1", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-2", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-3", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-4", "volumeFileSystemType": "Unmanaged"},
            {"name": "clrm_shared_volume-5", "volumeFileSystemType": "Unmanaged"}

        ],
        "addHostRequests": [
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 5)},
            {"serverHardwareUri": '%s, bay %i' % (ENC1, 6)},
        ]
    }
]

edit_network = 'Net_111'
add_ethernet_networks = 'Net_110'
add_vol = 'clrm_shared_volume-6'

HCP_Profiles_for_edit_SPT = ['Standard-CLRM-SPT-Gen9-480-Local', 'Standard-CLRM-SPT-Gen9-480-Local', 'Standard-CLRM-SPT-Gen10', 'Standard-CLRM-SPT-Gen9-660']

HCP_Profiles_for_del_add_SPT = ['Standard-CLRM-SPT-Gen10', 'Standard-CLRM-SPT-Gen9-480-Local', 'Standard-CLRM-SPT-Gen10', 'Standard-CLRM-SPT-Gen9-660']

HCP_Profiles_for_edit_SP = ['Standard-CLRM-SPT-Gen9-480-JBOD', 'Standard-CLRM-SPT-Gen9-480-Local', 'Standard-CLRM-SPT-Gen10', 'Standard-CLRM-SPT-Gen9-660']

HCP_Profiles_for_del_conn_SP = ['Standard-CLRM-SPT-Gen9-660', 'Standard-CLRM-SPT-Gen9-480-Local', 'Standard-CLRM-SPT-Gen10', 'Standard-CLRM-SPT-Gen9-660']

HCP_Profiles_for_add_vol_SPT = ['Standard-CLRM-SPT-Gen9-660', 'Standard-CLRM-SPT-Gen10']

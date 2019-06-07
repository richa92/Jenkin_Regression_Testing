"""Data file for Scale setup."""


from copy import deepcopy
import json
from common_data import *


def rlist(start, end, prefix='Net_', suffix='', step=1):
    """rlist."""
    return ['%s%s%s' % (prefix, str(x), suffix)
            for x in xrange(start, end + 1, step)]


def us(**kwargs):
    """uplink set."""
    return {'name': kwargs.get('name', None),
            'ethernetNetworkType': kwargs.get('ethernetNetworkType', 'Tagged'),
            'networkType': 'Ethernet',
            'networkUris': kwargs.get('networkUris', None),
            'primaryPort': None,
            'nativeNetworkUri': None,
            'mode': 'Auto',
            'logicalPortConfigInfos': kwargs.get('logicalPortConfigInfos', None)}


def lig(**kwargs):
    """lig definition."""
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


def conns(conn_c, conn_d, mgmt, lag):
    """connections definition."""
    return [{"id": 3, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-a", "requestedMbps": "2500", "networkUri": "ETH:%s" % mgmt, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            {"id": 5, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-c", "requestedMbps": "2500", "networkUri": "NS:%s" % conn_c, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            {"id": 6, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-d", "requestedMbps": "2500", "networkUri": "NS:%s" % conn_d, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            {"id": 7, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-a", "requestedMbps": "2500", "networkUri": "ETH:Net_100", "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            {"id": 9, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-c", "requestedMbps": "2500", "networkUri": "NS:%s" % conn_c, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            {"id": 10, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-d", "requestedMbps": "2500", "networkUri": "NS:%s" % conn_d, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
            ]


def getEthernetConns(conn_b, conn_c, conn_d, mgmt="Net_100", lag=None):
    """Ethernet networks Definition."""
    return conns(conn_c, conn_d, mgmt, lag) + [{"id": 4, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "NS:%s" % conn_b, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                                               {"id": 8, "name": "", "functionType": "Ethernet", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "NS:%s" % conn_b, "lagName": lag, "requestedVFs": "0", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                                               ]


def getFCOEConns(fcoe_a, fcoe_b, conn_c, conn_d, mgmt="Net_100", lag=None):
    """FCOE networks definition."""
    return conns(conn_c, conn_d, mgmt, lag) + [{"id": 4, "name": "FCOE_SideA_conn", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "FCOE:%s" % fcoe_a, "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
                                               {"id": 8, "name": "FCOE_SideB_conn", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "FCOE:%s" % fcoe_b, "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}}
                                               ]


def getISCSIConns(conn_b, conn_c, conn_d, bconfig=None, mgmt="Net_100", lag=None):
    """ISCSI connection definitions."""

    print "boot config is ", bconfig
    side = [{"id": 4, "name": "iSCSI_SideA_conn", "functionType": "iSCSI", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "ETH:%s" % conn_b, "lagName": lag},
            {"id": 8, "name": "iSCSI_SideB_conn", "functionType": "iSCSI", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "ETH:%s" % conn_b, "lagName": lag}]
    if bconfig is not None:
        for i in [0, 1]:
            boot_params = {"boot": {"priority": ISCSI_PRIORITY[i], "bootVolumeSource": "ManagedVolume"},
                           "ipv4": {"ipAddressSource": "UserDefined", "subnetMask": bconfig[i][0], "gateway": bconfig[i][1], "ipAddress": bconfig[i][2]}}
            side[i].update(boot_params)
    return conns(conn_c, conn_d, mgmt, lag) + [side[0], side[1]]


def getFCConns(fc_a, fc_b, conn_c, conn_d, mgmt="Net_100", lag=None):
    """FC networks definition."""
    return conns(conn_c, conn_d, mgmt, lag) + [{"id": 4, "name": "FC_SideA_conn", "functionType": "FibreChannel", "portId": "Mezz 3:1-b", "requestedMbps": "2500", "networkUri": "FC:%s" % fc_a, "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
                                               {"id": 8, "name": "FC_SideB_conn", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "requestedMbps": "2500", "networkUri": "FC:%s" % fc_b, "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}}
                                               ]


APPLIANCE_IP = '16.114.212.143'
HOSTNAME = 'orchid-ov.vse.rdlabs.hpecorp.net'
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'
FUSION_PROMPT = 'root'
FUSION_TIMEOUT = 35
ssh_server_ip = ''  # Used in appliance_certificates1.txt

one_gb = 1073741824

SSH_USER = 'root'
SSH_PASS = 'hpvse1'
interface = 'bond0'
one_gb = 1073741824

NUVO_VOL = '/home/testNuvo/orchid:/client_mnt'

ENC1 = 'MXQ825050L'
ENC2 = 'MXQ825050C'
ENC3 = 'MXQ825050K'
ENC4 = 'MXQ825050D'
ENC5 = 'MXQ825050F'
ENC6 = 'MXQ825050G'
ENC7 = 'MXQ825050J'
ENC8 = 'MXQ825050H'
ENC9 = 'MXQ80805Q4'
ENC10 = 'MXQ80805PZ'
ENC11 = 'MXQ80805Q0'

SAS_LOGICAL_JBOD_TYPE = 'sas-logical-jbodV4'

ISCSI_PRIORITY = ["primary", "Secondary"]

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
               'ipv4Gateway': '16.114.208.1',
               'ipv4NameServers': ['16.125.25.81', '16.125.25.82'],
               'virtIpv4Addr': APPLIANCE_IP,
               'app1Ipv4Addr': '16.114.212.144',
               'app2Ipv4Addr': '16.114.212.145',
               'ipv6Type': 'UNCONFIGURE',
               'hostname': HOSTNAME,
               'confOneNode': True,
               'domainName': 'vse.rdlabs.hpecorp.net',
               'aliasDisabled': True,
               }],
             }

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

timeandlocale = {'type': 'TimeAndLocale',
                 'dateTime': None,
                 'timezone': 'UTC',
                 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

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
       'ethernetNetworkType': 'Tagged'},
      {'name': 'Deploy_500',
       'type': ETHERNET_NETWORK_TYPE,
       'vlanId': 500,
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
       'vlanId': int(n[4:])} for n in rlist(284, 499)]

e4 = [{'name': n,
       'type': ETHERNET_NETWORK_TYPE,
       'purpose': 'General',
       'smartLink': False,
       'privateNetwork': False,
       'connectionTemplateUri': None,
       'ethernetNetworkType': 'Tagged',
       'vlanId': int(n[4:])} for n in rlist(501, 2100)]

ethernet_networks = e1 + e2 + e3 + e4

network_sets = [{'name': 'NetSet1', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(589, 649),
                 'nativeNetworkUri': None},
                {'name': 'NetSet2', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(650, 710),
                 'nativeNetworkUri': None},
                {'name': 'NetSet3', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(711, 771),
                 'nativeNetworkUri': None},
                {'name': 'NetSet4', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(772, 832),
                 'nativeNetworkUri': None},
                {'name': 'NetSet5', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(833, 893),
                 'nativeNetworkUri': None},
                {'name': 'NetSet6', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(894, 954),
                 'nativeNetworkUri': None},
                {'name': 'NetSet7', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(955, 1015),
                 'nativeNetworkUri': None},
                {'name': 'NetSet8', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1016, 1076),
                 'nativeNetworkUri': None},
                {'name': 'NetSet9', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1077, 1137),
                 'nativeNetworkUri': None},
                {'name': 'NetSet10', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1138, 1198),
                 'nativeNetworkUri': None},
                {'name': 'NetSet11', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1199, 1259),
                 'nativeNetworkUri': None},
                {'name': 'NetSet12', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1260, 1320),
                 'nativeNetworkUri': None},
                {'name': 'NetSet13', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1321, 1381),
                 'nativeNetworkUri': None},
                {'name': 'NetSet14', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1382, 1442),
                 'nativeNetworkUri': None},
                {'name': 'NetSet15', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1443, 1503),
                 'nativeNetworkUri': None},
                {'name': 'NetSet16', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1504, 1564),
                 'nativeNetworkUri': None},
                {'name': 'NetSet17', 'type': NETWORK_SET_TYPE, 'networkUris': rlist(1565, 1625),
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
        'managedSanUri': 'FCSan:Orchid-Switch-10:00:88:94:71:2e:e5:5d',
        'fabricType': 'FabricAttach'}]

fc2 = [{'type': FC_NETWORK_TYPE,
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True,
        'name': 'FC-SAN-B',
        'connectionTemplateUri': None,
        'managedSanUri': 'FCSan:Orchid-Switch-10:00:88:94:71:2e:e5:5e',
        'fabricType': 'FabricAttach'}]

fc_networks = fc1 + fc2

###
# LIGs
###

LIG1 = 'SASLIG1'
LIG2 = 'CarbonLIG1'
LIG3 = 'PotashLIG1'
LIG4 = 'PotashLIG2'
LIG5 = 'PotashLIG3'


Potash_US1 = {

    'Ethernet-Tagged': {
        'name': 'Ethernet-Tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(100, 282) + rlist(284, 499) + rlist(501, 2000),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'}
        ]
    },
    'Deployment': {
        'name': 'Deployment',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Deploy_500'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.2', 'speed': 'Auto'}
        ]
    },
    'FC-SideA': {
        'name': 'SAN-A',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC-SAN-A'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'}
        ]
    },
    'FC-SideB': {
        'name': 'SAN-B',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC-SAN-B'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'},
        ]
    },
}

Potash_US2 = {

    'Ethernet-Tagged': {
        'name': 'Ethernet-Tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(100, 282) + rlist(284, 499) + rlist(501, 2000),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'}
        ]
    },
    'Deployment': {
        'name': 'Deployment',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Deploy_500'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.2', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.2', 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}
        ]
    },

}

Potash_US3 = {

    'Ethernet-Tagged': {
        'name': 'Ethernet-Tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': rlist(100, 282) + rlist(284, 499) + rlist(501, 2000),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q6.1', 'speed': 'Auto'}
        ]
    },
    'FC-SideA': {
        'name': 'SAN-A',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC-SAN-A'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'}
        ]
    },
    'FC-SideB': {
        'name': 'SAN-B',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC-SAN-B'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'},
        ]
    },
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
            }

ligs = {LIG2: lig(name=LIG2,
                  interconnectMapTemplate=[{'bay': 2, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1},
                                           {'bay': 5, 'enclosure': -1, 'type': CARBON, 'enclosureIndex': -1}],
                  enclosureIndexes=[-1],
                  interconnectBaySet=2,
                  redundancyType='Redundant',
                  uplinkSets=deepcopy(carbon_US)),
        LIG3: lig(name=LIG3,
                  interconnectMapTemplate=[{'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
                                           {'bay': 6, 'enclosure': 1, 'type': CL10, 'enclosureIndex': 1},
                                           {'bay': 3, 'enclosure': 2, 'type': CL10, 'enclosureIndex': 2},
                                           {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
                                           {'bay': 3, 'enclosure': 3, 'type': CL10, 'enclosureIndex': 3},
                                           {'bay': 6, 'enclosure': 3, 'type': CL10, 'enclosureIndex': 3},
                                           {'bay': 3, 'enclosure': 4, 'type': CL10, 'enclosureIndex': 4},
                                           {'bay': 6, 'enclosure': 4, 'type': CL10, 'enclosureIndex': 4},
                                           {'bay': 3, 'enclosure': 5, 'type': CL10, 'enclosureIndex': 5},
                                           {'bay': 6, 'enclosure': 5, 'type': CL10, 'enclosureIndex': 5}
                                           ],
                  enclosureIndexes=[1, 2, 3, 4, 5],
                  uplinkSets=[deepcopy(v) for v in Potash_US1.itervalues()]),
        LIG4: lig(name=LIG4,
                  interconnectMapTemplate=[{'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
                                           {'bay': 6, 'enclosure': 1, 'type': CL20, 'enclosureIndex': 1},
                                           {'bay': 3, 'enclosure': 2, 'type': CL20, 'enclosureIndex': 2},
                                           {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
                                           {'bay': 3, 'enclosure': 3, 'type': CL20, 'enclosureIndex': 3},
                                           {'bay': 6, 'enclosure': 3, 'type': CL20, 'enclosureIndex': 3}
                                           ],
                  enclosureIndexes=[1, 2, 3],
                  uplinkSets=[deepcopy(v) for v in Potash_US2.itervalues()]),
        LIG5: lig(name=LIG5,
                  interconnectMapTemplate=[{'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
                                           {'bay': 6, 'enclosure': 1, 'type': CL20, 'enclosureIndex': 1},
                                           {'bay': 3, 'enclosure': 2, 'type': CL20, 'enclosureIndex': 2},
                                           {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
                                           {'bay': 3, 'enclosure': 3, 'type': CL20, 'enclosureIndex': 3},
                                           {'bay': 6, 'enclosure': 3, 'type': CL20, 'enclosureIndex': 3}
                                           ],
                  enclosureIndexes=[1, 2, 3],
                  uplinkSets=[deepcopy(v) for v in Potash_US3.itervalues()])}


EG1 = '5enc'
EG2 = '3enc'
EG3 = '3enc_carbon'

enc_groups = {EG1: {'name': EG1,
                    'enclosureCount': 5,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 1},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 2},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 3},
                         {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 4},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 2},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 3},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 4},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 5},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 1},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 2},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 3},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'SASLIG:%s' % LIG1, 'enclosureIndex': 4},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 2},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 3},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 4},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 5},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG3}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    },
              EG2: {'name': EG2,
                    'enclosureCount': 3,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG4},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG4}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    },
              EG3: {'name': EG3,
                    'enclosureCount': 3,
                    'configurationScript': None,
                    'interconnectBayMappings':
                        [{'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 2},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 3},
                         {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG5},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 1},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 2},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG2, 'enclosureIndex': 3},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:%s' % LIG5}],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                    },
              }

LE1 = 'LE_5ENC'
LE2 = 'LE_3ENC'
LE3 = 'LE_3ENC_CARBON'

les = [{'name': LE1,
        'enclosureUris': ['ENC:%s' % ENC1, 'ENC:%s' % ENC2, 'ENC:%s' % ENC3, 'ENC:%s' % ENC4, 'ENC:%s' % ENC5],
        'enclosureGroupUri': 'EG:%s' % EG1,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       {'name': LE2,
        'enclosureUris': ['ENC:%s' % ENC6, 'ENC:%s' % ENC7, 'ENC:%s' % ENC8],
        'enclosureGroupUri': 'EG:%s' % EG2,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       {'name': LE3,
        'enclosureUris': ['ENC:%s' % ENC9, 'ENC:%s' % ENC10, 'ENC:%s' % ENC11],
        'enclosureGroupUri': 'EG:%s' % EG3,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       ]

# StoreServ
STORESERV_NAME = 'orchid-3par-srv'
STORESERV_HOSTNAME = 'orchid-3par-srv.vse.rdlabs.hpecorp.net'
STORESERV_POOL1 = 'FC_r1'
STORESERV_POOL2 = 'FC_r5'

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
                                                              'maximum': 17592186044416,
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
                                                                      'default': 'SPOOL:FC_r5'
                                                                      }
                                                     }
                                      }
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
    "P11_boot_volume_Orchid",
    "P12_boot_volume_Orchid",
    "P13_boot_volume_Orchid",
    "P14_boot_volume_Orchid",
    "P15_boot_volume_Orchid",
    "P15_data_volume_Orchid",
    "P17_boot_volume_Orchid",
    "P18_boot_volume_Orchid",
    "P19_boot_volume_Orchid",
    "P20_boot_volume_Orchid",
    "P21_boot_volume_Orchid",
    "P22_boot_volume_Orchid",
    "P23_boot_volume_Orchid",
    "P24_boot_volume_Orchid",
    "P25_boot_volume_Orchid",
    "P27_boot_volume_Orchid",
    "P28_boot_volume_Orchid",
    "P29_boot_volume_Orchid",
    "P30_boot_volume_Orchid",
    "P31_boot_volume_Orchid",
    "P32_boot_volume_Orchid",
    "P32_data_volume_Orchid",
    "P38_boot_volume_Orchid",
    "P38_data_volume_Orchid",
    "P39_boot_volume_Orchid",
    "P40_boot_volume_Orchid",
    "P41_boot_volume_Orchid",
    "P42_boot_volume_Orchid",
    "P43_boot_volume_Orchid",
    "P44_boot_volume_Orchid",
    "P45_boot_volume_Orchid",
    "P46_boot_volume_Orchid",
    "P47_boot_volume_Orchid",
    "P48_boot_volume_Orchid",
    "P49_boot_volume_Orchid",
    "P50_boot_volume_Orchid",
    "P57_boot_volume_iscsi_orchid",
    "P60_boot_volume_iscsi_orchid",
    "P61_boot_volume_Orchid",
    "P62_boot_volume_Orchid",
    "P63_boot_volume_Orchid",
    "P65_boot_volume_Orchid",
    "P66_boot_volume_Orchid",
    "P67_boot_volume_Orchid",
    "P67_data_volume_Orchid",
    "P68_boot_volume_Orchid",
    "P69_boot_volume_Orchid",
    "P70_boot_volume_Orchid",
    "P71_boot_volume_Orchid"
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

SPP_WEB_URL = 'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/SPP/Orchid'

# Used for downloading the perl-Module-Pluggable RPM needed in Cent OS 7.x. Key is Cent OS version, Value is url to download RPM
RPM_WEB_URL = {'7': 'http://wpstwork4.vse.rdlabs.hpecorp.net/CDT/RPM/Pluggable/centos/7'}
# Name of the server hosting dev mode package needed for RM performance measurement. Dictionary with Key=OV major version and value is host name
dev_pack_host = {'4': 'ci-artifacts02.vse.rdlabs.hpecorp.net', '5': 'ci-artifacts04.vse.rdlabs.hpecorp.net'}

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
         "value": "16.114.212.147"},
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

US_name = 'fc_uplink'
newLicenses = {'licenseType': 'Synergy 8Gb FC Upgrade',
               'license': [{'key': 'QBQC CQEA H9PY KHX2 V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 RJ87 E9VA KJVT D5KM EFVW TSNJ Q5A8 M7SS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'},
                           {'key': 'QBQG BQEA H9PA CHWZ V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 VJW5 FKFE KJVT D5KM EFVW TSNJ Q5Y8 N7SS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'},
                           {'key': '9BQA DQEA H9PA KHWY V2B4 HWWV Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 NJKZ HLVE KJVT D5KM EFVW TSNJ Y5AM 67CS SMT9 YGS6 SMQQ MUCF UW2L MYN7 N2QC DHKQ XJUL LUQH TU8F 3DQC SW7N VEQW V886 FE23 YWAT J8U3 2YT5 RNNV MHS3 QKTQ 688U F8A7 F8SE Z2DX RJQ6 MHPE SN9R 3UNK TVPT 74UF NGGT EHM4 "EVAL-N3R43A_ILR N3R43A_ILR Synergy_8Gb_FC_Upgrade_License EVAL-N3R43A_ILR"'},
                           {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
                           {'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}
                           ]
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

fc_conns_noboot = [{"id": 1, "name": "FC-SAN-A", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-A", "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 2, "name": "FC-SAN-B", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-B", "boot": {"priority": "NotBootable", "iscsi": {}}}]

fc_conns_boot = [{"id": 1, "name": "FC-SAN-A", "functionType": "FibreChannel", "portId": "Mezz 2:1", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-A", "boot": {"priority": "Primary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}},
                 {"id": 2, "name": "FC-SAN-B", "functionType": "FibreChannel", "portId": "Mezz 2:2", "requestedMbps": "Auto", "networkUri": "FC:FC-SAN-B", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume", "iscsi": {}}}]


sp_eth_conns_123 = getEthernetConns("NetSet1", "NetSet2", "NetSet3")
sp_eth_conns_345 = getEthernetConns("NetSet3", "NetSet4", "NetSet5")
sp_eth_conns_678 = getEthernetConns("NetSet6", "NetSet7", "NetSet8")
sp_eth_conns_234 = getEthernetConns("NetSet2", "NetSet3", "NetSet4")
sp_eth_conns_567 = getEthernetConns("NetSet5", "NetSet6", "NetSet7")
sp_eth_conns_456 = getEthernetConns("NetSet4", "NetSet5", "NetSet6")
sp_eth_conns_246 = getEthernetConns("NetSet2", "NetSet4", "NetSet6")
sp_eth_conns_138 = getEthernetConns("NetSet1", "NetSet3", "NetSet8")
sp_eth_conns_281 = getEthernetConns("NetSet2", "NetSet8", "NetSet1")
sp_eth_conns_91011 = getEthernetConns("NetSet9", "NetSet10", "NetSet11")
sp_eth_conns_101112 = getEthernetConns("NetSet10", "NetSet11", "NetSet12")
sp_eth_conns_121314 = getEthernetConns("NetSet12", "NetSet13", "NetSet14")
sp_eth_conns_131415 = getEthernetConns("NetSet13", "NetSet14", "NetSet15")
sp_eth_conns_151617 = getEthernetConns("NetSet15", "NetSet16", "NetSet17")
# sp_eth_conns_16178 = getEthernetConns("NetSet16", "NetSet17", "NetSet8")

# Carbon FC Connections
sp_fc_eth_conns_123 = fc_conns_boot + sp_eth_conns_123
# sp_fc_eth_conns_345 = fc_conns_boot + sp_eth_conns_345
sp_fc_eth_conns_678 = fc_conns_boot + sp_eth_conns_678
# sp_fc_eth_conns_234 = fc_conns_boot + sp_eth_conns_234
sp_fc_eth_conns_456 = fc_conns_boot + sp_eth_conns_456
sp_fc_eth_conns_246 = fc_conns_boot + sp_eth_conns_246
sp_fc_eth_conns_281 = fc_conns_boot + sp_eth_conns_281
sp_fc_eth_conns_101112 = fc_conns_boot + sp_eth_conns_101112
# sp_fc_eth_conns_91011 = fc_conns_boot + sp_eth_conns_91011
# sp_fc_eth_conns_121314 = fc_conns_boot + sp_eth_conns_121314
sp_fc_eth_conns_151617 = fc_conns_boot + sp_eth_conns_151617

# sp_iscsi_conns_23 = getISCSIConns("iSCSI_283", "NetSet2", "NetSet3")
# sp_fc_iscsi_conns = fc_conns_boot + sp_iscsi_conns_23

# Potash native FC Connections
sp_fc_eth_conns_23 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet2", "NetSet3")
sp_fc_eth_conns_12 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet1", "NetSet2")
sp_fc_eth_conns_56 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet5", "NetSet6")
sp_fc_eth_conns_910 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet9", "NetSet10")
sp_fc_eth_conns_45 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet4", "NetSet5")
sp_fc_eth_conns_67 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet6", "NetSet7")
sp_fc_eth_conns_28 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet2", "NetSet8")
sp_fc_eth_conns_78 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet7", "NetSet8")
sp_fc_eth_conns_38 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet3", "NetSet8")
sp_fc_eth_conns_1516 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet15", "NetSet16")
sp_fc_eth_conns_1617 = getFCConns("FC-SAN-A", "FC-SAN-B", "NetSet16", "NetSet17")

# boot_config is a list of following items "subnetMask", "gateway", "ipAddress"
boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.150"], ["255.255.240.0", "16.114.208.1", "16.114.217.151"]]
sp_iscsi_conns_1314 = getISCSIConns("iSCSI_283", "NetSet13", "NetSet14", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.152"], ["255.255.240.0", "16.114.208.1", "16.114.217.153"]]
sp_iscsi_conns_78 = getISCSIConns("iSCSI_283", "NetSet7", "NetSet8", boot_config)

# boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.154"], ["255.255.240.0", "16.114.208.1", "16.114.217.155"]]
# sp_iscsi_conns_67 = getISCSIConns("iSCSI_283", "NetSet6", "NetSet7", boot_config)

# boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.156"], ["255.255.240.0", "16.114.208.1", "16.114.217.157"]]
# sp_iscsi_conns_78_2 = getISCSIConns("iSCSI_283", "NetSet7", "NetSet8", boot_config)

# boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.221"], ["255.255.240.0", "16.114.208.1", "16.114.217.222"]]
# sp_iscsi_conns_38 = getISCSIConns("iSCSI_283", "NetSet3", "NetSet8", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.223"], ["255.255.240.0", "16.114.208.1", "16.114.217.224"]]
sp_iscsi_conns_89 = getISCSIConns("iSCSI_283", "NetSet8", "NetSet9", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.225"], ["255.255.240.0", "16.114.208.1", "16.114.217.226"]]
sp_iscsi_conns_1011 = getISCSIConns("iSCSI_283", "NetSet10", "NetSet11", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.227"], ["255.255.240.0", "16.114.208.1", "16.114.217.228"]]
sp_iscsi_conns_1112 = getISCSIConns("iSCSI_283", "NetSet11", "NetSet12", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.217.229"], ["255.255.240.0", "16.114.208.1", "16.114.217.230"]]
sp_iscsi_conns_1213 = getISCSIConns("iSCSI_283", "NetSet12", "NetSet13", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.212.151"], ["255.255.240.0", "16.114.208.1", "16.114.212.152"]]
sp_iscsi_conns_1617 = getISCSIConns("iSCSI_283", "NetSet16", "NetSet17", boot_config)

boot_config = [["255.255.240.0", "16.114.208.1", "16.114.212.153"], ["255.255.240.0", "16.114.208.1", "16.114.212.154"]]
sp_iscsi_conns_1415 = getISCSIConns("iSCSI_283", "NetSet14", "NetSet15", boot_config)

assigned_sp_to_bay_map = dict(
    {
        'P1_480_O': '%s, bay %i' % (ENC1, 3),
        'P2_480_O': '%s, bay %i' % (ENC1, 4),
        'P3_480_O': '%s, bay %i' % (ENC1, 5),
        'P4_480_O': '%s, bay %i' % (ENC1, 6),
        'P5_480_O': '%s, bay %i' % (ENC1, 7),
        'P6_480_O': '%s, bay %i' % (ENC1, 8),
        'P7_480_O': '%s, bay %i' % (ENC1, 9),
        'P8_480_O': '%s, bay %i' % (ENC1, 10),
        'P9_480_O': '%s, bay %i' % (ENC1, 11),
        'P10_480_O': '%s, bay %i' % (ENC1, 12),
        'P11_480_O': '%s, bay %i' % (ENC2, 1),
        'P12_480_O': '%s, bay %i' % (ENC2, 2),
        'P13_480_O': '%s, bay %i' % (ENC2, 3),
        'P14_480_O': '%s, bay %i' % (ENC2, 4),
        'P15_480_O': '%s, bay %i' % (ENC2, 5),
        'P16_480_O': '%s, bay %i' % (ENC2, 6),
        'P17_480_O': '%s, bay %i' % (ENC2, 7),
        'P18_480_O': '%s, bay %i' % (ENC2, 8),
        'P19_480_O': '%s, bay %i' % (ENC2, 9),
        'P20_480_O': '%s, bay %i' % (ENC2, 10),
        'P21_480_O': '%s, bay %i' % (ENC3, 1),
        'P22_480_O': '%s, bay %i' % (ENC3, 2),
        'P23_480_O': '%s, bay %i' % (ENC3, 3),
        'P24_480_O': '%s, bay %i' % (ENC3, 4),
        'P25_480_O': '%s, bay %i' % (ENC3, 5),
        'P26_480_O': '%s, bay %i' % (ENC3, 6),
        'P27_480_O': '%s, bay %i' % (ENC3, 7),
        'P28_480_O': '%s, bay %i' % (ENC3, 8),
        'P29_480_O': '%s, bay %i' % (ENC3, 9),
        'P30_480_O': '%s, bay %i' % (ENC3, 10),
        'P31_480_O': '%s, bay %i' % (ENC3, 11),
        'P32_480_O': '%s, bay %i' % (ENC3, 12),
        'P33_480_O': '%s, bay %i' % (ENC4, 7),
        'P34_480_O': '%s, bay %i' % (ENC4, 8),
        'P35_480_O': '%s, bay %i' % (ENC4, 9),
        'P36_480_O': '%s, bay %i' % (ENC4, 10),
        'P37_480_O': '%s, bay %i' % (ENC4, 11),
        'P38_480_O': '%s, bay %i' % (ENC4, 12),
        'P39_480_O': '%s, bay %i' % (ENC5, 1),
        'P40_480_O': '%s, bay %i' % (ENC5, 2),
        'P41_480_O': '%s, bay %i' % (ENC5, 3),
        'P42_480_O': '%s, bay %i' % (ENC5, 4),
        'P43_480_O': '%s, bay %i' % (ENC5, 5),
        'P44_480_O': '%s, bay %i' % (ENC5, 6),
        'P45_480_O': '%s, bay %i' % (ENC5, 7),
        'P46_480_O': '%s, bay %i' % (ENC5, 8),
        'P47_480_O': '%s, bay %i' % (ENC5, 9),
        'P48_480_O': '%s, bay %i' % (ENC5, 10),
        'P49_480_O': '%s, bay %i' % (ENC5, 11),
        'P50_480_O': '%s, bay %i' % (ENC5, 12),
        'P51_480_O': '%s, bay %i' % (ENC6, 1),
        'P52_480_O': '%s, bay %i' % (ENC6, 2),
        'P53_480_O': '%s, bay %i' % (ENC6, 3),
        'P54_480_O': '%s, bay %i' % (ENC6, 4),
        'P55_480_O': '%s, bay %i' % (ENC6, 5),
        'P56_480_O': '%s, bay %i' % (ENC6, 8),
        'P57_480_O': '%s, bay %i' % (ENC7, 1),
        'P58_480_O': '%s, bay %i' % (ENC7, 7),
        'P59_480_O': '%s, bay %i' % (ENC8, 1),
        'P60_480_O': '%s, bay %i' % (ENC8, 7),
        'P61_480_O': '%s, bay %i' % (ENC9, 1),
        'P62_480_O': '%s, bay %i' % (ENC9, 3),
        'P63_480_O': '%s, bay %i' % (ENC9, 4),
        #        'P64_480_O': '%s, bay %i' % (ENC9, 7),
        'P65_480_O': '%s, bay %i' % (ENC10, 1),
        'P66_480_O': '%s, bay %i' % (ENC10, 7),
        'P67_480_O': '%s, bay %i' % (ENC11, 3),
        'P68_480_O': '%s, bay %i' % (ENC11, 4),
        'P69_480_O': '%s, bay %i' % (ENC11, 7),
        'P70_480_O': '%s, bay %i' % (ENC11, 8),
        'P71_480_O': '%s, bay %i' % (ENC11, 11),
    }
)

ljbod = [
    {"name": "P3_jbod_ENC1_9_10", "type": SAS_LOGICAL_JBOD_TYPE, "description": "", "driveEnclosure": '%s, bay %i' % (ENC1, 1),
     "driveBayUris": ['9', '10'], "eraseData": False, "clearMetaData": False},
    {"name": "P4_jbod_ENC1_11_12", "type": SAS_LOGICAL_JBOD_TYPE, "description": "", "driveEnclosure": '%s, bay %i' % (ENC1, 1),
     "driveBayUris": ['11', '12'], "eraseData": False, "clearMetaData": False},
    {"name": "P5_jbod_ENC1_13_14", "type": SAS_LOGICAL_JBOD_TYPE, "description": "", "driveEnclosure": '%s, bay %i' % (ENC1, 1),
     "driveBayUris": ['13', '14'], "eraseData": False, "clearMetaData": False},
]


spts = {'SPT_480_1': {'type': SERVER_PROFILE_TEMPLATE_TYPE, 'serverProfileDescription': 'Server profile for SY 480 Gen10 1',
                      'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Virtual',
                      'macType': 'Physical', 'wwnType': 'Physical', 'name': 'BB_SPT1',
                      'description': 'Server Profile Template created from SY 480 Gen10 1', 'affinity': 'Bay',
                      'connectionSettings': {'connections': deepcopy(sp_eth_conns_234), 'manageConnections': True},
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


assigned_sps = [
    {
        # Profile 1 : Encl 1, Bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P1_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 3),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P1',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_567),
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
        'bios': {
            'manageBios': True,
            "overriddenSettings":
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbSas1Enable", "value": "Disabled"}
                 ]
        },
        'localStorage': {
            'controllers': [{"logicalDrives": [{"name": None,
                                                "raidLevel": "RAID0",
                                                "bootable": True,
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
                                 "name": "P1_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False},
                                ]},
    },  # Profile 1  MXQ825050L, Bay 3`

    {  # Profile 2 : Encl 1, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P2_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 4),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P2',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_234),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                                                "raidLevel": "RAID0",
                                                "bootable": True,
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
                                 "name": "P2_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 146,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False},
                                ]},
    },  # Profile 2  MXQ825050L, Bay 4

    {  # Profile 3 : Encl 1, Bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P3_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 5),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile 3',
        'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_eth_conns_678)},
        'bootMode': {'manageMode': True, 'mode': 'UEFI',
                     'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [{"id": 1,
                                 "deviceSlot": "Mezz 1",
                                 "name": "P3_jbod_ENC1_9_10",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "sasLogicalJBODUri": "sas-logical-jbod:P3_jbod_ENC1_9_10",
                                 "eraseData": False},
                                ]},

    },  # Profile 3  MXQ825050L, Bay 5

    {  # Profile 4 : Encl 1, Bay 6
        'type': SERVER_PROFILE_TYPE,
        'name': 'P4_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 6),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile 4',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_123),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
            'secureBoot': 'Unmanaged'
        },
        'boot': {
            'manageBoot': True,
            'order': ['HardDisk']
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
        'localStorage': {
            'sasLogicalJBODs': [{"id": 1,
                                 "deviceSlot": "Mezz 1",
                                 "name": "P4_jbod_ENC1_11_12",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "sasLogicalJBODUri": "sas-logical-jbod:P4_jbod_ENC1_11_12",
                                 "eraseData": False},
                                ]},

    },  # Profile 4  MXQ825050L, Bay 6

    {  # Profile 5 : Encl 1, bay 7
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 7),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'name': 'P5_480_O',
        'description': 'Server Profile 5',
        'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_eth_conns_345)},
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'secureBoot': 'Unmanaged'
        },
        'boot': {
            'manageBoot': True,
            'order': ['HardDisk']
        },
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'sasLogicalJBODs': [{"id": 1,
                                 "deviceSlot": "Mezz 1",
                                 "name": "P5_jbod_ENC1_13_14",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "sasLogicalJBODUri": "sas-logical-jbod:P5_jbod_ENC1_13_14",
                                 "eraseData": False},
                                ]}

    },  # Profile 5  MXQ825050L, Bay 7

    {  # Profile 6 : Encl 1, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P6_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 8),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P6',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_246),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [{"name": None,
                                                "raidLevel": "RAID0",
                                                "bootable": True,
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
                                 "name": "P6_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 146,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False},
                                ]},

    },  # Profile 6  MXQ825050L, Bay 8

    {  # Profile 7 : Encl 1, Bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P7_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 9),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P7',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_138),
        },
        'boot': {
            'manageBoot': True,
            "order": ["HardDisk"],
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'secureBoot': 'Unmanaged'
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [{"name": None,
                                                "raidLevel": "RAID0",
                                                "bootable": True,
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
                                 "name": "P7_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 146,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False},
                                ]},
    },  # Profile 7  MXQ825050L, Bay 9

    {  # Profile 8 : Encl 1, bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P8_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 10),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P8',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_131415),
        },
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto',
                     'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
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
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P8_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 146,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}

    },  # Profile 8  MXQ825050L, Bay 10

    {  # Profile 9 : Encl 1, Bay 11
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 11),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical', 'wwnType': 'Physical', 'name': 'P9_480_O',
        'description': 'Server Profile created from SY 480 Gen9 1', 'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_eth_conns_121314)},
        'bootMode': {'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto',
                     'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                     'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings": [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P9_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 146,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}
    },  # Profile 9  MXQ825050L, Bay 11

    {  # Profile 10 : Encl 1, bay 12
        'type': SERVER_PROFILE_TYPE,
        'name': 'P10_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC1, 12),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P10',
        'affinity': 'Bay',
        'connectionSettings': {'connections': deepcopy(sp_eth_conns_91011)},
        'bootMode': {'manageMode': True,
                     'mode': 'UEFI',
                     'secureBoot': 'Unmanaged'},
        'boot': {'manageBoot': True,
                 'order': ['HardDisk']},
        'firmware': {'manageFirmware': False,
                     'firmwareBaselineUri': '',
                     'forceInstallFirmware': False,
                     'firmwareInstallType': None,
                     'firmwareActivationType': 'Immediate'},
        'bios': {'manageBios': True,
                 "overriddenSettings":
                     [{"id": "IntelPerfMonitoring", "value": "Enabled"}]},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P10_jbod_ENC1",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 146,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}
    },  # Profile 10  MXQ825050L, Bay 12

    {  # Profile 11 : Encl 2, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P11_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 1),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P11',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_23),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P11_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P11_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },

    },  # Profile 11  MXQ825050C, Bay 1

    {  # Profile 12 : Encl 2, bay 2
        'type': SERVER_PROFILE_TYPE,
        'name': 'P12_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 2),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P12',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P12_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P12_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 12  MXQ825050C, Bay 2

    {  # Profile 13 : Encl 2, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P13_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 3),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P13',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_56),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P13_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P13_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 13  MXQ825050C, Bay 3

    {  # Profile 14 : Encl 2, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P14_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 4),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P14',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_910),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P14_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P14_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
    },  # Profile 14  MXQ825050C, Bay 4

    {  # Profile 15 : Encl 2, Bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P15_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 5),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P15',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_101112),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P15_boot_volume_Orchid',
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
                    'volumeUri': 'VolName:P15_data_volume_Orchid',
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

        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 15  MXQ825050C, Bay 5

    {  # Profile 16 : Encl 2, bay 6
        'type': SERVER_PROFILE_TYPE,
        'name': 'P16_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 6),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P16',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_246),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
            'manageBios': False,
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {'controllers': [],
                         'sasLogicalJBODs': []},
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
                            "name": "P16_boot_volume_Orchid",
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
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P16_data_volume_Orchid",
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
    },  # Profile 16  MXQ825050C, Bay 6

    {  # Profile 17 : Encl 2, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P17_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 7),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P17',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_23),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P17_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P17_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 17  MXQ825050C, Bay 7

    {  # Profile 18 : Encl 2, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P18_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 8),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P18',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P18_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P18_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 18  MXQ825050C, Bay 8

    {  # Profile 19 : Encl 2, bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P19_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 9),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P19',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_56),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P19_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P19_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbSas1Enable", "value": "Disabled"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 19  MXQ825050C, Bay 9

    {  # Profile 20 : Encl 2, bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P20_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC2, 10),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P20',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_45),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P20_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P20_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 20  MXQ825050C, Bay 10

    {  # Profile 21 : Encl 3, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P21_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 1),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P21',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P21_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P21_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 21  MXQ825050K, Bay 1

    {  # Profile 22 : Encl 3, bay 2
        'type': SERVER_PROFILE_TYPE,
        'name': 'P22_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 2),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P22',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_45),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P22_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P22_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 22  MXQ825050K, Bay 2

    {  # Profile 23 : Encl 3, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P23_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 3),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P23',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_67),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P23_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P23_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 23  MXQ825050K,

    {  # Profile 24 : Encl 3, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P24_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 4),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P24',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_28),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P24_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P24_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 24  MXQ825050K, Bay 4

    {  # Profile 25 : Encl 3, bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P25_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 5),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P25',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P25_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P25_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 25  MXQ825050K, Bay 5

    {  # Profile 26 : Encl 3, Bay 6
        'type': SERVER_PROFILE_TYPE,
        'name': 'P26_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 6),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P26',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_456),
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
                            "name": "P26_boot_volume_Orchid",
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
                    'volumeUri': None,
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
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P26_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
            'mode': 'UEFI',
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 26  MXQ825050K, Bay 6

    {  # Profile 27 : Encl 3, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P27_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 7),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P27',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_67),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P27_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P27_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 27  MXQ825050K, Bay 7

    {  # Profile 28 : Encl 3, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P28_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 8),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P28',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_67),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P28_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P28_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 28  MXQ825050K, Bay 8

    {  # Profile 29 : Encl 3, bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P29_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 9),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P29',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_28),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P29_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P29_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 29  MXQ825050K, Bay 9

    {  # Profile 30 : Encl 3, bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P30_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 10),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P30',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P30_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P30_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 30  MXQ825050K, Bay 10

    {  # Profile 31 : Encl 3, bay 11
        'type': SERVER_PROFILE_TYPE,
        'name': 'P31_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 11),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P31',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_28),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P31_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P31_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 31  MXQ825050K, Bay 11

    {  # Profile 32 : Encl 3, Bay 12
        'type': SERVER_PROFILE_TYPE,
        'name': 'P32_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC3, 12),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P32',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_123),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P32_boot_volume_Orchid',
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
                    'volumeUri': 'VolName:P32_data_volume_Orchid',
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
            'mode': 'BIOS',
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"},
            ]
        },
    },  # Profile 32  MXQ825050K, Bay 12

    {  # Profile 33 : Encl 4, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P33_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC4, 7),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serverProfileTemplateUri': 'SPT:%s' % spts['SPT_480_1']['name'],
        'description': 'Server Profile P33',
        'affinity': 'Bay',
        'bios': {
            'manageBios': True,
            "overriddenSettings":
                [{"id": "IntelPerfMonitoring", "value": "Enabled"}]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
    },  # Profile 33  MXQ825050D, Bay 7

    {  # Profile 34 : Encl 4, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P34_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC4, 8),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P34',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_678),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P34_jbod_ENC4",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}
    },  # Profile 34  MXQ825050D, Bay 8

    {  # Profile 35 : Encl 4, bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P35_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC4, 9),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P35',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_281),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P35_jbod_ENC4",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}
    },  # Profile 35  MXQ825050D, Bay 9

    {  # Profile 36 : Encl 4, bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P36_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC4, 10),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P36',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_123),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P36_jbod_ENC4",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}
    },  # Profile 36  MXQ825050D, Bay 10

    {  # Profile 37 : Encl 4, bay 11
        'type': SERVER_PROFILE_TYPE,
        'name': 'P37_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC4, 11),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P37',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_281),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        'localStorage': {
            'controllers': [{"logicalDrives": [
                {"name": None,
                 "raidLevel": "RAID0",
                 "bootable": True,
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
                                 "name": "P37_jbod_ENC4",
                                 "numPhysicalDrives": 2,
                                 "driveMinSizeGB": 300,
                                 "driveMaxSizeGB": 300,
                                 "driveTechnology": "SasHdd",
                                 "eraseData": False}
                                ]}
    },  # Profile 37  MXQ825050D, Bay 11

    {  # Profile 38 : Encl 4, Bay 12
        'type': SERVER_PROFILE_TYPE,
        'name': 'P38_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC4, 12),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P38',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_123),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P38_boot_volume_Orchid',
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
                    'volumeUri': 'VolName:P38_data_volume_Orchid',
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
            'mode': 'BIOS',
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"},
                {"id": "EmbSas1Enable", "value": "Disabled"}
            ]
        },
    },  # Profile 38  MXQ825050D, Bay 12

    {  # Profile 39 : Encl 5, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P39_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 1),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P39',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_67),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P39_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P39_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 39  MXQ825050F, Bay 1

    {  # Profile 40 : Encl 5, bay 2
        'type': SERVER_PROFILE_TYPE,
        'name': 'P40_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 2),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P40',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_67),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P40_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P40_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 40  MXQ825050F, Bay 2

    {  # Profile 41 : Encl 5, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P41_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 3),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P41',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_78),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P41_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P41_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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


    },  # Profile 41  MXQ825050F, Bay 3

    {  # Profile 42 : Encl 5, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P42_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 4),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P42',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P42_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P42_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 42  MXQ825050F, Bay 4

    {  # Profile 43 : Encl 5, Bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P43_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 5),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P43',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_23),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P43_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P43_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
                {"id": "IntelPerfMonitoring", "value": "Enabled"},
                {"id": "EmbSas1Enable", "value": "Disabled"}
            ]
        },
    },  # Profile 43  MXQ825050F, Bay 5

    {  # Profile 44 : Encl 5, Bay 6
        'type': SERVER_PROFILE_TYPE,
        'name': 'P44_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 6),
        'enclosureGroupUri': 'EG:%s' % EG1,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P44',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_246),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P44_boot_volume_Orchid',
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
                    'volumeUri': None,
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
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P44_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 44  MXQ825050F, Bay 6

    {  # Profile 45 : Encl 5, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P45_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 7),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P45',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_28),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P45_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P45_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 45  MXQ825050F, Bay 7

    {  # Profile 46 : Encl 5, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P46_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 8),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P46',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P46_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P46_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 46  MXQ825050F, Bay 8

    {  # Profile 47 : Encl 5, bay 9
        'type': SERVER_PROFILE_TYPE,
        'name': 'P47_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 9),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P47',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_45),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P47_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P47_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 47  MXQ825050F, Bay 9

    {  # Profile 48 : Encl 5, bay 10
        'type': SERVER_PROFILE_TYPE,
        'name': 'P48_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 10),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P48',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_28),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P48_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P48_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 48  MXQ825050F, Bay 10

    {  # Profile 49 : Encl 5, bay 11
        'type': SERVER_PROFILE_TYPE,
        'name': 'P49_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 11),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P49',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_38),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P49_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P49_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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

    },  # Profile 49 : Encl 5, bay 11

    {  # Profile 50 : Encl 5, bay 12
        'type': SERVER_PROFILE_TYPE,
        'name': 'P50_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC5, 12),
        'enclosureGroupUri': 'EG:%s' % EG1, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P50',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_12),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P50_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P50_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 50  MXQ825050F, Bay 12

    {  # Profile 51 : Encl 6, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P51_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC6, 1),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P51',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_89),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P51_iscsi_boot_volume_Orchid",
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
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P51_iscsi_data_volume_Orchid",
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
                       }

    },  # Profile 51  MXQ825050G, Bay 1

    {  # Profile 52 : Encl 6, bay 2
        'type': SERVER_PROFILE_TYPE,
        'name': 'P52_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC6, 2),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P52',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_1011),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P52_iscsi_boot_volume_Orchid",
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
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P52_iscsi_data_volume_Orchid",
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
                                                 }
                                                ]
                       },
    },  # Profile 52  MXQ825050G, Bay 2

    {  # Profile 53 : Encl 6, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P53_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC6, 3),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P53',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_678),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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

    },  # Profile 53  MXQ825050G, Bay 3

    {  # Profile 54 : Encl 6, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P54_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC6, 4),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P54',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_1112),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P54_iscsi_boot_volume_Orchid",
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
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P54_iscsi_data_volume_Orchid",
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
                       }
    },  # Profile 54  MXQ825050G, Bay 4

    {  # Profile 55 : Encl 6, bay 5
        'type': SERVER_PROFILE_TYPE,
        'name': 'P55_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC6, 5),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Virtual',
        'description': 'Server Profile P55',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_eth_conns_345),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 55  MXQ825050G, Bay 5

    {  # Profile 56 : Encl 6, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P56_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC6, 8),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P56',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_1213),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P56_iscsi_boot_volume_Orchid",
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
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P56_iscsi_data_volume_Orchid",
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
                       }
    },  # Profile 56  MXQ825050G, Bay 8

    {  # Profile 57 : Encl 7, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P57_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC7, 1),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P57',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_1314),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': "SVOL:P57_boot_volume_iscsi_orchid",
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
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
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P57_iscsi_data_volume_orchid",
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
                       }
    },  # Profile 57  MXQ825050J, Bay 1

    {  # Profile 58 : Encl 7, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P58_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC7, 7),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P58',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_1617),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P58_iscsi_boot_volume_Orchid",
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
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P58_iscsi_data_volume_Orchid",
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
                       }
    },  # Profile 58  MXQ825050J, Bay 7

    {  # Profile 59 : Encl 8, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P59_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC8, 1),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P59',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_1415),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P59_iscsi_boot_volume_Orchid",
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
                                              },
                                             {'id': 2,
                                              'volumeUri': None,
                                              "lunType": "Auto",
                                              'isBootVolume': False,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []
                                                                },
                                                               ],
                                              "bootVolumePriority": "NotBootable",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              "volume": {"properties": {"name": "P59_iscsi_data_volume_Orchid",
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
                       }
    },  # Profile 59  MXQ825050H, Bay 1

    {  # Profile 60 : Encl 8, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P60_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC8, 7),
        'enclosureGroupUri': 'EG:%s' % EG2, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P60',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_iscsi_conns_78),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',
        "sanStorage": {"hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
                       "manageSanStorage": True,
                       "volumeAttachments": [{'id': 1,
                                              'volumeUri': "SVOL:P60_boot_volume_iscsi_orchid",
                                              "lunType": "Auto",
                                              'isBootVolume': True,
                                              'storagePaths': [{'isEnabled': True,
                                                                'connectionId': 4,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               {'isEnabled': True,
                                                                'connectionId': 8,
                                                                'targetSelector': 'Auto',
                                                                'targets': []},
                                                               ],
                                              "bootVolumePriority": "Primary",
                                              "volumeStorageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                              },
                                             ],
                       "sanSystemCredentials": [{"storageSystemUri": "SSYS:" + STOREVIRTUAL_NAME,
                                                 "chapLevel": "None"
                                                 },
                                                ]
                       }
    },  # Profile 60  MXQ825050H, Bay 7

    {  # Profile 61 : Encl 9, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P61_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC9, 1),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P61',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_1516),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P61_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P61_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 61  MXQ80805Q4, Bay 1

    {  # Profile 62 : Encl 9, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P62_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC9, 3),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P62',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_1617),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P62_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P62_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 62  MXQ80805Q4, Bay 3

    {  # Profile 63 : Encl 6, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P63_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC9, 4),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P63',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_23),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P63_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P63_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,

    },  # Profile 63  MXQ80805Q4, Bay 4

    {  # Profile 65 : Encl 10, bay 1
        'type': SERVER_PROFILE_TYPE,
        'name': 'P65_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC10, 1),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P65',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_23),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P65_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P65_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 65  MXQ80805PZ, Bay 1

    {  # Profile 66 : Encl 10, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P66_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC10, 7),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P66',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_56),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P66_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P66_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 66  MXQ80805PZ, Bay 7

    {  # Profile 67 : Encl 11, bay 3
        'type': SERVER_PROFILE_TYPE,
        'name': 'P67_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC11, 3),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P67',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_678),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P67_boot_volume_Orchid',
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
                    'volumeUri': 'VolName:P67_data_volume_Orchid',
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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


    },  # Profile 67  MXQ80805Q0, Bay 3

    {  # Profile 68 : Encl 11, bay 4
        'type': SERVER_PROFILE_TYPE,
        'name': 'P68_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC11, 4),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P68',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_151617),
        },
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P68_boot_volume_Orchid',
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
                    'volumeUri': None,
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
                    ],
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P68_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
                            "provisioningType": "Thin",
                            "isShareable": False,
                            "storagePool": "SP:" + STORESERV_POOL1
                        },
                        "isPermanent": False,
                        "templateUri": 'ROOT:' + STORESERV_POOL1,
                    },
                },

            ],

        }
    },  # Profile 68  MXQ80805Q0, Bay 4

    {  # Profile 69 : Encl 11, bay 7
        'type': SERVER_PROFILE_TYPE,
        'name': 'P69_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC11, 7),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P69',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_67),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P69_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P69_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFIOptimized',
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

    },  # Profile 69  MXQ80805Q0, Bay 7

    {  # Profile 70 : Encl 11, bay 8
        'type': SERVER_PROFILE_TYPE,
        'name': 'P70_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC11, 8),
        'enclosureGroupUri': 'EG:%s' % EG3, 'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P70',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_28),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P70_boot_volume_Orchid',
                    "lunType": "Auto",
                    'isBootVolume': True,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ]
                },
                {
                    'id': 2,
                    'volumeUri': None,
                    "lunType": "Auto",
                    'isBootVolume': False,
                    'storagePaths': [
                        {
                            'isEnabled': True,
                            'connectionId': 4,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                        {
                            'isEnabled': True,
                            'connectionId': 8,
                            'targetSelector': 'Auto',
                            'targets': []
                        },
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P70_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
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
                [{"id": "IntelPerfMonitoring", "value": "Enabled"},
                 {"id": "EmbeddedSata", "value": "Raid"}
                 ]
        },
        'hideUnusedFlexNics': True,
        'iscsiInitiatorNameType': 'AutoGenerated',

    },  # Profile 70  MXQ80805Q0, Bay 8

    {  # Profile 71 : Encl 11, Bay 11
        'type': SERVER_PROFILE_TYPE,
        'name': 'P71_480_O',
        'serverHardwareUri': 'SH:%s, bay %i' % (ENC11, 11),
        'enclosureGroupUri': 'EG:%s' % EG3,
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'description': 'Server Profile P71',
        'affinity': 'Bay',
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': '',
            'forceInstallFirmware': False,
            'firmwareInstallType': None
        },
        'connectionSettings': {
            'connections': deepcopy(sp_fc_eth_conns_281),
        },
        "sanStorage": {
            "hostOSType": "VMware (ESXi)",
            "manageSanStorage": True,
            "volumeAttachments": [
                {
                    'id': 1,
                    "bootVolumePriority": "Primary",
                    'volumeUri': 'VolName:P71_boot_volume_Orchid',
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
                    'volumeUri': None,
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
                    ],
                    "bootVolumePriority": "NotBootable",
                    "volumeStorageSystemUri": "SSYS:" + STORESERV_NAME,
                    "volume": {
                        "properties": {
                            "name": "P71_data_volume_Orchid",
                            "description": "",
                            "size": 1073741824,
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
            'mode': 'UEFI',
        },
        'bios': {
            'manageBios': True,
            "overriddenSettings": [
                {"id": "IntelPerfMonitoring", "value": "Enabled"}
            ]
        },
    },  # Profile 71  MXQ80805Q0, Bay 11
]

FLM_IPv6 = ["fe80::9af2:b3ff:fe24:bae0", "fe80::9af2:b3ff:fe23:63e8"]

# Added for FLT
ENCLOSURES_MGRBays = [{'MXQ80805Q4': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC11},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC10},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ80805Q0': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC10},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC9},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ80805PZ': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC9},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC11},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050C': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC1},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC3},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050L': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC8},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC2},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050H': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC7},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC1},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050J': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC6},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC8},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050G': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC5},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC7},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050F': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC4},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC6},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050D': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC3},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC5},
                                       'mgmtPortLinkState': 'Unlinked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},
                      {'MXQ825050K': [{'bayNumber': 1,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 2, 'serialNumber': ENC2},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'},
                                      {'bayNumber': 2,
                                       'linkPortState': 'Linked',
                                       'linkPortStatus': 'OK',
                                       'linkedEnclosure': {'bayNumber': 1, 'serialNumber': ENC4},
                                       'mgmtPortLinkState': 'Linked',
                                       'mgmtPortStatus': 'OK',
                                       'status': 'OK'}, ]},

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

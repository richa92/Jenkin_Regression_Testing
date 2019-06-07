from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

CONFIG = '3frame'

SSH_PASS = 'hpvse1'
interface = 'bond0'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
             [{'device': 'eth0',
               'macAddress': None,
               'interfaceName': 'vLAN101',
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
               'hostname': 'AR51-3ENCS.us.rdlabs.hpecorp.net',
               'confOneNode': True,
               'domainName': 'us.rdlabs.hpecorp.net',
               'aliasDisabled': True,
               }],
             }

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hp.net'], 'locale': 'en_US.UTF-8'}

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
#FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

#EG = '3enc-dualibs-EG'
EG = 'Enc3-ibs23-EG'
EG2 = 'EG2'
EG3 = 'EG3'

ENC1 = 'CN754406W7'
ENC2 = 'CN7544044C'
ENC3 = 'CN754406WT'

ENC1_BAY1_IP = '192.169.0.101'
ENC1_BAY1 = '%s, bay 1' % ENC1
ENC1_BAY4_IP = '192.169.0.103'
ENC1_BAY4 = '%s, bay 3' % ENC1
ENC2_BAY1_IP = '192.169.0.101'
ENC2_BAY1 = '%s, bay 1' % ENC2
ENC2_BAY4_IP = '192.169.0.103'
ENC2_BAY4 = '%s, bay 3' % ENC2
ENC3_BAY1_IP = '192.169.0.101'
ENC3_BAY1 = '%s, bay 1' % ENC3
ENC3_BAY4_IP = '192.169.0.103'
ENC3_BAY4 = '%s, bay 3' % ENC3

GW_IP = '192.169.0.1'

PING_LIST_1 = [ENC1_BAY1_IP, ENC1_BAY4_IP]
PING_LIST_3 = [ENC1_BAY1_IP, GW_IP]

SERVERS = [ENC1_BAY1, ENC1_BAY4, ENC2_BAY1, ENC2_BAY4, ENC3_BAY1, ENC3_BAY4]

LE = '3enc-dualibs-le'
LE2 = 'LE2'
LE3 = 'LE3'

LIG1 = '3enc-ha-cl20-ibs3-lig'
LIG2 = '3enc-Aside-cl10-ibs2-lig'
LIG3 = '3enc-Bside-cl10-ibs2-lig'

ranges = [{'name': 'FCOE-MAC', 'type': 'Range', 'category': 'id-range-VMAC', 'rangeCategory': 'CUSTOM',
           'startAddress': '00:BB:58:00:00:00', 'endAddress': '00:BB:58:00:00:BF', 'enabled': True},
          {'name': 'FCOE-WWN', 'type': 'Range', 'category': 'id-range-VWWN', 'rangeCategory': 'CUSTOM',
           'startAddress': '21:11:BB:58:00:00:00:00', 'endAddress': '21:11:BB:58:00:00:00:BF', 'enabled': True},
          {'name': 'FCOE-SN', 'type': 'Range', 'category': 'id-range-VSN', 'rangeCategory': 'CUSTOM',
           'startAddress': 'VCUAAAAAAA', 'endAddress': 'VCUAAAAADT', 'enabled': True}]

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

ethernet_networks = [{'name': 'net_401',
                      'type': 'ethernet-networkV300',
                      'vlanId': 401,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_402',
                      'type': 'ethernet-networkV300',
                      'vlanId': 402,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_403',
                      'type': 'ethernet-networkV300',
                      'vlanId': 403,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_404',
                      'type': 'ethernet-networkV300',
                      'vlanId': 404,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_405',
                      'type': 'ethernet-networkV300',
                      'vlanId': 405,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_406',
                      'type': 'ethernet-networkV300',
                      'vlanId': 406,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_407',
                      'type': 'ethernet-networkV300',
                      'vlanId': 407,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_408',
                      'type': 'ethernet-networkV300',
                      'vlanId': 408,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_409',
                      'type': 'ethernet-networkV300',
                      'vlanId': 409,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_410',
                      'type': 'ethernet-networkV300',
                      'vlanId': 410,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'tunnelnetwork1',
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

ethernet_ranges = [
    {'prefix': 'net_', 'suffix': '', 'start': 411, 'end': 599, 'name': None, 'type': 'ethernet-networkV300',
     'vlanId': None, 'purpose': 'General', 'smartLink': False, 'privateNetwork': False, 'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'}
    ]

network_sets = [{'name': 'fvtnetworkset1', 'type': 'network-setV300', 'networkUris': ['net_405','net_406','net_407','net_408','net_409','net_410','net_411','net_412','net_413','net_414'], 'nativeNetworkUri': None}]

fcoe_networks = [{'name': 'fcoenetwork1002', 'type': 'fcoe-networkV300', 'vlanId': 1002},
                 {'name': 'fcoenetwork1003', 'type': 'fcoe-networkV300', 'vlanId': 1003}]


###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
###

Enc2bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

###
# Interconnect bays configurations
###
# 3 Enclosures, Fabric 2
Enc3bay2ICMMap = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

# 3 Enclosures, Fabric 3
Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

uplink_set = {
    'bay3-fcoe1002-us': {
    'name': 'bay3-fcoe1002-us',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['fcoenetwork1002'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'}
    ]
    },
    'bay6-fcoe1003-us': {
    'name': 'bay6-fcoe1003-us',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['fcoenetwork1003'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'}
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
        {'enclosure': '1', 'bay': '3', 'port': 'Q3.3', 'speed': 'Auto'}
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
        {'enclosure': '1', 'bay': '3', 'port': 'Q3.4', 'speed': 'Auto'}
    ]
    },
    'mlag1-enet4x-us': {
    'name': 'mlag1-enet4x-us',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_401','net_402'],
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
        {'enclosure': '2', 'bay': '6', 'port': 'Q2.4', 'speed': 'Auto'}
    ]
    },
    'mlag2-enet4x-us': {
    'name': 'mlag2-enet4x-us',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_403','net_404'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'},
        {'enclosure': '1', 'bay': '3', 'port': 'Q4.2', 'speed': 'Auto'},
        {'enclosure': '1', 'bay': '3', 'port': 'Q4.3', 'speed': 'Auto'},
        {'enclosure': '1', 'bay': '3', 'port': 'Q4.4', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}
    ]
    },
    'mlag3-enetQ-us': {
    'name': 'mlag3-enetQ-us',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_405','net_406','net_407','net_408','net_409','net_410','net_411','net_412','net_413','net_414'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
    ]
    },
    'bay2-enet4x-us': {
        'name': 'bay2-enet4x-us',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net_401', 'net_402'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '2', 'port': 'Q2.2', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '2', 'port': 'Q2.3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '2', 'port': 'Q2.4', 'speed': 'Auto'}
        ]
    },
    'bay5-enetQ-us': {
        'name': 'bay5-enetQ-us',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net_403', 'net_404'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
        ]
    }

}

###
# LIGs for 2 and 3 enclosure setups
###
ligs = [
    {'name': 'Enc2-ibs3-LIG',
     'type': 'logical-interconnect-groupV3',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc2bay3ICMMap,
     'enclosureIndexes': [1, 2],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [deepcopy(uplink_set['bay3-tunnel4xC-us'])],
     },
    {'name': 'Enc3-ibs2-LIG',
     'type': 'logical-interconnect-groupV3',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc3bay2ICMMap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 2,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [deepcopy(uplink_set['bay2-enet4x-us']),
                    deepcopy(uplink_set['bay5-enetQ-us'])
                    ]
     },
    {'name': 'Enc3-ibs3-LIG',
     'type': 'logical-interconnect-groupV3',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc3bay3ICMMap,
     'enclosureIndexes': [1, 2, 3],
     'interconnectBaySet': 3,
     'redundancyType': 'HighlyAvailable',
     'uplinkSets': [deepcopy(uplink_set['bay3-fcoe1002-us']),
                    deepcopy(uplink_set['bay6-fcoe1003-us']),
                    deepcopy(uplink_set['bay3-tunnel4xC-us']),
                    deepcopy(uplink_set['bay3-untagged4xC-us']),
                    deepcopy(uplink_set['mlag1-enet4x-us']),
                    deepcopy(uplink_set['mlag2-enet4x-us']),
                    deepcopy(uplink_set['mlag3-enetQ-us'])
                    ],
     }
]

enc_groups = {
    'Enc3-ibs2-EG':
        {'name': 'Enc3-ibs2-EG',
         'type': 'EnclosureGroupV400',
         'enclosureCount': 3,
         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         'stackingMode': 'Enclosure',
         'interconnectBayMappingCount': 6,
         'configurationScript': None,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs2-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs2-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
        'Enc3-ibs3-EG':
        {'name': 'Enc3-ibs3-EG',
         'type': 'EnclosureGroupV400',
         'enclosureCount': 3,
         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         'stackingMode': 'Enclosure',
         'interconnectBayMappingCount': 6,
         'configurationScript': None,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs3-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs3-LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc3-ibs23-EG':
        {'name': 'Enc3-ibs23-EG',
         'type': 'EnclosureGroupV400',
         'enclosureCount': 3,
         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         'stackingMode': 'Enclosure',
         'interconnectBayMappingCount': 6,
         'configurationScript': None,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs2-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs3-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs2-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-ibs3-LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         }
}

###
# All logical enclosures
###
les = {
    '3Frame-ibs23-LE':
        {'name': '3Frame-ibs23-LE',
         'enclosureUris': ['ENC:%s' % ENC1, 'ENC:%s' % ENC2, 'ENC:%s' % ENC3],
         'enclosureGroupUri': 'EG:Enc3-ibs23-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

server_profile_templates = [
    {'type': 'ServerProfileTemplateV2',
     'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:EG 1',
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'Profile1', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                      'requestedMbps': '2000', 'networkUri': 'ETH:IC',
                      'boot': {'priority': 'Primary'}},
                     #                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     #                                     'requestedMbps': '2000', 'networkUri': 'ETH:net_102',
                     #                                     'boot': {'priority': 'NotBootable'}},
                     ]},
]

"""
Maps sever profile to encl, bay.  First column: server profile name. Second column: Enclosure, bay #
"""
server_profile_to_bay_map = {'%sbay1' % ENC1: '%s, bay 1' % ENC1,
                             '%sbay2' % ENC1: '%s, bay 4' % ENC1,
                             '%sbay3' % ENC2: '%s, bay 1' % ENC2,
                             '%sbay1' % ENC2: '%s, bay 4' % ENC2,
                             '%sbay2' % ENC3: '%s, bay 1' % ENC3,
                             '%sbay6' % ENC3: '%s, bay 4' % ENC3
                             }


def make_server_profile_dict(name, mezz=3, serverHardwareUri=None, serverHardwareTypeUri=None, enclosureUri=None,
                             enclosureGroupUri=None):
    connections = [{'id': 1, 'name': 'conn-401-1a', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-a' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 2, 'name': 'conn-401-2a', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-a' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 3, 'name': 'conn-FCoE-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:1-b' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1002',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 4, 'name': 'conn-FCoE-2b', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:2-b' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1003',
                    'boot': {'priority': 'NotBootable'}},
#                   {'id': 4, 'name': 'conn-402-2b', 'functionType': 'FibreChannel', 'portId': 'Mezz %s:2-b' % mezz,
#                    'requestedMbps': '2500', 'networkUri': 'FCOE:net_402',
#                    'boot': {'priority': 'NotBootable'}},
#                   {'id': 5, 'name': 'conn-403-1c', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-c' % mezz,
#                    'requestedMbps': '2500', 'networkUri': 'ETH:net_403',
#                    'boot': {'priority': 'NotBootable'}},
#                   {'id': 6, 'name': 'conn-404-2c', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-c' % mezz,
#                    'requestedMbps': '2500', 'networkUri': 'ETH:net_404',
#                    'boot': {'priority': 'NotBootable'}},
                   {'id': 5, 'name': 'conn-untag-1c', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-c' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:untaggednetwork1',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 6, 'name': 'conn-tunnel-2c', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-c' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnetwork1',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 7, 'name': 'conn-netset-1d', 'functionType': 'Ethernet', 'portId': 'Mezz %s:1-d' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
                    'boot': {'priority': 'NotBootable'}},
                   {'id': 8, 'name': 'conn-netset-2d', 'functionType': 'Ethernet', 'portId': 'Mezz %s:2-d' % mezz,
                    'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
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


def ENCprofiles(enc, eg='EG', count=13):
    return [['%s profile%s' % (enc, N), '%s, bay %s' % (enc, N), '', 'ENC:%s' % enc, 'EG:%s' % eg] for N in
            xrange(1, count)]


profiles = [['%sbay1' % ENC1, 3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
            ['%sbay2' % ENC1, 3, None, 'SY 480 Gen9 1', None, 'EG:%s' % EG],
            ['%sbay3' % ENC2, 3, None, 'SY 480 Gen9 2', None, 'EG:%s' % EG],
            ['%sbay1' % ENC2, 3, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG],
            ['%sbay2' % ENC3, 3, None, 'SY 480 Gen9 2', None, 'EG:%s' % EG],
            ['%sbay6' % ENC3, 3, None, 'SY 660 Gen9 1', None, 'EG:%s' % EG]
            ]

server_profiles_nohw = build_profiles(profiles)

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': None, 'enclosureUri': 'ENC:' + ENC1,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay1_SP', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [
                        {'id': 1, 'name': 'conn-401-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': 'conn-401-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 3, 'name': 'conn-FCoE-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1002',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 4, 'name': 'conn-FCoE-2b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1003',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 5, 'name': 'conn-403-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_403',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 6, 'name': 'conn-404-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_404',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 7, 'name': 'conn-netset-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                         'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 8, 'name': 'conn-netset-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                         'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                    ]
                    },
                   {'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 4',
                    'serverHardwareTypeUri': None, 'enclosureUri': 'ENC:' + ENC1,
                    'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay4_SP', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [
                        {'id': 1, 'name': 'conn-401-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 2, 'name': 'conn-401-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_401',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 3, 'name': 'conn-402-2b', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                         'requestedMbps': '2500', 'networkUri': 'ETH:net_402',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 4, 'name': 'conn-untag-1c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                         'requestedMbps': '2500', 'networkUri': 'ETH:untaggednetwork1',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 5, 'name': 'conn-tunnel-2c', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                         'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnetwork1',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 6, 'name': 'conn-netset-1d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                         'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                        {'id': 7, 'name': 'conn-netset-2d', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                         'requestedMbps': '2500', 'networkUri': 'NS:fvtnetworkset1',
                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                    ]
                    }
                   ]

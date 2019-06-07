from copy import deepcopy

import subprocess
import sys

FUSION_USERNAME = 'Administrator'  # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'  # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'  # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'  # Fusion SSH Password
# FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180  # Timeout.  Move this out???
FUSION_NIC = 'bond0'  # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

ENC_1 = 'CN754406W6'
ENC_2 = 'CN754XXXXX'
ENC_3 = 'CN754XXXXX'
ENC_4 = 'CN754XXXXX'
ENC_5 = 'CN754XXXXX'


def make_range_list(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


def rlist(start, end, prefix='net_', suffix=''):
    tlist = []
    for x in xrange(start, end + 1):
        tlist.append(prefix + str(x) + suffix)
    return tlist


SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# admin_credentials_TB = {'userName': 'Administrator', 'password': 'hpvse123'}

# serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}
#
# network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}
#
# backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}
#
# readonly_user = {'userName': 'readonly', 'password': 'readonly'}
#
# vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}
#
# appliance = {'type': 'ApplianceNetworkConfiguration',
#              'applianceNetworks':
#                  [{'device': 'eth0',
#                    'macAddress': None,
#                    'interfaceName': 'VLAN 106',
#                    'activeNode': '1',
#                    'unconfigure': False,
#                    'ipv4Type': 'DHCP',
#                    'ipv6Type': 'UNCONFIGURE',
#                    'hostname': 'portmon.usa.hp.com',
#                    'confOneNode': True,
#                    'domainName': 'usa.hp.com',
#                    'aliasDisabled': True}]}
#
# timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
          'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}], 'emailAddress': 'sarah@hp.com',
          'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
          'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}], 'emailAddress': 'nat@hp.com',
          'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
          'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}], 'emailAddress': 'backup@hp.com',
          'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True},
         {'userName': 'Readonly', 'password': 'readonly', 'fullName': 'readonly',
          'permissions': [{'roleName': 'Read only', 'scopeUri': None}], 'emailAddress': 'rheid@hp.com',
          'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True},
         {'userName': 'Storageonly', 'password': 'storageonly', 'fullName': 'storageadmin',
          'permissions': [{'roleName': 'Storage administrator', 'scopeUri': None}], 'emailAddress': 'rheid@hp.com',
          'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True},
         {'userName': 'FullRole', 'password': 'fullroleonly', 'fullName': 'fullroleadmin',
          'permissions': [{'roleName': 'Infrastructure administrator', 'scopeUri': None}],
          'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions', 'enabled': True},
         {'userName': 'Software', 'password': 'softwareonly', 'fullName': 'softwareadmin',
          'permissions': [{'roleName': 'Software administrator', 'scopeUri': None}], 'emailAddress': 'rheid@hp.com',
          'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, }
         ]

usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            {'userName': 'Readonly', 'password': 'readonly'},
            {'userName': 'Storageonly', 'password': 'storageonly'},
            {'userName': 'FullRole', 'password': 'fullroleonly'},
            {'userName': 'Software', 'password': 'softwareonly'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            ]

POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'readonly']

# licenses = [{'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
#            {'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
#            ]

# ethernet_networks = [{'name': 'net_100', 'type': 'ethernet-networkV300', 'vlanId': 100, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
#                      {'name': 'net_101', 'type': 'ethernet-networkV300', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
#                      {'name': 'net_102', 'type': 'ethernet-networkV300', 'vlanId': 102, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

ethernet_networks = [
    {'name': 'net_400',
     'type': 'ethernet-networkV4',
     'vlanId': 400,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_401',
     'type': 'ethernet-networkV4',
     'vlanId': 401,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_402',
     'type': 'ethernet-networkV4',
     'vlanId': 402,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_403',
     'type': 'ethernet-networkV4',
     'vlanId': 403,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_404',
     'type': 'ethernet-networkV4',
     'vlanId': 404,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_405',
     'type': 'ethernet-networkV4',
     'vlanId': 405,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_406',
     'type': 'ethernet-networkV4',
     'vlanId': 406,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_407',
     'type': 'ethernet-networkV4',
     'vlanId': 407,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_408',
     'type': 'ethernet-networkV4',
     'vlanId': 408,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_409',
     'type': 'ethernet-networkV4',
     'vlanId': 409,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net_410',
     'type': 'ethernet-networkV4',
     'vlanId': 410,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'tunnelnetwork1',
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
     'ethernetNetworkType': 'Untagged'},
]

network_sets = [
    {'name': 'netsetEnet', 'type': 'network-setV4', 'networkUris': rlist(401, 403, prefix='net_'),
     'nativeNetworkUri': 'net_401'},
]

fcoe_networks = [{'name': 'fcoenetwork1004', 'type': 'fcoe-networkV4', 'vlanId': 1004}]

###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

# enc_group_TB = {'enc_group1':
#               {'name': 'EG1',
#                'type': 'EnclosureGroupV400',
#                'enclosureCount': 2,
#                'enclosureTypeUri': '/rest/enclosure-types/SY12000',
#                'stackingMode': 'Enclosure',
#                'interconnectBayMappingCount': 0,
#                'configurationScript': None,
#                'interconnectBayMappings':
#                [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
#                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
#                 ],
#                'ipAddressingMode': 'External',
#                'ipRangeUris': [],
#                'powerMode': 'RedundantPowerFeed'
#                }}

enc_group1 = [{'name': 'EG1',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]},
              {'name': 'EG2',
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [{'hostname': '15.199.229.76', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG1',
         'force': 'true', 'licensingIntent': 'OneViewNoiLO'},
        {'hostname': '15.199.229.79', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG2',
         'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]

LIG3 = 'LIG2'
BAY = '1'

uplink_set = {
    'us-enet-Bside': {
        'name': 'us-enet-Bside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(409, 410, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '6', 'port': 'Q6.3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '6', 'port': 'Q6.4', 'speed': 'Auto'}
        ]
    },
    'us-fcoe-enet-Aside': {
        'name': 'us-fcoe-enet-Aside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoenetwork1004', 'net_400', 'net_401', 'net_402', 'net_403', 'net_404'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}
        ]
    },
    'us-nofcoe-enet-Aside': {
        'name': 'us-nofcoe-enet-Aside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net_400', 'net_401', 'net_402', 'net_403', 'net_404'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}
        ]
    },
    'us-fcoe-enet-Aside-1port': {
        'name': 'us-fcoe-enet-Aside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoenetwork1004', 'net_400', 'net_401', 'net_402', 'net_403', 'net_404'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}
        ]
    },
    'us-enet-Aside': {
        'name': 'us-enet-Aside',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(406, 407, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.1', 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': 'Q6.2', 'speed': 'Auto'}
        ]
    },

}

li_edit_uplinkset = {
    # 'us-fcoe-enet-Aside': {
    #     'name': 'us-fcoe-enet-Aside',
    #     'type': 'uplink-setV5',
    #     'ethernetNetworkType': 'Tagged',
    #     'networkType': 'Ethernet',
    #     'networkUris': ['net_400', 'net_401', 'net_402', 'net_403'],
    #     'fcNetworkUris': [],
    #     'fcoeNetworkUris': ['fcoenetwork1004'],
    #     'manualLoginRedistributionState': 'NotSupported',
    #     'lacpTimer': 'Long',
    #     'connectionMode': 'Auto',
    #     'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q3', 'desiredSpeed': 'Auto'},
    #                         ],
    #     'logicalInterconnectUri': 'QoS-LE1-Enc1-LIG'
    # },
    'us-fcoe-enet-Aside':
        {'name': 'us-fcoe-enet-Aside',
         'ethernetNetworkType': 'Tagged',
         'networkType': 'Ethernet',
         'networkUris': ['net_400', 'net_401', 'net_402', 'net_403', 'net_403'],
         'fcNetworkUris': [],
         'fcoeNetworkUris': ['fcoenetwork1004'],
         'lacpTimer': 'Short',
         'logicalInterconnectUri': None,
         'primaryPortLocation': None,
         'manualLoginRedistributionState': 'NotSupported',
         'connectionMode': 'Auto',
         'nativeNetworkUri': None,
         'portConfigInfos': [{'enclosure': ENC_1, 'bay': '3', 'port': 'Q3', 'desiredSpeed': 'Auto'},
                             ],
         },
}

ligs_noUplinkSets = {
    'Enc1-LIG': {
        'name': 'Enc1-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
        ],
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'qosConfiguration': None,
        'uplinkSets': [
        ],
    },
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
        ],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [
        ],
    },
    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [
        ],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [
        ],
    }
}

ligs = {
    'Enc1-LIG': {
        'name': 'Enc1-LIG',
        'interconnectMapTemplate': [
            {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
        ],
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'qosConfiguration': None,
        'uplinkSets': [
            deepcopy(uplink_set['us-fcoe-enet-Aside']),
            #            deepcopy(uplink_set['us-enet-Bside'])
        ],
    },
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            deepcopy(uplink_set['us-fcoe-enet-Aside']),
            #            deepcopy(uplink_set['us-enet-Bside'])
        ],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [
            deepcopy(uplink_set['us-fcoe-enet-Aside']),
            #            deepcopy(uplink_set['us-enet-Bside'])
        ],
    },
    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [
            deepcopy(uplink_set['us-fcoe-enet-Aside']),
            #            deepcopy(uplink_set['us-enet-Bside'])
        ],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'uplinkSets': [
            deepcopy(uplink_set['us-fcoe-enet-Aside']),
            #            deepcopy(uplink_set['us-enet-Bside'])
        ],
    }
}

edit_ligs = {
    'Enc1-LIG-AddUplinkset': {
        'ligBody': {
            'name': 'Enc1-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'qosConfiguration': None,
            'uplinkSets': [
                deepcopy(uplink_set['us-fcoe-enet-Aside']),
                deepcopy(uplink_set['us-enet-Bside']),
                deepcopy(uplink_set['us-enet-Aside'])
            ],
        },
    },
    'Enc1-LIG-EditUplinkset': {
        'ligBody': {
            'name': 'Enc1-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'qosConfiguration': None,
            'uplinkSets': [
                deepcopy(uplink_set['us-fcoe-enet-Aside-1port']),
                deepcopy(uplink_set['us-enet-Bside'])
            ],
        },
    },

    'Enc1-LIG-deleteUplinkset': {
        'ligBody': {
            'name': 'Enc1-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'qosConfiguration': None,
            'uplinkSets': [
                deepcopy(uplink_set['us-fcoe-enet-Aside']),
                deepcopy(uplink_set['us-enet-Bside'])
            ],
        },
    },
    'Enc1-LIG-QoSwithFCoE': {
        'ligBody': {
            'name': 'Enc1-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'qosConfiguration': None,
            'uplinkSets': [
                deepcopy(uplink_set['us-fcoe-enet-Aside']),
                deepcopy(uplink_set['us-enet-Bside']),
                deepcopy(uplink_set['us-enet-Aside'])
            ],
        },
    },
    'Enc1-LIG-QoSwithoutFCoE': {
        'ligBody': {
            'name': 'Enc1-LIG',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
            ],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
            'qosConfiguration': None,
            'uplinkSets': [
                deepcopy(uplink_set['us-nofcoe-enet-Aside']),
                deepcopy(uplink_set['us-enet-Bside']),
                deepcopy(uplink_set['us-enet-Aside'])
            ],
        },
    },

}

ls = [{'logicalSwitch': {'name': 'LS-56xx',
                         'state': 'Active',
                         'status': None,
                         'description': None,
                         'uri': None,
                         'category': None,
                         'eTag': None,
                         'created': None,
                         'modified': None,
                         'type': 'logical-switchV300',
                         'switchMap': None,
                         'logicalSwitchGroupUri': 'LSG:LSG-56xx-1',
                         'switchCredentialConfiguration': [{'snmpV1Configuration': {'communityString': 'nexus'},
                                                            'snmpV3Configuration': {'authorizationProtocol': None,
                                                                                    'privacyProtocol': None,
                                                                                    'securityLevel': None},
                                                            'logicalSwitchManagementHost': '15.199.203.171',
                                                            'snmpVersion': 'SNMPv1', 'snmpPort': 161}]},
       'logicalSwitchCredentials': [{'connectionProperties': [{'propertyName': 'SshBasicAuthCredentialUser',
                                                               'value': 'admin',
                                                               'valueFormat': 'Unknown',
                                                               'valueType': 'String'},
                                                              {'propertyName': 'SshBasicAuthCredentialPassword',
                                                               'value': 'HPvse123', 'valueFormat': 'SecuritySensitive',
                                                               'valueType': 'String'}]}]},
      ]

ethnets = [
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "Net1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "Net2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    }
]

serveradmin_user = {"type": "UserAndPermissions", "userName": "serveradmin", "fullName": "serveradmin",
                    "password": "serveradmin", "emailAddress": "", "officePhone": "", "mobilePhone": "",
                    "enabled": True, "roles": ["Server administrator"]}

# enc_group = [
#     {'name': 'EG1',
#      'configurationScript': None,
#      'powerMode': 'RedundantPowerFeed',
#      'ipRangeUris': [],
#      'ipAddressingMode': 'DHCP',
#      'enclosureCount': 1,
#      'interconnectBayMappings':
#          [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG1'},
#           {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG1'}]
#      }
# ]

enc_group = {
    'Enc1-EG':
        {'name': 'Enc1-EG',
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc2-EG':
        {'name': 'Enc2-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc3-EG':
        {'name': 'Enc3-EG',
         'enclosureCount': 3,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc4-EG':
        {'name': 'Enc4-EG',
         'enclosureCount': 4,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc5-EG':
        {'name': 'Enc5-EG',
         'enclosureCount': 5,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         }
}

QoS_Fcoe = {
    'qosConfiguration': {
        'activeQosConfig': {
            'type': 'QosConfiguration',
            'configType': 'CustomWithFCoE',
            'qosTrafficClassifiers': [
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '50',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Best effort',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            1,
                            0
                        ],
                        'dscpClassMapping': [
                            'DSCP 10, AF11',
                            'DSCP 12, AF12',
                            'DSCP 14, AF13',
                            'DSCP 8, CS1',
                            'DSCP 0, CS0'
                        ]
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 1,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class1',
                        'enabled': True
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '5',
                        'egressDot1pValue': 4,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class2',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '9',
                        'egressDot1pValue': 6,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class3',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '12',
                        'egressDot1pValue': 7,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class4',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': 'fcoe',
                        'egressDot1pValue': 3,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'FCoE lossless',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            3
                        ],
                        'dscpClassMapping': []
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '30',
                        'egressDot1pValue': 2,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Medium',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            4,
                            3,
                            2
                        ],
                        'dscpClassMapping': [
                            'DSCP 18, AF21',
                            'DSCP 20, AF22',
                            'DSCP 22, AF23',
                            'DSCP 26, AF31',
                            'DSCP 28, AF32',
                            'DSCP 30, AF33',
                            'DSCP 34, AF41',
                            'DSCP 36, AF42',
                            'DSCP 38, AF43',
                            'DSCP 16, CS2',
                            'DSCP 24, CS3',
                            'DSCP 32, CS4'
                        ]
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 5,
                        'maxBandwidth': 10,
                        'realTime': True,
                        'className': 'Real time',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            5,
                            6,
                            7
                        ],
                        'dscpClassMapping': [
                            'DSCP 46, EF',
                            'DSCP 40, CS5',
                            'DSCP 48, CS6',
                            'DSCP 56, CS7'
                        ]
                    }
                }
            ],
            'uplinkClassificationType': 'DOT1P',
            'downlinkClassificationType': 'DOT1P_AND_DSCP',
            'name': None,
            'state': None,
            'description': None,
            'status': None,
            'eTag': None,
            'created': None,
            'modified': None,
            'category': 'qos-aggregated-configuration',
            'uri': None
        },
        'inactiveFCoEQosConfig': None,
        'inactiveNonFCoEQosConfig': None,
        'type': 'qos-aggregated-configuration',
        'name': None,
        'state': None,
        'status': None,
        'eTag': None,
        'modified': None,
        'created': None,
        'category': 'qos-aggregated-configuration',
        'uri': None
    }
}

QoS_Fcoe_MaxBW = {
    'qosConfiguration': {
        'activeQosConfig': {
            'type': 'QosConfiguration',
            'configType': 'CustomWithFCoE',
            'qosTrafficClassifiers': [
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '40',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 40,
                        'realTime': False,
                        'className': 'Best effort',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            1,
                            0
                        ],
                        'dscpClassMapping': [
                            'DSCP 10, AF11',
                            'DSCP 12, AF12',
                            'DSCP 14, AF13',
                            'DSCP 8, CS1',
                            'DSCP 0, CS0'
                        ]
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 1,
                        'maxBandwidth': 10,
                        'realTime': False,
                        'className': 'Class1',
                        'enabled': True
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '5',
                        'egressDot1pValue': 4,
                        'maxBandwidth': 5,
                        'realTime': False,
                        'className': 'Class2',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '9',
                        'egressDot1pValue': 6,
                        'maxBandwidth': 9,
                        'realTime': False,
                        'className': 'Class3',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '12',
                        'egressDot1pValue': 7,
                        'maxBandwidth': 12,
                        'realTime': False,
                        'className': 'Class4',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': 'fcoe',
                        'egressDot1pValue': 3,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'FCoE lossless',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            3
                        ],
                        'dscpClassMapping': []
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '20',
                        'egressDot1pValue': 2,
                        'maxBandwidth': 20,
                        'realTime': False,
                        'className': 'Medium',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            4,
                            3,
                            2
                        ],
                        'dscpClassMapping': [
                            'DSCP 18, AF21',
                            'DSCP 20, AF22',
                            'DSCP 22, AF23',
                            'DSCP 26, AF31',
                            'DSCP 28, AF32',
                            'DSCP 30, AF33',
                            'DSCP 34, AF41',
                            'DSCP 36, AF42',
                            'DSCP 38, AF43',
                            'DSCP 16, CS2',
                            'DSCP 24, CS3',
                            'DSCP 32, CS4'
                        ]
                    }
                },
                {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 5,
                        'maxBandwidth': 10,
                        'realTime': True,
                        'className': 'Real time',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [
                            5,
                            6,
                            7
                        ],
                        'dscpClassMapping': [
                            'DSCP 46, EF',
                            'DSCP 40, CS5',
                            'DSCP 48, CS6',
                            'DSCP 56, CS7'
                        ]
                    }
                }
            ],
            'uplinkClassificationType': 'DOT1P',
            'downlinkClassificationType': 'DOT1P_AND_DSCP',
            'name': None,
            'state': None,
            'description': None,
            'status': None,
            'eTag': None,
            'created': None,
            'modified': None,
            'category': 'qos-aggregated-configuration',
            'uri': None
        },
        'inactiveFCoEQosConfig': None,
        'inactiveNonFCoEQosConfig': None,
        'type': 'qos-aggregated-configuration',
        'name': None,
        'state': None,
        'status': None,
        'eTag': None,
        'modified': None,
        'created': None,
        'category': 'qos-aggregated-configuration',
        'uri': None
    }
}

QoS_NoFcoe = {'qosConfiguration': {
    'activeQosConfig': {
        'type': 'QosConfiguration',
        'configType': 'CustomNoFCoE',
        'downlinkClassificationType': 'DOT1P',
        'uplinkClassificationType': 'DSCP',
        'qosTrafficClassifiers': [{
            'qosTrafficClass': {
                'bandwidthShare': '50',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Best effort',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [1, 0],
                'dscpClassMapping': ['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '10',
                'egressDot1pValue': 1,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class1',
                'enabled': True
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '10',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class2',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class3',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class4',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class5',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '30',
                'egressDot1pValue': 2,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Medium',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [4, 3, 2],
                'dscpClassMapping': ['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31',
                                     'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42',
                                     'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '10',
                'egressDot1pValue': 5,
                'maxBandwidth': 10,
                'realTime': True,
                'className': 'Real time',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [5, 6, 7],
                'dscpClassMapping': ['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']
            }
        }],
        'name': None,
        'state': None,
        'description': None,
        'status': None,
        'eTag': None,
        'category': 'qos-aggregated-configuration',
        'uri': None
    },
    'inactiveFCoEQosConfig': None,
    'inactiveNonFCoEQosConfig': None,
    'type': 'qos-aggregated-configuration',
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'qos-aggregated-configuration',
    'uri': None
}}

Li_Qos = {
    'activeQosConfig': {
        'type': 'QosConfiguration',
        'configType': 'CustomWithFCoE',
        'uplinkClassificationType': 'DOT1P',
        'downlinkClassificationType': 'DOT1P_AND_DSCP',
        'qosTrafficClassifiers': [{
            'qosTrafficClass': {
                'bandwidthShare': '65',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Best effort',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [1, 0],
                'dscpClassMapping': ['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class1',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class2',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class3',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class4',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': 'fcoe',
                'egressDot1pValue': 3,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'FCoE lossless',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [3],
                'dscpClassMapping': []
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '25',
                'egressDot1pValue': 2,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Medium',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [4, 3, 2],
                'dscpClassMapping': ['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31',
                                     'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42',
                                     'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '10',
                'egressDot1pValue': 5,
                'maxBandwidth': 10,
                'realTime': True,
                'className': 'Real time',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [5, 6, 7],
                'dscpClassMapping': ['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']
            }
        }],
        'name': None,
        'state': None,
        'description': None,
        'status': None,
        'eTag': None,
        'modified': None,
        'created': None,
        'category': 'qos-aggregated-configuration',
        'uri': None
    },
    'inactiveFCoEQosConfig': None,
    'inactiveNonFCoEQosConfig': None,
    'type': 'qos-aggregated-configuration',
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'modified': None,
    'created': None,
    'category': 'qos-aggregated-configuration',
    'uri': None
}
LE = 'LE'

# Logical_Enclosure = [{'name': LE,
#                       'enclosureUris': ['ENC:' ENC_1],  # REAL
#                       'enclosureGroupUri': 'EG:Enc1-EG',
#                       'firmwareBaselineUri': None,
#                       'forceInstallFirmware': False}]

les = {
    'QoS-LE1':
        {'name': 'QoS-LE1',
         'enclosureUris': ['ENC:%s' % ENC_1],
         'enclosureGroupUri': 'EG:Enc1-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         },
    'QoS-LE2':
        {'name': 'QoS-LE2',
         'enclosureUris': ['ENC:%s' % ENC_1, 'ENC:%s' % ENC_2],
         'enclosureGroupUri': 'EG:Enc2-EG',
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

Bulk_enet = {
    "vlanIdRange": "1-5",
    "namePrefix": "Enet",
    "privateNetwork": "false",
    "smartLink": "true",
    "purpose": "General",
    "type": "bulk-ethernet-network",
    "bandwidth": {
        "maximumBandwidth": 20000,
        "typicalBandwidth": 2500
    }}

# Linux servers:
# Blade 3 Server (SY660 Gen10) iLO - 15.245.132.219
# Blade 4 Server (SY660 Gen9) iLO - 15.245.134.21
# Blade 5 Server (SY660 Gen9) iLO - 15.245.134.22
# Blade 8 Server (SY480 Gen9) iLO - 15.245.133.175

servers = [ENC_1 + ', bay 3', ENC_1 + ', bay 4', ENC_1 + ', bay 5', ENC_1 + ', bay 8']

profiles_noConns = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            # 'connectionSettings': {
            #     'connections': [
            #         {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
            #          'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
            #         {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
            #          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
            #     ],
            # },
        },
        'IP': '10.11.0.211',
        'handle': None
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            # 'connectionSettings': {
            #     'connections': [
            #         {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
            #          'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
            #         {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
            #          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
            #     ],
            # },
        },
        'IP': '10.11.0.221',
        'handle': None
    },
    'Profile3': {
        'payload': {
            'name': 'Profile3',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 5',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            # 'connectionSettings': {
            #     'connections': [
            #         {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
            #          'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
            #         {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
            #          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
            #     ],
            # },
        },
        'IP': '10.1.0.33',
        'handle': None
    },
    'Profile4': {
        'payload': {
            'name': 'Profile4',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 8',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            # 'connectionSettings': {
            #     'connections': [
            #         {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
            #          'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
            #         {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
            #          'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
            #     ],
            # },
        },
        'IP': '10.1.0.44',
        'handle': None
    }
}

profiles = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.11.0.211',
        'handle': None
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.11.0.221',
        'handle': None
    },
    'Profile3': {
        'payload': {
            'name': 'Profile3',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 5',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.1.0.33',
        'handle': None
    },
    'Profile4': {
        'payload': {
            'name': 'Profile4',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 8',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.1.0.44',
        'handle': None
    }
}

edit_profiles = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.11.0.211',
        'handle': None
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.11.0.221',
        'handle': None
    },

    # FCOE Bandwidth change to 4Gbps from 2.5Gbps; Networks change from netset to net_401, net_403 and net_404
    'Profile1_editConn': {
        'payload': {
            'name': 'Profile1',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'ETH:net_401,net_403,net_404'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '4000', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.11.0.211',
        'handle': None
    },

    'Profile1_stackConn': {
        'payload': {
            'name': 'Profile1',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '2500', 'networkUri': 'ETH:net_401,net_403,net_404'},
                ],
            },
        },
        'IP': '10.11.0.211',
        'handle': None
    },

    'Profile2_addConn': {
        'payload': {
            'name': 'Profile2',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                    {'id': 3, 'name': 'conn-enet-2a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                     'requestedMbps': '2500', 'networkUri': 'ETH:net_409'},
                ],
            },
        },
        'IP': '10.11.0.221',
        'handle': None
    },
    'Profile2_deleteConn': {
        'payload': {
            'name': 'Profile2',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                    {'id': 2, 'name': 'conn-fcoe-1b', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoenetwork1004'},
                ],
            },
        },
        'IP': '10.11.0.221',
        'handle': None
    },

}

edit_profiles_noFCoE = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                ],
            },
        },
        'IP': '10.11.0.211',
        'handle': None
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                ],
            },
        },
        'IP': '10.11.0.221',
        'handle': None
    },
    'Profile3': {
        'payload': {
            'name': 'Profile3',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 5',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                ],
            },
        },
        'IP': '10.1.0.33',
        'handle': None
    },
    'Profile4': {
        'payload': {
            'name': 'Profile4',
            'type': 'ServerProfileV9',
            'serverHardwareUri': ENC_1 + ', bay 8',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netsetEnet'},
                ],
            },
        },
        'IP': '10.1.0.44',
        'handle': None
    }
}

# HOST = "10.11.1.188"
# # Ports are handled in ~/.ssh/config since we use OpenSSH
# COMMAND = "uname -a"
#
# ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
#                        shell=False,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE)
# result = ssh.stdout.readlines()
# if result == []:
#     error = ssh.stderr.readlines()
#     print >> sys.stderr, "ERROR: %s" % error
# else:
#     print result

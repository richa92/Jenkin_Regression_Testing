import os
import sys
import paramiko
import time
import re


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


def file_exists(file_path):
    file = os.path.exists('file_path')


def removefile(file_path):
    file = os.remove('file_path')


def Remove_Whitespace(instring):
    return instring.strip()

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ENC_1 = 'SGH710T243'
ENC2 = 'SGH714WYBX'
ENC1ICBAY3 = 'SGH710T243, interconnect 3'
ENC1ICBAY6 = 'SGH710T243, interconnect 6'

LE_name = 'LE'
DL_PORT = '1'
LIGname = 'LIG1'
PFPTrue = True
PFPFalse = False
ICM_1 = ENC_1 + ', interconnect 3'
li = 'LE-LIG1'
LE = 'LE'
EG_Name = 'EG1'
# non redundant setup
LIG_A_Side_Name = 'LIG_A_Side'
LIG_B_Side_Name = 'LIG_B_Side'
Non_Reduntant_A = 'NonRedundantASide'
Non_Reduntant_B = 'NonRedundantBSide'
Redundant_icmap = 'Redundant'


users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Storageadmin', 'password': 'Storageadmin', 'fullName': 'Storageadmin', "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'InfrastructureAdmin', 'password': 'InfrastructureAdmin', 'fullName': 'InfrastructureAdmin', "enabled": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         ]

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            {'userName': 'InfrastructureAdmin', 'password': 'InfrastructureAdmin'},
            ]


Ethernet = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Net_1',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 15,
    'purpose': 'General',
    'name': 'Net_2',
    'smartLink': True,
    'privateNetwork': False,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 20,
    'purpose': 'General',
    'name': 'Net_3',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 40,
    'purpose': 'General',
    'name': 'Net_4',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {'name': 'Net_5',
     'type': 'ethernet-networkV4',
     'vlanId': 50,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'Net_6',
     'type': 'ethernet-networkV4',
     'vlanId': 60,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'Net_7',
     'type': 'ethernet-networkV4',
     'vlanId': 70,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'Net_8',
     'type': 'ethernet-networkV4',
     'vlanId': 80,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'Net_9',
     'type': 'ethernet-networkV4',
     'vlanId': 90,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'Net_10',
     'type': 'ethernet-networkV4',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'}]

fcnets = [
    {
        "name": "FC1",
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    },
    {
        "name": "FC2",
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    },
    {
        "name": "FC3",
        "linkStabilityTime": "300",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    },
    {
        "name": "FC4",
        "linkStabilityTime": "400",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    }
]

fcoenets = [
    {
        "name": "FCoE1",
        "vlanId": "100",
        "type": "fcoe-networkV4"
    },
    {
        "name": "FCoE2",
        "vlanId": "200",
        "type": "fcoe-networkV4"
    }, {
        "name": "FCoE3",
        "vlanId": "300",
        "type": "fcoe-networkV4"
    }, {
        "name": "FCoE4",
        "vlanId": "400",
        "type": "fcoe-networkV4"
    },
]

icmap_Redundant = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                   {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                   ]

icmap_SE_ASide = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                  ]
icmap_SE_BSide = [{'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                  ]

uplink_sets = {'us1_enet': {'name': 'upset1',
                            'ethernetNetworkType': 'Tagged',
                            'networkType': 'Ethernet',
                            # 'networkUris': ['Net_1','Net_2','Net_3','Net_4','Net_5','FCoE1','FCoE2','FCoE3','FCoE4'],
                            'networkUris': ['Net_1', 'Net_2', 'Net_3', 'Net_4', 'Net_5'],
                            'nativeNetworkUri': None,
                            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}],
                            },
               'us1_fc': {
    'name': 'us_fc1',
            'networkType': 'FibreChannel',
            'ethernetNetworkType': None,
            'networkUris': ['FC1'],
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}]
},
    'us2_fc': {
    'name': 'us_fc2',
            'networkType': 'FibreChannel',
            'ethernetNetworkType': None,
            'networkUris': ['FC2'],
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'}]
},
    'us_enet_BSide': {
    'name': 'us_enet_BSide',
            'networkType': 'Ethernet',
            'ethernetNetworkType': 'Tagged',
            # 'networkUris': ['Net_1','Net_2','Net_3','Net_4','Net_5','FCoE1','FCoE2','FCoE3','FCoE4'],
            'networkUris': ['Net_1', 'Net_2', 'Net_3', 'Net_4', 'Net_5'],
            'mode': 'Auto',
            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'}]
},
}


LIGS_TB = {'lig_1':
           {'name': LIGname,
            'type': 'logical-interconnect-groupV4',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': icmap_Redundant,
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': Redundant_icmap,
            'uplinkSets': [uplink_sets['us1_enet'].copy()],
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None,
            }
           }
enc_group_Tbird = {'name': EG_Name,
                   'enclosureCount': 1,
                   'interconnectBayMappings':
                   [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIGname},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIGname},
                    ],
                   'ipAddressingMode': 'DHCP',
                   'ipRangeUris': [],
                   'powerMode': 'RedundantPowerFeed'
                   }
Logiacl_Enclosure_Tbird = [{'name': LE,
                            'enclosureUris': ['ENC:' + ENC_1],  # REAL
                            'enclosureGroupUri': 'EG:EG1',
                            'firmwareBaselineUri': None,
                            'forceInstallFirmware': False},
                           ]

LIG_A_Side = {'lig_1':
              {'name': LIG_A_Side_Name,
               'type': 'logical-interconnect-groupV4',
               'enclosureType': 'SY12000',
               'interconnectMapTemplate': icmap_SE_ASide,
               'enclosureIndexes': [1],
               'interconnectBaySet': 3,
               'redundancyType': Non_Reduntant_A,
               # 'uplinkSets': [uplink_sets['us1_enet'].copy(),uplink_sets['us1_fc'].copy(),uplink_sets['us2_fc'].copy()],
               'uplinkSets': [uplink_sets['us1_enet'].copy()],
               'ethernetSettings': None,
               'state': 'Active',
               'telemetryConfiguration': None,
               'snmpConfiguration': None,
               }
              }

LIG_B_Side = {'lig_2':
              {'name': LIG_B_Side_Name,
               'type': 'logical-interconnect-groupV4',
               'enclosureType': 'SY12000',
               'interconnectMapTemplate': icmap_SE_BSide,
               'enclosureIndexes': [1],
               'interconnectBaySet': 3,
               'redundancyType': Non_Reduntant_B,
               # 'uplinkSets': [uplink_sets['us1_enet'].copy(),uplink_sets['us1_fc'].copy(),uplink_sets['us2_fc'].copy()],
               'uplinkSets': [uplink_sets['us_enet_BSide'].copy()],
               'ethernetSettings': None,
               'state': 'Active',
               'telemetryConfiguration': None,
               'snmpConfiguration': None,
               }
              }

enc_group_Tbird_Non_Redundant = {'name': EG_Name,
                                 'enclosureCount': 1,
                                 'interconnectBayMappings':
                                 [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG_A_Side_Name},
                                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG_B_Side_Name},
                                  ],
                                 'ipAddressingMode': 'DHCP',
                                 'ipRangeUris': [],
                                 'powerMode': 'RedundantPowerFeed'
                                 }

server_profiles_redundant_with_fc_conn = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC_1 + ', bay 5',
                                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:' + EG_Name,
                                           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                                           'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                                           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  {'id': 5, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  {'id': 6, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  {'id': 7, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_4', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  # add this for fc and fcoe connections and comment 3rd and 4th connections
                                                                                  # {'id': 3, 'name': '', 'functionType': 'Fibre Channel', 'portId': 'Mezz 3:1-b',
                                                                                  # 'requestedMbps': '2500', 'networkUri': 'FC:Net_2',  'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                  # {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                                                  # 'requestedMbps': '2500', 'networkUri': 'ETH:Net_2',  'mac': None, 'wwpn': None, 'wwnn': None},

                                                                                  ]}}]

server_profiles_edit_eight_conn = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC_1 + ', bay 5',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:' + EG_Name,
                                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 5, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 6, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 7, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_4', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           {'id': 8, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_4', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                           # add this for fc and fcoe connections and comment 3rd and 4th connections
                                                                           # {'id': 3, 'name': '', 'functionType': 'Fibre Channel', 'portId': 'Mezz 3:1-b',
                                                                           # 'requestedMbps': '2500', 'networkUri': 'FC:Net_2',  'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           # {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                                           # 'requestedMbps': '2500', 'networkUri': 'ETH:Net_2',  'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           ]}}]

profile_reapply = [{"op": "replace", "path": "/connectionSettings/reapplyState", "value": "ApplyPending"}, {"op": "replace", "path": "/serverHardwareReapplyState", "value": "ApplyPending"}]

profile_refresh = [{"op": "replace", "path": "/refreshState", "value": "RefreshPending"}]

downlink_port_disable = [{"interconnectName": ENC1ICBAY3, "portType": "Downlink", "portId": ENC1ICBAY3 + ':d5', "enabled": False, "portName": "d5", "portStatus": "Linked", "type": "port", "associatedUplinkSetUri": "upset1", }, {"interconnectName": ENC1ICBAY6, "portType": "Downlink", "portId": ENC1ICBAY6 + ':d5', "enabled": False, "portName": "d5", "portStatus": "Linked", "type": "port", "associatedUplinkSetUri": "upset1", },
                         ]
downlink_port_enable = [{"interconnectName": ENC1ICBAY3, "portType": "Downlink", "portId": ENC1ICBAY3 + ':d5', "enabled": True, "portName": "d5", "portStatus": "Linked", "type": "port", "associatedUplinkSetUri": "upset1", }, {"interconnectName": ENC1ICBAY6, "portType": "Downlink", "portId": ENC1ICBAY6 + ':d5', "enabled": True, "portName": "d5", "portStatus": "Linked", "type": "port", "associatedUplinkSetUri": "upset1", },
                        ]

# ICM_list = [{'interconnectName':'0000A66101, interconnect 3'}]
ICM_list = [{'name': 'SGH710T243, interconnect 3'}, {'name': 'SGH710T243, interconnect 6'}]

icm_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]


server_profiles_edit_eight_conn_multi_mezz_without_lag = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC_1 + ', bay 5',
                                                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:' + EG_Name,
                                                           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                                                           'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                                                           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 3, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 4, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 5, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 6, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 7, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_4', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                                                  {'id': 8, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                                                                                   'requestedMbps': '2500', 'networkUri': 'ETH:Net_4', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                                                  ]}}]
Logical_Enclosure = [{'name': LE,
                      'enclosureUris': ['ENC:' + ENC_1],  # REAL
                      'enclosureGroupUri': 'EG:' + EG_Name,
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False},
                     ]

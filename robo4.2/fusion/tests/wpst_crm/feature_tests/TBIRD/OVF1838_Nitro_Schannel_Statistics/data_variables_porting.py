import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def Remove_Whitespace(instring):
    return instring.strip()


appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

users = [{"type": "UserAndPermissions", "userName": "Networkadmin", "fullName": "", "password": "Networkadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Storageadmin", "fullName": "", "password": "Storageadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Backupadmin", "fullName": "", "password": "Backupadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Serveradmin", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}]},
         ]

usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            ]

############################################################################
#                                Variables for Nitro Hardware
# ##########################################################################

##################################
# Interconnect bays configurations
# 3 Frame, IBS3 and IBS2
##################################

REDUNDANCY = ''
LIG = 'LIG2'
LIG_IBS2 = 'LIG' + '_' + REDUNDANCY + '_IBS2'
LIG1 = 'LIG'
frame = 3
IBS = 3
IBS_2 = 2
LIG_ETH1_UPLINKS = ['Q5', 'Q5']
LIG_FC_UPLINKS = ['Q2']
LIG_ETH1_UPLINKS_untagged = ['Q6', 'Q6']
LIG_ETH1_UPLINKS_tunnel = ['Q1', 'Q1']
EG = 'EG' + '-' + REDUNDANCY
LE = 'LE' + '-' + REDUNDANCY
ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZH'
ENC3 = 'MXQ81804ZG'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]
# LI = LE + '-' + LIG
li_name = LE + '-' + LIG
LI = LE + '-' + LIG

uplink_sets_in_lig = [
    {
        'name': 'US-eth1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_401', 'FcoE_1002'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_ETH1_UPLINKS[0], 'speed': 'Auto'}
        ]
    }]
uplink_sets_in_lig_Fc = [
    {
        'name': 'US_fc',
        'networkType': 'FibreChannel',
        'ethernetNetworkType': None,
        'networkUris': ['FC_1'],
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '2', 'port': LIG_FC_UPLINKS[0], 'speed': 'Speed16G'}
        ]
    }
]

uplink_sets_in_lig1 = [
    {
        'name': 'US_eth',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_401', 'eth_402'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_ETH1_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_ETH1_UPLINKS[1], 'speed': 'Auto'}
        ]
    }
]

uplink_sets_in_lig2 = [
    {
        'name': 'US_Tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['Tunnel_net'],
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_ETH1_UPLINKS_tunnel[0], 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_ETH1_UPLINKS_tunnel[1], 'speed': 'Auto'},
        ]
    },

    {'name': 'US_Untagged',
     'ethernetNetworkType': 'Untagged',
     'networkType': 'Ethernet',
     'networkUris': ['Untagged_net'],
     'nativeNetworkUri': None,
     'logicalPortConfigInfos': [
             {'enclosure': '1', 'bay': '3', 'port': LIG_ETH1_UPLINKS_untagged[1], 'speed': 'Auto'},
             {'enclosure': '2', 'bay': '6', 'port': LIG_ETH1_UPLINKS_untagged[0], 'speed': 'Auto'},
     ]
     }
]

icmap_1 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

icmap_2 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

icmap_1_ibs2 = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

icmap_2_ibs2 = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3_ibs2 = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


ethernet_networks = [{
    'type': 'ethernet-networkV4',
    'ethernetNetworkType': 'Tagged',
    'name': 'eth_401',
    'privateNetwork': False,
    'purpose': 'General',
    'smartLink': True,
    'vlanId': 401
},
    {
    'type': 'ethernet-networkV4',
        'ethernetNetworkType': 'Tagged',
        'name': 'eth_402',
        'privateNetwork': False,
        'purpose': 'General',
        'smartLink': True,
        'vlanId': 402
},
    {'name': 'Untagged_net',
     'type': 'ethernet-networkV4',
     'vlanId': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'Tunnel_net',
     'type': 'ethernet-networkV4',
     'vlanId': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'}]

network_sets = [{"name": "set1", "networkUris": ["eth_401", "eth_402"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None}]

fc_network = [{"type": "fc-networkV4",
               "name": "FC_1",
               "fabricType": "FabricAttach",
               "linkStabilityTime": 30,
               "autoLoginRedistribution": True
               }
              ]

fcoe_networks = {'name': 'FcoE_1002', 'type': 'fcoe-networkV4', 'vlanId': 1002}


if frame == 1:
    REDUNDANCY = 'Redundant'
    InterconnectMapTemplate = icmap_1
    icmap_ibs2 = icmap_1_ibs2
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'
    InterconnectMapTemplate = icmap_2
    icmap_ibs2 = icmap_2_ibs2
elif frame == 3:
    REDUNDANCY = 'HighlyAvailable'
    InterconnectMapTemplate = icmap_3
    icmap_ibs2 = icmap_3_ibs2

ligs_Nitro = [{'name': LIG,
               'interconnectMapTemplate': InterconnectMapTemplate,
               'enclosureIndexes': [x for x in xrange(1, frame + 1)],
               'interconnectBaySet': IBS,
               'redundancyType': REDUNDANCY,
               'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
               'uplinkSets': list(uplink_sets_in_lig),
               'downlinkSpeedMode': 'SPEED_25GB'
               },
              {'name': LIG_IBS2,
               'interconnectMapTemplate': icmap_ibs2,
               'enclosureIndexes': [x for x in xrange(1, frame + 1)],
               'interconnectBaySet': IBS_2,
               'redundancyType': REDUNDANCY,
               'uplinkSets': list(uplink_sets_in_lig_Fc),
               'downlinkSpeedMode': 'SPEED_25GB'
               }]
ligs = [{'name': LIG,
         'interconnectMapTemplate': InterconnectMapTemplate,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
         'uplinkSets': list(uplink_sets_in_lig[0])
         },
        {'name': LIG,
         'interconnectMapTemplate': InterconnectMapTemplate,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
         'uplinkSets': list(uplink_sets_in_lig1)
         },
        {'name': LIG,
         'interconnectMapTemplate': InterconnectMapTemplate,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
         'uplinkSets': list(uplink_sets_in_lig2)
         },
        {'name': LIG,
         'interconnectMapTemplate': InterconnectMapTemplate,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': REDUNDANCY,
         'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
         'uplinkSets': list(uplink_sets_in_lig2)
         }
        ]
lig_neg = [{'name': 'LIG_nw',
            'interconnectMapTemplate': InterconnectMapTemplate,
            'enclosureIndexes': [x for x in xrange(1, frame + 1)],
            'interconnectBaySet': IBS,
            'redundancyType': REDUNDANCY,
            'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 60},
            'uplinkSets': []
            },
           {'name': 'LIG_nw',
            'interconnectMapTemplate': InterconnectMapTemplate,
            'enclosureIndexes': [x for x in xrange(1, frame + 1)],
            'interconnectBaySet': IBS,
            'redundancyType': REDUNDANCY,
            'telemetryConfiguration':{'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 15, 'sampleInterval': 100},
            'uplinkSets': []
            }
           ]


enc_group = {
    'EG':
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
         'ipAddressingMode': 'DHCP'
         }}

enc_group1 = {'name': EG,
              'enclosureCount': frame,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG_IBS2},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG_IBS2},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
              'ipAddressingMode': "DHCP"
              }


LE_Nitro = {
    'LE':
        {'name': LE,
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

SP_1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'profile_R2_bay1', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                ]}}
        ]

SP_2 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 2',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'profile_R2_bay1', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}

                                                ]}}
        ]

SP_NS = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
          'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
          'name': 'ENC1bay1', 'description': '', 'affinity': 'Bay',
          "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                  'requestedMbps': '2500', 'networkUri': 'NS:set1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}

                                                 ]}}
         ]

SP_NS1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'ENC1bay1', 'description': '', 'affinity': 'Bay',
           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'NS:set1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                  ]}}
          ]

SP_3 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 2',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'profile_ENC2_bay2', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                {'id': 2, 'name': 'conn-fc1', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1-b',
                                                 'requestedMbps': 8000, 'networkUri': 'FC:FC_1',
                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                          'targets': [{'arrayWwpn': '20010002AC01EE50', 'lun': '0'}]},
                                                 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                ]}},
        {'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'profile_ZG_bay2', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                                 'requestedMbps': '2500', 'networkUri': 'FCOE:FcoE_1002', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                ]}}
        ]


SP_4 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'profile_R2_bay1', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged_net', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                ]}},
        {'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 3',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:' + EG,
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'profile_W5_bay6', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel_net', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                ]}}
        ]

linux_details = {'hostip': '15.245.134.7', 'username': 'root', 'password': 'rootpwd', 'dir_location': '/root/', 'python_cmd': 'python2.7'}

ilo_details_enc2_bay1 = {'ilo_ip': '15.245.133.8', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc3_bay3 = {'ilo_ip': '15.245.132.36', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc2_bay2 = {'ilo_ip': '15.245.133.44', 'username': 'Administrator', 'password': 'hpvse123'}
server_details = {'username': 'Administrator', 'password': 'hpvse@1'}
server_details1 = {'username': 'Administrator', 'password': 'Wpsthpvse@1'}
broadcast_ip = '172.16.1.255'
ping_cmd1 = "ping -t -l 1024 'gateway_ip' > sample.txt"
ping_cmds = ["ping -t -l 64 'gateway_ip' > sample.txt", "ping -t -l 512 'gateway_ip' > sample.txt", "ping -t -l 1024 'gateway_ip' > sample.txt"]
ping_cmd_512 = "ping -t -l 512 'gateway_ip' > sample.txt"
kill_cmd = "TASKKILL /F /IM PING.EXE"
kill_diskspd = "TASKKILL /F /IM diskspd.exe"
iperf_start_server = 'iperf3.exe -s'
sampling_interval = '300'

diskspd_cmd = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b10K -h -L E:\\sample.dat >C:\\sample1.dat", "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b20K -h -L E:\\sample.dat >C:\\sample1.dat", "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b30K -h -L E:\\sample.dat >C:\\sample1.dat"]

diskspd_cmd1 = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b10K -h -L C:\\sample.dat >C:\\sample1.dat", "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b20K -h -L C:\\sample.dat >C:\\sample1.dat", "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b30K -h -L C:\\sample.dat >C:\\sample1.dat"]

diff_sample_count = ['30', '15']
diff_sample_interval = ['70', '300']
diff_sample_interval_lag = ['100', '400']
diff_sample_interval_60 = ['60']
sample_interval_100 = '100'
invalid_sample_count_min = '11'
invalid_sample_count_max = '51'

invalid_sample_interval_min = '1'
invalid_sample_interval_max = '3601'

diff_octets = ['1000', '4000', '7000']
diff_pkts = ['80']
diff_pkts_bc = ['35']
diff_octets_bc = ['4000', '8000', '15000']
diff_sample_count_li = ['30', '20', '10']
diff_sample_interval_li = ['200', '400', '800']
time_interval_2min = '180'
time_interval_5min = '300'
time_interval_1min = '60'
time_interval = ['200', '400', '700']
time_interval_lag = ['200', '500']
time_interval_1 = ['300', '500', '900']
min_octets = '1000'
min_pkts = '30'
max_time = ['1200', '4800']
min_time = ['100', '400']
Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]


Li_body = {"type": "telemetry-configuration",
           "enableTelemetry": True,
           "sampleCount": 12,
           "sampleInterval": 200,
           "description": None,
           "status": None,
           "name": "",
           "state": None,
           "eTag": None,
           "created": None,
           "modified": None,
           "category": "telemetry-configurations",
           "uri": ""}

ENC = ['MXQ81804ZH', 'MXQ81804ZF', 'MXQ81804ZG']
# IC = ['MXQ81804ZF, interconnect 3','MXQ81804ZH, interconnect 6']
IC = ['MXQ81804ZH, interconnect 6', 'MXQ81804ZF, interconnect 3']
IC_IBS2 = ['MXQ81804ZF, interconnect 2', 'MXQ81804ZH, interconnect 5']
ICM = ['MXQ81804ZH, interconnect 6', 'MXQ81804ZF, interconnect 3']
ICM_6 = ['MXQ81804ZH, interconnect 6']

downlink_ports = ['d13', 'd1']
downlink_ports1 = ['d27', 'd14']
downlink_port = ['d13', 'd1']
downlink = ['d1']
downlink_fcoe = ['d27']
downlink_bay6 = ['d27']
uplink_ports = ['Q5']
downlink_bay3 = ['d13']
interconnect = ['MXQ81804ZF, interconnect 3']
IC_state = ["Maintenance", "Configured"]
ic_disable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"portV5"}]

ic_enable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"portV5"}]

disable_status = 'Unlinked'
enable_status = 'Linked'
subportCommon_stats_counters = ['rfc1757StatsOctets', 'rfc1757StatsPkts']
sp_lag = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG,
           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'profile_R2_bay1', 'description': '', 'affinity': 'Bay',
           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                  ]}}]

Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
detlete_team_cmd0 = "Remove-NetLbfoTeam 'Team1'"
team_status_cmd0 = "Get-NetLbfoTeam -Name 'Team1' | fl Name,Status"
tagging_cmd = "Set-NetAdapter -Name 'adapter_name' -VlanId 'vlan_id'"
windows_server_details = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse@1'}

state = ['Absent', 'Configured']
Action = ['EFuseOn', 'EFuseOff']
icbays = ['6', '3']

ligs_negative = [{'name': 'LIG_Negative',
                  'interconnectMapTemplate': InterconnectMapTemplate,
                  'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                  'interconnectBaySet': IBS,
                  'redundancyType': 'HighlyAvailable',
                  'telemetryConfiguration': {"type": "telemetry-configuration",
                                             "enableTelemetry": True, "sampleCount": 32489875,
                                             "sampleInterval": 60},
                  'uplinkSets': []
                  },
                 {'name': 'LIG_Negative',
                  'interconnectMapTemplate': InterconnectMapTemplate,
                  'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                  'interconnectBaySet': IBS,
                  'redundancyType': 'HighlyAvailable',
                  'telemetryConfiguration': {"type": "telemetry-configuration",
                                             "enableTelemetry": True, "sampleCount": 12,
                                             "sampleInterval": 1},
                  'uplinkSets': []
                  }]

interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]

sub_port_number = ['1', '2']

port = ['Mezz 3:1-a']

subportCommon_egress_counters = ['rfc1213IfOutOctets', 'rfc1213IfOutUcastPkts', 'rfc1213IfOutNUcastPkts']

SUBPORT_STATUS_WAIT = '160s'
FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.251'
Host = '15.245.131.251'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

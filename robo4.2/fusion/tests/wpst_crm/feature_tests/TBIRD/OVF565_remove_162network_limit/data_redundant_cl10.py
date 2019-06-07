from copy import deepcopy
from data_common import *

server1_HardwareTypeUri = 'SHT:SY 480 Gen10 4'
server2_HardwareTypeUri = 'SHT:SY 480 Gen10 2'
server3_HardwareTypeUri = 'SHT:SY 480 Gen10 4'
server4_HardwareTypeUri = 'SHT:SY 480 Gen10 4'
server5_HardwareTypeUri = 'SHT:SY 480 Gen10 4'

ServerProfileTemplate_type = 'ServerProfileTemplateV6'
ServerProfile_type = 'ServerProfileV10'
lig_type = 'logical-interconnect-groupV6'
ibs_inTest = 2

CONFIG = 'Redundant'
CXP = 'CL10'

# Rack AV51 Servers for this test suite
# ENC_1 = 'CN754406W4' servers used for testing
# ENC_2 = 'CN7545084F'
# Instead of 1st bay using 3rd bay as M2 is Bronco in 3rd bay server
BRONCOBAY1 = '3'
ENC1_SRVRBAY = '3'
ENC2_SRVRBAY = '3'

MEZZA1 = 'Mezz 2:1-a'
MEZZB1 = 'Mezz 2:2-a'

# For traffic verification: pattern matching for ping statistics and allowed loss
# keywords in additionalOVF565-keywords.txt file uses these search strings
NT_ZERO_PERCENT_LOSS = 'Lost = * (0% loss)'
LINUX_ZERO_PERCENT_LOSS = '0% packet loss'

# For S-Channel LAG connection, most of the time is 0 or 1 packet loss, rarely 2, set to 2
ALLOWED_PACKET_LOSS_SCHANNEL_LAG = 10

# RoboGalaxy Linux test head access info
linux_details = {"hostip": "15.245.132.112", "username": "root", "password": "hpvse123",
                 "dir_location": "/root/pexpect/pexpect-4.6.0/",
                 "python_cmd": "python2.7"}

# Blade server iLO access info
ilo_details = {'ilo_ip': '',
               "username": 'Administrator', "password": 'hpvse123'}

# Blade server with Windows OS access info
windows_server_cred = ["Administrator", 'Hpvse1']

uplink_set = {
    'us-enet': {
        'name': 'us-enet',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1, 1001, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': 'net_1',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
            #        {'enclosure': '1', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
        ]
    },
    'us-enet-B': {
        'name': 'us-enet-B',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': make_range_list(1101, 1262, 'net_'),
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
        ]
    }
}

###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 2
# updating to Rack AV51 IBS2 redundant configuration
###

Enc2Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 2, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 5, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 2, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 5, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 2, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 5, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# Logical Interconnect Groups
###
ligs = {
    'Enc1-LIG': {
        'name': 'Enc1-LIG',
        'interconnectMapTemplate': Enc1Map,
        'enclosureIndexes': [1],
        'interconnectBaySet': ibs_inTest,
        'redundancyType': 'Redundant',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            #                       deepcopy(uplink_set['us-fcoe1002-A-1']),
            #                       deepcopy(uplink_set['us-fcoe1003-B-1']),
            deepcopy(uplink_set['us-enet']),
            deepcopy(uplink_set['us-enet-B'])
        ],

    },
    'Enc2-LIG': {
        'name': 'Enc2-LIG',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 2,
        'redundancyType': 'Redundant',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            deepcopy(uplink_set['us-enet']),
            deepcopy(uplink_set['us-enet-B'])
        ],
    },
    'Enc3-LIG': {
        'name': 'Enc3-LIG',
        'interconnectMapTemplate': Enc3Map,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': ibs_inTest,
        'redundancyType': 'Redundant',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet']),
            deepcopy(uplink_set['us-enet-B'])
        ],
    },
    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': ibs_inTest,
        'redundancyType': 'Redundant',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet']),
            deepcopy(uplink_set['us-enet-B'])
        ],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': ibs_inTest,
        'redundancyType': 'Redundant',
        'uplinkSets': [
            deepcopy(uplink_set['us-enet']),
            deepcopy(uplink_set['us-enet-B'])
        ],
    }
}

###
# Enclosure Groups
###
enc_group = {
    'Enc1-EG':
        {'name': 'Enc1-EG',
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc2-EG':
        {'name': 'Enc2-EG',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc3-EG':
        {'name': 'Enc3-EG',
         'enclosureCount': 3,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc4-EG':
        {'name': 'Enc4-EG',
         'enclosureCount': 4,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc4-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc5-EG':
        {'name': 'Enc5-EG',
         'enclosureCount': 5,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         }
}

###
# Server profiles
###
profiles = {
    'Profile1': {
        'payload': {
            'name': 'Profile1',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'enclosureUri': ENC_1,
            # 'connections': [
            #     {	'name': 'conn',
            #       'functionType': 'Ethernet',
            #       'portId': 'Auto',
            #       'networkUri': 'wpstnetwork1',
            #       }
            # ]
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                     'requestedMbps': '2500', 'networkUri': 'netset1K'},
                ]
            },
        },
        'IP': '191.4.5.77',
        'handle': None
    },
    'Profile2': {
        'payload': {
            'name': 'Profile2',
            'serverHardwareUri': ENC_2 + ', bay 3',
            'enclosureUri': ENC_2,
            'connectionSettings': {
                'connections': [
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                     'requestedMbps': '2500', 'networkUri': 'netset1K'}
                ]
            },
        },
        'IP': '191.4.5.88',
        'handle': None
    },
    'Profile3': {
        'payload': {
            'name': 'Profile3',
            'serverHardwareUri': ENC_3 + ', bay 1',
            'enclosureUri': ENC_3,
            'connectionSettings': {
                'connections': [
                    {'name': 'conn',
                     'functionType': 'Ethernet',
                     'portId': 'Auto',
                     'networkUri': 'netset1K',
                     }
                ]
            },
        },
        'IP': '10.1.0.33',
        'handle': None
    },
    'Profile4': {
        'payload': {
            'name': 'Profile4',
            'serverHardwareUri': ENC_4 + ', bay 1',
            'enclosureUri': ENC_4,
            'connectionSettings': {
                'connections': [
                    {'name': 'conn',
                     'functionType': 'Ethernet',
                     'portId': 'Auto',
                     'networkUri': 'netset1K',
                     }
                ]
            },
        },
        'IP': '10.1.0.44',
        'handle': None
    },
    'Profile5': {
        'payload': {
            'name': 'Profile5',
            'serverHardwareUri': ENC_5 + ', bay 1',
            'enclosureUri': ENC_5,
            'connectionSettings': {
                'connections': [
                    {'name': 'conn',
                     'functionType': 'Ethernet',
                     'portId': 'Auto',
                     'networkUri': 'netset1K',
                     }
                ]
            },
        },
        'IP': '10.1.0.55',
        'handle': None
    }
}

###
# Data for Server Profile test cases
###

edit_server_profiles = {

    # Enclosure 1 Server Profile
    "Profile1":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_1, BRONCOBAY1),
         'enclosureUri': 'ENC:' + ENC_1,
         'serverHardwareTypeUri': server1_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc1-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile1', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', },
                 {'id': 2, 'name': 'conn-net-2a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:2-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset162', }
             ]
         },
         },

    # Enclosure 2 Server Profile
    "Profile2":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_2, BRONCOBAY1),
         'enclosureUri': 'ENC:' + ENC_2,
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile2', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', },
                 {'id': 2, 'name': 'conn-net-2a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:2-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset162', }
             ]
         },
         },

    # Enclosure 3 Server Profile
    "Profile3":
        {'type': 'ServerProfileV8',
         'serverHardwareUri': ENC_3 + ', bay 1', 'enclosureUri': 'ENC:' + ENC_3,
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile3', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', },
                 {'id': 2, 'name': 'conn-net-2a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:2-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset162', }
             ]
         },
         },

    # Enclosure 4 Server Profile
    "Profile4":
        {'type': 'ServerProfileV8',
         'serverHardwareUri': ENC_4 + ', bay 1', 'enclosureUri': 'ENC:' + ENC_4,
         'serverHardwareTypeUri': server4_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile4', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', },
                 {'id': 2, 'name': 'conn-net-2a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:2-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset162', }
             ]
         },
         },

    # Enclosure 5 Server Profile
    "Profile5":
        {'type': 'ServerProfileV8',
         'serverHardwareUri': ENC_5 + ', bay 1', 'enclosureUri': 'ENC:' + ENC_5,
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile5', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1d', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', },
                 {'id': 2, 'name': 'conn-net-2a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:2-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset162', }
             ]
         },
         }

}

neg_server_profiles = {
    # Enclosure 1 Server Profile
    "Profile1":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_1, BRONCOBAY1),
         'enclosureUri': 'ENC:' + ENC_1,
         'serverHardwareTypeUri': server1_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc1-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile1', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 2, 'name': 'conn-net-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:1-d',
                  'requestedMbps': '2500', 'networkUri': 'ETH:net_1001', },
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
             ]
         },
         },

    # Enclosure 2 Server Profile
    "Profile2":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_2, BRONCOBAY1),
         'enclosureUri': 'ENC:' + ENC_2,
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile2', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset501', },
                 {'id': 2, 'name': 'conn-net-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 2:1-d',
                  'requestedMbps': '2500', 'networkUri': 'ETH:net_1001', }
             ]
         },
         },

    # Enclosure 3 Server Profile
    "Profile3":
        {'type': 'ServerProfileV8',
         'serverHardwareUri': '{}, bay {}'.format(ENC_3, BRONCOBAY1), 'enclosureUri': 'ENC:' + ENC_3,
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile3', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset334', },
                 {'id': 2, 'name': 'conn-net-1d', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-d',
                  'requestedMbps': '2500', 'networkUri': 'ETH:net_1001', }
             ]
         },
         },

    # Enclosure 4 Server Profile
    "Profile4":
        {'type': 'ServerProfileV8',
         'serverHardwareUri': '{}, bay {}'.format(ENC_4, BRONCOBAY1), 'enclosureUri': 'ENC:' + ENC_4,
         'serverHardwareTypeUri': server4_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile4', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset251', },
                 {'id': 2, 'name': 'conn-net-1d', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-d',
                  'requestedMbps': '2500', 'networkUri': 'ETH:net_1001', }
             ]
         },
         },
    # Enclosure 5 Server Profile
    "Profile5":
        {'type': 'ServerProfileV8',
         'serverHardwareUri': '{}, bay {}'.format(ENC_5, BRONCOBAY1), 'enclosureUri': 'ENC:' + ENC_5,
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Profile5', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset201', },
                 {'id': 2, 'name': 'conn-net-1d', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-d',
                  'requestedMbps': '2500', 'networkUri': 'ETH:net_1001', }
             ]
         },
         }

}

###
# Data for Unassigned Profile test cases
###

server_profiles_unassigned = {

    # Enclosure 1 Server Profile Template
    "Enc1_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareTypeUri': server1_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc1-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc1_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
             ]
         },
         },

    # Enclosure 2 Server Profile Template
    "Enc2_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc2_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
             ]
         },
         },

    # Enclosure 3 Server Profile Template
    "Enc3_sp_unassigned":
        {'type': 'ServerProfileV8',
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc3_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
             ]
         },
         },

    # Enclosure 4 Server Profile Template
    "Enc4_sp_unassigned":
        {'type': 'ServerProfileV8',
         'serverHardwareTypeUri': server4_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc4_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
             ]
         },
         },

    # Enclosure 5 Server Profile Template
    "Enc5_sp_unassigned":
        {'type': 'ServerProfileV8',
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc5_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
             ]
         },
         }

}

neg_server_profiles_unassigned = {
    # Enclosure 1 Server Profile
    "Enc1_sp_unassigned":
        {
            'type': ServerProfile_type,
            'serverHardwareTypeUri': server1_HardwareTypeUri,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
            'name': 'Enc1_sp_unassigned', 'description': '', 'affinity': 'Bay',
            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
            'boot': {'manageBoot': True, 'order': ['HardDisk']},
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
            'connectionSettings': {
                'connections': [
                    {'id': 2, 'name': 'conn-net-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 2:1-d',
                     'requestedMbps': '2500', 'networkUri': 'ETH:net_1001',
                     },
                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': 'Mezz 2:1-a',
                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K',
                     }
                ]
            },
        },
    # Enclosure 2 Server Profile
    "Enc2_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc2_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset501',
                  }
             ]
         },
         },
    # Enclosure 3 Server Profile
    "Enc3_sp_unassigned":
        {'type': 'ServerProfileV8',
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc3_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset334', }
             ]
         },
         },

    # Enclosure 4 Server Profile
    "Enc4_sp_unassigned":
        {'type': 'ServerProfileV8',
         'serverHardwareTypeUri': server4_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc4_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset251', }
             ]
         },
         },

    # Enclosure 5 Server Profile
    "Enc5_sp_unassigned":
        {'type': 'ServerProfileV8',
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc5_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset201', }
             ]
         },
         }

}

server_profiles_HW = {
    "Enc1_sp_unassigned":
        {
            'type': ServerProfile_type,
            'serverHardwareUri': '{}, bay {}'.format(ENC_1, BRONCOBAY1),
            'serverHardwareTypeUri': server1_HardwareTypeUri,
            'enclosureUri': 'ENC:' + ENC_1,
            'enclosureGroupUri': 'EG:Enc1-EG',
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'name': 'Enc1_sp_unassigned', 'description': '', 'affinity': 'Bay',
            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
            'boot': {'manageBoot': True, 'order': ['HardDisk']},
            "localStorage": {"sasLogicalJBODs": [], "controllers": []},
            "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
            'connectionSettings': {
                'connections': [
                    {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                     'portId': MEZZA1,
                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K',
                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                ]
            },
        },
    "Enc2_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_2, BRONCOBAY1),
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureUri': 'ENC:' + ENC_2,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc2_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                  'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K',
                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
             ]
         },
         },
    "Enc3_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_3, BRONCOBAY1),
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_3,
         'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc3_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K',
                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
             ]
         },
         },
    "Enc4_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_4, BRONCOBAY1),
         'serverHardwareTypeUri': server4_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_4,
         'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc4_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K',
                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
             ]
         },
         },
    "Enc5_sp_unassigned":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_5, BRONCOBAY1),
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_5,
         'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
         'name': 'Enc5_sp_unassigned', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': True, 'order': ['HardDisk']},
         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
         "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []},
         'connectionSettings': {
             'connections': [
                 {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K',
                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
             ]
         },
         }
}

###
# Data for Profile Template test cases
###

server_profile_templates = {

    # Enclosure 1 Server Profile Template
    "Enc1_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server1_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc1-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc1_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': MEZZA1,
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
                                ]
                                }
         },

    # Enclosure 2 Server Profile Template
    "Enc2_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc2_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': MEZZA1,
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
                                ]
                                }
         },

    # Enclosure 3 Server Profile Template
    "Enc3_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc3_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
                                ]
                                }
         },

    # Enclosure 4 Server Profile Template
    "Enc4_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server4_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc4_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
                                ]
                                }
         },

    # Enclosure 5 Server Profile Template
    "Enc5_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc5_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
                                ]
                                }
         }

}

neg_server_profile_templates = {
    # Enclosure 1 Server Profile Template
    "Enc1_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server1_HardwareTypeUri, 'enclosureGroupUri': 'EG:Enc1-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc1_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 2, 'name': 'conn-net-X', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 2:1-d',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_1001', },
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': MEZZA1,
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset1K', }
                                ]
                                }
         },

    # Enclosure 2 Server Profile Template
    "Enc2_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server2_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc2-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc2_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': MEZZA1,
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset501', }
                                ]
                                }
         },

    # Enclosure 3 Server Profile Template
    "Enc3_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server3_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc3-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc3_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset334', }
                                ]
                                }
         },

    # Enclosure 4 Server Profile Template
    "Enc4_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server4_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc4-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc4_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset251', }
                                ]
                                }
         },

    # Enclosure 5 Server Profile Template
    "Enc5_sptemplate":
        {'type': ServerProfileTemplate_type,
         'serverHardwareTypeUri': server5_HardwareTypeUri,
         'enclosureGroupUri': 'EG:Enc5-EG',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc5_sptemplate', 'description': '', 'affinity': 'Bay',
         'connectionSettings': {"manageConnections": True,
                                'connections': [
                                    {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet',
                                     'portId': 'Mezz 3:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'NS:netset201', }
                                ]
                                }
         }

}

server_profiles_SPT = {
    "Enc1_sp_spt":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_1, BRONCOBAY1),
         'serverHardwareTypeUri': server1_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_1,
         'enclosureGroupUri': 'EG:Enc1-EG', 'serverProfileTemplateUri': 'SPT:Enc1_sptemplate',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc1_sp_spt', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': False, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': False, 'order': ['HardDisk']},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K'},
             ]
         },

         },

    "Enc2_sp_spt":
        {'type': ServerProfile_type,
         'serverHardwareUri': '{}, bay {}'.format(ENC_2, BRONCOBAY1),
         'serverHardwareTypeUri': server2_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_2,
         'enclosureGroupUri': 'EG:Enc2-EG', 'serverProfileTemplateUri': 'SPT:Enc2_sptemplate',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc2_sp_spt', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': False, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': False, 'order': ['HardDisk']},
         'connectionSettings': {
             'connections': [
                 {'id': 1, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': MEZZA1,
                  'requestedMbps': '2500', 'networkUri': 'NS:netset1K'}
             ]
         },
         },

    "Enc3_sp_spt":
        {'type': ServerProfile_type, 'serverHardwareUri': ENC_3 + ', bay 1',
         'serverHardwareTypeUri': server3_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_3,
         'enclosureGroupUri': 'EG:Enc3-EG', 'serverProfileTemplateUri': 'SPT:Enc3_sptemplate',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc3_sp_spt', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': False, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': False, 'order': ['HardDisk']},
         'connections': [
             {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
              'requestedMbps': '2500', 'networkUri': 'NS:netset1K'},
         ]
         },

    "Enc4_sp_spt":
        {'type': ServerProfile_type, 'serverHardwareUri': ENC_4 + ', bay 1',
         'serverHardwareTypeUri': server4_HardwareTypeUri,
         'enclosureUri': 'ENC:' + ENC_4,
         'enclosureGroupUri': 'EG:Enc4-EG', 'serverProfileTemplateUri': 'SPT:Enc4_sptemplate',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc4_sp_spt', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': False, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': False, 'order': ['HardDisk']},
         'connections': [
             {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
              'requestedMbps': '2500', 'networkUri': 'NS:netset1K'},
         ]
         },

    "Enc5_sp_spt":
        {'type': ServerProfile_type, 'serverHardwareUri': ENC_5 + ', bay 1',
         'serverHardwareTypeUri': server5_HardwareTypeUri, 'enclosureUri': 'ENC:' + ENC_5,
         'enclosureGroupUri': 'EG:Enc5-EG', 'serverProfileTemplateUri': 'SPT:Enc5_sptemplate',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'Enc5_sp_spt', 'description': '', 'affinity': 'Bay',
         'bootMode': {'manageMode': False, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
         'boot': {'manageBoot': False, 'order': ['HardDisk']},
         'connections': [
             {'id': 7, 'name': 'conn-netset-1a', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
              'requestedMbps': '2500', 'networkUri': 'NS:netset1K'},
         ]
         }
}

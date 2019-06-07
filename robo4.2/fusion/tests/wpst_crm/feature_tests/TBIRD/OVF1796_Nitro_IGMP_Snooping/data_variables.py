from copy import deepcopy
import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

enc_count = 1

APPLIANCE_IP = '15.245.131.111'

flag = False

empty = ""
ENC = "CN7544043V"
INTERCONNECTS = [ENC + ', interconnect 3', ENC + ', interconnect 6']
up_ports_3 = ['Q5', 'Q6']  # Linked uplink ports of that nitro module
up_ports_6 = 'Q6'  # Linked uplink ports of that Nitro module
dw_ports_1 = ['d1', 'd8']  # Linked downlink ports (Servers in configured state should be given here)
start_vlan = 40
end_vlan = 100
internal_network1 = [
    {
        "vlanIdRange": "40-100",
        "purpose": "General",
        "namePrefix": "Net-Vlan",
        "smartLink": True,
        "privateNetwork": False,
        "type": "bulk-ethernet-networkV1",
        "initialScopeUris": [],
        "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500}
    }
]
ethernet_network = [
    {
        "vlanId": "10",
        "purpose": "Management",
        "name": "Net-Vlan10",
        "smartLink": False,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV4"
    },
    {
        "vlanId": "20",
        "purpose": "Management",
        "name": "Net-Vlan20",
        "smartLink": False,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV4"
    },
    {
        "vlanId": "30",
        "purpose": "Management",
        "name": "Net-Vlan30",
        "smartLink": False,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV4"
    },
    {
        "vlanId": 0,
        "ethernetNetworkType": "Tunnel",
        "subnetUri": None,
        "purpose": "Management",
        "name": "Tunnel",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": "ethernet-networkV4",
        "initialScopeUris": []
    },
    {
        "vlanId": 0,
        "ethernetNetworkType": "Untagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "untagged",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": "ethernet-networkV4",
        "initialScopeUris": []
    }
]
# For negative scenarios
ethernet_network1 = [
    {
        "vlanId": "10",
        "purpose": "Management",
        "name": "Net-Vlan10",
        "smartLink": False,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV4"
    },
    {
        "vlanId": "30",
        "purpose": "Management",
        "name": "Net-Vlan30",
        "smartLink": False,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV4"
    }
]

ethernet_network2 = [
    {
        "vlanId": "20",
        "purpose": "Management",
        "name": "Net-Vlan20",
        "smartLink": False,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "ethernetNetworkType": "Tagged",
        "type": "ethernet-networkV4"
    }
]

fcoenets = [
    {
        "name": "FCOE",
        "vlanId": "1002",
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": "fcoe-networkV4",
        "initialScopeUris": []
    }
]
uplink_set = {
    'US_Vlan10': {
        'name': 'US_Vlan10',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net-Vlan10'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}

        ]
    },
    'US_Vlan20': {
        'name': 'US_Vlan20',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan20"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
        ]
    },
    'US_Vlan30': {
        'name': 'US_Vlan30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan30"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
        ]
    },

    'US_Vlan10_Enc2': {
        'name': 'US_Vlan10',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net-Vlan10'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
            #        {'enclosure': '1', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
        ]
    },
    'US_Vlan20_Enc2': {
        'name': 'US_Vlan20',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan20"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}
        ]
    },

    'US_Vlan30_Enc2': {
        'name': 'US_Vlan30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan30"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}
        ]
    },
    'US_Vlan10_Enc3': {
        'name': 'US_Vlan10',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net-Vlan10'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
            #        {'enclosure': '1', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
        ]
    },
    'US_Vlan20_Enc3': {
        'name': 'US_Vlan20',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan20"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}
        ]
    },
    'US_Vlan30_Enc3': {
        'name': 'US_Vlan30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan30"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}
        ]
    },

}
###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc2MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]


###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###
LIB_old = "mk"
Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}

    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
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
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

###
# Logical Interconnect Groups
###
ligs = {
    'Enc1-LIG_HA': {
        'name': 'Enc1-LIG_HA',
        'interconnectMapTemplate': Enc1Map,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'downlinkSpeedMode': 'SPEED_10GB',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            #                       deepcopy(uplink_set['us-fcoe1002-A-1']),
            #                       deepcopy(uplink_set['us-fcoe1003-B-1']),
            deepcopy(uplink_set['US_Vlan10']),
            deepcopy(uplink_set['US_Vlan20']),
            deepcopy(uplink_set['US_Vlan30'])

        ],

    },

    'Enc1-LIG_ASide': {
        'name': 'Enc1-LIG_ASide',
        'interconnectMapTemplate': Enc1MapASide,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'downlinkSpeedMode': 'SPEED_10GB',
        'redundancyType': 'NonRedundantASide',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10']),
            deepcopy(uplink_set['US_Vlan30'])
        ],
    },

    'Enc1-LIG_BSide': {
        'name': 'Enc1-LIG_BSide',
        'interconnectMapTemplate': Enc1MapBSide,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'downlinkSpeedMode': 'SPEED_10GB',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            #                       deepcopy(uplink_set['us-fcoe1002-A-1']),
            #                       deepcopy(uplink_set['us-fcoe1003-B-1']),
            deepcopy(uplink_set['US_Vlan20'])
        ],

    },

    'Enc2-LIG_HA': {
        'name': 'Enc2-LIG_HA',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        #        'uplinkSets': [uplink_set],
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc2']),
            deepcopy(uplink_set['US_Vlan20_Enc2']),
            deepcopy(uplink_set['US_Vlan30_Enc2'])
        ],
    },

    'Enc2-LIG_ASide': {
        'name': 'Enc2-LIG_ASide',
        'interconnectMapTemplate': Enc2MapASide,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        #        'uplinkSets': [uplink_set],
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc2']),
            deepcopy(uplink_set['US_Vlan30_Enc2'])
        ],
    },

    'Enc2-LIG_BSide': {
        'name': 'Enc2-LIG_BSide',
        'interconnectMapTemplate': Enc2MapBSide,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        #        'uplinkSets': [uplink_set],
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc2']),
            deepcopy(uplink_set['US_Vlan20_Enc2']),
            deepcopy(uplink_set['US_Vlan30_Enc2'])
        ],
    },

    'Enc3-LIG_HA': {
        'name': 'Enc3-LIG_HA',
        'interconnectMapTemplate': Enc3bay3ICMMap,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc2']),
            deepcopy(uplink_set['US_Vlan20_Enc2']),
            deepcopy(uplink_set['US_Vlan30_Enc2'])
        ],
    },

    'Enc3-LIG_ASide': {
        'name': 'Enc3-LIG_ASide',
        'interconnectMapTemplate': Enc3MapASide,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        #        'uplinkSets': [uplink_set],
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc3']),
            deepcopy(uplink_set['US_Vlan30_Enc3'])
        ],
    },

    'Enc3-LIG_BSide': {
        'name': 'Enc3-LIG_BSide',
        'interconnectMapTemplate': Enc3MapBSide,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        #        'uplinkSets': [uplink_set],
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc3']),
            deepcopy(uplink_set['US_Vlan20_Enc3']),
            deepcopy(uplink_set['US_Vlan30_Enc3'])
        ],
    },

    'Enc4-LIG': {
        'name': 'Enc4-LIG',
        'interconnectMapTemplate': Enc4Map,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10']),
            deepcopy(uplink_set['US_Vlan20'])
        ],
    },
    'Enc5-LIG': {
        'name': 'Enc5-LIG',
        'interconnectMapTemplate': Enc5Map,
        'enclosureIndexes': [1, 2, 3, 4, 5],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_10GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10']),
            deepcopy(uplink_set['US_Vlan20'])
        ],

    },
    'Enc1-LIG_HA_neg': {
        'name': 'Enc1-LIG_HA',
        'interconnectMapTemplate': Enc1Map,
        'enclosureIndexes': [1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'downlinkSpeedMode': 'SPEED_10GB',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            #                       deepcopy(uplink_set['us-fcoe1002-A-1']),
            #                       deepcopy(uplink_set['us-fcoe1003-B-1']),
        ],

    }

}

enc_group = {
    'Enc1-EG':
        {'name': 'Enc1-EG',
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG_HA'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG_HA'}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
        'Enc1-EG_ASide':
        {'name': 'Enc1-EG_ASide',
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG_ASide'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "DHCP",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc1-EG_BSide':
        {'name': 'Enc1-EG_BSide',
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG_ASide'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc1-LIG_BSide'}],
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
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG_HA'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG_HA'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
        'Enc2-EG_ASide':
        {'name': 'Enc2-EG_ASide',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG_ASide'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

        'Enc2-EG_BSide':
        {'name': 'Enc2-EG_BSide',
         'enclosureCount': 2,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG_ASide'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG_BSide'}],
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
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG_HA'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG_HA'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc3-EG_ASide':
        {'name': 'Enc3-EG_ASide',
         'enclosureCount': 3,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG_ASide'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },
    'Enc3-EG_BSide':
        {'name': 'Enc3-EG_BSide',
         'enclosureCount': 3,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG_ASide'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG_BSide'}],
         'ipAddressingMode': "External",
         'ipRangeUris': [],
         'powerMode': "RedundantPowerFeed"
         },

    'Enc4-EG':
        {'name': 'Enc4-EG',
         'type': 'EnclosureGroupV400',
         'enclosureCount': 4,
         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         'stackingMode': 'Enclosure',
         'interconnectBayMappingCount': 6,
         'configurationScript': None,
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
         'type': 'EnclosureGroupV400',
         'enclosureCount': 5,
         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         'stackingMode': 'Enclosure',
         'interconnectBayMappingCount': 6,
         'configurationScript': None,
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
ENC1 = 'CN7544043V'
ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'

les = {
    'Enc1-LE':
        {
            'name': 'LE_IGMP_SNOOPING_SE',
            'enclosureUris': ['ENC:' + ENC1],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc2-LE':
        {
            'name': 'LE_IGMP_SNOOPING_2ME',
            'enclosureUris': [ENC1, ENC2],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc3-LE':
        {
            'name': 'LE_IGMP_SNOOPING_3ME',
            'enclosureUris': [ENC1, ENC2, ENC3],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc4-LE':
        {
            'name': 'LE_IGMP_SNOOPING_4ME',
            'enclosureUris': [ENC1, ENC2, ENC3, ENC4],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc2-LE':
        {
            'name': 'LE_IGMP_SNOOPING_5ME',
            'enclosureUris': [ENC1, ENC2, ENC3, ENC4, ENC5],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        }
}
Server_profiles = {
    'Enc1_server_profiles_HA': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1,
                                 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'],
                                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'name': 'Enc1-' + ENC1 + '-bay-1',
                                 'description': '', 'affinity': 'Bay', 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet',
                                                                        'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}
                                 },
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'],
                                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'name': 'Enc1-' + ENC1 + '-bay-3',
                                 'description': '', 'affinity': 'Bay', 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet',
                                                                        'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10',
                                                                        'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                        'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30',
                                                                        'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}
                                 }
                                ],

    'Enc1_server_profiles_ASide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto',
                                                                              'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],

    'Enc1_server_profiles_BSide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],


    'Enc2_server_profiles_HA': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc2-' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 8',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc2_server_profiles_ASide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc2_server_profiles_BSide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],



    'Enc3_server_profiles_HA': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'name': 'Enc2-' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc3_server_profiles_ASide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc3_server_profiles_BSide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ]

}

ethernet_setting_disable_igmp = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
ethernet_setting_enable_igmp = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
ethernet_setting_enable_igmp_per_vlan = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "10,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan1 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "20,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan_30 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}


ethernet_setting_enable_igmp_per_vlan_10 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "10",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
ethernet_setting_enable_igmp_per_vlan1 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan_20 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "20",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
ethernet_setting_enable_igmp_per_vlan_40 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "40",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
lig_vlan = '99,49,40-44,51,50'
li_vlan = "99,44,43,40-42,49-50,51"

ethernet_setting_enable_igmp_per_vlan_neg = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
ethernet_setting_enable_igmp_li = {
    'type': 'EthernetInterconnectSettingsV4',
    'interconnectType': 'Ethernet',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    'igmpSnoopingVlanIds': "",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_settings_neg_timeintervals = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "10,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': "",
    'macRefreshInterval': 5
}

ethernet_settings_neg_timeintervals = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "10,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': "",
    'macRefreshInterval': 5
}
Edit_ligs = {
    'Enc1-LIG_HA':
        {'name': 'Enc1-LIG_HA',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1Map,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [uplink_set['US_Vlan10'],
                        uplink_set['US_Vlan20'],
                        uplink_set['US_Vlan30']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'Enc1-LIG_ASide':
        {'name': 'Enc1-LIG_ASide',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapASide,
         'downlinkSpeedMode': 'SPEED_10GB',
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantASide',
         'uplinkSets': [uplink_set['US_Vlan10'],
                        uplink_set['US_Vlan30']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc1-LIG_BSide':
        {'name': 'Enc1-LIG_BSide',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapBSide,
         'downlinkSpeedMode': 'SPEED_10GB',
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantBSide',
         'uplinkSets': [uplink_set['US_Vlan20']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc2-LIG_HA':
        {'name': 'Enc2-LIG_HA',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc2Map,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'downlinkSpeedMode': 'SPEED_10GB',
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [deepcopy(uplink_set['US_Vlan10_Enc2']),
                        deepcopy(uplink_set['US_Vlan20_Enc2']),
                        deepcopy(uplink_set['US_Vlan30_Enc2'])],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc3-LIG_HA':
        {'name': 'Enc3-LIG_HA',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc3bay3ICMMap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'downlinkSpeedMode': 'SPEED_10GB',
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [deepcopy(uplink_set['US_Vlan10_Enc3']),
                        deepcopy(uplink_set['US_Vlan20_Enc3']),
                        deepcopy(uplink_set['US_Vlan30_Enc3'])],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }
}

network_not_in_internalNWs_us = '50'
neg_FCOE = '1002'
invalid_ids = ['-4', '4.5', '$@#', 'abc', '23000', '4095']
negative_vlan = ['untagged', 'Tunnel', '1002']
TimeoutInterval_neg = ['10', '-5', '100', '129', '1226']
errorcode = 'CRM_ETHERNET_SETTINGS_INVALID_IGMP_SNOOPING_VLAN_IDS_LOGICAL_INTERCONNECT_GROUP'
errorcode1 = 'CRM_ETHERNET_SETTINGS_INVALID_IGMP_SNOOPING_VLAN_IDS_FORMAT'
errorcode2 = 'CRM_ETHERNET_SETTINGS_VALUE_OUT_OF_RANGE_IGMP_TIMEOUT_INTERVAL'
errorcode3 = 'CRM_SWITCH_SETTINGS_ID_INVALID'
Edit_lig_neg = {
    'Enc1-LIG_HA':
        {'name': 'Enc1-LIG_HA',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1Map,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [uplink_set['US_Vlan30']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp_per_vlan,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        'Enc1-LIG_ASide':
        {'name': 'Enc1-LIG_ASide',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapASide,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'downlinkSpeedMode': 'SPEED_10GB',
         'redundancyType': 'NonRedundantASide',
         'uplinkSets': [uplink_set['US_Vlan30']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp_per_vlan,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc1-LIG_BSide':
        {'name': 'Enc1-LIG_BSide',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapBSide,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantBSide',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp_per_vlan_20,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc2-LIG_HA':
        {'name': 'Enc2-LIG_HA',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc2Map,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [deepcopy(uplink_set['US_Vlan10_Enc2']),
                        deepcopy(uplink_set['US_Vlan20_Enc2']),
                        deepcopy(uplink_set['US_Vlan30_Enc2'])],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_igmp,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc3-LIG_HA':
        {'name': 'Enc3-LIG_HA',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc3bay3ICMMap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [deepcopy(uplink_set['US_Vlan10_Enc3']),
                        deepcopy(uplink_set['US_Vlan20_Enc3']),
                        deepcopy(uplink_set['US_Vlan30_Enc3'])],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         }
}

neg_uplink_sets = {'name': 'US_Vlan10',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': [],
                   'fcNetworkUris': [],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'NotSupported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '3', 'port': 'Q5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}
                                       ]}

neg_uplink_sets_Bside = {'name': 'US_Vlan20',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': [],
                         'fcNetworkUris': [],
                         'fcoeNetworkUris': [],
                         'lacpTimer': 'Short',
                         'logicalInterconnectUri': None,
                         'primaryPortLocation': None,
                         'manualLoginRedistributionState': 'NotSupported',
                         'connectionMode': 'Auto',
                         'nativeNetworkUri': None,
                         'portConfigInfos': [{'bay': '6', 'port': 'Q6', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]}


internal_networks = []
internal_networks_40 = ['ETH:Net-Vlan_40']
invalid_id = ['1 to 19']
linux_details = {"hostip": "15.245.134.7", "username": "root", "password": "rootpwd", "dir_location": "/root/", "python_cmd": "python2.7"}
ilo_details = {'ilo_ip': '', "username": 'Administrator', "password": 'hpvse123'}

module_file_path = "C:\\DEMO\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\OVF1796_IGMP_Snooping\\GetServerIPs.py"

windows_server_cred = ["Administrator", 'hpvse1']

windows_server = {'win_ip': '', "username": 'Administrator', "password": 'hpvse1'}

server_bays = [1, 2, 3]
Server_network_ips = {server_bays[0]: "", server_bays[1]: "", server_bays[2]: ""}
Server_network_ips_Aside = {server_bays[0]: "", server_bays[1]: ""}
Server_network_ips_Bside = {server_bays[0]: "", server_bays[1]: ""}

mcast_cmds = {'0': "C:\\Multicast\\mk_mc\\mcreceive 234.45.17.20 55000 200 > C:\\multicast_traffic_of_server1.dat",
              '1': "C:\\Multicast\\mk_mc\\mcreceive 234.45.17.20 55000 200 > C:\\multicast_traffic_of_server2.dat",
              '2': "C:\\Multicast\\mk_mc\\mcreceive 234.45.17.20 55000 200 > C:\\multicast_traffic_of_server3.dat"}

wdump_cmds = {'0': "C:\\Multicast\\mk_mc\\WinDump.exe -c 200 -p -i ",
              '1': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -p -i ",
              '2': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -p -i "}

wdump_cmds1 = {'0': "C:\\Multicast\\mk_mc\\WinDump.exe -c 200 -i ",
               '1': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -i ",
               '2': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -i "}

outputfile_guid_server = {0: "C:\\interface_traffic_of_server1.dat",
                          10: "C:\\second_interface_traffic_of_server1.dat",
                             1: "C:\\Interface_traffic_of_server2.dat",
                             2: "C:\\Interface_traffic_of_server3.dat",
                             12: "C:\\second_interface_traffic_of_server3.dat",
                             11: "C:\\second_Interface_traffic_of_server2.dat"}

msender = "C:\\Multicast\\mcast\\bin\\msender 234.45.17.20 55000 > sender.txt"

interface_guid_cmd = "C:\\Multicast\\mk_mc\\mk_get_guid.bat > "

server1_guids_keys = ['Ethernet1', 'Ethernet2', 'Ethernet3']
server2_guids_keys = ['Ethernet1', 'Ethernet2']
server3_guids_keys = ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet5']
delete_route = 'route delete 224.0.0.0'
IP = '192.168.10.*'
IP1 = '192.168.20.*'

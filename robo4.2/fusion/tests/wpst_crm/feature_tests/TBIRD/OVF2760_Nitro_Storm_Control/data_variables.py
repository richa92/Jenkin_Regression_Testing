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

enc_count = 1

APPLIANCE_IP = '15.245.131.111'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ENC1 = 'CN7544043V'
ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
icbays = ['3', '6']

ethernet_network = [{"vlanId": "10",
                     "purpose": "General",
                     "name": "Net-Vlan10",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "20",
                     "purpose": "General",
                     "name": "Net-Vlan20",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "30",
                     "purpose": "General",
                     "name": "Net-Vlan30",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"}]

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
        'networkUris': ['Net-Vlan20'],
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
        'networkUris': ['Net-Vlan30'],
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
            {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}
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
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapASide = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapBSide = \
    [
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc2MapASide = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    ]

Enc2MapBSide = \
    [
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

dto = [{'name': 'CN7544043V, interconnect 3'}, {'name': 'CN7544043V, interconnect 6'}]

Interconnects = {
    'Enc1-interconnect': ['CN7544043V, interconnect 3', 'CN7544043V, interconnect 6']
}


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
        'uplinkSets': [
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
        'redundancyType': 'NonRedundantASide',
        'downlinkSpeedMode': 'SPEED_10GB',
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
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan20'])
        ],

    },

    'Enc2-LIG_HA': {
        'name': 'Enc2-LIG_HA',
        'interconnectMapTemplate': Enc2Map,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
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
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc3']),
            deepcopy(uplink_set['US_Vlan20_Enc3']),
            deepcopy(uplink_set['US_Vlan30_Enc3'])
        ],
    },

    'Enc3-LIG_ASide': {
        'name': 'Enc3-LIG_ASide',
        'interconnectMapTemplate': Enc3MapASide,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
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
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc3']),
            deepcopy(uplink_set['US_Vlan20_Enc3']),
            deepcopy(uplink_set['US_Vlan30_Enc3'])
        ]
    }
}

ethernet_setting_disable_storm = {'enableStormControl': False}

Threshold = [1, 262143, 150, 3, 240, 50]

negative_storm_threshold = [-4, 262144, 'abc', '@#$', '34!', 0]

error_msg = "CRM_ETHERNET_SETTINGS_VALUE_OUT_OF_RANGE_STORM_CONTROL_THRESHOLD"

ethernet_setting_enable_storm = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableStormControl': True,
    'stormControlThreshold': "",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}


ethernet_setting_enable_storm_neg = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableStormControl': True,
    'stormControlThreshold': "",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

Edit_ligs1 = {
    'Enc1-LIG_HA':
        {'name': 'Enc1-LIG_HA',
         'type': 'logical-interconnect-groupV5',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1Map,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_set['US_Vlan10'],
                        uplink_set['US_Vlan20'],
                        uplink_set['US_Vlan30']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'downlinkSpeedMode': 'SPEED_10GB'
         },

        'Enc1-LIG_ASide':
        {'name': 'Enc1-LIG_ASide',
         'type': 'logical-interconnect-groupV5',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapASide,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantASide',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [uplink_set['US_Vlan10'],
                        uplink_set['US_Vlan30']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc1-LIG_BSide':
        {'name': 'Enc1-LIG_BSide',
         'type': 'logical-interconnect-groupV5',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapBSide,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantBSide',
         'downlinkSpeedMode': 'SPEED_10GB',
         'uplinkSets': [uplink_set['US_Vlan20']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
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
         'uplinkSets': [deepcopy(uplink_set['US_Vlan10_Enc2']),
                        deepcopy(uplink_set['US_Vlan20_Enc2']),
                        deepcopy(uplink_set['US_Vlan30_Enc2'])],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
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
         }
}


les = {
    'Enc1-LE':
        {
            'name': 'LE_STORM_CONTROL_SE',
            'enclosureUris': ['ENC:' + ENC1],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc2-LE':
        {
            'name': 'LE_STORM_CONTROL_2ME',
            'enclosureUris': [ENC1, ENC2],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc3-LE':
        {
            'name': 'LE_STORM_CONTROL_3ME',
            'enclosureUris': [ENC1, ENC2, ENC3],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        }
}

before_storm_enable_resp_lig = 'enabled=True'
Enc1_servers = [1, 2, 8]
Enc2_servers = [1, 2, 8]
Enc3_servers = [1, 2, 8]

Server_profiles = {
    'Enc1_server_profiles_HA': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                        'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                        'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}}
                                ],

    'Enc1_server_profiles_ASide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],

    'Enc1_server_profiles_BSide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],


    'Enc2_server_profiles_HA': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc2-' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc2_server_profiles_ASide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc2_server_profiles_BSide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],



    'Enc3_server_profiles_HA': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'name': 'Enc2-' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc3_server_profiles_ASide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc3_server_profiles_BSide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ]

}

BAY = 8

linux_details = {"hostip": "15.245.134.7", "username": "root", "password": "rootpwd", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '',
               "username": 'Administrator', "password": 'hpvse123'}

module_file_path = "C:\\Storm Control\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\OVF2760_Strom Control\\GetServerIPs.py"

windows_server_cred = ["Administrator", 'hpvse1']

windows_server = {'win_ip': '',
                  "username": 'Administrator', "password": 'hpvse1'}

server_bays = [1, 2, 8]
Server_network_ips = {server_bays[0]: "",
                      server_bays[1]: "",
                      server_bays[2]: ""}

mcast_cmds = {'0': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\multicast_traffic_of_server1.dat",
              '1': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\multicast_traffic_of_server2.dat",
              '2': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\multicast_traffic_of_server3.dat"}

US_Check = 'US_Vlan10'
Port_Check = 'Q5'
interconnectname_1 = 'CN7544043V, interconnect 3'
interconnectname_2 = 'CN7544043V, interconnect 6'
Alert_Message_Port = 'A packet storm has been detected on uplink set %s, ports {"name":"%s","uri":"IC_uri"}: %s. All packets causing the storm will be discarded until the packet rate drops below the specified threshold of 3 packets per second.' % (US_Check, interconnectname_1, Port_Check)

Port_Check1 = 'Q6'
US_Check1 = 'US_Vlan30'
Alert_Message_Port1 = 'A packet storm has been detected on uplink set %s, ports {"name":"%s","uri":"IC_uri"}: %s. All packets causing the storm will be discarded until the packet rate drops below the specified threshold of 3 packets per second.' % (US_Check1, interconnectname_1, Port_Check1)
US_Check2 = 'US_Vlan20'
Alert_Message_Port_Bside = 'A packet storm has been detected on uplink set %s, ports {"name":"%s","uri":"IC_uri"}: %s. All packets causing the storm will be discarded until the packet rate drops below the specified threshold of 3 packets per second.' % (US_Check2, interconnectname_2, Port_Check1)
downlink_Port_Check = 'd8'

broadcast_command_B_Side = "C:\\stormControl\\hping.exe -c 20000 -i 1 --fast 192.168.20.255"
broadcast_command = "C:\\stormControl\\hping.exe -c 20000 -i 1 --fast 192.168.10.255"
multicast_command = "C:\\stormControl\\iperf.exe -c 224.0.55.55 -u --ttl 5 -t 60 -P 10"

disable_interface_B_Side = "netsh interface set interface Ethernet3 disabled"
enable_interface_B_Side = "netsh interface set interface Ethernet3 enabled"
disable_interface_Aside = "netsh interface set interface Ethernet2 disabled"
enable_interface_Aside = "netsh interface set interface Ethernet2 enabled"
disable_interface = "netsh interface set interface Ethernet1 disabled"
enable_interface = "netsh interface set interface Ethernet1 enabled"
dlf_test_blade_downlinkport = "d8"
dlf_test_blade_uplinkport = 'Q5'
dlf_test_blade_uplinkport1 = 'Q6'
bcast_blade_downlinkport = "d1"

delete_route_command = "route delete 224.0.0.0"
set_route_command = "route add 224.0.0.0 mask 240.0.0.0 192.168.10.25"
set_route_command1 = "route add 224.0.0.0 mask 240.0.0.0 192.168.20.25"

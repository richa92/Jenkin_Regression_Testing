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


SSH_PASS = 'hpvse1'

enc_count = 1

APPLIANCE_IP = '15.186.9.89'

FUSION_IP = '15.186.9.89'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username

FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password

FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username

FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt

FUSION_TIMEOUT = 180              # Timeout.  Move this out???

FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator',
                                                                                                     'Backup administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}]


loggerlevel = r'INFO'   # use INFO|DEBUG

ENC1 = 'MXQ70800R7'
ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'
icbays = ['3', '6']

ethernet_network = [{"vlanId": "10",
                     "purpose": "Management",
                     "name": "Net-Vlan10",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "20",
                     "purpose": "Management",
                     "name": "Net-Vlan20",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "30",
                     "purpose": "Management",
                     "name": "Net-Vlan30",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "0",
                     "purpose": "Management",
                     "name": "Net-Untagged",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Untagged",
                     "type": "ethernet-networkV4"}]


POTASH = "Virtual Connect SE 40Gb F8 Module for Synergy"
CHLORIDE10 = "Synergy 10Gb Interconnect Link Module"

LIG1 = 'lig_tbird'

redundancyType = 'HighlyAvailable'

EG = '2enc-DUS-EG'

uplink_set = {
    'US_Vlan10': {
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
    'US_Vlan20': {
        'name': 'US_Vlan20',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ["Net-Vlan20"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}
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
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}
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

us_delete_network = {
    'name': 'US_Vlan10',
    'type': 'uplink-setV4',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': [],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
            {'desiredSpeed': 'Auto',
                'location': {
                    'locationEntries': [
                      {
                          'value': 'Q2',
                          'type': 'Port'
                      },
                        {
                          'value': '3',
                          'type': 'Bay'
                      },
                        {
                          'value': ENC1,
                          'type': 'Enclosure'
                      }
                    ]
                }
             }
    ],
    'logicalInterconnectUri': 'Enc2-LE-Enc2-LIG'
}


###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapASide = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapBSide = \
    [
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc2MapASide = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2MapBSide = \
    [
        {'bay': 6, 'enclosure': 1,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]


###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###
LIB_old = "mk"
Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}

    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3,
            'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5Map = \
    [
        {'bay': 3, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1,
            'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5,
            'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

Interconnects = {
    'Enc1-interconnect': ['MXQ70800R7, interconnect 3', 'MXQ70800R7, interconnect 6']
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
        'redundancyType': 'NonRedundantASide',
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            #                       deepcopy(uplink_set['us-fcoe1002-A-1']),
            #                       deepcopy(uplink_set['us-fcoe1003-B-1']),
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
        #        'uplinkSets': [uplink_set],
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
        #        'uplinkSets': [uplink_set],
        'uplinkSets': [
            #                       deepcopy(uplink_set['us-fcoe1002-A-1']),
            #                       deepcopy(uplink_set['us-fcoe1003-B-1']),
        ],

    }

}

ethernet_setting_disable_storm = {'enableStormControl': False}

Threshold = [1, 262143, 150, 3, 240]

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
    "igmpSnoopingVlanIds": "10",
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

ethernet_setting_enable_igmp_per_vlan_30 = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan_multiple = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "1-19",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan_commas = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "10,20,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}
ethernet_setting_enable_igmp_per_vlan_commas_ASide = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "10,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan_deleted = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "20,30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

ethernet_setting_enable_igmp_per_vlan_deleted_ASide = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "30",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

negative_vlans = [-4, 4.5, 'acb', '@3@', '34!', '#4']
errors_vlans = ['CRM_ETHERNET_SETTINGS_INVALID_IGMP_SNOOPING_VLAN_IDS_LOGICAL_INTERCONNECT_GROUP',
                'CRM_ETHERNET_SETTINGS_INVALID_IGMP_SNOOPING_VLAN_IDS_FORMAT'
                ]
valid_vlan_not_present = [50, 0, 4095]


ethernet_setting_enable_igmp_per_vlan_neg = {
    'type': 'EthernetInterconnectSettingsV4',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': True,
    "igmpSnoopingVlanIds": "",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}

Edit_ligs = {
    'Enc1-LIG_HA':
        {'name': 'Enc1-LIG_HA',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1Map,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
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

Edit_ligs1 = {
    'Enc1-LIG_HA':
        {'name': 'Enc1-LIG_HA',
         'type': 'logical-interconnect-groupV4',
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
         'snmpConfiguration': None
         },

        'Enc1-LIG_ASide':
        {'name': 'Enc1-LIG_ASide',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc1MapASide,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantASide',
         'uplinkSets': [uplink_set['US_Vlan10'],
                        uplink_set['US_Vlan30']],
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
         # 'type': 'EnclosureGroupV400',
         # 'enclosureCount': 1,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         # 'enclosureCount': 1,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         # 'enclosureCount': 1,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         'enclosureCount': 2,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         'enclosureCount': 2,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         'enclosureCount': 2,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         'enclosureCount': 3,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         'enclosureCount': 3,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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
         # 'type': 'EnclosureGroupV400',
         'enclosureCount': 3,
         # 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
         # 'stackingMode': 'Enclosure',
         # 'interconnectBayMappingCount': 6,
         # 'configurationScript': None,
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


les = {
    'Enc1-LE':
        {
            'name': 'LE_IGMP_SNOOPING_SE',
            'enclosureUris': [ENC1],
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


Enc1_servers = [1, 2, 3]
Enc2_servers = [1, 2, 3]
Enc3_servers = [1, 2, 3]
Server_profiles = {
    'Enc1_server_profiles_HA': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
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
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc1_server_profiles_ASide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc1_server_profiles_BSide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                     {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                         'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],


    'Enc2_server_profiles_HA': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
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
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc2_server_profiles_ASide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc2_server_profiles_BSide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
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
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],



    'Enc3_server_profiles_HA': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
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
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc3_server_profiles_ASide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc3_server_profiles_BSide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan20', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
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
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan30', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ]

}


enc_groups = [{'name': EG,
               'type': 'EnclosureGroupV300',
               'enclosureCount': 2,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }]

enc_groups_aside = [{'name': EG,
                     'type': 'EnclosureGroupV300',
                     'enclosureCount': 2,
                     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                     'stackingMode': 'Enclosure',
                     'interconnectBayMappingCount': 6,
                     'configurationScript': None,
                     'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3,
                          'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
                     'ipAddressingMode': "External",
                     'ipRangeUris': [],
                     'powerMode': "RedundantPowerFeed"
                     }]

enc_groups_bside = [{'name': EG,
                     'type': 'EnclosureGroupV300',
                     'enclosureCount': 2,
                     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                     'stackingMode': 'Enclosure',
                     'interconnectBayMappingCount': 6,
                     'configurationScript': None,
                     'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3,
                          'logicalInterconnectGroupUri': 'LIG:' + LIG1},
                         {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                         {'interconnectBay': 6,
                             'logicalInterconnectGroupUri': 'LIG:' + LIB_old},
                         {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
                     'ipAddressingMode': "External",
                     'ipRangeUris': [],
                     'powerMode': "RedundantPowerFeed"
                     }]

# ENC1 = 'CN754406W4'
# ENC2 = 'CN7545084F'
BAY = 3
# LE = '2enc-cl10-le'
# LI creation for both A side and HA
# LI = LE+'-'+LIG1
# Bside Configuration script
# LIB = LE+'-'+LIB_old
'''
lees = [{'name': LE,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
        'enclosureGroupUri': 'EG:'+EG,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]
'''

us = {'us-eth': {'name': 'us-eth',
                 'ethernetNetworkType': 'Tagged',
                 'networkType': 'Ethernet',
                 'networkUris': ['fvt4network8'],
                 'fcNetworkUris': [],
                 'fcoeNetworkUris': [],
                 'lacpTimer': 'Short',
                 'logicalInterconnectUri': None,
                 'primaryPortLocation': None,
                 'manualLoginRedistributionState': 'NotSupported',
                 'connectionMode': 'Auto',
                 'nativeNetworkUri': None,
                 'portConfigInfos': [{'enclosure': ENC1, 'bay': '3', 'port': 'Q2.3', 'desiredSpeed': 'Auto'}]}}


# 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23':
port_map = {'Q1': '61', 'Q1.1': '62', 'Q1.2': '63', 'Q1.3': '64', 'Q1.4': '65',
            'Q2': '66', 'Q2.1': '67', 'Q2.2': '68', 'Q2.3': '69', 'Q2.4': '70',
            'Q3': '71', 'Q3.1': '72', 'Q3.2': '73', 'Q3.3': '74', 'Q3.4': '75',
            'Q4': '76', 'Q4.1': '77', 'Q4.2': '78', 'Q4.3': '79', 'Q4.4': '80',
            'Q5': '81', 'Q5.1': '82', 'Q5.2': '83', 'Q5.3': '84', 'Q5.4': '85',
            'Q6': '86', 'Q6.1': '87', 'Q6.2': '88', 'Q6.3': '89', 'Q6.4': '90',
            'Q7': '91', 'Q7.1': '92', 'Q7.2': '93', 'Q7.3': '94', 'Q7.4': '95',
            'Q8': '96', 'Q8.1': '97', 'Q8.2': '98', 'Q8.3': '99', 'Q8.4': '100',
            'Q1:1': '62', 'Q1:2': '63', 'Q1:3': '64', 'Q1:4': '65',
            'Q2:1': '67', 'Q2:2': '68', 'Q2:3': '69', 'Q2:4': '70',
            'Q3:1': '72', 'Q3:2': '73', 'Q3:3': '74', 'Q3:4': '75',
            'Q4:1': '77', 'Q4:2': '78', 'Q4:3': '79', 'Q4:4': '80',
            'Q5:1': '82', 'Q5:2': '83', 'Q5:3': '84', 'Q5:4': '85',
            'Q6:1': '87', 'Q6:2': '88', 'Q6:3': '89', 'Q6:4': '90',
            'Q7:1': '92', 'Q7:2': '93', 'Q7:3': '94', 'Q7:4': '95',
            'Q8:1': '97', 'Q8:2': '98', 'Q8:3': '99', 'Q8:4': '100'
            }


lig_tbird_2enc = {"type": "logical-interconnect-groupV300",
                  "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                  "description": None,
                  "name": "lig_tbird",
                  "interconnectMapTemplate":
                  {"interconnectMapEntryTemplates": [
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]},
                          "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]},
                          "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23", "enclosureIndex": 2},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {
                          "type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 2}]},
                  "enclosureType": "SY12000",
                  "enclosureIndexes": [1, 2],
                  "interconnectBaySet": "3",
                  "redundancyType": "HighlyAvailable",
                  "internalNetworkUris": [],
                  "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                  "qosConfiguration": None,
                  # "uplinkSets": [{"networkUris":["/rest/ethernet-networks/48ee7ab1-2733-4fee-8110-9acbdf4e351d"],"lacpTimer":"Long","name":"bay3-enet4x-us","networkType":"Ethernet","ethernetNetworkType":"Tagged","primaryPort":None,"logicalPortConfigInfos":[{"desiredSpeed":"Auto","logicalLocation":{"locationEntries":[{"type":"Bay","relativeValue":3},{"type":"Port","relativeValue":67},{"type":"Enclosure","relativeValue":1}]}}],"mode":"Auto"}]
                  "uplinkSets": [
                      {"networkUris": ["fvt4network1", "fvt4network2"],
                       "lacpTimer":"Long",
                       "name":"bay3-enet4x-us",
                       "networkType":"Ethernet",
                       "ethernetNetworkType":"Tagged",
                       "primaryPort":None,
                       "logicalPortConfigInfos":[
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 3},
                                                {"type": "Port",
                                                 "relativeValue": 67},
                                                {"type": "Enclosure", "relativeValue": 1}]
                            }},
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 3},
                                                {"type": "Port",
                                                 "relativeValue": 68},
                                                {"type": "Enclosure", "relativeValue": 1}]
                            }}
                      ], "mode": "Auto"},

                      {"networkUris": ["FC_1"],
                       "mode":"Auto",
                       "lacpTimer":"Short",
                       "primaryPort":None,
                       "logicalPortConfigInfos":[{"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Port", "relativeValue": 62}, {"type": "Enclosure", "relativeValue": 1}]}}],
                       "networkType": "FibreChannel",
                       "ethernetNetworkType": None,
                       "name": "US_FC"},


                      {"networkUris": ["fvt4network3"],
                       "lacpTimer":"Long",
                       "name":"bay3-enetQ-us",
                       "networkType":"Ethernet",
                       "ethernetNetworkType":"Tagged",
                       "primaryPort":None,
                       "logicalPortConfigInfos":[
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 3},
                                                {"type": "Port",
                                                 "relativeValue": 71},
                                                {"type": "Enclosure", "relativeValue": 1}]
                            }},
                      ], "mode": "Auto"},

                      {"networkUris": ["fvt4network4", "fvt4network6", "fvt4network7"],
                       "lacpTimer":"Long",
                       "name":"bay6-enet4x-us",
                       "networkType":"Ethernet",
                       "ethernetNetworkType":"Tagged",
                       "primaryPort":None,
                       "logicalPortConfigInfos":[
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                {"type": "Port",
                                                 "relativeValue": 67},
                                                {"type": "Enclosure", "relativeValue": 2}]
                            }},
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                {"type": "Port",
                                                 "relativeValue": 68},
                                                {"type": "Enclosure", "relativeValue": 2}]
                            }},
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                {"type": "Port",
                                                 "relativeValue": 69},
                                                {"type": "Enclosure", "relativeValue": 2}]
                            }},
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                {"type": "Port",
                                                 "relativeValue": 70},
                                                {"type": "Enclosure", "relativeValue": 2}]
                            }}

                      ], "mode": "Auto"},
                      {"networkUris": ["fvt4network5"],
                       "lacpTimer":"Long",
                       "name":"bay6-enetQ-us",
                       "networkType":"Ethernet",
                       "ethernetNetworkType":"Tagged",
                       "primaryPort":None,
                       "logicalPortConfigInfos":[
                          {"desiredSpeed": "Auto", "logicalLocation":
                           {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                {"type": "Port",
                                                 "relativeValue": 76},
                                                {"type": "Enclosure", "relativeValue": 2}]
                            }},
                      ], "mode": "Auto"},
                  ]
                  }

Lig_tbird_Aside = {"type": "logical-interconnect-groupV300",
                   "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"}, "description": None, "name": LIG1, "interconnectMapTemplate": {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23", "enclosureIndex": 1}, {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 2}]},
                   "enclosureType": "SY12000", "enclosureIndexes": [1, 2], "interconnectBaySet": "3", "redundancyType": "NonRedundantASide", "internalNetworkUris": [], "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"}, "qosConfiguration": None, "uplinkSets": [
                       {"networkUris": ["fvt4network1", "fvt4network2"], "lacpTimer":"Long", "name":"bay3-enet4x-us-Aside", "networkType":"Ethernet",
                        "ethernetNetworkType":"Tagged", "primaryPort":None,
                        "logicalPortConfigInfos":[
                           {"desiredSpeed": "Auto", "logicalLocation":
                            {"locationEntries": [{"type": "Bay", "relativeValue": 3},
                                                 {"type": "Port",
                                                     "relativeValue": 67},
                                                 {"type": "Enclosure", "relativeValue": 1}]
                             }},
                           {"desiredSpeed": "Auto", "logicalLocation":
                            {"locationEntries": [{"type": "Bay", "relativeValue": 3},
                                                 {"type": "Port",
                                                     "relativeValue": 68},
                                                 {"type": "Enclosure", "relativeValue": 1}]
                             }}

                       ], "mode": "Auto"},
                       {"networkUris": ["FC_1"], "mode":"Auto", "lacpTimer":"Short", "primaryPort":None, "logicalPortConfigInfos":[{"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Port", "relativeValue": 62}, {"type": "Enclosure", "relativeValue": 1}]}}],
                        "networkType": "FibreChannel", "ethernetNetworkType": None, "name": "US_FC"}, {"networkUris": ["fvt4network3"],
                                                                                                       "lacpTimer":"Long", "name":"bay3-enetQ-us", "networkType":"Ethernet", "ethernetNetworkType":"Tagged", "primaryPort":None,
                                                                                                       "logicalPortConfigInfos":[
                            {"desiredSpeed": "Auto", "logicalLocation":
                             {"locationEntries": [{"type": "Bay", "relativeValue": 3},
                                                  {"type": "Port",
                                                      "relativeValue": 71},
                                                  {"type": "Enclosure", "relativeValue": 1}]
                              }},
                        ], "mode": "Auto"}, ]
                   }


Lig_tbird_Bside = {"type": "logical-interconnect-groupV300",
                   "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"}, "description": None, "name": LIB_old, "interconnectMapTemplate": {"interconnectMapEntryTemplates": [
                       {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 1}, {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23", "enclosureIndex": 2}]},
                   "enclosureType": "SY12000", "enclosureIndexes": [1, 2], "interconnectBaySet": "3", "redundancyType": "NonRedundantBSide", "internalNetworkUris": [], "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"}, "qosConfiguration": None, "uplinkSets": [
                       {"networkUris": ["fvt4network1", "fvt4network2"], "lacpTimer":"Long", "name":"bay3-enet4x-us-Bside", "networkType":"Ethernet",
                        "ethernetNetworkType":"Tagged", "primaryPort":None,
                        "logicalPortConfigInfos":[
                           {"desiredSpeed": "Auto", "logicalLocation":
                            {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                 {"type": "Port",
                                                     "relativeValue": 67},
                                                 {"type": "Enclosure", "relativeValue": 2}]
                             }},
                           {"desiredSpeed": "Auto", "logicalLocation":
                            {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                 {"type": "Port",
                                                     "relativeValue": 68},
                                                 {"type": "Enclosure", "relativeValue": 2}]
                             }}

                       ], "mode": "Auto"},
                       {"networkUris": ["FC_1"], "mode":"Auto", "lacpTimer":"Short", "primaryPort":None, "logicalPortConfigInfos":[{"desiredSpeed": "Auto", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Port", "relativeValue": 62}, {"type": "Enclosure", "relativeValue": 2}]}}],
                           "networkType": "FibreChannel", "ethernetNetworkType": None, "name": "US_FC"}, {"networkUris": ["fvt4network3"],
                                                                                                          "lacpTimer":"Long", "name":"bay3-enetQ-us", "networkType":"Ethernet", "ethernetNetworkType":"Tagged", "primaryPort":None,
                                                                                                          "logicalPortConfigInfos":[
                               {"desiredSpeed": "Auto", "logicalLocation":
                                {"locationEntries": [{"type": "Bay", "relativeValue": 6},
                                                     {"type": "Port",
                                                         "relativeValue": 71},
                                                     {"type": "Enclosure", "relativeValue": 2}]
                                 }},
                           ], "mode": "Auto"}, ]
                   }

'''
#HA second Profile details
{'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2'+ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network5', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]}
'''

server_profiles = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc1' + ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                        'networkUri': 'ETH:fvt4network5', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                        'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                                        'networkUri': 'ETH:fvt4network4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]},
                   {'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                              'networkUri': 'ETH:fvt4network5', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                              'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                                              'networkUri': 'ETH:fvt4network4', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]}
                   ]

'''
ASide 2nd Profile
                    {'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:'+EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Enc2'+ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    #{'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                    ]},

'''

server_profiles_Aside = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': 'Enc1' + ENC1 + '-bay-2', 'description': '', 'affinity': 'Bay',
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'boot': {'manageBoot': True, 'order': ['HardDisk']},
                          'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                           'networkUri': 'ETH:fvt4network2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          # {'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          # {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                          ]},

                         ]
server_profiles_Bside = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC2 + ', bay 2',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'boot': {'manageBoot': True, 'order': ['HardDisk']},
                          'connections': [{'id': 1, 'name': 'conAA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': 'conAB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                           'networkUri': 'ETH:fvt4network2', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          # {'id': 3, 'name': 'connBA', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', #'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          # {'id': 4, 'name': 'connBB', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:fvt4network3', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                          ]},

                         ]

analyzer_port = "Q2:3"
analyzer_dport = "d2"
used_uplink_port = "Q2:2"
fc_uplink_port = "Q1:1"
stacking_port = "Q7"
analyzer_port_2 = "Q6"
analyzer_port_3 = "Q2:4"
# Timer for configuring the Port monitoring
pm_timer = 400
# Timer for Configuring the Port Monitoring When switched from Port Q3.3 to Q5
pm_timer_q5 = 800
# Logical enclosure Create timer
le_timer = 0
bay_no = 3
li_portmonitor = {"type": "port-monitor",
                  "enablePortMonitor": 'true',
                  "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                   "portUri": "UplinkportUri"},
                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"}]
                  }

linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '',
               "username": 'Administrator', "password": 'hpvse123'}

module_file_path = "C:\\Orange_Works\\Initial_workS_3.10\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\IGMP\\GetServerIPs.py"

windows_server_cred = ["Administrator", 'password@123']

windows_server = {'win_ip': '',
                  "username": 'Administrator', "password": 'password@123'}

server_bays = [1, 2, 3]
Server_network_ips = {server_bays[0]: "",
                      server_bays[1]: "", server_bays[2]: ""}
Server_network_ips_Aside = {server_bays[0]: "", server_bays[1]: ""}

mcast_cmds = {'0': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\multicast_traffic_of_server1.dat",
              '1': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\multicast_traffic_of_server2.dat",
              '2': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\multicast_traffic_of_server3.dat"}

server_guid = {"1": [], "2": [], "3": []}

outputfile_guid_server = {0: "C:\\interface_traffic_of_server1.dat", 10: "C:\\second_interface_traffic_of_server1.dat", 1: "C:\\Interface_traffic_of_server2.dat",
                          2: "C:\\Interface_traffic_of_server3.dat", 12: "C:\\second_interface_traffic_of_server3.dat", 11: "C:\\second_Interface_traffic_of_server2.dat"}

wdump_cmds = {'0': "C:\\Multicast\\mk_mc\\WinDump.exe -c 200 -i ",
              '1': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -i ",
              '2': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -i "}

msender = "C:\\Multicast\\mcast\\bin\\msender 235.45.17.10 1234 > sender.txt"

interface_guid_cmd = "C:\\Multicast\\mk_mc\\mk_get_guid.bat > "


server1_guids_keys = ['Ethernet1', 'Ethernet2']
server2_guids_keys = ['Ethernet1', 'Ethernet2']
server3_guids_keys = ['Ethernet1', 'Ethernet2', 'Ethernet3']


broadcast_command = "C:\\hping\\hping.exe -c 20000 -i 1 --fast 192.168.10.255"
multicast_command = "C:\\Iperf\\iperf.exe -c 224.0.55.55 -u --ttl 5 -t 60 -P 10"

disable_interface = "netsh interface set interface Ethernet1 disabled"
enable_interface = "netsh interface set interface Ethernet1 enabled"

dlf_test_blade_downlinkport = "d3"
dlf_test_blade_uplinkport = 'Q2'
bcast_blade_downlinkport = "d1"
valDict = {'status_code': 200, 'taskState': 'Completed'}

delete_route_command = "route delete 224.0.0.0"
set_route_command = "route add 224.0.0.0 mask 240.0.0.0 192.168.10.25"

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

enc_count = 3

APPLIANCE_IP = '15.245.131.251'

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

ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZG'
ENC3 = 'MXQ81804ZH'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'
icbays = ['3', '6']

ethernet_network = [{"vlanId": "401",
                     "purpose": "General",
                     "name": "Net-Vlan401",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "402",
                     "purpose": "General",
                     "name": "Net-Vlan402",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "403",
                     "purpose": "General",
                     "name": "Net-Vlan403",
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
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ['Net-Vlan401'],
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
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ['Net-Vlan402'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'}
        ]
    },
    'US_Vlan30': {
        'name': 'US_Vlan30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ['Net-Vlan403'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '3', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}
        ]
    },

    'US_Vlan10_Enc2': {
        'name': 'US_Vlan10',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ['Net-Vlan401'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}
        ]
    },
    'US_Vlan20_Enc2': {
        'name': 'US_Vlan20',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ["Net-Vlan402"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'}
        ]
    },

    'US_Vlan30_Enc2': {
        'name': 'US_Vlan30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ["Net-Vlan403"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}
        ]
    },
    'US_Vlan10_Enc3': {
        'name': 'US_Vlan10',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ['Net-Vlan401'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}
        ]
    },
    'US_Vlan20_Enc3': {
        'name': 'US_Vlan20',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ["Net-Vlan402"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'}
        ]
    },
    'US_Vlan30_Enc3': {
        'name': 'US_Vlan30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'consistencyChecking': 'ExactMatch',    # Only applicable for 5.0 OV
        'networkUris': ["Net-Vlan403"],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}
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
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
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

dto = [{'name': 'MXQ81804ZF, interconnect 3'}, {'name': 'MXQ81804ZH, interconnect 6'}]

Interconnects = {
    'Enc3-interconnect': ['MXQ81804ZF, interconnect 3', 'MXQ81804ZH, interconnect 6']
}
ic_name = {'name': 'MXQ81804ZF, interconnect 3'}


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
        'type': 'logical-interconnect-groupV6',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10']),
            deepcopy(uplink_set['US_Vlan20']),
            deepcopy(uplink_set['US_Vlan30'])
        ],

    },

    'Enc1-LIG_ASide': {
        'name': 'Enc1-LIG_ASide',
        'interconnectMapTemplate': Enc1MapASide,
        'type': 'logical-interconnect-groupV6',
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
        'type': 'logical-interconnect-groupV6',
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'downlinkSpeedMode': 'SPEED_25GB',
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan10_Enc3']),
            deepcopy(uplink_set['US_Vlan20_Enc3']),
            deepcopy(uplink_set['US_Vlan30_Enc3'])
        ],
    },

    'Enc3-LIG_ASide': {
        'name': 'Enc3-LIG_ASide',
        'interconnectMapTemplate': Enc3MapASide,
        'type': 'logical-interconnect-groupV6',
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
        'downlinkSpeedMode': 'SPEED_25GB',
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [

            deepcopy(uplink_set['US_Vlan10_Enc3']),
            deepcopy(uplink_set['US_Vlan30_Enc3'])
        ],
    },

    'Enc3-LIG_BSide': {
        'name': 'Enc3-LIG_BSide',
        'interconnectMapTemplate': Enc3MapBSide,
        'type': 'logical-interconnect-groupV6',
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'downlinkSpeedMode': 'SPEED_25GB',
        'uplinkSets': [
            deepcopy(uplink_set['US_Vlan20_Enc3'])
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
        'uplinkSets': [],

    }

}

ethernet_setting_disable_storm = {'enableStormControl': False}

Threshold = [1, 262143, 150, 3, 240]

negative_storm_threshold = [-4, 262144, 0]

error_msg = "CRM_ETHERNET_SETTINGS_VALUE_OUT_OF_RANGE_STORM_CONTROL_THRESHOLD"

ethernet_setting_enable_storm = {
    'type': 'EthernetInterconnectSettingsV5',
    'enableFastMacCacheFailover': False,
    'enableIgmpSnooping': False,
    'enableStormControl': True,
    'stormControlThreshold': "",
    'enableNetworkLoopProtection': False,
    'igmpIdleTimeoutInterval': 260,
    'macRefreshInterval': 5
}


ethernet_setting_enable_storm_neg = {
    'type': 'EthernetInterconnectSettingsV5',
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
         'ethernetSettings': ethernet_setting_enable_igmp,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc3-LIG_ASide':
        {'name': 'Enc3-LIG_ASide',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc3MapASide,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantASide',
         'downlinkSpeedMode': 'SPEED_25GB',
         'uplinkSets': [uplink_set['US_Vlan10_Enc3'],
                        uplink_set['US_Vlan30_Enc3']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc3-LIG_BSide':
        {'name': 'Enc3-LIG_BSide',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc3MapBSide,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'NonRedundantBSide',
         'downlinkSpeedMode': 'SPEED_25GB',
         'uplinkSets': [uplink_set['US_Vlan20_Enc3']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
    'Enc3-LIG_HA':
        {'name': 'Enc3-LIG_HA',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': Enc3bay3ICMMap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'downlinkSpeedMode': 'SPEED_25GB',
         'uplinkSets': [deepcopy(uplink_set['US_Vlan10_Enc3']),
                        deepcopy(uplink_set['US_Vlan20_Enc3_HA']),
                        deepcopy(uplink_set['US_Vlan30_Enc3'])],
         'stackingMode': 'Enclosure',
         'ethernetSettings': ethernet_setting_enable_storm,
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
         'ipAddressingMode': 'DHCP',
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
         'ipAddressingMode': 'DHCP',
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
         'ipAddressingMode': 'DHCP',
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
            'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC3, 'ENC:' + ENC2],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc4-LE':
        {
            'name': 'LE_STORM_CONTROL_4ME',
            'enclosureUris': [ENC1, ENC2, ENC3, ENC4],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc2-LE':
        {
            'name': 'LE_STORM_CONTROL_5ME',
            'enclosureUris': [ENC1, ENC2, ENC3, ENC4, ENC5],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        }
}

before_storm_enable_resp_lig = 'enabled=True'
Enc1_servers = [1, 2, 3]
Enc2_servers = [1, 2, 3]
Enc3_servers = [1, 2, 3]
Server_profiles = {
    'Enc1_server_profiles_HA': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                        'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}},
                                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                        'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}}
                                ],

    'Enc1_server_profiles_ASide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],

    'Enc1_server_profiles_BSide': [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-8', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],


    'Enc2_server_profiles_HA': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc2-' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]},
                                {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                  'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                 ]}
                                ],

    'Enc2_server_profiles_ASide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1-' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],

    'Enc2_server_profiles_BSide': [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc2-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
                                   {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc1-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc1' + ENC1 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connections': [{'id': 1, 'name': 'Conn_Vlan10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': 'Conn_Vlan30', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                     'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]}
                                   ],



    'Enc3_server_profiles_HA': [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'ENC1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan401', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan20', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                        'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}},
                                {'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 3',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Enc2-' + ENC2 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan401', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                       {'id': 2, 'name': 'Conn_Vlan403', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                        'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}},
                                {'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 2',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                              'name': 'ENC2-' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                 'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan402', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                       ]}}],

    'Enc3_server_profiles_ASide': [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1-' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan401', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan403', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG_ASide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2-' + ENC2 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan401', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan403', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ],

    'Enc3_server_profiles_BSide': [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                                 'name': 'Enc1' + ENC1 + '-bay-1', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan402', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan401', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan401', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 2',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'ENC2' + ENC2 + '-bay-2', 'description': '', 'affinity': 'Bay',
                                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                                                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan403', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}},
                                   {'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 3',
                                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:' + enc_group['Enc3-EG_BSide']['name'], 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Enc2' + ENC2 + '-bay-3', 'description': '', 'affinity': 'Bay',
                                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Disabled'},
                                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                                    'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_Vlan402', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': 'Conn_Vlan403', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500',
                                                                           'networkUri': 'ETH:Net-Vlan403', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]}}
                                   ]

}

linux_details = {"hostip": "15.245.134.7", "username": "root", "password": "rootpwd", "dir_location": "/root/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '',
               "username": 'Administrator', "password": 'hpvse123'}

module_file_path = "C:\\Checkout\\fusion\\tests\\wpst_crm\\feature_tests\\TBIRD\\OVF2760_Nitro_Storm_Control\\GetServerIPs.py"

windows_server_cred = ["Administrator", 'hpvse@1']

windows_server = {'win_ip': '',
                  "username": 'Administrator', "password": 'hpvse@1'}

server_bays = [1, 2, 3]
Server_network_ips = {server_bays[0]: "",
                      server_bays[1]: "",
                      server_bays[2]: ""}
Server_network_ips_Aside = {server_bays[0]: "", server_bays[1]: ""}

mcast_cmds = {'0': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\Multicast\\multicast_traffic_of_server1.dat",
              '1': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\Multicast\\multicast_traffic_of_server1.dat",
              '2': "C:\\Multicast\\mk_mc\\mcreceive 235.45.17.10 1234 50 > C:\\Multicast\\multicast_traffic_of_server3.dat"}

server_guid = {"1": [], "2": [], "3": []}

outputfile_guid_server = {0: "C:\\interface_traffic_of_server1.dat", 10: "C:\\second_interface_traffic_of_server1.dat", 1: "C:\\Interface_traffic_of_server2.dat",
                          2: "C:\\Interface_traffic_of_server3.dat", 12: "C:\\second_interface_traffic_of_server3.dat", 11: "C:\\second_Interface_traffic_of_server2.dat"}

wdump_cmds = {'0': "C:\\Multicast\\mk_mc\\WinDump.exe -c 200 -i ",
              '1': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -i ",
              '2': "C:\\Multicast\\mk_mc\\WinDump.exe -c 150 -i "}

msender = "C:\\Multicast\\mcast\\bin\\msender 235.45.17.10 1234 > sender.txt"

interface_guid_cmd = "C:\\Multicast\\mk_mc\\mk_get_guid.bat > "
US_Check = 'US_Vlan10'
Port_Check = 'Q5'
interconnectname_1 = 'MXQ81804ZF, interconnect 3'
interconnectname_2 = 'MXQ81804ZH, interconnect 6'
Alert_Message_Port = 'A packet storm has been detected on uplink set %s, ports {"name":"%s","uri":"IC_uri"}: %s. All packets causing the storm will be discarded until the packet rate drops below the specified threshold of 3 packets per second.' % (US_Check, interconnectname_1, Port_Check)
Port_Check1 = 'Q5'
US_Check1 = 'US_Vlan30'
Alert_Message_Port1 = 'A packet storm has been detected on uplink set %s, ports {"name":"%s","uri":"IC_uri"}: %s. All packets causing the storm will be discarded until the packet rate drops below the specified threshold of 3 packets per second.' % (US_Check1, interconnectname_1, Port_Check1)
US_Check2 = 'US_Vlan20'
Alert_Message_Port_Bside = 'A packet storm has been detected on uplink set %s, ports {"name":"%s","uri":"IC_uri"}: %s. All packets causing the storm will be discarded until the packet rate drops below the specified threshold of 3 packets per second.' % (US_Check2, interconnectname_2, Port_Check1)
downlink_Port_Check = 'd3'


server1_guids_keys = ['Ethernet1', 'Ethernet2']
server2_guids_keys = ['Ethernet1', 'Ethernet2']
server3_guids_keys = ['Ethernet1', 'Ethernet2', 'Ethernet3']

broadcast_command_B_Side = "C:\\stormControl\\hping.exe -c 20000 -i 1 --fast 10.4.2.255"
broadcast_command = "C:\\stormControl\\hping.exe -c 20000 -i 1 --fast 10.4.1.255"
multicast_command = "C:\\stormControl\\iperf.exe -c 224.0.55.55 -u --ttl 5 -t 60 -P 20"

disable_interface_B_Side = "netsh interface set interface Ethernet3 disabled"
enable_interface_B_Side = "netsh interface set interface Ethernet3 enabled"
disable_interface_Aside = "netsh interface set interface Network disabled"
enable_interface_Aside = "netsh interface set interface Network enabled"
disable_interface = "netsh interface set interface Network 3 disabled"
enable_interface = "netsh interface set interface Network 3 enabled"
IP1 = '192.168.10.22'

dlf_test_blade_downlinkport = "d27"
dlf_test_blade_uplinkport = "Q3"
dlf_test_blade_uplinkport1 = "Q5"
dlf_test_blade_uplinkport2 = 'Q6'
bcast_blade_downlinkport = "d1"

valDict = {'status_code': 200, 'taskState': 'Completed'}

delete_route_command = "route delete 224.0.0.0"
set_route_command = "route add 224.0.0.0 mask 240.0.0.0 172.16.1.25"
set_route_command1 = "route add 224.0.0.0 mask 240.0.0.0 172.16.2.25"

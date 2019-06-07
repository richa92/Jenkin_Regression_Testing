from data_common import *

###
# Interconnect bays configurations
# 2 Enclosure
###

Enc2_NonRedundant_ASide_CL10 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2_NonRedundant_ASide_CL20 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2_NonRedundant_BSide_CL10_Potash_On_Same_Enclosure = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2_NonRedundant_BSide_CL10_Potash_On_Different_Enclosure = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    ]

Enc2_NonRedundant_BSide_CL20_Potash_On_Same_Enclosure = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2_NonRedundant_BSide_CL20_Potash_On_Different_Enclosure = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    ]

Enc2_Redundant_CL10 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2_Redundant_CL20 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2_HA_CL10 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    ]

Enc2_HA_CL20 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    ]

###
# Interconnect bays configurations
# 4 Enclosure
###

Enc4_NonRedundant_ASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
    ]

Enc4_NonRedundant_BSide_Potash_On_Same_Enclosure = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
    ]

Enc4_NonRedundant_BSide_Potash_On_Different_Enclosure = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
    ]

Enc4_Redundant = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
    ]

Enc4_HA = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 4},
    ]

###
# LIGs for all 2 and 4 enclosure setups
###

ligs = {
    'Enc2-NonRedundant-ASide-CL10-LIG': {
        'name': 'Enc2-NonRedundant-ASide-CL10-LIG',
        'interconnectMapTemplate': Enc2_NonRedundant_ASide_CL10,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
    },
    'Enc2-NonRedundant-BSide-CL10-Potash-On-Same-Enclosure-LIG': {
        'name': 'Enc2-NonRedundant-BSide-CL10-Potash-On-Same-Enclosure-LIG',
        'interconnectMapTemplate': Enc2_NonRedundant_BSide_CL10_Potash_On_Same_Enclosure,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
    },
    'Enc2-NonRedundant-BSide-CL10-Potash-On-Different-Enclosure-LIG': {
        'name': 'Enc2-NonRedundant-BSide-CL10-Potash-On-Different-Enclosure-LIG',
        'interconnectMapTemplate': Enc2_NonRedundant_BSide_CL10_Potash_On_Different_Enclosure,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
    },
    'Enc2-NonRedundant-ASide-CL20-LIG': {
        'name': 'Enc2-NonRedundant-ASide-CL20-LIG',
        'interconnectMapTemplate': Enc2_NonRedundant_ASide_CL20,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
    },
    'Enc2-NonRedundant-BSide-CL20-Potash-On-Same-Enclosure-LIG': {
        'name': 'Enc2-NonRedundant-BSide-CL20-Potash-On-Same-Enclosure-LIG',
        'interconnectMapTemplate': Enc2_NonRedundant_BSide_CL20_Potash_On_Same_Enclosure,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
    },
    'Enc2-NonRedundant-BSide-CL20-Potash-On-Different-Enclosure-LIG': {
        'name': 'Enc2-NonRedundant-BSide-CL20-Potash-On-Different-Enclosure-LIG',
        'interconnectMapTemplate': Enc2_NonRedundant_BSide_CL20_Potash_On_Different_Enclosure,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
    },
    'Enc2-Redundant-CL10-LIG': {
        'name': 'Enc2-Redundant-CL10-LIG',
        'interconnectMapTemplate': Enc2_Redundant_CL10,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
    },
    'Enc2-Redundant-CL20-LIG': {
        'name': 'Enc2-Redundant-CL20-LIG',
        'interconnectMapTemplate': Enc2_Redundant_CL20,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
    },
    'Enc2-HA-CL10-LIG': {
        'name': 'Enc2-HA-CL10-LIG',
        'interconnectMapTemplate': Enc2_HA_CL10,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
    },
    'Enc2-HA-CL20-LIG': {
        'name': 'Enc2-HA-CL20-LIG',
        'interconnectMapTemplate': Enc2_HA_CL20,
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
    },
    'Enc4-NonRedundant-ASide-LIG': {
        'name': 'Enc4-NonRedundant-ASide-LIG',
        'interconnectMapTemplate': Enc4_NonRedundant_ASide,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantASide',
    },
    'Enc4-NonRedundant-BSide-Potash-On-Same-Enclosure-LIG': {
        'name': 'Enc4-NonRedundant-BSide-Potash-On-Same-Enclosure-LIG',
        'interconnectMapTemplate': Enc4_NonRedundant_BSide_Potash_On_Same_Enclosure,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
    },
    'Enc4-NonRedundant-BSide-Potash-On-Different-Enclosure-LIG': {
        'name': 'Enc4-NonRedundant-BSide-Potash-On-Different-Enclosure-LIG',
        'interconnectMapTemplate': Enc4_NonRedundant_BSide_Potash_On_Different_Enclosure,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'NonRedundantBSide',
    },
    'Enc4-Redundant-LIG': {
        'name': 'Enc4-Redundant-LIG',
        'interconnectMapTemplate': Enc4_Redundant,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
    },
    'Enc4-HA-LIG': {
        'name': 'Enc4-HA-LIG',
        'interconnectMapTemplate': Enc4_HA,
        'enclosureIndexes': [1, 2, 3, 4],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
    },
}

#####
# Enclosure Groups
#####

enc_group = {
    'Enc2-NonRedundant-CL10-Potash-On-Same-Enclosure-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-ASide-CL10-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-BSide-CL20-Potash-On-Same-Enclosure-LIG'}
        ],
    },
    'Enc2-NonRedundant-CL10-Potash-On-Different-Enclosure-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-ASide-CL10-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-BSide-CL20-Potash-On-Different-Enclosure-LIG'}
        ],
    },
    'Enc2-NonRedundant-CL20-Potash-On-Same-Enclosure-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-ASide-CL20-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-BSide-CL10-Potash-On-Same-Enclosure-LIG'}
        ],
    },
    'Enc2-NonRedundant-CL20-Potash-On-Different-Enclosure-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-ASide-CL20-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-NonRedundant-BSide-CL10-Potash-On-Different-Enclosure-LIG'}
        ],
    },
    'Enc2-Redundant-CL10-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-Redundant-CL10-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-Redundant-CL10-LIG'}
        ],
    },
    'Enc2-Redundant-CL20-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-Redundant-CL20-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-Redundant-CL20-LIG'}
        ],
    },
    'Enc2-HA-CL10-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-HA-CL10-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-HA-CL10-LIG'}
        ],
    },
    'Enc2-HA-CL20-EG': {
        'name': 'Enc2-EG',
        'enclosureCount': 2,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-HA-CL20-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-HA-CL20-LIG'}
        ],
    },
    'Enc4-NonRedundant-Potash-On-Same-Enclosure-EG': {
        'name': 'Enc4-EG',
        'enclosureCount': 4,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-NonRedundant-ASide-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-NonRedundant-BSide-Potash-On-Same-Enclosure-LIG'}
        ],
    },
    'Enc4-NonRedundant-Potash-On-Different-Enclosure-EG': {
        'name': 'Enc4-EG',
        'enclosureCount': 4,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-NonRedundant-ASide-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-NonRedundant-BSide-Potash-On-Different-Enclosure-LIG'}
        ],
    },
    'Enc4-Redundant-EG': {
        'name': 'Enc4-EG',
        'enclosureCount': 4,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-Redundant-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-Redundant-LIG'}
        ],
    },
    'Enc4-HA-EG': {
        'name': 'Enc4-EG',
        'enclosureCount': 4,
        'interconnectBayMappings': [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc4-HA-LIG'},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc4-HA-LIG'}
        ],
    },
}

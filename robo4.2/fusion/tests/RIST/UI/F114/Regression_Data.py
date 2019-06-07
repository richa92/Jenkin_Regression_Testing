enc_names = ['CN754406XL', 'CN754404R6', 'CN754406WB']
enc_list = ["ENC:%s" % enc for enc in enc_names]
LI = {'name': 'LE_SYNERGY-LIG_POTASH'}
LIG1 = 'LIG_POTASH'

uplink_sets = {
                'us_tagged_1': {
                    'name': 'us_tagged',
                    'ethernetNetworkType': 'Tagged',
                    'networkType': 'Ethernet',
                    'networkUris': ['dev101-management','dev102-vmmigration','dev103-ft-a','dev104'],
                    'nativeNetworkUri': None,
                    'mode': 'Auto',
                    'lacpTimer': 'Long',
                    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1:1', 'speed': 'Auto'}, ]
                },
            }

icmap = {
                'LIG_POTASH': [
                    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
                ],
                'LIG_SAS': [
                    {'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                    {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
                ],
            }

LIG = [
                {
                    'name': 'LIG_POTASH',
                    'type': 'logical-interconnect-groupV300',
                    'enclosureType': 'SY12000',
                    'interconnectMapTemplate': icmap['LIG_POTASH'],
                    'enclosureIndexes': [1, 2, 3],
                    'internalNetworkUris': ['dev100'],
                    'interconnectBaySet': 3,
                    'redundancyType': 'HighlyAvailable',
                    'fcoeSettings': {'fcoeMode': 'FcfNpv'},
                    'stackingMode': 'Enclosure',
                    'ethernetSettings': None,
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': None,
                    'uplinkSets': [uplink_sets['us_tagged_1'].copy(), ],

                }
            ]

SAS_LIG = [
                {
                    "name": "LIG_SAS",
                    "state": "Active",
                    "type": "sas-logical-interconnect-group",
                    "enclosureType": "SY12000",
                    "interconnectMapTemplate": icmap["LIG_SAS"],
                    "enclosureIndexes": [1],
                    "interconnectBaySet": 1,
                }
            ]

EG = [
                {
                    'name': 'EG_SYNERGY',
                    'type': 'EnclosureGroupV300',
                    'enclosureCount': 3,
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'interconnectBayMappingCount': 3,
                    'configurationScript': None,
                    'interconnectBayMappings':
                    [
                        {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG[0]["name"]},
                        {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG[0]["name"]},
                        {"interconnectBay": 1, "enclosureIndex": 1, "logicalInterconnectGroupUri": "SASLIG:" + SAS_LIG[0]["name"]},
                        {"interconnectBay": 4, "enclosureIndex": 1, "logicalInterconnectGroupUri": "SASLIG:" + SAS_LIG[0]["name"]}
                    ],
                    'ipAddressingMode': "External",
                    'ipRangeUris': [],
                    'powerMode': "RedundantPowerFeed"
                }
            ]

LE = {"name": "LE_SYNERGY",
                  "enclosureUris": enc_list,
                  "enclosureGroupUri": "EG:" + EG[0]["name"],
                  "firmwareBaselineUri": None,
                  "forceInstallFirmware": False}
ENC_1 = 'CN754404R1'
ENC_2 = 'CN754406W2'
ENC_3 = 'CN754404R5'
ENC_4 = 'CN754404QX'
ENC_5 = 'CN7544044D'

appliance_ip = '15.245.131.152'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

networks = {
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-networkV1'
}

ns_dto = {
    'type': 'network-setV4',
    'networkUris': None
}

les = {
    'name': 'LE',
    'enclosureUris': [ENC_1, ENC_2, ENC_3, ENC_4, ENC_5],
    'enclosureGroupUri': 'Enc5-EG',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}

uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': None,
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '2', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '5', 'port': 'Q6', 'speed': 'Auto'}
    ]
}

###
# Interconnect bays configurations
# 2 Enclosure, Fabric 2
###

Enc5Map = \
    [
        {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 2, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 5, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 2, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 5, 'enclosure': 4, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 2, 'enclosure': 5, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 5, 'enclosure': 5, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 5},
    ]

###
# Logical Interconnect Groups
###
lig = {
    'name': 'Enc5-LIG',
    'interconnectMapTemplate': Enc5Map,
    'enclosureIndexes': [1, 2, 3, 4, 5],
    'interconnectBaySet': 2,
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [uplink_set],
}


###
# Enclosure Groups
###
enc_group = {
    'name': 'Enc5-EG',
    'enclosureCount': 5,
    'interconnectBayMappings': [
        {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
        {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:Enc5-LIG'},
        {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
    ]
}

###
# Server profiles
###
Profiles = [
    {
        'payload': {
            'name': 'Profile1',
            'serverHardwareUri': ENC_1 + ', bay 3',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'Enc5-EG',
            'connectionSettings': {
                    'connections': [
                        {	'name': 'conn1',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-a',
                          'networkUri': 'LNS_1',
                                        'lagName': 'LAG1'
                          },
                        {	'name': 'conn2',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-a',
                          'networkUri': 'LNS_1',
                          'lagName': 'LAG1'
                          },
                        {	'name': 'conn3',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-b',
                          'networkUri': 'LNS_9',
                          },
                        {	'name': 'conn4',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-c',
                          'networkUri': 'LNS_10',
                          },
                        {	'name': 'conn5',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-d',
                          'networkUri': 'LNS_11',
                          },
                        {	'name': 'conn6',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-e',
                          'networkUri': 'LNS_12',
                          },
                        {	'name': 'conn7',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-f',
                          'networkUri': 'LNS_13',
                          },
                        {	'name': 'conn8',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-g',
                          'networkUri': 'LNS_14',
                          },
                        {	'name': 'conn9',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-h',
                          'networkUri': 'LNS_15',
                          },
                        {	'name': 'conn10',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-b',
                          'networkUri': 'LNS_16',
                          },
                        {	'name': 'conn11',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-c',
                          'networkUri': 'LNS_17',
                          },
                        {	'name': 'conn12',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-d',
                          'networkUri': 'LNS_18',
                          },
                        {	'name': 'conn13',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-e',
                          'networkUri': 'LNS_19',
                          },
                        {	'name': 'conn14',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-f',
                          'networkUri': 'LNS_20',
                          },
                        {	'name': 'conn15',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-g',
                          'networkUri': 'LNS_21',
                          },
                        {	'name': 'conn16',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-h',
                          'networkUri': 'LNS_22',
                          }
                    ]
            }
        },
        'ILO': '15.245.132.177',
    },
    {
        'payload': {
            'name': 'Profile2',
            'serverHardwareUri': ENC_1 + ', bay 2',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'Enc5-EG',
            'connectionSettings': {
                    'connections': [
                        {	'name': 'conn1',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-a',
                          'networkUri': 'LNS_2',
                          },
                        {	'name': 'conn2',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-b',
                          'networkUri': 'LNS_23',
                          },
                        {	'name': 'conn3',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-c',
                          'networkUri': 'LNS_24',
                          },
                        {	'name': 'conn4',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-d',
                          'networkUri': 'RNS_1',
                          },
                        {	'name': 'conn5',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-e',
                          'networkUri': 'LNS_25',
                          },
                        {	'name': 'conn6',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-f',
                          'networkUri': 'LNS_26',
                          },
                        {	'name': 'conn7',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-g',
                          'networkUri': 'LNS_27',
                          },
                        {	'name': 'conn8',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-h',
                          'networkUri': 'RNS_2',
                          },
                        {	'name': 'conn9',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-a',
                          'networkUri': 'LNS_3',
                          },
                        {	'name': 'conn10',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-b',
                          'networkUri': 'LNS_28',
                          },
                        {	'name': 'conn11',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-c',
                          'networkUri': 'LNS_29',
                          },
                        {	'name': 'conn12',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-d',
                          'networkUri': 'LNS_30',
                          },
                        {	'name': 'conn13',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-e',
                          'networkUri': 'LNS_31',
                          },
                        {	'name': 'conn14',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-f',
                          'networkUri': 'LNS_32',
                          },
                        {	'name': 'conn15',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-g',
                          'networkUri': 'LNS_33',
                          },
                        {	'name': 'conn16',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-h',
                          'networkUri': 'LNS_34',
                          }
                    ]
            }
        }
    },
    {
        'payload': {
            'name': 'Profile3',
            'serverHardwareUri': ENC_1 + ', bay 4',
            'enclosureUri': ENC_1,
            'enclosureGroupUri': 'Enc5-EG',
            'connectionSettings': {
                    'connections': [
                        {	'name': 'conn1',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-a',
                          'networkUri': 'LNS_4',
                          },
                        {	'name': 'conn2',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-b',
                          'networkUri': 'LNS_35',
                          },
                        {	'name': 'conn3',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-c',
                          'networkUri': 'LNS_36',
                          },
                        {	'name': 'conn4',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-d',
                          'networkUri': 'LNS_37',
                          },
                        {	'name': 'conn5',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-e',
                          'networkUri': 'LNS_38',
                          },
                        {	'name': 'conn6',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-f',
                          'networkUri': 'LNS_39',
                          },
                        {	'name': 'conn7',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-g',
                          'networkUri': 'LNS_40',
                          },
                        {	'name': 'conn8',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-h',
                          'networkUri': 'LNS_41',
                          },
                        {	'name': 'conn9',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-a',
                          'networkUri': 'LNS_5',
                          },
                        {	'name': 'conn10',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-b',
                          'networkUri': 'LNS_42',
                          },
                        {	'name': 'conn11',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-c',
                          'networkUri': 'LNS_43',
                          },
                        {	'name': 'conn12',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-d',
                          'networkUri': 'LNS_44',
                          },
                        {	'name': 'conn13',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-e',
                          'networkUri': 'LNS_45',
                          },
                        {	'name': 'conn14',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-f',
                          'networkUri': 'LNS_46',
                          },
                        {	'name': 'conn15',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-g',
                          'networkUri': 'LNS_47',
                          },
                        {	'name': 'conn16',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-h',
                          'networkUri': 'LNS_48',
                          },
                    ]
            }
        },
    },
    {
        'payload': {
            'name': 'Profile4',
            'serverHardwareUri': ENC_2 + ', bay 2',
            'enclosureUri': ENC_2,
            'enclosureGroupUri': 'Enc5-EG',
            'connectionSettings': {
                    'connections': [
                        {	'name': 'conn1',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-a',
                          'networkUri': 'LNS_6',
                          },
                        {	'name': 'conn2',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-b',
                          'networkUri': 'LNS_49',
                          },
                        {	'name': 'conn3',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-c',
                          'networkUri': 'LNS_50',
                          },
                        {	'name': 'conn4',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-d',
                          'networkUri': 'LNS_51',
                          },
                        {	'name': 'conn5',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-e',
                          'networkUri': 'LNS_52',
                          },
                        {	'name': 'conn6',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-f',
                          'networkUri': 'LNS_53',
                          },
                        {	'name': 'conn7',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-g',
                          'networkUri': 'LNS_54',
                          },
                        {	'name': 'conn8',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:1-h',
                          'networkUri': 'LNS_55',
                          },
                        {	'name': 'conn9',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-a',
                          'networkUri': 'LNS_7',
                          },
                        {	'name': 'conn10',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-b',
                          'networkUri': 'LNS_56',
                          },
                        {	'name': 'conn11',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-c',
                          'networkUri': 'LNS_57',
                          },
                        {	'name': 'conn12',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-d',
                          'networkUri': 'LNS_58',
                          },
                        {	'name': 'conn13',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-e',
                          'networkUri': 'LNS_59',
                          },
                        {	'name': 'conn14',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-f',
                          'networkUri': 'LNS_60',
                          },
                        {	'name': 'conn15',
                          'functionType': 'Ethernet',
                          'portId': 'Mezz 2:2-g',
                          'networkUri': 'LNS_61',
                          },
                    ]
            }
        },
    }]

add_connection = {
    'name': 'added_connection',
    'functionType': 'Ethernet',
    'portId': 'Mezz 2:2-g',
    'networkUri': 'LNS_8',
}

add_connection2 = {
    'name': 'added_connection2',
    'functionType': 'Ethernet',
    'portId': 'Mezz 2:2-h',
    'networkUri': 'LNS_62',
}

duplicate_connection = {
    'name': 'duplicate_connection',
    'functionType': 'Ethernet',
    'portId': 'Mezz 2:2-h',
    'networkUri': 'LNS_9',
}
'''
Nitro Data File For OVF6852
'''
ENC_1 = 'MXQ81804ZF'
ENC_2 = 'MXQ81804ZH'
ENC_3 = 'MXQ81804ZG'

appliance_ip = '15.245.131.251'
user = {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

network = {
    'purpose': 'Management',
    'smartLink': False,
    'privateNetwork': False,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'
}

networks = {
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-networkV2'
}

ns_dto = {
    'type': 'network-setV5',
    'networkUris': None
}

uplink_set = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': None,
    'networkSetUris': ['RNS_401'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
    ]
}

###
# Interconnect bays configurations
# 3 Enclosure, Fabric 3
###

Enc3Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
    ]

###
# Logical Interconnect Groups
###
lig = {
    'name': 'Enc3-LIG',
    'interconnectMapTemplate': Enc3Map,
    'enclosureIndexes': [1, 2, 3],
    'interconnectBaySet': 3,
    'redundancyType': 'HighlyAvailable',
    'downlinkSpeedMode': 'SPEED_50GB',
    'uplinkSets': [uplink_set],
}


###
# Enclosure Groups
###
enc_group = {
    'name': 'Enc3-EG',
    'enclosureCount': 3,
    'interconnectBayMappings': [
        {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'},
        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc3-LIG'}
    ]
}

les = {
    'name': 'LE',
    'enclosureUris': [ENC_1, ENC_2, ENC_3],
    'enclosureGroupUri': 'Enc3-EG',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}

###
# Server profile
###
profile = {
    'name': 'Profile1',
    'serverHardwareUri': ENC_1 + ', bay 1',
    'enclosureUri': ENC_1,
    'enclosureGroupUri': 'Enc3-EG',
    'connectionSettings': {
        'connections': [
            {
                'name': 'conn1',
                'functionType': 'Ethernet',
                'portId': 'Mezz 3:1-a',
                'networkUri': 'RNS_401',
            }
        ]
    }
}
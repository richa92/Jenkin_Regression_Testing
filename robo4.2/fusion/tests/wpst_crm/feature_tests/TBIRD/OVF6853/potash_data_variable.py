'''
Potash Data File For OVF6853
'''
ENC_1 = 'CN7544044G'
ENC_2 = 'CN7545084V'

appliance_ip = '15.245.131.72'
user = {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}


def make_range_list(start, end, prefix='net_', suffix=''):
    """ Make Range List
    [Arguments]
    start: start number
    end: end number
    prefix: prefix
    suffix:  	suffix
    [Example]
    Make Range List	start	end	prefix	suffix
    """
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


networks_list = make_range_list(401, 501)

network = {
    "purpose": "Management",
    "smartLink": False,
    "privateNetwork": False,
    "ethernetNetworkType": "Tagged",
    "type": "ethernet-networkV4"
}

bulk_networks = {
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

uplink_set_1 = {
    'name': 'US1',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_499'],
    'mode': 'Auto',
    'nativeNetworkUri': None,
    'logicalPortConfigInfos': [
        {'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
        {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}
    ]
}

add_uplinkset = {
    'name': 'US2',
    'type': 'uplink-setV6',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_460', 'net_401', 'net_402', 'net_403', 'net_404', 'net_405', 'net_406', 'net_407', 'net_408', 'net_409', 'net_410'],
    'networkSetUris': ['RNS_1'],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
                {
                    'desiredSpeed': 'Auto',
                    'location': {
                      'locationEntries': [
                          {
                              'value': 'Q3',
                              'type': 'Port'
                          },
                          {
                              'value': '3',
                              'type': 'Bay'
                          },
                          {
                              'value': ENC_1,
                              'type': 'Enclosure'
                          }
                      ]
                    }
                }
    ],
}
uplink_set_duplicate_networks = {
    'name': 'uplink_set_duplicate_networks',
    'type': 'uplink-setV6',
    'ethernetNetworkType': 'Tagged',
    'networkType': 'Ethernet',
    'networkUris': ['net_460', 'net_401', 'net_402', 'net_403', 'net_404', 'net_405', 'net_406', 'net_407', 'net_408', 'net_409', 'net_410'],
    'networkSetUris': ['RNS_1'],
    'manualLoginRedistributionState': 'NotSupported',
    'connectionMode': 'Auto',
    'portConfigInfos': [
        {
            'desiredSpeed': 'Auto',
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
                              'value': ENC_1,
                              'type': 'Enclosure'
                          }
                      ]
            }
        }
    ]
}

###
# Interconnect bays configurations
# 2 Enclosure, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    ]

###
# Logical Interconnect Groups
###
lig = {
    'name': 'Enc2-LIG',
    'interconnectMapTemplate': Enc2Map,
    'enclosureIndexes': [1, 2],
    'interconnectBaySet': 3,
    'internalNetworkUris': ['net_430'],
    'redundancyType': 'HighlyAvailable',
    'uplinkSets': [uplink_set_1]
}


###
# Enclosure Groups
###
enc_group = {
    'name': 'Enc2-EG',
    'enclosureCount': 2,
    'interconnectBayMappings': [
        {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'},
        {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Enc2-LIG'}
    ]
}

les = {
    'name': 'LE',
    'enclosureUris': [ENC_1, ENC_2],
    'enclosureGroupUri': 'Enc2-EG',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}

###
# Server profile
###
Profiles = {
    'name': 'Profile1',
    'serverHardwareUri': ENC_1 + ', bay 1',
    'enclosureUri': ENC_1,
    'enclosureGroupUri': 'Enc2-EG',
    'connectionSettings': {
        'connections': [
            {
                'name': 'conn1',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'networkUri': 'RNS_401',
            }
        ]
    }
}

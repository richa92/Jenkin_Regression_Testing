def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist

SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'
FUSION_PASSWORD = 'hpvse123'
FUSION_SSH_USERNAME = 'root'
FUSION_SSH_PASSWORD = 'hpvse1'


FUSION_PROMPT = '#'
FUSION_TIMEOUT = 180
FUSION_NIC = 'bond0'
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN 106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'portmon.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'], 'locale': 'en_US.UTF-8'}

user_single = {
    'emailAddress': 'user01@hpe.com',
    'enabled': True,
    'fullName': 'user01',
    'mobilePhone': '09876543210',
    'officePhone': '12345678900',
    'password': 'asdf@1230',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user01'
}

users = [{
    'emailAddress': 'user1@hpe.com',
    'enabled': True,
    'fullName': 'user1',
    'mobilePhone': '09876543211',
    'officePhone': '12345678901',
    'password': 'asdf@1231',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user1'
},
    {
    'emailAddress': 'user2@hpe.com',
    'enabled': True,
    'fullName': 'user2',
    'mobilePhone': '09876543212',
    'officePhone': '12345678902',
    'password': 'asdf@1232',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user2'
},
    {
    'emailAddress': 'user3@hpe.com',
    'enabled': True,
    'fullName': 'user3',
    'mobilePhone': '09876543213',
    'officePhone': '12345678903',
    'password': 'asdf@1233',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user3'
},
    {
    'emailAddress': 'user4@hpe.com',
    'enabled': True,
    'fullName': 'user4',
    'mobilePhone': '09876543214',
    'officePhone': '12345678904',
    'password': 'asdf@1234',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user4'
},
    {
    'emailAddress': 'user5@hpe.com',
    'enabled': True,
    'fullName': 'user5',
    'mobilePhone': '09876543215',
    'officePhone': '12345678905',
    'password': 'asdf@1235',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user5'
},
    {
    'emailAddress': 'user6@hpe.com',
    'enabled': True,
    'fullName': 'user6',
    'mobilePhone': '09876543216',
    'officePhone': '12345678906',
    'password': 'asdf@1236',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user6'
},
    {
    'emailAddress': 'user7@hpe.com',
    'enabled': True,
    'fullName': 'user7',
    'mobilePhone': '09876543217',
    'officePhone': '12345678907',
    'password': 'asdf@1237',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user7'
},
    {
    'emailAddress': 'user8@hpe.com',
    'enabled': True,
    'fullName': 'user8',
    'mobilePhone': '09876543218',
    'officePhone': '12345678908',
    'password': 'asdf@1238',
    'roles': ['Read only'],
    'type': 'UserAndRoles',
    'userName': 'user8'
}]

fcnets = [
    {
        "type": "fc-networkV4",
        "name": "FC_1",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_2",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_3",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_4",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_5",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_6",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_7",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_8",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_9",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_10",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_11",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_12",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    }
]

mul_fcnets = [
    {
        "type": "fc-networkV4",
        "name": "FC_01",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_02",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_03",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_04",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_05",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_06",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_07",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_08",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_09",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    },
    {
        "type": "fc-networkV4",
        "name": "FC_010",
        "fabricType": "FabricAttach",
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True
    }
]

uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed16G'}]},
               'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Speed8G'}]},
               'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Speed4G'}]},
               }

lig_uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]},
                   'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Speed16G'}]},
                   'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '3', 'speed': 'Speed8G'}]},
                   'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '4', 'speed': 'Speed4G'}]},
                   'UplinkSet_5': {'name': 'UplinkSet_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_5'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '5', 'speed': 'Auto'}]},
                   'UplinkSet_6': {'name': 'UplinkSet_6', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_6'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'}]},
                   'UplinkSet_7': {'name': 'UplinkSet_7', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_7'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'}]},
                   'UplinkSet_8': {'name': 'UplinkSet_8', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_8'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'}]},
                   'UplinkSet_9': {'name': 'UplinkSet_9', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_9'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'}]},
                   'UplinkSet_10': {'name': 'UplinkSet_10', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_10'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q2.1', 'speed': 'Auto'}]},
                   'UplinkSet_11': {'name': 'UplinkSet_11', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_11'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q3.1', 'speed': 'Auto'}]},
                   'UplinkSet_12': {'name': 'UplinkSet_12', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_12'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q4.1', 'speed': 'Auto'}]},
                   }

LIG1 = 'LIG_1-1'
LIG2 = 'LIG_2-1'
LIG3 = 'LIG_3'
ligs = {'lig1':
        {'name': 'LIG_1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy(), uplink_sets['UplinkSet_3'].copy(), uplink_sets['UplinkSet_4'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         },
        'lig2':
        {'name': 'LIG_2',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         },
        'lig3':
        {'name': 'LIG_3',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_sets['UplinkSet_2'].copy(), lig_uplink_sets['UplinkSet_3'].copy(),
                        lig_uplink_sets['UplinkSet_4'].copy(), lig_uplink_sets['UplinkSet_5'].copy(), lig_uplink_sets['UplinkSet_6'].copy(),
                        lig_uplink_sets['UplinkSet_7'].copy(), lig_uplink_sets['UplinkSet_8'].copy(), lig_uplink_sets['UplinkSet_9'].copy(),
                        lig_uplink_sets['UplinkSet_10'].copy(), lig_uplink_sets['UplinkSet_11'].copy(), lig_uplink_sets['UplinkSet_12'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         }
        }
PROFILE = 'CN7545049F_Bay1-Carbon'
ENC1 = 'CN7545049F'
enc_groups = {'enc_group1':
              {'name': 'EG_1',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_1'}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'ambientTemperatureMode': 'Standard',
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group2':
              {'name': 'EG_2',
               'enclosureCount': 1,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_2'},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_2'}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'ambientTemperatureMode': 'Standard',
               'powerMode': 'RedundantPowerFeed'
               }
              }

LE1 = 'LE_1'
LE2 = 'LE_2'
les = {'le1':
       {'name': 'LE_1',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG_1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       'le2':
       {'name': 'LE_2',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG_2',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       }

li_uplink_sets = [{'name': 'us1',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_1'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us2',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_2'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us3',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_3'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '3', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us4',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_4'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '4', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us5',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_5'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us6',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_6'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '6', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us7',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_7'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '7', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us8',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_8'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '8', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us9',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_9'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': 'Q1:1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us10',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_10'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': 'Q2:1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us11',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_11'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': 'Q3:1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  {'name': 'us12',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_12'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': 'Q4:1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]
                   }
                  ]

server_profiles = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': PROFILE, 'description': 'Server using Carbon', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'bootMode': None,
                    'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1'},
                                    {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2'},
                                    ]}
                   ]

server_profiles_4Gb = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                        'name': PROFILE, 'description': 'Server using Carbon', 'affinity': 'Bay',
                        'boot': {'manageBoot': False},
                        'bootMode': None,
                        'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '4000', 'networkUri': 'FC:FC_1'},
                                        {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'None', 'requestedMbps': '4000', 'networkUri': 'FC:FC_2'}
                                        ]}
                       ]


true = True
false = False


"""
default_variables = {'admin_credentials': admin_credentials,
                     'appliance': appliance,
                     'encs': encs,
                     'enc_groups': enc_groups,
                     'ethernet_networks': ethernet_networks,
                     'ethernet_ranges': ethernet_ranges,
                     'fc_networks': fc_networks,
                     'fcoe_networks': fcoe_networks,
                     'fcoe_ranges': fcoe_ranges,
                     'les': les,
                     'licenses': licenses,
                     'ligs': ligs,
                     'network_sets': network_sets,
                     'network_set_ranges': network_set_ranges,
                     'ranges': ranges,
                     'rc': rc,
                     'server_profiles': server_profiles,
                     'uplink_sets': uplink_sets,
                     'users': users,
                     'timeandlocale': timeandlocale,
                     'true': true, 'false': false,
                     'vcenter': vcenter}


def get_variables():

    variables = default_variables
    return variables
"""

def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

admin_credentials_TB = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

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

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'readonly', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

LIGS_TB = [{'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                        ],

            'uplinkSets': [],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'readCommunity': 'public',
                                  'systemContact': '',
                                  'enabled': 'true',
                                  'category': 'snmp-configuration'
                                  }},
           {'name': 'LIG2',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                        ],

            'uplinkSets': [],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'readCommunity': 'public',
                                  'systemContact': '',
                                  'enabled': 'true',
                                  'category': 'snmp-configuration'
                                  }}
           ]


lig_type = "logical-interconnect-groupV400"

lig_body1 = {"name": "LIG_A",
             "type": "logical-interconnect-groupV400",
             "enclosureType": "C7000",
             "interconnectMapTemplate": {},
             "uplinkSets": [],
             "stackingMode": "Enclosure",
             "ethernetSettings": None,
             "state": "Active",
             "telemetryConfiguration": None,
             "snmpConfiguration": None,
             "qosConfiguration": None}


POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'readonly']

ethernet_networks = [{'name': 'net_100', 'type': 'ethernet-networkV4', 'vlanId': 100, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_101', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_102', 'type': 'ethernet-networkV4', 'vlanId': 102, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

ENC1 = 'CN754404R2'
ENC2 = 'CN754406W5'
fcoe_networks = [{'name': 'fcoe_103', 'type': 'fcoe-networkV300', 'vlanId': 103}]


les = {'name': 'LE1',
       'enclosureUris': ['ENC:' + ENC2, 'ENC:' + ENC1],
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False
       }


enc_group_TB = {'enc_group1':
                {'name': 'EG1',
                 'type': 'EnclosureGroupV300',
                 'enclosureCount': 2,
                 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                 'stackingMode': 'Enclosure',
                 'interconnectBayMappingCount': 0,
                 'configurationScript': None,
                 'interconnectBayMappings':
                 [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
                  ],
                    'ipAddressingMode': 'External',
                    'ipRangeUris': [],
                    'powerMode': 'RedundantPowerFeed'
                 }}
enc_group = [{'name': 'EG1',
              'type': 'EnclosureGroupV300',
              'enclosureTypeUri': '/rest/enclosure-types/c7000',
              'stackingMode': 'Enclosure',
              'interconnectBayMappingCount': 8,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]},
             {'name': 'EG2',
              'type': 'EnclosureGroupV400',
              'enclosureTypeUri': '/rest/enclosure-types/c7000',
              'stackingMode': 'Enclosure',
              'interconnectBayMappingCount': 8,
              'configurationScript': None,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [{'hostname': '15.199.229.76', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG1', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}, {'hostname': '15.199.229.79', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG2', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]


ENC1 = 'Enc-76'
LIG1 = 'LIG1'
BAY = '1'


ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10 Enet Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10 Enet Module'}
                                     ],
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration':None},
        {'name': 'LIG2',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}
                                     ],
         'uplinkSets': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration':None}
        ]
ls = [{'logicalSwitch': {'name': 'LS-56xx',
                         'state': 'Active',
                         'status': None,
                         'description': None,
                         'uri': None,
                         'category': None,
                         'eTag': None,
                         'created': None,
                         'modified': None,
                         'type': 'logical-switchV400',
                         'switchMap': None,
                         'logicalSwitchGroupUri': 'LSG:LSG-56xx-1',
                         'switchCredentialConfiguration': [{'snmpV1Configuration': {'communityString': 'nexus'},
                                                            'snmpV3Configuration': {'authorizationProtocol': None,
                                                                                    'privacyProtocol': None,
                                                                                    'securityLevel': None},
                                                            'logicalSwitchManagementHost': '15.199.203.171',
                                                            'snmpVersion': 'SNMPv1', 'snmpPort': 161}]},
       'logicalSwitchCredentials': [{'connectionProperties': [{'propertyName': 'SshBasicAuthCredentialUser',
                                                               'value': 'admin',
                                                               'valueFormat': 'Unknown',
                                                               'valueType': 'String'},
                                                              {'propertyName': 'SshBasicAuthCredentialPassword',
                                                               'value': 'HPvse123', 'valueFormat': 'SecuritySensitive',
                                                               'valueType': 'String'}]}]},
      ]

li_uplink_sets = {'us1': {'name': 'Invalid-Uses-AnalyzerPort',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['net_100'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': 'X10', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                  }

server_profiles = [{'type': 'ServerProfileV6', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                                     'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_103',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-c',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:net_102',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                   ]

ethnets = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Net1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Net2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    }
]

fcnets = [
    {
        "name": "FC1",
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    },
    {
        "name": "FC2",
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    }
]

fcoenets = [
    {
        "name": "FCoE1",
        "vlanId": "10",
        "type": "fcoe-networkV4"
    },
    {
        "name": "FCoE2",
        "vlanId": "20",
        "type": "fcoe-networkV4"
    }
]

ethnetsets = [
    {
        "name": "EthNetSet1",
        "networkUris": [],
        "type": "network-setV4",

    },
    {
        "name": "EthNetSet2",
        "networkUris": [],
        "type": "network-setV4",
    }
]

scopes = [
    {
        "name": "Scope1",
        "description": "Scope1 for testing",
        "type": "ScopeV3"
    },
    {
        "name": "Scope2",
        "description": "Scope2 for Testing",
        "type": "ScopeV3"
    }
]

serveradmin_user = {"type": "UserAndRoles", "userName": "serveradmin", "fullName": "serveradmin", "password": "serveradmin", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "roles": ["Server administrator"]}

scope_resources = {"addedResourceUris": [], "removedResourceUris": []}

scope_assignresources = [{"op": "add", "path": "/addedResourceUris/-", "value": ""}]

scope_put = {"type": "ScopeV3", "name": "", "description": "", "addedResourceUris": [], "removedResourceUris": []}


scope_removeresources = [{"op": "replace", "path": "/removedResourceUris", "value": [""]}]

patch_headers = 'application/json-patch+json'


scope_1 = [
    {
        "name": "S1",
        "description": "Scope1 for testing",
        "type": "ScopeV3"
    },
    {
        "name": "S2",
        "description": "Scope2 for Testing",
        "type": "ScopeV3"
    }
]

scope_2 = {"name": "ScopeTest",
           "description": "Scope1 for testing",
           "type": "ScopeV3"}


LSG_1 = [
    {

        "type": "logical-switch-groupV400",
        "name": "LSG-56xx-1",
        "state": "Active",
        "switchMapTemplate": {
            "switchMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "relativeValue": 1,
                        "type": "StackingMemberId"}]
                },
                "permittedSwitchTypeUri": "SW"}]}
    },
    {
        "type": "logical-switch-groupV400",
        "name": "LSG-56xx-2",
        "state": "Active",
        "switchMapTemplate": {
            "switchMapEntryTemplates": [{
                "logicalLocation": {
                    "locationEntries": [{
                        "relativeValue": 1,
                        "type": "StackingMemberId"}]},
                "permittedSwitchTypeUri": "SW"}]}
    }
]

type_switch = ["C56XX"]

Bulk_enet = {
    "vlanIdRange": "1-5",
    "namePrefix": "Enet",
    "privateNetwork": "false",
    "smartLink": "true",
    "purpose": "General",
    "type": "bulk-ethernet-network",
    "bandwidth": {
        "maximumBandwidth": 20000,
        "typicalBandwidth": 2500
    }}

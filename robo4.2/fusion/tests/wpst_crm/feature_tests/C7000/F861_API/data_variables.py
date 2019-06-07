def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

admin_credentials_TB = {'userName': 'Administrator', 'password': 'wpsthpse1'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'}],
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
enc_group2 = [{'name': 'EG1',
               'type': 'EnclosureGroupV700',
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
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}
              ]

encss = [{'hostname': '15.245.129.23', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG2', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]

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
         {'userName': 'Readonly', 'password': 'readonly', 'fullName': 'readonly', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Storageonly', 'password': 'storageonly', 'fullName': 'storageadmin', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'FullRole', 'password': 'fullroleonly', 'fullName': 'fullroleadmin', 'roles': ['Infrastructure administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Software', 'password': 'softwareonly', 'fullName': 'softwareadmin', 'roles': ['Software administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            {'userName': 'Readonly', 'password': 'readonly'},
            {'userName': 'Storageonly', 'password': 'storageonly'},
            {'userName': 'FullRole', 'password': 'fullroleonly'},
            {'userName': 'Software', 'password': 'softwareonly'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            ]


POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'readonly']


ethernet_networks = [{'name': 'net_100', 'type': 'ethernet-networkV400', 'vlanId': 100, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_101', 'type': 'ethernet-networkV400', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_102', 'type': 'ethernet-networkV400', 'vlanId': 102, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

ENC1 = 'CN754404R2'
ENC2 = 'CN754406W5'
fcoe_networks = [{'name': 'fcoe_103', 'type': 'fcoe-networkV300', 'vlanId': 103}]

les = {'le1':
       {'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }}


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
enc_group1 = {'name': 'EG2', "interconnectBayMappings": [
    {"interconnectBay": 1, "logicalInterconnectGroupUri": 'LIG:LIG1'},
    {"interconnectBay": 2, "logicalInterconnectGroupUri": 'LIG:LIG1'},
    {"interconnectBay": 3, "logicalInterconnectGroupUri": None},
    {"interconnectBay": 4, "logicalInterconnectGroupUri": None},
    {"interconnectBay": 5, "logicalInterconnectGroupUri": None},
    {"interconnectBay": 6, "logicalInterconnectGroupUri": None},
    {"interconnectBay": 7, "logicalInterconnectGroupUri": None},
    {"interconnectBay": 8, "logicalInterconnectGroupUri": None}],
    "ipRangeUris": [],
    "enclosureCount": 1,
    "osDeploymentSettings": None,
    "configurationScript": None,
    "powerMode": None,
    "ambientTemperatureMode": "Standard"}


encs = [{'hostname': '15.245.129.23', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG1', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}, {'hostname': '15.199.229.79', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG2', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]


ENC1 = 'Enc-79'
LIG3 = 'LIG2'
BAY = '1'


LIGS_TB = [{'name': 'LIG2',
            'type': 'logical-interconnect-groupV300',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'enclosureIndex': 1}
                                        ],

            'uplinkSets': [],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType':'Redundant',
            'internalNetworkUris': [],
            'qosConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'readCommunity': 'public',
                                  'systemContact': '',
                                  'enabled': 'true',
                                  'category': 'snmp-configuration'
                                  }
            }]


ls = [{'logicalSwitch': {'name': 'LS-56xx',
                         'state': 'Active',
                         'status': None,
                         'description': None,
                         'uri': None,
                         'category': None,
                         'eTag': None,
                         'created': None,
                         'modified': None,
                         'type': 'logical-switchV300',
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
        "type": "ethernet-networkV300",
        "ethernetNetworkType": "Tagged",
        "name": "Net1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV300",
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
        "type": "fc-networkV300"
    },
    {
        "name": "FC2",
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV300"
    }
]

fcoenets = [
    {
        "name": "FCoE1",
        "vlanId": "10",
        "type": "fcoe-networkV300"
    },
    {
        "name": "FCoE2",
        "vlanId": "20",
        "type": "fcoe-networkV300"
    }
]

ethnetsets = [
    {
        "name": "EthNetSet1",
        "networkUris": [],
        "type": "network-setV300",
    },
    {
        "name": "EthNetSet2",
        "networkUris": [],
        "type": "network-setV300",
    }
]

scopes = [
    {
        "name": "Scope1",
        "description": "Scope1 for testing",
        "type": "Scope"
    },
    {
        "name": "Scope2",
        "description": "Scope2 for Testing",
        "type": "Scope"
    }
]

serveradmin_user = {"type": "UserAndRoles", "userName": "serveradmin", "fullName": "serveradmin", "password": "serveradmin", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "roles": ["Server administrator"]}

scope_resources = {"addedResourceUris": [], "removedResourceUris": []}

scope_1 = [
    {
        "name": "S1",
        "description": "Scope1 for testing",
        "type": "Scope"
    },
    {
        "name": "S2",
        "description": "Scope2 for Testing",
        "type": "Scope"
    }
]

scope_2 = {"name": "ScopeTest",
           "description": "Scope1 for testing",
           "type": "Scope"}


LSG_1 = [
    {

        "type": "logical-switch-groupV300",
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
        "type": "logical-switch-groupV300",
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
LIG1 = 'LIG1'
LIG3 = 'LE1-LIG_1'
type_switch = ["C56XX"]
enc_group = [{'name': 'EG1',
              'type': 'EnclosureGroupV300',
              'enclosureTypeUri': '/rest/enclosure-types/SY12000',
              'stackingMode': 'Enclosure',
              'interconnectBayMappingCount': 2,
              'configurationScript': None,
              'powerMode': 'RedundantPowerFeed',
                           'ipAddressingMode': 'DHCP',
                           'enclosureCount': 1,
              'interconnectBayMappings':
              [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG2'},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG2'}]}]

QoS_Fcoe = {'qosConfiguration':
            {
                'activeQosConfig': {
                    'type': 'QosConfiguration',
                    'configType': 'CustomWithFCoE',
                    'uplinkClassificationType': 'DOT1P_AND_DSCP',
                    'downlinkClassificationType': 'DOT1P_AND_DSCP',
                                  'qosTrafficClassifiers': [
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '55',
                                              'egressDot1pValue': 0,
                                              'maxBandwidth': 100,
                                              'realTime': False,
                                              'className': 'Best effort',
                                              'enabled': True
                                          },
                                          'qosClassificationMapping': {
                                              'dot1pClassMapping': [
                                                  1,
                                                  0
                                              ],
                                              'dscpClassMapping':[
                                                  'DSCP 10, AF11',
                                                  'DSCP 12, AF12',
                                                  'DSCP 14, AF13',
                                                  'DSCP 8, CS1',
                                                  'DSCP 0, CS0'
                                              ]
                                          }
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '0',
                                              'egressDot1pValue': 0,
                                              'maxBandwidth': 100,
                                              'realTime': False,
                                              'className': 'Class1',
                                              'enabled': False
                                          },
                                          'qosClassificationMapping': None
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '0',
                                              'egressDot1pValue': 0,
                                              'maxBandwidth': 100,
                                              'realTime': False,
                                              'className': 'Class2',
                                              'enabled': False
                                          },
                                          'qosClassificationMapping': None
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '0',
                                              'egressDot1pValue': 0,
                                              'maxBandwidth': 100,
                                              'realTime': False,
                                              'className': 'Class4',
                                              'enabled': False
                                          },
                                          'qosClassificationMapping': None
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '10',
                                              'egressDot1pValue': 1,
                                              'maxBandwidth': 10,
                                              'realTime': False,
                                              'className': 'Class5',
                                              'enabled': True
                                          },
                                          'qosClassificationMapping': None
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': 'fcoe',
                                              'egressDot1pValue': 3,
                                              'maxBandwidth': 100,
                                              'realTime': False,
                                              'className': 'FCoE lossless',
                                              'enabled': True
                                          },
                                          'qosClassificationMapping': {
                                              'dot1pClassMapping': [
                                                  3
                                              ],
                                              'dscpClassMapping':[

                                              ]
                                          }
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '25',
                                              'egressDot1pValue': 2,
                                              'maxBandwidth': 100,
                                              'realTime': False,
                                              'className': 'Medium',
                                              'enabled': True
                                          },
                                          'qosClassificationMapping': {
                                              'dot1pClassMapping': [
                                                  4,
                                                  3,
                                                  2
                                              ],
                                              'dscpClassMapping':[
                                                  'DSCP 18, AF21',
                                                  'DSCP 20, AF22',
                                                  'DSCP 22, AF23',
                                                  'DSCP 26, AF31',
                                                  'DSCP 28, AF32',
                                                  'DSCP 30, AF33',
                                                  'DSCP 34, AF41',
                                                  'DSCP 36, AF42',
                                                  'DSCP 38, AF43',
                                                  'DSCP 16, CS2',
                                                  'DSCP 24, CS3',
                                                  'DSCP 32, CS4'
                                              ]
                                          }
                                      },
                                      {
                                          'qosTrafficClass': {
                                              'bandwidthShare': '10',
                                              'egressDot1pValue': 5,
                                              'maxBandwidth': 10,
                                              'realTime': True,
                                              'className': 'Real time',
                                              'enabled': True
                                          },
                                          'qosClassificationMapping': {
                                              'dot1pClassMapping': [
                                                  5,
                                                  6,
                                                  7
                                              ],
                                              'dscpClassMapping':[
                                                  'DSCP 46, EF',
                                                  'DSCP 40, CS5',
                                                  'DSCP 48, CS6',
                                                  'DSCP 56, CS7'
                                              ]
                                          }
                                      }
                                  ],
                    'name': None,
                    'state': None,
                    'description': None,
                    'status': None,
                    'eTag': None,
                    'category': 'qos-aggregated-configuration',
                    'uri': None
                },
                'inactiveFCoEQosConfig': None,
                'inactiveNonFCoEQosConfig': None,
                'type': 'qos-aggregated-configuration',
                'name': None,
                'state': None,
                'status': None,
                'eTag': None,
                'category': 'qos-aggregated-configuration',
                'uri': None
            }}

QoS_NoFcoe = {'qosConfiguration': {
    'activeQosConfig': {
        'type': 'QosConfiguration',
        'configType': 'CustomNoFCoE',
                'downlinkClassificationType': 'DOT1P',
                'uplinkClassificationType': 'DSCP',
                'qosTrafficClassifiers': [{
                    'qosTrafficClass': {
                        'bandwidthShare': '55',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Best effort',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [1, 0],
                        'dscpClassMapping': ['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']
                    }
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 1,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class1',
                        'enabled': True
                    },
                    'qosClassificationMapping': None
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class2',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '0',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class3',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '0',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class4',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '0',
                        'egressDot1pValue': 0,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Class5',
                        'enabled': False
                    },
                    'qosClassificationMapping': None
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '25',
                        'egressDot1pValue': 2,
                        'maxBandwidth': 100,
                        'realTime': False,
                        'className': 'Medium',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [4, 3, 2],
                        'dscpClassMapping': ['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31', 'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42', 'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']
                    }
                }, {
                    'qosTrafficClass': {
                        'bandwidthShare': '10',
                        'egressDot1pValue': 5,
                        'maxBandwidth': 10,
                        'realTime': True,
                        'className': 'Real time',
                        'enabled': True
                    },
                    'qosClassificationMapping': {
                        'dot1pClassMapping': [5, 6, 7],
                        'dscpClassMapping': ['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']
                    }
                }],
        'name': None,
        'state': None,
        'description': None,
        'status': None,
        'eTag': None,
        'category': 'qos-aggregated-configuration',
        'uri': None
    },
    'inactiveFCoEQosConfig': None,
    'inactiveNonFCoEQosConfig': None,
    'type': 'qos-aggregated-configuration',
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'qos-aggregated-configuration',
    'uri': None
}}
Li_Qos = {
    'activeQosConfig': {
        'type': 'QosConfiguration',
        'configType': 'CustomWithFCoE',
        'uplinkClassificationType': 'DOT1P',
        'downlinkClassificationType': 'DOT1P_AND_DSCP',
        'qosTrafficClassifiers': [{
            'qosTrafficClass': {
                'bandwidthShare': '65',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Best effort',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [1, 0],
                'dscpClassMapping': ['DSCP 10, AF11', 'DSCP 12, AF12', 'DSCP 14, AF13', 'DSCP 8, CS1', 'DSCP 0, CS0']
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class1',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class2',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class3',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '0',
                'egressDot1pValue': 0,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Class4',
                'enabled': False
            },
            'qosClassificationMapping': None
        }, {
            'qosTrafficClass': {
                'bandwidthShare': 'fcoe',
                'egressDot1pValue': 3,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'FCoE lossless',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [3],
                'dscpClassMapping': []
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '25',
                'egressDot1pValue': 2,
                'maxBandwidth': 100,
                'realTime': False,
                'className': 'Medium',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [4, 3, 2],
                'dscpClassMapping': ['DSCP 18, AF21', 'DSCP 20, AF22', 'DSCP 22, AF23', 'DSCP 26, AF31', 'DSCP 28, AF32', 'DSCP 30, AF33', 'DSCP 34, AF41', 'DSCP 36, AF42', 'DSCP 38, AF43', 'DSCP 16, CS2', 'DSCP 24, CS3', 'DSCP 32, CS4']
            }
        }, {
            'qosTrafficClass': {
                'bandwidthShare': '10',
                'egressDot1pValue': 5,
                'maxBandwidth': 10,
                'realTime': True,
                'className': 'Real time',
                'enabled': True
            },
            'qosClassificationMapping': {
                'dot1pClassMapping': [5, 6, 7],
                'dscpClassMapping': ['DSCP 46, EF', 'DSCP 40, CS5', 'DSCP 48, CS6', 'DSCP 56, CS7']
            }
        }],
        'name': None,
        'state': None,
        'description': None,
        'status': None,
        'eTag': None,
        'modified': None,
        'created': None,
        'category': 'qos-aggregated-configuration',
                    'uri': None
    },
    'inactiveFCoEQosConfig': None,
    'inactiveNonFCoEQosConfig': None,
    'type': 'qos-aggregated-configuration',
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'modified': None,
    'created': None,
    'category': 'qos-aggregated-configuration',
    'uri': None
}
LE = 'LE'

Logical_Enclosure = [{'name': LE,
                      'enclosureUris': ['ENC:' + ENC1],
                      'enclosureGroupUri': 'EG:EG1',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]
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

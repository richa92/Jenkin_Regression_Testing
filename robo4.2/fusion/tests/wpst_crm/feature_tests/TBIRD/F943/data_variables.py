def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}


usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            ]

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

users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {"type": "UserAndRoles", "userName": "Storageadmin", "fullName": "", "password": "Storageadmin", "emailAddress": "", "officePhone": "", "mobilePhone": "", "roles": ["Storage administrator"]},
         ]


POSITIVE_USERS = ['Administrator', 'Networkadmin']
NEGATIVE_USERS = ['Serveradmin', 'Backupadmin', 'readonly']

# licenses = [{'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
#            {'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
#            ]

ethernet_networks = [{'name': 'net_100', 'type': 'ethernet-networkV4', 'vlanId': 100, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_101', 'type': 'ethernet-networkV4', 'vlanId': 101, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'net_102', 'type': 'ethernet-networkV4', 'vlanId': 102, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

fcoe_networks = [{'name': 'fcoe_103', 'type': 'fcoe-networkV300', 'vlanId': 103}]

enc_group1 = [{'name': 'EG1',
               'enclosureCount': 1,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'ambientTemperatureMode':'Standard',
               'powerMode': 'RedundantPowerFeed'},
              {'name': 'EG2',
               'enclosureCount': 1,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG2'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'ambientTemperatureMode':'Standard',
               'powerMode': 'RedundantPowerFeed'}]

encs = [{'hostname': '15.199.229.76', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG1', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}, {'hostname': '15.199.229.79', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG2', 'force': 'true', 'licensingIntent': 'OneViewNoiLO'}]


ENC1 = 'CN754406W6'
LIG1 = 'LIG1'
LIG3 = 'LIG3'

BAY = '1'

ligs1 = [{'name': 'LIG1',
          'type': 'logical-interconnect-groupV4',
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
          'type': 'logical-interconnect-groupV4',
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

fcoe = {"name": "net2",
        "vlanId": "10",
        "type": "fcoe-networkV4"}

fcoenets = [
    {
        "name": "FCoENet",
        "vlanId": "1004",
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


uplink_sets = {'us1': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['FCoENet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['FCoENet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                  {'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}
                                                  ]},
               'us3': {'name': 'us3',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': [],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                  ]},
               'us4': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['FCoENet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': []}}


icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
         ]


# ligs = {'lig1':
# {'name': 'LIG1',
# 'type': 'logical-interconnect-groupV300',
# 'enclosureType': 'SY12000',
# 'interconnectMapTemplate': icmap,
# new
# 'enclosureIndexes': [1],
# 'interconnectBaySet':3,
# 'redundancyType': 'Redundant',
# 'redundancyType': 'NonRedundantASide',
# 'redundancyType': 'NonRedundantASide',
# 'fcoeSettings': {'fcoeMode': 'FcfNpv'},
# end new
# 'uplinkSets': [uplink_sets['Q1.1-Q6.4'].copy()],
# 'uplinkSets': [uplink_sets['us1'].copy()],
# 'stackingMode': 'Enclosure',
# 'ethernetSettings': None,
# 'state': None,
# 'telemetryConfiguration': None,
# 'snmpConfiguration': None}}

ligs = {'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': None,
         'state': None,
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig2':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['us2'].copy()],
         'ethernetSettings': None,
         'state': None,
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig3':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['us3'].copy()],
         'ethernetSettings': None,
         'state': None,
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig4':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['us4'].copy()],
         'ethernetSettings': None,
         'state': None,
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        }

enc_group = [{'name': 'EG1',
              'enclosureCount': 1,
              'ipRangeUris': [],
              'ambientTemperatureMode':'Standard',
              'powerMode': 'RedundantPowerFeed',
              'ipAddressingMode': 'DHCP',
              'interconnectBayMappings':
              [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG1'},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG1'}]}]

LE = 'LE'

Logical_Enclosure = [{'name': LE,
                      'enclosureUris': ['ENC:' + ENC1],  # REAL
                      'enclosureGroupUri': 'EG:EG1',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]

server_profiles = [{'type': 'ServerProfileV8',
                    'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC1,
                    'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual',
                    'macType': 'Virtual',
                    'wwnType': 'Virtual',
                    'name': 'Profile1',
                    'description': '',
                    'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1,
                                     'name': '1',
                                     'functionType': 'FibreChannel',
                                     'portId': 'Mezz 3:1-b',
                                     'requestedMbps': '2500',
                                     'networkUri': 'FCOE:FCoENet',
                                     'mac': 'f6:f1:10:e0:00:04',
                                     'wwpn': '10:00:12:5c:24:60:00:00',
                                     'wwnn': '10:00:12:5c:24:60:00:01'}]}
                   ]

server_profiles_edit = [{'type': 'ServerProfileV8',
                         'serverHardwareUri': ENC1 + ', bay 1',
                         'serverHardwareTypeUri': '',
                         'enclosureUri': 'ENC:' + ENC1,
                         'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual',
                         'macType': 'Virtual',
                         'wwnType': 'Virtual',
                         'name': 'Profile1',
                         'description': '',
                         'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'boot': {'manageBoot': False},
                         'connections': []}
                        ]

server_profiles_edit1 = [{'type': 'ServerProfileV8',
                          'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC1,
                          'enclosureGroupUri': 'EG:EG1',
                          'serialNumberType': 'Virtual',
                          'macType': 'Virtual',
                          'wwnType': 'Virtual',
                          'name': 'Profile1',
                          'description': '',
                          'affinity': 'Bay',
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'boot': {'manageBoot': False},
                          'connections': [{'id': 1,
                                           'name': '1',
                                           'functionType': 'FibreChannel',
                                           'portId': 'Mezz 3:1-b',
                                           'requestedMbps': '2500',
                                           'networkUri': 'FCOE:FCoENet',
                                           'mac': 'e6:4c:e0:b0:00:01',
                                           'wwpn': '10:00:12:5c:24:60:00:00',
                                           'wwnn': '10:00:12:5c:24:60:00:01'}]}
                         ]

api = [101, 120, 199, 200, 201, 300]

interconnects = [{'interconnectName': 'CN754406W6, interconnect 3'}]

ports = [{'uplink_port': 'Q3', 'downlink_port': 'd1', 'Secondary_Port': 'Q4'}]

uplink_ports = ['Q3', 'Q4']

downlink_ports = ['d1']

Disable_Port = [{"interconnectName": "CN754406W6, interconnect 3", "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":False, "portName":"Q3", "portStatus":"Unknown", "type":"port"},
                {"interconnectName": "CN754406W6, interconnect 3", "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":False, "portName":"Q4", "portStatus":"Unknown", "type":"port"}]

Enable_Port = [{"interconnectName": "CN754406W6, interconnect 3", "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":True, "portName":"Q3", "portStatus":"Unknown", "type":"port"}, {"interconnectName": "CN754406W6, interconnect 3", "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":True, "portName":"Q4", "portStatus":"Unknown", "type":"port"}]

downlink_port_disable = [{"interconnectName": "CN754406W6, interconnect 3", "portType": "Downlink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":False, "portName":"d1", "portStatus":"Unknown", "type":"port"}]

downlink_port_enable = [{"interconnectName": "CN754406W6, interconnect 3", "portType": "Downlink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":True, "portName":"d1", "portStatus":"Unknown", "type":"port"}]

FIPsnooping_Parameters = {"fcfMacAddress": "78:48:59:6a:2d:38", "fcID": "01:0b:01", "lagId": "2", "fcfName": "10:00:78:48:59:6a:2d:31", "fcoeMacAddress": "0e:fc:00:01:0b:01", "fcMap": "0e:fc:00"}

FIPsnooping_Parameters_uplink = {"fcfMacAddress": ["78:48:59:6a:2d:38"], "fcID": [], "lagId": "2", "fcfName": "10:00:78:48:59:6a:2d:31", "fcoeMacAddress": [], "fcMap": "0e:fc:00"}

FIPsnooping_Parameters_downlink = {"fcfMacAddress": ["78:48:59:6a:2d:38"], "lagId": "2", "fcfName": "10:00:78:48:59:6a:2d:31", "fcMap": None, "network": "FCoENet", "externalVlan": "1004", "fcoeLoginCount": "1", "port": "d1"}

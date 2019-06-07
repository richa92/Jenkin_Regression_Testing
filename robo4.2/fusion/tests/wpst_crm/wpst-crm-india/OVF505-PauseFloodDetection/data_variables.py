def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'
APPLIANCE_IP = '15.115.13.84'
LIGname = 'LIG12'
PFPtrue = True
OA_HOST = '15.212.162.72'
OA_USER = 'Administrator'
OA_PASS = 'password'
DEVICE = 'IOM'
ACTIONON = 'ON'
ACTIONOFF = 'OFF'
BAY1 = '1'
BAY2 = '2'
BAY3 = '3'
BAY4 = '4'
BAY1_IP = '15.212.162.86'
BAY2_IP = '15.212.162.87'
BAY3_IP = '15.212.162.88'
BAY4_IP = '15.212.162.89'
VC_USER = 'root'
OA_CLI_PROMPT = 'Callisto-OA1'
li = 'Callisto-LIG12'
ICM_1 = 'Callisto, interconnect 1'
ICM_2 = 'Callisto, interconnect 2'
ICM_3 = 'Callisto, interconnect 3'
ICM_4 = 'Callisto, interconnect 4'
SERVER_BAY = 'Callisto, bay 9'
UL_PORT_X5_NUMBER = '21'
UL_PORT_X1_NUMBER = '33'
UL_PORT_X8_NUMBER = '24'
UL_PORT_X7_NUMBER = '23'
DL_PORT_NUMBER = '9'
DL_PORT_NAME = 'd9'
UL_PORT_NAME = 'X5'
UL_PORT_NAME_X1 = 'X1'
STACKING_PORT_NAME = 'X8'
DL_PF_OPTION = '1'
UL_PF_OPTION = '2'
PFD_PORT_STATUS_REASON = 'PauseFloodDetected'
PORT_STATUS_REASON_ACTIVE = 'Active'
PORT_STATUS_REASON_STANDBY = 'Standby'
PORT_STATUS_REASON_OK = 'Ok'
PORT_STATUS_LINK = 'Linked'
PORT_STATUS_UNLINK = 'Unlinked'
PORT_STATUS_UNKNOWN = 'Unknown'
PORT_STATUS_DISABLED = 'AdminDisabled'
PORT_STATUS_REASON_NONE = 'None'
PORT_STATUS_REASON_UP = 'Unpopulated'
DISABLE_PORT = 'false'
ENABLE_PORT = 'true'
UPLINK_MSG = 'A pause flood condition has been detected on the uplink port(s) X5.'
UPLINK_STACKING_MSG = 'A pause flood condition has been detected on the uplink port(s) X5,X8.'
DOWNLINK_MSG = 'Connection on downlink port 9, subport a  has failed. A pause frame flood condition caused the port to be unlinked.'
POWER_OFF_MSG = 'Interconnect Callisto, interconnect 1 has been POWERED_OFF'
POWER_ON_MSG = 'Interconnect Callisto, interconnect 1 has been POWERED_ON'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'biggs.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

enc_groups = [{'name': 'EG_1',
               'type': 'EnclosureGroupV400',
               'enclosureCount': 1,
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG12'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG12'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG12'},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG12'},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}
              ]

icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
         ]

uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                  {'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               'us3': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X4', 'speed': 'Auto'},
                                                  ]},
               'us4': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'},
                                                  ]}
               }

ligs_test = [{'name': 'LIG12',
              'type': 'logical-interconnect-groupV300',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': icmap,
              'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': None,
              'snmpConfiguration': None,
              'qosConfiguration': None}
             ]

ligs = [{'name': 'LIG12',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None},
        {'name': 'LIG12',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us3'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None},
        {'name': 'LIG12',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'enablePauseFloodProtection': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None},
        {'name': 'LIG12',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'enablePauseFloodProtection': True},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None},
        {'name': 'LIG12',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'enablePauseFloodProtection': True},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None},
        {'name': 'LIG12',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us4'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'enablePauseFloodProtection': True},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None}
        ]

varTrue = True
varFalse = False

li_disable = {"type": "EthernetInterconnectSettingsV201", "enablePauseFloodProtection": False}
li_enable = {"type": "EthernetInterconnectSettingsV201", "enablePauseFloodProtection": True}

LIG1 = 'LIG12'
encs = [{'hostname': '15.212.162.72', 'username': 'Administrator', 'password': 'password', 'enclosureGroupUri': 'EG:EG_1', 'force': True, 'licensingIntent': 'OneViewNoiLO'}
        ]

ethernet_networks = [{'name': 'eth-100',
                      'type': 'ethernet-networkV300',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-101',
                      'type': 'ethernet-networkV300',
                      'vlanId': 101,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'}
                     ]

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'Callisto, bay 9',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:Callisto', 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_PauseFlood', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': 'Conn1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': 'Conn2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]}
                   ]
server_profiles1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'Callisto, bay 9',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:Callisto', 'enclosureGroupUri': 'EG:EG_1', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Sp_PauseFlood', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': False},
                     'connections': []}
                    ]
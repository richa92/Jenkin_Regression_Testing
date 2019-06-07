import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


# Appliance IP
APPLIANCE_IP = '15.186.14.17'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ENC1 = 'aus-c7000-188'

timeout = '300'
interval = '5'

users = [{'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'wpsthpvse1', 'enabled': True,
          'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'wpsthpvse1', 'enabled': True,
          'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]


network_credentials = {'userName': 'nat', 'password': 'wpsthpvse1'}
server_credentials = {'userName': 'sarah', 'password': 'wpsthpvse1'}

network_user = {'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'wpsthpvse1', 'enabled': True,
                'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]}

serveradmin = {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'wpsthpvse1', 'enabled': True,
               'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}

description = "Connection on downlink port 1, subport a has failed. Network wpstnetwork1 assigned to this connection was deleted."

description1 = "An error has occurred on connection 1.  Network wpstnetwork1 assigned to this connection was deleted."
description2 = "has failed. Network set wpstnetworkset2 assigned to this connection was deleted."
description4 = "has failed. The subport is unlinked."
ligs = [{'name': 'LIG-COMP-SS1',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'}
                                     ],
         'uplinkSets': [{'name': 'ss-comp-ug1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['wpstnetwork1', 'wpstnetwork3'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                    {'bay': '3', 'port': 'X1', 'speed': 'Auto'}
                                                    ]

                         }
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        {'name': 'LIG-COMP-SS2',
         'type': 'logical-interconnect-groupV6',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}
                                     ],
         'uplinkSets': [{'name': 'ss-comp-ug2',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['wpstnetwork2'],
                          'nativeNetworkUri': None,
                          'mode': 'Auto',
                          'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'},
                                                     {'bay': '4', 'port': 'X1', 'speed': 'Auto'}
                                                     ]

                         }
                        ],
         'internalNetworkUris': ['wpstnetwork1', 'wpstnetwork3', 'wpstnetwork4', 'wpstnetwork5', 'wpstnetwork6'],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}]

Fc_network = [{'name': 'FC_1', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_2', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_3', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_4', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_5', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'}]

enet = [{'purpose': 'General',
         'name': 'wpstnetwork1',
         'vlanId': 10,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork2',
         'vlanId': 20,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork3',
         'vlanId': 30,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork4',
         'vlanId': 40,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork5',
         'vlanId': 50,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork6',
         'vlanId': 60,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork7',
         'vlanId': 70,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork8',
         'vlanId': 80,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork9',
         'vlanId': 90,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         },
        {'purpose': 'General',
         'name': 'wpstnetwork10',
         'vlanId': 100,
         'smartLink': False,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tagged',
         'type': 'ethernet-networkV4'
         }]


EG = {'name': 'config4-group',
      'interconnectBayMappings': [
          {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS1'},
          {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS2'},
          {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS1'},
          {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS2'},
          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
      'ipRangeUris': [],
      'enclosureCount': 1,
      'osDeploymentSettings': None,
      'configurationScript': None,
      'powerMode': None,
      'ambientTemperatureMode': 'Standard'}

enclosures = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config4-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

OA_HOST = '15.186.2.227'
OA_USER = 'Administrator'
OA_PASS = 'Compaq123'
interconnect_bay = '1'

Downlink_linkedPort = ['d5', 'd5', 'd5', 'd5']
Unlinked_down = ['d7']
Profile1 = 'aus-c7000-188-Profile1'
Profile2 = 'aus-c7000-188-Profile2'

server_profile1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:config4-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:wpstnetwork1',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:wpstnetwork3',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                           ]},
                    'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profile2 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 5',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:config4-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile2', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'networkUri': 'NS:wpstnetworkset2',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:wpstnetwork2',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                    'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]


network_set = [{'name': 'wpstnetworkset1',
                'nativeNetworkUri': None,
                'networkUris': ['wpstnetwork1'],
                'connectionTemplateUri': None,
                'type': 'network-setV4',
                'initialScopeUris':[]
                },
               {'name': 'wpstnetworkset2',
                'nativeNetworkUri': None,
                'networkUris': ['wpstnetwork4'],
                'connectionTemplateUri': None,
                'type': 'network-setV4',
                'initialScopeUris':[]
                },
               {'name': 'wpstnetworkset3',
                'nativeNetworkUri': None,
                'networkUris': ['wpstnetwork3'],
                'connectionTemplateUri': None,
                'type': 'network-setV4',
                'initialScopeUris':[]
                }]

state = 'CONFIGURED'
Interconnect1 = ENC1 + ', interconnect 1'
Interconnect3 = ENC1 + ', interconnect 3'
Interconnect2 = ENC1 + ', interconnect 2'
Interconnect4 = ENC1 + ', interconnect 4'

PortID = ['X3']
PortID_2 = ['Q4.1']

PORTDETAILS = ['d1', 'd2', 'd3', 'd4']

INTERCONNECTS = ['aus-c7000-188,interconnect 1', 'aus-c7000-188,interconnect 2', 'aus-c7000-188,interconnect 3', 'aus-c7000-188,interconnect 4']

ic_enable_downlink = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["Ethernet", "EnetFcoe"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"portV5"}]

ic_enable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet"], "configPortTypes":["Ethernet"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"portV5"}]

ic_disable_Uplink = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["Ethernet", "EnetFcoe"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"portV5"}]

ic_disable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet"], "configPortTypes":["Ethernet"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"portV5"}]

def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

Appliance_IP = '15.199.233.245'

ENC1 = 'WPST-PAAU56-EN2'

US_name = 'Untagged'

Poweron_Server_Sleeptime = '600'

uplinksets_name = ['Untagged, Tunnel']

Tunnel = 'LAN_tunnel1'

SP_names = ['SP_1', 'SP_2']


LI_name = 'WPST-PAAU56-EN2-LIG1'

Network_list_created = ['LAN_tagged1', 'LAN_tagged2', 'LAN_tunnel1', 'LAN_tunnel2', 'LAN_untagged1', 'LAN_untagged2']

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

network_delete_alerts = ['crm.connectionStateChange', 'profilemgr.Connections.NETWORK_DELETED', 'crm.connectionStateChange']

Invalid_enettype = ['Tagged', 'Tunnel']

Tagged_networks = ['LAN_tagged1', 'LAN_tagged2']

delete_networks_sp = ['LAN_tunnel1', 'LAN_untagged1']

Untagged_networks = ['LAN_untagged1', 'LAN_untagged2']

Tunnel_networks = ['LAN_tunnel1', 'LAN_tunnel2']

relative_port_value = ['18', '17']

Network_name = ['LAN_tagged1', 'LAN_untagged1', 'LAN_tunnel1']

network_sets = [{'name': 'netset1', 'type': 'network-setV300','connectionTemplateUri': None, 'networkUris': ['network-a'], 'nativeNetworkUri': None}]

typicalBandwidth = ['3500', '4000', '4500']

maximumBandwidth = ['7500', '8000', '8500']

Network_type = ['Untagged', 'Tunnel', 'Tagged']

Connection_template = {"type":"connection-template",
                       "name": "name741613270-14800592096",
                       "bandwidth":
                       {"maximumBandwidth": "9000",
                       "typicalBandwidth": "3500"}
                      }

ethernet_networks = [{'name': 'LAN_tagged1',
                      'type': 'ethernet-networkV300',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': False,
                      'ethernetNetworkType': 'Tagged',
                      'connectionTemplateUri': None,
                      'privateNetwork': False
                      },
                     {'name': 'LAN_tagged2',
                      'type': 'ethernet-networkV300',
                      'vlanId': 101,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'LAN_untagged1',
                      'type': 'ethernet-networkV300',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'LAN_untagged2',
                      'type': 'ethernet-networkV300',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'LAN_tunnel1',
                      'type': 'ethernet-networkV300',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     {'name': 'LAN_tunnel2',
                      'type': 'ethernet-networkV300',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'},
                     ]

fc_networks = [{'type': 'fc-networkV300',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

ethernet_edit = [{'name': 'LAN_tagged1',
                      'type': 'ethernet-networkV300',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                 {'name': 'LAN_untagged1',
                      'type': 'ethernet-networkV300',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                 {'name': 'LAN_tunnel1',
                      'type': 'ethernet-networkV300',
                      'vlanId': None,
                      'purpose': 'General',
                      'smartLink': False,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tunnel'}
                 ]

uplink_sets = {'us1': {'name': 'Untagged',
                       'ethernetNetworkType': 'Untagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['fcoe-range32a'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]
                       },
               'us2': {'name': 'Tunnel',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['fcoe-range32a'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]
                       },
               'us3': {'name': 'Tagged',
                       'ethernetNetworkType': 'Ethernet',
                       'networkType': 'Ethernet',
                       'networkUris': ['fcoe-range32a'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]
                      }
               }


ligs = {'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                                     ],
         'uplinkSets': [uplink_sets['us1'], uplink_sets['us2']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration':None}
         
lig = {'name': 'LIG2',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                                     ],
         'uplinkSets': [uplink_sets['us3']],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration':None}         

enc_group = {'name': 'EG175',
             'type': 'EnclosureGroupV400',
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
                  {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
             }

encs = [{'hostname': '15.245.129.11', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG175', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

server_profiles_gen8_bay1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:'+ENC1, 'enclosureGroupUri': 'EG:EG175', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                    'name': 'SP_1', 'description': '', 'affinity': 'Bay',
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:LAN_untagged1',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}],
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'bios':{'manageBios': False, 'overriddenSettings':[]}, 'sanStorage': None}]

server_profiles_gen8_bay2 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:'+ENC1, 'enclosureGroupUri': 'EG:EG175', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                    'name': 'SP_2', 'description': '', 'affinity': 'Bay',
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:LAN_tunnel1',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}],
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'bios':{'manageBios': False, 'overriddenSettings':[]}, 'sanStorage': None}]


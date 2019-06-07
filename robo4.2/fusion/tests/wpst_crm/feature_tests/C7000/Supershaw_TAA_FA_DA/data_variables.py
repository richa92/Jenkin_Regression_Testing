# Appliance Credentials
appliance_ip = '15.245.132.63'
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
OA_USER = "Administrator"
OA_PASS = "wpsthpvse1"
interconnect_bay1 = '1'
interconnect_bay2 = '2'
ENCLOSURE_IP = '15.245.129.56'
SWITCH_IP = '15.245.128.66'
SWITCH_USER = 'admin'
SWITCH_PASSWRD = 'wpsthpvse1'
ENC = 'FVT-PAAW63-EN2'
Server_IP = '192.168.0.220'
DEVICE = 'IOM'
ACTION = ['ON', 'OFF']
oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "wpsthpvse1"}
Server_bay_num = '1'
downlink_1 = 'd1'
downlink_10 = 'd10'
expected_conn_map_d1 = ['20:21:00:02:ac:00:2a:64']  # Connection map details in 3par
expected_conn_map_ic1 = '20:21:00:02:ac:00:2a:64'  # connection map details in 3par
expected_conn_map_ic2 = '20:23:00:02:ac:00:2a:64'  # connection map details in 3par
expected_conn_map_d10 = ['20:23:00:02:ac:00:2a:64']  # connection map details in 3par
win_server_details = {"username": "Administrator", "password": "hpvse@1"}
INTERCONNECTS = ['FVT-PAAW63-EN2, interconnect 1', 'FVT-PAAW63-EN2, interconnect 2']
Uplink_Ports = [['Q1.1', 'X5'], ['X3', 'X5']]
BFS_PING_LIST = '192.168.0.224'
BFS_gateway_ip = '192.168.0.1'
LINUX_BFS_USER = 'Administrator'
LINUX_BFS_PWD = 'hpvse1'
LINUX_BFS_PROMPT = 'ESXi'
diskspd_cmd = "powershell.exe Get-disk -FriendlyName *3PARdata* > C:\\WINDOWSLUN.txt"
# After doing poweroff/efuseoff/disable uplink/downlink lun count should get reduced. Since we are getting lun count 1 for ic1 and lun count 2 for ic2.When doing poweroff/efuseoff/disable uplink/downlink lun count should get reduced. When poweroff/efuseoff/disable uplink/downlink IC1 -> Getting list disk output as 2 LUn.
lun_count_total = '3'  # For ic1 - 1lun,for ic2 - 2 luns
lun_count_ic1 = '2'
lun_count_ic2 = '1'
# After power off fa connection in ic2, number of logins should get reduced
login1 = '1'
login0 = '0'

fc_networks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FA1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': False,
                'name': 'FA2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               {'type': 'fc-networkV4',
                'linkStabilityTime': 0,
                'autoLoginRedistribution': False,
                'name': 'DA2',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'DirectAttach'},
               ]

ethernet_networks = {'name': 'Enet_101',
                     'type': 'ethernet-networkV4',
                     'vlanId': '101',
                     'purpose': 'Management',
                     'smartLink': True,
                     'privateNetwork': False,
                     'ethernetNetworkType': 'Tagged'}

uplink_sets = {'UplinkSet_1': {'name': 'us_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                               'networkUris': ['Enet_101'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'Q1.1', 'speed': 'Auto'}, {'bay': '2', 'enclosure': '1', 'port': 'Q4.1', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'us_fa1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                               'networkUris': ['FA1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '2', 'enclosure': '1', 'port': 'X3', 'speed': 'Auto'}]},
               'UplinkSet_3': {'name': 'us_da1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                               'networkUris': ['DA1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]},
               'UplinkSet_4': {'name': 'us_da2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                               'networkUris': ['DA2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '2', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]}
               }

lig = {'name': 'LIG1',
       'type': 'logical-interconnect-groupV5',
       'enclosureType': 'C7000',
       'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}],
       'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy(),
                      uplink_sets['UplinkSet_3'].copy(), uplink_sets['UplinkSet_4'].copy()],
       'internalNetworkUris': [],
       'stackingMode': 'Enclosure',
       'ethernetSettings': None,
       'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None,
                'qosConfiguration': None}

enc_group = {'name': 'EG',
             'enclosureCount': 1,
             'configurationScript': None,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
             'ipAddressingMode': 'External',
             'ipRangeUris': [],
             'ambientTemperatureMode': 'Standard',
             'powerMode': 'RedundantPowerFeed'
             }

encs = [{'hostname': ENCLOSURE_IP, 'username': 'Administrator', 'password': 'wpsthpvse1',
         'enclosureGroupUri': 'EG:EG', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]
LI = 'FVT-PAAW63-EN2-LIG1'

server_profile1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC,
                    'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet',
                                                                 'portId': 'Auto', 'requestedMbps': '2500',
                                                                 'networkUri': 'ETH:Enet_101'},
                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel',
                                                            'portId': 'Auto', 'requestedMbps': '2500',
                                                            'networkUri': 'FC:DA1',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None,
                                                            'wwpn': '', 'wwnn': ''},
                                                           {'id': 3, 'name': '3', 'functionType': 'FibreChannel',
                                                            'portId': 'Auto', 'requestedMbps': '2500',
                                                            'networkUri': 'FC:FA1',
                                                            'boot': {'priority': 'NotBootable'}, 'mac': None,
                                                            'wwpn': '', 'wwnn': ''}
                                                           ]},
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                    'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profile_bfs = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC + ', bay 10',
                       'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC,
                       'enclosureGroupUri': 'EG:EG',
                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                       'name': 'Profile10', 'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet',
                                                               'portId': 'Auto', 'requestedMbps': '1000',
                                                               'networkUri': 'ETH:Enet_101'},
                                                              {'id': 2, 'name': '2', 'functionType': 'FibreChannel',
                                                               'portId': 'Auto', 'requestedMbps': '1000',
                                                               'networkUri': 'FC:DA2',
                                                               'boot': {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:23:00:02:AC:00:2A:64", "lun": "0"}], "iscsi": {}}, 'mac': None,
                                                               'wwpn': '', 'wwnn': ''}
                                                              ]},
                       'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                       'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

					   
Edit_Uplink_Port = {'associatedUplinkSetUri': '',
                    'interconnectName': INTERCONNECTS[0],
                    'portType': 'Uplink',
                    'portId': '',
                    'portHealthStatus': '',
                    'capability': ['FibreChannel'],
                    'configPortTypes': ['FibreChannel'],
                    'enabled': '',
                    'portName': '',
                    'portStatus': '',
                    'type': 'port'}
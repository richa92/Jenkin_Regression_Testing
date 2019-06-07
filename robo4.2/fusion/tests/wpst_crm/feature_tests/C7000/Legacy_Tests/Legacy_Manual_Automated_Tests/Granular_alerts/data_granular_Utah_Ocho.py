import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


APPLIANCE_IP = '15.186.30.57'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ENC1 = 'USE0515652'

timeout = '300'
interval = '5'


users = [{'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'hpvse123', 'enabled': True,
          'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'hpvse123', 'enabled': True,
          'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]

network_credentials = {'userName': 'nat', 'password': 'hpvse123'}
server_credentials = {'userName': 'sarah', 'password': 'hpvse123'}

network_user = {'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'hpvse123', 'enabled': True,
                'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]}

serveradmin = {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'hpvse123', 'enabled': True,
               'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}

Fc_network = [{'name': 'FC_1', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_2', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_3', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_4', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'},
              {'name': 'FC_5', 'linkStabilityTime': '30', 'autoLoginRedistribution': True, 'fabricType': 'FabricAttach', 'type': 'fc-networkV4'}]

lig = {'name': 'LIG-COMP-SS',
       'type': 'logical-interconnect-groupV6',
       'enclosureType': 'C7000',
       'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 20-Port FC Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 20-Port FC Module'}],
       'uplinkSets': [{'name': 'ss-comp-ug1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'],
                       'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                       'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                      # {'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                      {'name': 'ss-comp-ug3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'],
                       'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                       'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                      {'name': 'ss-comp-ug2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'],
                       'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                       'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                      {'name': 'ss-comp-ug4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'],
                       'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                       'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}],
       'stackingMode': 'Enclosure',
       'ethernetSettings': None,
       'state': 'Active',
       'telemetryConfiguration': None,
       'snmpConfiguration': None}

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
          {'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
          {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
          {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
          {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS'},
          {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
          {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
      'ipRangeUris': [],
      'enclosureCount': 1,
      'osDeploymentSettings': None,
      'configurationScript': None,
      'powerMode': None,
      'ambientTemperatureMode': 'Standard'}

enclosures = [{'hostname': '15.186.17.26', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:config4-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]


OA_HOST = '15.186.17.26'
OA_USER = 'Administrator'
OA_PASS = 'compaq'
interconnect_bay = '3'

Downlink_linkedPort = ['d1', 'd1', 'd2', 'd2']
Unlinked_down = ['d7']
Profile1 = 'USE0515652-Profile1'
Profile2 = 'USE0515652-Profile2'

description = "Connection on downlink port 1, subport a has failed. Network wpstnetwork1 assigned to this connection was deleted."

description1 = "An error has occurred on connection 1.  Network wpstnetwork1 assigned to this connection was deleted."

description2 = "has failed. Network set wpstnetworkset2 assigned to this connection was deleted."

description4 = "has failed. The subport is unlinked."

server_profile1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:config4-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                    'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profile2 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:config4-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile2', 'description': '', 'affinity': 'Bay',
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                                            'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                    'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]


network_set = [{'name': 'wpstnetworkset1',
                'nativeNetworkUri': None,
                'networkUris': ['FC_1'],
                'connectionTemplateUri': None,
                'type': 'network-setV4',
                'initialScopeUris':[]
                },
               {'name': 'wpstnetworkset2',
                'nativeNetworkUri': None,
                'networkUris': ['FC_4'],
                'connectionTemplateUri': None,
                'type': 'network-setV4',
                'initialScopeUris':[]
                },
               {'name': 'wpstnetworkset3',
                'nativeNetworkUri': None,
                'networkUris': ['FC_3'],
                'connectionTemplateUri': None,
                'type': 'network-setV4',
                'initialScopeUris':[]
                }]

state = 'CONFIGURED'
Interconnect1 = ENC1 + ', interconnect 3'
Interconnect3 = ENC1 + ', interconnect 5'
Interconnect2 = ENC1 + ', interconnect 4'
Interconnect4 = ENC1 + ', interconnect 6'

PortID = ['1']
PortID_2 = ['1']

INTERCONNECTS = ['USE0515652,interconnect 3', 'USE0515652,interconnect 4', 'USE0515652,interconnect 5', 'USE0515652,interconnect 6']

ic_enable_downlink = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"portV5"}]


ic_enable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"portV5"}]

ic_disable_Uplink = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes":["Ethernet", "EnetFcoe"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"portV5"}]

ic_disable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"portV5"}]

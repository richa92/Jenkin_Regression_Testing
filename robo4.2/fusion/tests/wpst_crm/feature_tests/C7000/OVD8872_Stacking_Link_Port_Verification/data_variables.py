"""Data Variable"""


def make_range_list(start, end, prefix='net_', suffix=''):
    """Function Definition"""
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


APPLIANCE_IP = '15.186.22.215'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

INTERCONNECTS_list = ['enc1, interconnect 1', 'enc1, interconnect 2', 'enc1, interconnect 3', 'enc1, interconnect 4', 'enc1, interconnect 5', 'enc1, interconnect 6']
stacking_ports = ['X7', 'X8']
portType = 'Stacking'
PortStatus = 'Linked'
ENC1 = 'enc1'
LIG = 'LIG'
liupdate = {"sppUri": ' ', "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}
LI = {'name': ENC1 + '-' + LIG}

Firmware_Bundles = ['bp-2018-03-29-01.iso', 'bp-2019-02-28.iso']

fw_uri_4_10 = '/rest/firmware-drivers/bp-2018-03-29-01'

fw_uri_5_0 = '/rest/firmware-drivers/bp-2019-02-28'

SPP_4_10 = 'bp-2018-03-29-01.iso'

SPP_5_0 = 'bp-2019-02-28.iso'

server_profiles = [[{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 6',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Profile6', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'HardDisk', 'PXE']},
                     'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}}],
                   [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Profile3', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                     'connectionSettings':{'connections': [{'id': 1, 'name': 'Conn_1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}}]]

ethernet_network = [{"vlanId": "10",
                     "purpose": "General",
                     "name": "Net10",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "20",
                     "purpose": "General",
                     "name": "Net20",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "30",
                     "purpose": "General",
                     "name": "Net30",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "40",
                     "purpose": "General",
                     "name": "Net40",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"}]

uplink_set = {'UplinkSet_1': {'name': 'us_1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Net10'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                              'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '1', 'port': 'X5', 'speed': 'Auto'}]},
              'UplinkSet_2': {'name': 'us_2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Net20'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                              'logicalPortConfigInfos': [{'bay': '2', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
              'UplinkSet_3': {'name': 'us_3', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Net30'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                              'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
              'UplinkSet_4': {'name': 'us_4', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Net40'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                              'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]}}

li = ENC1 + 'LIG'
LIG = 'LIG'
LIG = {'name': 'LIG',
       'type': 'logical-interconnect-groupV7',
       'enclosureType': 'C7000',
       'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                   {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}
                                   ],
       'uplinkSets': [uplink_set['UplinkSet_1'].copy()],
       'stackingMode': 'Enclosure',
       'ethernetSettings': None,
       'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None,
                'qosConfiguration': None}

Edit_LIG = [{'name': 'LIG',
             'type': 'logical-interconnect-groupV7',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}
                                         ],
             'uplinkSets': [],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None,
             'qosConfiguration': None}]

encs = [{'hostname': '15.186.18.129', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG', 'force': False, 'licensingIntent': 'OneView'}]

enc_groups = {'name': 'EG',
                      'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                  {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                  {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                  {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                                                  {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
              'ipRangeUris': [],
              'enclosureCount': 1,
              'osDeploymentSettings': None,
              'configurationScript': None,
              'powerMode': None,
              'ambientTemperatureMode': 'Standard'}

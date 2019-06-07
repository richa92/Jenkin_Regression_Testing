###########################################################################
# Data_Variables.py
# All the required data and user input needs to be specified in this file
# before triggerring the Automation Suite.
###########################################################################
APPLIANCE_IP = '90.1.6.222'
Appliance_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
SSH_USER = 'root'
SSH_PASS = 'hpvse1'
NITRO_IC_TYPE = 'Virtual Connect SE 100Gb F32 Module for Synergy'
SUPPORT_ICM = 'Synergy 50Gb Interconnect Link Module'
INTERCONNECT1 = 'SGH737XD79, interconnect 1'
INTERCONNECT2 = 'SGH737XD7A, interconnect 4'
OneViewPrompt = '~]#'

#  When we have to login to Nitro ICM as root user, below password has to be used.
NitroUserName = 'OneView'
nitro_root_password = 'UnoVista'

###########################################################################
#  MAT PreRequisite
###########################################################################
MATLIG1 = 'MAT_LIG1'
MATLIG2 = 'MAT_LIG3'
ENC1 = 'SGH737XD7A'
ENC2 = 'SGH737XD79'
EG = 'EG'
LI = 'LE-LIG'
MAT_networks = [{'name': 'network_SFLOW',
                 'type': 'ethernet-networkV4',
                 'vlanId': 1,
                 'purpose': 'General',
                 'smartLink': True,
                 'privateNetwork': False,
                 'connectionTemplateUri': None,
                 'ethernetNetworkType': 'Tagged',
                                        'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
                                        'initialScopeUris': []},
                {'name': 'network_MLAG',
                 'type': 'ethernet-networkV4',
                 'vlanId': 30,
                 'purpose': 'General',
                 'smartLink': True,
                 'privateNetwork': False,
                 'connectionTemplateUri': None,
                 'ethernetNetworkType': 'Tagged',
                                        'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
                                        'initialScopeUris': []},
                {'name': 'network_Tunnel',
                 'type': 'ethernet-networkV4',
                 'vlanId': 0,
                 'purpose': 'General',
                 'smartLink': True,
                 'privateNetwork': True,
                 'connectionTemplateUri': None,
                 'ethernetNetworkType': 'Tunnel',
                                        'bandwidth': {'maximumBandwidth': 50000, 'typicalBandwidth': 2500},
                                        'initialScopeUris': []}]

MAT_networkset = [{"name": "mlag_net", "networkUris": ["network_MLAG", "network_SFLOW"], "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None}]

Modify_MAT_networkset = [{"name": "mlag_net", "bandwidth": {"maximumBandwidth": 50000, "typicalBandwidth": 2500}, "type": "connection-template", "uri": None}]

MAT_uplink_sets = {'MAT_UplinkSet_MLAG': {'name': 'MLAG', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                          'networkUris': ['network_MLAG'], 'mode': 'Auto',
                                          'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q2', 'speed': 'Auto'},
                                                                     {'enclosure': '2', 'bay': '4', 'port': 'Q2', 'speed': 'Auto'}]},
                   'MAT_UplinkSet_SFLOW': {'name': 'SFLOW', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                           'networkUris': ['network_SFLOW'], 'mode': 'Auto',
                                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q3', 'speed': 'Auto'},
                                                                      {'enclosure': '2', 'bay': '4', 'port': 'Q3', 'speed': 'Auto'}]},
                   'MAT_UplinkSet_Tunnel': {'name': 'Tunnel', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tunnel',
                                            'networkUris': ['network_Tunnel'], 'mode': 'Auto',
                                            'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1', 'speed': 'Auto'},
                                                                       {'enclosure': '2', 'bay': '4', 'port': 'Q1', 'speed': 'Auto'}]}}

MAT_LIGS = [{'name': MATLIG1,
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'SY12000',
             "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
             'uplinkSets': [MAT_uplink_sets['MAT_UplinkSet_MLAG'].copy(), MAT_uplink_sets['MAT_UplinkSet_SFLOW'].copy(), MAT_uplink_sets['MAT_UplinkSet_Tunnel'].copy()],
             'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': NITRO_IC_TYPE, 'enclosureIndex': 1},
                                         {'bay': 4, 'enclosure': 1, 'type': SUPPORT_ICM, 'enclosureIndex': 1},
                                         {'bay': 1, 'enclosure': 2, 'type': SUPPORT_ICM, 'enclosureIndex': 2},
                                         {'bay': 4, 'enclosure': 2, 'type': NITRO_IC_TYPE, 'enclosureIndex': 2}],
             'internalNetworkUris': [],
             'interconnectBaySet': 1,
             'redundancyType': 'HighlyAvailable',
             'enclosureIndexes': [1, 2],
             'downlinkSpeedMode':'SPEED_50GB',
             'qosConfiguration': None
             },
            {'name': MATLIG2,
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'SY12000',
             "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
             'uplinkSets': [],
             'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': NITRO_IC_TYPE, 'enclosureIndex': 1},
                                         {'bay': 6, 'enclosure': 1, 'type': SUPPORT_ICM, 'enclosureIndex': 1},
                                         {'bay': 3, 'enclosure': 2, 'type': SUPPORT_ICM, 'enclosureIndex': 2},
                                         {'bay': 6, 'enclosure': 2, 'type': NITRO_IC_TYPE, 'enclosureIndex': 2}],
             'internalNetworkUris': [],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'enclosureIndexes': [1, 2],
             'downlinkSpeedMode':'SPEED_25GB',
             'qosConfiguration': None
             }]


enc_group = [{'name': 'EG',
              'enclosureCount': 2,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + MATLIG1},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + MATLIG2},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + MATLIG1},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + MATLIG2}],
              'ipAddressingMode': 'DHCP'}]

Logical_Enclosure = {'name': 'LE',
                     'enclosureUris': ['ENC:' + ENC2, 'ENC:' + ENC1],
                     'enclosureGroupUri': 'EG:' + EG,
                     'firmwareBaselineUri': None,
                     'forceInstallFirmware': False}

profile_MAT = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 8',
                'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                'name': 'profile_MLAG', 'description': '', 'affinity': 'Bay',
                "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                        'requestedMbps': '2500', 'networkUri': 'NS:mlag_net', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                       {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                        'requestedMbps': '2500', 'networkUri': 'NS:mlag_net', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                       {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 1:1-c',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:network_Tunnel', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                       {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 1:2-c',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:network_Tunnel', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                       ]}},
               {'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
                'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                'name': 'profile_PrivateNet', 'description': '', 'affinity': 'Bay',
                "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                         'requestedMbps': '2500', 'networkUri': 'ETH:network_Tunnel', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                       {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                                         'requestedMbps': '2500', 'networkUri': 'ETH:network_Tunnel', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                       ]}}]

#########################################################################
#    SSH Feature
#########################################################################

linuxip = '90.1.0.201'
linuxuser = 'root'
linuxpassword = 'iso*help'
firmwareurl = 'http://hf-cit.us.rdlabs.hpecorp.net:9300/r2.0.0/Nitro/development/build-87/'
firmwareupdatepackage = 'icm_fv2-2.0.0-87-2018-08-10-D.pkg'

interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]
interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
netop_user = [{"op": "replace", "path": "/netOpPasswd", "value": "netop123"}]
enable_facePlateSerial = [{"op": "replace", "path": "/facePlateSerial", "value": "enable"}]
enable_cansrial = [{"op": "replace", "path": "/canmicSerial", "value": "enable"}]

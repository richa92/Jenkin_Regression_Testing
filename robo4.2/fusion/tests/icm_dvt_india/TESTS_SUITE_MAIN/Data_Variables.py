
###########################################################################
# Data_Variables.py
# All the required data and user input needs to be specified in this file
# before triggerring the Automation Suite.
###########################################################################

APPLIANCE_IP = '90.1.0.102'
Appliance_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

OV_root_usr = 'root'
OV_root_pwd = 'hpvse1'

INTERCONNECT1 = 'SGH724SERS, interconnect 4'
INTERCONNECT2 = 'SGH724SERY, interconnect 1'

OneViewPrompt = '~]#'

FC_Downlink_Port1 = 'TwentyGigE0/1/9'
FC_Downlink_Port2 = 'TwentyGigE1/1/9'

FC_Uplink_Port1 = 'Ten-GigabitEthernet0/0/5:1'
FC_Uplink_Port2 = 'Ten-GigabitEthernet1/0/5:1'

FCOE_Downlink_Port1 = 'TwentyGigE0/2/8'
FCOE_Downlink_Port2 = 'TwentyGigE1/2/8'

FCOE_Uplink_Port1 = 'Ten-GigabitEthernet0/0/2:1'
FCOE_Uplink_Port2 = 'Ten-GigabitEthernet1/0/2:1'

FC_DA_Downlink_Port1 = 'TwentyGigE0/2/3'
FC_DA_Downlink_Port2 = 'TwentyGigE1/2/3'

FC_DA_Uplink_Port1 = 'Ten-GigabitEthernet0/0/4:1'
FC_DA_Uplink_Port2 = 'Ten-GigabitEthernet1/0/4:1'

MLAG_Uplink_Port1 = 'FortyGigE0/0/1'
MLAG_Uplink_Port2 = 'FortyGigE1/0/1'

STACKING_PORT1 = 'FortyGigE0/0/7'
STACKING_PORT2 = 'FortyGigE0/0/8'

STACKING_PORT3 = 'FortyGigE1/0/7'
STACKING_PORT4 = 'FortyGigE1/0/8'

#  When we have to login to Potash ICM as root user, below password has to be used.
potash_root_password = 'UnoVista'

#  Need to login to Potash ICM with Username as 'OneView' and RandomPassword
PotashUserName = 'OneView'

LI = 'LE-MAT_LIG'
FCoE_VLAN1 = '150'
FCoE_VLAN2 = '300'

interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]
interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]

networkset = [{"name": "net", "networkUris": [{'ETH': 'dum1', 'ETH2': 'dum2'}], "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": 'ETH3:dum2'}]


testing_fabric_networks = [{'name': 'fabric_attach_network1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
                           {'name': 'fabric_attach_network2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]


testing_direct_networks = [{'name': 'direct_attach_network1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'},
                           {'name': 'direct_attach_network2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'}]


testing_fcoe_networks = [{'name': 'fcoe_network', 'type': 'fcoe-networkV4', 'vlanId': 30, 'managedSanUri': None},
                         {'name': 'fcoe_network2', 'type': 'fcoe-networkV4', 'vlanId': 40, 'managedSanUri': None}]


testing_uplink_sets = {'UplinkSet_1': {'name': 'tagged_networks', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                       'networkUris': ['tagged_network1', 'tagged_network2'], 'mode': 'Auto',
                                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q2.2', 'speed': 'Auto'}]},
                       'UplinkSet_2': {'name': 'fcoe_networks', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                       'networkUris': ['fcoe_network', 'fcoe_network2'], 'mode': 'Auto',
                                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '4', 'port': 'Q2.3', 'speed': 'Auto'}]},
                       'UplinkSet_3': {'name': 'fabric_networks', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fabric_attach_network1', 'fabric_attach_network2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q3.2', 'speed': 'Auto'}]},
                       'UplinkSet_4': {'name': 'direct_networks', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['direct_attach_network1', 'direct_attach_network2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                       'logicalPortConfigInfos': [{'bay': '4', 'port': 'Q3.3', 'speed': 'Auto'}]}}


FA_ligs = {'name': 'LIG_FA',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
           'uplinkSets': [testing_uplink_sets['UplinkSet_3'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'Redundant',
           'enclosureIndexes': [1],
           'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
           }


DA_ligs = {'name': 'LIG_DA',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
           'uplinkSets': [testing_uplink_sets['UplinkSet_4'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'Redundant',
           'enclosureIndexes': [1],
           'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
           }


FCOE_ligs = {'name': 'LIG_FCOE',
             'type': 'logical-interconnect-groupV4',
             'enclosureType': 'SY12000',
             "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
             'uplinkSets': [testing_uplink_sets['UplinkSet_2'].copy()],
             'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                         {'bay': 4, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
             'internalNetworkUris': [],
             'interconnectBaySet': 1,
             'redundancyType': 'Redundant',
             'enclosureIndexes': [1],
             'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
             }


server_profiles = [
    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:ENC02CLDVT, bay 3',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'SAN', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': 'managed manually', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'connections': [
                        {'id': 2, 'name': 'conn_eth', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:ETH1', 'functionType': 'Ethernet'},
                        {'id': 3, 'name': 'conn_ether', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:ETH2', 'functionType': 'Ethernet'}


                    ],
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},

     'bios': {'manageBios': False, 'overriddenSettings': []}},


    {'type': 'ServerProfileV6', 'serverHardwareUri': 'SH:CN75160609, bay 12',
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'name': 'BFS_FCoE_test', 'description': '', 'affinity': 'Bay',
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'connections': [
         {'id': 1, 'name': 'conn_FCoE1', 'portId': 'Mezz 1:1-b', 'requestedMbps': '8000', 'networkUri': 'FCOE:FCoE_A201', 'functionType': 'FibreChannel',
          'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'macType': 'UserDefined', 'mac': '94:57:A5:08:DE:40', 'wwpnType': 'UserDefined', 'wwnn': '10:00:62:02:50:70:00:06', 'wwpn': '20:00:94:57:A5:08:DE:41'},
         {'id': 2, 'name': 'conn_FCoE2', 'portId': 'Mezz 1:2-b', 'requestedMbps': '10000', 'networkUri': 'FCOE:FCoE_B200', 'functionType': 'FibreChannel',
          'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'macType': 'UserDefined', 'mac': '94:57:A5:08:DE:48', 'wwpnType': 'UserDefined', 'wwnn': '10:00:14:02:ec:c8:83:39', 'wwpn': '20:00:94:57:A5:08:DE:49'},
         {'id': 3, 'name': 'eth_conn', 'portId': 'Mezz 1:1-a', 'requestedMbps': '2000', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'}
     ],
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1, 'volumeUri': 'FCoE_Jan9_150_jithu', 'lunType': 'Manual', 'lun': 1,
                                           'isBootVolume': True,
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                             'storageTargetType': 'Auto', 'storageTargets': []
                                                             },
                                                            {'isEnabled': True, 'connectionId': 2,
                                                             'storageTargetType': 'Auto', 'storageTargets': []
                                                             }
                                                            ]}]},
     'localStorage':{'sasLogicalJBODs': [], 'controllers': []},
     'bios': {'manageBios': False, 'overriddenSettings': []}}
]

###########################################################################
#  MAT PreRequisite
###########################################################################
PreRequisite_Ethernet_networks = [{'name': 'net1', 'type': 'ethernet-networkV4', 'vlanId': 10, 'purpose': 'Management',
                                  'smartLink': False, 'privateNetwork': False},
                                  {'name': '1GB_Net', 'type': 'ethernet-networkV4', 'vlanId': 20, 'purpose': 'Management',
                                  'smartLink': False, 'privateNetwork': False}]

MAT_networkset = [{"name": "mlag_net", "networkUris": [{'ETH:net1'}], "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None}]

PreRequisite_FC_networks = [{'name': 'FC_A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
                           {'name': 'FC_B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]


PreRequisite_FCOE_networks = [{'name': 'FCoE1', 'type': 'fcoe-networkV4', 'vlanId': 150, 'managedSanUri': None},
                         {'name': 'FCoE2', 'type': 'fcoe-networkV4', 'vlanId': 300, 'managedSanUri': None}]

PreRequisite_FCDA_networks = [{'name': 'FC_DA1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'},
                           {'name': 'FC_DA2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                            'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'}]

MAT_uplink_sets = {'MAT_UplinkSet_1': {'name': 'MLAG', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                   'networkUris': ['net1'], 'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1', 'speed': 'Auto'},
                                                              {'enclosure': '2', 'bay': '4', 'port': 'Q1', 'speed': 'Auto'}]},
                    'MAT_UplinkSet_3': {'name': 'UP_FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                    'networkUris': ['FCoE1'], 'mode': 'Auto',
                                    'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q2.1', 'speed': 'Auto'}]},
                    'MAT_UplinkSet_4': {'name': 'UP_FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                    'networkUris': ['FCoE2'], 'mode': 'Auto',
                                    'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '4', 'port': 'Q2.1', 'speed': 'Auto'}]},
                    'MAT_UplinkSet_5': {'name': 'UP_FC1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                    'networkUris': [ 'FC_A'], 'mode': 'Auto', 'lacpTimer': 'Short',
                                    'primaryPort': None,'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q5.1', 'speed': 'Auto'}]},
                    'MAT_UplinkSet_6': {'name': 'UP_FC2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                    'networkUris': ['FC_B'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '4', 'port': 'Q5.1', 'speed': 'Auto'}]},
                    'MAT_UplinkSet_7': {'name': ' up_da1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                    'networkUris': ['FC_DA1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q4.1', 'speed': 'Auto'}]},
                    'MAT_UplinkSet_8': {'name': ' up_da2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                    'networkUris': ['FC_DA2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '4', 'port': 'Q4.1', 'speed': 'Auto'}]}}


MAT_LIGS = [{'name': 'MAT_LIG',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
           'uplinkSets': [MAT_uplink_sets['MAT_UplinkSet_1'].copy(),MAT_uplink_sets['MAT_UplinkSet_3'].copy(),MAT_uplink_sets['MAT_UplinkSet_4'].copy(),MAT_uplink_sets['MAT_UplinkSet_5'].copy(),MAT_uplink_sets['MAT_UplinkSet_6'].copy(),MAT_uplink_sets['MAT_UplinkSet_7'].copy(),MAT_uplink_sets['MAT_UplinkSet_8'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                       {'bay': 1, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                       {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'HighlyAvailable',
           'enclosureIndexes': [1,2],
           'qosConfiguration': None
           }]

MATLIG1 = 'MAT_LIG'
ENC1 = 'SGH724SERS'
ENC2 = 'SGH724SERY'
EG = 'EG'
enc_group = [{'name': 'EG',
                'enclosureCount': 2,
               'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + MATLIG1},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + MATLIG1},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}],
                'ipAddressingMode': 'DHCP'}]

Logical_Enclosure = {'name': 'LE',
                     'enclosureUris': ['ENC:' + ENC2,'ENC:' + ENC1],
                     'enclosureGroupUri': 'EG:' + EG,
                     'firmwareBaselineUri': None,
                     'forceInstallFirmware': False}


Profile_FCOE = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 8',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'profile_FCOE', 'description': '', 'affinity': 'Bay', 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'}, 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {'connections': [ {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCoE1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21:01:00:02:ac:01:c8:79', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCoE2', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20:01:00:02:ac:01:c8:79', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}}]

profile_MLAG= [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'profile_MLAG', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'NS:mlag_net', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'NS:mlag_net', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                           ]}}]

Profile_FC = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 9',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'profile_FC', 'description': '', 'affinity': 'Bay', 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'}, 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {'connections': [ {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC_A', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21:01:00:02:ac:01:c8:79', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC_B', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20:01:00:02:ac:01:c8:79', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}}]

Profile_FC_DA = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'profile_FC_DA', 'description': '', 'affinity': 'Bay', 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'}, 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {'connections': [ {'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC_DA1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21240002AC01C879', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'FC:FC_DA2', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20240002AC01C879', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}}]



profile_netset= [{'type': 'ServerProfileV9', 'serverHardwareUri': 'SH:ENC02CLDVT, bay 3',
                    'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                    'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'SAN', 'description': '', 'affinity': 'Bay',
                    'firmware': {'manageFirmware': False, 'firmwareBaselineUri': 'managed manually', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                    'connections': [
                        {'id': 2, 'name': 'conn_eth', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net1', 'functionType': 'Ethernet'}],
                        #{'id': 3, 'name': 'conn_ether', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:ETH2', 'functionType': 'Ethernet'}],
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},

                   'bios': {'manageBios': False, 'overriddenSettings': []}}]


###########################################################################
#  Tagged LLDP Data Variables
###########################################################################

lig_edit_taggedLLDP =  {
          'IPV4_ONLY':
            {'name': 'MAT_LIG',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings","lldpIpAddressMode":"IPV4"},
           'uplinkSets': [MAT_uplink_sets['MAT_UplinkSet_1'].copy(),MAT_uplink_sets['MAT_UplinkSet_3'].copy(),MAT_uplink_sets['MAT_UplinkSet_4'].copy(),MAT_uplink_sets['MAT_UplinkSet_5'].copy(),MAT_uplink_sets['MAT_UplinkSet_6'].copy(),MAT_uplink_sets['MAT_UplinkSet_7'].copy(),MAT_uplink_sets['MAT_UplinkSet_8'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                       {'bay': 1, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                       {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'HighlyAvailable',
           'enclosureIndexes': [1,2],
           'qosConfiguration': None
           },

        'IPV6_ONLY':
        {'name': 'MAT_LIG',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings","lldpIpAddressMode":"IPV6"},
           'uplinkSets': [MAT_uplink_sets['MAT_UplinkSet_1'].copy(),MAT_uplink_sets['MAT_UplinkSet_3'].copy(),MAT_uplink_sets['MAT_UplinkSet_4'].copy(),MAT_uplink_sets['MAT_UplinkSet_5'].copy(),MAT_uplink_sets['MAT_UplinkSet_6'].copy(),MAT_uplink_sets['MAT_UplinkSet_7'].copy(),MAT_uplink_sets['MAT_UplinkSet_8'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                       {'bay': 1, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                       {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'HighlyAvailable',
           'enclosureIndexes': [1,2],
           'qosConfiguration': None
           },
        'BOTH_IPV4_IPV6':
            {'name': 'MAT_LIG',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings","lldpIpAddressMode":"BOTH_IPV4_IPV6"},
           'uplinkSets': [MAT_uplink_sets['MAT_UplinkSet_1'].copy(),MAT_uplink_sets['MAT_UplinkSet_3'].copy(),MAT_uplink_sets['MAT_UplinkSet_4'].copy(),MAT_uplink_sets['MAT_UplinkSet_5'].copy(),MAT_uplink_sets['MAT_UplinkSet_6'].copy(),MAT_uplink_sets['MAT_UplinkSet_7'].copy(),MAT_uplink_sets['MAT_UplinkSet_8'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                       {'bay': 1, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                       {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'HighlyAvailable',
           'enclosureIndexes': [1,2],
           'qosConfiguration': None
           },
        'DISABLE_LLDP':
            {'name': 'MAT_LIG',
           'type': 'logical-interconnect-groupV4',
           'enclosureType': 'SY12000',
           "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
           'uplinkSets': [MAT_uplink_sets['MAT_UplinkSet_1'].copy(),MAT_uplink_sets['MAT_UplinkSet_3'].copy(),MAT_uplink_sets['MAT_UplinkSet_4'].copy(),MAT_uplink_sets['MAT_UplinkSet_5'].copy(),MAT_uplink_sets['MAT_UplinkSet_6'].copy(),MAT_uplink_sets['MAT_UplinkSet_7'].copy(),MAT_uplink_sets['MAT_UplinkSet_8'].copy()],
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                       {'bay': 4, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                       {'bay': 1, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                       {'bay': 4, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
           'internalNetworkUris': [],
           'interconnectBaySet': 1,
           'redundancyType': 'HighlyAvailable',
           'enclosureIndexes': [1,2],
           'qosConfiguration': None
           }
        }


MLAGTEAMEDIP='30.10.1.40'
MLAGRESULTS='C:\Users\Administrator\Desktop\ISSURESULTS\\'
MLAGSERVERIP='90.1.0.155'
MLAGSERVERUSER='Administrator'
MLAGSERVERPASSWORD='hpvse123'
MLAGSERVERDOMAINPWD='12iso*help'

firmwareupgrade_url='http://hf-cit.us.rdlabs.hpecorp.net:9300/r1.3.0/Potash/development/fv1-1.3.0-34/'
firmwareupgrade_package='icm_fv1-1.3.0-34-2018-01-03-D.pkg'
firmwaredowngrade_url='http://hf-cit.us.rdlabs.hpecorp.net:9300/r1.3.0/Potash/development/fv1-1.3.0-33/'
firmwaredowngrade_package='icm_fv1-1.3.0-33-2018-01-02-D.pkg'

linuxip='90.1.0.201'
linuxuser='root'
linuxpassword='iso*help'
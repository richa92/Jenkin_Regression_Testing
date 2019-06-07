
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

features = "security"

featureTogglesMapping = {
    "security": ["META_FIPSCompliant"]
}

Potash_IC_FIPS = {'name': 'CN754404RC, interconnect 3'}
Potash_LI_ibs3 = {'name': 'LE-LIG_Potash_HA'}
Potash_LI_ibs2 = {'name': 'LE-LIG_Potash_A'}
Carbon_LI = {'name': 'LE-LIG_Carbon-1'}
Potash_LI = {'name': 'LE-LIG_Potash_HA'}

upgradeBundleAbsloutePath = 'C:\SPP\potash\upgrade.iso'
downgradeBundleAbsloutePath = 'C:\SPP\potash\downgrade.iso'

LE_FW_UPGRADE = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/upgrade",
                 "firmwareUpdateOn": "SharedInfrastructureOnly",
                 "logicalInterconnectUpdateMode": "Orchestrated",
                 "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                 "updateFirmwareOnUnmanagedInterconnect": True}

LI_fwupdate_orchestrated = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
                            'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
                            'validationType': 'ValidateBestEffort',
                            'sppUri': '/rest/firmware-drivers/upgrade'}

LI_downgrade = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
                'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
                'validationType': 'ValidateBestEffort',
                'sppUri': '/rest/firmware-drivers/downgrade'}


ethernet_networks = [{'name': 'eth_200', 'type': 'ethernet-networkV4', 'vlanId': 200, 'purpose': 'Management',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'eth_100', 'type': 'ethernet-networkV4', 'vlanId': 100, 'purpose': 'Management',
                      'smartLink': False, 'privateNetwork': False}
                     ]

ethernet_networks_new = [{'name': 'eth_102', 'type': 'ethernet-networkV4', 'vlanId': 102, 'purpose': 'Management',
                          'smartLink': False, 'privateNetwork': False}
                         ]

fc_networks = [
    {'name': 'FC_A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'FC_B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'Carbon_A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'Carbon_B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
]

fcoe_networks = [{'name': 'FCoE_A201', 'type': 'fcoe-networkV4', 'vlanId': 201, 'managedSanUri': None},
                 {'name': 'FCoE_B200', 'type': 'fcoe-networkV4', 'vlanId': 200, 'managedSanUri': None}
                 ]

uplink_sets_carbon = {'upset_eth_200': {'name': 'up_eth_a', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                        'networkUris': ['eth_200'], 'mode': 'Auto',
                                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]},
                      'upset_carbon_a': {'name': 'up_carbon_a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                         'networkUris': ['Carbon_A'], 'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '1', 'port': '1', 'speed': 'Auto'}]},
                      'upset_carbon_b': {'name': 'up_carbon_b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                         'networkUris': ['Carbon_B'], 'mode': 'Auto',
                                         'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '4', 'port': '2', 'speed': 'Auto'}]}

                      }

uplink_sets = {'upset_eth_200': {'name': 'up_eth_a', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                 'networkUris': ['eth_200'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]},
               'upset_fc_a': {'name': 'up_fc_a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                              'networkUris': ['FC_A'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'upset_fc_b': {'name': 'up_fc_b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                              'networkUris': ['FC_B'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}]}

               }
uplink_set_new = {'name': 'up_eth_b', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                  'networkUris': ['eth_100'], 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'desiredSpeed': 'Auto',
                                              'logicalLocation':
                                              {'locationEntries': [
                                                  {'relativeValue': 62, 'type': 'Port'},
                                                  {'relativeValue': 6, 'type': 'Bay'},
                                                  {'relativeValue': 2, 'type': 'Enclosure'}
                                              ]
                                              }
                                              }
                                             ],
                  }

lig_potash_HA = {'name': 'LIG_Potash_HA',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'SY12000',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                 'uplinkSets': [uplink_sets['upset_eth_200'].copy(),
                                uplink_sets['upset_fc_a'].copy(),
                                uplink_sets['upset_fc_b'].copy()
                                ],
                 'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                             {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                             {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                             {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}],
                 'internalNetworkUris': [],
                 'interconnectBaySet': 3,
                 'redundancyType': 'HighlyAvailable',
                 'enclosureIndexes': [1, 2],
                 'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
                 }
lig_potash_A = {'name': 'LIG_Potash_A',
                'type': 'logical-interconnect-groupV6',
                'enclosureType': 'SY12000',
                "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                'uplinkSets': [],
                'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},

                                            {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}],
                'internalNetworkUris': [],
                'interconnectBaySet': 2,
                'redundancyType': 'NonRedundantASide',
                'enclosureIndexes': [1, 2],
                'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
                }

lig_carbon = {'name': 'LIG_Carbon',
              'type': 'logical-interconnect-groupV6',
              'enclosureType': 'SY12000',
              "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
              'uplinkSets': [],
              'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                          {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
              'internalNetworkUris': [],
              'interconnectBaySet': 1,
              'redundancyType': 'Redundant',
              'enclosureIndexes': [-1],
              'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
              }

enc_groups_me_old = {'name': 'EG_HA',
                     'enclosureCount': 2,
                     'interconnectBayMappings': [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon"},
                                                 {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_A"},
                                                 {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"},
                                                 {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon"},
                                                 {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                 {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"},
                                                 {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_A"},
                                                 {'interconnectBay': 3, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"},
                                                 {'interconnectBay': 6, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"}
                                                 ],
                     'ipAddressingMode': 'DHCP',
                     'powerMode': 'RedundantPowerFeed'}

enc_groups_me = {'name': 'EG_HA',
                 'enclosureCount': 2,
                 'interconnectBayMappings': [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"},
                                             {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"},
                                             {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 3, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"},
                                             {'interconnectBay': 6, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Potash_HA"}
                                             ],
                 'ipAddressingMode': 'DHCP',
                 'powerMode': 'RedundantPowerFeed'}


licenses_1 = [{'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
              {'key': 'ABSE D9MA H9P9 CHUZ V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9FQP XN5W CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

# logical_enclosure_multi = {'name': 'LE', 'enclosureUris': ['ENC:FVTVP30012', 'ENC:FVTVP30010'], 'enclosureGroupUri': 'EG:EG_HA', 'firmwareBaselineUri': None,
# s                          'forceInstallFirmware': False}

logical_enclosure_multi = {'name': 'LE', 'enclosureUris': ['ENC:CN754404RC', 'ENC:FVTCRMBFS3'], 'enclosureGroupUri': 'EG:EG_HA', 'firmwareBaselineUri': None, 'forceInstallFirmware': False}
expected_logical_enclosure = {'type': 'LogicalEnclosureV4', 'name': 'LE', 'status': 'OK', 'enclosureUris': ['ENC:FVTVP30012', 'ENC:FVTVP30010'], 'enclosureGroupUri': 'EG:EG_HA'}

server_profile = {'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:FVTVP30012, bay 6',
                  'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                  'macType': 'Physical', 'wwnType': 'Physical',
                  'name': 'BFS_FC_SP', 'description': '', 'affinity': 'Bay',
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                  'connectionSettings': {
                      'connections': [
                          {'id': 1, 'name': 'conn_fc_a', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:FC_A', 'functionType': 'FibreChannel',
                             'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                          {'id': 2, 'name': 'conn_fc_b', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:FC_B', 'functionType': 'FibreChannel',
                           'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                          {'id': 3, 'name': 'eth_conn_a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth_200', 'functionType': 'Ethernet'}
                      ]},
                  'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                  'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                  'sanStorage': {'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                 'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:BFS_Security', 'lunType': 'Manual', 'lun': 1,
                                                        'isBootVolume': True,
                                                        'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                            'targetSelector': 'Auto', 'targets': []
                                                                          },
                                                                         {'isEnabled': True, 'connectionId': 2,
                                                                          'targetSelector': 'Auto', 'targets': []
                                                                          }
                                                                         ]}]},
                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                  'bios': {'manageBios': False, 'overriddenSettings': []}}

edit_server_profile = {'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:FVTVP30012, bay 6',
                       'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                       'macType': 'Physical', 'wwnType': 'Physical', 'serverProfileTemplateUri': '',
                       'name': 'BFS_FC_SP', 'description': '', 'affinity': 'Bay',
                       "iscsiInitiatorName": None, "iscsiInitiatorNameType": "AutoGenerated",
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                                    'firmwareInstallType': None, "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
                       'connectionSettings': {'connections': [
                           {'id': 1, 'name': 'conn_fc_a', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:FC_A', 'functionType': 'FibreChannel',

                            'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume', 'iscsi': {},
                                     "targets": [
                                  {
                                      "arrayWwpn": "20110002AC009290",
                                      "lun": "1"
                                  }
                            ],
                            }},
                           {'id': 2, 'name': 'conn_fc_b', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FC:FC_B', 'functionType': 'FibreChannel',

                            'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume', 'iscsi': {},
                                     "targets": [
                                {
                                    "arrayWwpn": "21110002AC009290",
                                    "lun": "1"
                                }
                            ],
                            }},
                           {'id': 3, 'name': 'eth_conn_a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth_200', 'functionType': 'Ethernet',
                            'boot': {'priority': 'NotBootable', 'iscsi': {}}},
                           {'id': 4, 'name': 'eth_conn_b', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet',
                            'boot': {'priority': 'NotBootable', 'iscsi': {}}}
                       ]},
                       'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                       'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                       'sanStorage': {'hostOSType': 'SuSE (10.x, 11.x, 12.x)', 'manageSanStorage': True,
                                      'volumeAttachments': [{'id': 1, 'volumeStorageSystemUri': 'SSYS:3par', 'volumeStoragePoolUri': 'SPOOL:test', 'volumeUri': 'VolName:BFS_Security', 'lunType': 'Manual', 'lun': '1',
                                                             'isBootVolume': True,
                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                               'targetSelector': 'Auto', "targets": ["20:11:00:02:AC:00:92:90"]
                                                                               },
                                                                              {'isEnabled': True, 'connectionId': 2,
                                                                               'targetSelector': 'Auto', "targets": ["21:11:00:02:AC:00:92:90"]
                                                                               }
                                                                              ]},
                                                            {'id': 2, 'volumeStorageSystemUri': 'SSYS:3par', 'volumeStoragePoolUri': 'SPOOL:test', 'volumeUri': 'VolName:BFS_Security_data_shared', 'lunType': 'Auto', 'lun': None,
                                                             'isBootVolume': False,
                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                               'targetSelector': 'Auto', "targets": ["20:11:00:02:AC:00:92:90"]
                                                                               },
                                                                              {'isEnabled': True, 'connectionId': 2,
                                                                               'targetSelector': 'Auto', "targets": ["21:11:00:02:AC:00:92:90"]
                                                                               }
                                                                              ]}

                                                            ]},
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                       'bios': {'manageBios': False, 'overriddenSettings': []}}
disable_uplink = {
    "associatedUplinkSetUri": "up_eth",
    "interconnectName": "FVTVP30012, interconnect 3",
    "portType": "Uplink",
    "portId": "FVTVP30012, interconnect 3:Q2:1",
              "portHealthStatus": "Normal",
              "capability": [
                  "Ethernet",
                  "FibreChannel",
                  "EnetFcoe"
              ],
    "configPortTypes": [
                  "Ethernet",
                  "EnetFcoe"
              ],
    "enabled": "false",
    "portName": "Q2:1",
    "portStatus": "Linked",
    "type": "port"
}

enable_uplink = {
    "associatedUplinkSetUri": "up_eth",
    "interconnectName": "FVTVP30012, interconnect 3",
    "portType": "Uplink",
    "portId": "FVTVP30012, interconnect 3:Q2:1",
              "portHealthStatus": "Normal",
              "capability": [
                  "Ethernet",
                  "FibreChannel",
                  "EnetFcoe"
              ],
    "configPortTypes": [
                  "Ethernet",
                  "EnetFcoe"
              ],
    "enabled": "true",
    "portName": "Q2:1",
    "portStatus": "Linked",
    "type": "port"
}
app_sd_body = {"errorCode": "CI", "encrypt": True}
le_sd_body_enc = {"errorCode": "LE", "encrypt": True}
support_dump = {"LI_name": "LE-LIG_Potash_HA"}

storage_systems_fc = {"type": "StorageSystemV4", "credentials": {"username": "3paradm", "password": "3pardata"},
                      "name": "3par",
                      "hostname": "192.168.144.125",
                      "family": "StoreServ",
                      "deviceSpecificAttributes":
                      {"managedDomain": "NO DOMAIN"
                       },
                      "ports": [{"type": "StorageTargetPortV4",
                                 "name": "0:1:1",
                                 "expectedNetworkUri": "FC:FC_A",
                                 "expectedNetworkName": "FC_A",
                                 "mode": "Managed"},
                                {"type": "StorageTargetPortV4",
                                 "name": "0:1:2",
                                 "expectedNetworkUri": None,
                                 "expectedNetworkName": None,
                                 "mode": "AutoSelectExpectedSan"},
                                {"type": "StorageTargetPortV4",
                                 "name": "1:1:1",
                                 "expectedNetworkUri": "FC:FC_B",
                                 "expectedNetworkName": "FC_B",
                                 "mode": "Managed"},
                                {"type": "StorageTargetPortV4",
                                 "name": "1:1:2",
                                 "expectedNetworkUri": None,
                                 "expectedNetworkName": None,
                                 "mode": "AutoSelectExpectedSan"},
                                {"type": "StorageTargetPortV4",
                                 "name": "1:2:1",
                                 "expectedNetworkUri": None,
                                 "expectedNetworkName": None,
                                 "mode": "AutoSelectExpectedSan"},
                                {"type": "StorageTargetPortV4",
                                 "name": "1:2:2",
                                 "expectedNetworkUri": None,
                                 "expectedNetworkName": None,
                                 "mode": "AutoSelectExpectedSan"},
                                ]

                      }

storage_systems_desc_fc = {"type": "StorageSystemV4", "credentials": {"username": "3paradm", "password": "3pardata"},
                           "name": "3par",
                           "hostname": "192.168.144.125",
                           "family": "StoreServ",
                           "deviceSpecificAttributes":
                           {"managedDomain": "NO DOMAIN"
                            },
                           "ports": [{"type": "StorageTargetPortV4",
                                      "name": "1:2:2",
                                      "expectedNetworkUri": None,
                                      "expectedNetworkName": None,
                                      "mode": "AutoSelectExpectedSan"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "1:2:1",
                                      "expectedNetworkUri": None,
                                      "expectedNetworkName": None,
                                      "mode": "AutoSelectExpectedSan"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "1:1:2",
                                      "expectedNetworkUri": None,
                                      "expectedNetworkName": None,
                                      "mode": "AutoSelectExpectedSan"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "1:1:1",
                                      "expectedNetworkUri": "FC:FC_B",
                                      "expectedNetworkName": "FC_B",
                                      "mode": "Managed"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "0:1:2",
                                      "expectedNetworkUri": None,
                                      "expectedNetworkName": None,
                                      "mode": "AutoSelectExpectedSan"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "0:1:1",
                                      "expectedNetworkUri": "FC:FC_A",
                                      "expectedNetworkName": "FC_A",
                                      "mode": "Managed"},
                                     ]

                           }

expected_storage_systems_fc = [{"type": "StorageSystemV4", "credentials": {"username": "3paradm"},
                                "name": "3par",
                                "hostname": "192.168.144.125",
                                "family": "StoreServ",
                                "deviceSpecificAttributes":
                                            {"managedDomain": "NO DOMAIN",
                                             "serialNumber": "1637520"
                                             },
                                "ports": [{"type": "StorageTargetPortV4",
                                           "name": "0:1:1",
                                           "expectedNetworkUri": "FC:FC_A",
                                           "expectedNetworkName": "FC_A",
                                           "mode": "Managed"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "0:1:2",
                                           "expectedNetworkUri": None,
                                           "expectedNetworkName": None,
                                           "mode": "AutoSelectExpectedSan"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "1:1:1",
                                           "expectedNetworkUri": "FC:FC_B",
                                           "expectedNetworkName": "FC_B",
                                           "mode": "Managed"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "1:1:2",
                                           "expectedNetworkUri": None,
                                           "expectedNetworkName": None,
                                           "mode": "AutoSelectExpectedSan"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "1:2:1",
                                           "expectedNetworkUri": None,
                                           "expectedNetworkName": None,
                                           "mode": "AutoSelectExpectedSan"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "1:2:2",
                                           "expectedNetworkUri": None,
                                           "expectedNetworkName": None,
                                           "mode": "AutoSelectExpectedSan"},
                                          ]

                                }
                               ]

storage_pool_fc = {'storageSystemUri': '3par', 'name': 'test', "isManaged": True}


storage_volumes_fc = [
    {
        "name": "",
        "description": "",
                       "storageSystemUri": "3par",
                       "deviceVolumeName": "BFS_Security",
                       "isShareable": False


    },
    {
        "name": "",
        "description": "",
                       "storageSystemUri": "3par",
                       "deviceVolumeName": "BFS_Security_data_shared",
                       "isShareable": True
    }

]


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

features = "security"

featureTogglesMapping = {
    "security": ["META_FIPSCompliant"]
}

Carbon16_LI_ibs2 = {'name': 'LE-LIG_Carbon_16-1'}
ENC1 = 'FVTVP30012'
ICM_1 = ENC1 + ', interconnect 1'
ICM_2 = ENC1 + ', interconnect 2'
ICM_4 = ENC1 + ', interconnect 4'
ICM_5 = ENC1 + ', interconnect 5'


Carbon_16_ICM = 'Virtual Connect SE 16Gb FC Module for Synergy'

LIG_Version = 'logical-interconnect-groupV6'
LIG_ethernet_version = 'EthernetInterconnectSettingsV5'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'


upgradeBundleAbsloutePath = 'C:\SPP\carbon_16\upgrade.iso'
downgradeBundleAbsloutePath = 'C:\SPP\carbon_16\downgrade.iso'

ethernet_networks = [{'name': 'eth_200', 'type': eth_network_Version, 'vlanId': 200, 'purpose': 'Management',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'eth_100', 'type': eth_network_Version, 'vlanId': 100, 'purpose': 'Management',
                      'smartLink': False, 'privateNetwork': False}
                     ]

ethernet_networks_new = [{'name': 'eth_102', 'type': eth_network_Version, 'vlanId': 102, 'purpose': 'Management',
                          'smartLink': False, 'privateNetwork': False}
                         ]


fc_networks = [
    {'name': 'FC_A', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'FC_B', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'Carbon_A', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'Carbon_B', 'type': fc_network_version, 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
]

licenses_1 = [{'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
              {'key': 'ABSE D9MA H9P9 CHUZ V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9FQP XN5W CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

fcoe_networks = [{'name': 'FCoE_A201', 'type': 'fcoe-networkV4', 'vlanId': 201, 'managedSanUri': None},
                 {'name': 'FCoE_B200', 'type': 'fcoe-networkV4', 'vlanId': 200, 'managedSanUri': None}
                 ]

uplink_sets = {'upset_eth_200': {'name': 'up_eth_a', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                 'networkUris': ['eth_200'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]},
               'upset_fc_a': {'name': 'up_fc_a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                              'networkUris': ['FC_A'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'upset_eth_100': {'name': 'up_eth_b', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                 'networkUris': ['eth_100'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]},
               'upset_fc_b': {'name': 'up_fc_b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                              'networkUris': ['FC_B'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]}

               }


lig_carbon_16 = {'name': 'LIG_Carbon_16',
                 'type': LIG_Version,
                 'enclosureType': 'SY12000',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                 # 'uplinkSets': [uplink_sets['upset_fc_b'].copy()],
                 'uplinkSets': [],
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': Carbon_16_ICM, 'enclosureIndex': -1},
                                             {'bay': 4, 'enclosure': -1, 'type': Carbon_16_ICM, 'enclosureIndex': -1}],
                 'internalNetworkUris': [],
                 'interconnectBaySet': 1,
                 'redundancyType': 'Redundant',
                 'enclosureIndexes': [-1],
                 'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
                 }

encl_group = [{"name": "EG-CARBON_16",
               "interconnectBayMappings": [{"interconnectBay": 1,
                                            "logicalInterconnectGroupUri": "LIG:LIG_Carbon_16"},
                                           {"interconnectBay": 4,
                                            "logicalInterconnectGroupUri": "LIG:LIG_Carbon_16"}],
               "configurationScript": "",
               "powerMode": "RedundantPowerFeed",
               "ipAddressingMode": "DHCP",
               "ipRangeUris": [],
               "enclosureCount": 2}]


logical_encl = [{"name": "LE",
                 "enclosureUris": ["ENC:SGH734VBEB"],
                 "enclosureGroupUri": "EG:EG-CARBON_16",
                 "firmwareBaselineUri": None,
                 "forceInstallFirmware": False}]

enc_groups_me = {'name': 'EG-CARBON_16',
                 'enclosureCount': 2,
                 'interconnectBayMappings': [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon_16"},
                                             {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon_16"},
                                             {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None}
                                             ],
                 'ipAddressingMode': 'DHCP',
                 'powerMode': 'RedundantPowerFeed'}

logical_enclosure_multi = {'name': 'LE',
                           'enclosureUris': ['ENC:FVTVP30012', 'ENC:FVTVP30010'],
                           'enclosureGroupUri': 'EG:EG-CARBON_16',
                           'firmwareBaselineUri': None,
                           'forceInstallFirmware': False}

LI_downgrade = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
                'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
                'validationType': 'ValidateBestEffort',
                'sppUri': '/rest/firmware-drivers/downgrade'}


LI_fwupdate_orchestrated = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
                            'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
                            'validationType': 'ValidateBestEffort',
                            'sppUri': '/rest/firmware-drivers/upgrade'}

lig_enablev1_v2 = {
    'type': 'snmp-configuration',
    "readCommunity": "oneviewtest",
    "enabled": True,
    'systemContact': '',
    'snmpAccess': [],
    'v3Enabled': True,
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}

lig_snmp_unsupported_users = {
    'type': 'snmp-configuration',
    "readCommunity": "public",
    "enabled": False,
    'systemContact': '',
    'snmpAccess': [],
    'v3Enabled': True,
    'snmpUsers': [
        {'snmpV3UserName': 'snmptestuser3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'TDEA'},
        {'snmpV3UserName': 'snmptestuser2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
        {'snmpV3UserName': 'snmptestuser1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}

    ],
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}

disable_uplink = {
    "associatedUplinkSetUri": "up_eth",
    "interconnectName": "FVTVP30012, interconnect 2",
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
    "interconnectName": "FVTVP30012, interconnect 2",
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

uplink_set_new = {'name': 'up_eth_b', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                  'networkUris': ['eth_100'], 'mode': 'Auto',
                  'logicalPortConfigInfos': [{'desiredSpeed': 'Auto',
                                              'logicalLocation':
                                              {'locationEntries': [
                                                  {'relativeValue': 63, 'type': 'Port'},
                                                  {'relativeValue': 2, 'type': 'Bay'},
                                                  {'relativeValue': 1, 'type': 'Enclosure'}
                                              ]
                                              }
                                              }
                                             ],
                  }


server_profile = {'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:FVTVP30012, bay 6',
                  'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                  'macType': 'Physical', 'wwnType': 'Physical',
                  'name': 'SP_Nitro_data', 'description': '', 'affinity': 'Bay',
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                  'connectionSettings': {
                      'connections': [
                          {'id': 1, 'name': 'eth_conn_a', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth_200', 'functionType': 'Ethernet'}
                      ]},
                  'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                  'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                  'bios': {'manageBios': False, 'overriddenSettings': []}
                  }

edit_server_profile = {'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:FVTVP30012, bay 6',
                       'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                       'macType': 'Physical', 'wwnType': 'Physical', 'serverProfileTemplateUri': '',
                       'name': 'SP_Nitro_data', 'description': '', 'affinity': 'Bay',
                       "iscsiInitiatorName": None, "iscsiInitiatorNameType": "AutoGenerated",
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False,
                                    'firmwareInstallType': None, "firmwareScheduleDateTime": "", "firmwareActivationType": "Immediate"},
                       'connectionSettings': {'connections': [
                           {'id': 1, 'name': 'eth_conn_a', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth_100', 'functionType': 'Ethernet'},
                           {'id': 2, 'name': 'eth_conn_b', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth_200', 'functionType': 'Ethernet'}
                       ]},
                       'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                       'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                       'bios': {'manageBios': False, 'overriddenSettings': []}}

icm_dic = {'name': 'FVTVP30012, interconnect 3'}

app_sd_body = {"errorCode": "CI", "encrypt": True}
le_sd_body_enc = {"errorCode": "LE", "encrypt": True}
support_dump = {"LI_name": "LE-LIG_Nitro"}

LE_FW_UPGRADE = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/upgrade",
                 "firmwareUpdateOn": "SharedInfrastructureOnly",
                 "logicalInterconnectUpdateMode": "OrchestratedBestEffort",
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

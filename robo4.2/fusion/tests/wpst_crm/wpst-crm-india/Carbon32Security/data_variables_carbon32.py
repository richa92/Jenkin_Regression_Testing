# data_carbon32
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

fc_networks = [
    {'name': 'Carbon_A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'Carbon_B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
]
uplink_sets = {'upset_eth_100': {'name': 'up_eth_100', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                 'networkUris': ['eth_100'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.4', 'speed': 'Auto'},
                                                            {'enclosure': '2', 'bay': '5', 'port': 'Q1.4', 'speed': 'Auto'}
                                                            ]},
               'upset_carbon_a': {'name': 'up_carbon_a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                  'networkUris': ['Carbon_A'], 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '1', 'port': '2', 'speed': 'Auto'}]},
               'upset_carbon_b': {'name': 'up_carbon_b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                  'networkUris': ['Carbon_B'], 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '4', 'port': '2', 'speed': 'Auto'}]}

               }


lig_carbon_32 = {'name': 'LIG_Carbon_32',
                 'type': 'logical-interconnect-groupV6',
                 'enclosureType': 'SY12000',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                 'uplinkSets': [uplink_sets['upset_carbon_a'].copy(),
                                uplink_sets['upset_carbon_b'].copy()],
                 'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                             {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}],
                 'internalNetworkUris': [],
                 'interconnectBaySet': 1,
                 'redundancyType': 'Redundant',
                 'enclosureIndexes': [-1],
                 'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
                 }

lig_carbon_32_snmp_config = {
    'type': 'snmp-configuration',
    'snmpUsers': [
        {'snmpV3UserName': 'snmptestuser1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
    ],
    'readCommunity': 'public',
    'systemContact': '',
    'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'snmptestuser1', 'inform':False, 'communityString':'', 'port':'11650'}],
    'snmpAccess': [],
    'v3Enabled': True,
    'enabled': False,
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}
lig_carbon_32_invalid_users = {
    'type': 'snmp-configuration',
    'snmpUsers': [
        {'snmpV3UserName': 'snmptestuser1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
        {'snmpV3UserName': 'snmptestuser2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
        {'snmpV3UserName': 'snmptestuser3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
        {'snmpV3UserName': 'snmptestuser4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}
    ],
    'readCommunity': 'public',
    'systemContact': '',
    'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'snmptestuser1', 'inform':False, 'communityString':'', 'port':'11650'}],
    'snmpAccess': [],
    'v3Enabled': True,
    'enabled': False,
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}
li_snmp_v1_v2_enable = {
    'type': 'snmp-configuration',
    'snmpUsers': [
        {'snmpV3UserName': 'snmptestuser1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
    ],
    'readCommunity': 'public',
    'systemContact': '',
    'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'snmptestuser1', 'inform':False, 'communityString':'', 'port':'11650'}],
    'snmpAccess': [],
    'v3Enabled': True,
    'enabled': True,
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}
li_snmp_v1_v2_disable = {
    'type': 'snmp-configuration',
    'snmpUsers': [
        {'snmpV3UserName': 'snmptestuser1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
    ],
    'readCommunity': 'public',
    'systemContact': '',
    'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'snmptestuser1', 'inform':False, 'communityString':'', 'port':'11650'}],
    'snmpAccess': [],
    'v3Enabled': True,
    'enabled': False,
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}
enc_groups_me = {'name': 'EG_Carbon_32',
                 'enclosureCount': 2,
                 'interconnectBayMappings': [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon_32"},
                                             {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon_32"},
                                             {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None}
                                             ],
                 'ipAddressingMode': 'DHCP',
                 'powerMode': 'RedundantPowerFeed'}

lig_enablev1_v2 = {
    'type': 'snmp-configuration',
    "readCommunity": "public",
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
        {'snmpV3UserName': 'snmptestuser3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
        {'snmpV3UserName': 'snmptestuser2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES'}
    ],
    'description': None,
    'name': None,
    'state': None,
    'status': None,
    'eTag': None,
    'category': 'snmp-configuration',
    'uri': None
}

logical_enclosure_multi = {'name': 'LE', 'enclosureUris': ['ENC:FVTVP30012', 'ENC:FVTVP30010'], 'enclosureGroupUri': 'EG:EG_Carbon_32',
                           'firmwareBaselineUri': None,
                           'forceInstallFirmware': False}

le_sd_body_enc = {"errorCode": "LE", "encrypt": True}

server_profile = {'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:FVTVP30010, bay 6',
                  'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical',
                  'macType': 'Physical', 'wwnType': 'Physical',
                  'name': 'SP_Carbon32', 'description': '', 'affinity': 'Bay',
                  'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                  'connectionSettings': {
                      'connections': [
                          {'id': 1, 'name': 'conn_fc_a', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:Carbon_A', 'functionType': 'FibreChannel',
                             'boot': {'priority': 'NotBootable', 'iscsi': {}}, 'mac': None, 'wwpn': None, 'wwnn': None},
                          {'id': 2, 'name': 'conn_fc_b', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:Carbon_B', 'functionType': 'FibreChannel',
                           'boot': {'priority': 'NotBootable', 'iscsi': {}}, 'mac': None, 'wwpn': None, 'wwnn': None}

                      ]},
                  'boot': {'manageBoot': True, 'order': ['HardDisk', 'CD', 'USB', 'PXE']},
                  'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                  'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                 'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:carbon32_data', 'lunType': 'Auto', 'lun': None,
                                                        'isBootVolume': False,
                                                        'storagePaths': [{'isEnabled': True, 'connectionId': 1,
                                                                          'targetSelector': 'Auto', 'targets': []
                                                                          }
                                                                         ]}]},
                  'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                  'bios': {'manageBios': False, 'overriddenSettings': []}}


remote_syslog = {"type": "RemoteSyslog",
                 "sendTestLog": True,
                 "remoteSyslogPort": "514",
                 "remoteSyslogDestination": "192.168.144.167",
                 "enabled": True
                 }

storage_systems_fc = {"type": "StorageSystemV4", "credentials": {"username": "3paradm", "password": "3pardata"},
                      "name": "3par",
                      "hostname": "192.168.144.125",
                      "family": "StoreServ",
                      "deviceSpecificAttributes":
                      {"managedDomain": "NO DOMAIN"
                       },
                      "ports": [{"type": "StorageTargetPortV4",
                                 "name": "0:1:1",
                                 "expectedNetworkUri": "FC:Carbon_B",
                                 "expectedNetworkName": "Carbon_B",
                                 "mode": "Managed"},
                                {"type": "StorageTargetPortV4",
                                 "name": "0:1:2",
                                 "expectedNetworkUri": None,
                                 "expectedNetworkName": None,
                                 "mode": "AutoSelectExpectedSan"},
                                {"type": "StorageTargetPortV4",
                                 "name": "1:1:1",
                                 "expectedNetworkUri": "FC:Carbon_A",
                                 "expectedNetworkName": "Carbon_A",
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
                                      "expectedNetworkUri": "FC:Carbon_A",
                                      "expectedNetworkName": "Carbon_A",
                                      "mode": "Managed"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "0:1:2",
                                      "expectedNetworkUri": None,
                                      "expectedNetworkName": None,
                                      "mode": "AutoSelectExpectedSan"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "0:1:1",
                                      "expectedNetworkUri": "FC:Carbon_B",
                                      "expectedNetworkName": "Carbon_B",
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
                                           "expectedNetworkUri": None,
                                           "expectedNetworkName": None,
                                           "mode": "AutoSelectExpectedSan"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "0:1:2",
                                           "expectedNetworkUri": None,
                                           "expectedNetworkName": None,
                                           "mode": "AutoSelectExpectedSan"},
                                          {"type": "StorageTargetPortV4",
                                           "name": "1:1:1",
                                           "expectedNetworkUri": "FC:Carbon_A",
                                           "expectedNetworkName": "Carbon_A",
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
                       "deviceVolumeName": "carbon32_data",
                       "isShareable": False


    },
    {
        "name": "",
        "description": "",
                       "storageSystemUri": "3par",
                       "deviceVolumeName": "data_carbon32_199",
                       "isShareable": False
    }

]

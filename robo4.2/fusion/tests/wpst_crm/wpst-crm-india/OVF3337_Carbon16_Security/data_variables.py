admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

upgradeBundleAbsloutePath = 'C:\carbon\upgrade.iso'
downgradeBundleAbsloutePath = 'C:\carbon\downgrade.iso'
downgradeincompatibleBundleAbsloutePath = 'C:\carbon\downgrade_incompatible.iso'

fc_networks = [
    {'name': 'Carbon_A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': 'Carbon_B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
     'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
]

Carbon_LI = {'name': 'LE-LIG_Carbon-1'}
uplink_sets = {
    'upset_carbon_a': {'name': 'up_carbon_a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                       'networkUris': ['Carbon_A'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '1', 'port': '1', 'speed': 'Auto'}]},
    'upset_carbon_b': {'name': 'up_carbon_b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                       'networkUris': ['Carbon_B'], 'mode': 'Auto',
                       'logicalPortConfigInfos': [{'enclosure': '-1', 'bay': '4', 'port': '1', 'speed': 'Auto'}]}

}

lig_carbon = {'name': 'LIG_Carbon',
              'type': 'logical-interconnect-groupV5',
              'enclosureType': 'SY12000',
              "ethernetSettings": {"type": "EthernetInterconnectSettingsV4", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
              'uplinkSets': [uplink_sets['upset_carbon_a'].copy(),
                             uplink_sets['upset_carbon_b'].copy()],
              'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                          {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
              'internalNetworkUris': [],
              'interconnectBaySet': 1,
              'redundancyType': 'Redundant',
              'enclosureIndexes': [-1],
              'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}
              }

lig_carbon_snmp_config = {
    'type': 'snmp-configuration',
    'snmpUsers': [
        {'snmpV3UserName': 'snmptestuser1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
    ],
    'readCommunity': 'public',
    'systemContact': '',
    'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'snmptestuser1', 'inform':False, 'communityString':'', 'port':'163'}],
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
snmp_user2 = {'snmpV3UserName': 'snmptestuser2',
              'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                   'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                  {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123',
                                   'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
              'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
enc_groups_me = {'name': 'EG_HA',
                 'enclosureCount': 2,
                 'interconnectBayMappings': [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon"},
                                             {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon"},
                                             {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 3, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None},
                                             {'interconnectBay': 6, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None}
                                             ],
                 'ipAddressingMode': 'DHCP',
                 'powerMode': 'RedundantPowerFeed'}

logical_enclosure_multi = {'name': 'LE', 'enclosureUris': ['ENC:FVTVP30012', 'ENC:FVTVP30010'], 'enclosureGroupUri': 'EG:EG_HA', 'firmwareBaselineUri': None,
                           'forceInstallFirmware': False}

enc_group_external = {'name': 'EG_HA_external',
                      'enclosureCount': 2,
                      'interconnectBayMappings': [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon"},
                                                  {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Carbon"},
                                                  {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 3, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None},
                                                  {'interconnectBay': 6, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': None}
                                                  ],
                      'ipAddressingMode': 'External',
                      'powerMode': 'RedundantPowerFeed'}

logical_enclosure_external = {'name': 'LE', 'enclosureUris': ['ENC:FVTVP30012', 'ENC:FVTVP30010'], 'enclosureGroupUri': 'EG:EG_HA_external', 'firmwareBaselineUri': None,
                              'forceInstallFirmware': False}


server_profile = {'type': 'ServerProfileV9', 'serverHardwareUri': 'SH:FVTVP30012, bay 4',
                  'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG_HA', 'serialNumberType': 'Physical',
                  'macType': 'Physical', 'wwnType': 'Physical',
                  'name': 'SP_Carbon_data', 'description': '', 'affinity': 'Bay',
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
                                 'volumeAttachments': [{'id': 1, 'volumeUri': 'VolName:BFS_Carbon__142_data_shared', 'lunType': 'Auto', 'lun': None,
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
                 "remoteSyslogDestination": "192.168.148.98",
                 "enabled": True
                 }

remote_syslog_fips = {"type": "RemoteSyslog",
                      "sendTestLog": True,
                      "remoteSyslogPort": "514",
                      "remoteSyslogDestination": "192.168.148.49",
                      "enabled": True
                      }

LI_upgrade = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
              'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
              'validationType': 'ValidateBestEffort',
              'sppUri': '/rest/firmware-drivers/upgrade'}

LI_downgrade = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
                'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
                'validationType': 'ValidateBestEffort',
                'sppUri': '/rest/firmware-drivers/downgrade'}

LI_downgrade_incompatible = {'command': 'UPDATE', 'ethernetActivationDelay': '0', 'ethernetActivationType': 'PairProtect',
                             'fcActivationType': 'PairProtect', 'fcActivationDelay': '0', 'force': True,
                             'validationType': 'ValidateBestEffort',
                             'sppUri': '/rest/firmware-drivers/downgrade_incompatible'}

storage_systems_fc = {"type": "StorageSystemV4", "credentials": {"username": "3paradm", "password": "3pardata"},
                      "name": "3par",
                      "hostname": "192.168.144.125",
                      "family": "StoreServ",
                      "deviceSpecificAttributes":
                      {"managedDomain": "NO DOMAIN"
                       },
                      "ports": [{"type": "StorageTargetPortV4",
                                 "name": "0:1:1",
                                 "expectedNetworkUri": "FC:Carbon_A",
                                 "expectedNetworkName": "Carbon_A",
                                 "mode": "Managed"},
                                {"type": "StorageTargetPortV4",
                                 "name": "0:1:2",
                                 "expectedNetworkUri": None,
                                 "expectedNetworkName": None,
                                 "mode": "AutoSelectExpectedSan"},
                                {"type": "StorageTargetPortV4",
                                 "name": "1:1:1",
                                 "expectedNetworkUri": "FC:Carbon_B",
                                 "expectedNetworkName": "Carbon_B",
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
                                      "expectedNetworkUri": "FC:Carbon_B",
                                      "expectedNetworkName": "Carbon_B",
                                      "mode": "Managed"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "0:1:2",
                                      "expectedNetworkUri": None,
                                      "expectedNetworkName": None,
                                      "mode": "AutoSelectExpectedSan"},
                                     {"type": "StorageTargetPortV4",
                                      "name": "0:1:1",
                                      "expectedNetworkUri": "FC:Carbon_A",
                                      "expectedNetworkName": "Carbon_A",
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
                       "deviceVolumeName": "BFS_Carbon_142",
                       "isShareable": False


    },
    {
        "name": "",
        "description": "",
                       "storageSystemUri": "3par",
                       "deviceVolumeName": "BFS_Carbon__142_data_shared",
                       "isShareable": True
    }

]

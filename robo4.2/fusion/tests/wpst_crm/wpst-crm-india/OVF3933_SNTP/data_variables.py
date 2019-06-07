"""
    Data File for Nitro SNTP feature
"""
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

invalid_config_param = 'CRM_NTP_CONFIGURATION_INVALID_CAST_FIELD'
invalid_dst_time = 'CRM_NTP_CONFIGURATION_INVALID_DST_ENDTIME'
invalid_timezone = 'CRM_NTP_CONFIGURATION_INVALID_TIMEZONE'
invalid_dst = 'CRM_NTP_CONFIGURATION_DST_STARTTIME_SHOULD_BE_LESSTHAN_DST_ENDTIME'
invalid_time = 'CRM_NTP_CONFIGURATION_INVALID_DST_TIME'

ENC1 = 'SGH734VBEB'
ENC2 = 'SGH734VBE6'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
METHANE = 'Synergy 50Gb Interconnect Link Module'
LIG_Version = 'logical-interconnect-groupV7'
LIG_ethernet_version = 'EthernetInterconnectSettingsV6'
eth_network_Version = 'ethernet-networkV4'
fcoe_network_version = 'fcoe-networkV4'
fc_network_version = 'fc-networkV4'
UPLINK_TYPE = 'uplink-setV5'
SERVER_PROFILE = 'ServerProfileV10'

LE_NAME = "LE"
LIG_NAME = "LIG_Nitro"
LI_NAME = LE_NAME + '-' + LIG_NAME
US_NAME = 'US1'

ethernet_networks = [
    {"vlanIdRange": "21-25",
     "namePrefix": "Eth_network",
     "privateNetwork": False,
     "smartLink": True,
     "purpose": "General",
     "type": "bulk-ethernet-networkV1",
     "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500},
     }
]

lig_nitro_snmp_not_working = {'name': 'LIG_Nitro',
                              "type": LIG_Version,
                              'enclosureType': 'SY12000',
                              "ethernetSettings": {'type': LIG_ethernet_version, "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              'uplinkSets': [],
                              'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': NITRO, 'enclosureIndex': 1},
                                                          {'bay': 5, 'enclosure': 1, 'type': METHANE, 'enclosureIndex': 1},
                                                          {'bay': 2, 'enclosure': 2, 'type': METHANE, 'enclosureIndex': 2},
                                                          {'bay': 5, 'enclosure': 2, 'type': NITRO, 'enclosureIndex': 2}],
                              'internalNetworkUris': [],
                              'interconnectBaySet': 2,
                              'redundancyType': 'HighlyAvailable',
                              'enclosureIndexes': [1, 2],
                              'snmpConfiguration': {'type': 'snmp-configuration',
                                                    # 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA1', 'v3PrivacyProtocol': 'DES'}],'readCommunity': 'public',
                                                    # 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA1', 'v3PrivacyProtocol': 'DES'}],'readCommunity': 'public',
                                                    'snmpUsers': [{'snmpV3UserName': 'user1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA1', 'v3PrivacyProtocol': 'AES128'}], 'readCommunity': 'public',
                                                    # 'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'11650'}],
                                                    'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':False, 'communityString':'', 'port':'162'}],
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
                                                    }}

lig_nitro = {"name": "LIG_Nitro",
             "type": LIG_Version,
             "downlinkSpeedMode": "SPEED_10GB",
             "enclosureType": "SY12000",
             "ethernetSettings": {'type': LIG_ethernet_version, 'interconnectType': 'Ethernet', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5,
                                  'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True},
             "description": None,
             "status": None,
             "state": None,
             "category": None,
             "created": None,
             "modified": None,
             "eTag": None,
             "uri": None,
             "uplinkSets": [],
             'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': NITRO, 'enclosureIndex': 1},
                                         {'bay': 5, 'enclosure': 1, 'type': METHANE, 'enclosureIndex': 1},
                                         {'bay': 2, 'enclosure': 2, 'type': METHANE, 'enclosureIndex': 2},
                                         {'bay': 5, 'enclosure': 2, 'type': NITRO, 'enclosureIndex': 2}],
             "internalNetworkUris": [],
             'interconnectBaySet': 2,
             'redundancyType': 'HighlyAvailable',
             'enclosureIndexes': [1, 2],
             "qosConfiguration": {"activeQosConfig": {"type": "QosConfiguration", "configType": "Passthrough", "downlinkClassificationType": None, "uplinkClassificationType": None, "qosTrafficClassifiers": None, "description": None, "status": None, "name": None, "state": None, "category": "qos-aggregated-configuration", "created": None, "modified": None, "eTag": None, "uri": None}, "inactiveFCoEQosConfig": None, "inactiveNonFCoEQosConfig": None, "type": "qos-aggregated-configuration", "name": None, "state": None, "status": None, "eTag": None, "modified": None, "created": None, "category": "qos-aggregated-configuration", "uri": None}
             }

enc_group_nitro = [{"name": "EG_HA",
                    "interconnectBayMappings": [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"},
                                                {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 5, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"},
                                                {'interconnectBay': 6, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': None},
                                                {'interconnectBay': 2, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"},
                                                {'interconnectBay': 5, 'enclosureIndex': 2, 'logicalInterconnectGroupUri': "LIG:LIG_Nitro"}
                                                ],
                    "configurationScript": "",
                    "powerMode": "RedundantPowerFeed",
                    "ipAddressingMode": "DHCP",
                    "ipRangeUris": [],
                    "enclosureCount": 2}]

Logical_Enclosure_HA = [{"name": "LE",
                         "enclosureUris": ['ENC:SGH734VBEB', 'ENC:SGH734VBE6'],
                         "enclosureGroupUri": "EG:EG_HA",
                         "firmwareBaselineUri": None,
                         "forceInstallFirmware": False}]

li_name = {'name': 'LE-LIG1'}
IC_name = 'SGH751SLBJ, interconnect 3'
edit_lig = [{'name': 'LIG_Nitro',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'SY12000',
             "ethernetSettings": {"type": "EthernetInterconnectSettingsV5", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "enableTaggedLldp": False, 'enableDdns': True, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
             'uplinkSets': [],
             'interconnectMapTemplate': [{'bay': 2, 'enclosure': 1, 'type': NITRO, 'enclosureIndex': 1},
                                         {'bay': 5, 'enclosure': 1, 'type': METHANE, 'enclosureIndex': 1},
                                         {'bay': 2, 'enclosure': 2, 'type': METHANE, 'enclosureIndex': 2},
                                         {'bay': 5, 'enclosure': 2, 'type': NITRO, 'enclosureIndex': 2}],
             'internalNetworkUris': [],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'enclosureIndexes': [1, 2],
             'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}, 'ntpConfiguration': {'type': 'ntp-configuration', 'enabled': True, 'category': 'ntp_configuration', 'protocolType': 'Sntp', 'authProtocol': None, 'timeZone': None, 'authId': None, 'clientVersion': 'V4', 'clockFormat': 'Twelve_Hours', 'dstStartTime': None, 'dstEndTime': None, 'addressingMode': {'addressingMode': 'Unicast', 'pollInterval': '16', 'pollTimeout': '1', 'pollRetry': '1', 'serverAutoDiscovery': 1, 'sendRequest': False, 'groupAddress': None}},
             }]

unicast = {'addressingMode': 'Unicast', 'pollInterval': 16, 'pollTimeout': 1, 'pollRetry': 1, 'serverAutoDiscovery': 1, 'sendRequest': False, 'groupAddress': None}
multicast = {'addressingMode': 'Multicast', 'pollTimeout': 1, 'pollInterval': 0, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 1000, 'groupAddress': "224.0.0.0", 'sendRequest': False}
broadcast = {'addressingMode': 'Broadcast', 'pollTimeout': 1, 'pollInterval': 0, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 1000, 'groupAddress': "", 'sendRequest': False}
manycast = {'addressingMode': 'Manycast', 'pollTimeout': 1, 'pollInterval': 16, 'pollRetry': 1, 'serverAutoDiscovery': 0, 'delayTime': 0, 'groupAddress': "", 'sendRequest': False}

unicast_edit = {'addressingMode': 'Unicast', 'pollInterval': 16384, 'pollTimeout': 30, 'pollRetry': 10, 'serverAutoDiscovery': 0, 'sendRequest': False, 'groupAddress': None}
unicast_invalid = {'addressingMode': 'Unicast', 'pollInterval': 16385, 'pollTimeout': 35, 'pollRetry': 15, 'serverAutoDiscovery': 0, 'sendRequest': False, 'groupAddress': None}

broadcast_edit = {'addressingMode': 'Broadcast', 'pollTimeout': 30, 'pollInterval': 0, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 1000, 'groupAddress': "", 'sendRequest': True}
broadcast_invalid = {'addressingMode': 'Broadcast', 'pollTimeout': 30, 'pollInterval': 0, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 1000, 'groupAddress': "", 'sendRequest': False}

multicast_edit = {'addressingMode': 'Multicast', 'pollTimeout': 30, 'pollInterval': 0, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 15000, 'groupAddress': "224.0.0.0", 'sendRequest': True}
multicast_invalid = {'addressingMode': 'Multicast', 'pollTimeout': 31, 'pollInterval': 16385, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 15000, 'groupAddress': "224.0.0.0", 'sendRequest': True}

manycast_edit = {'addressingMode': 'Manycast', 'pollTimeout': 30, 'pollInterval': 16384, 'pollRetry': 10, 'serverAutoDiscovery': 0, 'delayTime': 0, 'groupAddress': "", 'sendRequest': False}
edit_lig_ntp = {'type': 'ntp-configuration', 'custom': True, 'category': 'ntp-configuration', 'protocolType': 'Sntp', 'authProtocol': None, 'timeZone': None, 'authId': None, 'authKey': None, 'clientVersion': 'V4', 'clockFormat': 'Twelve_Hours', 'dstStartTime': None, 'dstEndTime': None, 'addressingMode': unicast}

broadcast_max = {'addressingMode': 'Broadcast', 'pollTimeout': 30, 'pollInterval': 16384, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 15000, 'groupAddress': "", 'sendRequest': True}
unicast_max = {'addressingMode': 'Unicast', 'pollInterval': 16384, 'pollTimeout': 30, 'pollRetry': 10, 'serverAutoDiscovery': 0, 'sendRequest': False, 'groupAddress': None}
multicast_max = {'addressingMode': 'Multicast', 'pollTimeout': 30, 'pollInterval': 16384, 'pollRetry': 0, 'serverAutoDiscovery': 0, 'delayTime': 15000, 'groupAddress': "224.0.0.0", 'sendRequest': True}
manycast_max = {'addressingMode': 'Manycast', 'pollTimeout': 30, 'pollInterval': 16384, 'pollRetry': 1, 'serverAutoDiscovery': 0, 'delayTime': 0, 'groupAddress': "", 'sendRequest': False}

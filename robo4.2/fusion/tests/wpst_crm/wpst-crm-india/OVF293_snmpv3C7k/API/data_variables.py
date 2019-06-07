def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

lig1_ethernetsettings = {'type': 'EthernetInterconnectSettingsV3', 'enableRichTLV': True, 'interconnectType': 'Ethernet'}
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}
storage_admin = {'userName': 'Storageadmin', 'password': 'Storageadmin'}
backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}
server_admin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}
read_only = {'userName': 'ReadOnlyAdmin', 'password': 'Readonlyadmin'}


LIG1 = 'LIG_New1'
LIG2 = 'LIG_FC'


users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Storageadmin', 'password': 'Storageadmin', 'fullName': 'Storageadmin', "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'ReadOnlyAdmin', 'password': 'Readonlyadmin', 'fullName': 'Readonlyadmin', "enabled": True, "permissions": [{"roleName": "Read only", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         ]


icmap_snmp = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'}]


icmap_FC = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'}]


ethernet_networks1 = [{'name': 'net100',
                       'type': 'ethernet-networkV4',
                       'vlanId': 100,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},

                      {'name': 'eth-101',
                       'type': 'ethernet-networkV300',
                       'vlanId': 101,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},
                      ]

fc_network = [{'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'fabricType': 'FabricAttach',
               'autoLoginRedistribution': True,
               'name': 'fc1',
               'state': 'Active'}]


uplink_sets = {'us1': {'name': 'US1',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['net100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X6', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X6', 'speed': 'Auto'},
                                                  ]},

               'us2': {'name': 'US2',
                       'ethernetNetworkType': 'NA',
                       'networkType': 'FibreChannel',
                       'networkUris': ['fc1'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '5', 'port': 'X19', 'speed': 'Auto', 'enclosure': '1'},

                                                  ]}


               }


uplink_sets2 = {'us1':

                {'name': 'US_FC',
                 'ethernetNetworkType': 'NA',
                 'networkType': 'FibreChannel',
                 'networkUris': ['fc1'],
                 'primaryPort': None,
                 'nativeNetworkUri': None,
                 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '5', 'port': '3', 'speed': 'Auto', 'enclosure': '1'}]
                 }
                }

LIG_new = {
    'name': 'LIG_New1',
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'C7000',
    'interconnectMapTemplate': icmap_snmp,
    'uplinkSets': [uplink_sets['us1']],
    'stackingMode': 'Enclosure',
    'ethernetSettings': None,
    'state': 'Active',
    'telemetryConfiguration': None,
    'snmpConfiguration': None
}


LIG_FC = {
    'name': 'LIG_FC',
    'type': 'logical-interconnect-groupV4',
    'enclosureType': 'C7000',
    'interconnectMapTemplate': icmap_FC,
    'uplinkSets': [],
    'stackingMode': 'Enclosure',
    'ethernetSettings': None,
    'state': 'Active',
    'telemetryConfiguration': None,
    'snmpConfiguration': None
}

add_snmp_users_six_combinations = {'type': 'snmp-configuration',
                                   'trapDestinations': [],
                                   'snmpAccess': [],
                                   'snmpUsers': [
                                       {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                       {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                       {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},

                                   ],
                                   'readCommunity': 'public',
                                   'v3Enabled': True,
                                   'enabled': True,
                                   'description': '',
                                   'category': 'snmp-configuration',
                                   'uri': ''}

add_snmp_users_six_combinations_original = {'lig1':
                                            {

                                                'name': 'LIG_New1',
                                                'type': 'logical-interconnect-groupV4',
                                                'enclosureType': 'C7000',
                                                'interconnectMapTemplate': icmap_snmp,
                                                'uplinkSets': [uplink_sets['us1']],
                                                'stackingMode': 'Enclosure',
                                                'ethernetSettings': None,
                                                'state': 'Active',
                                                'telemetryConfiguration': None,
                                                'snmpConfiguration': {'type': 'snmp-configuration',
                                                                      'trapDestinations': [{'inform': False, 'engineId': None,
                                                                                            'trapFormat': 'SNMPv3',
                                                                                            'trapDestination': '192.168.148.49',
                                                                                            'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                            'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                            'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                            'vcmTrapCategories':['Legacy'],
                                                                                            'userName':'User1',
                                                                                            'port': '163'}],
                                                                      'snmpAccess': [],
                                                                      'snmpUsers': [
                                                                          {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                          {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                          {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},

                                                                      ],
                                                                      'readCommunity': 'public',
                                                                      'v3Enabled': True,
                                                                      'enabled': True,
                                                                      'description': '',
                                                                      'category': 'snmp-configuration',
                                                                      'uri': ''
                                                                      }
                                            }

                                            }


add_lig_fc = {'type': 'snmp-configuration',
              'trapDestinations': [{'inform': False, 'engineId': None, 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.49', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                    'enetTrapCategories': ['PortStatus', 'PortThresholds', 'Other'],
                                    'trapSeverities': ['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                    'vcmTrapCategories': ['Legacy'],
                                    'userName': 'User1',
                                    'port': '163'}],
              'snmpAccess': [],
              'snmpUsers': [
                  {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                  {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

              ],
              'readCommunity': 'public',
              'v3Enabled': True,
              'enabled': False,
              'description': '',
              'category': 'snmp-configuration',
              'uri': ''}


add_lig_fc_original = {'lig2':
                       {
                           'name': 'LIG_FC',
                           'type': 'logical-interconnect-groupV4',
                           'enclosureType': 'C7000',
                           'interconnectMapTemplate': icmap_FC,
                           'uplinkSets': [],
                           'stackingMode': 'Enclosure',
                           'ethernetSettings': None,
                           'state': 'Active',
                           'telemetryConfiguration': None,
                           'snmpConfiguration': {'type': 'snmp-configuration',
                                                 'trapDestinations': [{'inform': False, 'engineId': None, 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.49', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                       'enetTrapCategories': ['PortStatus', 'PortThresholds', 'Other'],
                                                                       'trapSeverities': ['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                       'vcmTrapCategories': ['Legacy'],
                                                                       'userName': 'User1',
                                                                       'port': '163'}],
                                                 'snmpAccess': [],
                                                 'snmpUsers': [
                                                     {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

                                                 ],
                                                 'readCommunity': 'public',
                                                 'v3Enabled': True,
                                                 'enabled': False,
                                                 'description': '',
                                                 'category': 'snmp-configuration',
                                                 'uri': ''}

                       }
                       }


enc_group_1 = {'name': 'EG_SNMP',
               # 'type': 'EnclosureGroupV7',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'enclosureCount': 1,
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_New1'},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_New1'},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_FC'},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}


enc_group = {'name': 'EG_SNMP',
             'configurationScript': None,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_New1'},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_New1'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_FC'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
             'ipRangeUris': [],
             'enclosureCount': 1,
             'ambientTemperatureMode': 'Standard'
             }
enc_group_fc = {'name': 'EG_SNMP',
                'configurationScript': None,
                'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_FC'},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
                'ipRangeUris': [],
                'enclosureCount': 1,
                'ambientTemperatureMode': 'Standard'
                }

encREAL = [{'hostname': '192.168.144.133', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG_SNMP', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]

encs = encREAL

server_profiles = [{'type': 'ServerProfileV8', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EG_SNMP', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net100', 'mac': None, 'wwpn': '', 'wwnn': ''}]
                    }]


user_proto_priv = [{'user': 'User1', 'auth': 'MD5', 'priv': 'None'},
                   {'user': 'User2', 'auth': 'SHA1', 'priv': 'None'},
                   {'user': 'User3', 'auth': 'MD5', 'priv': 'DES'},
                   {'user': 'User4', 'auth': 'MD5', 'priv': 'AES-128'},
                   {'user': 'User5', 'auth': 'SHA1', 'priv': 'DES'},
                   {'user': 'User6', 'auth': 'SHA1', 'priv': 'AES-128'}]


user_proto_priv_1 = [{'user': 'User1', 'auth': 'MD5', 'priv': 'None'},
                     {'user': 'User2', 'auth': 'SHA1', 'priv': 'None'},
                     {'user': 'User3', 'auth': 'MD5', 'priv': 'DES'}]


edit_li_exiting_snmp_users_auth_and_authpriv = {'snmpConfiguration':
                                                {
                                                    'type': 'snmp-configuration',
                                                    'readCommunity': 'public',
                                                    'systemContact': '',
                                                    'v3Enabled': True,
                                                    'snmpUsers': [
                                                        {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                        {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                        {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                        {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                        {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                        {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                    'trapDestinations': [{'inform': False, 'engineId': None,
                                                                          'trapFormat': 'SNMPv3',
                                                                          'trapDestination': '192.168.148.49',
                                                                          'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                          'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                          'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                          'vcmTrapCategories':['Legacy'],
                                                                          'userName':'User1',
                                                                          'port': '163'}],
                                                    'snmpAccess': [],
                                                    'enabled': False,
                                                    'description': None,
                                                    'category': 'snmp-configuration',
                                                    'uri': None
                                                }
                                                }

edit_li_User2 = {'snmpConfiguration': {
    'type': 'snmp-configuration',
    'readCommunity': 'public',
    'systemContact': '',
    'v3Enabled': True,
    'snmpUsers': [
        {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
        {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
        {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
        {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
        {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
        {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
    'trapDestinations': [{'inform': False, 'engineId': None,
                          'trapFormat': 'SNMPv3',
                          'trapDestination': '192.168.148.49',
                          'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                          'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                          'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                          'vcmTrapCategories':['Legacy'],
                          'userName':'User2', 'port': '163'}],

    'snmpAccess': [],
    'enabled': False,
    'description': None,
    'category': 'snmp-configuration',
    'uri': None
}
}

edit_li_User3 = {'snmpConfiguration':
                 {
                     'type': 'snmp-configuration',
                     'readCommunity': 'public',
                     'systemContact': '',
                     'v3Enabled': True,
                     'snmpUsers': [
                             {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                     'trapDestinations': [{'inform': False, 'engineId': None,
                                           'trapFormat': 'SNMPv3',
                                           'trapDestination': '192.168.148.49',
                                           'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                           'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                           'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                           'vcmTrapCategories':['Legacy'],
                                           'userName':'User3',
                                           'port': '163'}],
                     'snmpAccess': [],
                     'enabled': False,
                     'description': None,
                     'category': 'snmp-configuration',
                     'uri': None
                 }
                 }
edit_li_User3_1 = {'snmpConfiguration':
                   {
                       'type': 'snmp-configuration',
                       'readCommunity': 'public',
                       'systemContact': '',
                       'v3Enabled': True,
                       'snmpUsers': [
                               {'snmpV3UserName': 'User1', 'securityLevel': 'Auth', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                               {'snmpV3UserName': 'User2', 'securityLevel': 'Auth', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                               {'snmpV3UserName': 'User3', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                               {'snmpV3UserName': 'User4', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                               {'snmpV3UserName': 'User5', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                               {'snmpV3UserName': 'User6', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                       'trapDestinations': [{'inform': False, 'engineId': None,
                                             'trapFormat': 'SNMPv3',
                                             'trapDestination': '192.168.148.49',
                                             'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                             'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                             'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                             'vcmTrapCategories':['Legacy'],
                                             'userName':'User3',
                                             'port': '163'}],
                       'snmpAccess': [],
                       'enabled': False,
                       'description': None,
                       'category': 'snmp-configuration',
                       'uri': None
                   }
                   }

edit_li_User4 = {'snmpConfiguration':
                 {
                     'type': 'snmp-configuration',
                     'readCommunity': 'public',
                     'systemContact': '',
                     'v3Enabled': True,
                     'snmpUsers': [
                             {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                     'trapDestinations': [{'inform': False, 'engineId': None,
                                           'trapFormat': 'SNMPv3',
                                           'trapDestination': '192.168.148.49',
                                           'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                           'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                           'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                           'vcmTrapCategories':['Legacy'],
                                           'userName':'User4',
                                           'port': '163'}],
                     'snmpAccess': [],
                     'enabled': False,
                     'description': None,
                     'category': 'snmp-configuration',
                     'uri': None
                 }
                 }

edit_li_User5 = {'snmpConfiguration':
                 {
                     'type': 'snmp-configuration',
                     'readCommunity': 'public',
                     'systemContact': '',
                     'v3Enabled': True,
                     'snmpUsers': [
                             {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                     'trapDestinations': [{'inform': False, 'engineId': None,
                                           'trapFormat': 'SNMPv3',
                                           'trapDestination': '192.168.148.49',
                                           'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                           'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                           'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                           'vcmTrapCategories':['Legacy'],
                                           'userName':'User5',
                                           'port': '163'}],
                     'snmpAccess': [],
                     'enabled': False,
                     'description': None,
                     'category': 'snmp-configuration',
                     'uri': None
                 }
                 }

edit_li_User6 = {'snmpConfiguration':
                 {
                     'type': 'snmp-configuration',
                     'readCommunity': 'public',
                     'systemContact': '',
                     'v3Enabled': True,
                     'snmpUsers': [
                             {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                     'trapDestinations': [{'inform': False, 'engineId': None,
                                           'trapFormat': 'SNMPv3',
                                           'trapDestination': '192.168.148.49',
                                           'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                           'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                           'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                           'vcmTrapCategories':['Legacy'],
                                           'userName':'User6',
                                           'port': '163'}],
                     'snmpAccess': [],
                     'enabled': False,
                     'description': None,
                     'category': 'snmp-configuration',
                     'uri': None
                 }
                 }
downlink_disable = {'interconnectName': 'SGH411DFYA, interconnect 1', 'enabled': False,
                    'portName': 'X6',
                    'type': 'port',
                    }

downlink_enable = {'interconnectName': 'SGH411DFYA, interconnect 1', 'enabled': True,
                   'portName': 'X6',
                   'type': 'port',
                   }

user_proto_priv_lig = [{'user': 'User1', 'auth': 'MD5', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                       {'user': 'User2', 'auth': 'SHA1', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                       {'user': 'User3', 'auth': 'MD5', 'priv': 'DES', 'auth_pass': 'password123', 'priv_pass': 'password123'},
                       ]

user_proto_priv_lig_fc = [{'user': 'User1', 'auth': 'MD5', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                          {'user': 'User2', 'auth': 'SHA1', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                          ]

user_proto_priv_li = [{'user': 'User1', 'auth': 'MD5', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                      {'user': 'User2', 'auth': 'SHA1', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                      {'user': 'User3', 'auth': 'MD5', 'priv': 'DES', 'auth_pass': 'password123', 'priv_pass': 'password123'},
                      {'user': 'User4', 'auth': 'MD5', 'priv': 'AES-128', 'auth_pass': 'password123', 'priv_pass': 'password123'},
                      {'user': 'User5', 'auth': 'SHA1', 'priv': 'DES', 'auth_pass': 'password123', 'priv_pass': 'password123'},
                      {'user': 'User6', 'auth': 'SHA1', 'priv': 'AES-128', 'auth_pass': 'password123', 'priv_pass': 'password123'},
                      ]

# LIG Scenarios Data Variables- LIG_Scenarios_C7K
add_snmp_lig1_6_combinations = {'lig1':
                                {'name': 'LIG_New_DefaultNoAuth',
                                 'type': 'logical-interconnect-groupV4',
                                 'enclosureType': 'C7000',
                                 'interconnectMapTemplate': icmap_snmp,
                                 # 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                                 'uplinkSets': [],
                                 'stackingMode': 'Enclosure',
                                 # 'ethernetSettings':{'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                                 'ethernetSettings': None,
                                 'state': 'Active',
                                 'telemetryConfiguration': None,
                                 'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'trapDestinations': [],
                                                       'snmpAccess': ["192.168.2.0/24"],
                                                       'snmpUsers': [
                                                               {'snmpV3UserName': '1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                               {'snmpV3UserName': '2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}

                                                       ],
                                                       'readCommunity': 'public',
                                                       'v3Enabled': True,
                                                       'enabled': True,
                                                       'description': '',
                                                       'category': 'snmp-configuration',
                                                       'uri': ''}
                                 }
                                }

add_snmp_lig_Auth_MD5 = {'lig1':
                         {'name': 'LIG_New_SecAuthMD5',
                          'type': 'logical-interconnect-groupV4',
                          'enclosureType': 'C7000',
                          'interconnectMapTemplate': icmap_snmp,
                          # 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                          'uplinkSets': [],
                          'stackingMode': 'Enclosure',
                          # 'ethernetSettings':{'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': {'type': 'snmp-configuration',
                                                'trapDestinations': [],
                                                'snmpAccess': [],
                                                'snmpUsers': [

                                                        {'snmpV3UserName': '3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}

                                                ],
                                                'readCommunity': 'public',
                                                'v3Enabled': True,
                                                'enabled': True,
                                                'description': '',
                                                'category': 'snmp-configuration',
                                                'uri': ''}
                          }
                         }

add_snmp_lig_Auth_SHA1 = {'lig1':
                          {'name': 'LIG_New_SecAuthSHA1',
                           'type': 'logical-interconnect-groupV4',
                           'enclosureType': 'C7000',
                           'interconnectMapTemplate': icmap_snmp,
                           'uplinkSets': [],
                           'stackingMode': 'Enclosure',
                           'ethernetSettings': None,
                           'state': 'Active',
                           'telemetryConfiguration': None,
                           'snmpConfiguration': {'type': 'snmp-configuration',
                                                 'trapDestinations': [],
                                                 'snmpAccess': ["192.168.2.0/24"],
                                                 'snmpUsers': [
                                                         {'snmpV3UserName': '3', 'securityLevel': 'Auth', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                 ],
                                                 'readCommunity': 'public',
                                                 'v3Enabled': True,
                                                 'enabled': True,
                                                 'description': '',
                                                 'category': 'snmp-configuration',
                                                 'uri': ''}
                           }
                          }

add_snmp_lig_Auth_Priv_MD5_DES = {'lig1':
                                  {'name': 'LIG_New_AuthPrivMD5_DES',
                                   'type': 'logical-interconnect-groupV4',
                                   'enclosureType': 'C7000',
                                   'interconnectMapTemplate': icmap_snmp,
                                   'uplinkSets': [],
                                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [],
                                                         'snmpAccess': ["192.168.2.0/24"],
                                                         'snmpUsers': [{'snmpV3UserName': '5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                                   }
                                  }

add_snmp_lig_Auth_Priv_MD5_AES128 = {'lig1':
                                     {'name': 'LIG_New_AuthPrivMD5_AES128',
                                      'type': 'logical-interconnect-groupV300',
                                      'enclosureType': 'C7000',
                                      'interconnectMapTemplate': icmap_snmp,
                                      # 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                                      'uplinkSets': [],
                                      'stackingMode': 'Enclosure',
                                      # 'ethernetSettings':{'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                                      'ethernetSettings': None,
                                      'state': 'Active',
                                      'telemetryConfiguration': None,
                                      'snmpConfiguration': {'type': 'snmp-configuration',
                                                            'trapDestinations': [],
                                                            'snmpAccess': ["192.168.2.0/24"],
                                                            'snmpUsers': [
                                                                    {'snmpV3UserName': '6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                            ],
                                                            'readCommunity': 'public',
                                                            'v3Enabled': True,
                                                            'enabled': True,
                                                            'description': '',
                                                            'category': 'snmp-configuration',
                                                            'uri': ''}
                                      }
                                     }

add_snmp_lig_Auth_Priv_SHA1_DES = {'lig1':
                                   {'name': 'LIG_New_AuthPrivSH1_AES_DES',
                                    'type': 'logical-interconnect-groupV4',
                                    'enclosureType': 'C7000',
                                    'interconnectMapTemplate': icmap_snmp,
                                    'uplinkSets': [],
                                    'stackingMode': 'Enclosure',
                                    'ethernetSettings': None,
                                    'state': 'Active',
                                    'telemetryConfiguration': None,
                                    'snmpConfiguration': {'type': 'snmp-configuration',
                                                          'trapDestinations': [],
                                                          'snmpAccess': ["192.168.2.0/24"],
                                                          'snmpUsers': [{'snmpV3UserName': '10', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'}],
                                                          'readCommunity': 'public',
                                                          'v3Enabled': True,
                                                          'enabled': True,
                                                          'description': '',
                                                          'category': 'snmp-configuration',
                                                          'uri': ''}
                                    }
                                   }

add_snmp_lig_Auth_Priv_SHA1_AES128 = {'lig1':
                                      {'name': 'LIG_New_AuthPrivSH1_AES128',
                                       'type': 'logical-interconnect-groupV4',
                                       'enclosureType': 'C7000',
                                       'interconnectMapTemplate': icmap_snmp,
                                       'uplinkSets': [],
                                       'stackingMode': 'Enclosure',
                                       'ethernetSettings': None,
                                       'state': 'Active',
                                       'telemetryConfiguration': None,
                                       'snmpConfiguration': {'type': 'snmp-configuration',
                                                             'trapDestinations': [],
                                                             'snmpAccess': ["192.168.2.0/24"],
                                                             'snmpUsers': [{'snmpV3UserName': 'User1', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                             'readCommunity': 'public',
                                                             'v3Enabled': True,
                                                             'enabled': True,
                                                             'description': '',
                                                             'category': 'snmp-configuration',
                                                             'uri': ''}
                                       }}

edit_snmp_lig_trap_snmpv3_disabled = {'lig1':
                                      {'name': 'LIG_New_AuthPrivSH1_AES128',
                                       'type': 'logical-interconnect-groupV4',
                                       'enclosureType': 'C7000',
                                       'interconnectMapTemplate': icmap_snmp,
                                       'uplinkSets': [],
                                       'stackingMode': 'Enclosure',
                                       'ethernetSettings': None,
                                       'state': 'Active',
                                       'telemetryConfiguration': None,
                                       'snmpConfiguration': {'type': 'snmp-configuration',
                                                             'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                                   'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                                   'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                                   'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                                             'snmpAccess': ["192.168.2.0/24"],
                                                             'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                             'readCommunity': 'public',
                                                             'v3Enabled': False,
                                                             'enabled': True,
                                                             'description': '',
                                                             'category': 'snmp-configuration',
                                                             'uri': ''}
                                       }}

edit_snmp_lig_trap_destinations_no_users = {'lig1':
                                            {'name': 'LIG_New_AuthPrivSH1_AES128',
                                             'type': 'logical-interconnect-groupV4',
                                             'enclosureType': 'C7000',
                                             'interconnectMapTemplate': icmap_snmp,
                                             'uplinkSets': [],
                                             'stackingMode': 'Enclosure',
                                             'ethernetSettings': None,
                                             'state': 'Active',
                                             'telemetryConfiguration': None,
                                             'snmpConfiguration': {'type': 'snmp-configuration',
                                                                   'trapDestinations': [],
                                                                   'snmpAccess': ["192.168.2.0/24"],
                                                                   'snmpUsers': [],
                                                                   'readCommunity': 'public',
                                                                   'v3Enabled': True,
                                                                   'enabled': True,
                                                                   'description': '',
                                                                   'category': 'snmp-configuration',
                                                                   'uri': ''}
                                             }}

edit_snmp_lig_trap_destinations_without_users = {'lig1':
                                                 {'name': 'LIG_New_AuthPrivSH1_AES128',
                                                  'type': 'logical-interconnect-groupV4',
                                                  'enclosureType': 'C7000',
                                                  'interconnectMapTemplate': icmap_snmp,
                                                  'uplinkSets': [],
                                                  'stackingMode': 'Enclosure',
                                                  'ethernetSettings': None,
                                                  'state': 'Active',
                                                  'telemetryConfiguration': None,
                                                  'snmpConfiguration': {'type': 'snmp-configuration',
                                                                        'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                                              'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                                              'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                                              'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                                                        'snmpAccess': ["192.168.2.0/24"],
                                                                        'snmpUsers': [],
                                                                        'readCommunity': 'public',
                                                                        'v3Enabled': True,
                                                                        'enabled': True,
                                                                        'description': '',
                                                                        'category': 'snmp-configuration',
                                                                        'uri': ''}
                                                  }}

edit_snmp_lig_trap_destinations_type_Trap = {'lig1':
                                             {'name': 'LIG_New_AuthPrivSH1_AES128',
                                              'type': 'logical-interconnect-groupV4',
                                              'enclosureType': 'C7000',
                                              'interconnectMapTemplate': icmap_snmp,
                                              # 'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                                              'uplinkSets': [],
                                              'stackingMode': 'Enclosure',
                                              # 'ethernetSettings':{'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                                              'ethernetSettings': None,
                                              'state': 'Active',
                                              'telemetryConfiguration': None,
                                              'snmpConfiguration': {'type': 'snmp-configuration',
                                                                    'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                                          'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                                          'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                                          'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                                                    'snmpAccess': ["192.168.2.0/24"],

                                                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],

                                                                    'readCommunity': 'public',
                                                                    'v3Enabled': True,
                                                                    'enabled': True,
                                                                    'description': '',
                                                                    'category': 'snmp-configuration',
                                                                    'uri': ''}
                                              }}

edit_snmp_lig_trap_destinations_type_Inform_wo_engineID = {'lig1':
                                                           {'name': 'LIG_New_AuthPrivSH1_AES128',
                                                            'type': 'logical-interconnect-groupV4',
                                                            'enclosureType': 'C7000',
                                                            'interconnectMapTemplate': icmap_snmp,
                                                            'uplinkSets': [],
                                                            'stackingMode': 'Enclosure',
                                                            'ethernetSettings': None,
                                                            'state': 'Active',
                                                            'telemetryConfiguration': None,
                                                            'snmpConfiguration': {'type': 'snmp-configuration',
                                                                                  'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                                                        'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                                                        'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                                                        'userName':'User1', 'inform':True, 'engineId':'', 'communityString':'', 'port':'162'}],
                                                                                  'snmpAccess': ["192.168.2.0/24"],
                                                                                  'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                                                  'readCommunity': 'public',
                                                                                  'v3Enabled': True,
                                                                                  'enabled': True,
                                                                                  'description': '',
                                                                                  'category': 'snmp-configuration',
                                                                                  'uri': ''}
                                                            }}

edit_snmp_lig_trap_dest_add_non_def_port = {'lig1':
                                            {'name': 'LIG_New_DefaultNoAuth',
                                             'type': 'logical-interconnect-groupV300',
                                             'enclosureType': 'C7000',
                                             'interconnectMapTemplate': icmap_snmp,
                                             'uplinkSets': [],
                                             'stackingMode': 'Enclosure',
                                             'ethernetSettings': None,
                                             'state': 'Active',
                                             'telemetryConfiguration': None,
                                             'snmpConfiguration': {'type': 'snmp-configuration',

                                                                   'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                                         'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                                         'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                                         'userName':'Test3', 'inform':False, 'communityString':'', 'port':'190'}],
                                                                   'snmpAccess': ["192.168.2.0/24"],
                                                                   'snmpUsers': [{'snmpV3UserName': 'Test3', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                                 {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],

                                                                   'readCommunity': 'public',
                                                                   'v3Enabled': True,
                                                                   'enabled': True,
                                                                   'description': '',
                                                                   'category': 'snmp-configuration',
                                                                   'uri': ''}
                                             }}

edit_snmp_traps = {'lig1':
                   {'name': 'LIG_MAX_Traps',
                    'type': 'logical-interconnect-groupV4',
                    'enclosureType': 'C7000',
                    'interconnectMapTemplate': icmap_snmp,
                    'uplinkSets': [],
                    'stackingMode': 'Enclosure',
                    'ethernetSettings': None,
                    'state': 'Active',
                    'telemetryConfiguration': None,
                    'snmpConfiguration': {'type': 'snmp-configuration',
                                          'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.72', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test2', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.76', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.75', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.77', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '10.10.3.78', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'}],

                                          'snmpAccess': ["192.168.3.0/24"],
                                          'snmpUsers': [{'snmpV3UserName': 'Test6', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                        {'snmpV3UserName': 'Test5', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                        {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                        {'snmpV3UserName': 'Test3', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                        {'snmpV3UserName': 'Test2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                        {'snmpV3UserName': 'Test1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                          'readCommunity': 'public',
                                          'v3Enabled': True,
                                          'enabled': True,
                                          'description': '',
                                          'category': 'snmp-configuration',
                                          'uri': ''}
                    }}

edit_lig_snmp_trap_Address = {'lig1':
                              {'name': 'LIG_New_DefaultNoAuth',
                               'type': 'logical-interconnect-groupV4',
                               'enclosureType': 'C7000',
                               'interconnectMapTemplate': icmap_snmp,
                               'uplinkSets': [],
                               'stackingMode': 'Enclosure',
                               'ethernetSettings': None,
                               'state': 'Active',
                               'telemetryConfiguration': None,
                               'snmpConfiguration': {'type': 'snmp-configuration',
                                                     'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'162'}],
                                                     'snmpAccess': ['192.168.3.0/24'],
                                                     'snmpUsers': [{'snmpV3UserName': 'Test4', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                   ],

                                                     'readCommunity': 'public',
                                                     'v3Enabled': True,
                                                     'enabled': True,
                                                     'description': '',
                                                     'category': 'snmp-configuration',
                                                     'uri': ''}
                               }}

edit_lig_snmp_trap_Inform = {'lig1':
                             {'name': 'LIG_New_DefaultNoAuth',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureType': 'C7000',
                              'interconnectMapTemplate': icmap_snmp,
                              'uplinkSets': [],
                              'stackingMode': 'Enclosure',
                              'ethernetSettings': None,
                              'state': 'Active',
                              'telemetryConfiguration': None,
                              'snmpConfiguration': {'type': 'snmp-configuration',
                                                    'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'162'}],
                                                    'snmpAccess': ['192.168.3.0/24'],
                                                    'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                                    'readCommunity': 'public',
                                                    'v3Enabled': True,
                                                    'enabled': True,
                                                    'description': '',
                                                    'category': 'snmp-configuration',
                                                    'uri': ''}
                              }}

edit_lig_snmp_trap_Port = {'lig1':
                           {'name': 'LIG_New_DefaultNoAuth',
                            'type': 'logical-interconnect-groupV4',
                            'enclosureType': 'C7000',
                            'interconnectMapTemplate': icmap_snmp,
                            'uplinkSets': [],
                            'stackingMode': 'Enclosure',
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                                                  'snmpAccess': ['192.168.3.0/24'],
                                                  'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                                  'readCommunity': 'public',
                                                  'v3Enabled': True,
                                                  'enabled': True,
                                                  'description': '',
                                                  'category': 'snmp-configuration',
                                                  'uri': ''}
                            }}

edit_lig_snmp_user_name = {'lig1':
                           {'name': 'LIG_New_DefaultNoAuth',
                            'type': 'logical-interconnect-groupV4',
                            'enclosureType': 'C7000',
                            'interconnectMapTemplate': icmap_snmp,
                            'uplinkSets': [],
                            'stackingMode': 'Enclosure',
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test5', 'inform':False, 'communityString':'', 'port':'180'}],
                                                  'snmpAccess': ['192.168.3.0/24'],
                                                  'snmpUsers': [{'snmpV3UserName': 'Test5', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                                  'readCommunity': 'public',
                                                  'v3Enabled': True,
                                                  'enabled': True,
                                                  'description': '',
                                                  'category': 'snmp-configuration',
                                                  'uri': ''}
                            }}

edit_lig_snmp_trap_type_inform = {'lig1':
                                  {'name': 'LIG_New_DefaultNoAuth',
                                   'type': 'logical-interconnect-groupV4',
                                   'enclosureType': 'C7000',
                                   'interconnectMapTemplate': icmap_snmp,
                                   'uplinkSets': [],
                                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'180'},
                                                                              {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                                                         'snmpAccess': ['192.168.3.0/24'],
                                                         'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                                   }}

edit_lig_snmp_security_level = {'lig1':
                                {'name': 'LIG_New_DefaultNoAuth',
                                 'type': 'logical-interconnect-groupV4',
                                 'enclosureType': 'C7000',
                                 'interconnectMapTemplate': icmap_snmp,
                                 'uplinkSets': [],
                                 'stackingMode': 'Enclosure',
                                 'ethernetSettings': None,
                                 'state': 'Active',
                                 'telemetryConfiguration': None,
                                 'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'180'},
                                                                            {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                                                       'snmpAccess': ['192.168.3.0/24'],
                                                       'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                       'readCommunity': 'public',
                                                       'v3Enabled': True,
                                                       'enabled': True,
                                                       'description': '',
                                                       'category': 'snmp-configuration',
                                                       'uri': ''}
                                 }}

edit_lig_snmp_invalid_port = {'lig1':
                              {'name': 'LIG_New_DefaultNoAuth',
                               'type': 'logical-interconnect-groupV4',
                               'enclosureType': 'C7000',
                               'interconnectMapTemplate': icmap_snmp,
                               'uplinkSets': [],
                               'stackingMode': 'Enclosure',
                               'ethernetSettings': None,
                               'state': 'Active',
                               'telemetryConfiguration': None,
                               'snmpConfiguration': {'type': 'snmp-configuration',
                                                     'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'abc'},
                                                                          {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                                                     'snmpAccess': ['192.168.3.0/24'],
                                                     'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                     'readCommunity': 'public',
                                                     'v3Enabled': True,
                                                     'enabled': True,
                                                     'description': '',
                                                     'category': 'snmp-configuration',
                                                     'uri': ''}
                               }}

edit_lig_snmp_invalid_engineID = {'lig1':
                                  {'name': 'LIG_New_DefaultNoAuth',
                                   'type': 'logical-interconnect-groupV300',
                                   'enclosureType': 'C7000',
                                   'interconnectMapTemplate': icmap_snmp,
                                   'uplinkSets': [],
                                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [{'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'12345', 'communityString':'', 'port':'180'}],
                                                         'snmpAccess': ['192.168.3.0/24'],
                                                         'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                                   }}

add_snmp_traps = {'lig1':
                  {'name': 'LIG_MAX_Traps',
                   'type': 'logical-interconnect-groupV4',
                   'enclosureType': 'C7000',
                   'interconnectMapTemplate': icmap_snmp,
                   'uplinkSets': [],
                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                                              {'trapDestination': '10.10.3.72', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test2', 'inform':False, 'communityString':'', 'port':'162'},
                                                                              {'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                                              {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                                              {'trapDestination': '10.10.3.76', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                                                              {'trapDestination': '10.10.3.75', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'}],
                                                         'snmpAccess': ["192.168.2.0/24"],
                                                         'snmpUsers': [{'snmpV3UserName': 'Test6', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                       {'snmpV3UserName': 'Test5', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                       {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                       {'snmpV3UserName': 'Test3', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                       {'snmpV3UserName': 'Test2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                       {'snmpV3UserName': 'Test1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                   }}

# LIG Eror Scenarios
edit_snmp_user_duplicate_error = {'lig1':
                                  {'name': 'LIG_SecLevel_2',
                                   'type': 'logical-interconnect-groupV4',
                                   'enclosureType': 'C7000',
                                   'interconnectMapTemplate': icmap_snmp,
                                   'uplinkSets': [],
                                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [],
                                                         'snmpAccess': ["192.168.2.0/24"],
                                                         'snmpUsers': [
                                                             {'snmpV3UserName': 'One', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                             {'snmpV3UserName': 'One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                         ],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                                   }
                                  }

Invalidvalues_UserName = {'lig1':
                          {'name': 'LIG_SecLevel_4',
                           'type': 'logical-interconnect-groupV4',
                           'enclosureType': 'C7000',
                           'interconnectMapTemplate': icmap_snmp,
                           'uplinkSets': [],
                           'stackingMode': 'Enclosure',
                           'ethernetSettings': None,
                           'state': 'Active',
                           'telemetryConfiguration': None,
                           'snmpConfiguration': {'type': 'snmp-configuration',
                                                 'trapDestinations': [],
                                                 'snmpAccess': ["192.168.2.0/24"],
                                                 'snmpUsers': [{'snmpV3UserName': 'One_1212-nfn1213231323434434_****((((3$$$%%%', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, ],
                                                 'readCommunity': 'public',
                                                 'v3Enabled': True,
                                                 'enabled': True,
                                                 'description': '',
                                                 'category': 'snmp-configuration',
                                                 'uri': ''}
                           }
                          }

Invalidvalues_AuthPassPhrase = {'lig1':
                                {'name': 'LIG_SecLevel_6',
                                 'type': 'logical-interconnect-groupV4',
                                 'enclosureType': 'C7000',
                                 'interconnectMapTemplate': icmap_snmp,
                                 'uplinkSets': [],
                                 'stackingMode': 'Enclosure',
                                 'ethernetSettings': None,
                                 'state': 'Active',
                                 'telemetryConfiguration': None,
                                 'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'trapDestinations': [],
                                                       'snmpAccess': ["192.168.2.0/24"],
                                                       'snmpUsers': [
                                                           {'snmpV3UserName': 'Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                       ],
                                                       'readCommunity': 'public',
                                                       'v3Enabled': True,
                                                       'enabled': True,
                                                       'description': '',
                                                       'category': 'snmp-configuration',
                                                       'uri': ''}
                                 }
                                }

Invalidvalues_Auth_Priv_Pass_Phrase = {'lig1':
                                       {'name': 'LIG_SecLevel_7',
                                        'type': 'logical-interconnect-groupV4',
                                        'enclosureType': 'C7000',
                                        'interconnectMapTemplate': icmap_snmp,
                                        'uplinkSets': [],
                                        'stackingMode': 'Enclosure',
                                        'ethernetSettings': None,
                                        'state': 'Active',
                                        'telemetryConfiguration': None,
                                        'snmpConfiguration': {'type': 'snmp-configuration',
                                                              'trapDestinations': [],
                                                              'snmpAccess': ["192.168.2.0/24"],
                                                              'snmpUsers': [{'snmpV3UserName': '5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '@'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}],
                                                              'readCommunity': 'public',
                                                              'v3Enabled': True,
                                                              'enabled': True,
                                                              'description': '',
                                                              'category': 'snmp-configuration',
                                                              'uri': ''}
                                        }
                                       }

Mandatory_Attribute_Check_Name = {'lig1':
                                  {'name': 'LIG_SecLevel_7',
                                   'type': 'logical-interconnect-groupV4',
                                   'enclosureType': 'C7000',
                                   'interconnectMapTemplate': icmap_snmp,
                                   'uplinkSets': [],
                                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [],
                                                         'snmpAccess': ["192.168.2.0/24"],
                                                         'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, ],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                                   }
                                  }

Mandatory_Attribute_Check_Authlgo = {'lig1':
                                     {'name': 'LIG_SecLevel_7',
                                      'type': 'logical-interconnect-groupV4',
                                      'enclosureType': 'C7000',
                                      'interconnectMapTemplate': icmap_snmp,
                                      'uplinkSets': [],
                                      'stackingMode': 'Enclosure',
                                      'ethernetSettings': None,
                                      'state': 'Active',
                                      'telemetryConfiguration': None,
                                      'snmpConfiguration': {'type': 'snmp-configuration',
                                                            'trapDestinations': [],
                                                            'snmpAccess': ["192.168.2.0/24"],
                                                            'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}, ],
                                                            'readCommunity': 'public',
                                                            'v3Enabled': True,
                                                            'enabled': True,
                                                            'description': '',
                                                            'category': 'snmp-configuration',
                                                            'uri': ''}
                                      }
                                     }

Mandatory_Attribute_Check_AuthPassPhrase = {'lig1':
                                            {'name': 'LIG_SecLevel_7',
                                             'type': 'logical-interconnect-groupV4',
                                             'enclosureType': 'C7000',
                                             'interconnectMapTemplate': icmap_snmp,
                                             'uplinkSets': [],
                                             'stackingMode': 'Enclosure',
                                             'ethernetSettings': None,
                                             'state': 'Active',
                                             'telemetryConfiguration': None,
                                             'snmpConfiguration': {'type': 'snmp-configuration',
                                                                   'trapDestinations': [],
                                                                   'snmpAccess': ["192.168.2.0/24"],
                                                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '$'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}, ],
                                                                   'readCommunity': 'public',
                                                                   'v3Enabled': True,
                                                                   'enabled': True,
                                                                   'description': '',
                                                                   'category': 'snmp-configuration',
                                                                   'uri': ''}
                                             }
                                            }

Mandatory_Attribute_Check_Auth_Priv_PassPhrase = {'lig1':
                                                  {'name': 'LIG_SecLevel_7',
                                                   'type': 'logical-interconnect-groupV4',
                                                   'enclosureType': 'C7000',
                                                   'interconnectMapTemplate': icmap_snmp,
                                                   'uplinkSets': [],
                                                   'stackingMode': 'Enclosure',
                                                   'ethernetSettings': None,
                                                   'state': 'Active',
                                                   'telemetryConfiguration': None,
                                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                                         'trapDestinations': [],
                                                                         'snmpAccess': ["192.168.2.0/24"],
                                                                         'snmpUsers': [{'snmpV3UserName': ' ', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}],
                                                                         'readCommunity': 'public',
                                                                         'v3Enabled': True,
                                                                         'enabled': True,
                                                                         'description': '',
                                                                         'category': 'snmp-configuration',
                                                                         'uri': ''}
                                                   }
                                                  }

Password_Length_Check = {'lig1':
                         {'name': 'LIG_SecLevel_7',
                          'type': 'logical-interconnect-groupV4',
                          'enclosureType': 'C7000',
                          'interconnectMapTemplate': icmap_snmp,
                          'uplinkSets': [],
                          'stackingMode': 'Enclosure',
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': {'type': 'snmp-configuration',
                                                'trapDestinations': [],
                                                'snmpAccess': ["192.168.2.0/24"],
                                                'snmpUsers': [{'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}, ],
                                                'readCommunity': 'public',
                                                'v3Enabled': True,
                                                'enabled': True,
                                                'description': '',
                                                'category': 'snmp-configuration',
                                                'uri': ''}
                          }
                         }

Maximum_No_Of_Users = {'lig1':
                       {'name': 'LIG_SecLevel_8',
                        'type': 'logical-interconnect-groupV4',
                        'enclosureType': 'C7000',
                        'interconnectMapTemplate': icmap_snmp,
                        'uplinkSets': [],
                        'stackingMode': 'Enclosure',
                        'ethernetSettings': None,
                        'state': 'Active',
                        'telemetryConfiguration': None,
                        'snmpConfiguration': {'type': 'snmp-configuration',
                                              'trapDestinations': [],
                                              'snmpAccess': ["192.168.2.0/24"],
                                              'snmpUsers': [
                                                  {'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                  {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                              ],
                                              'readCommunity': 'public',
                                              'v3Enabled': True,
                                              'enabled': True,
                                              'description': '',
                                              'category': 'snmp-configuration',
                                              'uri': ''}
                        }
                       }

Network_Admin_Users = {'lig1':
                       {'name': 'LIG_Network_Admin1',
                        'type': 'logical-interconnect-groupV4',
                        'enclosureType': 'C7000',
                        'interconnectMapTemplate': icmap_snmp,
                        'uplinkSets': [],
                        'stackingMode': 'Enclosure',
                        'ethernetSettings': None,
                        'state': 'Active',
                        'telemetryConfiguration': None,
                        'snmpConfiguration': {'type': 'snmp-configuration',
                                              'trapDestinations': [],
                                              'snmpAccess': ["192.168.2.0/24"],
                                              'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                            {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                            {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}, ],
                                              'readCommunity': 'public',
                                              'v3Enabled': True,
                                              'enabled': True,
                                              'description': '',
                                              'category': 'snmp-configuration',
                                              'uri': ''}
                        }
                       }

Server_Admin_Users = {'lig1':
                      {'name': 'LIG_Server_Admin1',
                       'type': 'logical-interconnect-groupV4',
                       'enclosureType': 'C7000',
                       'interconnectMapTemplate': icmap_snmp,
                       'uplinkSets': [],
                       'stackingMode': 'Enclosure',
                       'ethernetSettings': None,
                       'state': 'Active',
                       'telemetryConfiguration': None,
                       'snmpConfiguration': {'type': 'snmp-configuration',
                                             'trapDestinations': [],
                                             'snmpAccess': ["192.168.2.0/24"],
                                             'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, ],
                                             'readCommunity': 'public',
                                             'v3Enabled': True,
                                             'enabled': True,
                                             'description': '',
                                             'category': 'snmp-configuration',
                                             'uri': ''}
                       }
                      }

# Error messages with error codes

error_no_users = {'message': 'The user User1 specified for the SNMPv3 trap destination 10.10.3.71 does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_engine_id_missing = {'message': 'An engine ID is required for the SNMPv3 trap destination 10.10.3.71 for inform.', 'errorCode': 'CRM_SNMP_CONFIGURATION_ENGINE_ID_MISSING'}
error_missing_Parameter = {'message': 'Invalid JSON data type.', 'errorCode': 'INVALID_JSON_DATA_TYPE'}
error_invalid_engine_id = {'message': 'The engine ID for SNMPv3 trap destination 10.10.3.74 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_ENGINEID'}
error_lig = {'message': 'The user name Test4 for the SNMPv3 configuration already exists.', 'errorCode': 'CRM_SNMP_CONFIGURATION_DUPLICATE_USER_NAME'}
error_invalid_user = {'message': 'The user name One_1212-nfn1213231323434434_****((((3$$$%%% for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_invalid_Auth_password = {'message': 'The authentication password for SNMPv3 user User1 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_AUTH_PWD_INVALID'}
error_invalid_Priv_password = {'message': 'The privacy password for SNMPv3 user User5 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_PRIV_PWD_INVALID'}
error_Mandatory_Attribute_Check = {'message': 'The user name for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_Mandatory_Attribute_Check1 = {'message': 'The user name for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_Mandatory_Attribute_Check = {'message': 'The user name for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_Mandatory_Attribute_Check2 = {'message': 'The user name  for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_Mandatory_Attribute_Check3 = {'message': 'The user name  for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_Mandatory_Attribute_Check4 = {'message': 'The user name   for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_Maximum_No_of_users = {'message': 'There can be no more than 6 SNMPv3 users.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX'}
error_server_admin = {'errorCode': 'ACTION_FORBIDDEN_BY_ROLE'}
error_missing_credential = {'message': 'The credential type MD5 is needed but not present.', 'errorCode': 'CRM_MISSING_CREDENTIAL_KEY'}
error_credential_operation_failed = {'message': 'Add Snmpv3 user operation failed.', 'errorCode': 'CRM_ADD_USER_CREDENTIAL_OPERATION_FAILED'}
error_no_users = {'message': 'The user User1 specified for the SNMPv3 trap destination 10.10.3.71 does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_unique_trap_ip = {'message': 'The trap destination 192.168.148.49 already exists.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_DUPLICATE'}
error_engine_id_for_inform = {'message': 'The SNMPv3 trap destination has an engine ID and the notification type is trap.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_SHOULD_NOT_HAVE_ENGINEID'}
error_max_traps = {'message': 'The SNMP trap destinations cannot be added because the maximum number of 6 trap destinations has been exceeded.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_EXCEEDS_MAX'}
error_max_users = {'message': 'There can be no more than 6 SNMPv3 users.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX'}
error_trap_with_non_existing_users = {'message': 'The user User7 specified for the SNMPv3 trap destination does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_invalid_trap_ip = {'message': 'Snmp configuration contains a trap destination that has an invalid IP address: 192', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_IP_INVALID'}
error_invalid_port = {'message': 'The port number for trap destination is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_PORTNO'}


# Edit LIG Scenarios
snmp_add_lig_edit_user = {'lig1':
                          {'name': 'LIG7',
                           'type': 'logical-interconnect-groupV4',
                           'enclosureType': 'C7000',
                           'interconnectMapTemplate': icmap_snmp,
                           'uplinkSets': [],
                           'stackingMode': 'Enclosure',
                           'ethernetSettings': None,
                           'state': 'Active',
                           'telemetryConfiguration': None,
                           'snmpConfiguration': {'type': 'snmp-configuration',
                                                 'trapDestinations': [],
                                                 'snmpAccess': ["192.168.2.0/24"],
                                                 'snmpUsers': [
                                                     {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'Auth_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'Auth_Priv_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                     {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                 ],
                                                 'readCommunity': 'public',
                                                 'v3Enabled': True,
                                                 'enabled': True,
                                                 'description': '',
                                                 'category': 'snmp-configuration',
                                                 'uri': ''}
                           }
                          }

snmp_edit_lig_users = {'lig1':
                       {'name': 'LIG7',
                        'type': 'logical-interconnect-groupV4',
                        'enclosureType': 'C7000',
                        'interconnectMapTemplate': icmap_snmp,
                        'uplinkSets': [],
                        'stackingMode': 'Enclosure',
                        'ethernetSettings': None,
                        'state': 'Active',
                        'telemetryConfiguration': None,
                        'snmpConfiguration': {'type': 'snmp-configuration',
                                              'trapDestinations': [],
                                              'snmpAccess': ["192.168.2.0/24"],
                                              'snmpUsers': [
                                                  {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'Auth_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'Auth_Priv_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
                                              ],
                                              'readCommunity': 'public',
                                              'v3Enabled': True,
                                              'enabled': True,
                                              'description': '',
                                              'category': 'snmp-configuration',
                                              'uri': ''}
                        }
                       }

snmp_edit_lig_users_AuthtoAuthPriv = {'lig1':
                                      {'name': 'LIG7',
                                       'type': 'logical-interconnect-groupV4',
                                       'enclosureType': 'C7000',
                                       'interconnectMapTemplate': icmap_snmp,
                                       'uplinkSets': [],
                                       'stackingMode': 'Enclosure',
                                       'ethernetSettings': None,
                                       'state': 'Active',
                                       'telemetryConfiguration': None,
                                       'snmpConfiguration': {'type': 'snmp-configuration',
                                                             'trapDestinations': [],
                                                             'snmpAccess': ["192.168.2.0/24"],
                                                             'snmpUsers': [
                                                                 {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                 {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'Auth_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                             ],
                                                             'readCommunity': 'public',
                                                             'v3Enabled': True,
                                                             'enabled': True,
                                                             'description': '',
                                                             'category': 'snmp-configuration',
                                                             'uri': ''}
                                       }
                                      }

snmp_edit_lig_users_AuthPrivtoNone = {'lig1':
                                      {'name': 'LIG7',
                                       'type': 'logical-interconnect-groupV4',
                                       'enclosureType': 'C7000',
                                       'interconnectMapTemplate': icmap_snmp,
                                       'uplinkSets': [],
                                       'stackingMode': 'Enclosure',
                                       'ethernetSettings': None,
                                       'state': 'Active',
                                       'telemetryConfiguration': None,
                                       'snmpConfiguration': {'type': 'snmp-configuration',
                                                             'trapDestinations': [],
                                                             'snmpAccess': ["192.168.2.0/24"],
                                                             'snmpUsers': [
                                                                 {'snmpV3UserName': 'Auth_Three', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                 {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                                                 {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                 {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                             ],
                                                             'readCommunity': 'public',
                                                             'v3Enabled': True,
                                                             'enabled': True,
                                                             'description': '',
                                                             'category': 'snmp-configuration',
                                                             'uri': ''}
                                       }
                                      }

snmp_edit_lig_users_AuthtoNone = {'lig1':
                                  {'name': 'LIG7',
                                   'type': 'logical-interconnect-groupV4',
                                   'enclosureType': 'C7000',
                                   'interconnectMapTemplate': icmap_snmp,
                                   'uplinkSets': [],
                                   'stackingMode': 'Enclosure',
                                   'ethernetSettings': None,
                                   'state': 'Active',
                                   'telemetryConfiguration': None,
                                   'snmpConfiguration': {'type': 'snmp-configuration',
                                                         'trapDestinations': [],
                                                         'snmpAccess': ["192.168.2.0/24"],
                                                         'snmpUsers': [
                                                             {'snmpV3UserName': 'Auth_Three', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                             {'snmpV3UserName': 'Auth_One', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                             {'snmpV3UserName': 'Auth_Two', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                             {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                         ],
                                                         'readCommunity': 'public',
                                                         'v3Enabled': True,
                                                         'enabled': True,
                                                         'description': '',
                                                         'category': 'snmp-configuration',
                                                         'uri': ''}
                                   }
                                  }

snmp_edit_lig_users_invalid_Pass_Phrase = {'lig1':
                                           {'name': 'LIG7',
                                            'type': 'logical-interconnect-groupV4',
                                            'enclosureType': 'C7000',
                                            'interconnectMapTemplate': icmap_snmp,
                                            'uplinkSets': [],
                                            'stackingMode': 'Enclosure',
                                            'ethernetSettings': None,
                                            'state': 'Active',
                                            'telemetryConfiguration': None,
                                            'snmpConfiguration': {'type': 'snmp-configuration',
                                                                  'trapDestinations': [],
                                                                  'snmpAccess': ["192.168.2.0/24"],
                                                                  'snmpUsers': [
                                                                      {'snmpV3UserName': 'Auth_Three', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                      {'snmpV3UserName': 'Auth_One', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                      {'snmpV3UserName': 'Auth_Two', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                      {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '_'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '12@12345678912456789123456789123456789123456789'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                                  ],
                                                                  'readCommunity': 'public',
                                                                  'v3Enabled': True,
                                                                  'enabled': True,
                                                                  'description': '',
                                                                  'category': 'snmp-configuration',
                                                                  'uri': ''}
                                            }
                                           }

snmp_edit_lig_users_Authentication_Algorithm_empty = {'lig1':
                                                      {'name': 'LIG7',
                                                       'type': 'logical-interconnect-groupV4',
                                                       'enclosureType': 'C7000',
                                                       'interconnectMapTemplate': icmap_snmp,
                                                       'uplinkSets': [],
                                                       'stackingMode': 'Enclosure',
                                                       'ethernetSettings': None,
                                                       'state': 'Active',
                                                       'telemetryConfiguration': None,
                                                       'snmpConfiguration': {'type': 'snmp-configuration',
                                                                             'trapDestinations': [],
                                                                             'snmpAccess': ["192.168.2.0/24"],
                                                                             'snmpUsers': [
                                                                                 {'snmpV3UserName': 'Auth_Three', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                                 {'snmpV3UserName': 'Auth_One', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                                 {'snmpV3UserName': ' ', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '1'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                                 {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@12345678912456789123456789123456789123456789'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                                                             ],
                                                                             'readCommunity': 'public',
                                                                             'v3Enabled': True,
                                                                             'enabled': True,
                                                                             'description': '',
                                                                             'category': 'snmp-configuration',
                                                                             'uri': ''}
                                                       }
                                                      }

# Edit LI Scenarios
edit_li_exiting_snmp_users_auth_to_authpriv = {'snmpConfiguration':
                                               {
                                                   'type': 'snmp-configuration',
                                                   'readCommunity': 'public',
                                                   'systemContact': '',
                                                   'v3Enabled': True,
                                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                 {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                 {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                   'trapDestinations': [{'inform': False,
                                                                         'engineId': None,
                                                                         'trapFormat': 'SNMPv3',
                                                                         'trapDestination': '192.168.148.49',
                                                                         'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                         'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                         'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                         'vcmTrapCategories':['Legacy'],
                                                                         'userName':'User1',
                                                                         'port': '163'}],
                                                   'snmpAccess': [],
                                                   'enabled': False,
                                                   'description': None,
                                                   'category': 'snmp-configuration',
                                                   'uri': None
                                               }
                                               }

edit_li_exiting_snmp_users_authpass_to_authprivpass = {'snmpConfiguration':
                                                       {
                                                           'type': 'snmp-configuration',
                                                           'readCommunity': 'public',
                                                           'systemContact': '',
                                                           'v3Enabled': True,
                                                           'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                         {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                                         {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                         {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                         {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                         {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                           'trapDestinations': [{'inform': False,
                                                                                 'engineId': None,
                                                                                 'trapFormat': 'SNMPv3',
                                                                                 'trapDestination': '192.168.148.49',
                                                                                 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                 'vcmTrapCategories':['Legacy'],
                                                                                 'userName':'User1',
                                                                                 'port': '163'}],
                                                           'snmpAccess': [],
                                                           'enabled': False,
                                                           'description': None,
                                                           'category': 'snmp-configuration',
                                                           'uri': None
                                                       }
                                                       }

edit_li_exiting_snmp_users_seclev_AuthPrivtoNone = {'snmpConfiguration':
                                                    {
                                                        'type': 'snmp-configuration',
                                                        'readCommunity': 'public',
                                                        'systemContact': '',
                                                        'v3Enabled': True,
                                                        'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                      {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                      {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                      {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                      {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                      {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                        'trapDestinations': [{'inform': False,
                                                                              'engineId': None,
                                                                              'trapFormat': 'SNMPv3',
                                                                              'trapDestination': '192.168.148.49',
                                                                              'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                              'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                              'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                              'vcmTrapCategories':['Legacy'],
                                                                              'userName':'User1',
                                                                              'port': '163'}],
                                                        'snmpAccess': [],
                                                        'enabled': False,
                                                        'description': None,
                                                        'category': 'snmp-configuration',
                                                        'uri': None
                                                    }
                                                    }

edit_li_exiting_snmp_users_seclev_AuthtoNone = {'snmpConfiguration':
                                                {
                                                    'type': 'snmp-configuration',
                                                    'readCommunity': 'public',
                                                    'systemContact': '',
                                                    'v3Enabled': True,
                                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                  {'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                  {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                  {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                  {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                  {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                    'trapDestinations': [{'inform': False,
                                                                          'engineId': None,
                                                                          'trapFormat': 'SNMPv3',
                                                                          'trapDestination': '192.168.148.49',
                                                                          'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                          'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                          'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                          'vcmTrapCategories':['Legacy'],
                                                                          'userName':'User1',
                                                                          'port': '163'}],
                                                    'snmpAccess': [],
                                                    'enabled': False,
                                                    'description': None,
                                                    'category': 'snmp-configuration',
                                                    'uri': None
                                                }
                                                }

edit_li_exiting_snmp_users_Auth_Invalid_PassPhrase = {'snmpConfiguration':
                                                      {
                                                          'type': 'snmp-configuration',
                                                          'readCommunity': 'public',
                                                          'systemContact': '',
                                                          'v3Enabled': True,
                                                          'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                        {'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                        {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                        {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password@123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                        {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                        {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                          'trapDestinations': [{'inform': False,
                                                                                'engineId': None,
                                                                                'trapFormat': 'SNMPv3',
                                                                                'trapDestination': '192.168.148.49',
                                                                                'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                'vcmTrapCategories':['Legacy'],
                                                                                'userName':'User1',
                                                                                'port': '163'}],
                                                          'snmpAccess': [],
                                                          'enabled': False,
                                                          'description': None,
                                                          'category': 'snmp-configuration',
                                                          'uri': None
                                                      }
                                                      }

edit_li_exiting_snmp_users_AuthPriv_Invalid_PassPhrase = {'snmpConfiguration':
                                                          {
                                                              'type': 'snmp-configuration',
                                                              'readCommunity': 'public',
                                                              'systemContact': '',
                                                              'v3Enabled': True,
                                                              'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                            {'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                            {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                            {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password@123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                            {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                            {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                              'trapDestinations': [{'inform': False,
                                                                                    'engineId': None,
                                                                                    'trapFormat': 'SNMPv3',
                                                                                    'trapDestination': '192.168.148.49',
                                                                                    'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                    'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                    'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                    'vcmTrapCategories':['Legacy'],
                                                                                    'userName':'User1',
                                                                                    'port': '163'}],
                                                              'snmpAccess': [],
                                                              'enabled': False,
                                                              'description': None,
                                                              'category': 'snmp-configuration',
                                                              'uri': None
                                                          }
                                                          }

edit_li_exiting_snmp_Auth_Algorithm_empty = {'snmpConfiguration':
                                             {
                                                 'type': 'snmp-configuration',
                                                 'readCommunity': 'public',
                                                 'systemContact': '',
                                                 'v3Enabled': True,
                                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                               {'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'', 'v3PrivacyProtocol':'NA'},
                                                               {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password@123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                               {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                               {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                               {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                 'trapDestinations': [{'inform': False,
                                                                       'engineId': None,
                                                                       'trapFormat': 'SNMPv3',
                                                                       'trapDestination': '192.168.148.49',
                                                                       'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                       'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                       'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                       'vcmTrapCategories':['Legacy'],
                                                                       'userName':'User1',
                                                                       'port': '163'}],
                                                 'snmpAccess': [],
                                                 'enabled': False,
                                                 'description': None,
                                                 'category': 'snmp-configuration',
                                                 'uri': None
                                             }
                                             }

edit_li_exiting_snmp_Auth_Passphrase_empty = {'snmpConfiguration':
                                              {
                                                  'type': 'snmp-configuration',
                                                  'readCommunity': 'public',
                                                  'systemContact': '',
                                                  'v3Enabled': True,
                                                  'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                  'trapDestinations': [{'inform': False,
                                                                        'engineId': None,
                                                                        'trapFormat': 'SNMPv3',
                                                                        'trapDestination': '192.168.148.49',
                                                                        'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                        'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                        'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                        'vcmTrapCategories':['Legacy'],
                                                                        'userName':'User1',
                                                                        'port': '163'}],
                                                  'snmpAccess': [],
                                                  'enabled': False,
                                                  'description': None,
                                                  'category': 'snmp-configuration',
                                                  'uri': None
                                              }
                                              }

edit_li_exiting_snmp_AuthPriv_Passphrase_empty = {'snmpConfiguration':
                                                  {
                                                      'type': 'snmp-configuration',
                                                      'readCommunity': 'public',
                                                      'systemContact': '',
                                                      'v3Enabled': True,
                                                      'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                                    {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                    {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                    {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                    {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                    {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                      'trapDestinations': [{'inform': False,
                                                                            'engineId': None,
                                                                            'trapFormat': 'SNMPv3',
                                                                            'trapDestination': '192.168.148.49',
                                                                            'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                            'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                            'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                            'vcmTrapCategories':['Legacy'],
                                                                            'userName':'User1',
                                                                            'port': '163'}],
                                                      'snmpAccess': [],
                                                      'enabled': False,
                                                      'description': None,
                                                      'category': 'snmp-configuration',
                                                      'uri': None
                                                  }
                                                  }

edit_li_exiting_snmp_users_auth_and_passphrase = {'snmpConfiguration':
                                                  {
                                                      'type': 'snmp-configuration',
                                                      'readCommunity': 'public',
                                                      'systemContact': '',
                                                      'v3Enabled': True,
                                                      'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                    {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                                    {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                    {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                    {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                    {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                      'trapDestinations': [{'inform': False,
                                                                            'engineId': None,
                                                                            'trapFormat': 'SNMPv3',
                                                                            'trapDestination': '192.168.148.49',
                                                                            'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                            'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                            'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                            'vcmTrapCategories':['Legacy'],
                                                                            'userName':'User1',
                                                                            'port': '163'}],
                                                      'snmpAccess': [],
                                                      'enabled': False,
                                                      'description': None,
                                                      'category': 'snmp-configuration',
                                                      'uri': None
                                                  }
                                                  }

edit_li_snmpv3_disabled_add_trap_destination = {'snmpConfiguration':
                                                {
                                                    'type': 'snmp-configuration',
                                                    'readCommunity': 'public',
                                                    'systemContact': '',
                                                    'v3Enabled': False,
                                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                  {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                                  {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                  {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                  {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                  {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                    'trapDestinations': [{'inform': False,
                                                                          'engineId': None,
                                                                          'trapFormat': 'SNMPv3',
                                                                          'trapDestination': '192.168.148.49',
                                                                          'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                          'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                          'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                          'vcmTrapCategories':['Legacy'],
                                                                          'userName':'User1',
                                                                          'port': '163'}],
                                                    'snmpAccess': [],
                                                    'enabled': False,
                                                    'description': None,
                                                    'category': 'snmp-configuration',
                                                    'uri': None
                                                }
                                                }

edit_li_snmpv3_enabled_add_trap_destination = {'snmpConfiguration':
                                               {
                                                   'type': 'snmp-configuration',
                                                   'readCommunity': 'public',
                                                   'systemContact': '',
                                                   'v3Enabled': True,
                                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                                 {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                 {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                 {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                   'trapDestinations': [{'inform': True,
                                                                         'engineId': '0xFFFFFFFFFFFF',
                                                                         'trapFormat': 'SNMPv3',
                                                                         'trapDestination': '192.168.148.49',
                                                                         'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                         'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                         'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                         'vcmTrapCategories':['Legacy'],
                                                                         'userName':'User1',
                                                                         'port': '163'}],
                                                   'snmpAccess': [],
                                                   'enabled': False,
                                                   'description': None,
                                                   'category': 'snmp-configuration',
                                                   'uri': None
                                               }
                                               }

edit_li_exiting_snmp_no_snmp_users = {'snmpConfiguration':
                                      {
                                          'type': 'snmp-configuration',
                                          'readCommunity': 'public',
                                          'systemContact': '',
                                          'v3Enabled': True,
                                          'snmpUsers': [],
                                          'trapDestinations': [{'inform': False,
                                                                'engineId': None,
                                                                'trapFormat': 'SNMPv3',
                                                                'trapDestination': '192.168.148.49',
                                                                'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                'vcmTrapCategories':['Legacy'],
                                                                'userName':'User1',
                                                                'port': '163'}],
                                          'snmpAccess': [],
                                          'enabled': False,
                                          'description': None,
                                          'category': 'snmp-configuration',
                                          'uri': None
                                      }
                                      }

edit_li_exiting_inform_disabled_Trap_type = {'snmpConfiguration':
                                             {
                                                 'type': 'snmp-configuration',
                                                 'readCommunity': 'public',
                                                 'systemContact': '',
                                                 'v3Enabled': True,
                                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                               {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                               {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                               {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                               {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                               {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                 'trapDestinations': [{'inform': False,
                                                                       'engineId': None,
                                                                       'trapFormat': 'SNMPv3',
                                                                       'trapDestination': '192.168.148.49',
                                                                       'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                       'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                       'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                       'vcmTrapCategories':['Legacy'],
                                                                       'userName':'User1',
                                                                       'port': '163'}],
                                                 'snmpAccess': [],
                                                 'enabled': False,
                                                 'description': None,
                                                 'category': 'snmp-configuration',
                                                 'uri': None
                                             }
                                             }

edit_li_snmpv3_enabled_add_trap_inform_No_EngineId = {'snmpConfiguration':
                                                      {
                                                          'type': 'snmp-configuration',
                                                          'readCommunity': 'public',
                                                          'systemContact': '',
                                                          'v3Enabled': True,
                                                          'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                        {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                                        {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                        {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                        {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                        {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                          'trapDestinations': [{'inform': True,
                                                                                'engineId': ' ',
                                                                                'trapFormat': 'SNMPv3',
                                                                                'trapDestination': '192.168.148.49',
                                                                                'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                'vcmTrapCategories':['Legacy'],
                                                                                'userName':'User1',
                                                                                'port': '163'}],
                                                          'snmpAccess': [],
                                                          'enabled': False,
                                                          'description': None,
                                                          'category': 'snmp-configuration',
                                                          'uri': None
                                                      }
                                                      }

edit_li_snmpv3_add_more_than_one_user_trap_destination = {'snmpConfiguration':
                                                          {
                                                              'type': 'snmp-configuration',
                                                              'readCommunity': 'public',
                                                              'systemContact': '',
                                                              'v3Enabled': True,
                                                              'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                            {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                                            {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                            {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                                            {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                                            {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                              'trapDestinations': [{'inform': False,
                                                                                    'engineId': None,
                                                                                    'trapFormat': 'SNMPv3',
                                                                                    'trapDestination': '192.168.148.49',
                                                                                    'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                    'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                    'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                    'vcmTrapCategories':['Legacy'],
                                                                                    'userName':'User1',
                                                                                    'port': '163'},
                                                                                   {'inform': False,
                                                                                    'engineId': None,
                                                                                    'trapFormat': 'SNMPv3',
                                                                                    'trapDestination': '192.168.148.49',
                                                                                    'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                    'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                    'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                    'vcmTrapCategories':['Legacy'],
                                                                                    'userName':'User2',
                                                                                    'port': '163'},
                                                                                   {'inform': False,
                                                                                    'engineId': None,
                                                                                    'trapFormat': 'SNMPv3',
                                                                                    'trapDestination': '192.168.148.50',
                                                                                    'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                    'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                    'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                    'vcmTrapCategories':['Legacy'],
                                                                                    'userName':'User1',
                                                                                    'port': '163'}],
                                                              'snmpAccess': [],
                                                              'enabled': False,
                                                              'description': None,
                                                              'category': 'snmp-configuration',
                                                              'uri': None
                                                          }
                                                          }

edit_li_snmpv3_engine_id_trap = {'snmpConfiguration':
                                 {
                                     'type': 'snmp-configuration',
                                     'readCommunity': 'public',
                                     'systemContact': '',
                                     'v3Enabled': True,
                                     'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                   {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                   {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                   {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                   {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                   {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                     'trapDestinations': [{'inform': False,
                                                           'engineId': '0xFFFFFFFFFFFF',
                                                           'trapFormat': 'SNMPv3',
                                                           'trapDestination': '192.168.148.49',
                                                           'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                           'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                           'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                           'vcmTrapCategories':['Legacy'],
                                                           'userName':'User1',
                                                           'port': '163'},
                                                          ],
                                     'snmpAccess': [],
                                     'enabled': False,
                                     'description': None,
                                     'category': 'snmp-configuration',
                                     'uri': None
                                 }
                                 }

edit_li_snmpv3_auth_improper_credential = {'snmpConfiguration':
                                           {
                                               'type': 'snmp-configuration',
                                               'readCommunity': 'public',
                                               'systemContact': '',
                                               'v3Enabled': True,
                                               'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": ")", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                               'trapDestinations': [{'inform': False,
                                                                     'engineId': '0xFFFFFFFFFFFF',
                                                                     'trapFormat': 'SNMPv3',
                                                                     'trapDestination': '192.168.148.49',
                                                                     'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                     'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                     'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                     'vcmTrapCategories':['Legacy'],
                                                                     'userName':'User1',
                                                                     'port': '163'},
                                                                    ],
                                               'snmpAccess': [],
                                               'enabled': False,
                                               'description': None,
                                               'category': 'snmp-configuration',
                                               'uri': None
                                           }
                                           }

edit_li_snmpv3_priv_improper_credential = {'snmpConfiguration':
                                           {
                                               'type': 'snmp-configuration',
                                               'readCommunity': 'public',
                                               'systemContact': '',
                                               'v3Enabled': True,
                                               'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "@", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                               'trapDestinations': [{'inform': False,
                                                                     'engineId': '0xFFFFFFFFFFFF',
                                                                     'trapFormat': 'SNMPv3',
                                                                     'trapDestination': '192.168.148.49',
                                                                     'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                     'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                     'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                     'vcmTrapCategories':['Legacy'],
                                                                     'userName':'User1',
                                                                     'port': '163'},
                                                                    ],
                                               'snmpAccess': [],
                                               'enabled': False,
                                               'description': None,
                                               'category': 'snmp-configuration',
                                               'uri': None
                                           }
                                           }

edit_li_snmpv3_add_max_traps = {'snmpConfiguration':
                                {
                                    'type': 'snmp-configuration',
                                    'readCommunity': 'public',
                                    'systemContact': '',
                                    'v3Enabled': True,
                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [{'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.49', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User1', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.50', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User2', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.51', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User3', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.52', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User4', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.53', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User5', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.54', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User6', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.55', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User2', 'port': '163'},
                                                         ],
                                    'snmpAccess': [],
                                    'enabled': False,
                                    'description': None,
                                    'category': 'snmp-configuration',
                                    'uri': None
                                }
                                }

edit_li_snmpv3_add_max_users = {'snmpConfiguration':
                                {
                                    'type': 'snmp-configuration',
                                    'readCommunity': 'public',
                                    'systemContact': '',
                                    'v3Enabled': True,
                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                  {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User7', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [{'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.49', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User1', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.50', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User2', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.51', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User3', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.52', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User4', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.53', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User5', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.54', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User6', 'port': '163'},
                                                         {'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.55', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User2', 'port': '163'},
                                                         ],
                                    'snmpAccess': [],
                                    'enabled': False,
                                    'description': None,
                                    'category': 'snmp-configuration',
                                    'uri': None
                                }
                                }

edit_li_snmpv3_trap_user_doesnot_exists = {'snmpConfiguration':
                                           {
                                               'type': 'snmp-configuration',
                                               'readCommunity': 'public',
                                               'systemContact': '',
                                               'v3Enabled': True,
                                               'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                             {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                             {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                             {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                             {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                             {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                             ],
                                               'trapDestinations': [{'inform': False, 'engineId': 'None', 'trapFormat': 'SNMPv3', 'trapDestination': '192.168.148.49', 'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'', 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'], 'vcmTrapCategories':['Legacy'], 'userName':'User7', 'port': '163'},

                                                                    ],
                                               'snmpAccess': [],
                                               'enabled': False,
                                               'description': None,
                                               'category': 'snmp-configuration',
                                               'uri': None
                                           }
                                           }

edit_li_snmpv3_auth_missing_pwd = {'snmpConfiguration':
                                   {
                                       'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'v3Enabled': True,
                                       'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                     {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                     {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                     {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                     {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                       'trapDestinations': [{'inform': True,
                                                             'engineId': '0xFFFFFFFFFFFF',
                                                             'trapFormat': 'SNMPv3',
                                                             'trapDestination': '192.168.148.49',
                                                             'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                             'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                             'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                             'vcmTrapCategories':['Legacy'],
                                                             'userName':'User1',
                                                             'port': '163'},
                                                            ],
                                       'snmpAccess': [],
                                       'enabled': False,
                                       'description': None,
                                       'category': 'snmp-configuration',
                                       'uri': None
                                   }
                                   }

edit_li_snmpv3_priv_missing_pwd = {'snmpConfiguration':
                                   {
                                       'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'v3Enabled': True,
                                       'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                     {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                     {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                     {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                     {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                       'trapDestinations': [{'inform': True,
                                                             'engineId': '0xFFFFFFFFFFFF',
                                                             'trapFormat': 'SNMPv3',
                                                             'trapDestination': '192.168.148.49',
                                                             'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                             'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                             'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                             'vcmTrapCategories':['Legacy'],
                                                             'userName':'User1',
                                                             'port': '163'},
                                                            ],
                                       'snmpAccess': [],
                                       'enabled': False,
                                       'description': None,
                                       'category': 'snmp-configuration',
                                       'uri': None
                                   }
                                   }

edit_li_snmpv3_user_invalid = {'snmpConfiguration':
                               {
                                   'type': 'snmp-configuration',
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'v3Enabled': True,
                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                 {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                 {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                 {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                 {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                 ],
                                   'trapDestinations': [{'inform': True,
                                                         'engineId': '0xFFFFFFFFFFFF',
                                                         'trapFormat': 'SNMPv3',
                                                         'trapDestination': '192.168.148.49',
                                                         'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                         'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                         'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                         'vcmTrapCategories':['Legacy'],
                                                         'userName':'User1',
                                                         'port': '163'},
                                                        ],
                                   'snmpAccess': [],
                                   'enabled': False,
                                   'description': None,
                                   'category': 'snmp-configuration',
                                   'uri': None
                               }
                               }
edit_li_snmpv3_user_invalid_add = {'snmpConfiguration':
                                   {
                                       'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'v3Enabled': True,
                                       'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                     {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                     {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                     {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                     {'snmpV3UserName': '+', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                     ],
                                       'trapDestinations': [{'inform': True,
                                                             'engineId': '0xFFFFFFFFFFFF',
                                                             'trapFormat': 'SNMPv3',
                                                             'trapDestination': '192.168.148.49',
                                                             'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                             'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                             'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                             'vcmTrapCategories':['Legacy'],
                                                             'userName':'User1',
                                                             'port': '163'},
                                                            ],
                                       'snmpAccess': [],
                                       'enabled': False,
                                       'description': None,
                                       'category': 'snmp-configuration',
                                       'uri': None
                                   }
                                   }

edit_li_snmpv3_engine_id_invalid = {'snmpConfiguration':
                                    {
                                        'type': 'snmp-configuration',
                                        'readCommunity': 'public',
                                        'systemContact': '',
                                        'v3Enabled': True,
                                        'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                      {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                      {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                      {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                      {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                      ],
                                        'trapDestinations': [{'inform': True,
                                                              'engineId': '123',
                                                              'trapFormat': 'SNMPv3',
                                                              'trapDestination': '192.168.148.49',
                                                              'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                              'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                              'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                              'vcmTrapCategories':['Legacy'],
                                                              'userName':'User1',
                                                              'port': '163'},
                                                             ],
                                        'snmpAccess': [],
                                        'enabled': False,
                                        'description': None,
                                        'category': 'snmp-configuration',
                                        'uri': None
                                    }
                                    }

edit_li_snmpv3_host_invalid = {'snmpConfiguration':
                               {
                                   'type': 'snmp-configuration',
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'v3Enabled': True,
                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                 {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                 {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                 {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                 {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                 ],
                                   'trapDestinations': [{'inform': False,
                                                         'engineId': 'None',
                                                         'trapFormat': 'SNMPv3',
                                                         'trapDestination': '192',
                                                         'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                         'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                         'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                         'vcmTrapCategories':['Legacy'],
                                                         'userName':'User1',
                                                         'port': '163'},
                                                        ],
                                   'snmpAccess': [],
                                   'enabled': False,
                                   'description': None,
                                   'category': 'snmp-configuration',
                                   'uri': None
                               }
                               }

edit_li_snmpv3_invalid_range = {'snmpConfiguration':
                                {
                                    'type': 'snmp-configuration',
                                    'readCommunity': 'public',
                                    'systemContact': '',
                                    'v3Enabled': True,
                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                  {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                  {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [{'inform': True,
                                                          'engineId': '0xFFFFFFFFFFFF',
                                                          'trapFormat': 'SNMPv3',
                                                          'trapDestination': '192.168.148.49',
                                                          'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                          'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                          'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                          'vcmTrapCategories':['Legacy'],
                                                          'userName':'User1',
                                                          'port': '162000000'}],
                                    'snmpAccess': [],
                                    'enabled': False,
                                    'description': None,
                                    'category': 'snmp-configuration',
                                    'uri': None
                                }
                                }

# Update From group
edit_snmp_lig_trap_snmpv3_disabled_UFG = {'lig1':
                                          {'name': 'LIG_New1',
                                           'type': 'logical-interconnect-groupV4',
                                           'enclosureType': 'C7000',
                                           'interconnectMapTemplate': icmap_snmp,
                                           'uplinkSets': [uplink_sets['us1']],
                                           'stackingMode': 'Enclosure',
                                           'ethernetSettings': None,
                                           'state': 'Active',
                                           'telemetryConfiguration': None,
                                           'snmpConfiguration': {'type': 'snmp-configuration',
                                                                 'trapDestinations': [{'inform': False, 'engineId': None,
                                                                                       'trapFormat': 'SNMPv3',
                                                                                       'trapDestination': '192.168.148.49',
                                                                                       'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                       'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                       'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                       'vcmTrapCategories':['Legacy'],
                                                                                       'userName':'User1',
                                                                                       'port': '163'}],
                                                                 'snmpAccess': [],
                                                                 'snmpUsers': [
                                                                     {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                     {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                     {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                 ],
                                                                 'readCommunity': 'public',
                                                                 'v3Enabled': False,
                                                                 'enabled': False,
                                                                 'description': '',
                                                                 'category': 'snmp-configuration',
                                                                 'uri': ''}
                                           }

                                          }

edit_snmp_lig_trap_snmpv3_enabled_UFG = {'lig1':
                                         {'name': 'LIG_New1',
                                          'type': 'logical-interconnect-groupV4',
                                          'enclosureType': 'C7000',
                                          'interconnectMapTemplate': icmap_snmp,
                                          'uplinkSets': [uplink_sets['us1']],
                                          'stackingMode': 'Enclosure',
                                          'ethernetSettings': None,
                                          'state': 'Active',
                                          'telemetryConfiguration': None,
                                          'snmpConfiguration': {'type': 'snmp-configuration',
                                                                'trapDestinations': [],
                                                                'snmpAccess': [],
                                                                'snmpUsers': [
                                                                    {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                    {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                    {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                ],
                                                                'readCommunity': 'public',
                                                                'v3Enabled': True,
                                                                'enabled': False,
                                                                'description': '',
                                                                'category': 'snmp-configuration',
                                                                'uri': ''}
                                          }

                                         }

edit_snmp_lig_trap_snmpv3_addtrap_UFG = {'lig1':
                                         {'name': 'LIG_New1',
                                          'type': 'logical-interconnect-groupV4',
                                          'enclosureType': 'C7000',
                                          'interconnectMapTemplate': icmap_snmp,
                                          'uplinkSets': [uplink_sets['us1']],
                                          'stackingMode': 'Enclosure',
                                          'ethernetSettings': None,
                                          'state': 'Active',
                                          'telemetryConfiguration': None,
                                          'snmpConfiguration': {'type': 'snmp-configuration',
                                                                'trapDestinations': [{'inform': False, 'engineId': None,
                                                                                      'trapFormat': 'SNMPv3',
                                                                                      'trapDestination': '192.168.148.49',
                                                                                      'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                      'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                      'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                      'vcmTrapCategories':['Legacy'],
                                                                                      'userName':'User1',
                                                                                      'port': '163'}],
                                                                'snmpAccess': [],
                                                                'snmpUsers': [
                                                                    {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                    {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                    {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                ],
                                                                'readCommunity': 'public',
                                                                'v3Enabled': True,
                                                                'enabled': False,
                                                                'description': '',
                                                                'category': 'snmp-configuration',
                                                                'uri': ''}
                                          }

                                         }

edit_snmp_lig_trap_snmpv3_add_access_UFG = {'lig1':
                                            {'name': 'LIG_New1',
                                             'type': 'logical-interconnect-groupV4',
                                             'enclosureType': 'C7000',
                                             'interconnectMapTemplate': icmap_snmp,
                                             'uplinkSets': [uplink_sets['us1']],
                                             'stackingMode': 'Enclosure',
                                             'ethernetSettings': None,
                                             'state': 'Active',
                                             'telemetryConfiguration': None,
                                             'snmpConfiguration': {'type': 'snmp-configuration',
                                                                   'trapDestinations': [{'inform': False, 'engineId': None,
                                                                                         'trapFormat': 'SNMPv3',
                                                                                         'trapDestination': '192.168.148.49',
                                                                                         'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                                         'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                                         'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                         'vcmTrapCategories':['Legacy'],
                                                                                         'userName':'User1',
                                                                                         'port': '163'}],
                                                                   'snmpAccess': ['192.168.144.146/24'],
                                                                   'snmpUsers': [
                                                                       {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                       {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                       {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},

                                                                   ],
                                                                   'readCommunity': 'public',
                                                                   'v3Enabled': True,
                                                                   'enabled': False,
                                                                   'description': '',
                                                                   'category': 'snmp-configuration',
                                                                   'uri': ''}
                                             }

                                            }

edit_snmp_lig_snmpv3_Auth_UFG = {'lig1':
                                 {'name': 'LIG_New1',
                                  'type': 'logical-interconnect-groupV4',
                                  'enclosureType': 'C7000',
                                  'interconnectMapTemplate': icmap_snmp,
                                  'uplinkSets': [uplink_sets['us1']],
                                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': {'type': 'snmp-configuration',
                                                        'trapDestinations': [{'inform': False, 'engineId': None,
                                                                              'trapFormat': 'SNMPv3',
                                                                              'trapDestination': '192.168.148.49',
                                                                              'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                              'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                              'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                              'vcmTrapCategories':['Legacy'],
                                                                              'userName':'User1',
                                                                              'port': '163'}],
                                                        'snmpAccess': ['192.168.144.146/24'],
                                                        'snmpUsers': [
                                                            {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                            {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                        ],
                                                        'readCommunity': 'public',
                                                        'v3Enabled': True,
                                                        'enabled': False,
                                                        'description': '',
                                                        'category': 'snmp-configuration',
                                                        'uri': ''}
                                  }

                                 }

edit_snmp_lig_snmpv3_Priv_UFG = {'lig1':
                                 {'name': 'LIG_New1',
                                  'type': 'logical-interconnect-groupV4',
                                  'enclosureType': 'C7000',
                                  'interconnectMapTemplate': icmap_snmp,
                                  'uplinkSets': [uplink_sets['us1']],
                                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': {'type': 'snmp-configuration',
                                                        'trapDestinations': [{'inform': False, 'engineId': None,
                                                                              'trapFormat': 'SNMPv3',
                                                                              'trapDestination': '192.168.148.49',
                                                                              'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                              'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                              'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                              'vcmTrapCategories':['Legacy'],
                                                                              'userName':'User1',
                                                                              'port': '163'}],
                                                        'snmpAccess': ['192.168.144.146/24'],
                                                        'snmpUsers': [
                                                            {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                            {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                        ],
                                                        'readCommunity': 'public',
                                                        'v3Enabled': True,
                                                        'enabled': False,
                                                        'description': '',
                                                        'category': 'snmp-configuration',
                                                        'uri': ''}
                                  }

                                 }

edit_snmp_lig_snmpv3_Severity_UFG = {'lig1':
                                     {'name': 'LIG_New1',
                                      'type': 'logical-interconnect-groupV4',
                                      'enclosureType': 'C7000',
                                      'interconnectMapTemplate': icmap_snmp,
                                      'uplinkSets': [uplink_sets['us1']],
                                      'stackingMode': 'Enclosure',
                                      'ethernetSettings': None,
                                      'state': 'Active',
                                      'telemetryConfiguration': None,
                                      'snmpConfiguration': {'type': 'snmp-configuration',
                                                            'trapDestinations': [{'inform': False, 'engineId': None,
                                                                                  'trapFormat': 'SNMPv3',
                                                                                  'trapDestination': '192.168.148.49',
                                                                                  'fcTrapCategories': ['PortStatus'], 'communityString':'',
                                                                                                                      'enetTrapCategories':['PortStatus', 'Other'],
                                                                                                                      'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                                                                      'vcmTrapCategories':['Legacy'],
                                                                                                                      'userName':'User1',
                                                                                                                      'port': '163'}],
                                                            'snmpAccess': ['192.168.144.146/24'],
                                                            'snmpUsers': [
                                                                {'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                                {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                                {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                                {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                            ],
                                                            'readCommunity': 'public',
                                                            'v3Enabled': True,
                                                            'enabled': False,
                                                            'description': '',
                                                            'category': 'snmp-configuration',
                                                            'uri': ''}
                                      }

                                     }

edit_snmp_lig_snmpv3_remove_Users_UFG = {'lig1':
                                         {'name': 'LIG_New1',
                                          'type': 'logical-interconnect-groupV4',
                                          'enclosureType': 'C7000',
                                          'interconnectMapTemplate': icmap_snmp,
                                          'uplinkSets': [uplink_sets['us1']],
                                          'stackingMode': 'Enclosure',
                                          'ethernetSettings': None,
                                          'state': 'Active',
                                          'telemetryConfiguration': None,
                                          'snmpConfiguration': {'type': 'snmp-configuration',
                                                                'trapDestinations': [],
                                                                'snmpAccess': ['192.168.144.146/24'],
                                                                'snmpUsers': [],
                                                                'readCommunity': 'public',
                                                                'v3Enabled': True,
                                                                'enabled': False,
                                                                'description': '',
                                                                'category': 'snmp-configuration',
                                                                'uri': ''}
                                          }

                                         }

# Edit LI with UFG

edit_li_snmpv3_add_users_traps_UFG = {'snmpConfiguration':
                                      {
                                          'type': 'snmp-configuration',
                                          'readCommunity': 'public',
                                          'systemContact': '',
                                          'v3Enabled': True,
                                          'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                        {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                        {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                        {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                        {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                        {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                          'trapDestinations': [{'inform': False,
                                                                'engineId': None,
                                                                'trapFormat': 'SNMPv3',
                                                                'trapDestination': '192.168.148.49',
                                                                'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                                'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                                'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                                'vcmTrapCategories':['Legacy'],
                                                                'userName':'User1',
                                                                'port': '163'}],
                                          'snmpAccess': [],
                                          'enabled': False,
                                          'description': None,
                                          'category': 'snmp-configuration',
                                          'uri': None
                                      }
                                      }

edit_li_snmpv3_edit_user_Auth_UFG = {'snmpConfiguration':
                                     {
                                         'type': 'snmp-configuration',
                                         'readCommunity': 'public',
                                         'systemContact': '',
                                         'v3Enabled': True,
                                         'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, ], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                       {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                       {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                       {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                       {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                       {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                         'trapDestinations': [{'inform': False,
                                                               'engineId': None,
                                                               'trapFormat': 'SNMPv3',
                                                               'trapDestination': '192.168.148.49',
                                                               'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                               'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                               'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                               'vcmTrapCategories':['Legacy'],
                                                               'userName':'User1',
                                                               'port': '163'}],
                                         'snmpAccess': [],
                                         'enabled': False,
                                         'description': None,
                                         'category': 'snmp-configuration',
                                         'uri': None
                                     }
                                     }

edit_li_snmpv3_edit_user_Priv_UFG = {'snmpConfiguration':
                                     {
                                         'type': 'snmp-configuration',
                                         'readCommunity': 'public',
                                         'systemContact': '',
                                         'v3Enabled': True,
                                         'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                       {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                       {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                       {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                       {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                       {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                         'trapDestinations': [{'inform': False,
                                                               'engineId': None,
                                                               'trapFormat': 'SNMPv3',
                                                               'trapDestination': '192.168.148.49',
                                                               'fcTrapCategories': ['Other', 'PortStatus'], 'communityString':'',
                                                               'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'],
                                                               'trapSeverities':['Normal', 'Critical', 'Info', 'Warning', 'Minor', 'Unknown', 'Major'],
                                                               'vcmTrapCategories':['Legacy'],
                                                               'userName':'User1',
                                                               'port': '163'}],
                                         'snmpAccess': [],
                                         'enabled': False,
                                         'description': None,
                                         'category': 'snmp-configuration',
                                         'uri': None
                                     }
                                     }

edit_li_snmpv3_edit_trap_severity_UFG = {'snmpConfiguration':
                                         {
                                             'type': 'snmp-configuration',
                                             'readCommunity': 'public',
                                             'systemContact': '',
                                             'v3Enabled': True,
                                             'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                           {'snmpV3UserName': 'User2', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                           {'snmpV3UserName': 'User3', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                           {'snmpV3UserName': 'User4', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                                           {'snmpV3UserName': 'User5', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                           {'snmpV3UserName': 'User6', 'userCredentials': [{"propertyName": "SnmpV3AuthorizationPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "password123", "valueFormat": "SecuritySensitive", "valueType": "String"}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                             'trapDestinations': [{'inform': False,
                                                                   'engineId': None,
                                                                   'trapFormat': 'SNMPv3',
                                                                   'trapDestination': '192.168.148.49',
                                                                   'fcTrapCategories': ['Other'], 'communityString':'',
                                                                   'enetTrapCategories':['Other'],
                                                                   'trapSeverities':['Warning', 'Minor', 'Unknown', 'Major'],
                                                                   'vcmTrapCategories':['Legacy'],
                                                                   'userName':'User1',
                                                                   'port': '163'}],
                                             'snmpAccess': [],
                                             'enabled': False,
                                             'description': None,
                                             'category': 'snmp-configuration',
                                             'uri': None
                                         }
                                         }

edit_li_snmpv3_remove_users_UFG = {'snmpConfiguration':
                                   {
                                       'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'systemContact': '',
                                       'v3Enabled': True,
                                       'snmpUsers': [],
                                       'trapDestinations': [],
                                       'snmpAccess': [],
                                       'enabled': False,
                                       'description': None,
                                       'category': 'snmp-configuration',
                                       'uri': None}
                                   }


SNMPV3_body_Default_NoAuthNoPriv = {'type': 'snmp-configuration',
                                    'trapDestinations': [{'trapDestination': '10.10.3.71',
                                                          'trapFormat': 'SNMPv3',
                                                          'trapSeverities': ['Major'],
                                                          'vcmTrapCategories':['Legacy'],
                                                          'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                          'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                    'snmpAccess': ["192.168.2.0/24"],
                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'readCommunity': 'public',
                                    'v3Enabled': False,
                                    'enabled': True,
                                    'description': '',
                                    'category': 'snmp-configuration',
                                    'uri': ''}


SNMPV3_body_Auth_MD5 = {'type': 'snmp-configuration',
                        'trapDestinations': [],
                        'snmpAccess': [],
                        'snmpUsers': [
                            {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}
                        ],
                        'readCommunity': 'public',
                        'v3Enabled': True,
                        'enabled': True,
                        'description': '',
                        'category': 'snmp-configuration',
                        'uri': ''}

SNMPV3_body_Auth_SHA = {'type': 'snmp-configuration',
                        'trapDestinations': [],
                        'snmpAccess': [],
                        'snmpUsers': [
                            {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}
                        ],
                        'readCommunity': 'public',
                        'v3Enabled': True,
                        'enabled': True,
                        'description': '',
                        'category': 'snmp-configuration',
                        'uri': ''}

SNMPV3_body_Auth_Priv_MD5_DES = {'type': 'snmp-configuration',
                                 'trapDestinations': [],
                                 'snmpAccess': ["192.168.2.0/24"],
                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}],
                                 'readCommunity': 'public',
                                 'v3Enabled': True,
                                 'enabled': True,
                                 'description': '',
                                 'category': 'snmp-configuration',
                                 'uri': ''}


SNMPV3_body_Auth_Priv_MD5_AES128 = {'type': 'snmp-configuration',
                                    'trapDestinations': [],
                                    'snmpAccess': ["192.168.2.0/24"],
                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}],
                                    'readCommunity': 'public',
                                    'v3Enabled': True,
                                    'enabled': True,
                                    'description': '',
                                    'category': 'snmp-configuration',
                                    'uri': ''}

SNMPV3_body_Auth_Priv_SHA_DES = {'type': 'snmp-configuration',
                                 'trapDestinations': [],
                                 'snmpAccess': ["192.168.2.0/24"],
                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'}],
                                 'readCommunity': 'public',
                                 'v3Enabled': True,
                                 'enabled': True,
                                 'description': '',
                                 'category': 'snmp-configuration',
                                 'uri': ''}


SNMPV3_body_Auth_Priv_SHA_AES128 = {'type': 'snmp-configuration',
                                    'trapDestinations': [],
                                    'snmpAccess': ["192.168.2.0/24"],
                                    'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'readCommunity': 'public',
                                    'v3Enabled': True,
                                    'enabled': True,
                                    'description': '',
                                    'category': 'snmp-configuration',
                                    'uri': ''}

SNMPV3_body_Auth_MD5 = {'type': 'snmp-configuration',
                        'trapDestinations': [],
                        'snmpAccess': ["192.168.2.0/24"],
                        'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}],

                        'readCommunity': 'public',
                        'v3Enabled': True,
                        'enabled': True,
                        'description': '',
                        'category': 'snmp-configuration',
                        'uri': ''}

SNMPV3_body_snmp_disable = {'type': 'snmp-configuration',
                            'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                                   'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                                   'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                                   'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                            'snmpAccess': ["192.168.2.0/24"],
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                            'readCommunity': 'public',
                            'v3Enabled': False,
                            'enabled': True,
                            'description': '',
                            'category': 'snmp-configuration',
                            'uri': ''}

SNMPV3_body_snmp_lig_trap_destinations_no_users = {'type': 'snmp-configuration',
                                                   'trapDestinations': [],
                                                   'snmpAccess': ["192.168.2.0/24"],
                                                   'snmpUsers': [],
                                                   'readCommunity': 'public',
                                                   'v3Enabled': True,
                                                   'enabled': True,
                                                   'description': '',
                                                   'category': 'snmp-configuration',
                                                   'uri': ''}

snmp_lig_trap_destinations_without_users = {'type': 'snmp-configuration',
                                            'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                  'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                  'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                            'snmpAccess': ["192.168.2.0/24"],
                                            'snmpUsers': [],
                                            'readCommunity': 'public',
                                            'v3Enabled': True,
                                            'enabled': True,
                                            'description': '',
                                            'category': 'snmp-configuration',
                                            'uri': ''}

snmp_lig_trap_destinations_type_Trap = {'type': 'snmp-configuration',
                                        'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                              'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                              'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                              'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                        'snmpAccess': ["192.168.2.0/24"],

                                        'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],

                                        'readCommunity': 'public',
                                        'v3Enabled': True,
                                        'enabled': True,
                                        'description': '',
                                        'category': 'snmp-configuration',
                                        'uri': ''}

snmp_lig_trap_destinations_type_Inform_wo_engineID = {'type': 'snmp-configuration',
                                                      'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                                            'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                                            'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                                            'userName':'User1', 'inform':True, 'engineId':'', 'communityString':'', 'port':'162'}],
                                                      'snmpAccess': ["192.168.2.0/24"],
                                                      'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                      'readCommunity': 'public',
                                                      'v3Enabled': True,
                                                      'enabled': True,
                                                      'description': '',
                                                      'category': 'snmp-configuration',
                                                      'uri': ''}


snmp_lig_trap_dest_add_non_def_port = {'type': 'snmp-configuration',

                                       'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3',
                                                             'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                                             'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                                             'userName':'Test3', 'inform':False, 'communityString':'', 'port':'190'}],
                                       'snmpAccess': ["192.168.2.0/24"],
                                       'snmpUsers': [{'snmpV3UserName': 'Test3', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                     {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],

                                       'readCommunity': 'public',
                                       'v3Enabled': True,
                                       'enabled': True,
                                       'description': '',
                                       'category': 'snmp-configuration',
                                       'uri': ''}


snmp_traps = {'type': 'snmp-configuration',
              'trapDestinations': [{'trapDestination': '10.10.3.71', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.72', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test2', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.76', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.75', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.77', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'},
                                   {'trapDestination': '10.10.3.78', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test1', 'inform':False, 'communityString':'', 'port':'162'}],

              'snmpAccess': ["192.168.3.0/24"],
              'snmpUsers': [{'snmpV3UserName': 'Test6', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                            {'snmpV3UserName': 'Test5', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                            {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                            {'snmpV3UserName': 'Test3', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                            {'snmpV3UserName': 'Test2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                            {'snmpV3UserName': 'Test1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
              'readCommunity': 'public',
              'v3Enabled': True,
              'enabled': True,
              'description': '',
              'category': 'snmp-configuration',
              'uri': ''}


lig_snmp_trap_Address1 = {'type': 'snmp-configuration',
                          'trapDestinations': [{'trapDestination': '10.10.3.78', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'162'}],
                          'snmpAccess': ['192.168.3.0/24'],
                          'snmpUsers': [{'snmpV3UserName': 'Test4', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                        ],

                          'readCommunity': 'public',
                          'v3Enabled': True,
                          'enabled': True,
                          'description': '',
                          'category': 'snmp-configuration',
                          'uri': ''}


lig_snmp_trap_Address = {'type': 'snmp-configuration',

                         'trapDestinations': [{'trapDestination': '10.10.3.79', 'trapFormat': 'SNMPv3',
                                               'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'],
                                               'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'],
                                               'userName':'Test3', 'inform':False, 'communityString':'', 'port':'190'}],
                         'snmpAccess': ["192.168.2.0/24"],
                         'snmpUsers': [{'snmpV3UserName': 'Test3', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                       {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],

                         'readCommunity': 'public',
                         'v3Enabled': True,
                         'enabled': True,
                         'description': '',
                         'category': 'snmp-configuration',
                         'uri': ''}


lig_snmp_trap_Inform = {'type': 'snmp-configuration',
                        'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'162'}],
                        'snmpAccess': ['192.168.3.0/24'],
                        'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                        'readCommunity': 'public',
                        'v3Enabled': True,
                        'enabled': True,
                        'description': '',
                        'category': 'snmp-configuration',
                        'uri': ''}


lig_snmp_trap_port = {'type': 'snmp-configuration',
                      'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                      'snmpAccess': ['192.168.3.0/24'],
                      'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                      'readCommunity': 'public',
                      'v3Enabled': True,
                      'enabled': True,
                      'description': '',
                      'category': 'snmp-configuration',
                      'uri': ''}


lig_snmp_user_name = {'type': 'snmp-configuration',
                      'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test5', 'inform':False, 'communityString':'', 'port':'180'}],
                      'snmpAccess': ['192.168.3.0/24'],
                      'snmpUsers': [{'snmpV3UserName': 'Test5', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                      'readCommunity': 'public',
                      'v3Enabled': True,
                      'enabled': True,
                      'description': '',
                      'category': 'snmp-configuration',
                      'uri': ''}

lig_snmp_trap_type_inform = {'type': 'snmp-configuration',
                             'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'180'},
                                                  {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                             'snmpAccess': ['192.168.3.0/24'],
                             'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                             'readCommunity': 'public',
                             'v3Enabled': True,
                             'enabled': True,
                             'description': '',
                             'category': 'snmp-configuration',
                             'uri': ''}

lig_snmp_security_level = {'type': 'snmp-configuration',
                           'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'180'},
                                                {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                           'snmpAccess': ['192.168.3.0/24'],
                           'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                           'readCommunity': 'public',
                           'v3Enabled': True,
                           'enabled': True,
                           'description': '',
                           'category': 'snmp-configuration',
                           'uri': ''}


lig_snmp_invalid_port = {'type': 'snmp-configuration',
                         'trapDestinations': [{'trapDestination': '10.10.3.73', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':False, 'communityString':'', 'port':'abc'},
                                              {'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'0xFFFFFFFFFFFFFFFF', 'communityString':'', 'port':'180'}],
                         'snmpAccess': ['192.168.3.0/24'],
                         'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                         'readCommunity': 'public',
                         'v3Enabled': True,
                         'enabled': True,
                         'description': '',
                         'category': 'snmp-configuration',
                         'uri': ''}


lig_snmp_invalid_engineID = {'type': 'snmp-configuration',
                             'trapDestinations': [{'trapDestination': '10.10.3.74', 'trapFormat': 'SNMPv3', 'trapSeverities': ['Major'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus'], 'fcTrapCategories':['PortStatus'], 'userName':'Test4', 'inform':True, 'engineId':'12345', 'communityString':'', 'port':'180'}],
                             'snmpAccess': ['192.168.3.0/24'],
                             'snmpUsers': [{'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                             'readCommunity': 'public',
                             'v3Enabled': True,
                             'enabled': True,
                             'description': '',
                             'category': 'snmp-configuration',
                             'uri': ''}


snmp_user_duplicate_error = {'type': 'snmp-configuration',
                             'trapDestinations': [],
                             'snmpAccess': ["192.168.2.0/24"],
                             'snmpUsers': [
                                 {'snmpV3UserName': 'Test4', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                 {'snmpV3UserName': 'Test4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                             ],
                             'readCommunity': 'public',
                             'v3Enabled': True,
                             'enabled': True,
                             'description': '',
                             'category': 'snmp-configuration',
                             'uri': ''}


snmp_Invalidvalues_UserName = {'type': 'snmp-configuration',
                               'trapDestinations': [],
                               'snmpAccess': ["192.168.2.0/24"],
                               'snmpUsers': [{'snmpV3UserName': 'One_1212-nfn1213231323434434_****((((3$$$%%%', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, ],
                               'readCommunity': 'public',
                               'v3Enabled': True,
                               'enabled': True,
                               'description': '',
                               'category': 'snmp-configuration',
                               'uri': ''}


snmp_Invalidvalues_AuthPassPhrase = {'type': 'snmp-configuration',
                                     'trapDestinations': [],
                                     'snmpAccess': ["192.168.2.0/24"],
                                     'snmpUsers': [
                                         {'snmpV3UserName': 'Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                     ],
                                     'readCommunity': 'public',
                                     'v3Enabled': True,
                                     'enabled': True,
                                     'description': '',
                                     'category': 'snmp-configuration',
                                     'uri': ''}


snmp_Invalidvalues_Auth_Priv_Pass_Phrase = {'type': 'snmp-configuration',
                                            'trapDestinations': [],
                                            'snmpAccess': ["192.168.2.0/24"],
                                            'snmpUsers': [{'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '@'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}],
                                            'readCommunity': 'public',
                                            'v3Enabled': True,
                                            'enabled': True,
                                            'description': '',
                                            'category': 'snmp-configuration',
                                            'uri': ''}


snmp_Mandatory_Attribute_Check_Name = {'type': 'snmp-configuration',
                                       'trapDestinations': [],
                                       'snmpAccess': ["192.168.2.0/24"],
                                       'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, ],
                                       'readCommunity': 'public',
                                       'v3Enabled': True,
                                       'enabled': True,
                                       'description': '',
                                       'category': 'snmp-configuration',
                                       'uri': ''}

snmp_Mandatory_Attribute_Check_Authlgo = {'type': 'snmp-configuration',
                                          'trapDestinations': [],
                                          'snmpAccess': ["192.168.2.0/24"],
                                          'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}, ],
                                          'readCommunity': 'public',
                                          'v3Enabled': True,
                                          'enabled': True,
                                          'description': '',
                                          'category': 'snmp-configuration',
                                          'uri': ''}


snmp_Mandatory_Attribute_Check_AuthPassPhrase = {'type': 'snmp-configuration',
                                                 'trapDestinations': [],
                                                 'snmpAccess': ["192.168.2.0/24"],
                                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '$'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'}, ],
                                                 'readCommunity': 'public',
                                                 'v3Enabled': True,
                                                 'enabled': True,
                                                 'description': '',
                                                 'category': 'snmp-configuration',
                                                 'uri': ''}


snmp_Mandatory_Attribute_Check_Auth_Priv_PassPhrase = {'type': 'snmp-configuration',
                                                       'trapDestinations': [],
                                                       'snmpAccess': ["192.168.2.0/24"],
                                                       'snmpUsers': [{'snmpV3UserName': ' ', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}],
                                                       'readCommunity': 'public',
                                                       'v3Enabled': True,
                                                       'enabled': True,
                                                       'description': '',
                                                       'category': 'snmp-configuration',
                                                       'uri': ''}


snmp_Password_Length_Check = {'type': 'snmp-configuration',
                              'trapDestinations': [],
                              'snmpAccess': ["192.168.2.0/24"],
                              'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'}, ],
                              'readCommunity': 'public',
                              'v3Enabled': True,
                              'enabled': True,
                              'description': '',
                              'category': 'snmp-configuration',
                              'uri': ''}


snmp_Maximum_No_Of_Users = {'type': 'snmp-configuration',
                            'trapDestinations': [],
                            'snmpAccess': ["192.168.2.0/24"],
                            'snmpUsers': [
                                {'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                                {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                            ],
                            'readCommunity': 'public',
                            'v3Enabled': True,
                            'enabled': True,
                            'description': '',
                            'category': 'snmp-configuration',
                            'uri': ''}


add_lig_snmpv3_edit_user = {'type': 'snmp-configuration',
                            'trapDestinations': [],
                            'snmpAccess': ["192.168.2.0/24"],
                            'snmpUsers': [
                                {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                {'snmpV3UserName': 'Auth_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                {'snmpV3UserName': 'Auth_Priv_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                            ],
                            'readCommunity': 'public',
                            'v3Enabled': True,
                            'enabled': True,
                            'description': '',
                            'category': 'snmp-configuration',
                            'uri': ''}

edit_lig_snmpv3_users = {'type': 'snmp-configuration',
                         'trapDestinations': [],
                         'snmpAccess': ["192.168.2.0/24"],
                         'snmpUsers': [
                             {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'Auth_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                             {'snmpV3UserName': 'Auth_Priv_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                             {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
                         ],
                         'readCommunity': 'public',
                         'v3Enabled': True,
                         'enabled': True,
                         'description': '',
                         'category': 'snmp-configuration',
                         'uri': ''}

edit_lig_snmpv3_users_AuthtoAuthPriv = {'type': 'snmp-configuration',
                                        'trapDestinations': [],
                                        'snmpAccess': ["192.168.2.0/24"],
                                        'snmpUsers': [
                                            {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                            {'snmpV3UserName': 'Auth_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                            {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                        ],
                                        'readCommunity': 'public',
                                        'v3Enabled': True,
                                        'enabled': True,
                                        'description': '',
                                        'category': 'snmp-configuration',
                                        'uri': ''}


edit_lig_snmpv3_users_AuthPrivtoNone = {'type': 'snmp-configuration',
                                        'trapDestinations': [],
                                        'snmpAccess': ["192.168.2.0/24"],
                                        'snmpUsers': [
                                            {'snmpV3UserName': 'Auth_Three', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                            {'snmpV3UserName': 'Auth_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'Auth_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                        ],
                                        'readCommunity': 'public',
                                        'v3Enabled': True,
                                        'enabled': True,
                                        'description': '',
                                        'category': 'snmp-configuration',
                                        'uri': ''}


edit_lig_snmpv3_users_AuthtoNone = {'type': 'snmp-configuration',
                                    'trapDestinations': [],
                                    'snmpAccess': ["192.168.2.0/24"],
                                    'snmpUsers': [
                                        {'snmpV3UserName': 'Auth_Three', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                        {'snmpV3UserName': 'Auth_One', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                        {'snmpV3UserName': 'Auth_Two', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                        {'snmpV3UserName': 'Auth_Priv_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                                    ],
                                    'readCommunity': 'public',
                                    'v3Enabled': True,
                                    'enabled': True,
                                    'description': '',
                                    'category': 'snmp-configuration',
                                    'uri': ''}

snmpv3_Network_Admin_Users = {'type': 'snmp-configuration',
                              'trapDestinations': [],
                              'snmpAccess': ["192.168.2.0/24"],
                              'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                            {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                            {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}, ],
                              'readCommunity': 'public',
                              'v3Enabled': True,
                              'enabled': True,
                              'description': '',
                              'category': 'snmp-configuration',
                              'uri': ''}


snmpv3_Server_Admin_Users = {'type': 'snmp-configuration',
                             'trapDestinations': [],
                             'snmpAccess': ["192.168.2.0/24"],
                             'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}, ],
                             'readCommunity': 'public',
                             'v3Enabled': True,
                             'enabled': True,
                             'description': '',
                             'category': 'snmp-configuration',
                             'uri': ''}

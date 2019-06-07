def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]


ethernet_networks1 = [{'name': 'eth-101',
                       'type': 'ethernet-networkV4',
                       'vlanId': 0,
                       'purpose': 'General',
                       'smartLink': False,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'}]


uplink_sets_tbird = {'us1': {'name': 'Uplinkset1',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['eth-101'],
                             'primaryPort': None,
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'}, ]}, }


icmap_SE_Multi_LIG1 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                       {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'}]


enc_grp = [{'name': 'EG_SNMP',
            'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                                        {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
            'ipAddressingMode': 'DHCP',
            'ipRangeUris': None,
            'enclosureCount': 1,
            'osDeploymentSettings': {'manageOSDeployment': False, 'deploymentModeSettings': {'deploymentMode': 'None', 'deploymentNetworkUri': None}},
            'powerMode': 'RedundantPowerFeed'}]


les_tbird_SE_Multi_LIG = [{'name': 'LE',
                           'enclosureUris': ['ENC:RAVIENCL10'],
                           'enclosureGroupUri': 'EG:EG_SNMP',
                           'firmwareBaselineUri': None,
                           'forceInstallFirmware': False
                           }]


server_profiles_tbird_Multi_LIG = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'RAVIENCL10, bay 4', 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:RAVIENCL10', 'enclosureGroupUri': 'EG:EG',
                                    'name': 'SP_SNMP_ENC1_BAY4', 'description': '', 'affinity': 'Bay', 'boot': {'manageBoot': False},
                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 3:1-a',
                                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 3:2-a',
                                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''}]}]


uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               }


icmap_02 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'},

            ]
icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'}]


server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

# Tbird Data variables

error_lig = {'message': 'SNMP configuration has a User Name No_Auth_No_Priv which is already existing.', 'errorCode': 'CRM_SNMP_CONFIGURATION_DUPLICATE_USER_NAME'}
error_invalid_user = {'message': 'The user name for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_invalid_Auth_password = {'message': 'The authorization password for SNMPv3 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_AUTH_PWD_INVALID_FOR_POTASH'}
error_invalid_Priv_password = {'message': 'The privacy password for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_PRIV_PWD_INVALID_FOR_POTASH'}
error_Mandatory_Attribute_Check = {'message': 'SNMP configuration has a null or empty User Name.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
error_Maximum_No_of_users = {'message': 'There can be no more than 10 SNMPv3 users.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX'}
error_server_admin = {'message': 'Authorization error: User not authorized for this operation.', 'errorCode': 'AUTHORIZATION'}
error_missing_Parameter = {'message': 'Invalid JSON data type.', 'errorCode': 'INVALID_JSON_DATA_TYPE'}
error_user_name_missing_Parameter = {'message': 'SNMP configuration has a null or empty User Name.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
error_no_users = {'message': 'SNMP trap destination has a user which does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_wrong_user = {'message': 'The user Wrong_User_Name specified for the SNMPv3 trap destination does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_invalid_engine_id = {'message': 'The engine ID for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_ENGINEID'}
error_Maximum_No_of_Traps = {'message': 'The SNMP trap destinations cannot be added because the maximum number of 6 trap destinations has been exceeded.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_EXCEEDS_MAX'}
error_missing_auth_password = {'message': 'The credential type SHA256 is needed but not present.', 'errorCode': 'CRM_MISSING_CREDENTIAL_KEY'}
error_missing_priv_password = {'message': 'The credential type AES256 is needed but not present.', 'errorCode': 'CRM_MISSING_CREDENTIAL_KEY'}
error_invalid_length = {'message': 'The authorization password for SNMPv3 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_AUTH_PWD_LENGTH_INVALID'}
error_invalid_length = {'message': 'The user name for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_invalid_snmp_user_in_trap = {'message': 'The user User11 specified for the SNMPv3 trap destination does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_engineid_in_trap = {'message': 'The SNMPv3 trap destination has an engine ID and the notification type is trap.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_SHOULD_NOT_HAVE_ENGINEID'}
error_invalid_port = {'message': 'The port number for trap destination is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_PORTNO'}
error_missing_engineid = {'message': 'An engine ID is required for the SNMPv3 trap destination for inform.', 'errorCode': 'CRM_SNMP_CONFIGURATION_ENGINE_ID_MISSING'}


icmap_SE_Multi_LIG = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                      ]

# FIPS Data Variables
# LIG Variables
LIG_FIPS = 'LIG_FIPS'
FIPS_ligs_tbird_SE_Multi_LIG_Scenario = {'name': 'LIG_FIPS',
                                         'type': 'logical-interconnect-groupV4',
                                         'enclosureType': 'SY12000',
                                         'enclosureIndexes': [1],
                                         'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                                         'uplinkSets': [uplink_sets_tbird['us1']],
                                         'interconnectBaySet': 3,
                                         'redundancyType': 'Redundant',
                                         'ethernetSettings': None,
                                         'state': 'Active',
                                         'telemetryConfiguration': None,
                                         'snmpConfiguration': None}

OVF292_FIPS_ligs_AuthPriv_SHA256_AES128 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'category': 'snmp-configuration'}

OVF292_FIPS_ligs_AuthPriv_SHA256_AES192 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None
                                           }

OVF292_FIPS_ligs_AuthPriv_SHA256_AES256 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User3', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None}

OVF292_FIPS_ligs_AuthPriv_SHA384_AES128 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User4', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None
                                           }

OVF292_FIPS_ligs_AuthPriv_SHA384_AES192 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User5', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None}

OVF292_FIPS_ligs_AuthPriv_SHA384_AES256 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User6', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None}

OVF292_FIPS_ligs_AuthPriv_SHA512_AES128 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User7', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None}

OVF292_FIPS_ligs_AuthPriv_SHA512_AES192 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User8', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None}

OVF292_FIPS_ligs_AuthPriv_SHA512_AES256 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'User9', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'description': None,
                                           'category': 'snmp-configuration',
                                           'uri': None}

OVF292_FIPS_edit_snmp_user_no_engineid = {'type': 'snmp-configuration',
                                          'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                          'readCommunity': 'public',
                                          'systemContact': '',
                                          'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'userName': 'User1', 'inform': True, 'communityString': '', 'port': '162'}],
                                          'snmpAccess': [],
                                          'v3Enabled': True,
                                          'enabled': False,
                                          'description': None,
                                          'category': 'snmp-configuration',
                                          'uri': None}

OVF292_FIPS_add_trap_engineid = {'type': 'snmp-configuration',
                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'readCommunity': 'public',
                                 'systemContact': '',
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                       'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'engineId':'0x80001F888071F26C0ED6B8E15800000000', 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'v3Enabled': True,
                                 'enabled': False,
                                 'description': None,
                                 'category': 'snmp-configuration',
                                 'uri': None}

OVF292_FIPS_maximum_No_Of_traps = {'type': 'snmp-configuration',
                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                        {'trapDestination': '11.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                        {'trapDestination': '12.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                        {'trapDestination': '13.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                        {'trapDestination': '14.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                        {'trapDestination': '15.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                        {'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                   'snmpAccess': [],
                                   'v3Enabled': True,
                                   'enabled': False,
                                   'description': None,
                                   'category': 'snmp-configuration',
                                   'uri': None}

OVF292_FIPS_maximum_No_Of_Users = {'type': 'snmp-configuration',
                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User3', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User4', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User5', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User6', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User7', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User8', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User9', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User10', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                 {'snmpV3UserName': 'User11', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'trapDestinations': [],

                                   'snmpAccess': [],
                                   'v3Enabled': True,
                                   'enabled': False,
                                   'description': None,
                                   'category': 'snmp-configuration',
                                   'uri': None}

OVF292_FIPS_invalid_length_Auth_Phrase = {'type': 'snmp-configuration',
                                          'snmpUsers': [{'snmpV3UserName': '1234567890123456k7890l123h567890', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                          'readCommunity': 'public',
                                          'systemContact': '',
                                          'trapDestinations': [],
                                          'snmpAccess': [],
                                          'v3Enabled': True,
                                          'enabled': False,
                                          'description': None,
                                          'category': 'snmp-configuration',
                                          'uri': None}

OVF292_FIPS_Add_trap_invalid_user = {'type': 'snmp-configuration',
                                     'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                     'readCommunity': 'public',
                                     'systemContact': '',
                                     'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User11', 'inform':False, 'communityString':'', 'port':'162'}],
                                     'snmpAccess': [],
                                     'v3Enabled': True,
                                     'enabled': False,
                                     'description': None,
                                     'category': 'snmp-configuration',
                                     'uri': None}

OVF292_FIPS_missing_Auth_Pass_Phrase = {'type': 'snmp-configuration',
                                        'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                        'readCommunity': 'public',
                                        'systemContact': '',
                                        'trapDestinations': [],
                                        'snmpAccess': [],
                                        'v3Enabled': True,
                                        'enabled': False,
                                        'description': None,
                                        'category': 'snmp-configuration',
                                        'uri': None}

OVF292_FIPS_missing_Auth_Priv_Pass_Phrase = {'type': 'snmp-configuration',
                                             'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                             'readCommunity': 'public',
                                             'systemContact': '',
                                             'trapDestinations': [],
                                             'snmpAccess': [],
                                             'v3Enabled': True,
                                             'enabled': False,
                                             'description': None,
                                             'category': 'snmp-configuration',
                                             'uri': None}


OVF292_FIPS_missing_Auth_Phrase = {'type': 'snmp-configuration',
                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': '', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'trapDestinations': [],
                                   'snmpAccess': [],
                                   'v3Enabled': True,
                                   'enabled': False,
                                   'description': None,
                                   'category': 'snmp-configuration',
                                   'uri': None}

OVF292_FIPS_Invalidvalues_UserName = {'type': 'snmp-configuration',
                                      'snmpUsers': [{'snmpV3UserName': 'One_1212-nfn1213231323434434_****((((3$$$%%%', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                      'readCommunity': 'public',
                                      'systemContact': '',
                                      'trapDestinations': [],
                                      'snmpAccess': [],
                                      'v3Enabled': True,
                                      'enabled': False,
                                      'description': None,
                                      'category': 'snmp-configuration',
                                      'uri': None}


OVF292_FIPS_Invalidvalues_AuthPassPhrase = {'type': 'snmp-configuration',
                                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                            'readCommunity': 'public',
                                            'systemContact': '',
                                            'trapDestinations': [],
                                            'snmpAccess': [],
                                            'v3Enabled': True,
                                            'enabled': False,
                                            'description': None,
                                            'category': 'snmp-configuration',
                                            'uri': None}


OVF292_FIPS_Invalidvalues_Auth_Priv_Pass_Phrase = {'type': 'snmp-configuration',
                                                   'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                                   'readCommunity': 'public',
                                                   'systemContact': '',
                                                   'trapDestinations': [],
                                                   'snmpAccess': [],
                                                   'v3Enabled': True,
                                                   'enabled': False,
                                                   'description': None,
                                                   'category': 'snmp-configuration',
                                                   'uri': None}


OVF292_FIPS_invalid_engineid = {'type': 'snmp-configuration',
                                'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                'readCommunity': 'public',
                                'systemContact': '',
                                'trapDestinations': [{'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'engineId':'0xFFF', 'communityString':'', 'port':'162'}],
                                'snmpAccess': [],
                                'v3Enabled': True,
                                'enabled': False,
                                'description': None,
                                'category': 'snmp-configuration',
                                'uri': None}


OVF292_FIPS_invalid_format = {'type': 'snmp-configuration',
                              'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                              'readCommunity': 'public',
                              'systemContact': '',
                              'trapDestinations': [{'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv4', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                              'snmpAccess': [],
                              'v3Enabled': True,
                              'enabled': False,
                              'description': None,
                              'category': 'snmp-configuration',
                              'uri': None}

OVF292_FIPS_invalid_port = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                            'readCommunity': 'public',
                            'systemContact': '',
                            'trapDestinations': [{'trapDestination': '10.101.11.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'1620000'}],
                            'snmpAccess': [],
                            'v3Enabled': True,
                            'enabled': False,
                            'description': None,
                            'category': 'snmp-configuration',
                            'uri': None}

# LI Variables

edit_li_add_trap_destination = {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES128', 'userCredentials': None}],
                                'systemContact': 'None',
                                'v3Enabled': True,
                                'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                'snmpAccess': [],
                                'enabled': False,
                                'category': 'snmp-configuration',
                                'uri': None}

edit_li_add_trap_destination1 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination2 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination3 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination4 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination5 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination6 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination7 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_add_trap_destination8 = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'snmpUsers': [{'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                 'systemContact': 'None',
                                 'v3Enabled': True,
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None}

edit_li_no_engine_id = {'type': 'snmp-configuration',
                        'readCommunity': 'public',
                        'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}], 'readCommunity': 'public',
                        'systemContact': '',
                        'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'engineId':'', 'communityString':'', 'port':'162'}],
                        'snmpAccess': [],
                        'v3Enabled': True,
                        'enabled': False,
                        'category': 'snmp-configuration',
                        'uri': None}

edit_li_trap_engineid = {'type': 'snmp-configuration',
                         'readCommunity': 'public',
                         'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                         'readCommunity': 'public',
                         'systemContact': '',
                         'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'engineId':'0x80001F888071F26C0ED6B8E15800000000', 'communityString':'', 'port':'162'}],
                         'snmpAccess': [],
                         'enabled': False,
                         'v3Enabled': True,
                         'category': 'snmp-configuration',
                         'uri': None}


edit_li_max_trap = {'type': 'snmp-configuration',
                    'readCommunity': 'public',
                    'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                    'systemContact': '',
                    'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                         {'trapDestination': '11.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                         {'trapDestination': '12.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                         {'trapDestination': '13.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                         {'trapDestination': '14.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                         {'trapDestination': '15.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                         {'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],

                    'snmpAccess': [],
                    'enabled': False,
                    'v3Enabled': True,
                    'category': 'snmp-configuration',
                    'uri': None}

edit_li_max_users = {'type': 'snmp-configuration',
                     'readCommunity': 'public',
                     'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User3', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User4', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User5', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User6', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User7', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User8', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User9', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User10', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                   {'snmpV3UserName': 'User11', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                     'systemContact': '',
                     'trapDestinations': [],
                     'snmpAccess': [],
                     'enabled': False,
                     'v3Enabled': True,
                     'category': 'snmp-configuration',
                     'uri': None}

edit_li_length_validate = {'type': 'snmp-configuration',
                           'readCommunity': 'public',
                           'snmpUsers': [{'snmpV3UserName': '1234567890123456k7890l123h567890', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                           'systemContact': '',
                           'trapDestinations': [],
                           'snmpAccess': [],
                           'enabled': False,
                           'v3Enabled': True,
                           'category': 'snmp-configuration',
                           'uri': None}

edit_li_invalid_user_in_trap = {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                'systemContact': '',
                                'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User11', 'inform':False, 'communityString':'', 'port':'162'}],
                                'snmpAccess': [],
                                'enabled': False,
                                'v3Enabled': True,
                                'category': 'snmp-configuration',
                                'uri': None}

li_missing_Auth_Pass_Phrase = {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                               'systemContact': '',
                               'trapDestinations': [],
                               'snmpAccess': [],
                               'enabled': False,
                               'v3Enabled': True,
                               'category': 'snmp-configuration',
                               'uri': None}

li_missing_priv_Pass_Phrase = {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                               'systemContact': '',
                               'trapDestinations': [],
                               'snmpAccess': [],
                               'enabled': False,
                               'v3Enabled': True,
                               'category': 'snmp-configuration',
                               'uri': None}

li_missing_auth_Phrase = {'type': 'snmp-configuration',
                          'readCommunity': 'public',
                          'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': '', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                          'systemContact': '',
                          'trapDestinations': [],
                          'snmpAccess': [],
                          'enabled': False,
                          'v3Enabled': True,
                          'category': 'snmp-configuration',
                          'uri': None}

li_invalid_username = {'type': 'snmp-configuration',
                       'readCommunity': 'public',
                       'snmpUsers': [{'snmpV3UserName': 'One_1212-nfn1213231323434434_****((((3$$$%%%', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                       'systemContact': '',
                       'trapDestinations': [],
                       'snmpAccess': [],
                       'enabled': False,
                       'v3Enabled': True,
                       'category': 'snmp-configuration',
                       'uri': None}

edit_li_invalid_auth_pwd = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                            'readCommunity': 'public',
                            'systemContact': '',
                            'trapDestinations': [],
                            'snmpAccess': [],
                            'enabled': False,
                            'v3Enabled': True,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_li_invalid_priv_pwd = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                            'readCommunity': 'public',
                            'systemContact': '',
                            'trapDestinations': [],
                            'snmpAccess': [],
                            'enabled': False,
                            'v3Enabled': True,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_li_invalid_engineid = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                            'readCommunity': 'public',
                            'systemContact': '',
                            'trapDestinations': [{'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                  'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'engineId':'0xFFF', 'communityString':'', 'port':'162'}],
                            'snmpAccess': [],
                            'enabled': False,
                            'v3Enabled': True,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_li_invalid_format = {'type': 'snmp-configuration',
                          'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                          'readCommunity': 'public',
                          'systemContact': '',
                          'trapDestinations': [{'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv4', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                          'snmpAccess': [],
                          'enabled': False,
                          'v3Enabled': True,
                          'category': 'snmp-configuration',
                          'uri': None}

edit_li_invalid_port = {'type': 'snmp-configuration',
                        'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],  # {'snmpV3UserName':'Two','securityLevel':'Auth','userCredentials':[{'propertyName':'SnmpV3AuthorizationPassword','value':'*()!@#$%&^*'}],'v3AuthProtocol':'MD5','v3PrivacyProtocol':'NA'},
                        'readCommunity': 'public',
                        'systemContact': '',
                        'trapDestinations': [{'trapDestination': '10.101.11.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                              'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'1620000'}],
                        'snmpAccess': [],
                        'enabled': False,
                        'v3Enabled': True,
                        'category': 'snmp-configuration',
                        'uri': None}

# Update from Group variables

edit_lig_UFG_LI_Add_User = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                          {'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                            'trapDestinations': [],
                            'snmpAccess': [],
                            'v3Enabled': True,
                            'enabled': False,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_lig_UFG_LI_Add_trap = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                          {'snmpV3UserName': 'User2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                            'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],
                            'snmpAccess': [],
                            'v3Enabled': True,
                            'enabled': False,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_lig_UFG_LI_edit_User_Auth = {'type': 'snmp-configuration',
                                  'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                                {'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                {'snmpV3UserName': 'User3', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                {'snmpV3UserName': 'User4', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                  'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User2', 'inform':False, 'communityString':'', 'port':'162'}],
                                  'snmpAccess': [],
                                  'v3Enabled': True,
                                  'enabled': False,
                                  'category': 'snmp-configuration',
                                              'uri': None}

edit_lig_UFG_LI_edit_User_AuthPriv = {'type': 'snmp-configuration',
                                      'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                                    {'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'User3', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'User4', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'User5', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'User6', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'User7', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}, ],
                                      'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User3', 'inform':False, 'communityString':'', 'port':'162'}],
                                      'snmpAccess': [],
                                      'v3Enabled': True,
                                      'enabled': False,
                                      'category': 'snmp-configuration',
                                      'uri': None}

edit_li_UFG_LI_edit_User_Auth = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'systemContact': '',
                                 'v3Enabled': True,
                                 'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                               {'snmpV3UserName': 'User2', 'v3AuthProtocol': 'SH384', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'User3', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'User4', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'User5', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'User6', 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'User7', 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}, ],
                                 'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':False, 'communityString':'', 'port':'162', 'engineId': None}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration',
                                 'uri': None
                                 }

edit_li_UFG_LI_Remove_Users = {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'snmpUsers': [],
                               'systemContact': 'None',
                               'v3Enabled': True,
                               'trapDestinations': [],
                               'snmpAccess': [],
                               'enabled': False,
                               'category': 'snmp-configuration',
                               'uri': None}

Password_Length_Check = {'type': 'snmp-configuration',
                         'trapDestinations': [],
                         'snmpAccess': ["192.168.2.0/24"],
                         'snmpUsers': [{'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '******'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192'}, ],
                         'readCommunity': 'public',
                         'v3Enabled': True,
                         'enabled': True,
                         'description': '',
                         'category': 'snmp-configuration',
                         'uri': ''}

Mandatory_Attribute_Check_Auth_Priv_PassPhrase = {'type': 'snmp-configuration',
                                                  'trapDestinations': [],
                                                  'snmpAccess': ["192.168.2.0/24"],
                                                  'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'}],
                                                  'readCommunity': 'public',
                                                  'v3Enabled': True,
                                                  'enabled': True,
                                                  'description': '',
                                                  'category': 'snmp-configuration',
                                                  'uri': ''}

Mandatory_Attribute_Check_AuthPassPhrase = {'type': 'snmp-configuration',
                                            'trapDestinations': [],
                                            'snmpAccess': ["192.168.2.0/24"],
                                            'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '$'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'NA'}, ],
                                            'readCommunity': 'public',
                                            'v3Enabled': True,
                                            'enabled': True,
                                            'description': '',
                                            'category': 'snmp-configuration',
                                            'uri': ''}

Mandatory_Attribute_Check_Authlgo = {'type': 'snmp-configuration',
                                     'trapDestinations': [],
                                     'snmpAccess': ["192.168.2.0/24"],
                                     'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA'}, ],
                                     'readCommunity': 'public',
                                     'v3Enabled': True,
                                     'enabled': True,
                                     'description': '',
                                     'category': 'snmp-configuration',
                                     'uri': ''}

Mandatory_Attribute_Check_Name = {'type': 'snmp-configuration',
                                  'trapDestinations': [],
                                  'snmpAccess': ["192.168.2.0/24"],
                                  'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                  'readCommunity': 'public',
                                  'v3Enabled': True,
                                  'enabled': True,
                                  'description': '',
                                  'category': 'snmp-configuration',
                                  'uri': ''}

import os
import sys
import paramiko
import time
import re


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


def file_exists(file_path):
    file = os.path.exists('file_path')


def removefile(file_path):
    file = os.remove('file_path')


def Remove_Whitespace(instring):
    return instring.strip()

LE_name = 'LE'
LIGname = 'LIG1'
LI = 'LE-LIG1'
POWER_OFF = 'Off'
POWER_ON = 'On'
RESET = 'Reset'
POWER_STATE = '/powerState'
RESET_STATE = '/deviceResetState'
IC_CONFIG_STATE = 'Configured'
IC_CONFIG_ERROR_STATE = 'Configuration error'
IC_ABSENT_STATE = 'Absent'
IC_MAINTENANCE_STATE = 'Maintenance'
ENC1 = 'SGH734VBE6'
HOST = '192.168.145.60'
Efuse_sleep_time = '500'
Efuse_Action = ['EFuseOn', 'EFuseOff']
Bay_No = '2'
EM_SN = ENC1
INTERCONNECTS = [ENC1 + ', interconnect 2']
INTERCONNECTS1 = [ENC1 + ', interconnect 5']
error_path_value = {'message': 'The value false for /sendTestTrap is invalid.', 'errorCode': 'CRM_INVALID_PATCH_REQUEST'}
error_trapdestination_missing = {'message': 'SNMP configuration contains a trap destination with a null or empty destination IP address.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_IP_MISSING'}
SERVER_BAY = ENC1 + ', bay 1'
Upload_Sleep_Time = '4200'
ic_firmwareVersion_old = '2.0.0.66'
ic_firmwareVersion_new = '2.0.0.69'
ic_firmwareVersion_old_unsupported = '1.1.0.6'
old_SPP_bundle = 'Cust-K130-43-EM202-Dev-G10.iso'
old_SPP_bundle_name = 'Cust-K130-43-EM202-Dev-G10'
latest_SPP_bundle = 'Cust-K130-rc5-N200-69D-EM204-G10.iso'
latest_SPP_bundle_name = 'Cust-K130-rc5-N200-69D-EM204-G10'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

li_body = [{'op': 'replace',
            'path': '/sendTestTrap',
            'value': 'true'}]

li_body1 = [{'op': 'replace',
             'path': '/sendTestTrap',
             'value': 'false'}]

liupdate_body = {"sppUri": '',
                 "command": "UPDATE",
                 "force": True,
                 "ethernetActivationType": "Parallel",
                 "ethernetActivationDelay": "0",
                 "fcActivationType": "Parallel",
                 "fcActivationDelay": "0",
                 "validationType": "None"}

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
                             'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'},
                                                        {'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'}, ]}, }


icmap_SE_Multi_LIG1 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy'},
                       {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy'}

                       ]

ligs_tbird_SE_Multi_LIG = {'type': 'snmp-configuration',
                           'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA'},
                                         {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128'},
                                         {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES192'},
                                         {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'},
                                         {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'TDEA'},
                                         {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'TDEA'},
                                         {'snmpV3UserName': 'User7', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                           'readCommunity': 'public',
                           'systemContact': '',
                           'trapDestinations': [],
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


ligs_tbird_SE_Multi_LIG_All_Users = {'name': 'LIG1',
                                     'type': 'logical-interconnect-groupV6',
                                     'enclosureType': 'SY12000',
                                     'enclosureIndexes': [1],
                                     'interconnectMapTemplate': icmap_SE_Multi_LIG1,
                                     'uplinkSets': [],
                                     'interconnectBaySet': 2,
                                     'redundancyType': 'Redundant',
                                     'ethernetSettings': None,
                                     'state': 'Active',
                                     'telemetryConfiguration': None,
                                     'snmpConfiguration': None}

ligs_tbird_SE_Multi_LIG_Scenario = {'name': 'LIG_New',
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


add_snmp_users_six_combinations = {'type': 'snmp-configuration',
                                   'snmpUsers': [
                                       {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                       {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                       {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                                       {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'}, ],
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'11650'}],
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

add_snmp_users_six_combinations_fips = {'type': 'snmp-configuration',
                                        'snmpUsers': [
                                            {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                            {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                            {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                                            {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'}, ],
                                        'readCommunity': 'public',
                                        'systemContact': '',
                                        'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User8', 'inform':False, 'communityString':'', 'port':'11650'}],
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
li_snmp_trap = {'type': 'snmp-configuration',
                'snmpUsers': [
                    {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                    {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'},
                    {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                    {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'}, ],
                'readCommunity': 'public',
                'systemContact': '',
                'trapDestinations': [{'trapDestination': [], 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'11650'}],
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

edit_ligs_tbird_SE_Multi_LIG_All_Users = {'type': 'snmp-configuration',
                                          'snmpUsers': [
                                              {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                              {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'TDEA'},
                                              {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                              {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES192'},
                                              {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'},
                                              {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'DES56'},
                                              {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'TDEA'},
                                              {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES128'},
                                              {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192'}, ],
                                          'readCommunity': 'public',
                                          'systemContact': '',
                                          'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'11650'}],
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


enc_grp = [{'name': 'EG_SNMP',
            'interconnectBayMappings': [{'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                                        {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'}],
            'ipAddressingMode': 'DHCP',
            'ipRangeUris': None,
            'enclosureCount': 1,
            'osDeploymentSettings': {'manageOSDeployment': False, 'deploymentModeSettings': {'deploymentMode': 'None', 'deploymentNetworkUri': None}},
            'powerMode': 'RedundantPowerFeed'}]


les_tbird_SE_Multi_LIG = [{'name': 'LE',
                           'enclosureUris': ['ENC:SGH734VBE6'],
                           'enclosureGroupUri': 'EG:EG_SNMP',
                           'firmwareBaselineUri': None,
                           'forceInstallFirmware': False
                           }]


server_profiles_tbird_Multi_LIG = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'EM1FFFF500, bay 4', 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:EM1FFFF500', 'enclosureGroupUri': 'EG:EG_SNMP',
                                    'name': 'SP_SNMP_ENC1_BAY4', 'description': '', 'affinity': 'Bay', 'boot': {'manageBoot': False},
                                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'mezz 3:1-a',
                                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''},
                                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'mezz 3:2-a',
                                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'wwpn': '', 'wwnn': ''}]}]


#  Edit LI E2E Flow


edit_li_add_trap_destination_tbird = {'type': 'snmp-configuration',
                                      'readCommunity': 'public',
                                      'snmpUsers': [{'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                    {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'},
                                                    {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                                                    {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'}, ],
                                      'systemContact': 'None',
                                      'v3Enabled': True,
                                      'trapDestinations': [{'trapDestination': '', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'11650'}],
                                      'snmpAccess': [],
                                      'enabled': False,
                                      'category': 'snmp-configuration',
                                      'uri': None}

edit_li_add_trap_destination_tbird_FIPS = {'type': 'snmp-configuration',
                                           'readCommunity': 'public',
                                           'snmpUsers': [{'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}, ],
                                           'systemContact': 'None',
                                           'v3Enabled': True,
                                           'trapDestinations': [{'trapDestination': '', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User8', 'inform':False, 'communityString':'', 'port':'11650'}],
                                           'snmpAccess': [],
                                           'enabled': False,
                                           'category': 'snmp-configuration',
                                           'uri': None}

edit_li_with_auth_priv_users_old = {'snmpConfiguration':
                                    {'type': 'snmp-configuration',
                                     'readCommunity': 'public',

                                     'snmpUsers': [],
                                     'systemContact': 'None',
                                     'v3Enabled': True,
                                     'trapDestinations': [],
                                     'snmpAccess': [],
                                     'enabled': False,
                                     'category': 'snmp-configuration',
                                     'uri': None}
                                    }

edit_li_with_auth_priv_users = {'type': 'snmp-configuration',
                                'readCommunity': 'public',
                                'snmpUsers': [
                                    {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                    {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                    {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                                    {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'}, ],
                                'systemContact': 'None',
                                'v3Enabled': True,
                                'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User7', 'inform':False, 'communityString':'', 'port':'11650'}],
                                'snmpAccess': [],
                                'enabled': True,
                                'category': 'snmp-configuration',
                                'uri': None}

edit_li_with_auth_priv_users_fips = {'type': 'snmp-configuration',
                                     'readCommunity': 'public',
                                     'snmpUsers': [
                                         {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}, ],
                                     'systemContact': 'None',
                                     'v3Enabled': True,
                                     'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User8', 'inform':False, 'communityString':'', 'port':'11650'}],
                                     'snmpAccess': [],
                                     'enabled': True,
                                     'category': 'snmp-configuration',
                                     'uri': None}

edit_li_with_auth_priv_users_inform = {'type': 'snmp-configuration',
                                       'readCommunity': 'public',
                                       'snmpUsers': [
                                           {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                           {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'TDEA'},
                                           {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'},
                                           {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES192'},
                                           {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES256'},
                                           {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'DES56'},
                                           {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'TDEA'},
                                           {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128'},
                                           {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                                           {'snmpV3UserName': 'User10', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                       'systemContact': 'None',
                                       'v3Enabled': True,
                                       'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'engineId':'0x8000000b035cb90147ba60', 'communityString':'', 'port':'162'}],
                                       'snmpAccess': [],
                                       'enabled': False,
                                       'category': 'snmp-configuration',
                                       'uri': None}


edit_li_with_auth_priv_users_inform1 = {'type': 'snmp-configuration',
                                        'readCommunity': 'public',
                                        'snmpUsers': [
                                            {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                            {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'TDEA'},
                                            {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'},
                                            {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES192'},
                                            {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES256'},
                                            {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'DES56'},
                                            {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'TDEA'},
                                            {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES128'},
                                            {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},
                                            {'snmpV3UserName': 'User10', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES256'}],
                                        'systemContact': 'None',
                                        'v3Enabled': True,
                                        'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'communityString':'', 'port':'162'}],
                                        'snmpAccess': [],
                                        'enabled': False,
                                        'category': 'snmp-configuration',
                                        'uri': None}


encREAL = [{'hostname': '10.10.2.11', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EGLldp', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]

encs = encREAL
LIG1 = 'LIG1'
LIG_New = 'LIG_New'
# LE = 'SGH411DFYA'

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

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
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'}]

icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
         ]


server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

server_profiles1 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC2', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     ]},

                    ]


ligs_snmp = {'lig1':
             {'name': 'LIG_SNMP1',
              'type': 'logical-interconnect-groupV300',
              'enclosureType': 'C7000',
              'interconnectMapTemplate': icmap,

              'uplinkSets': [],
              'stackingMode': 'Enclosure',
              'ethernetSettings': None,
              'state': 'Active',
              'telemetryConfiguration': None,
              'snmpConfiguration': {'type': 'snmp-configuration',
                                    'trapDestinations': [{'trapDestination': '10.10.3.71',
                                                          'trapFormat': 'SNMPv3',
                                                          'trapSeverities': [],
                                                          'vcmTrapCategories':[],
                                                          'enetTrapCategories':[],
                                                          'fcTrapCategories':[],
                                                          'port':'162',
                                                          'inform': False,
                                                          'securityLevel':'NoAuthNoPrivacy',
                                                          'userName':'TEST6'}],
                                    'snmpAccess': [],
                                    'readCommunity': 'public',

                                    'snmpUsers': [{'userType': 'LOCAL',
                                                   'engineId': '',
                                                   'minimumv3SecurityLevel': 'NoAuthNoPrivacy',
                                                   'snmpV3UserName': 'TEST6',
                                                   'v3AuthProtocol': 'NA',
                                                   'v3PrivacyProtocol': 'NA',
                                                   'userCredentials': [],
                                                   'securityLevel':'NoAuthNoPrivacy'}],
                                    'v3Enabled': True,
                                    'enabled': True,
                                    'category': 'snmp-configuration',
                                    }}, }


edit_ligs_snmp = {'lig1':
                  {'name': ' LIG_SNMP3',
                   'type': 'logical-interconnect-groupV300',
                   'enclosureType': 'C7000',
                   'interconnectMapTemplate': icmap,

                   'uplinkSets': [],
                   'stackingMode': 'Enclosure',
                   'ethernetSettings': None,
                   'state': 'Active',
                   'telemetryConfiguration': None,
                   'snmpConfiguration': {'type': 'snmp-configuration',
                                         'trapDestinations': [{
                                             'communityString': 'public',
                                             'securityLevel': ' ',
                                             'engineId': ' ',
                                             'trapSeverities': ['Major', 'Critical'],
                                             'enetTrapCategories': ['PortStatus'],
                                             'fcTrapCategories': [],
                                             'vcmTrapCategories': [],
                                             'trapFormat': 'SNMPv1',
                                             'trapDestination': '15.212.161.102',
                                                                'inform': False,
                                                                'userName': 'TEST7',
                                                                'port': '163'
                                         }],
                                         'snmpAccess': [],
                                         'readCommunity': 'public',
                                         'snmpUsers': [{'userType': 'LOCAL',
                                                        'engineId': '',
                                                        'minimumv3SecurityLevel': 'NoAuthNoPrivacy',
                                                        'snmpV3UserName': 'TEST7',
                                                        'v3AuthProtocol': 'NA',
                                                        'v3PrivacyProtocol': 'NA',
                                                        'userCredentials': [],
                                                        'securityLevel':'NoAuthNoPrivacy'}],
                                         'v3Enabled': True,
                                         'enabled': True,
                                         'category': 'snmp-configuration',
                                         }, }}

icmap_snmp = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'}
              ]

icmap_snmp2 = [
    {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'}
]

edit_snmp_lig = {'lig1':
                 {'name': 'LIG1',
                  'type': 'logical-interconnect-groupV300',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': icmap_snmp,

                  'uplinkSets': [],
                  'stackingMode': 'Enclosure',

                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': {'type': 'snmp-configuration',
                                        'trapDestinations': [{"enetTrapCategories": [], "vcmTrapCategories": [], "trapFormat": "SNMPv3", "communityString": "public", "fcTrapCategories": [], "trapDestination": "10.10.3.72", "trapSeverities": []}],
                                        'snmpAccess': ["192.168.2.0/24"],
                                        'snmpUsers': [{'userType': 'LOCAL', 'engineId': '', 'minimumv3SecurityLevel': 'NoAuthNoPrivacy', 'snmpV3UserName': 'Local_NoAuthNoPriv', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [], 'securityLevel':'NoAuthNoPrivacy'}],

                                        'readCommunity': 'public',
                                        'v3Enabled': True,
                                        'enabled': False,
                                        'description': '',
                                        'category': 'snmp-configuration',
                                        'uri': ''}
                  }
                 }

ENCLOSURE_IP = '10.10.1.223'

enclosure_credentials = {'userName': 'Administrator', 'password': 'Admin'}

Preview_uri = '/rest/enclosure-preview'

Preview_body = {"hostname": ENCLOSURE_IP, "username": enclosure_credentials['userName'], "password": enclosure_credentials['password'], "ligPrefix": "LIG_SNMP1", "force": True, "logicalInterconnectGroupNeeded": True}


li_snmp_add_Access1 = {'type': 'snmp-configuration', 'v3Enabled': True, 'snmpUsers': [], 'trapDestinations': [], 'snmpAccess': [], 'enabled': False, 'category': 'snmp-configuration', 'uri': None}
li_snmp_add_user = {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'snmpUsers': [{'snmpV3UserName': 'Seven', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}], 'trapDestinations': [], 'snmpAccess': ['192.168.2.0/24', '192.168.147.3/24'], 'v3Enabled': True, 'enabled': True, 'category': 'snmp-configuration'}


#  Tbird Data variables

# error_lig = {'message': 'SNMP configuration has a User Name No_Auth_No_Priv which is already existing.', 'errorCode': 'CRM_SNMP_CONFIGURATION_DUPLICATE_USER_NAME'}
# error_invalid_user = {'message': 'SNMP configuration has a Username which exceeds 31 characters.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_EXCEEDS_MAX'}
# error_invalid_Auth_password = {'message': 'SNMP configuration has an Authentication Password which has an invalid length.', 'errorCode': 'CRM_SNMP_CONFIGURATION_AUTH_PWD_LENGTH_INVALID'}
# error_invalid_Priv_password = {'message': 'SNMP configuration has an Privacy Password which has an invalid length.', 'errorCode': 'CRM_SNMP_CONFIGURATION_PRIV_PWD_LENGTH_INVALID'}
# error_Mandatory_Attribute_Check = {'message': 'SNMP configuration has a null or empty User Name.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
# error_Maximum_No_of_users = {'message': 'The SNMP users cannot be added because the maximum number of 6 users has been exceeded.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX'}
# error_server_admin = {'message': 'Authorization error: User not authorized for this operation.', 'errorCode': 'AUTHORIZATION'}
# error_missing_Parameter = {'message': 'Invalid JSON data type.', 'errorCode': 'INVALID_JSON_DATA_TYPE'}
# error_user_name_missing_Parameter = {'message': 'SNMP configuration has a null or empty User Name.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
# error_no_users = {'message': 'SNMP trap destination has a user which does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
# error_wrong_user = {'message': 'The user Wrong_User_Name specified for the SNMPv3 trap destination 192.168.144.167 does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
# error_invalid_engine_id = {'message': 'The engine ID for SNMPv3 trap destination 192.168.144.167 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_ENGINEID'}
# error_Maximum_No_of_Traps = {'message': 'The SNMP trap destinations cannot be added because the maximum number of 6 trap destinations has been exceeded.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_EXCEEDS_MAX'}


icmap_SE_Multi_LIG = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                      {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy'},
                      ]
ligs_tbird_SE_Multi_LIG_No_Name = {'type': 'snmp-configuration',

                                   'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'trapDestinations': [],
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


ligs_tbird_SE_Multi_LIG_AuthprotocolMD5 = {'type': 'snmp-configuration',
                                           'snmpUsers': [{'snmpV3UserName': 'Auth_MD5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],
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


ligs_tbird_SE_Multi_LIG_AuthprotocolSHA1 = {'type': 'snmp-configuration',
                                            'snmpUsers': [{'snmpV3UserName': 'Auth_SHA1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                            'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [], 'snmpAccess': [], 'v3Enabled': True, 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None
                                            }


ligs_tbird_SE_Multi_LIG_AuthprotocolSHA2 = {'type': 'snmp-configuration',
                                            'snmpUsers': [{'snmpV3UserName': 'Auth_SHA256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'}],
                                            'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [], 'snmpAccess': [], 'v3Enabled': True, 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None}


ligs_tbird_SE_Multi_LIG_Authprotocol_SHA1_DES = {'type': 'snmp-configuration',
                                                 'snmpUsers': [{'snmpV3UserName': 'Auth_Priv', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'}],
                                                 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [], 'snmpAccess': [], 'v3Enabled': True, 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None}


ligs_tbird_SE_Multi_LIG_Authprotocol_SHA1_AES128 = {'type': 'snmp-configuration',
                                                    'snmpUsers': [{'snmpV3UserName': 'Auth_Priv', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                                    'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [], 'snmpAccess': [], 'v3Enabled': True, 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None}


ligs_tbird_SE_Multi_LIG_Authprotocol_SHA2_AES192 = {'type': 'snmp-configuration',
                                                    'snmpUsers': [{'snmpV3UserName': 'Auth_Priv', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'AES192'}],
                                                    'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [], 'snmpAccess': [], 'v3Enabled': True, 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None}


ligs_tbird_SE_Multi_LIG_Authprotocol_SHA2_AES256 = {'type': 'snmp-configuration',
                                                    'snmpUsers': [{'snmpV3UserName': 'Auth_Priv', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'AES256'}],
                                                    'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [], 'snmpAccess': [], 'v3Enabled': True, 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None}


lig_tbird_edit_snmp_user_duplicate_error = {'type': 'snmp-configuration',
                                            'trapDestinations': [],
                                            'snmpUsers': [
                                                {'snmpV3UserName': 'No_Auth_No_Priv', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                {'snmpV3UserName': 'No_Auth_No_Priv', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}
                                            ],
                                            'readCommunity': 'public',
                                            'v3Enabled': True,
                                            'enabled': True,
                                            'description': '',
                                            'category': 'snmp-configuration',
                                            'uri': ''}


lig_tbird_Invalidvalues_UserName = {'type': 'snmp-configuration',
                                    'trapDestinations': [],
                                    'snmpUsers': [
                                        {'snmpV3UserName': 'One_1212-nfn1213231323434434_****((((3$$$%%%', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                    ],
                                    'readCommunity': 'public',
                                    'v3Enabled': True,
                                    'enabled': True,
                                    'description': '',
                                    'category': 'snmp-configuration',
                                    'uri': ''}


lig_tbird_Invalidvalues_AuthPassPhrase = {'type': 'snmp-configuration',
                                          'trapDestinations': [],
                                          'snmpUsers': [

                                              {'snmpV3UserName': 'Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ' '}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

                                          ],
                                          'readCommunity': 'public',
                                          'v3Enabled': True,
                                          'enabled': True,
                                          'description': '',
                                          'category': 'snmp-configuration',
                                          'uri': ''}


lig_tbird_Invalidvalues_Auth_Priv_Pass_Phrase = {'type': 'snmp-configuration',
                                                 'trapDestinations': [],
                                                 'snmpUsers': [
                                                     {'snmpV3UserName': '5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '*'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'}
                                                 ],
                                                 'readCommunity': 'public',
                                                 'v3Enabled': True,
                                                 'enabled': True,
                                                 'description': '',
                                                 'category': 'snmp-configuration',
                                                 'uri': ''}


lig_tbird_Mandatory_Attribute_Check_Name = {'type': 'snmp-configuration',
                                            'trapDestinations': [],
                                            'snmpUsers': [{'snmpV3UserName': '', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                                            'readCommunity': 'public',
                                            'v3Enabled': True,
                                            'enabled': True,
                                            'description': '',
                                            'category': 'snmp-configuration',
                                            'uri': ''}


lig_tbird_Mandatory_Attribute_Check_Authlgo = {'type': 'snmp-configuration',
                                               'trapDestinations': [],
                                               'snmpUsers': [

                                                   {'snmpV3UserName': '', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

                                               ],
                                               'readCommunity': 'public',
                                               'v3Enabled': True,
                                               'enabled': True,
                                               'description': '',
                                               'category': 'snmp-configuration',
                                               'uri': ''}

lig_tbird_Mandatory_Attribute_Check_AuthPassPhrase = {'type': 'snmp-configuration',
                                                      'trapDestinations': [],

                                                      'snmpUsers': [

                                                          {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '$'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

                                                      ],
                                                      'readCommunity': 'public',
                                                      'v3Enabled': True,
                                                      'enabled': True,
                                                      'description': '',
                                                      'category': 'snmp-configuration',
                                                      'uri': ''}


lig_tbird_Mandatory_Attribute_Check_Auth_Priv_PassPhrase = {
    'snmpConfiguration': {'type': 'snmp-configuration',
                          'trapDestinations': [],
                          'snmpUsers': [
                              {'snmpV3UserName': '', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': ''}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                          ],
                          'readCommunity': 'public',
                          'v3Enabled': True,
                          'enabled': True,
                          'description': '',
                          'category': 'snmp-configuration',
                          'uri': ''}
}

lig_tbird_Password_Length_Check = {
    'snmpConfiguration': {'type': 'snmp-configuration',
                          'trapDestinations': [],
                          'snmpUsers': [
                              {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '******'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '*'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                          ],
                          'readCommunity': 'public',
                          'v3Enabled': True,
                          'enabled': True,
                          'description': '',
                          'category': 'snmp-configuration',
                          'uri': ''}
}


lig_tbird_Maximum_No_Of_Users = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'trapDestinations': [],
                                                       'snmpUsers': [
                                                           {'snmpV3UserName': 'User1', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                           {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                           {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                           {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                                                           {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'DES56'},
                                                           {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'AES128'},
                                                           {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}
                                                       ],
                                                       'readCommunity': 'public',
                                                       'v3Enabled': True,
                                                       'enabled': True,
                                                       'description': '',
                                                       'category': 'snmp-configuration',
                                                       'uri': ''}
                                 }


lig_tbird_Network_Admin_Users = {'lig1':
                                 {'name': 'LIG_Network_Admin1',
                                  'type': 'logical-interconnect-groupV300',
                                  'enclosureType': 'SY12000',
                                  'interconnectMapTemplate': icmap_SE_Multi_LIG1,

                                  'uplinkSets': [],
                                     'stackingMode': 'Enclosure',
                                     'interconnectBaySet': 2,
                                     'redundancyType': 'Redundant',

                                     'ethernetSettings': None,
                                     'state': 'Active',
                                     'telemetryConfiguration': None,
                                  'snmpConfiguration': {'type': 'snmp-configuration',
                                                        'trapDestinations': [],

                                                        'snmpUsers': [
                                                            {'snmpV3UserName': 'User1', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},
                                                            {'snmpV3UserName': 'User2', 'securityLevel': 'Auth', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User3', 'securityLevel': 'Auth', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User4', 'securityLevel': 'Auth', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                                                            {'snmpV3UserName': 'User5', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                                            {'snmpV3UserName': 'User6', 'securityLevel': 'AuthPrivacy', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},

                                                        ],
                                                        'readCommunity': 'public',
                                                        'v3Enabled': True,
                                                        'enabled': True,
                                                        'description': '',
                                                        'category': 'snmp-configuration',
                                                        'uri': ''}
                                  }
                                 }

lig_tbird_Server_Admin_Users = {'lig1':
                                {'name': 'LIG_Server_Admin1',
                                 'type': 'logical-interconnect-groupV300',
                                 'enclosureType': 'SY12000',
                                 'interconnectMapTemplate': icmap_SE_Multi_LIG1,

                                 'uplinkSets': [],
                                 'stackingMode': 'Enclosure',
                                 'interconnectBaySet': 2,
                                 'redundancyType': 'Redundant',

                                 'ethernetSettings': None,
                                 'state': 'Active',
                                 'telemetryConfiguration': None,
                                 'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'trapDestinations': [],

                                                       'snmpUsers': [
                                                           {'snmpV3UserName': 'User1', 'securityLevel': 'NoAuthNoPrivacy', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'},

                                                       ],
                                                       'readCommunity': 'public',
                                                       'v3Enabled': True,
                                                       'enabled': True,
                                                       'description': '',
                                                       'category': 'snmp-configuration',
                                                       'uri': ''}
                                 }
                                }


lig_tbird_add_lig_snmp_users = {
    'snmpConfiguration': {'type': 'snmp-configuration',
                          'trapDestinations': [],
                          'snmpUsers': [
                              {'snmpV3UserName': 'Auth_Modified_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                              {'snmpV3UserName': 'Auth_Modified_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                              {'snmpV3UserName': 'Auth_Modified_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                              {'snmpV3UserName': 'Auth_Priv_Modified_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                              {'snmpV3UserName': 'Auth_Priv_Modified_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                          ],
                          'readCommunity': 'public',
                          'v3Enabled': True,
                          'enabled': True,
                          'description': '',
                          'category': 'snmp-configuration',
                          'uri': ''}
}


lig_tbird_edit_lig_snmp_users = {
    'snmpConfiguration': {'type': 'snmp-configuration',
                          'trapDestinations': [],
                          'snmpUsers': [
                              {'snmpV3UserName': 'Auth_Modified_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                              {'snmpV3UserName': 'Auth_Modified_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                              {'snmpV3UserName': 'Auth_Modified_Three', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}], 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA'},
                              {'snmpV3UserName': 'Auth_Priv_Modified_One', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                              {'snmpV3UserName': 'Auth_Priv_Modified_Two', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123'}], 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'}
                          ],
                          'readCommunity': 'public',
                          'v3Enabled': True,
                          'enabled': True,
                          'description': '',
                          'category': 'snmp-configuration',
                          'uri': ''}
}


edit_li_tbird_nopriv = {'snmpConfiguration':
                        {
                            'type': 'snmp-configuration',
                            'readCommunity': 'public',
                            'systemContact': '',
                            'v3Enabled': True,
                            'snmpUsers': [{'snmpV3UserName': 'Two',
                                           'securityLevel': 'NoAuthNoPrivacy',
                                           'userCredentials': [],
                                           'v3AuthProtocol':'NA',
                                           'v3PrivacyProtocol':'NA'},
                                          {'snmpV3UserName': 'One1',
                                           'securityLevel': 'Auth',
                                              'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'Password@123456', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'NA'},
                                          {'snmpV3UserName': 'Three',
                                           'securityLevel': 'AuthPrivacy',
                                              'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'Password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'Password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'MD5',
                                           'v3PrivacyProtocol': 'DES56'}],
                            'trapDestinations': [],
                            'snmpAccess': [],
                            'enabled': False,
                            'description': None,
                            'category': 'snmp-configuration',
                            'uri': None
                        }
                        }


edit_li_add_trap_destination = {'type': 'snmp-configuration',
                                'readCommunity': '',
                                'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                'systemContact': 'None',
                                'v3Enabled': True,
                                'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':False, 'communityString':'', 'port':'163'}],
                                'snmpAccess': [],
                                'enabled': False,
                                'category': 'snmp-configuration',
                                'uri': None}

edit_li_add_trap_remove_user = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                      'readCommunity': 'public',
                                                      'snmpUsers': [],
                                                      'systemContact': 'None',
                                                      'v3Enabled': True,
                                                      'trapDestinations': [],
                                                      'snmpAccess': [],
                                                      'enabled': False,
                                                      'category': 'snmp-configuration',
                                                      'uri': None}}


edit_li_add_trap_no_user = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'readCommunity': 'public',
                                                  'snmpUsers': [],
                                                  'systemContact': 'None',
                                                  'v3Enabled': True,
                                                  'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'Wrong_User_Name', 'inform':False, 'communityString':'', 'port':'162'}],
                                                  'snmpAccess': [],
                                                  'enabled': False,
                                                  'category': 'snmp-configuration',
                                                  'uri': None}}


edit_li_add_trap_type_inform = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                      'readCommunity': 'public',
                                                      'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                      'systemContact': 'None',
                                                      'v3Enabled': True,
                                                      'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'163'}],
                                                      'snmpAccess': [],
                                                      'enabled': False,
                                                      'category': 'snmp-configuration',
                                                      'uri': None
                                                      }}


edit_li_add_trap_no_engine_id = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'readCommunity': 'public',
                                                       'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                       'systemContact': 'None',
                                                       'v3Enabled': True,
                                                       'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':' ', 'communityString':'', 'port':'163'}],
                                                       'snmpAccess': [],
                                                       'enabled': False,
                                                       'category': 'snmp-configuration',
                                                       'uri': None
                                                       }}


edit_li_add_trap_non_default_port = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                           'readCommunity': 'public',
                                                           'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                           'systemContact': 'None',
                                                           'v3Enabled': True,
                                                           'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'}],
                                                           'snmpAccess': [],
                                                           'enabled': False,
                                                           'category': 'snmp-configuration',
                                                           'uri': None
                                                           }}


edit_li_add_trap_invalid_port = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                       'readCommunity': 'public',
                                                       'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                       'systemContact': 'None',
                                                       'v3Enabled': True,
                                                       'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'1-2'}],
                                                       'snmpAccess': [],
                                                       'enabled': False,
                                                       'category': 'snmp-configuration',
                                                       'uri': None
                                                       }}

edit_li_add_trap_invalid_engine_id = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                            'readCommunity': 'public',
                                                            'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                            'systemContact': 'None',
                                                            'v3Enabled': True,
                                                            'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0x!@# $', 'communityString':'', 'port':'162'}],
                                                            'snmpAccess': [],
                                                            'enabled': False,
                                                            'category': 'snmp-configuration',
                                                            'uri': None
                                                            }}

edit_li_add_trap_max = {'type': 'snmp-configuration',
                        'readCommunity': 'public',
                        'snmpUsers': [{'snmpV3UserName': 'user1', 'securityLevel': 'NoAuthNoPrivacy', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                        'systemContact': 'None',
                        'v3Enabled': True,
                        'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.50', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.51', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.52', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.53', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.54', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.55', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.56', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.57', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'},
                                             {'trapDestination': '192.168.149.58', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'192'}
                                             ],
                        'snmpAccess': [],
                        'enabled': False,
                        'category': 'snmp-configuration',
                        'uri': None
                        }

edit_li_edit_trap_address = {'type': 'snmp-configuration',
                             'readCommunity': 'public',
                             'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                             'systemContact': 'None',
                             'v3Enabled': True,
                             'trapDestinations': [{'trapDestination': '192.168.149.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'162'}],
                             'snmpAccess': [],
                             'enabled': False,
                             'category': 'snmp-configuration',
                             'uri': None
                             }

edit_li_edit_trap_user_name = {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                             {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                               'systemContact': 'None',
                               'v3Enabled': True,
                               'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'162'}],
                               'snmpAccess': [],
                               'enabled': False,
                               'category': 'snmp-configuration',
                               'uri': None
                               }

edit_li_edit_trap_security_level = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                          'readCommunity': 'public',
                                                          'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                                                        {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                          'systemContact': 'None',
                                                          'v3Enabled': True,
                                                          'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'162'}],
                                                          'snmpAccess': [],
                                                          'enabled': False,
                                                          'category': 'snmp-configuration',
                                                          'uri': None
                                                          }}
edit_li_edit_trap_snmpv1 = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'readCommunity': 'public',
                                                  'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                                                {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                  'systemContact': 'None',
                                                  'v3Enabled': True,
                                                  'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'162'},
                                                                       {'trapDestination': '192.168.148.50', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'communityString':'public', 'port':'162'}
                                                                       ],
                                                  'snmpAccess': [],
                                                  'enabled': False,
                                                  'category': 'snmp-configuration',
                                                  'uri': None
                                                  }}

edit_li_edit_trap_snmpv1_to_snmpv3 = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                            'readCommunity': 'public',
                                                            'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                                                          {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                            'systemContact': 'None',
                                                            'v3Enabled': True,
                                                            'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'162'},
                                                                                 {'trapDestination': '192.168.148.50', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':False, 'communityString':'', 'port':'162'}
                                                                                 ],
                                                            'snmpAccess': [],
                                                            'enabled': False,
                                                            'category': 'snmp-configuration',
                                                            'uri': None
                                                            }}

edit_li_edit_trap_snmpv3_to_snmpv1 = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                            'readCommunity': 'public',
                                                            'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                                                          {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                            'systemContact': 'None',
                                                            'v3Enabled': True,
                                                            'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':True, 'engineId':'0xFFFFFFFFFFFF', 'communityString':'', 'port':'162'},
                                                                                 {'trapDestination': '192.168.148.50', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'communityString':'public', 'port':'162'}
                                                                                 ],
                                                            'snmpAccess': [],
                                                            'enabled': False,
                                                            'category': 'snmp-configuration',
                                                            'uri': None
                                                            }}

edit_li_remove_trap_entries = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                     'readCommunity': 'public',
                                                     'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                                                   {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None}],
                                                     'systemContact': 'None',
                                                     'v3Enabled': True,
                                                     'trapDestinations': [],
                                                     'snmpAccess': [],
                                                     'enabled': False,
                                                     'category': 'snmp-configuration',
                                                     'uri': None
                                                     }}

edit_li_edit_snmp_user_AuthandAuthpriv = {'type': 'snmp-configuration',
                                          'readCommunity': 'public',
                                          'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': None},
                                                        {'snmpV3UserName': 'user2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                        {'snmpV3UserName': 'user3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                          'systemContact': 'None',
                                          'v3Enabled': True,
                                          'trapDestinations': [],
                                          'snmpAccess': [],
                                          'enabled': False,
                                          'category': 'snmp-configuration',
                                          'uri': None}

edit_lig_UFG_LI_Add_User = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                          {'snmpV3UserName': 'user2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                            'trapDestinations': [],
                            'snmpAccess': [],
                            'v3Enabled': True,
                            'enabled': False,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_lig_UFG_LI_Add_trap = {'type': 'snmp-configuration',
                            'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                          {'snmpV3UserName': 'user2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                            'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':False, 'communityString':'', 'port':'162'}],
                            'snmpAccess': [],
                            'v3Enabled': True,
                            'enabled': False,
                            'category': 'snmp-configuration',
                            'uri': None}

edit_lig_UFG_LI_Add_access = {'type': 'snmp-configuration',
                              'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                            {'snmpV3UserName': 'user2', 'userCredentials': [], 'v3AuthProtocol':'NA', 'v3PrivacyProtocol':'NA'}],
                              'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user1', 'inform':False, 'communityString':'', 'port':'162'}],
                              'snmpAccess': ['192.168.144.167/24'],
                              'v3Enabled': True,
                              'enabled': False,
                              'category': 'snmp-configuration',
                              'uri': None}

edit_lig_UFG_LI_edit_User_Auth = {'type': 'snmp-configuration',
                                  'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                                {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                {'snmpV3UserName': 'user3', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                {'snmpV3UserName': 'user4', 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                  'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':False, 'communityString':'', 'port':'162'}],
                                  'snmpAccess': [],
                                  'v3Enabled': True,
                                  'enabled': False,
                                  'category': 'snmp-configuration',
                                  'uri': None}

edit_lig_UFG_LI_edit_User_AuthPriv = {'type': 'snmp-configuration',
                                      'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                                    {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'user3', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'user4', 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    # {'snmpV3UserName': 'user5', 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'user6', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'TDEA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                                    {'snmpV3UserName': 'user7', 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],
                                      'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':False, 'communityString':'', 'port':'162'}],
                                      'snmpAccess': [],
                                      'v3Enabled': True,
                                      'enabled': False,
                                      'category': 'snmp-configuration',
                                      'uri': None}


edit_li_UFG_LI_edit_User_Auth = {'type': 'snmp-configuration',
                                 'readCommunity': 'public',
                                 'systemContact': '',
                                 'v3Enabled': True,
                                 'snmpUsers': [{'snmpV3UserName': 'user1', 'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA', 'userCredentials': []},
                                               {'snmpV3UserName': 'user2', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'user3', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'user4', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               # {'snmpV3UserName': 'user5', 'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password@123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'user6', 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'TDEA', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               {'snmpV3UserName': 'user7', 'v3AuthProtocol': 'SHA2', 'v3PrivacyProtocol': 'AES128', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]},
                                               ],
                                 'trapDestinations': [{'trapDestination': '192.168.144.167', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[], 'userName':'user2', 'inform':False, 'communityString':'', 'port':'162', 'engineId': None}],
                                 'snmpAccess': [],
                                 'enabled': False,
                                 'category': 'snmp-configuration'
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
                               'uri': None
                               }

#  Demo Scenarios for Tbird

user_proto_priv_lig = [{'user': 'User1', 'auth': 'MD5', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                       {'user': 'User2', 'auth': 'SHA1', 'priv': 'None', 'auth_pass': 'password123', 'priv_pass': ''},
                       {'user': 'User3', 'auth': 'MD5', 'priv': 'DES', 'auth_pass': 'password123', 'priv_pass': 'password123'}

                       ]


#  Demo Scenarios
tbird_user_proto_priv = [{'user': 'user1', 'auth': 'SHA512', 'priv': 'None'},
                         {'user': 'potashuser', 'auth': 'SHA1', 'priv': 'None'},
                         {'user': 'User4', 'auth': 'SHA384', 'priv': 'AES128'},
                         {'user': 'User5', 'auth': 'SHA512', 'priv': 'AES256'},
                         {'user': 'User3', 'auth': 'SHA384', 'priv': '3DES'}
                         ]


tbird_user_proto_priv_All_Users = [{'user': 'User1', 'auth': 'SHA1', 'priv': 'None'},
                                   {'user': 'User2', 'auth': 'SHA256', 'priv': 'None'},
                                   {'user': 'User3', 'auth': 'SHA384', 'priv': 'None'},
                                   {'user': 'User4', 'auth': 'SHA512', 'priv': 'None'},
                                   {'user': 'User5', 'auth': 'SHA1', 'priv': 'DES56'},
                                   {'user': 'User6', 'auth': 'SHA256', 'priv': 'TDEA'},
                                   {'user': 'User7', 'auth': 'SHA256', 'priv': 'AES128'},
                                   {'user': 'User8', 'auth': 'SHA384', 'priv': 'AES192'},
                                   {'user': 'User9', 'auth': 'SHA1', 'priv': 'AES256'},
                                   {'user': 'User10', 'auth': 'None', 'priv': 'None'}]


tbird_user_proto_priv_all_original = [{'user': 'User1', 'auth': 'SHA1', 'priv': 'None'},
                                      {'user': 'User2', 'auth': 'SHA256', 'priv': 'None'},
                                      {'user': 'User3', 'auth': 'SHA384', 'priv': 'None'},
                                      {'user': 'User4', 'auth': 'SHA512', 'priv': 'None'},
                                      {'user': 'User5', 'priv': 'DES', 'auth': 'SHA1'},
                                      {'user': 'User6', 'priv': '3DES', 'auth': 'SHA256'},
                                      {'user': 'User7', 'priv': 'AES128', 'auth': 'SHA512'},
                                      {'user': 'User8', 'priv': 'AES192', 'auth': 'SHA384'},
                                      {'user': 'User9', 'priv': 'AES256', 'auth': 'SHA1'},
                                      {'user': 'User10', 'priv': 'None', 'auth': 'None'}]


tbird_user_proto_priv_all = [{'user': 'User1', 'auth': 'SHA1', 'priv': 'None'},
                             {'user': 'User2', 'auth': 'SHA256', 'priv': 'None'},
                             {'user': 'User3', 'auth': 'SHA384', 'priv': 'None'},
                             {'user': 'User4', 'auth': 'SHA512', 'priv': 'None'},
                             {'user': 'User5', 'priv': 'DES', 'auth': 'SHA1'},
                             {'user': 'User6', 'priv': '3DES', 'auth': 'SHA256'},
                             {'user': 'User7', 'priv': 'AES128', 'auth': 'SHA512'},
                             {'user': 'User8', 'priv': 'AES192', 'auth': 'SHA384'},
                             {'user': 'User9', 'priv': 'AES256', 'auth': 'SHA1'}]


tbird_user_proto_priv_1 = [

    {'user': 'User1', 'auth': 'SHA1', 'priv': 'DES'},
    {'user': 'User2', 'auth': 'SHA1', 'priv': '3DES'},
    {'user': 'User3', 'auth': 'SHA1', 'priv': 'AES128'},
    {'user': 'User4', 'auth': 'SHA1', 'priv': 'AES192'},
    {'user': 'User5', 'auth': 'SHA1', 'priv': 'AES256'},
    {'user': 'User6', 'auth': 'SHA256', 'priv': 'DES'},
    {'user': 'User7', 'auth': 'SHA256', 'priv': '3DES'},
    {'user': 'User8', 'auth': 'SHA256', 'priv': 'AES128'},
    {'user': 'User9', 'auth': 'SHA256', 'priv': 'AES192'},
    {'user': 'User10', 'auth': 'SHA256', 'priv': 'AES256'}

]

tbird_user_proto_priv_2 = [{'user': 'User1', 'auth': 'SHA1', 'priv': 'DES'},
                           {'user': 'User2', 'auth': 'SHA512', 'priv': '3DES'},
                           {'user': 'User3', 'auth': 'SHA512', 'priv': 'AES128'},
                           {'user': 'User4', 'auth': 'SHA512', 'priv': 'AES192'},
                           {'user': 'User5', 'auth': 'SHA512', 'priv': 'AES256'},
                           {'user': 'User6', 'auth': 'SHA384', 'priv': 'DES'},
                           {'user': 'User7', 'auth': 'SHA384', 'priv': '3DES'},
                           {'user': 'User8', 'auth': 'SHA384', 'priv': 'AES128'},
                           {'user': 'User9', 'auth': 'SHA384', 'priv': 'AES192'},
                           {'user': 'User10', 'auth': 'SHA1', 'priv': 'AES128'}



                           ]
tbird_user_proto_priv_3 = [{'user': 'User1', 'auth': 'SHA1', 'priv': 'DES'},
                           {'user': 'User2', 'auth': 'SHA512', 'priv': '3DES'},
                           {'user': 'User3', 'auth': 'SHA512', 'priv': 'AES128'},
                           {'user': 'User4', 'auth': 'SHA512', 'priv': 'AES192'},
                           {'user': 'User5', 'auth': 'SHA512', 'priv': 'AES256'},
                           {'user': 'User6', 'auth': 'SHA384', 'priv': 'DES'},
                           {'user': 'User7', 'auth': 'SHA384', 'priv': '3DES'},
                           {'user': 'User8', 'auth': 'SHA384', 'priv': 'AES128'},
                           {'user': 'User9', 'auth': 'SHA384', 'priv': 'AES192'},
                           {'user': 'User10', 'auth': 'SHA384', 'priv': 'AES256'}



                           ]

uplink_disable_tbird1 = {'interconnectName': 'EM1FFFF500, interconnect 3', 'enabled': False,
                         'portName': 'Q5:1',
                         'type': 'port',
                         }

uplink_enable_tbird1 = {'interconnectName': 'EM1FFFF500, interconnect 3', 'enabled': True,
                        'portName': 'Q5:1',
                        'type': 'port',
                        }


edit_li_no_engine_id = {'snmpConfiguration': {'type': 'snmp-configuration',
                                              'readCommunity': 'public',
                                              'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                              'readCommunity': 'public',
                                              'systemContact': '',
                                              'trapDestinations': [{'trapDestination': '10.101.11.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                    'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'engineId':'', 'communityString':'', 'port':'162'}],

                                              'snmpAccess': [],
                                              'v3Enabled': True,
                                              'enabled': False,
                                              'category': 'snmp-configuration',
                                              'uri': None}}


edit_li_trap_engineid = {'snmpConfiguration': {'type': 'snmp-configuration',
                                               'readCommunity': 'public',
                                               'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                               'readCommunity': 'public',
                                               'systemContact': '',
                                               'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                     'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'engineId':'0x80001F888071F26C0ED6B8E15800000000', 'communityString':'', 'port':'162'}],
                                               'snmpAccess': [],
                                               'enabled': False,
                                               'v3Enabled': True,
                                               'category': 'snmp-configuration',
                                               'uri': None}}


edit_li_max_trap = {'snmpConfiguration': {'type': 'snmp-configuration',
                                          'readCommunity': 'public',
                                          'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES192', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                          'readCommunity': 'public',
                                          'systemContact': '',
                                          'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '11.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '12.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '13.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '14.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '15.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'},
                                                               {'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],

                                          'snmpAccess': [],
                                          'enabled': False,
                                          'v3Enabled': True,
                                          'category': 'snmp-configuration',
                                          'uri': None}}

edit_li_max_users = {'snmpConfiguration': {'type': 'snmp-configuration',
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

                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'trapDestinations': [],

                                           'snmpAccess': [],
                                           'enabled': False,
                                           'v3Enabled': True,
                                           'category': 'snmp-configuration',
                                           'uri': None}}

edit_li_length_validate = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                 'readCommunity': 'public',
                                                 'snmpUsers': [{'snmpV3UserName': '1234567890123456k7890l123h567890', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                 'readCommunity': 'public',
                                                 'systemContact': '',
                                                 'trapDestinations': [],

                                                 'snmpAccess': [],
                                                 'enabled': False,
                                                 'v3Enabled': True,
                                                 'category': 'snmp-configuration',
                                                 'uri': None}}

edit_li_invalid_user_in_trap = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                      'readCommunity': 'public',
                                                      'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                      'readCommunity': 'public',
                                                      'systemContact': '',
                                                      'trapDestinations': [{'trapDestination': '10.10.101.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                            'fcTrapCategories':[], 'userName':'User11', 'inform':False, 'communityString':'', 'port':'162'}],

                                                      'snmpAccess': [],
                                                      'enabled': False,
                                                      'v3Enabled': True,
                                                      'category': 'snmp-configuration',
                                                      'uri': None}}

li_missing_Auth_Pass_Phrase = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                     'readCommunity': 'public',
                                                     'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                     'readCommunity': 'public',
                                                     'systemContact': '',
                                                     'trapDestinations': [],

                                                     'snmpAccess': [],
                                                     'enabled': False,
                                                     'v3Enabled': True,
                                                     'category': 'snmp-configuration',
                                                     'uri': None}}

li_missing_priv_Pass_Phrase = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                     'readCommunity': 'public',
                                                     'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': '', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                     'readCommunity': 'public',
                                                     'systemContact': '',
                                                     'trapDestinations': [],

                                                     'snmpAccess': [],
                                                     'enabled': False,
                                                     'v3Enabled': True,
                                                     'category': 'snmp-configuration',
                                                     'uri': None}}

li_missing_auth_Phrase = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                'readCommunity': 'public',
                                                'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': '', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                'readCommunity': 'public',
                                                'systemContact': '',
                                                'trapDestinations': [],

                                                'snmpAccess': [],
                                                'enabled': False,
                                                'v3Enabled': True,
                                                'category': 'snmp-configuration',
                                                'uri': None}}

li_invalid_username = {'snmpConfiguration': {'type': 'snmp-configuration',
                                             'readCommunity': 'public',
                                             'snmpUsers': [{'snmpV3UserName': 'One_1212-nfn1213231323434434_****((((3$$$%%%', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                             'readCommunity': 'public',
                                             'systemContact': '',
                                             'trapDestinations': [],

                                             'snmpAccess': [],
                                             'enabled': False,
                                             'v3Enabled': True,
                                             'category': 'snmp-configuration',
                                             'uri': None}}

edit_li_invalid_auth_pwd = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'readCommunity': 'public',
                                                  'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                  'readCommunity': 'public',
                                                  'systemContact': '',
                                                  'trapDestinations': [],

                                                  'snmpAccess': [],
                                                  'enabled': False,
                                                  'v3Enabled': True,
                                                  'category': 'snmp-configuration',
                                                  'uri': None}}

edit_li_invalid_priv_pwd = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'readCommunity': 'public',
                                                  'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'pass', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                  'readCommunity': 'public',
                                                  'systemContact': '',
                                                  'trapDestinations': [],

                                                  'snmpAccess': [],
                                                  'enabled': False,
                                                  'v3Enabled': True,
                                                  'category': 'snmp-configuration',
                                                  'uri': None}}

edit_li_invalid_engineid = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                  'readCommunity': 'public',
                                                  'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                  'readCommunity': 'public',
                                                  'systemContact': '',
                                                  'trapDestinations': [{'trapDestination': '192.168.148.49', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                        'fcTrapCategories':[], 'userName':'User1', 'inform':True, 'engineId':'0xFFF', 'communityString':'', 'port':'162'}],

                                                  'snmpAccess': [],
                                                  'enabled': False,
                                                  'v3Enabled': True,
                                                  'category': 'snmp-configuration',
                                                  'uri': None}}

edit_li_invalid_format = {'snmpConfiguration': {'type': 'snmp-configuration',
                                                'readCommunity': 'public',
                                                'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                                'readCommunity': 'public',
                                                'systemContact': '',
                                                'trapDestinations': [{'trapDestination': '16.10.101.1', 'trapFormat': 'SNMPv4', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                      'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'162'}],

                                                'snmpAccess': [],
                                                'enabled': False,
                                                'v3Enabled': True,
                                                'category': 'snmp-configuration',
                                                'uri': None}}

edit_li_invalid_port = {'snmpConfiguration': {'type': 'snmp-configuration',
                                              'readCommunity': 'public',
                                              'snmpUsers': [{'snmpV3UserName': 'User1', 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'AES256', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'passwords123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]}],

                                              'readCommunity': 'public',
                                              'systemContact': '',
                                              'trapDestinations': [{'trapDestination': '10.101.11.1', 'trapFormat': 'SNMPv3', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[],
                                                                    'fcTrapCategories':[], 'userName':'User1', 'inform':False, 'communityString':'', 'port':'1620000'}],

                                              'snmpAccess': [],

                                              'enabled': False,
                                              'v3Enabled': True,
                                              'category': 'snmp-configuration',
                                              'uri': None}
                        }


#  Tbird Data variables

error_lig = {'message': 'SNMP configuration has a User Name No_Auth_No_Priv which is already existing.', 'errorCode': 'CRM_SNMP_CONFIGURATION_DUPLICATE_USER_NAME'}
error_invalid_user = {'message': 'The user name One_1212-nfn1213231323434434_****((((3$$$%%% for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_invalid_Auth_password = {'message': 'The authentication password for SNMPv3 user User1 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_AUTH_PWD_INVALID'}
error_invalid_Priv_password = {'message': 'The privacy password for SNMPv3 user User1 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_PRIV_PWD_INVALID'}
error_Mandatory_Attribute_Check = {'message': 'SNMP configuration has a null or empty User Name.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
error_Maximum_No_of_users = {'message': 'There can be no more than 10 SNMPv3 users.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX'}
error_server_admin = {'message': 'Authorization error: User not authorized for this operation.', 'errorCode': 'AUTHORIZATION'}
error_missing_Parameter = {'message': 'Invalid JSON data type.', 'errorCode': 'INVALID_JSON_DATA_TYPE'}
error_user_name_missing_Parameter = {'message': 'SNMP configuration has a null or empty User Name.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
error_no_users = {'message': 'SNMP trap destination has a user which does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_wrong_user = {'message': 'The user Wrong_User_Name specified for the SNMPv3 trap destination 192.168.148.49 does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_invalid_engine_id = {'message': 'The engine ID for SNMPv3 trap destination 192.168.148.49 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_ENGINEID'}
error_Maximum_No_of_Traps = {'message': 'The SNMP trap destinations cannot be added because the maximum number of 6 SNMPv3 trap destinations has been exceeded.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_EXCEEDS_MAX'}
error_missing_engineid = {'message': 'An engine ID is required for the SNMPv3 trap destination 10.101.11.1 for inform.', 'errorCode': 'CRM_SNMP_CONFIGURATION_ENGINE_ID_MISSING'}


# error_lig = {'message':'SNMP configuration has a User Name No_Auth_No_Priv which is already existing.', 'errorCode':'CRM_SNMP_CONFIGURATION_DUPLICATE_USER_NAME'}
# error_invalid_user = {'message':'The user name for SNMPv3 configuration is invalid.', 'errorCode':'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
# error_invalid_Auth_password = {'message':'The authorization password for SNMPv3 is invalid.', 'errorCode':'CRM_SNMP_CONFIGURATION_AUTH_PWD_INVALID_FOR_POTASH'}
# error_invalid_Priv_password = {'message':'The privacy password for SNMPv3 configuration is invalid.', 'errorCode':'CRM_SNMP_CONFIGURATION_PRIV_PWD_INVALID_FOR_POTASH'}
# error_Mandatory_Attribute_Check = {'message':'SNMP configuration has a null or empty User Name.', 'errorCode':'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
# error_Maximum_No_of_users = {'message':'There can be no more than 10 SNMPv3 users.', 'errorCode':'CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX'}
# error_server_admin = {'message':'Authorization error: User not authorized for this operation.', 'errorCode':'AUTHORIZATION'}
# error_missing_Parameter = {'message':'Invalid JSON data type.', 'errorCode':'INVALID_JSON_DATA_TYPE'}
# error_user_name_missing_Parameter = {'message':'SNMP configuration has a null or empty User Name.', 'errorCode':'CRM_SNMP_CONFIGURATION_USER_NAME_MISSING'}
# error_no_users = {'message':'SNMP trap destination has a user which does not exist.', 'errorCode':'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
# error_wrong_user = {'message': 'The user Wrong_User_Name specified for the SNMPv3 trap destination does not exist.',  'errorCode':'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
# error_invalid_engine_id= {'message': 'The engine ID for SNMPv3 configuration is invalid.',  'errorCode':'CRM_SNMP_CONFIGURATION_INVALID_ENGINEID'}
# error_Maximum_No_of_Traps= {'message': 'The SNMP trap destinations cannot be added because the maximum number of 6 trap destinations has been exceeded.',  'errorCode':'CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_EXCEEDS_MAX'}
error_missing_auth_password = {'message': 'The credential type SHA256 is needed but not present.', 'errorCode': 'CRM_MISSING_CREDENTIAL_KEY'}
error_missing_priv_password = {'message': 'The credential type AES256 is needed but not present.', 'errorCode': 'CRM_MISSING_CREDENTIAL_KEY'}
# error_invalid_length= {'message': 'The authorization password for SNMPv3 is invalid.',  'errorCode':'CRM_SNMP_CONFIGURATION_AUTH_PWD_LENGTH_INVALID'}
error_invalid_length = {'message': 'The user name 1234567890123456k7890l123h567890 for SNMPv3 configuration is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_INVALID'}
error_invalid_snmp_user_in_trap = {'message': 'The user User11 specified for the SNMPv3 trap destination 10.10.101.1 does not exist.', 'errorCode': 'CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND'}
error_engineid_in_trap = {'message': 'The SNMPv3 trap destination 10.10.101.1 has an engine ID and the notification type is trap.', 'errorCode': 'CRM_SNMP_CONFIGURATION_TRAP_SHOULD_NOT_HAVE_ENGINEID'}
error_invalid_port = {'message': 'The port number for trap destination 10.101.11.1 is invalid.', 'errorCode': 'CRM_SNMP_CONFIGURATION_INVALID_PORTNO'}
# error_missing_engineid= {'message': 'An engine ID is required for the SNMPv3 trap destination for inform.',  'errorCode':'CRM_SNMP_CONFIGURATION_ENGINE_ID_MISSING'}

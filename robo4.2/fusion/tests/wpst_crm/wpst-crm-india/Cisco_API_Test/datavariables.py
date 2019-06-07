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


# setup:
switch5k12 = "192.168.144.116"
switch5k16 = "192.168.144.77"
switch6k13 = "192.168.144.117"
switch6k14 = "192.168.144.120"

swtch_model = "N5K-C5548UP"
SWITCH_USERNAME = "admin"
SWITCH_PASSWORD = "Welcome@123"
fex_bay1 = 'SGH439WJKT, interconnect 1'
fex_bay2 = 'SGH439WJKT, interconnect 2'
switch = "Cisco Nexus 55xx"
enclname = "SGH439WJKT"


ligs = [{'name': 'LIG',
         'type': 'logical-interconnect-groupV300',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Cisco Fabric Extender for HP BladeSystem'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'Cisco Fabric Extender for HP BladeSystem'}

                                     ],
         'uplinkSets': [{'name': 'us1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['eth-10'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos':[{'bay': '1', 'port': '2', 'speed': 'Auto'},
                                                   {'bay': '1', 'port': '4', 'speed': 'Auto'},
                                                   {'bay': '1', 'port': '5', 'speed': 'Auto'}
                                                   ]}
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'qosConfiguration': None}
        ]

encs = [{'hostname': '10.10.6.28', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EG', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]

server_profiles = [
    {'type': 'ServerProfileV7', 'serverHardwareUri': 'SGH439WJKT, bay 1',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH439WJKT', 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'sp1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                    'connections': [{'id': 1, 'name': 'conn1', 'functionType': 'Ethernet', 'portId': '1:1a',
                                     'requestedMbps': '2500', 'networkUri': 'ETH:eth-10',
                                     'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]}]

server_profiles1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SGH439WJKT, bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH439WJKT', 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Sp1', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                     'connections': [{'id': 1, 'name': 'conn1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '', 'networkUri': 'ETH:eth-10', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                     ]}

                    ]

enc_groups = [{'name': 'EG',
               'type': 'EnclosureGroupV400',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]


edit_dwnlk1 = [{"associatedUplinkSetUri": None, "interconnectName": fex_bay1, "portType": "Downlink", "portId": "d1", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe"],
                "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":True, "portName":"d1", "portStatus":"Linked", "type":"port"}]

lsgs = [{'name': 'LSG-2-55xx', 'type': 'logical-switch-groupV300',
         'switchMapTemplate': {'switchMapEntryTemplates': [{'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
                                                            'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'},
                                                           {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                                                            'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'}]}},
        {'name': 'LSG-1-50xx', 'type': 'logical-switch-groupV300', 'switchMapTemplate': {'switchMapEntryTemplates': [
            {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
             'permittedSwitchTypeUri': 'SWT:Cisco Nexus 50xx'}]}},
        {'name': 'LSG-1-55xx', 'type': 'logical-switch-groupV300', 'switchMapTemplate': {'switchMapEntryTemplates': [
            {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
             'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'}]}},
        {'name': 'LSG-2-6xxx', 'type': 'logical-switch-groupV300',
         'switchMapTemplate': {'switchMapEntryTemplates': [
             {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
              'permittedSwitchTypeUri': 'SWT:Cisco Nexus 600x'},
             {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                 'permittedSwitchTypeUri': 'SWT:Cisco Nexus 600x'}]}},
        {'name': 'LSG-1-6xxx', 'type': 'logical-switch-groupV300',
         'switchMapTemplate': {'switchMapEntryTemplates': [
             {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
              'permittedSwitchTypeUri': 'SWT:Cisco Nexus 600x'}]}},
        {'name': 'LSG-1-56xx', 'type': 'logical-switch-groupV300',
         'switchMapTemplate': {'switchMapEntryTemplates': [
             {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
              'permittedSwitchTypeUri': 'SWT:Cisco Nexus 56xx'}]}}]

edit_lsg = [{'name': 'lsg11-1', 'state': 'Active',
             'uri': 'LSG:lsg13-1',
             'type': 'logical-switch-groupV300',
             'switchMapTemplate': {'switchMapEntryTemplates': [{'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
                                                                'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'}, {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                                                                                                                    'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'}]}}]

edit_lsg1 = [{'name': 'lsg11-1', 'state': 'Active',
              'uri': 'LSG:lsg13-1',
              'type': 'logical-switch-groupV300',
              'switchMapTemplate': {'switchMapEntryTemplates': [{'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
                                                                 'permittedSwitchTypeUri': 'SWT:Cisco Nexus 55xx'}]}}]

edit_icm = [{"associatedUplinkSetUri": None, "interconnectName": None, "portType": "Downlink", "portId": None, "portHealthStatus": "Disabled", "capability": ["EnetFcoe", "Ethernet"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":None, "portName":None, "portStatus":"Unlinked", "type":"port"}]

# TODO - new managementLevel enum:  BASIC_MANAGED, MONITORED
ls_create = [{"logicalSwitch": {"name": "LS1-1", "state": "Active", "type": "logical-switchV300", "managementLevel": "BASIC_MANAGED",
                                "logicalSwitchGroupUri": "LSG:LSG-2-55xx",
                                "switchCredentialConfiguration":
                                [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                  "snmpV3Configuration": {"authorizationProtocol": None, "privacyProtocol": None, "securityLevel": None},
                                  "logicalSwitchManagementHost": switch5k12, "snmpVersion": "SNMPv1", "snmpPort": 161},
                                 {"snmpV1Configuration": {"communityString": "wpstcs"}, "snmpV3Configuration": {"authorizationProtocol": None, "privacyProtocol": None,
                                                                                                                "securityLevel": None},
                                    "logicalSwitchManagementHost": switch5k16, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
              "logicalSwitchCredentials": [{"connectionProperties": [
                  {"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                  {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                  {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                  {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]


ls_auth_authpriv = [
    {"logicalSwitch":
     {"name": "LS1-1", "managementLevel": "BASIC_MANAGED",
      "state": "Active", "status": None, "description": None,
      "uri": None, "category": None, "eTag": None, "created": None, "modified": None,
      "type": "logical-switchV300", "switchMap": None,
      "logicalSwitchGroupUri": "LSG:LSG-2-55xx",
      "switchCredentialConfiguration": [
          {"snmpV1Configuration": {"communityString": None},
           "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
           "logicalSwitchManagementHost": "192.168.144.77", "snmpVersion": "SNMPv3", "snmpPort": 161},
          {"snmpV1Configuration": {"communityString": None},
           "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
           "logicalSwitchManagementHost": "192.168.144.116", "snmpVersion": "SNMPv3", "snmpPort": 161}]},
        "logicalSwitchCredentials": [

         {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},

         {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]
     }
]

ls3 = [
    {"logicalSwitch":
     {"name": "LS1-1", "managementLevel": "MONITORED",
      "state": "Active", "status": None, "description": None,
      "uri": None, "category": None, "eTag": None, "created": None, "modified": None,
      "type": "logical-switchV300", "switchMap": None,
      "logicalSwitchGroupUri": "LSG:LSG-2-55xx",
      "switchCredentialConfiguration": [
          {"snmpV1Configuration": {"communityString": None},
           "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
           "logicalSwitchManagementHost": "192.168.144.77", "snmpVersion": "SNMPv3", "snmpPort": 161},
          {"snmpV1Configuration": {"communityString": None},
           "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
           "logicalSwitchManagementHost": "192.168.144.116", "snmpVersion": "SNMPv3", "snmpPort": 161}]},
        "logicalSwitchCredentials": [

         {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},

         {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                                   {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                   {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]
     }
]

ls_apriv_apriv = [{"logicalSwitch": {"name": "LS1-1", "managementLevel": "BASIC_MANAGED", "state": "Active", "status": None, "description": None, "uri": None, "category": None, "eTag": None, "created": None, "modified": None,
                                     "type": "logical-switchV300",
                                     "switchMap": None,
                                     "logicalSwitchGroupUri": "LSG:LSG-2-55xx",
                                     "switchCredentialConfiguration": [
                                         {"snmpV1Configuration": {"communityString": None},
                                          "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                             "logicalSwitchManagementHost": "192.168.144.116", "snmpVersion": "SNMPv3", "snmpPort": 161},
                                         {"snmpV1Configuration": {"communityString": None},
                                          "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"
                                                                  }, "logicalSwitchManagementHost": "192.168.144.77", "snmpVersion": "SNMPv3", "snmpPort": 161}]},
                   "logicalSwitchCredentials": [{"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                                                          {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                                                                          {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
                                                {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"
                                                                           }, {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls4 = [{"logicalSwitch": {"name": "LS1-1", "managementLevel": "BASIC_MANAGED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                          "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                        "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                        "logicalSwitchManagementHost": switch5k12, "snmpVersion": "SNMPv1", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                                                                                                               "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                                                                                                               "logicalSwitchManagementHost": switch5k16, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
        "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls5 = [{"logicalSwitch": {"name": "TestLS1", "managementLevel": "BASIC_MANAGED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                          "logicalSwitchGroupUri": "LSG:LSG-1-55xx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                        "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                        "logicalSwitchManagementHost": switch5k12, "snmpVersion": "SNMPv3", "snmpPort": 161}]},
        "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls6 = [{"logicalSwitch": {"name": "LS1-3", "managementLevel": "BASIC_MANAGED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                          "logicalSwitchGroupUri": "LSG:LSG-1-55xx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                        "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                        "logicalSwitchManagementHost": switch5k16, "snmpVersion": "SNMPv3", "snmpPort": 161}]},
        "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls7 = [{"logicalSwitch": {"name": "TestLSN", "managementLevel": "BASIC_MANAGED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                          "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": None},
                                                                                                        "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": None, "securityLevel": "Auth"},
                                                                                                        "logicalSwitchManagementHost": switch5k12, "snmpVersion": "SNMPv3", "snmpPort": 161},
                                                                                                       {"snmpV1Configuration": {"communityString": None}, "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                        "logicalSwitchManagementHost": switch5k16, "snmpVersion": "SNMPv3", "snmpPort": 161}]},
        "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls8 = [{"logicalSwitch": {"name": "LS2-1", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                          "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                        "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                        "logicalSwitchManagementHost": switch5k12, "snmpVersion": "SNMPv1", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                                                                                                               "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                                                                                                               "logicalSwitchManagementHost": switch5k16, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
        "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls9 = [{"logicalSwitch": {"name": "LS1-1", "managementLevel": "MONITORED", "state": "Active", "status": None, "description": None, "uri": None, "category": None, "eTag": None, "created": None, "modified": None,
                          "type": "logical-switchV300",
                          "switchMap": None,
                          "logicalSwitchGroupUri": "LSG:LSG-2-55xx",
                          "switchCredentialConfiguration": [
                              {"snmpV1Configuration": {"communityString": None},
                               "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                  "logicalSwitchManagementHost": "192.168.144.116", "snmpVersion": "SNMPv3", "snmpPort": 161},
                              {"snmpV1Configuration": {"communityString": None},
                               "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"
                                                       }, "logicalSwitchManagementHost": "192.168.144.77", "snmpVersion": "SNMPv3", "snmpPort": 161}]},
        "logicalSwitchCredentials": [{"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                                                               {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                                                               {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
                                     {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"
                                                                }, {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls10 = [{"logicalSwitch": {"name": "LS2-1", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                           "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                         "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                         "logicalSwitchManagementHost": switch6k13, "snmpVersion": "SNMPv1", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                                                                                                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                                                                                                                "logicalSwitchManagementHost": switch6k14, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
         "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls11 = [{"logicalSwitch": {"name": "LS2-1", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                           "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                         "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                         "logicalSwitchManagementHost": switch6k13, "snmpVersion": "SNMPv1", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "wpstcs"},
                                                                                                                                                                                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                                                                                                                "logicalSwitchManagementHost": switch6k14, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
         "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]


ls12 = [{"logicalSwitch": {"name": "LS2-3", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                           "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": None},
                                                                                                         "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                         "logicalSwitchManagementHost": switch6k13, "snmpVersion": "SNMPv3", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "public"},
                                                                                                                                                                                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                                                                                                                "logicalSwitchManagementHost": switch6k14, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
         "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]


ls13 = [{"logicalSwitch": {"name": "LS2-3", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                           "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": None},
                                                                                                         "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                         "logicalSwitchManagementHost": switch6k13, "snmpVersion": "SNMPv3", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "public"},
                                                                                                                                                                                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                                                                                                                "logicalSwitchManagementHost": switch6k14, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
         "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls14 = [{"logicalSwitch": {"name": "LS2-3", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                           "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": None},
                                                                                                         "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "Auth"},
                                                                                                         "logicalSwitchManagementHost": switch6k13, "snmpVersion": "SNMPv3", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": "public"},
                                                                                                                                                                                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                                                                                                                "logicalSwitchManagementHost": switch6k14, "snmpVersion": "SNMPv1", "snmpPort": 161}]},
         "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls15 = [{"logicalSwitch": {"name": "TestLS1", "managementLevel": "MONITORED", "state": "Active", "category": None, "created": None, "type": "logical-switchV300", "switchMap": None,
                           "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": None},
                                                                                                         "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                         "logicalSwitchManagementHost": switch6k13, "snmpVersion": "SNMPv3", "snmpPort": 161}, {"snmpV1Configuration": {"communityString": None},
                                                                                                                                                                                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": "AES128", "securityLevel": "AuthPrivacy"},
                                                                                                                                                                                                "logicalSwitchManagementHost": switch6k14, "snmpVersion": "SNMPv3", "snmpPort": 161}]},
         "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

lsedittest = [{"logicalSwitch": {"name": "LS1-2", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS1",
                                 "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                                 [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.12",
                                   "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                   "snmpV3Configuration": None,
                                   "snmpV1Configuration": {"communityString": "public"}, "sshUsername": "admin", "snmpPort": 161},

                                     {"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.16",
                                      "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                      "snmpV3Configuration": None, "snmpV1Configuration": {"communityString": "public"},
                                      "sshUsername": "admin", "snmpPort": 161}],
                                 "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

lsedit1_1 = [{"logicalSwitch":
              {"name": "LS1-2", "managementLevel": "BASIC_MANAGED", "state": "Active", "status": None, "description": None, "uri": "LS:LS1-1", "category": None, "eTag": "None", "created": "None", "modified": None, "type": "logical-switchV300", "switchMap": None,
               "switchCredentialConfiguration": [
                   {"snmpVersion": "SNMPv3", "switchUri": "SWT:192.168.144.116", "logicalSwitchManagementHost": "192.168.144.116", "logicalSwitchManagementHostIpAddress": "192.168.144.116", "memberId": 0, "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": None, "securityLevel": "Auth", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161},

                   {"snmpVersion": "SNMPv3", "switchUri": "SWT:192.168.144.77", "logicalSwitchManagementHost": "192.168.144.77", "logicalSwitchManagementHostIpAddress": "192.168.144.77", "memberId": 0, "snmpV3Configuration": {"authorizationProtocol": "MD5", "privacyProtocol": None, "securityLevel": "Auth", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161}
               ],

                  "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"},

              "logicalSwitchCredentials": [
                  {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},

                  {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}, {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"}, {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}
             ]


lsedit1 = [{"logicalSwitch": {"name": "LS1-2", "managementLevel": "MONITORED", "state": "Active", "uri": "LS:LS1-1",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": None,
                                "snmpV1Configuration": {"communityString": "wpstcs"}, "sshUsername": "admin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": None, "snmpV1Configuration": {"communityString": "wpstcs"},
                                   "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

lsedit2 = [{"logicalSwitch": {"name": "LS1-3", "managementLevel": "MONITORED", "state": "Active", "uri": "LS:LS1-2",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"},
                                  "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"},
                                   "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

lsedit3 = [{"logicalSwitch": {"name": "LS1-4", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS1-3",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": None,
                                "snmpV1Configuration": {"communityString": "public"}, "sshUsername": "admin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None,
                                   "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

lsedit4 = [{"logicalSwitch": {"name": "LS1-5", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS1-4",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"},
                                  "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": None, "snmpV1Configuration": {"communityString": "wpstcs"},
                                   "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]


lsedit5 = [{"logicalSwitch": {"name": "LS1-6", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS1-5",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": {"authorizationProtocol": "SHA", "securityLevel": "Auth", "privacyProtocol": "AES128", "snmpV3UserName": "wpstsha"},
                                  "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "Auth", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None,
                                   "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "wpstsha", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]


lsedit6 = [{"logicalSwitch": {"name": "LS1-7", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS1-6",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "DES56", "snmpV3UserName": "wpstdes56"},
                                  "snmpV1Configuration": None, "sshUsername": "wpstadmin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"},
                                   "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "wpstadmin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "wpstdes56", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]


lsedit7 = [{"logicalSwitch": {"name": "LS1-11", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS1-7",
                              "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                              [{"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k12,
                                "logicalSwitchManagementHost": switch5k12, "logicalSwitchManagementHostIpAddress": switch5k12,
                                "snmpV3Configuration": {"authorizationProtocol": "SHA", "securityLevel": "Auth", "privacyProtocol": "AES128", "snmpV3UserName": "wpstsha"},
                                  "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161},

                                  {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:" + switch5k16,
                                   "logicalSwitchManagementHost": switch5k16, "logicalSwitchManagementHostIpAddress": switch5k16,
                                   "snmpV3Configuration": {"authorizationProtocol": "SHA", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "wpstsha"}, "snmpV1Configuration": None,
                                   "sshUsername": "admin", "snmpPort": 161}],
                              "logicalSwitchGroupUri": "LSG:LSG-2-55xx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "wpstsha", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "wpstsha", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls2edit1 = [{"logicalSwitch": {"name": "LS2-4", "managementLevel": "MONITORED", "state": "Active", "uri": "LS:LS2-1",
                               "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                               [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.13",
                                 "logicalSwitchManagementHost": switch6k13, "logicalSwitchManagementHostIpAddress": switch6k13,
                                 "snmpV3Configuration": None,
                                 "snmpV1Configuration": {"communityString": "wpstcs"}, "sshUsername": "admin", "snmpPort": 161},

                                   {"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.14",
                                    "logicalSwitchManagementHost": switch6k14, "logicalSwitchManagementHostIpAddress": switch6k14,
                                    "snmpV3Configuration": None, "snmpV1Configuration": {"communityString": "wpstcs"},
                                    "sshUsername": "admin", "snmpPort": 161}],
                               "logicalSwitchGroupUri": "LSG:LSG-2-6xxxx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls2edit2 = [{"logicalSwitch": {"name": "LS2-5", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS2-4",
                               "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                               [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.13",
                                 "logicalSwitchManagementHost": switch6k13, "logicalSwitchManagementHostIpAddress": switch6k13,
                                 "snmpV3Configuration": None,
                                 "snmpV1Configuration": {"communityString": "public"}, "sshUsername": "admin", "snmpPort": 161},

                                   {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:10.10.3.14",
                                    "logicalSwitchManagementHost": switch6k14, "logicalSwitchManagementHostIpAddress": switch6k14,
                                    "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None,
                                    "sshUsername": "admin", "snmpPort": 161}],
                               "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls2edit3 = [{"logicalSwitch": {"name": "LS2-7", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS2-5",
                               "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                               [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.13",
                                 "logicalSwitchManagementHost": switch6k13, "logicalSwitchManagementHostIpAddress": switch6k13,
                                 "snmpV3Configuration": None,
                                 "snmpV1Configuration": {"communityString": "public"}, "sshUsername": "admin", "snmpPort": 161},

                                   {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:10.10.3.14",
                                    "logicalSwitchManagementHost": switch6k14, "logicalSwitchManagementHostIpAddress": switch6k14,
                                    "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "Auth", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None,
                                    "sshUsername": "admin", "snmpPort": 161}],
                               "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls2edit4 = [{"logicalSwitch": {"name": "LS2-12", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS2-7",
                               "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                               [{"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:10.10.3.13",
                                 "logicalSwitchManagementHost": switch6k13, "logicalSwitchManagementHostIpAddress": switch6k13,
                                 "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"},
                                   "snmpV1Configuration": None, "sshUsername": "admin", "snmpPort": 161},

                                   {"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.14",
                                    "logicalSwitchManagementHost": switch6k14, "logicalSwitchManagementHostIpAddress": switch6k14,
                                    "snmpV3Configuration": None, "snmpV1Configuration": {"communityString": "wpstcs"},
                                    "sshUsername": "admin", "snmpPort": 161}],
                               "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]
ls2edit5 = [{"logicalSwitch": {"name": "LS2-13", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS2-12",
                               "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                               [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.13",
                                 "logicalSwitchManagementHost": switch6k13, "logicalSwitchManagementHostIpAddress": switch6k13,
                                 "snmpV3Configuration": None,
                                 "snmpV1Configuration": {"communityString": "wpstcs"}, "sshUsername": "admin", "snmpPort": 161},

                                   {"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.14",
                                    "logicalSwitchManagementHost": switch6k14, "logicalSwitchManagementHostIpAddress": switch6k14,
                                    "snmpV3Configuration": None, "snmpV1Configuration": {"communityString": "wpstcs"},
                                    "sshUsername": "admin", "snmpPort": 161}],
                               "logicalSwitchGroupUri": "LSG:LSG-2-6xxxx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

ls2edit6 = [{"logicalSwitch": {"name": "LS2-1", "managementLevel": "BASIC_MANAGED", "state": "Active", "uri": "LS:LS2-13",
                               "type": "logical-switchV300", "switchMap": None, "switchCredentialConfiguration":

                               [{"memberId": 0, "snmpVersion": "SNMPv1", "switchUri": "SWT:10.10.3.13",
                                 "logicalSwitchManagementHost": switch6k13, "logicalSwitchManagementHostIpAddress": switch6k13,
                                 "snmpV3Configuration": None,
                                 "snmpV1Configuration": {"communityString": "public"}, "sshUsername": "admin", "snmpPort": 161},

                                   {"memberId": 0, "snmpVersion": "SNMPv3", "switchUri": "SWT:10.10.3.14",
                                    "logicalSwitchManagementHost": switch6k14, "logicalSwitchManagementHostIpAddress": switch6k14,
                                    "snmpV3Configuration": {"authorizationProtocol": "MD5", "securityLevel": "AuthPrivacy", "privacyProtocol": "AES128", "snmpV3UserName": "harish1"}, "snmpV1Configuration": None,
                                    "sshUsername": "admin", "snmpPort": 161}],
                               "logicalSwitchGroupUri": "LSG:LSG-2-6xxx", "consistencyStatus": "CONSISTENT"}, "logicalSwitchCredentials": [
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"}]},
    {"connectionProperties": [{"propertyName": "SshBasicAuthCredentialUser", "value": "admin", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SshBasicAuthCredentialPassword", "value": "Welcome@123", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3User", "value": "harish1", "valueFormat": "Unknown", "valueType": "String"},
                              {"propertyName": "SnmpV3AuthorizationPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"},
                              {"propertyName": "SnmpV3PrivacyPassword", "value": "12iso*help", "valueFormat": "SecuritySensitive", "valueType": "String"}]}]}]

updateports1 = [{"portType": "Uplink", "portId": "1.1", "enabled": True, "portName": "1.1", "portStatus": "Linked", "type": "port"}]

updateports = [{"portType": "Uplink", "portId": "1.1", "portHealthStatus": "Disabled", "enabled": True, "portName": "1.1", "portStatus": "Unlinked", "type": "port"}]
updateports_false = [{"portType": "Uplink", "portId": "1.1", "portHealthStatus": "Disabled", "enabled": False, "portName": "1.1", "portStatus": "Unlinked", "type": "port"}]

ethernet_networks = [{'name': 'eth-10', 'type': 'ethernet-networkV300', 'vlanId': 10, 'purpose': 'General', 'smartLink': True,
                      'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
                     {'name': 'eth-11', 'type': 'ethernet-networkV300', 'vlanId': 10, 'purpose': 'General',
                      'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'}]

fcoe_networks = [{'name': 'FCOE-10', 'type': 'fcoe-networkV300', 'vlanId': 10},
                 {'name': 'FCOE-100', 'type': 'fcoe-networkV300', 'vlanId': 10},
                 {'name': 'FCOE-101', 'type': 'fcoe-networkV300', 'vlanId': 101}]

fc_networks = [{'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-1-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
               {'type': 'fc-networkV300', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'name': 'SAN-2-A', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}]

lig_tbird_1enc = {'type': 'logical-interconnect-groupV300',
                  'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enablePauseFloodProtection': True, 'enableRichTLV': False, 'interconnectType': 'Ethernet', 'dependentResourceUri': None, 'name': 'defaultEthernetSwitchSettings', 'category': None, 'uri': '/ethernetSettings'},
                  'description': None,
                  'name': 'LIG-bay3-1enc',
                  'interconnectMapTemplate':
                  {'interconnectMapEntryTemplates': [
                      {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                      {'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 6}, {'type': 'Enclosure', 'relativeValue': 1}]}, 'permittedInterconnectTypeUri': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}]},
                  'enclosureType': 'SY12000', 'enclosureIndexes': [1], 'interconnectBaySet': '3',
                  'redundancyType': 'Redundant', 'internalNetworkUris': [],
                  'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': None, 'snmpAccess': None, 'enabled': True, 'description': None, 'name': None, 'state': None, 'category': 'snmp-configuration'},
                  'qosConfiguration': None,
                  'uplinkSets': [
                      {'networkUris': ['eth-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 61}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                       'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'eth-100'},
                      {'networkUris': ['SAN-1-A'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 72}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                       'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'name': 'SAN-1-A'},
                      {'networkUris': ['FCOE-100'], 'mode':'Auto', 'lacpTimer':'Short', 'primaryPort':None,
                       'logicalPortConfigInfos':[{'desiredSpeed': 'Auto', 'logicalLocation': {'locationEntries': [{'type': 'Bay', 'relativeValue': 3}, {'type': 'Port', 'relativeValue': 66}, {'type': 'Enclosure', 'relativeValue': 1}]}}],
                       'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'name': 'FCOE-100'}
                  ]}
con_data = [{"portName": "1.3", "speed": None, "vendorName": "CISCO-AVAGO     ", "vendorPartNumber": "SFBR-709SMZ-CS1 ", "vendorRevision": "G4.1", "vendorOui": "--", "extIdentifier": "4",
             "serialNumber": "AVD2020A1J0     ", "identifier": "SFP", "connector": "CISCO_10Gbase_SR"}, {"portName": "1.5", "speed": None, "vendorName": "CISCO-FINISAR   ",
                                                                                                         "vendorPartNumber": "FTLX8570D3BCL-C2", "vendorRevision": "A   ", "vendorOui": "--", "extIdentifier": "4", "serialNumber": "FNS18231A7U     ",
                                                                                                         "identifier": "SFP", "connector": "FET_10G"}]

li_1enc = {'name': 'LE_1Enc-LIG-bay3-1enc'}

enc_groups_1enc = [{'name': 'EG_1Enc_Bay3',
                    'type': 'EnclosureGroupV300',
                    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                    'stackingMode': 'Enclosure',
                    'ipAddressingMode': 'External',
                    'interconnectBayMappingCount': 0,
                    'enclosureCount': 1,
                    'configurationScript': None,
                    'interconnectBayMappings':
                    [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc'},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG-bay3-1enc'}
                     ]}]

les_potash_1enc = {'name': 'LE_1Enc', 'enclosureUris': ['ENC:EM1FFFF500'],
                   'enclosureGroupUri': 'EG:EG_1Enc_Bay3',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

ICM_powercycle = [{'op': 'replace', 'path': '/deviceResetState', 'value': 'Reset'}]

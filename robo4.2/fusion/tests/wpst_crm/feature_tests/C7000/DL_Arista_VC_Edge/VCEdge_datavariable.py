def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}
LSG1 = 'LSG_ARISTA'
LSG_new = 'LSG_new'
LS1 = 'LS_ARISTA'
LS_new = 'LS_new'
SWITCH1 = '15.186.17.219'
SWITCH2 = '15.186.17.208'
SWITCH1_USER = 'admin'
SWITCH1_PASS = 'password'
Switch_type = 'Arista 7050SX'
ARISTA_IPS = ['15.186.17.219', '15.186.17.208']
ARISTA_IPS_1 = ['15.186.17.219']
invalid_username = ['admin123', 'password$%^&^', '!@#$%^&*()#$%^&#$%^^&&**((', '1234567890qwerty@#']
invalid_password = ['password123', 'admin$%^&^', '!@#$%^&*()#$%^&#$%^^&&**((fdfsdfsdf', '1234567890qwerty@#']
reboot_command = 'reload'
SERVER_NAME = ['ILOMXQ7340093']
Port_Name = ["1", "1"]
switch1_port = ['1', '1']
switch2_port = ['2', '2']
uplink_stacking_port = '54.1'
UnlinkedPort_Name = ["12", "12"]
consistencyStatus = 'CONSISTENT'
advanced_statistics = [{"ifInOctets": "", "ifOutOctets": "", "ifInUcastPkts": "", "ifOutUcastPkts": ""}, {"ifInOctets": "", "ifOutOctets": "", "ifInUcastPkts": "", "ifOutUcastPkts": ""}]

advanced_statistics_uplink = [{"ifInOctets": "", "ifOutOctets": "", "ifInUcastPkts": "", "ifOutUcastPkts": ""}, {"ifInOctets": "", "ifOutOctets": "", "ifInUcastPkts": "", "ifOutUcastPkts": ""}]
Network_delete_message_in_sp = "An error has occurred on connection "
Network_delete_message_in_switch = "Connection on downlink port"
varTrue = True
varFalse = False
Alert = ['Active', 'Locked', 'Cleared']

invalid_switch_cred_err_msg = "Credentials for switch failed."
invalid_switch_ip_err_msg = "Unable to establish a connection to the switch."

lsgs = [{'name': LSG1,
         'type': 'logical-switch-groupV4',
         'switchMapTemplate': {'switchMapEntryTemplates': [
             {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
              'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}, {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                                                               'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}
         ]}},
        {'name': LSG1,
         'type': 'logical-switch-groupV4',
         'switchMapTemplate': {'switchMapEntryTemplates': [
                               {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
                                'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}, {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                                                                                 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}
                               ]}},
        {'name': LSG1,
         'type': 'logical-switch-groupV4',
         'switchMapTemplate': {'switchMapEntryTemplates': [
                               {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
                                'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}, {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                                                                                 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}
                               ]}},

        ]
username = {"propertyName": "SshBasicAuthCredentialUser", "value": SWITCH1_USER, "valueFormat": "Unknown",
            "valueType": "String"}
password = {"propertyName": "SshBasicAuthCredentialPassword", "value": SWITCH1_PASS,
            "valueFormat": "SecuritySensitive", "valueType": "String"}
property1 = [{"connectionProperties": [
    username, password
]},
    {"connectionProperties": [
        username, password,
    ]}]

# TODO - new managementLevel enum:  BASIC_MANAGED, MONITORED
lss = [{"logicalSwitch": {"name": LS1, "state": "Active", "type": "logical-switchV4", "managementLevel": "BASIC_MANAGED",
                          "logicalSwitchGroupUri": "LSG:" + LSG1,
                          "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "None"},
                                                             "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                     "privacyProtocol": None,
                                                                                     "securityLevel": None},
                                                             "logicalSwitchManagementHost": SWITCH1,
                                                             "snmpVersion": "SNMPv1", "snmpPort": 0}, {"snmpV1Configuration": {"communityString": "None"},
                                                                                                       "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                                                               "privacyProtocol": None,
                                                                                                                               "securityLevel": None},
                                                                                                       "logicalSwitchManagementHost": SWITCH2,
                                                                                                       "snmpVersion": "SNMPv1", "snmpPort": 0}]},
        "logicalSwitchCredentials": property1},
       {"logicalSwitch": {"name": LS1, "state": "Active", "type": "logical-switchV4", "managementLevel": "BASIC_MANAGED",
                          "logicalSwitchGroupUri": "LSG:" + LSG1,
                          "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "None"},
                                                             "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                     "privacyProtocol": None,
                                                                                     "securityLevel": None},
                                                             "logicalSwitchManagementHost": SWITCH1,
                                                             "snmpVersion": "SNMPv1", "snmpPort": 0}, {"snmpV1Configuration": {"communityString": "None"},
                                                                                                       "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                                                               "privacyProtocol": None,
                                                                                                                               "securityLevel": None},
                                                                                                       "logicalSwitchManagementHost": SWITCH2,
                                                                                                       "snmpVersion": "SNMPv1", "snmpPort": 0}]},
        "logicalSwitchCredentials": property1},
       {"logicalSwitch": {"name": LS1, "state": "Active", "type": "logical-switchV4", "managementLevel": "BASIC_MANAGED",
                          "logicalSwitchGroupUri": "LSG:" + LSG1,
                          "switchCredentialConfiguration": [{"snmpV1Configuration": {"communityString": "None"},
                                                             "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                     "privacyProtocol": None,
                                                                                     "securityLevel": None},
                                                             "logicalSwitchManagementHost": SWITCH1,
                                                             "snmpVersion": "SNMPv1", "snmpPort": 0}, {"snmpV1Configuration": {"communityString": "None"},
                                                                                                       "snmpV3Configuration": {"authorizationProtocol": None,
                                                                                                                               "privacyProtocol": None,
                                                                                                                               "securityLevel": None},
                                                                                                       "logicalSwitchManagementHost": SWITCH2,
                                                                                                       "snmpVersion": "SNMPv1", "snmpPort": 0}]},
        "logicalSwitchCredentials": property1},

       ]

fcoenets = [
    {
        "name": "fcoe1",
        "vlanId": "1602",
        "type": "fcoe-networkV4"
    }, ]

fcnets = [
    {
        "name": "fc1",
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "type": "fc-networkV4"
    }, ]


# NS_nw_names = ['Net_Vlan30', 'Net_Vlan40']


power_delivery_device = {"name": "Arista_power_device", "deviceType": "RackPdu", "model": "DCS-7050SX-72Q-R", "ratedCapacity": "3", "lineVoltage": "2", "phaseType": "SinglePhase", "feedIdentifier": "A", "partNumber": "", "serialNumber": "", "powerConnections": [{"connectionUri": "", "deviceConnection": 1}, {"connectionUri": "", "deviceConnection": 2}, {"connectionUri": "", "deviceConnection": 1}, {"connectionUri": "", "deviceConnection": 2}]}
power_delivery_device1 = {"name": "Arista_power_device", "deviceType": "RackPdu", "model": "DCS-7050SX-72Q-R", "ratedCapacity": "3", "lineVoltage": "2", "phaseType": "SinglePhase", "feedIdentifier": "A", "partNumber": "", "serialNumber": "", "id": "", "uuid": "", "eTag": "", "powerConnections": [{"connectionUri": "", "deviceConnection": 1}, {"connectionUri": "", "deviceConnection": 2}, {"connectionUri": "", "deviceConnection": 1}, {"connectionUri": "", "deviceConnection": 2}]}

Power_delivery_device_name = "Arista_power_device"


Switch_validate_list = ["JPE17140684", "4.19.0F", "Configured", "15.186.17.219", "1", "primary", "JPE16182019", "4.19.0F", "Configured", "15.186.17.208", "2", "secondary"]
Switch1_validate_list = ["JPE17140684", "4.19.0F", "Configured", "15.186.17.219", "1", "primary"]
Switch2_validate_list = ["JPE16182019", "4.19.0F", "Configured", "15.186.17.208", "2", "secondary"]
vpc_peer_mlag_switch1 = ["10.0.0.2", "Port-Channel10", "15.186.17.208", "up", "4094", "mlag1", "JPE17140684"]
vpc_peer_mlag_switch2 = ["10.0.0.1", "Port-Channel10", "15.186.17.219", "up", "4094", "mlag1", "JPE16182019"]


switch_ip = ['15.186.17.219', '15.186.17.208']
# interface = 4
switch_details = {'userName': 'admin', 'password': 'password'}
Commands = ['enable', 'config', 'interface ethernet', 'no shutdown', 'shutdown', 'vlan', 'switchport mode access', 'switchport access vlan', 'no vlan', 'show vlan', 'show active', 'switchport trunk allowed vlan', 'switchport trunk native vlan', 'write']
pattern = 'allowed vlan'
SHT_names = "DL360 Gen10 1"
sample = ['10', '10']


invalid_networks = [{'name': 'net_101', 'type': 'ethernet-networkV4', 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
                    {'name': 'net_102', 'type': 'ethernet-networkV4', 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tunnel'}]
Neg_lsg_invalid = {'state': 'Active', 'type': 'logical-switch-groupV4', 'name': 'Neg_LSG', 'switchMapTemplate': {'switchMapEntryTemplates': [{'logicalLocation': {'locationEntries': [{'relativeValue': '1', 'type': 'StackingMemberId'}]}, 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}, {'logicalLocation': {'locationEntries': [{'relativeValue': '2', 'type': 'StackingMemberId'}]}, 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}, {'logicalLocation': {'locationEntries': [{'relativeValue': '3', 'type': 'StackingMemberId'}]}, 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}]}}
Valdict_invalid = {'status_code': 400, 'errorCode': 'CRM_INVALID_NUMBER_OF_ARISTA_SWITCHES_IN_LOGICAL_SWITCH_GROUP', 'message': 'Unable to create logical switch group for Arista 7050SX switches. Minimum supported number of switches for this logical switch group type is 2.'}
Neg_lsg_negative = {'state': 'Active', 'type': 'logical-switch-groupV4', 'name': 'Neg_LSG', 'switchMapTemplate': {'switchMapEntryTemplates': [{'logicalLocation': {'locationEntries': [{'relativeValue': '-1', 'type': 'StackingMemberId'}]}, 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}, {'logicalLocation': {'locationEntries': [{'relativeValue': '2', 'type': 'StackingMemberId'}]}, 'permittedSwitchTypeUri': 'SWT:Arista 7050SX'}]}}
Valdict_negative = {'status_code': 400, 'errorCode': 'CRM_MISSING_LOGICAL_SWITCH_MAP_MEMBER_ID', 'message': 'The member ID 1 should be present but is not found in the switch map'}
Valdict_profile = {'status_code': 200, 'taskErrors': [{'errorCode': 'RACKEDGE_CONNECTION_INVALID_NETWORK_TYPE', 'message': 'Only tagged networks are allowed for DL Server connection 1', 'errorSource': None, 'recommendedActions': ['Select a tagged network for connection 1.'], 'nestedErrors':[], 'details':'', 'data':{}}], 'taskState': 'Error'}
server_profile_dl = {'type': 'ServerProfileV9', 'serverHardwareUri': '', 'serverHardwareTypeUri': '', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'name': '', 'description': '', 'affinity': None, 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': '0', 'networkUri': '', 'mac': None, 'wwpn': '', 'wwnn': ''}]}}

Val_list = ['LogicalSwitchCollectionV4', 'CONSISTENT', 'mlag1', SWITCH1, SWITCH2, 'Configured', '4.19.0F', 'DCS-7050SX-72Q-R']
No_of_servers = 8
# DL_server_names = ['ILOMXQ7320BDJ','ILO2M2732010V']
# The command order should not be changed
Commands = ['enable', 'config', 'interface ethernet', 'no shutdown', 'shutdown', 'vlan', 'switchport mode access', 'switchport access vlan', 'no vlan', 'show vlan', 'show active']
Uplink_Port_No = "54/1"
Port_No = "4"
Vlan_Id = "10"
Alert_Messages = ['The overall status of the system network is critical.', 'Connection deployed on downlink port 6.', 'An error has occurred on connection 1.']
server_profile_1 = {'type': 'ServerProfileV9', 'serverHardwareUri': 'DL_server_names[0]',
                    'serverHardwareTypeUri': '',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': None,
                    'boot': {'manageBoot': False},
                    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                    'connectionSettings': {'connections': [
                        {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                         'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                       'wwnn': None},
                        {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                         'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                       'wwnn': None}
                    ]}}
Network_1 = {'connectionTemplateUri': None,
             'ethernetNetworkType': 'Tagged',
             'name': 'Net_Vlan10',
             'privateNetwork': False,
             'purpose': 'General',
             'smartLink': True,
             'type': 'ethernet-networkV4',
             'vlanId': 10
             }

Arista_switch_details = {'ip': '15.186.17.219', 'userName': 'admin', 'password': 'password'}
# The command order should not be changed
Commands = ['enable', 'config', 'interface ethernet', 'no shutdown', 'shutdown', 'vlan', 'switchport mode access', 'switchport access vlan', 'no vlan', 'show vlan', 'show active', 'switchport trunk allowed vlan', 'switchport trunk native vlan', 'write']
Uplink_Port_No = "54/1"
downlink_Port_No = "2"
Vlan_Id = "10"
Vlan_Id_Format = "0010"
port_details = [{'type': 'port', 'portType': 'Downlink', 'portId': '', 'portHealthStatus': 'Normal', 'enabled': '', 'portName': '', 'portStatus': 'Linked'}]
Alert_Messages = ['The overall status of the system network is critical.', 'Connection deployed on downlink port 6.', 'An error has occurred on connection 1.']
status_code = '200'
Err_Msg = 'CRM_INVALID_SWITCH_CREDENTIALS'

TeamName1 = 'NS1_Conn1'

TeamName1_VlanID1 = '10'
TeamName1_VlanID2 = '20'
TeamName1_VlanID3 = '30'

Team1_Adapter1_Name = 'Embedded Flexible LOM 1 Port 1'

linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password",
                 "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

ilo_details = [{'ilo_ip': '15.186.15.14', 'username': 'Administrator', 'password': 'hpvse123'}, {'ilo_ip': '15.186.15.49', 'username': 'Administrator', 'password': 'hpvse123'}]

server_details = ['Administrator', 'hpvse@123']

win_server_details = {"ip": '15.186.15.49', "username": "Administrator", "password": "hpvse123"}
win_ilo_details = [{'ip': '15.186.15.14', 'username': 'Administrator', 'password': 'hpvse123'}, {"ip": '15.186.15.49', "username": "Administrator", "password": "hpvse123"}]
win_server_telnet_details = {"username": "Administrator", "password": "hpvse@123"}

delete_team_cmd1 = "Remove-NetLbfoTeam 'NS1_conn1'"
delete_team_cmd2 = "Remove-NetLbfoTeam 'NS2_conn2'"
delete_team_cmd_native = "Remove-NetLbfoTeam 'NS1_conn1_native'"
delete_team_cmd_native_edit = "Remove-NetLbfoTeam 'NS1_conn1_native_edit'"

team_cmd1 = "PowerShell.exe"
team_cmd2 = " -ExecutionPolicy Bypass -File .\\create_team.ps1"
team_cmd = "PowerShell.exe -ExecutionPolicy Bypass -File .\\create_team.ps1"
ps_cmd = "Powershell.exe -File C:\\Users\\Administrator\\Desktop\\create_team.ps1"

ps_cmd1 = "Powershell.exe -File C:\\Users\\Administrator\\Desktop\\team_70_20_30.ps1"
ps_cmd2 = "Powershell.exe -File C:\\Users\\Administrator\\Desktop\\team_edit_40_50_60.ps1"
# ######## Path will change #####
module_file_path = "C:\\TH_4_10\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\DL_ARista_Integration\\GetServerIPs.py"

IPpppp_list = [['192.168.30.24', '192.168.40.25'], ['192.168.20.22', '192.168.50.10'], [u'192.168.30.26', u'192.168.40.27'], ['192.168.20.33', '192.168.50.99']]

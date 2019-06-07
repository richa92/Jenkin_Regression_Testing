def rlist(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


# the following parameters have to be changed when we get a new hardware: Plexxi connect credentials, Appliance variables, switch details, LSG, server hardware details, profiles

# Plexxi connect credentials
plexxi_connect_host = '15.186.27.170'
plexxi_connect_version = '5.0'
plexxi_connect_user = 'admin'
plexxi_connect_password = 'plexxi'
switch_login = 'admin'
switch_password = 'plexxi'
sudo_password = 'plexxi'
switch_login_prompt = '$'
sudo_command = 'sudo px-shell'
sudo_login_prompt = 'admin:'
sudo_password_prompt = '[sudo] password for admin:'
plexxi_switch_prompt = '>'
# Appliance variables
APPLIANCE_IP_4_20 = '15.186.31.85'
Fabric_name = 'Composable Fabric'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
new_admin_credentials = {'userName': 'Administrator', 'password': 'hpvse1234'}
plexxi_credentials = {"current_password": "plexxi123", "new_password": "plexxi"}
new_credentials_plexxi = {"current_password": "plexxi", "new_password": "plexxi123"}

RACKS = '3'
Rack_length = RACKS + 1

# switch details
plexxi_Switch_IPS = {'Rack_1': ['15.186.12.49', '15.186.12.50'], 'Rack_2': ['15.186.12.59', '15.186.12.60'], 'Rack_3': ['15.186.12.69', '15.186.12.70']}

Plexxi_switch_names = {'Rack_1': ['plexxiR1S1', 'plexxiR1S2'], 'Rack_2': ['plexxiR2S1', 'plexxiR2S2'], 'Rack_3': ['plexxiR3S1', 'plexxiR3S2']}

switch_names = ['plexxiR1S1', 'plexxiR1S2', 'plexxiR2S1', 'plexxiR2S2', 'plexxiR3S1', 'plexxiR3S2']

LS_neg_switches = ['plexxiR3S1', 'plexxiR2S1']

Switch_details = [{'name': 'plexxiR1S1', 'modelName': 'Composable Fabric FM 3180', 'firmwareVersion': '0-bamboo-master-2018100601', 'state': 'Configured', 'chassisId': 'E0:39:D7:84:12:00'}, {'name': 'plexxiR1S2', 'modelName': 'Composable Fabric FM 3180', 'firmwareVersion': '0-bamboo-master-2018100601', 'state': 'Configured', 'chassisId': 'E0:39:D7:84:14:00'}, {'name': 'plexxiR2S1', 'modelName': 'Composable Fabric FM 3180', 'firmwareVersion': '0-bamboo-master-2018100601', 'state': 'Configured', 'chassisId': 'E0:39:D7:84:17:80'}, {'name': 'plexxiR2S2', 'modelName': 'Composable Fabric FM 3180', 'firmwareVersion': '0-bamboo-master-2018100601', 'state': 'Configured', 'chassisId': 'E0:39:D7:84:17:00'}, {'name': 'plexxiR3S1', 'modelName': 'Composable Fabric FM 3180', 'firmwareVersion': '0-bamboo-master-2018100601', 'state': 'Configured', 'chassisId': 'E0:39:D7:84:25:80'}, {'name': 'plexxiR3S2', 'modelName': 'Composable Fabric FM 3180', 'firmwareVersion': '0-bamboo-master-2018100601', 'state': 'Configured', 'chassisId': 'E0:39:D7:84:28:00'}]

# LSG
LSG = 'LSG'
LSG_new = 'LSG_new'

vlan_network = ['10', '20']

vlan_NS = [['10', '20'], ['30', '40']]

# server hardware details

DH_380_IPs = {'Rack_1': ['15.186.30.39', '15.186.30.32'], 'Rack_2': ['15.186.24.219', '15.186.24.205'], 'Rack_3': ['15.186.24.211']}

DH_360_Ips = {'Rack_1': ['15.186.16.182', '15.186.16.151'], 'Rack_2': ['15.186.22.246', '15.186.24.217', '15.186.24.77', '15.186.24.216', '15.186.24.209', '15.186.24.218'], 'Rack_3': ['15.186.24.222', '15.186.24.213', '15.186.24.214', '15.186.24.212', '15.186.24.65', '15.186.24.220']}

DH_360_Serverhardwares = {'Rack_1': [], 'Rack_2': [], 'Rack_3': []}

DH_380_Serverhardwares = {'Rack_1': [], 'Rack_2': [], 'Rack_3': []}

serverhardwares = {'Rack_1': ['ILOMXQ733085B'], 'Rack_2': ['ILOMXQ82505G5'], 'Rack_3': ['ILOMXQ82505GQ']}

config_type = ['same_nw', 'diff_nw', 'same_ns', 'diff_ns']

error_messages_sp = ['RACKEDGE_CONNECTION_INVALID_NETWORK_TYPE', 'NetworkNotMatchFunctionType', 'NetworkNotMatchFunctionType']

alert_msg = ['Unable to establish communication with the Composable Fabric Manager at 15.186.31.239.', 'Communication with the Composable Fabric Manager is restored.', 'An error has occurred on connection 1.  Network Net_Vlan_10 assigned to this connection was deleted.', 'An error has occurred on connection 1.  Network set Net_Set_1 assigned to this connection was deleted.']

ls_names = ['LS1', 'LS2', 'LS3']

# profiles
single_ns_Serverhardware = ['ILO2M2732010R']
single_nw_Serverhardware = ['ILOMXQ82505GT']
single_lnw_Serverhardware = ['ILO2M2732010Q']

portName = '1'
windows_details = {"username": "Administrator", "password": "password@123"}
redhat_details = {"username": "root", "password": "password@123"}
server_Auth_details = {"username": "", "password": ""}
Server_details = {"ip": '', "username": '', "password": ''}

win_server_details = {"ip": '', "username": "Administrator", "password": "password@123"}

ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}

ilo_details1 = {'username': 'Administrator', 'password': 'hpvse123'}

windows_server_details = {'windows_ip': '', 'username': 'Administrator', 'password': 'password@123'}
disable_server_interface = 'ILOMXQ82503C0'
ilo_details_WI = {'ip': '15.186.24.218', 'username': 'Administrator', 'password': 'hpvse123'}

ilo_details_SNW = {'ip': '15.186.24.212', 'username': 'Administrator', 'password': 'hpvse123'}

ping_cmd = "ping 'ppppp'"
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp' -TeamingMode 'LACP'"
Powershell_get_mac2 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp'"
Powershell_get_mac3 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq'"
Powershell_get_mac4 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
tagging_cmd = "Add-NetLbfoTeamNIC -Team 'Team1' -VlanID 'vlan_id'"
remove_tagging_cmd = "Remove-NetLbfoTeamNIC -Team 'Team1' -VlanID 'vlan_id'"

interface_disable = "Disable-NetAdapter -Name 'name'"
interface_enable = "Enable-NetAdapter -Name 'name'"


profiles = {b'Rack_1': ['ILO2M2732010R'], b'Rack_2': ['ILO2M2733056R', 'ILOMXQ82505G6'], b'Rack_3': ['ILOMXQ82503CP', 'ILOMXQ82505GQ']}

name = ['ping0.txt', 'ping1.txt', 'ping2.txt', 'ping3.txt']

number = '4'
Ping_Lost = 'Lost'

profiles_team = ['ILOMXQ82503C0', 'ILOMXQ82505GD']
profile_LAG_name = ['ILOMXQ82505GN']
profile_LAG_LNS_name = ['ILOMXQ82503C0']
profile_LAG_RNS_name = ['ILOMXQ82505G7']

Profiles_10 = ['']

DL_SH_body = {"hostname": "enc-ilo.corp.com",
              "username": "Administrator",
              "password": "hpvse123",
              "force": True,
              "licensingIntent": "OneView",
              # "licensingIntent":"OneViewNoiLO",
              "configurationState": "Managed",
              }

disable_access_port = [{'portType': 'Downlink', 'portId': '', 'portHealthStatus': 'Normal', 'enabled': False, 'portName': '', 'portStatus': 'Linked', 'type': 'portV5'}]

enable_access_port = [{'portType': 'Downlink', 'portId': '', 'portHealthStatus': 'Normal', 'enabled': True, 'portName': '', 'portStatus': 'Linked', 'type': 'portV5'}]

Fabric_claim = [{"op": "replace", "path": "/state", "value": "Adding"}]

refresh_body = [{"op": "replace", "path": "/refreshState", "value": "RefreshPending"}]

Reapply_fabric = [{"op": "replace", "path": "/reapplyState", "value": "ApplyPending"}]  # not yet developed, need to develop later

user_passwrd_body = {"type": "UserAndPermissions", "userName": "administrator", "fullName": "Default appliance administrator", "currentPassword": "hpvse123", "password": "hpvse1234", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "replaceRoles": False, "permissions": []}
user_passwrd_body1 = {"type": "UserAndPermissions", "userName": "administrator", "fullName": "Default appliance administrator", "currentPassword": "hpvse1234", "password": "hpvse123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "replaceRoles": False, "permissions": []}

lsgs = {'name': LSG,
        'type': 'logical-switch-groupV4',
        'switchMapTemplate': {'switchMapEntryTemplates': [
            {'logicalLocation': {'locationEntries': [{'relativeValue': 1, 'type': 'StackingMemberId'}]},
             'permittedSwitchTypeUri': SWITCH_TYPE}, {'logicalLocation': {'locationEntries': [{'relativeValue': 2, 'type': 'StackingMemberId'}]},
                                                      'permittedSwitchTypeUri': SWITCH_TYPE}
        ]}}

lss = [{"logicalSwitch": {"name": " ",
                          "managementLevel": "BASIC_MANAGED",
                          "type": "logical-switchV5", "switchMap": None, "switchCredentialConfiguration": None, "logicalSwitchGroupUri": 'LSG:' + LSG, "initialScopeUris": [], "switchUris":[]}, "logicalSwitchCredentials":None}]

ls1 = [{"logicalSwitch": {"name": " ",
                          "managementLevel": "BASIC_MANAGED",
                          "type": "logical-switchV5", "switchMap": None, "switchCredentialConfiguration": None, "logicalSwitchGroupUri": 'LSG:' + LSG, "initialScopeUris": [], "switchUris":[]}, "logicalSwitchCredentials":None}]

bulk_networks_4000 = {
    'vlanIdRange': '1-4000',
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-networkV1',
    'bandwidth': {
        'maximumBandwidth': 10000,
        'typicalBandwidth': 2000}
}

ethnets = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Net_Vlan_10",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Net_Vlan_20",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Net_Vlan_30",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 30
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "Net_Vlan_40",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 40
    }]

net_vlan4001 = [{
    "type": "ethernet-networkV4",
    "ethernetNetworkType": "Tagged",
    "name": "net_4001",
    "privateNetwork": False,
    "purpose": "General",
    "smartLink": True,
    "vlanId": 4001
}]
Untagged_network = [{
    'name': 'untaggednet',
    'type': 'ethernet-networkV4',
    'vlanId': None,
    'purpose': 'General',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Untagged'
}]

fc_netowrks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'FC1',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

FCoE_network = [
    {
        "name": "FCOE",
        "vlanId": "1002",
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": "fcoe-networkV4",
        "initialScopeUris": []
    }
]

network_sets = [
    {'name': 'Net_Set_1', 'type': 'network-setV4', 'networkUris': ['Net_Vlan_10', 'Net_Vlan_20'],
     'nativeNetworkUri': None},
    {'name': 'Net_Set_2', 'type': 'network-setV4', 'networkUris': ['Net_Vlan_30', 'Net_Vlan_40'],
     'nativeNetworkUri': None}]

network_sets1 = [
    {'name': 'Net_Set_1', 'type': 'network-setV4', 'networkUris': ['Net_Vlan_10', 'Net_Vlan_20'],
     'nativeNetworkUri': None}
]
network_sets_4000 = [{'name': 'netset_4000', 'type': 'network-setV4', 'networkSetType': 'Large', 'networkUris': rlist(1, 4000, prefix='net_'),
                      'nativeNetworkUri': None}]

network_sets_4001 = [{'name': 'netset_4001', 'type': 'network-setV4', 'networkSetType': 'Large', 'networkUris': rlist(1, 4001, prefix='net_'),
                      'nativeNetworkUri': None}]

network_sets_neg = [
    {'name': 'Net_Set_3', 'type': 'network-setV4', 'networkUris': ['Net_Vlan_10', 'net_4001'],
     'nativeNetworkUri': None},
    {'name': 'Net_Set_4', 'type': 'network-setV4', 'networkUris': ['Net_Vlan_20', 'net_4001'],
     'nativeNetworkUri': None}]

update_ns_del = [{'name': 'Net_Set_1', 'delete_networkUris': ['Net_Vlan_20']}]
update_ns_add = [{'name': 'Net_Set_1', 'add_networkUris': ['Net_Vlan_10', 'Net_Vlan_20']}]

oneview_config = [
    {
        "host": APPLIANCE_IP_4_20,
        "username": admin_credentials['userName'],
        "password": admin_credentials['password'],
        "description": "",
        "enabled": True,
        "verify_ssl": True,
        "name": "HPE OneView Configuration"
    }
]
profile_template_networks = [{'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                              'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
                              'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                              'name': 'DL380_sn_Template', 'description': '', 'affinity': None,
                              "boot": None, 'bootMode': {'manageMode': False},
                              'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_10', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                                     {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_10', 'ipv4': {}}], "manageConnections": True}},

                             {'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                              'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
                              'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                              'name': 'DL360_sn_Template', 'description': '', 'affinity': None,
                              "boot": None, 'bootMode': {'manageMode': False},
                              'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_10', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                                     {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_10', 'ipv4': {}}], "manageConnections": True}}]

Edit_template_network = [{'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                          'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
                          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': 'DL380_sn_Template', 'description': '', 'affinity': None,
                          "boot": None, 'bootMode': {'manageMode': False},
                          'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_10', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                                 {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_20', 'ipv4': {}}], "manageConnections": True}},

                         {'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                          'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
                          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': 'DL360_sn_Template', 'description': '', 'affinity': None,
                          "boot": None, 'bootMode': {'manageMode': False},
                          'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_10', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                                 {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan_20', 'ipv4': {}}], "manageConnections": True}}]

profile_template_ns = [{'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                        'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'DL380_snw_Template', 'description': '', 'affinity': None,
                        "boot": None, 'bootMode': {'manageMode': False},
                        'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_1', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                               {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_1', 'ipv4': {}}], "manageConnections": True}},

                       {'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                        'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'DL360_snw_Template', 'description': '', 'affinity': None,
                        "boot": None, 'bootMode': {'manageMode': False},
                        'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_1', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                               {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_1', 'ipv4': {}}], "manageConnections": True}}]

Edit_template_ns = [{'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                     'serverHardwareTypeUri': 'SHT:DL380 Gen10 1',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'DL380_snw_Template', 'description': '', 'affinity': None,
                     "boot": None, 'bootMode': {'manageMode': False},
                     'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_1', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                            {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_2', 'ipv4': {}}], "manageConnections": True}},

                    {'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                     'serverHardwareTypeUri': 'SHT:DL360 Gen10 1',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'DL360_snw_Template', 'description': '', 'affinity': None,
                     "boot": None, 'bootMode': {'manageMode': False},
                     'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_1', 'requestedVFs': 'Auto', 'ipv4': {}},
                                                            {'id': 2, 'name': 'c2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2', 'requestedMbps': 0, 'networkUri': 'NS:Net_Set_2', 'ipv4': {}}], "manageConnections": True}}]


profile = {'type': 'ServerProfileV10', 'serverHardwareUri': '', 'serverProfileTemplateUri': ''}

Server_profiles_neg_nw = [{'type': 'ServerProfileV10', 'serverHardwareUri': '',
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': '', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections': [
                               {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                'networkUri': 'ETH:untaggednet', 'mac': None, 'wwpn': None,
                                'wwnn': None}

                           ]}},
                          {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': '', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections': [
                               {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                'networkUri': 'FC:FC1', 'mac': None, 'wwpn': None,
                                'wwnn': None}

                           ]}},
                          {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': '', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections': [
                               {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                'networkUri': 'FCOE:FCOE', 'mac': None, 'wwpn': None,
                                'wwnn': None}

                           ]}}]


server_profile_sn = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                     'serverHardwareTypeUri': '',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': '', 'description': '', 'affinity': None,
                     'boot': {'manageBoot': False},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                     'connectionSettings': {'connections': [
                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                       'networkUri': 'ETH:Net_Vlan_10', 'mac': None, 'wwpn': None,
                                       'wwnn': None},
                             {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                       'networkUri': 'ETH:Net_Vlan_10', 'mac': None, 'wwpn': None,
                                       'wwnn': None}
                     ]}}

server_profile_dn = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                     'serverHardwareTypeUri': '',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': '', 'description': '', 'affinity': None,
                     'boot': {'manageBoot': False},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                     'connectionSettings': {'connections': [
                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                       'networkUri': 'ETH:Net_Vlan_10', 'mac': None, 'wwpn': None,
                                       'wwnn': None},
                             {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                       'networkUri': 'ETH:Net_Vlan_20', 'mac': None, 'wwpn': None,
                              'wwnn': None}
                     ]}}

server_profile_sns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                      'serverHardwareTypeUri': '',
                      'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                      'name': '', 'description': '', 'affinity': None,
                      'boot': {'manageBoot': False},
                      "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                      'connectionSettings': {'connections': [
                          {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                           'networkUri': 'NS:Net_Set_1', 'mac': None, 'wwpn': None,
                           'wwnn': None},
                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                           'networkUri': 'NS:Net_Set_1', 'mac': None, 'wwpn': None,
                           'wwnn': None}
                      ]}}

server_profile_dns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                      'serverHardwareTypeUri': '',
                      'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                      'name': '', 'description': '', 'affinity': None,
                      'boot': {'manageBoot': False},
                      "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                      'connectionSettings': {'connections': [
                          {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                           'networkUri': 'NS:Net_Set_1', 'mac': None, 'wwpn': None,
                           'wwnn': None},
                          {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                           'networkUri': 'NS:Net_Set_2', 'mac': None, 'wwpn': None,
                           'wwnn': None}
                      ]}}

server_profile_4000_ns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                          'serverHardwareTypeUri': '',
                          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': '', 'description': '', 'affinity': None,
                          'boot': {'manageBoot': False},
                          "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                          'connectionSettings': {'connections': [
                              {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                               'networkUri': 'NS:netset_4000', 'mac': None, 'wwpn': None,
                               'wwnn': None},
                              {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                               'networkUri': 'NS:netset_4000', 'mac': None, 'wwpn': None,
                               'wwnn': None}
                          ]}}

server_profile_4001_nw = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                          'serverHardwareTypeUri': '',
                          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': '', 'description': '', 'affinity': None,
                          'boot': {'manageBoot': False},
                          "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                          'connectionSettings': {'connections': [
                              {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                               'networkUri': 'ETH:net_4001', 'mac': None, 'wwpn': None,
                               'wwnn': None},
                              {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                               'networkUri': 'ETH:net_4001', 'mac': None, 'wwpn': None,
                               'wwnn': None}
                          ]}}

server_profile_4001_ns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                          'serverHardwareTypeUri': '',
                          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': '', 'description': '', 'affinity': None,
                          'boot': {'manageBoot': False},
                          "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                          'connectionSettings': {'connections': [
                              {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                               'networkUri': 'NS:Net_Set_3', 'mac': None, 'wwpn': None,
                               'wwnn': None},
                              {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                               'networkUri': 'NS:Net_Set_4', 'mac': None, 'wwpn': None,
                               'wwnn': None}
                          ]}}

server_profile_nw_ns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                        'serverHardwareTypeUri': '',
                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': '', 'description': '', 'affinity': None,
                        'boot': {'manageBoot': False},
                        "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                        'connectionSettings': {'connections': [
                            {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                             'networkUri': 'ETH:Net_Vlan_10', 'mac': None, 'wwpn': None,
                             'wwnn': None},
                            {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                             'networkUri': 'NS:Net_Set_2', 'mac': None, 'wwpn': None,
                             'wwnn': None}
                        ]}}

server_profile_single_ns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                            'serverHardwareTypeUri': '',
                            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': '', 'description': '', 'affinity': None,
                            'boot': {'manageBoot': False},
                            "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                            'connectionSettings': {'connections': [
                                {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                 'networkUri': 'NS:Net_Set_1', 'mac': None, 'wwpn': None,
                                 'wwnn': None},

                            ]}}


server_profile_Large_ns = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': '', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections': [
                               {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                'networkUri': 'NS:netset_4000', 'mac': None, 'wwpn': None,
                                'wwnn': None},

                           ]}}

server_profile_single_nw = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                            'serverHardwareTypeUri': '',
                            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': '', 'description': '', 'affinity': None,
                            'boot': {'manageBoot': False},
                            "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                            'connectionSettings': {'connections': [
                                {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                 'networkUri': 'ETH:Net_Vlan_30', 'mac': None, 'wwpn': None,
                                 'wwnn': None},

                            ]}}

profile_LAG = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
               'serverHardwareTypeUri': '',
               'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
               'name': '', 'description': '', 'affinity': None,
               'boot': {'manageBoot': False},
               "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
               'connectionSettings': {'connections': [
                   {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                    'networkUri': 'ETH:Net_Vlan_10', 'lagName': 'LAG1', 'mac': None, 'wwpn': None,
                    'wwnn': None},
                   {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                    'networkUri': 'ETH:Net_Vlan_10', 'lagName': 'LAG1', 'mac': None, 'wwpn': None,
                    'wwnn': None}
               ]}}

profile_LAG_LNS = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                   'serverHardwareTypeUri': '',
                   'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': '', 'description': '', 'affinity': None,
                   'boot': {'manageBoot': False},
                   "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                   'connectionSettings': {'connections': [
                       {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                        'networkUri': 'NS:netset_4000', 'lagName': 'LAG1', 'mac': None, 'wwpn': None,
                        'wwnn': None},
                       {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                        'networkUri': 'NS:netset_4000', 'lagName': 'LAG1', 'mac': None, 'wwpn': None,
                        'wwnn': None}
                   ]}}

profile_LAG_RNS = {'type': 'ServerProfileV10', 'serverHardwareUri': '',
                   'serverHardwareTypeUri': '',
                   'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': '', 'description': '', 'affinity': None,
                   'boot': {'manageBoot': False},
                   "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                   'connectionSettings': {'connections': [
                       {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                        'networkUri': 'NS:Net_Set_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None,
                        'wwnn': None},
                       {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                        'networkUri': 'NS:Net_Set_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None,
                        'wwnn': None}
                   ]}}

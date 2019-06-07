from copy import deepcopy
import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'password@123'}

enc_count = 2
enc_cnt = 2

APPLIANCE_IP = '15.245.131.162'

FUSION_PROMPT = '#'
FUSION_IP = '15.245.131.162'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'password@123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_TIMEOUT = 180              # Timeout.  Move this out???

ethernet_network = [{"vlanId": "401",
                     "purpose": "Management",
                     "name": "Net-Vlan401",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "402",
                     "purpose": "Management",
                     "name": "Net-Vlan402",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "403",
                     "purpose": "Management",
                     "name": "Net-Vlan403",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "404",
                     "purpose": "Management",
                     "name": "Net-Vlan404",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    {"vlanId": "405",
                     "purpose": "Management",
                     "name": "Net-Vlan405",
                     "smartLink": False,
                     "privateNetwork": False,
                     "connectionTemplateUri": None,
                     "ethernetNetworkType": "Tagged",
                     "type": "ethernet-networkV4"},
                    ]

ENC1 = 'MXQ734024M'

network_sets = [{"name": "Netset1", "networkUris": ["Net-Vlan401"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None},
                {"name": "Netset2", "networkUris": ["Net-Vlan401", "Net-Vlan402", "Net-Vlan403"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None},
                {"name": "Netset3", "networkUris": ["Net-Vlan"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None}
                ]
update_network_sets = [{"name": "Netset1", "networkUris": ["Net-Vlan401"], "add_networkUris":["Net-Vlan402"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None}]
update_network_sets1 = [{"name": "Netset1", "networkUris": ["Net-Vlan401"], "delete_networkUris":["Net-Vlan402"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None}]

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': ' Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': ' Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

uplink_set = {
    'US_Vlan405': {
        'name': 'US_Vlan405',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net-Vlan405'],
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'}
        ]
    }}


LIG = 'LIG1'
LE = 'LE1'
ENC1 = 'MXQ734024M'
ENC2 = 'CN7545084B'
ligs = {
    'LIG1': {
        'name': 'LIG1',
        'type': 'logical-interconnect-groupV6',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
                                    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
                                    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                    ],
        'enclosureIndexes': [1, 2],
        'interconnectBaySet': 3,
        'uplinkSets': [uplink_set['US_Vlan405'].copy()],
        'redundancyType': 'HighlyAvailable',
        'internalNetworkUris': ['Net-Vlan401', 'Net-Vlan402', 'Net-Vlan403', 'Net-Vlan404'],
        'downlinkSpeedMode': 'SPEED_10GB',
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    }}

enc_group = {'name': 'EG1',
             'enclosureCount': 2,
             'interconnectBayMappings':
             [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
              ],
             'ipAddressingMode': 'DHCP',
             'ipRangeUris': [],
             'powerMode': 'RedundantPowerFeed'
             }

les = {'name': 'LE1',
       'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False

       }
Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']
port_name = ['Q5', 'Q5']

server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['name'],
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay3', 'description': 'Gen9 Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan405',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                        ]}}]

server_profiles1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['name'],
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': ENC1 + '_Bay3', 'description': 'Gen9 Win', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan402',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan405',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                         ]}}]

server_profiles2 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['name'],
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': ENC1 + '_Bay3', 'description': 'Gen9 Win', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                          'requestedMbps': '2500', 'networkUri': 'NS:Netset1',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                          'requestedMbps': '2500', 'networkUri': 'NS:Netset1',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan405',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                         ]}}]

server_profiles3 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['name'],
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': ENC1 + '_Bay1', 'description': 'Gen9 Win', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                          'requestedMbps': '2500', 'networkUri': 'NS:Netset1',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                          'requestedMbps': '2500', 'networkUri': 'NS:Netset2',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan405',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                         ]}}]

server_profiles4 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + enc_group['name'],
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': ENC1 + '_Bay1', 'description': 'Gen9 Win', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings': {
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan401',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                          'requestedMbps': '2500', 'networkUri': 'NS:Netset1',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:Net-Vlan405',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                         ]}}]

ilo_details_enc1_bay6 = {'ilo_ip': '15.245.132.5', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc2_bay1 = {'ilo_ip': '15.245.132.194', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc2_bay2 = {'ilo_ip': '15.245.132.204', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc1_bay4 = {'ilo_ip': '15.245.132.17', 'username': 'Administrator', 'password': 'hpvse123'}
server_credentials_old = {'userName': 'Administrator', 'password': '-hpvse123.'}
server_credentials = {'userName': 'Administrator', 'password': '-hpvse123.'}
server_credentials1 = {'userName': 'Administrator', 'password': 'Hpvse@1'}
ping_cmd_enc1_bay4 = ['ping -S 10.11.1.101 10.11.1.102>a.txt',
                      'ping -S 10.11.1.101 10.11.1.103>b.txt',
                      'ping -S 10.11.1.101 10.11.1.104>c.txt',
                      'ping -S 10.11.1.102 10.11.1.101>d.txt',
                      'ping -S 10.11.1.102 10.11.1.103>e.txt',
                      'ping -S 10.11.1.102 10.11.1.104>f.txt',
                      'ping -S 10.11.1.103 10.11.1.101>g.txt',
                      'ping -S 10.11.1.103 10.11.1.102>h.txt',
                      'ping -S 10.11.1.103 10.11.1.104>i.txt',
                      'ping -S 10.11.1.104 10.11.1.101>j.txt',
                      'ping -S 10.11.1.104 10.11.1.102>k.txt',
                      'ping -S 10.11.1.104 10.11.1.103>l.txt']
ping_cmd_enc2_bay4 = ['ping -S 10.11.1.105 10.12.1.103>1.txt',
                      'ping -S 10.12.1.103 10.11.1.105>2.txt'
                      ]
ping_cmd_enc1_bay6_1 = ['ping -S 10.11.1.201 10.11.1.202>z.txt',
                        'ping -S 10.11.1.202 10.11.1.201>x.txt'
                        ]
ping_cmd_enc1_bay6_2 = ['ping -S 10.11.1.201 10.11.1.202>ab.txt',
                        'ping -S 10.11.1.202 10.11.1.201>cd.txt']
ping_cmd_enc1_bay6_3 = ['ping -S 10.11.1.201 10.12.1.201>ef.txt',
                        'ping -S 10.11.1.202 10.12.1.201>gh.txt'
                        ]
ping_cmd_enc1_bay6_4 = ['ping -S 10.12.1.201 10.12.1.202>ij.txt',
                        'ping -S 10.12.1.202 10.12.1.201>kl.txt'
                        ]
ping_cmd_enc1_bay6_5 = ['ping -S 10.11.1.201 10.11.1.203>mn.txt',
                        'ping -S 10.11.1.203 10.11.1.201>op.txt']
pingfile = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt', 'g.txt', 'h.txt', 'i.txt', 'j.txt', 'k.txt', 'l.txt']
pingfile1 = ['1.txt', '2.txt']
pingfile2 = ['z.txt', 'x.txt']
pingfile3 = ['ab.txt', 'cd.txt']
pingfile4 = ['ef.txt', 'gh.txt']
pingfile5 = ['ij.txt', 'kl.txt']
pingfile6 = ['mn.txt', 'op.txt']
Ping_Lost = 'Lost'
dw_ports_3 = ['d1']
alertstate_ICM = 'Active'
alertstate_profiles = 'Locked'
alertType_ICM = 'crm.connectionStateChange'
interconnect_alert = 'Connection on downlink port'
alertType_profiles = 'profilemgr.Connections.CONNECTION_SCMB_ERROR'
profile_alert = 'An error has occurred on connection'
content1 = 'General failure'
content2 = 'Destination host unreachable'
content3 = 'TTL'
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]
IC_stacking_domain_role = ['Subordinate', 'Master']
ENCs = [ENC1, ENC2]
bay_numbers = ['3', '6']
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac_list = ["New-netlbfoteam -name 'Team1' -TeamMembers 'pppp' -TeamingMode 'SwitchIndependent'", "New-netlbfoteam -name 'Team2' -TeamMembers 'pppp' -TeamingMode 'SwitchIndependent'"]
Powershell_get_mac_list1 = ["Add-NetLbfoteamNIC -Team 'Team1' -VlanID 401", "Add-NetLbfoteamNIC -Team 'Team2' -VlanID 401"]
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp' -TeamingMode 'SwitchIndependent'"
Powershell_get_mac3 = "New-netlbfoteam -name 'Team2' -TeamMembers 'pppp' -TeamingMode 'SwitchIndependent'"
Powershell_get_mac2 = "Add-NetLbfoteamNIC -Team 'Team1' -VlanID 401"
Powershell_get_mac4 = "Add-NetLbfoteamNIC -Team 'Team2' -VlanID 401"
Powershell_get_mac5 = "Add-NetLbfoteamNIC -Team 'Team2' -VlanID 402"
Powershell_get_mac6 = "Add-NetLbfoteamNIC -Team 'Team1' -VlanID 402"
powershell_set_static_ip_list = ["netsh interface ip set address \"Team1 - VLAN 401\" static 10.11.1.201 255.255.255.0 10.11.0.1", "netsh interface ip set address \"Team2 - VLAN 401\" static 10.11.1.202 255.255.255.0 10.11.0.1"]
Powershell_set_static_ip = "netsh interface ip set address \"Team1 - VLAN 401\" static 10.11.1.201 255.255.255.0 10.11.0.1"
Powershell_set_static_ip1 = "netsh interface ip set address \"Team2 - VLAN 401\" static 10.11.1.202 255.255.255.0 10.11.0.1"
Powershell_set_static_ip2 = "netsh interface ip set address \"Team2 - VLAN 402\" static 10.12.1.201 255.255.255.0 10.11.0.1"
Powershell_set_static_ip3 = "netsh interface ip set address \"Team1 - VLAN 402\" static 10.12.1.202 255.255.255.0 10.11.0.1"
Powershell_set_static_ip4 = "netsh interface ip set address \"xxxx\" static 10.11.1.203 255.255.255.0 10.11.0.1"
Powershell_set_static = ["netsh interface ip set address \"xxxx\" static 10.11.1.101 255.255.255.0 10.11.0.1", "netsh interface ip set address \"xxxx\" static 10.11.1.102 255.255.255.0 10.11.0.1", "netsh interface ip set address \"xxxx\" static 10.11.1.103 255.255.255.0 10.11.0.1", "netsh interface ip set address \"xxxx\" static 10.11.1.104 255.255.255.0 10.11.0.1"]
Powershell_set_static1 = ["netsh interface ip set address \"xxxx\" static 10.11.1.105 255.255.255.0 10.11.0.1", "netsh interface ip set address \"xxxx\" static 10.12.1.103 255.255.255.0 10.11.0.1"]
delete_team_cmd0 = "Remove-NetLbfoTeam 'Team1'"
delete_team_cmd1 = "Remove-NetLbfoTeam 'Team2'"
delete_static_ip = "netsh interface ipv4 delete address \"yyyy\" addr=10.11.1.203 gateway=10.11.0.1"
delete_static_ip1_diff_networks = ["netsh interface ipv4 delete address \"yyyy\" addr=10.11.1.105 gateway=10.11.0.1", "netsh interface ipv4 delete address \"yyyy\" addr=10.12.1.103 gateway=10.11.0.1"]
delete_static_ip1_same_networks = ["netsh interface ipv4 delete address \"yyyy\" addr=10.11.1.101 gateway=10.11.0.1", "netsh interface ipv4 delete address \"yyyy\" addr=10.11.1.102 gateway=10.11.0.1", "netsh interface ipv4 delete address \"yyyy\" addr=10.11.1.103 gateway=10.11.0.1", "netsh interface ipv4 delete address \"yyyy\" addr=10.11.1.104 gateway=10.11.0.1"]

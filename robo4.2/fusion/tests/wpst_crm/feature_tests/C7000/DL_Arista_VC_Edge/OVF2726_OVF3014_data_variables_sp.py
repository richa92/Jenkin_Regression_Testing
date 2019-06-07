
import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


def get_matching_lines_with_number(string, pattern, case_insensitive=False):
    if case_insensitive:
        pattern = pattern.lower()
        contains = lambda line: pattern in line.lower()
    else:
        contains = lambda line: pattern in line
    print '*INFO* %s' % (string)
    print '*INFO* %s' % (pattern)
    print '*INFO* %s' % (contains)
    lines = string.splitlines()
    matching = [line for line in lines if contains(line)]
    print '*INFO* %d out of %d lines matched' % (len(matching), len(lines))
    return '\n'.join(matching), len(matching)

SSH_PASS = 'hpvse1'

APPLIANCE_IP_4_10 = '15.186.16.43'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

'''
OVF2726 & OVF3014
'''
Network_body = {'connectionTemplateUri': None,
                'ethernetNetworkType': 'Tagged',
                'name': 'Net_Vlan_30',
                'privateNetwork': False,
                'purpose': 'General',
                'smartLink': True,
                'type': 'ethernet-networkV4',
                'vlanId': 30
                }

Vlans = [10, 20, 30, 40, 50, 60, 70, 80]

reboot = 'REBOOT'

'''
# #used in ovf2724 data variables
DL_SH_IP = ['15.186.17.202','15.186.15.75','15.186.15.14','15.186.15.49']
mphosts_addresses = {'DHCP':'','LinkLocal':'','Lookup':''}
server_models = ['ProLiant DL380 Gen10','ProLiant DL360 Gen10']
#380 360 HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr
#adapter_models = ['HPE FlxFbr 10/25Gb 2p 622FLR-SFP28 Adptr', 'HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr']
adapter_models = ['HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr', 'HPE Eth 10/25Gb 2p 631FLR-SFP28 Adptr']
valDict = {'taskState':'Completed'}

sw_type = 'Ethernet'
slotNumber = '1'
serverState = 'OK'
switches_IP = ['15.186.17.219','15.186.17.208']

DL_SH_body = { "hostname" : "enc-ilo.corp.com",
               "username" : "Administrator",
               "password" : "hpvse123",
               "force" : True,
               "licensingIntent":"OneView",
               #"licensingIntent":"OneViewNoiLO",
               "configurationState":"Managed",
               }

##used in ovf2724 data variables
'''

Network_set_body = {'connectionTemplateUri': None,
                    'name': 'NS1',
                    'nativeNetworkUri': None,
                    'networkUris': [],
                    'type': 'network-setV4'
                    }


NS_nw_names = [['Net_Vlan50', 'Net_Vlan60'], ['Net_Vlan30', 'Net_Vlan40'], ['Net_Vlan50', 'Net_Vlan60'], ['Net_Vlan30', 'Net_Vlan40']]

Network_sets = [['Net_Vlan70', 'Net_Vlan20', 'Net_Vlan30'], ['Net_Vlan40', 'Net_Vlan50', 'Net_Vlan60']]

nw_set_names = ['Net_Set1', 'Net_Set2']
nw_names = ['Net_Vlan10', 'Net_Vlan20', 'Net_Vlan30']
# 2 DL 360 , 2 DL 380
DL_server_names = ['ILOMXQ7340093', 'ILOMXQ733085B', 'ILO2M2733056Q', 'ILO2M2733056R']
# 1 DL360,1 DL380
DL_server_names1 = ['ILOMXQ7340093', 'ILO2M2733056Q']

Interfaces_number = [4, 6, 1, 2]

sp_names = ['Profile1DL360', 'Profile2DL360', 'Profile1DL380', 'Profile2DL380']


server_profiles = [[{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                     'serverHardwareTypeUri': '',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Profile1DL360', 'description': '', 'affinity': None,
                     'boot': {'manageBoot': False},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                     'connectionSettings': {'connections': [
                         {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                          'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                          'wwnn': None},
                         {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                          'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                          'wwnn': None}
                     ]}}],

                   [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[1],
                     'serverHardwareTypeUri': '',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Profile2DL360', 'description': '', 'affinity': None,
                     'boot': {'manageBoot': False},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                     'connectionSettings': {'connections': [
                         {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                           'networkUri': 'ETH:Net_Vlan50', 'mac': None, 'wwpn': None,
                                           'wwnn': None},
                         {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                           'networkUri': 'ETH:Net_Vlan60', 'mac': None, 'wwpn': None,
                                           'wwnn': None}
                     ]}}],
                   [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[2],
                     'serverHardwareTypeUri': '',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Profile1DL380', 'description': '', 'affinity': None,
                     'boot': {'manageBoot': False},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                  "secureBoot": "Disabled"},
                     'connectionSettings': {'connections': [
                         {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                           'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                           'wwnn': None},
                         {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                           'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                           'wwnn': None}]}}],
                   [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[3],
                     'serverHardwareTypeUri': '',
                     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Profile2DL380', 'description': '', 'affinity': None,
                     'boot': {'manageBoot': False},
                     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                  "secureBoot": "Disabled"},
                     'connectionSettings': {'connections': [
                         {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                           'networkUri': 'ETH:Net_Vlan50', 'mac': None, 'wwpn': None,
                                           'wwnn': None},
                         {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                           'networkUri': 'ETH:Net_Vlan60', 'mac': None, 'wwpn': None,
                                           'wwnn': None}
                     ]}}]]

server_profiles_3 = [[{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                       'serverHardwareTypeUri': '',
                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                       'name': 'Profile1DL360', 'description': '', 'affinity': None,
                       'boot': {'manageBoot': False},
                       "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                       'connectionSettings': {'connections': [
                           {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                            'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                            'wwnn': None},
                           {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                            'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                            'wwnn': None}
                       ]}}],

                     [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[1],
                       'serverHardwareTypeUri': '',
                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                       'name': 'Profile1DL380', 'description': '', 'affinity': None,
                       'boot': {'manageBoot': False},
                       "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                    "secureBoot": "Disabled"},
                       'connectionSettings': {'connections': [
                           {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                            'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                            'wwnn': None},
                           {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                            'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                            'wwnn': None}]}}],
                     [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[2],
                       'serverHardwareTypeUri': '',
                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                       'name': 'Profile2DL380', 'description': '', 'affinity': None,
                       'boot': {'manageBoot': False},
                       "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                    "secureBoot": "Disabled"},
                       'connectionSettings': {'connections': [
                           {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                            'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                            'wwnn': None},
                           {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                            'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                            'wwnn': None}
                       ]}}]]


server_profiles_nw_set = [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': 'Profile1DL360', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections':
                                                  [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                             'portId': 'Flr 1:1',
                                                             'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                             'wwnn': None},
                                                   {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                             'portId': 'Flr 1:2',
                                                             'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                             'wwnn': None}
                                                   ]}},

                          {'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[1],
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': 'Profile2DL360', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections':
                                                  [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                    'portId': 'Flr 1:1',
                                                    'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                    'wwnn': None},
                                                   {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                    'portId': 'Flr 1:2',
                                                    'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                    'wwnn': None}
                                                   ]}},
                          {'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[2],
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': 'Profile1DL380', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                        "secureBoot": "Disabled"},
                           'connectionSettings': {'connections':
                                                  [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                    'portId': 'Flr 1:1',
                                                    'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                    'wwnn': None},
                                                   {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                    'portId': 'Flr 1:2',
                                                    'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                    'wwnn': None}
                                                   ]}},
                          {'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[3],
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': 'Profile2DL380', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                        "secureBoot": "Disabled"},
                           'connectionSettings': {'connections':
                                                  [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                    'portId': 'Flr 1:1',
                                                    'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                    'wwnn': None},
                                                   {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                    'portId': 'Flr 1:2',
                                                    'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                    'wwnn': None}
                                                   ]}}]

server_profiles_nw_set_3 = [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                             'serverHardwareTypeUri': '',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile1DL360', 'description': '', 'affinity': None,
                             'boot': {'manageBoot': False},
                             "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                             'connectionSettings': {'connections':
                                                    [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                               'portId': 'Flr 1:1',
                                                               'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                               'wwnn': None},
                                                     {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                               'portId': 'Flr 1:2',
                                                      'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                      'wwnn': None}
                                                     ]}},

                            {'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[1],
                             'serverHardwareTypeUri': '',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile1DL380', 'description': '', 'affinity': None,
                             'boot': {'manageBoot': False},
                             "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                          "secureBoot": "Disabled"},
                             'connectionSettings': {'connections':
                                                    [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                               'portId': 'Flr 1:1',
                                                               'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                               'wwnn': None},
                                                     {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                               'portId': 'Flr 1:2',
                                                      'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                      'wwnn': None}
                                                     ]}},
                            {'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[2],
                             'serverHardwareTypeUri': '',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile2DL380', 'description': '', 'affinity': None,
                             'boot': {'manageBoot': False},
                             "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                          "secureBoot": "Disabled"},
                             'connectionSettings': {'connections':
                                                    [{'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet',
                                                               'portId': 'Flr 1:1',
                                                               'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                                               'wwnn': None},
                                                     {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet',
                                                               'portId': 'Flr 1:2',
                                                      'networkUri': 'ETH:Net_Vlan40', 'mac': None, 'wwpn': None,
                                                      'wwnn': None}
                                                     ]}}]


server_profiles_body_edit = {'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                             'serverHardwareTypeUri': '',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile2DL360', 'description': '', 'affinity': None,
                             'boot': {'manageBoot': False},
                             "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                             'connectionSettings': {'connections': [
                                 {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                  'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                  'wwnn': None},
                                 {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                  'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                  'wwnn': None}
                             ]}}

switch_ip = ['15.186.17.208', '15.186.17.219']
interface = 4
switch_details = {'userName': 'admin', 'password': 'password'}
Commands = ['enable', 'config', 'interface ethernet', 'no shutdown', 'shutdown', 'vlan', 'switchport mode access', 'switchport access vlan', 'no vlan', 'show vlan', 'show active', 'switchport trunk allowed vlan', 'switchport trunk native vlan', 'write']
pattern = 'allowed vlan'
enable = ['False', 'True']
sample = ['10', '10']
sw_linked_downlink_ports = [1, 2, 4, 6]
port_details = [{'type': 'port', 'portType': 'Downlink', 'portId': '31bfa40e-eb07-4fe2-bb2d-15226663466a:4', 'portHealthStatus': 'Normal', 'enabled': '', 'portName': '4', 'portStatus': 'Linked'}]
disable_vlan = ['no switchport trunk native vlan none', 'switchport trunk allowed vlan none']
redhat_ip = '15.186.12.45'
redhat_pattern = '<BROADCAST,MULTICAST,UP,LOWER_UP>'
server_Auth_details = [{"username": "Administrator", "password": "hpvse@123"}, {"username": "root", "password": "hpvse123"}]


'''
shyamala's variables
'''
invalid_networks = [{'name': 'net_101', 'type': 'ethernet-networkV4', 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Untagged'},
                    {'name': 'net_102', 'type': 'ethernet-networkV4', 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tunnel'}]
server_profile_dl = {'type': 'ServerProfileV9', 'serverHardwareUri': '', 'serverHardwareTypeUri': '', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'name': '', 'description': '', 'affinity': None, 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': '0', 'networkUri': '', 'mac': None, 'wwpn': '', 'wwnn': ''}]}}
Network_1 = {'connectionTemplateUri': None,
             'ethernetNetworkType': 'Tagged',
             'name': 'Net_Vlan10',
             'privateNetwork': False,
             'purpose': 'General',
             'smartLink': True,
             'type': 'ethernet-networkV4',
             'vlanId': 10
             }
Network_2 = {'connectionTemplateUri': None,
             'ethernetNetworkType': 'Tagged',
             'name': 'Net_Vlan20',
             'privateNetwork': False,
             'purpose': 'General',
             'smartLink': True,
             'type': 'ethernet-networkV4',
             'vlanId': 20
             }
# First hardware type should be windows server
Hardware_Type = ['DL360 Gen10 1', 'DL380 Gen10 1']
profile_template = {'type': 'ServerProfileTemplateV5', 'serverProfileDescription': '', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical', 'name': '', 'description': '', 'affinity': None, 'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan70', 'ipv4': {}}], 'manageConnections': True}, 'boot': None, 'bootMode': {'manageMode': False}, 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareActivationType': 'Immediate'}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated', 'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None, 'osDeploymentSettings': None, 'initialScopeUris': []}

profile_from_temp = {'type': 'ServerProfileV9', 'serverHardwareUri': '', 'serverHardwareTypeUri': '', 'enclosureGroupUri': '', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': 'AutoGenerated', 'macType': 'Physical', 'wwnType': 'Physical', 'name': '', 'description': '', 'affinity': None, 'connectionSettings': {'connections': [{'id': 1, 'name': 'c1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1', 'requestedMbps': 0, 'networkUri': 'ETH:Net_Vlan70', 'requestedVFs': 'Auto', 'ipv4': {}}]}, 'boot': None, 'bootMode': {'manageMode': False}, 'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics': True, 'iscsiInitiatorName': '', 'serverProfileTemplateUri': '', 'osDeploymentSettings': None, 'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': None, 'initialScopeUris': []}
Alert_switchports = ['The overall status of the system network is critical.', 'Connection deployed on downlink port 6.', 'An error has occurred on connection 1.']
status_code = '200'
Err_Msg = 'CRM_INVALID_SWITCH_CREDENTIALS'

Alert_Nset_changeconfig = ['Connectivity lost for adapter in slot 0, port 1.']
Alert_Nset_delete = ['Connection on downlink port']
Nativenetwork = ['Net_Vlan70', 'Net_Vlan40']
server_profile_nwset = [{'type': 'ServerProfileV9', 'serverHardwareUri': '',
                         'serverHardwareTypeUri': '',
                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                         'name': '', 'description': '', 'affinity': None,
                         'boot': {'manageBoot': False},
                         "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                         'connectionSettings': {'connections': [
                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                       'networkUri': 'NS:Net_Set1', 'mac': None, 'wwpn': None,
                                       'wwnn': None},
                         ]}}]
server_profile_samevlan = [{'type': 'ServerProfileV9', 'serverHardwareUri': '',
                            'serverHardwareTypeUri': '',
                            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': '', 'description': '', 'affinity': None,
                            'boot': {'manageBoot': False},
                            "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                            'connectionSettings': {'connections': [
                                {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                 'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                 'wwnn': None},
                                {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                 'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                 'wwnn': None}
                            ]}}]
server_profile_maxvlan = [{'type': 'ServerProfileV9', 'serverHardwareUri': '',
                           'serverHardwareTypeUri': '',
                           'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                           'name': '', 'description': '', 'affinity': None,
                           'boot': {'manageBoot': False},
                           "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                           'connectionSettings': {'connections': [
                               {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                'networkUri': 'NS:Net_Set1', 'mac': None, 'wwpn': None,
                                'wwnn': None},
                               {'id': 2, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                'networkUri': 'NS:Net_Set1', 'mac': None, 'wwpn': None,
                                'wwnn': None}
                           ]}}]
server_profile_1 = {'type': 'ServerProfileV9', 'serverHardwareUri': '',
                    'serverHardwareTypeUri': '',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Profile1', 'description': '', 'affinity': None,
                    'boot': {'manageBoot': False},
                    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                    'connectionSettings': {'connections': [
                        {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                         'networkUri': 'ETH:Net_10', 'mac': None, 'wwpn': None,
                                       'wwnn': None},
                    ]}}
Vlan_range = '2-165'
set_vlan = ['10,20,30,40,50,60,70,80']
switch_vlan = '10,20,30,40,50,60,70,80'
Nset_Max_Error_Message = 'CRM_DOMAIN_NETWORK_SET_LIMIT_EXCEEDED'
server_hardware = ['ILOMXQ7340093', 'ILO2M2733056Q']
linux_server_cred = {'username': 'root', 'password': 'hpvse123'}
ps_cmd_native = "Powershell.exe -File C:\\Users\\Administrator\\Desktop\\nativeteam.ps1"
ps_cmd_native_edit = "Powershell.exe -File C:\\Users\\Administrator\\Desktop\\nativeteamedit.ps1"
Edit_nset = 'Net_Set2'
Timout_for_server = '300s'


server_profiles_fcoe_connection = [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                                    'serverHardwareTypeUri': '',
                                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                    'name': 'Profile1', 'description': '', 'affinity': None,
                                    'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flr 1:2',
                                                                            'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                           ]}}]
server_profiles_fc_connection = [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                                  'serverHardwareTypeUri': '',
                                  'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                  'name': 'Profile1', 'description': '', 'affinity': None,
                                  'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                  'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flr 1:2',
                                                                          'requestedMbps': '2500', 'networkUri': 'FC:fc1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                         ]}}]

server_profiles_multiple_connection = [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                                        'serverHardwareTypeUri': '',
                                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                        'name': 'Profile1', 'description': '', 'affinity': None,
                                        'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                                                                'requestedMbps': '2500', 'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                               {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                                                                'requestedMbps': '2500', 'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                               {'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flr 1:3',
                                                                                'requestedMbps': '2500', 'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                               ]}}]

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

switch1_port = ['1', '1']
switch2_port = ['2', '2']
ARISTA_IPS_1 = ['15.186.17.219']
LS1 = 'LS_ARISTA'
server_profiles_edit_body = {'type': 'ServerProfileV9', 'serverHardwareUri': '',
                             'serverHardwareTypeUri': '',
                             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                             'name': 'Profile1DL360', 'description': '', 'affinity': None, 'eTag': '',
                             'boot': {'manageBoot': False},
                             "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                             'connectionSettings': {'connections': [
                                 {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                  'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                  'wwnn': None},
                                 {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                  'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                  'wwnn': None}]}}


Network_delete_message_in_sp = "An error has occurred on connection "
Network_delete_message_in_switch = "Connection on downlink port"
enable_vlan_message_in_switch = "configuration is not consistent with the default OneView configuration."
varTrue = True
varFalse = False
Alert = ['Active', 'Locked', 'Cleared']
reboot_command = 'reload'

server_profiles_network_delete_tc_4 = [[{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                                         'serverHardwareTypeUri': '',
                                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Profile1DL360', 'description': '', 'affinity': None,
                                         'boot': {'manageBoot': False},
                                         "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                                         'connectionSettings': {'connections': [
                                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                              'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                              'wwnn': None},
                                             {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                              'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                              'wwnn': None}
                                         ]}}],

                                       [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[1],
                                         'serverHardwareTypeUri': '',
                                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Profile2DL360', 'description': '', 'affinity': None,
                                         'boot': {'manageBoot': False},
                                         "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                                         'connectionSettings': {'connections': [
                                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                              'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                              'wwnn': None},
                                             {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                                 'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                                 'wwnn': None}
                                         ]}}],
                                       [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[2],
                                         'serverHardwareTypeUri': '',
                                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Profile1DL380', 'description': '', 'affinity': None,
                                         'boot': {'manageBoot': False},
                                         "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                                      "secureBoot": "Disabled"},
                                         'connectionSettings': {'connections': [
                                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                              'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                              'wwnn': None},
                                             {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                                 'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                                 'wwnn': None}]}}],
                                       [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[3],
                                         'serverHardwareTypeUri': '',
                                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                         'name': 'Profile2DL380', 'description': '', 'affinity': None,
                                         'boot': {'manageBoot': False},
                                         "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                                      "secureBoot": "Disabled"},
                                         'connectionSettings': {'connections': [
                                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                              'networkUri': 'ETH:Net_Vlan10', 'mac': None, 'wwpn': None,
                                              'wwnn': None},
                                             {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                                 'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                                 'wwnn': None}
                                         ]}}]]
server_profiles_network_delete_tc = [[{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[0],
                                       'serverHardwareTypeUri': '',
                                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                       'name': 'Profile1DL360', 'description': '', 'affinity': None,
                                       'boot': {'manageBoot': False},
                                       "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                                       'connectionSettings': {'connections': [
                                           {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                            'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                            'wwnn': None},
                                           {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                            'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                            'wwnn': None}
                                       ]}}],

                                     [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[1],
                                       'serverHardwareTypeUri': '',
                                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                       'name': 'Profile2DL360', 'description': '', 'affinity': None,
                                       'boot': {'manageBoot': False},
                                       "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                                    "secureBoot": "Disabled"},
                                       'connectionSettings': {'connections': [
                                           {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                            'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                            'wwnn': None},
                                           {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                               'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                               'wwnn': None}]}}],
                                     [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[2],
                                       'serverHardwareTypeUri': '',
                                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                       'name': 'Profile1DL380', 'description': '', 'affinity': None,
                                       'boot': {'manageBoot': False},
                                       "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                                    "secureBoot": "Disabled"},
                                       'connectionSettings': {'connections': [
                                           {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                            'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                            'wwnn': None},
                                           {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                               'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                               'wwnn': None}
                                       ]}}],
                                     [{'type': 'ServerProfileV9', 'serverHardwareUri': DL_server_names[3],
                                       'serverHardwareTypeUri': '',
                                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                       'name': 'Profile2DL380', 'description': '', 'affinity': None,
                                       'boot': {'manageBoot': False},
                                         "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto",
                                                      "secureBoot": "Disabled"},
                                         'connectionSettings': {'connections': [
                                             {'id': 1, 'name': 'Downlink_1', 'functionType': 'Ethernet', 'portId': 'Flr 1:1',
                                              'networkUri': 'ETH:Net_Vlan20', 'mac': None, 'wwpn': None,
                                              'wwnn': None},
                                             {'id': 1, 'name': 'Downlink_2', 'functionType': 'Ethernet', 'portId': 'Flr 1:2',
                                              'networkUri': 'ETH:Net_Vlan30', 'mac': None, 'wwpn': None,
                                              'wwnn': None}
                                         ]}}]

                                     ]

'''
janani
'''
Arista_login_details = [{'ip': '15.186.17.208', 'userName': 'admin', 'password': 'password'},
                        {'ip': '15.186.17.219', 'userName': 'admin', 'password': 'password'}]

Vlan_Id_switches = ['50', '60']
Original_Vlan_Id = ['30', '40']

ls_body = {}

enable_vlan = ['switchport trunk allowed vlan ']
vlan_enable = ['20', '30']

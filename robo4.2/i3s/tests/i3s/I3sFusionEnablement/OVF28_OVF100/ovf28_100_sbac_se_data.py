import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import environment_data as env

admin_credentials = {"userName": "Administrator", "password": "admin123", "authLoginDomain": "LOCAL", "loginMsgAck": None}

User1_credentials = {'userName': 'User1', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

scopes = [{"name": "Scope1_sbac", "description": "", "type": "ScopeV3", "addedResourceUris": [], "removedResourceUris": []}]

users = [{"type": "UserAndPermissions", "userName": "User1", "fullName": "",
          "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
          "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'sbac_network',
                      'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '80', 'purpose': 'General'}]

connections = [{"id": 1, "name": "Deployment Network A", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                "networkUri": 'ETH:' + env.networks['iscsi'], "mac": None, "wwpn": "", "wwnn": "", "requestedVFs": "Auto",
                "ipv4": {"ipAddressSource": None, "subnetMask": None, "gateway": None, "ipAddress": None},
                "boot": {"priority": "NotBootable", "iscsi": {}}},
               {"id": 2, "name": "Management Network A", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500",
                "networkUri": 'ETH:' + env.networks['mgmt'], "mac": None, "wwpn": "", "wwnn": "", "requestedVFs": "Auto",
                "ipv4": {"ipAddressSource": None, "subnetMask": None, "gateway": None, "ipAddress": None},
                "boot": {"priority": "NotBootable", "iscsi": {}}}]

OVF28_OVF100_TC01 = [{'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "OVF28_OVF100_TC01_Scope", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic'], "removedResourceUris": []},
                      'isNegative': False}]

OVF28_OVF100_TC02 = [{'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "OVF28_OVF100_TC02_Scope", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic'], "removedResourceUris": []},
                      'isNegative': False}]

OVF28_OVF100_TC03 = [{'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "OVF28_OVF100_TC03_Scope", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic not existing'], "removedResourceUris": []},
                      'isNegative': False}]

OVF28_OVF100_TC04 = [{'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "tc_04_MARKETING", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                                               'Osdp:dp2With1Nic_StaticAndDhcpNic'],
                                         "removedResourceUris": []},
                      'isNegative': False},
                     {'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None},
                      'scope_creation': {"name": "tc_04_FINANCE", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                                               'Osdp:dp2With1Nic_StaticAndDhcpNic'],
                                         "removedResourceUris": []},
                      'isNegative': False}]

OVF28_OVF100_TC05 = [{'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "tc_05_MARKETING", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic'], "removedResourceUris": []},
                      'isNegative': False},
                     {'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "tc_05_FINANCE", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:Deploy ESXi with management NIC'], "removedResourceUris": []},
                      'isNegative': False}]

OVF28_OVF100_TC06 = [{'user_scope_update': {'userName': 'User1', 'role': 'Scope administrator', 'scope': None,
                                            'scope_update_add': None, 'scope_update_delete': None, 'replaceRoles': True},
                      'scope_creation': {"name": "tc_06_PRODUCTION", "description": "", "type": "ScopeV3",
                                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic'], "removedResourceUris": []},
                      'isNegative': False}]

OVF28_OVF100_TC06_01 = [{"type": "UserAndPermissions", "userName": "tc_06_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": 'tc_06_PRODUCTION'}]}]

OVF28_OVF100_TC07_01 = [{"name": "tc_07_TEST", "description": "", "type": "ScopeV3",
                         "addedResourceUris": [], "removedResourceUris": []},
                        {"name": "tc_07_DEV", "description": "", "type": "ScopeV3",
                         "addedResourceUris": [], "removedResourceUris": []}]

OVF28_OVF100_TC07_02 = [{"type": "UserAndPermissions", "userName": "tc_07_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC08_01 = [{"name": "tc_08_TEST", "description": "", "type": "ScopeV3",
                         "addedResourceUris": [], "removedResourceUris": []},
                        {"name": "tc_08_DEV", "description": "", "type": "ScopeV3",
                         "addedResourceUris": [], "removedResourceUris": []}]

OVF28_OVF100_TC08_02 = [{"type": "UserAndPermissions", "userName": "tc_08_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC08_03 = [[{"userName": "tc_08_User", "permissions": [{"roleName": "Server administrator", "scopeUri": 'tc_08_TEST'}], 'replaceRoles': False}],
                        [{"userName": "tc_08_User", "permissions": [{"roleName": "Server administrator", "scopeUri": 'tc_08_DEV'}], 'replaceRoles': False}]]

OVF28_OVF100_TC09_01 = [{"name": "LINUX_tc_09", "description": "", "type": "ScopeV3",
                         "addedResourceUris": [], "removedResourceUris": []}]

OVF28_OVF100_TC09_02 = [{"type": "UserAndPermissions", "userName": "tc_09_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

OVF28_OVF100_TC09_03 = [{"userName": "tc_09_User", "permissions": [{"roleName": "Read only", "scopeUri": 'LINUX_tc_09'}], 'replaceRoles': True}]

OVF28_OVF100_TC10_01 = [{"name": "LINUX_tc_10", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic', 'ETH:' + env.networks['iscsi'],
                                               'ETH:' + env.networks['mgmt'], 'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC10_02 = [{"type": "UserAndPermissions", "userName": "tc_10_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC10_03 = [{"userName": "tc_10_User", "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_10'}], 'replaceRoles': True}]

OVF28_OVF100_TC10_04 = {'userName': 'tc_10_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC10_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_10"]}]

OVF28_OVF100_TC11_01 = [{"name": "LINUX_tc_11", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []},
                        {"name": "WINDOWS_tc_11", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC11_02 = [{"type": "UserAndPermissions", "userName": "tc_11_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC11_03 = [{"userName": "tc_11_User",
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_11'},
                                         {"roleName": "Server administrator", "scopeUri": 'WINDOWS_tc_11'}], 'replaceRoles': True}]

OVF28_OVF100_TC11_04 = {'userName': 'tc_11_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC11_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_11", "Scope:WINDOWS_tc_11"]}]

OVF28_OVF100_TC12_01 = [{"name": "LINUX_tc_12", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []},
                        {"name": "WINDOWS_tc_12", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC12_02 = [{"type": "UserAndPermissions", "userName": "tc_12_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC12_03 = [{"userName": "tc_12_User",
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_12'},
                                         {"roleName": "Server administrator", "scopeUri": 'WINDOWS_tc_12'}], 'replaceRoles': True}]

OVF28_OVF100_TC12_04 = {'userName': 'tc_12_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC12_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_12"]}]

OVF28_OVF100_TC12_06 = [[{'scope': 'LINUX_tc_12', 'scope_update_add': ['ETH:sbac_network'], 'scope_update_delete': None}]]

OVF28_OVF100_TC13_01 = [{"name": "LINUX_tc_13", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []},
                        {"name": "WINDOWS_tc_13", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC13_02 = [{"type": "UserAndPermissions", "userName": "tc_13_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC13_03 = [{"userName": "tc_13_User",
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_13'},
                                         {"roleName": "Server administrator", "scopeUri": 'WINDOWS_tc_13'}], 'replaceRoles': True}]

OVF28_OVF100_TC13_04 = {'userName': 'tc_13_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC13_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_13", "Scope:WINDOWS_tc_13"]}]

OVF28_OVF100_TC13_06 = [[{'scope': 'LINUX_tc_13', 'scope_update_add': ['ETH:sbac_network'], 'scope_update_delete': None}]]

OVF28_OVF100_TC14_01 = [{"name": "PRODUCTION_tc_14", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC14_02 = [{"type": "UserAndPermissions", "userName": "tc14_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'PRODUCTION_tc_14'}]}]

OVF28_OVF100_TC14_03 = {'userName': 'tc14_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC14_04 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:PRODUCTION_tc_14"]}]

OVF28_OVF100_TC15_01 = [{"name": "LINUX_tc_15", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC15_02 = [{"type": "UserAndPermissions", "userName": "tc15_User_1", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Read only", "scopeUri": 'LINUX_tc_15'}]},
                        {"type": "UserAndPermissions", "userName": "tc15_User_2", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_15'}]}]

OVF28_OVF100_TC15_03 = {'userName': 'tc15_User_1', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC15_05 = {'userName': 'tc15_User_2', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC15_04 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_15"]}]

OVF28_OVF100_TC16_01 = [{"name": "PRODUCTION_tc_16", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri'], 'SH:' + env.servers[1]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC16_02 = [{"type": "UserAndPermissions", "userName": "tc16_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'PRODUCTION_tc_16'}]}]

OVF28_OVF100_TC16_03 = {'userName': 'tc16_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC16_04 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:PRODUCTION_tc_16"]}]

OVF28_OVF100_TC16_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[1]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[1]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:PRODUCTION_tc_16"]}]

OVF28_OVF100_TC16_06 = [{"name": "PRODUCTION_tc_16", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['SH:' + env.servers[0]['serverHardwareUri'], 'SH:' + env.servers[1]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC17_01 = [{"name": "LINUX_tc_17", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic', 'Osdp:dp2With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []},
                        {"name": "WINDOWS_tc_17", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic', 'Osdp:dp2With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC17_02 = [{"type": "UserAndPermissions", "userName": "tc_17_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": None}]}]

OVF28_OVF100_TC17_03 = [{"userName": "tc_17_User",
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_17'},
                                         {"roleName": "Server administrator", "scopeUri": 'WINDOWS_tc_17'}], 'replaceRoles': True}]

OVF28_OVF100_TC17_04 = {'userName': 'tc_17_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC17_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_17", "Scope:WINDOWS_tc_17"]}]

OVF28_OVF100_TC17_06 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp2With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_17", "Scope:WINDOWS_tc_17"]}]

OVF28_OVF100_TC18_01 = [{"name": "LINUX_tc_18", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []},
                        {"name": "WINDOWS_tc_18", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC18_02 = [{"type": "UserAndPermissions", "userName": "tc18_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX_tc_18'},
                                         {"roleName": "Server administrator", "scopeUri": 'WINDOWS_tc_18'}]}]

OVF28_OVF100_TC18_03 = {'userName': 'tc18_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC18_04 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX_tc_18", "Scope:WINDOWS_tc_18"]}]

OVF28_OVF100_TC18_05 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:WINDOWS_tc_18"]}]

OVF28_OVF100_TC18_06 = {'userName': 'tc18_User', 'role': 'Scope administrator', 'scope': 'WINDOWS_tc_18',
                        'scope_update_add': None, 'scope_update_delete': None, 'replaceRole': False}

OVF28_OVF100_TC19_01 = [{"name": "WINDOWS_tc_19", "description": "", "type": "ScopeV3",
                         "addedResourceUris": [], "removedResourceUris": []}]

OVF28_OVF100_TC19_02 = [{"type": "UserAndPermissions", "userName": "tc19_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Read only", "scopeUri": 'WINDOWS_tc_19'}]}]

OVF28_OVF100_TC20_01 = [{"name": "TEST_tc_20", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []},
                        {"name": "PROD_tc_20", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic', 
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC20_02 = [{"type": "UserAndPermissions", "userName": "tc_20_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'TEST_tc_20'},
                                         {"roleName": "Server administrator", "scopeUri": 'PROD_tc_20'}]}]

OVF28_OVF100_TC20_05 = {'userName': 'tc_20_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC20_03 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:TEST_tc_20", "Scope:PROD_tc_20"]}]

OVF28_OVF100_TC20_04 = [[{"userName": "tc_20_User", "permissions": [{"roleName": "Server administrator", "scopeUri": 'PROD_tc_20'}], 'replaceRoles': True}]]

OVF28_OVF100_TC21_01 = [{"name": "LINUX1_tc_21", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC21_02 = [{"type": "UserAndPermissions", "userName": "tc_21_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": 'LINUX1_tc_21'}]}]

OVF28_OVF100_TC21_04 = {'userName': 'tc_21_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC21_03 = [
    {'type': 'ServerProfileV8',
     'name': 'ovf28_100_sp',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:LINUX1_tc_21"]}]

OVF28_OVF100_TC22_01 = [{"type": "UserAndPermissions", "userName": "tc_22_User", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Scope administrator", "scopeUri": None}]}]

OVF28_OVF100_TC22_02 = {'userName': 'tc_22_User', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC22_03 = [{"name": "OVF28_OVF100_TC22", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic'],
                         "removedResourceUris": []}]

OVF28_OVF100_TC23_01 = [{"name": "TEST_tc_23", "description": "", "type": "ScopeV3",
                         "addedResourceUris": ['Osdp:dp1With1Nic_StaticAndDhcpNic',
                                               'ETH:' + env.networks['iscsi'], 'ETH:' + env.networks['mgmt'],
                                               'SH:' + env.servers[0]['serverHardwareUri']],
                         "removedResourceUris": []}]

OVF28_OVF100_TC23_02 = [{"type": "UserAndPermissions", "userName": "tc23_User_MIKE", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": "TEST_tc_23"}]},
                        {"type": "UserAndPermissions", "userName": "tc23_User_BOB", "fullName": "",
                         "password": "admin123", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True,
                         "permissions": [{"roleName": "Server administrator", "scopeUri": "TEST_tc_23"}]}]

OVF28_OVF100_TC23_03 = [{'userName': 'tc23_User_MIKE', 'role': 'Server administrator', 'scope': 'TEST_tc_23',
                         'scope_update_add': None, 'scope_update_delete': None},
                        {'userName': 'tc23_User_BOB', 'role': 'Server administrator', 'scope': 'TEST_tc_23',
                         'scope_update_add': None, 'scope_update_delete': None}]

OVF28_OVF100_TC23_04 = {'userName': 'tc23_User_MIKE', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC23_05 = {'userName': 'tc23_User_BOB', 'password': 'admin123', "authLoginDomain": "LOCAL", "loginMsgAck": None}

OVF28_OVF100_TC23_06 = [
    {'type': 'ServerProfileV8',
     'name': 'SP_tc_23_MIKE',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:TEST_tc_23"]}]

OVF28_OVF100_TC23_07 = [
    {'type': 'ServerProfileV8',
     'name': 'SP_tc_23_BOB',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:TEST_tc_23"]}]

OVF28_OVF100_TC23_08 = [
    {'type': 'ServerProfileV8',
     'name': 'SP_tc_23_MIKE',
     'iscsiInitiatorNameType': 'AutoGenerated',
     'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
     'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
     'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
     'firmware': {'firmwareInstallType': None, 'forceInstallFirmware': False, 'manageFirmware': False, 'firmwareBaselineUri': None},
     'hideUnusedFlexNics': True,
     'macType': 'Virtual', 'wwnType': 'Virtual',
     'osDeploymentSettings': {
         'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
         'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                                {'name': 'Hostname', 'value': 'esxbay1'},
                                {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                {'name': 'Password', 'value': None},
                                {'name': 'SSH', 'value': 'enabled'}],
         'osVolumeUri': None},
     'connectionSettings': env.se_connSettings,
     'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
     'boot': {'manageBoot': True, 'order': []},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'localStorage': {},
     'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False},
     "initialScopeUris": ["Scope:TEST_tc_23"]}]

# import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import environment_data as env

connSettings = {
    "reapplyState": "NotApplying",
    'connections': [{'id': 1, 'name': 'Deployment Network A',
                     'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                     'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                     'ipv4': {'ipAddressSource': 'SubnetPool'},
                     'boot': {'bootVolumeSource': 'UserDefined',
                              'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                              'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                    {'id': 2, 'name': 'Blade_boot_mgmt',
                     'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                     'portId': 'Mezz 3:1-b', 'requestedVFs': 0, 'requestedMbps': '2500',
                     'boot': {'priority': 'NotBootable', 'iscsi': {}}}]}

spt = {'type': 'ServerProfileTemplateV4', 'name': 'OVF806_SPT',
       'serverProfileDescription': 'Server Profile Template',
       'iscsiInitiatorNameType': 'AutoGenerated',
       'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
       'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
       'affinity': 'Bay', 'hideUnusedFlexNics': True,
       'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
       'macType': 'Virtual', 'wwnType': 'Virtual',
       'osDeploymentSettings': {
                  'osDeploymentPlanUri': 'dpWith1Nic_StaticNic',
                  'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com', "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                         {'name': 'Hostname', 'value': 'esxbay1', "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                         {'name': 'ManagementNIC.connectionid', 'value': '2'},
                                         {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                                         {'name': 'ManagementNIC.vlanid', 'value': '0'},
                                         {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                                         {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                                         {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                                         {'name': 'Password', 'value': None},
                                         {'name': 'SSH', 'value': 'enabled', "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
       'connectionSettings': {
           'manageConnections': True,
           'connections': [{'id': 1, 'name': 'Deployment Network A',
                            'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                            'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                            'ipv4': {'ipAddressSource': 'SubnetPool'},
                            'boot': {'bootVolumeSource': 'UserDefined',
                                     'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                     'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                           {'id': 2, 'name': 'Blade_boot_mgmt',
                            'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                            'portId': 'Mezz 3:1-b', 'requestedVFs': 0, 'requestedMbps': '2500',
                            'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
       'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
       'boot': {'manageBoot': True, 'order': []},
       'bios': {'manageBios': False, 'overriddenSettings': []},
       'localStorage': {},
       'sanStorage': None}

sp_from_spt = {'type': 'ServerProfileV8', 'name': 'OVF806_SP',
               'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
               'serverProfileTemplateUri': 'SPT:' + spt['name']}

sptWithTeamedNicDp = {
    'type': 'ServerProfileTemplateV4', 'name': 'OVF806_SPT',
    'serverProfileDescription': 'Server Profile Template',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dpWith1Nic_StaticAndDhcpNic_TeamNic',
        'osCustomAttributes': [{"name": "DomainName", "value": "hpe.com", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {"name": "Hostname", "value": "esxbay1", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {"name": "ManagementNIC.connectionid", "value": "2"},
                               {"name": "ManagementNIC.dhcp", "value": "false"},
                               {"name": "ManagementNIC.ipv4disable", "value": "false"},
                               {"name": "ManagementNIC.networkuri", "value": 'ETH:' + env.networks['mgmt']},
                               {"name": "ManagementNIC.constraint", "value": "auto"},
                               {"name": "ManagementNIC.vlanid", "value": "0"},
                               {"name": "Password", "value": None},
                               {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
    'connectionSettings': {
        'manageConnections': True,
        'connections': [{'id': 1, 'name': 'Deployment Network A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': None}

tc08_edit_spt = {
    'type': 'ServerProfileTemplateV4', 'name': 'OVF806_SPT',
    'serverProfileDescription': 'Server Profile Template',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dpWith1Nic_StaticAndDhcpNic_noPswd',
        'osCustomAttributes': [{"name": "DomainName", "value": "oneview.com", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {"name": "Hostname", "value": "hyperv1", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {"name": "ManagementNIC.connectionid", "value": "2"},
                               {"name": "ManagementNIC.dhcp", "value": "false"},
                               {"name": "ManagementNIC.ipv4disable", "value": "false"},
                               {"name": "ManagementNIC.networkuri", "value": 'ETH:' + env.networks['mgmt']},
                               {"name": "ManagementNIC.constraint", "value": "auto"},
                               {"name": "ManagementNIC.vlanid", "value": "0"},
                               {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
    'connectionSettings': {
        'manageConnections': True,
        'connections': [{'id': 1, 'name': 'Deployment Network A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': None}

tc11_editSpt = {
    'type': 'ServerProfileTemplateV4', 'name': 'OVF806_SPT',
    'serverProfileDescription': 'Server Profile Template',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dp1With1Nic_StaticAndDhcpNic',
        'osCustomAttributes': [{'name': 'DomainName', 'value': 'oneview.com', "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {'name': 'Hostname', 'value': 'hyperv1', "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {'name': 'ManagementNIC.connectionid', 'value': '2'},
                               {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                               {'name': 'ManagementNIC.vlanid', 'value': '0'},
                               {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                               {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                               {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                               {'name': 'Password', 'value': None},
                               {'name': 'SSH', 'value': 'enabled', "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
    'connectionSettings': {
        'manageConnections': True,
        'connections': [{'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
                'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
                'boot': {'manageBoot': True, 'order': []},
                'bios': {'manageBios': False, 'overriddenSettings': []},
                'localStorage': {},
                'sanStorage': None}

tc14_editSp = {
    'type': 'ServerProfileV8', 'name': 'OVF806_SP',
    'serverProfileTemplateUri': 'SPT:' + spt['name'],
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dpWith1Nic_StaticAndDhcpNic_noPswd',
        'osCustomAttributes': [{"name": "DomainName", "value": "oneview.com", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {"name": "Hostname", "value": "hyperv1", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {"name": "ManagementNIC.connectionid", "value": "2"},
                               {"name": "ManagementNIC.dhcp", "value": "false"},
                               {"name": "ManagementNIC.ipv4disable", "value": "false"},
                               {"name": "ManagementNIC.networkuri", "value": 'ETH:' + env.networks['mgmt']},
                               {"name": "ManagementNIC.constraint", "value": "auto"},
                               {"name": "ManagementNIC.vlanid", "value": "0"},
                               {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
    'connectionSettings': {
        "reapplyState": "NotApplying",
        'connections': [{'id': 1, 'name': 'Deployment Network A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
               'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
               'boot': {'manageBoot': True, 'order': []},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'localStorage': {},
               'sanStorage': None}

tc15_editSp = {
    'type': 'ServerProfileV8', 'name': 'OVF806_SP',
    'serverProfileTemplateUri': 'SPT:' + spt['name'],
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dp2With1Nic_StaticAndDhcpNic',
        'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com', "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {'name': 'Hostname', 'value': 'esxbay1', "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {'name': 'ManagementNIC.connectionid', 'value': '2'},
                               {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                               {'name': 'ManagementNIC.vlanid', 'value': '0'},
                               {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                               {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                               {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                               {'name': 'Password', 'value': None},
                               {'name': 'SSH', 'value': 'enabled', "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]},
    'connectionSettings': {
        "reapplyState": "NotApplying",
        'connections': [{'id': 1, 'name': 'Deployment Network A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
               'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
               'boot': {'manageBoot': True, 'order': []},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'localStorage': {},
               'sanStorage': None}

tc17_editSp = {
    'type': 'ServerProfileV8', 'name': 'OVF806_SP',
    'serverProfileTemplateUri': 'SPT:' + spt['name'],
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dpWith1Nic_StaticAndDhcpNic_TeamNic',
        "osCustomAttributes": [{"name": "DomainName", "value": "hpe.com", "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                               {"name": "Hostname", "value": "esxbay1", "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                               {"name": "ManagementNIC.connectionid", "value": "2"},
                               {"name": "ManagementNIC.dhcp", "value": "false"},
                               {"name": "ManagementNIC.ipv4disable", "value": "false"},
                               {"name": "ManagementNIC.networkuri", "value": 'ETH:' + env.networks['mgmt']},
                               {"name": "ManagementNIC.constraint", "value": "auto"},
                               {"name": "ManagementNIC.vlanid", "value": "0"},
                               {"name": "Password", "value": None},
                               {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}],
        "osVolumeUri": None,
        "forceOsDeployment": False},
    'connectionSettings': {
        "reapplyState": "NotApplying",
        'connections': [{'id': 1, 'name': 'Deployment Network A', 'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt A', 'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-c', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': None}

cas_dpWithUserName = {
    'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com', "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                           {'name': 'Hostname', 'value': 'esxbay1', "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                           {"name": "UserName", "value": "admin", "constraints": "{\"regex\":\"\",\"helpText\":\"\"}", "type": "string"},
                           {'name': 'ManagementNIC.connectionid', 'value': '2'},
                           {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                           {'name': 'ManagementNIC.vlanid', 'value': '0'},
                           {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                           {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                           {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                           {'name': 'Password', 'value': None},
                           {'name': 'SSH', 'value': 'enabled', "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]}

cas_dpWith1Nic_StaticNic = {
    'osCustomAttributes': [{'name': 'DomainName', 'value': 'hpe.com'},
                           {'name': 'Hostname', 'value': 'esxbay1'},
                           {'name': 'ManagementNIC.connectionid', 'value': '2'},
                           {'name': 'ManagementNIC.dhcp', 'value': 'false'},
                           {'name': 'ManagementNIC.vlanid', 'value': '0'},
                           {'name': 'ManagementNIC.ipv4disable', 'value': 'false'},
                           {'name': 'ManagementNIC.networkuri', 'value': 'ETH:' + env.networks['mgmt']},
                           {'name': 'ManagementNIC.constraint', 'value': 'auto'},
                           {'name': 'Password', 'value': None},
                           {'name': 'SSH', 'value': 'enabled'}]}

tc31_spt = {
    'type': 'ServerProfileTemplateV4', 'name': 'OVF806_SPT',
    'serverProfileDescription': 'Server Profile Template',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {'osDeploymentPlanUri': 'dpWithUserName',
                             'osCustomAttributes': cas_dpWithUserName['osCustomAttributes']},
    'connectionSettings': {
        'manageConnections': True,
        'connections': [{'id': 1, 'name': 'Deployment Network A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-b', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto',
                 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': None}

edit_tc31_spt = {
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dpWith1Nic_StaticNic',
        'osCustomAttributes': cas_dpWith1Nic_StaticNic['osCustomAttributes']}}

tc34_sp = {
    'type': 'ServerProfileV8',
    'name': 'OVF806_SP',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
    'serverHardwareTypeUri': 'SHT:' + env.servers[0]['serverHardwareTypeUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'hideUnusedFlexNics': True,
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
               'osDeploymentPlanUri': 'dpWith1Nic_StaticNic',
               'osCustomAttributes': cas_dpWith1Nic_StaticNic['osCustomAttributes'],
        'osVolumeUri': None},
    'connectionSettings': {
        "reapplyState": "NotApplying",
        'connections': [{'id': 1, 'name': 'Deployment Network A',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['iscsi'],
                         'portId': 'Mezz 3:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500',
                         'ipv4': {'ipAddressSource': 'SubnetPool'},
                         'boot': {'bootVolumeSource': 'UserDefined',
                                  'priority': 'Primary', 'ethernetBootType': 'iSCSI',
                                  'iscsi': {'initiatorNameSource': 'ProfileInitiatorName'}}},
                        {'id': 2, 'name': 'Blade_boot_mgmt',
                         'functionType': 'Ethernet', 'networkUri': 'ETH:' + env.networks['mgmt'],
                         'portId': 'Mezz 3:1-b', 'requestedVFs': 0, 'requestedMbps': '2500',
                         'boot': {'priority': 'NotBootable', 'iscsi': {}}}]},
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto', 'mode': 'UEFIOptimized'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}}

edit_tc35_sp = {
    'type': 'ServerProfileV8', 'name': 'OVF806_SP',
    'serverProfileTemplateUri': 'SPT:' + spt['name'],
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'SH:' + env.servers[0]['serverHardwareUri'],
    'enclosureGroupUri': 'EG:' + env.egs[0]['enclosureGroupUri'],
    'affinity': 'Bay', 'hideUnusedFlexNics': True,
    'firmware': {'forceInstallFirmware': False, 'manageFirmware': False},
    'macType': 'Virtual', 'wwnType': 'Virtual',
    'osDeploymentSettings': {
        'osDeploymentPlanUri': 'dpWithUserName',
        'osCustomAttributes': cas_dpWithUserName['osCustomAttributes']},
    'connectionSettings': connSettings,
    'bootMode': {'manageMode': True, 'pxeBootPolicy': 'Auto',
                 'mode': 'UEFIOptimized', 'secureBoot': 'Unmanaged'},
    'boot': {'manageBoot': True, 'order': []},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'localStorage': {},
    'sanStorage': None}

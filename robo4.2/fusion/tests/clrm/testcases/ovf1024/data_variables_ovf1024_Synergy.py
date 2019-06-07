"""
 data variable file for import test case in Synergy Setup
"""
ov_ip = '10.1.1.122'
ov_credentials = {'userName': 'Administrator', 'password': 'admin123'}
vol_storage_sys_uri = "SSYS:test"
vol_storage_sys_uri_iscsi = "SSYS:CLRM-QA-VSA"
target_vcenter = {'vc': '10.1.0.21', 'user': 'Administrator@vsphere.local', 'password': 'Welcome123#',
                  'datacenter': 'DC1_Reg', 'cluster': 'Import_Cluster'
                  }

target_vcenter_38 = {'vc': '10.1.0.38', 'user': 'Administrator@vsphere.local', 'password': 'Orion!@#123',
                     'datacenter': 'DC1', 'cluster': 'Import_Cluster'
                     }

target_vcenter_OVTC45327 = {'vc': '10.1.0.30', 'user': 'Administrator@vsphere.local', 'password': 'Welcome123#',
                            'datacenter': 'DC1_Reg', 'cluster': 'OVTC33074'
                            }

deploy_configs = {
    'user': 'root',
    'password': "hpVSE123#"
}

server_hardware_list = ["MXQ7480421, bay 6"]
server_hardware_list_1 = ["MXQ7480421, bay 6", "MXQ7480421, bay 12"]

server_hardware_list_different_Hw = ["MXQ7480421, bay 6", "SGH736WS9C, bay 3"]
EG_122 = 'EG-3enc'
virtualSwitchConfigPolicy = {
    "manageVirtualSwitches": True,
    "configurePortGroups": True
}

hypervisorClusterSettings = {
    "type": "Vmware",
    "drsEnabled": False,
    "haEnabled": False,
    "multiNicVMotion": False,
    "virtualSwitchType": "Standard"
}

cluster_extra_volumes = [{'id': 3,
                          "volumeStorageSystemUri": vol_storage_sys_uri,
                          'lunType': 'Auto',
                          "volumeUri": "svol6",
                          'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                          },
                         {'id': 4,
                          "volumeStorageSystemUri": vol_storage_sys_uri,
                          'lunType': 'Auto',
                          "volumeUri": "svol2",
                          'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                          }]
EG = EG_122
SPT_Type = 'ServerProfileTemplateV6'
SP_Type = 'ServerProfileV11'
HCP_Type = 'HypervisorClusterProfileV3'
Server_hardware_type = ['SHT:SY 480 Gen9 1', 'SHT:SY 480 Gen9 2']
osDeploymentPlan = ['ESX-6.7_singleNic']

SPT_Import = [{'name': 'OVTC29141_SPT', 'type': SPT_Type, 'serverProfileDescription': '', 'serverHardwareTypeUri': Server_hardware_type[0],
               'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                                      'connections': [
                                          {
                                              "id": 1,
                                              "name": "Deployment Network A",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:1-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {
                                              "id": 2,
                                              "name": "Deployment Network B",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:2-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_nw1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 5, 'name': 'conn_ns', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 6, 'name': 'conn_prod', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_146', 'boot': {'priority': 'NotBootable'}}
                                      ]},
               'boot': {'manageBoot': True, 'order': ["HardDisk"]},
               'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
               'osDeploymentSettings': {
                   "osDeploymentPlanUri": osDeploymentPlan[0],
                   "osCustomAttributes": [
                       {
                           "name": "Hostname",
                           "value": "{enclosure}{enclosurebay}",
                           "constraints": "{\"helpText\":\"\"}",
                           "type": "hostname"
                       },
                       {
                           "name": "ManagementNIC.vlanid",
                           "value": "0",
                           "constraints": None,
                           "type": "integer"
                       },
                       {
                           "name": "ManagementNIC.networkuri",
                           "value": "ETH:mgmt_nw",
                           "constraints": None,
                           "type": None
                       },
                       {
                           "name": "Password",
                           "value": "hpVSE123#",
                           "constraints": None,
                           "type": "password"
                       },
                       {
                           "name": "ManagementNIC.constraint",
                           "value": "auto",
                           "constraints": None,
                           "type": None
                       },
                       {
                           "name": "SSH",
                           "value": "enabled",
                           "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                           "type": "option"
                       },
                       {
                           "name": "DomainName",
                           "value": "lab.local",
                           "constraints": "{\"helpText\":\"\"}",
                           "type": "fqdn"
                       },
                       {
                           "name": "ManagementNIC.connectionid",
                           "value": "3",
                           "constraints": None,
                           "type": None
                       }
                   ]
},
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [
                       {'id': 1,
                        "volumeStorageSystemUri": vol_storage_sys_uri,
                        'lunType': 'Auto',
                                   "volumeUri": "v:svol5",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        },
                       {'id': 2,
                        "volumeStorageSystemUri": vol_storage_sys_uri,
                        'lunType': 'Auto',
                                   "volumeUri": "v:svol6",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        }]}},
    {'name': 'OVTC33040_SPT', 'type': SPT_Type, 'serverProfileDescription': '', 'serverHardwareTypeUri': Server_hardware_type[0],
               'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
               'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                                      'connections': [
                                          {
                                              "id": 1,
                                              "name": "Deployment Network A",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:1-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {
                                              "id": 2,
                                              "name": "Deployment Network B",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:2-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                          {"id": 4, "name": 'iscsi_conn', 'functionType': 'Ethernet','portId': 'Mezz 3:1-b', "requestedMbps": "2500", 'networkUri': 'ETH:iscsi_nw', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 5, 'name': 'conn_ns', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 6, 'name': 'conn_prod', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_146', 'boot': {'priority': 'NotBootable'}}
                                      ]},
               'boot': {'manageBoot': True, 'order': ["HardDisk"]},
               'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
               'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
               'bios': {'manageBios': False, 'overriddenSettings': []},
               'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
               'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
               'osDeploymentSettings': {
                   "osDeploymentPlanUri": osDeploymentPlan[0],
                   "osCustomAttributes": [
                       {
                           "name": "Hostname",
                           "value": "{enclosure}{enclosurebay}",
                           "constraints": "{\"helpText\":\"\"}",
                           "type": "hostname"
                       },
                       {
                           "name": "ManagementNIC.vlanid",
                           "value": "0",
                           "constraints": None,
                           "type": "integer"
                       },
                       {
                           "name": "ManagementNIC.networkuri",
                           "value": "ETH:mgmt_nw",
                           "constraints": None,
                           "type": None
                       },
                       {
                           "name": "Password",
                           "value": "hpVSE123#",
                           "constraints": None,
                           "type": "password"
                       },
                       {
                           "name": "ManagementNIC.constraint",
                           "value": "auto",
                           "constraints": None,
                           "type": None
                       },
                       {
                           "name": "SSH",
                           "value": "enabled",
                           "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                           "type": "option"
                       },
                       {
                           "name": "DomainName",
                           "value": "lab.local",
                           "constraints": "{\"helpText\":\"\"}",
                           "type": "fqdn"
                       },
                       {
                           "name": "ManagementNIC.connectionid",
                           "value": "3",
                           "constraints": None,
                           "type": None
                       }
                   ]
},
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [
                       {'id': 1,
                        "volumeStorageSystemUri": vol_storage_sys_uri_iscsi,
                        'lunType': 'Auto',
                                   "volumeUri": "v:iSCSI_vol",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        },
                       {'id': 2,
                        "volumeStorageSystemUri": vol_storage_sys_uri_iscsi,
                        'lunType': 'Auto',
                                   "volumeUri": "v:ISCCSI_Vol1",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        }]}},
    {'name': 'OVTC29143_SPT', 'type': SPT_Type, 'serverProfileDescription': '', 'serverHardwareTypeUri': Server_hardware_type[0],
     'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
     'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                                      'connections': [
                                          {
                                              "id": 1,
                                              "name": "Deployment Network A",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:1-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {
                                              "id": 2,
                                              "name": "Deployment Network B",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:2-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_nw1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 5, 'name': 'conn_ns', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 6, 'name': 'conn_prod', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},

                                      ]},
     'boot': {'manageBoot': True, 'order': ["HardDisk"]},
     'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'osDeploymentSettings': {
        "osDeploymentPlanUri": osDeploymentPlan[0],
        "osCustomAttributes": [
            {
                "name": "Hostname",
                "value": "{enclosure}{enclosurebay}",
                "constraints": "{\"helpText\":\"\"}",
                "type": "hostname"
            },
            {
                "name": "ManagementNIC.vlanid",
                "value": "0",
                "constraints": None,
                "type": "integer"
            },
            {
                "name": "ManagementNIC.networkuri",
                "value": "ETH:mgmt_nw",
                "constraints": None,
                "type": None
            },
            {
                "name": "Password",
                "value": "hpVSE123#",
                "constraints": None,
                "type": "password"
            },
            {
                "name": "ManagementNIC.constraint",
                "value": "auto",
                "constraints": None,
                "type": None
            },
            {
                "name": "SSH",
                "value": "enabled",
                "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                "type": "option"
            },
            {
                "name": "DomainName",
                "value": "lab.local",
                "constraints": "{\"helpText\":\"\"}",
                "type": "fqdn"
            },
            {
                "name": "ManagementNIC.connectionid",
                "value": "3",
                "constraints": None,
                "type": None
            }
        ]
    },
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [
                       {'id': 1,
                        "volumeStorageSystemUri": vol_storage_sys_uri,
                        'lunType': 'Auto',
                                   "volumeUri": "v:svol5",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]}]}},
    {'name': 'OVTC29144_SPT_1', 'type': SPT_Type, 'serverProfileDescription': '', 'serverHardwareTypeUri': Server_hardware_type[0],
     'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
     'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                                      'connections': [
                                          {
                                              "id": 1,
                                              "name": "Deployment Network A",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:1-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {
                                              "id": 2,
                                              "name": "Deployment Network B",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:2-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_nw1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 5, 'name': 'conn_ns', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 6, 'name': 'conn_prod', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_146', 'boot': {'priority': 'NotBootable'}}
                                      ]},
     'boot': {'manageBoot': True, 'order': ["HardDisk"]},
     'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'osDeploymentSettings': {
        "osDeploymentPlanUri": osDeploymentPlan[0],
        "osCustomAttributes": [
            {
                "name": "Hostname",
                "value": "{enclosure}{enclosurebay}",
                "constraints": "{\"helpText\":\"\"}",
                "type": "hostname"
            },
            {
                "name": "ManagementNIC.vlanid",
                "value": "0",
                "constraints": None,
                "type": "integer"
            },
            {
                "name": "ManagementNIC.networkuri",
                "value": "ETH:mgmt_nw",
                "constraints": None,
                "type": None
            },
            {
                "name": "Password",
                "value": "hpVSE123#",
                "constraints": None,
                "type": "password"
            },
            {
                "name": "ManagementNIC.constraint",
                "value": "auto",
                "constraints": None,
                "type": None
            },
            {
                "name": "SSH",
                "value": "enabled",
                "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                "type": "option"
            },
            {
                "name": "DomainName",
                "value": "lab.local",
                "constraints": "{\"helpText\":\"\"}",
                "type": "fqdn"
            },
            {
                "name": "ManagementNIC.connectionid",
                "value": "3",
                "constraints": None,
                "type": None
            }
        ]
    },
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [
                       {'id': 1,
                        "volumeStorageSystemUri": vol_storage_sys_uri,
                        'lunType': 'Auto',
                                   "volumeUri": "v:svol5",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        }]}},

    {'name': 'OVTC29144_SPT_2', 'type': SPT_Type, 'serverProfileDescription': '', 'serverHardwareTypeUri': Server_hardware_type[1],
     'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
     'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                                      'connections': [
                                          {
                                              "id": 1,
                                              "name": "Deployment Network A",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:1-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {
                                              "id": 2,
                                              "name": "Deployment Network B",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:i3s_deploy_nw",
                                              "portId": "Mezz 3:2-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                              "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                              "lagName": None
                                          },
                                          {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_nw1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 5, 'name': 'conn_ns', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:netset1', 'boot': {'priority': 'NotBootable'}},
                                          {'id': 6, 'name': 'conn_prod', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:net_146', 'boot': {'priority': 'NotBootable'}}
                                      ]},
     'boot': {'manageBoot': True, 'order': ["HardDisk"]},
     'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'osDeploymentSettings': {
        "osDeploymentPlanUri": osDeploymentPlan[0],
        "osCustomAttributes": [
            {
                "name": "Hostname",
                "value": "{enclosure}{enclosurebay}",
                "constraints": "{\"helpText\":\"\"}",
                "type": "hostname"
            },
            {
                "name": "ManagementNIC.vlanid",
                "value": "0",
                "constraints": None,
                "type": "integer"
            },
            {
                "name": "ManagementNIC.networkuri",
                "value": "ETH:mgmt_nw",
                "constraints": None,
                "type": None
            },
            {
                "name": "Password",
                "value": "hpVSE123#",
                "constraints": None,
                "type": "password"
            },
            {
                "name": "ManagementNIC.constraint",
                "value": "auto",
                "constraints": None,
                "type": None
            },
            {
                "name": "SSH",
                "value": "enabled",
                "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                "type": "option"
            },
            {
                "name": "DomainName",
                "value": "lab.local",
                "constraints": "{\"helpText\":\"\"}",
                "type": "fqdn"
            },
            {
                "name": "ManagementNIC.connectionid",
                "value": "3",
                "constraints": None,
                "type": None
            }
        ]
    },
    'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                   'volumeAttachments': [
                       {'id': 1,
                        "volumeStorageSystemUri": vol_storage_sys_uri,
                        'lunType': 'Auto',
                                   "volumeUri": "v:svol5",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        }]}},
    {'name': 'OVTC64029_SPT', 'type': SPT_Type, 'serverProfileDescription': '',
     'serverHardwareTypeUri': Server_hardware_type[0], 'enclosureGroupUri': 'EG:' + EG,
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '',
     'affinity': 'Bay',
     'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                            'connections': [
                                {
                                    "id": 1,
                                    "name": "Deployment Network A",
                                    "functionType": "Ethernet",
                                    "networkUri": "ETH:i3s_deploy_nw",
                                    "portId": "Mezz 3:1-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                    "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                    "lagName": None
                                },
                                {
                                    "id": 2,
                                    "name": "Deployment Network B",
                                    "functionType": "Ethernet",
                                    "networkUri": "ETH:i3s_deploy_nw",
                                    "portId": "Mezz 3:2-a",
                                              "requestedVFs": "Auto",
                                              "requestedMbps": "2500",
                                              "ipv4": {
                                                  "ipAddressSource": "SubnetPool"
                                              },
                                    "boot": {
                                                  "bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {
                                                      "initiatorNameSource": "ProfileInitiatorName",
                                                      "secondBootTargetIp": "",
                                                      "chapLevel": "None"
                                                  },
                                                  "bootVlanId": None
                                              },
                                    "lagName": None
                                },
                                {'id': 3, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_3par_nw1', 'boot': {'priority': 'NotBootable'}},
                                {'id': 4, 'name': 'conn_ns', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:OVTC64029_netset_untag_prod_vmotion', 'boot': {'priority': 'NotBootable'}},
                                {'id': 5, 'name': 'conn_ns2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:OVTC64029_netset_untag_prod_vmotion', 'boot': {'priority': 'NotBootable'}}
                            ]},
     'boot': {'manageBoot': True, 'order': ["HardDisk"]},
     'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'osDeploymentSettings': {
         "osDeploymentPlanUri": osDeploymentPlan[0],
         "osCustomAttributes": [
             {
                 "name": "Hostname",
                 "value": "{enclosure}{enclosurebay}",
                 "constraints": "{\"helpText\":\"\"}",
                 "type": "hostname"
             },
             {
                 "name": "ManagementNIC.vlanid",
                 "value": "0",
                 "constraints": None,
                 "type": "integer"
             },
             {
                 "name": "ManagementNIC.networkuri",
                 "value": "ETH:net_148",
                 "constraints": None,
                 "type": None
             },
             {
                 "name": "Password",
                 "value": "hpVSE123#",
                 "constraints": None,
                 "type": "password"
             },
             {
                 "name": "ManagementNIC.constraint",
                 "value": "auto",
                 "constraints": None,
                 "type": None
             },
             {
                 "name": "SSH",
                 "value": "enabled",
                 "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                 "type": "option"
             },
             {
                 "name": "DomainName",
                 "value": "lab.local",
                 "constraints": "{\"helpText\":\"\"}",
                 "type": "fqdn"
             },
             {
                 "name": "ManagementNIC.connectionid",
                 "value": "3",
                 "constraints": None,
                 "type": None
             }
         ]
     },
     'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                    'volumeAttachments': [
                                  {'id': 1,
                                   "volumeStorageSystemUri": vol_storage_sys_uri,
                                   'lunType': 'Auto',
                                   "volumeUri": "v:svol5",
                                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                                   }]}},
    {'name': 'OVTC29150_SPT', 'type': SPT_Type, 'serverProfileDescription': '',
     'serverHardwareTypeUri': Server_hardware_type[0], 'enclosureGroupUri': 'EG:' + EG,
     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
     'connectionSettings': {'manageConnections': True, "complianceControl": "Checked",
                            'connections': [{"id": 1,
                                             "name": "Deployment Network A",
                                             "functionType": "Ethernet",
                                             "networkUri": "ETH:i3s_deploy_nw",
                                             "portId": "Mezz 3:1-a",
                                             "requestedVFs": "Auto",
                                             "requestedMbps": "2500",
                                             "ipv4": {"ipAddressSource": "SubnetPool"},
                                             "boot": {"bootVolumeSource": "UserDefined",
                                                      "priority": "Primary",
                                                      "ethernetBootType": "iSCSI",
                                                      "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                                "secondBootTargetIp": "",
                                                                "chapLevel": "None"},
                                                      "bootVlanId": None},
                                             "lagName": None},
                                            {"id": 2,
                                             "name": "Deployment Network B",
                                             "functionType": "Ethernet",
                                             "networkUri": "ETH:i3s_deploy_nw",
                                             "portId": "Mezz 3:2-a",
                                             "requestedVFs": "Auto",
                                             "requestedMbps": "2500",
                                             "ipv4": {"ipAddressSource": "SubnetPool"},
                                             "boot": {"bootVolumeSource": "UserDefined",
                                                      "priority": "Secondary",
                                                      "ethernetBootType": "iSCSI",
                                                      "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                                "secondBootTargetIp": "",
                                                                "chapLevel": "None"},
                                                      "bootVlanId": None},
                                             "lagName": None},
                                            {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                            {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_3par_nw1', 'boot': {'priority': 'NotBootable'}},
                                            {'id': 5, 'name': 'netset1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:network_set5', 'boot': {'priority': 'NotBootable'}},
                                            {'id': 6, 'name': 'netset2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:network_set5', 'boot': {'priority': 'NotBootable'}}]},
     'boot': {'manageBoot': True, 'order': ["HardDisk"]},
     'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
     'osDeploymentSettings': {"osDeploymentPlanUri": "ESX-6.7_singleNic",
                              "osCustomAttributes": [{"name": "Hostname",
                                                      "value": "{enclosure}{enclosurebay}",
                                                      "constraints": "{\"helpText\":\"\"}",
                                                      "type": "hostname"},
                                                     {"name": "ManagementNIC.vlanid",
                                                      "value": "0",
                                                      "constraints": None,
                                                      "type": "integer"},
                                                     {"name": "ManagementNIC.networkuri",
                                                      "value": "ETH:mgmt_nw",
                                                      "constraints": None,
                                                      "type": None},
                                                     {"name": "Password",
                                                      "value": "hpVSE123#",
                                                      "constraints": None,
                                                      "type": "password"},
                                                     {"name": "ManagementNIC.constraint",
                                                      "value": "auto",
                                                      "constraints": None,
                                                      "type": None},
                                                     {"name": "SSH",
                                                      "value": "enabled",
                                                      "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                                                      "type": "option"},
                                                     {"name": "DomainName",
                                                      "value": "lab.local",
                                                      "constraints": "{\"helpText\":\"\"}",
                                                      "type": "fqdn"},
                                                     {"name": "ManagementNIC.connectionid",
                                                      "value": "3",
                                                      "constraints": None,
                                                      "type": None}]},
     'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                    'volumeAttachments': [{'id': 1,
                                           "volumeStorageSystemUri": vol_storage_sys_uri,
                                           'lunType': 'Auto',
                                           "volumeUri": "v:svol5",
                                           'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]}]}}]

profiles_OVTC29141 = [{"type": SP_Type, "name": "OVTC29141_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC29143 = [{"type": SP_Type, "name": "OVTC29143_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29143_SPT"}]

profiles_OVTC29144 = [{"type": SP_Type, "name": "OVTC29144_SP_1",
                       "serverHardwareUri": 'SH:' + server_hardware_list_different_Hw[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT_1"},
                      {"type": SP_Type, "name": "OVTC29144_SP_2",
                       "serverHardwareUri": 'SH:' + server_hardware_list_different_Hw[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT_2"}]

profiles_OVTC33056 = [{"type": SP_Type, "name": "OVTC33056_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC45327 = [{"type": SP_Type, "name": "OVTC45327_SP_1",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC64029_SPT"},
                      {"type": SP_Type, "name": "OVTC45327_SP_2",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC64029_SPT"}]

OVTC29145_hardware = [{'type': HCP_Type, 'name': 'OVTC29145', 'server_hardware': server_hardware_list_1[1:2]}]

profiles_OVTC64029 = [{"type": SP_Type, "name": "OVTC64029_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC64029_SPT"},
                      {"type": SP_Type, "name": "OVTC64029_SP_2",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC64029_SPT"}]

profiles_OVTC29141 = [{"type": SP_Type, "name": "OVTC29141_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC33064 = [{"type": SP_Type, "name": "OVTC33064_SP1",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"},
                      {"type": SP_Type, "name": "OVTC33064_SP2",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC33082 = [{"type": SP_Type, "name": "OVTC33082_SP1",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"},
                      {"type": SP_Type, "name": "OVTC33082_SP2",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC33070 = [{"type": SP_Type, "name": "OVTC33070_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC33063 = [{"type": SP_Type, "name": "OVTC33063_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC29151 = [{"type": SP_Type, "name": "OVTC29151_SP_1",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT_1"},
                      {"type": "SP_Type", "name": "OVTC29151_SP_2",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT_1"}]

profiles_OVTC63963 = [{"type": SP_Type, "name": "OVTC63963_SP_1",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC64029_SPT"}
                      ]

profiles_OVTC29150 = [{"type": SP_Type, "name": "OVTC29150_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29150_SPT"}]

profiles_OVTC45342 = [{"type": SP_Type, "name": "OVTC45342_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT_1"}]

profiles_OVTC63961 = [{"name": "OVTC63961_SP", "type": SP_Type, "serverHardwareTypeUri": Server_hardware_type[0],
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       'enclosureGroupUri': 'EG:' + EG, "serialNumberType": "Virtual",
                       "macType": "Virtual", "wwnType": "Virtual", "description": "", "affinity": "Bay",
                       'connectionSettings': {'connections': [{"id": 1,
                                                               "name": "Deployment Network A",
                                                               "functionType": "Ethernet",
                                                               "networkUri": "ETH:i3s_deploy_nw",
                                                               "portId": "Mezz 3:1-a",
                                                               "requestedVFs": "Auto",
                                                               "requestedMbps": "2500",
                                                               "ipv4": {"ipAddressSource": "SubnetPool"},
                                                               "boot": {"bootVolumeSource": "UserDefined",
                                                                        "priority": "Primary",
                                                                        "ethernetBootType": "iSCSI",
                                                                        "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                                                  "secondBootTargetIp": "",
                                                                                  "chapLevel": "None"},
                                                                        "bootVlanId": None},
                                                               "lagName": None},
                                                              {"id": 2,
                                                               "name": "Deployment Network B",
                                                               "functionType": "Ethernet",
                                                               "networkUri": "ETH:i3s_deploy_nw",
                                                               "portId": "Mezz 3:2-a",
                                                               "requestedVFs": "Auto",
                                                               "requestedMbps": "2500",
                                                               "ipv4": {"ipAddressSource": "SubnetPool"},
                                                               "boot": {"bootVolumeSource": "UserDefined",
                                                                        "priority": "Secondary",
                                                                        "ethernetBootType": "iSCSI",
                                                                        "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                                                  "secondBootTargetIp": "",
                                                                                  "chapLevel": "None"},
                                                                        "bootVlanId": None},
                                                               "lagName": None},
                                                              {'id': 3, 'name': 'corp_conn', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:mgmt_nw', 'boot': {'priority': 'NotBootable'}},
                                                              {'id': 4, 'name': 'san_conn', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FC:fc_3par_nw1', 'boot': {'priority': 'NotBootable'}},
                                                              {'id': 5, 'name': 'netset1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:network_set5', 'boot': {'priority': 'NotBootable'}},
                                                              {'id': 6, 'name': 'netset2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:network_set5', 'boot': {'priority': 'NotBootable'}}]},
                       'boot': {'manageBoot': True, 'order': ["HardDisk"]},
                       'bootMode': {'manageMode': True, 'mode': "UEFIOptimized", 'pxeBootPolicy': "Auto", 'secureBoot': "Unmanaged"},
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                       'bios': {'manageBios': False, 'overriddenSettings': []},
                       'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                       'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
                       'osDeploymentSettings': {"osDeploymentPlanUri": "ESX-6.7_singleNic",
                                                "osCustomAttributes": [{"name": "Hostname",
                                                                        "value": "{enclosure}{enclosurebay}",
                                                                        "constraints": "{\"helpText\":\"\"}",
                                                                        "type": "hostname"},
                                                                       {"name": "ManagementNIC.vlanid",
                                                                        "value": "0",
                                                                        "constraints": None,
                                                                        "type": "integer"},
                                                                       {"name": "ManagementNIC.networkuri",
                                                                        "value": "ETH:mgmt_nw",
                                                                        "constraints": None,
                                                                        "type": None},
                                                                       {"name": "Password",
                                                                        "value": "hpVSE123#",
                                                                        "constraints": None,
                                                                        "type": "password"},
                                                                       {"name": "ManagementNIC.constraint",
                                                                        "value": "auto",
                                                                        "constraints": None,
                                                                        "type": None},
                                                                       {"name": "SSH",
                                                                        "value": "enabled",
                                                                        "constraints": "{\"options\":[\"enabled\",\"disabled\"]}",
                                                                        "type": "option"},
                                                                       {"name": "DomainName",
                                                                        "value": "lab.local",
                                                                        "constraints": "{\"helpText\":\"\"}",
                                                                        "type": "fqdn"},
                                                                       {"name": "ManagementNIC.connectionid",
                                                                        "value": "3",
                                                                        "constraints": None,
                                                                        "type": None}]},
                       "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                      "volumeAttachments": []}}]

profiles_OVTC45337 = [{"type": SP_Type, "name": "OVTC45337_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list_1[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

profiles_OVTC45337_update = [{"type": SP_Type, "name": "OVTC45337_SP",
                              "serverHardwareUri": 'SH:' + server_hardware_list_1[1],
                              "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT"}]

host_datacenter = 'DC2'

OVTC64029_update = [{'type': HCP_Type, 'name': 'OVTC64029', 'server_hardware': server_hardware_list_1[:2]}]
OVTC64030_update = [{'type': HCP_Type, 'name': 'OVTC64030', 'server_hardware': server_hardware_list_1[:2]}]
OVTC64031_update = [{'type': HCP_Type, 'name': 'OVTC64031', 'HostProfileUris': []}]
OVTC64032_update = [{'type': HCP_Type, 'name': 'OVTC64032', 'HostProfileUris': []}]
OVTC29151_update1 = [{'type': HCP_Type, 'name': 'OVTC29151', 'shared_volume': [{'name': "svol6", 'volumeFileSystemType': 'VMFS'}]}]
OVTC29151_update2 = [{'type': HCP_Type, 'name': 'OVTC29151', 'HostProfileUris': [server_hardware_list_1[1:2]], 'del_shared_volume': ['svol6']}]
OVTC45337_grow = [{'type': HCP_Type, 'name': 'OVTC45337', 'server_hardware': [server_hardware_list_1[0]]}]
OVTC45337_shrink = [{'type': HCP_Type, 'name': 'OVTC45337', 'HostProfileUris': [server_hardware_list_1[1]]}]

OVTC45342_switch_name = "net_146"
OVTC33054_cluster = [{'type': HCP_Type, 'name': 'OVTC33054_1', 'path': target_vcenter['datacenter'], 'vcenter': target_vcenter['vc'],
                      'profile_name': "OVTC29141_SPT", 'hypervisor_type': 'Vmware', 'server_password': 'hpVSE123#',
                      'shared_volume': [{'name': 'svol5', 'volumeFileSystemType': 'VMFS'}],
                      'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}]

profiles_OVTC33040 = [{"type": SP_Type, "name": "OVTC33040_SP", "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC33040_SPT"}]
OVTC33040_volume_name = "iSCSI_vol"

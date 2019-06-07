"""
 data variable file for import test case in IPv6 Setup
"""
ov_ip = '[fd17:3fc6:e357:6e4b:0:0:0:25]'
ov_credentials = {'userName': 'Administrator', 'password': 'admin123'}
vol_storage_sys_uri = "SSYS:CLRM-QA-VSA"
enclosure_type = "C7K"

server_hardware_list = ["SGH538YVJH, bay 8"]

server_hardware_list_different_Hw = ["SGH538YVJH, bay 11", "SGH538YVJH, bay 6"]

target_vcenter_ipv4 = {'vc': '10.1.0.38', 'user': 'Administrator@vsphere.local', 'password': 'Orion!@#123',
                       'datacenter': 'Sushil_DC', 'cluster': 'Test Cluster'
                       }

target_vcenter_ipv6 = {'vc': 'fd17:3fc6:e357:6e4b:0:0:0:23', 'user': 'Administrator@vsphere.local', 'password': 'Welcome123#',
                       'datacenter': 'Sushil_DC', 'cluster': 'Import_Cluster_C7K'
                       }
target_vcenter = {'vc': 'fd17:3fc6:e357:6e4b:0:0:0:23', 'user': 'Administrator@vsphere.local', 'password': 'Welcome123#',
                  'datacenter': 'BAla_DC', 'cluster': 'Import_Cluster_IPV6'
                  }

mgmt_net = {'ips': ['10.1.1.231', '10.1.1.232', '10.1.1.233', '10.1.1.234', '10.1.1.235', '10.1.1.236'],
            'netmask': '255.255.252.0', 'gw': '10.1.0.1'
            }

mgmt_net_ipv6 = {'ips': ['fd17:3fc6:e357:6e4b:0:0:0:51', 'fd17:3fc6:e357:6e4b:0:0:0:52', 'fd17:3fc6:e357:6e4b:0:0:0:53',
                         'fd17:3fc6:e357:6e4b:0:0:0:54', 'fd17:3fc6:e357:6e4b:0:0:0:55', 'fd17:3fc6:e357:6e4b:0:0:0:56',
                         'fd17:3fc6:e357:6e4b:0:0:0:57', 'fd17:3fc6:e357:6e4b:0:0:0:58', 'fd17:3fc6:e357:6e4b:0:0:0:59'],
                 'netmask': '64'
                 }

ipv6 = "True"

if ipv6 == "True":
    target_vcenter = target_vcenter
    mgmt_net = mgmt_net_ipv6

mgmt_nic = "vmnic2"

# parameters for Autodeploy
deploy_configs = {
    "deployment_vc": {'vc': '10.1.47.13', 'user': 'Administrator@vsphere.local', 'password': 'Welcome123#',
                      'datacenter': 'Deploy_DC', 'cluster': 'test_cluster1'
                      },
    "add_rule": "E:\\Shares\\testRepo\prod\\fusion\\tests\\clrm\\esxi_autodeploy\\Add_autodeploy_rule.ps1",
    "remove_rule": "E:\\Shares\\testRepo\prod\\fusion\\tests\\clrm\\esxi_autodeploy\\Remove_autodeploy_rule.ps1",
                "esxi_config": {'version': '6.7',
                                "depot_path": "E:\\Shares\\autodeploy\\HPE-ESXi-6.7.0-Update1-Gen9plus-670.U1.10.3.5.12.zip",
                                'image': "HPE-ESXi-6.7.0-Update1-Gen9plus-670.U1.10.3.5.12",
                                'profile': 'ESXI_67_C7k_G9',
                                'user': 'root',
                                'password': "Welcome123#"
                                }
}

# Parameters for ESXI Deployment via CPT tool
esxi_cred = {'user': 'root',
             'password': "HPvse123$"
             }

cpt_host = {"host": "10.1.0.34",
            "user": "root",
            "password": "iso*help"}

ESXi65 = {"os_name": "ESXi65x64",
          "os_repo": "http://10.1.0.34/iso/vmware/6.5/VMware-ESXi-6.5.0-Update2-8294253-HPE-Gen9plus-650.U2.10.2.0.14-May2018.iso",
          "deployment_network": "net_147",
          "ilo_user": "iloadmin",
          "ilo_pass": "admin123"}

ESXi67 = {"os_name": "ESXi67",
          "os_repo": "http://10.1.0.34/iso/vmware/6.7/VMware-VCSA-all-6.7.0-U1-10244745.iso",
          "deployment_network": "net_147",
          "ilo_user": "iloadmin",
          "ilo_pass": "admin123"}


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
EG = 'EG1'

# SPT Import for AutoDeploy
SPT_Import = [
    {
        'name': 'OVTC29141_SPT', 'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
        'enclosureGroupUri': 'EG:' + EG, 'affinity': 'Bay',
        'hideUnusedFlexNics': True,
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'osDeploymentSettings': None,
        'firmware': {'complianceControl': 'Checked', 'manageFirmware': False, 'forceInstallFirmware': False},
        'connectionSettings': {'complianceControl': 'Checked', 'manageConnections': True,
                               'connections': [
                                   {'id': 1, 'name': 'net_147_1', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Mezz 3:1-a', 'boot': {"priority": "Primary", "ethernetBootType": "PXE"}},
                                   {'id': 2, 'name': 'net_147_2', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 3, 'name': 'mgmt1', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 4, 'name': 'mgmt2', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 5, 'name': 'vmotion1', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 6, 'name': 'vmotion2', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}}
                               ]
                               },
        'bootMode': {'complianceControl': 'Checked', 'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'complianceControl': 'Checked', 'manageBoot': True, 'order': ['HardDisk']},
        'bios': {'complianceControl': 'Unchecked', 'manageBios': False, 'overriddenSettings': []},
        'localStorage': {'complianceControl': 'Unchecked', 'sasLogicalJBODs': [], 'controllers': []}

    },
    {
        'name': 'OVTC29143_SPT', 'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
        'enclosureGroupUri': 'EG:' + EG, 'affinity': 'Bay',
        'hideUnusedFlexNics': True,
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'osDeploymentSettings': None,
        'firmware': {'complianceControl': 'Checked', 'manageFirmware': False, 'forceInstallFirmware': False},
        'connectionSettings': {'complianceControl': 'Checked', 'manageConnections': True,
                               'connections': [
                                   {'id': 1, 'name': 'net_147_1', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Mezz 3:1-a', 'boot': {"priority": "Primary", "ethernetBootType": "PXE"}},
                                   {'id': 2, 'name': 'net_147_2', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 3, 'name': 'mgmt1', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 4, 'name': 'mgmt2', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 5, 'name': 'vmotion1', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 6, 'name': 'vmotion2', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}}
                               ]
                               },
        'bootMode': {'complianceControl': 'Checked', 'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'complianceControl': 'Checked', 'manageBoot': True, 'order': ['HardDisk']},
        'bios': {'complianceControl': 'Unchecked', 'manageBios': False, 'overriddenSettings': []},
        'localStorage': {'complianceControl': 'Unchecked', 'sasLogicalJBODs': [], 'controllers': []}
    },
    {
        'name': 'OVTC29144_SPT', 'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
        'enclosureGroupUri': 'EG:' + EG, 'affinity': 'Bay',
        'hideUnusedFlexNics': True,
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'osDeploymentSettings': None,
        'firmware': {'complianceControl': 'Checked', 'manageFirmware': False, 'forceInstallFirmware': False},
        'connectionSettings': {'complianceControl': 'Checked', 'manageConnections': True,
                               'connections': [
                                   {'id': 1, 'name': 'net_147_1', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Mezz 3:1-a', 'boot': {"priority": "Primary", "ethernetBootType": "PXE"}},
                                   {'id': 2, 'name': 'net_147_2', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 3, 'name': 'mgmt1', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 4, 'name': 'mgmt2', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 5, 'name': 'vmotion1', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 6, 'name': 'vmotion2', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}}
                               ]
                               },
        'bootMode': {'complianceControl': 'Checked', 'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'complianceControl': 'Checked', 'manageBoot': True, 'order': ['HardDisk']},
        'bios': {'complianceControl': 'Unchecked', 'manageBios': False, 'overriddenSettings': []},
        'localStorage': {'complianceControl': 'Unchecked', 'sasLogicalJBODs': [], 'controllers': []}
    },
    {
        'name': 'OVTC29144_SPT_1', 'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen10 1',
        'enclosureGroupUri': 'EG:' + EG, 'affinity': 'Bay',
        'hideUnusedFlexNics': True,
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'osDeploymentSettings': None,
        'firmware': {'complianceControl': 'Checked', 'manageFirmware': False, 'forceInstallFirmware': False},
        'connectionSettings': {'complianceControl': 'Checked', 'manageConnections': True,
                               'connections': [
                                   {'id': 1, 'name': 'net_147_1', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Mezz 3:1-a', 'boot': {"priority": "Primary", "ethernetBootType": "PXE"}},
                                   {'id': 2, 'name': 'net_147_2', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 3, 'name': 'mgmt1', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 4, 'name': 'mgmt2', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 5, 'name': 'vmotion1', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 6, 'name': 'vmotion2', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}}
                               ]
                               },
        'bootMode': {'complianceControl': 'Checked', 'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'complianceControl': 'Checked', 'manageBoot': True, 'order': ['HardDisk']},
        'bios': {'complianceControl': 'Unchecked', 'manageBios': False, 'overriddenSettings': []},
        'localStorage': {'complianceControl': 'Unchecked', 'sasLogicalJBODs': [], 'controllers': []}
    },
    {
        'name': 'OVTC29145_SPT', 'type': 'ServerProfileTemplateV7',
        'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
        'enclosureGroupUri': 'EG:' + EG, 'affinity': 'Bay',
        'hideUnusedFlexNics': True,
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'osDeploymentSettings': None,
        'firmware': {'complianceControl': 'Checked', 'manageFirmware': False, 'forceInstallFirmware': False},
        'connectionSettings': {'complianceControl': 'Checked', 'manageConnections': True,
                               'connections': [
                                   {'id': 1, 'name': 'net_147_1', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Mezz 3:1-a', 'boot': {"priority": "Primary", "ethernetBootType": "PXE"}},
                                   {'id': 2, 'name': 'net_147_2', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 3, 'name': 'mgmt1', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 4, 'name': 'mgmt2', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 5, 'name': 'vmotion1', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}},
                                   {'id': 6, 'name': 'vmotion2', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'boot': {'priority': 'NotBootable'}}
                               ]
                               },
        'bootMode': {'complianceControl': 'Checked', 'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
        'boot': {'complianceControl': 'Checked', 'manageBoot': True, 'order': ['HardDisk']},
        'bios': {'complianceControl': 'Unchecked', 'manageBios': False, 'overriddenSettings': []},
        'localStorage': {'complianceControl': 'Unchecked', 'sasLogicalJBODs': [], 'controllers': []}
    }
]

# SPT import payload for CPT
SPT_Import_cpt = [{
    'name': 'OVTC29141_SPT', 'type': 'ServerProfileTemplateV6',
    'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen9 1',
    'enclosureGroupUri': 'EG:' + EG, 'affinity': 'Bay',
    'hideUnusedFlexNics': True,
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'serialNumberType': 'Virtual',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'osDeploymentSettings': None,
    'firmware': {'complianceControl': 'Checked', 'manageFirmware': False, 'forceInstallFirmware': False},
    'connectionSettings': {'complianceControl': 'Checked', 'manageConnections': True,
                           'connections': [
                               {'id': 1, 'name': 'net_147_1', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Flb 1:1-a', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'boot': {'priority': 'NotBootable'}},
                               {'id': 2, 'name': 'net_147_2', 'functionType': 'Ethernet', 'networkUri': 'ETH:net_147', 'portId': 'Auto', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'boot': {'priority': 'NotBootable'}},
                               {'id': 3, 'name': 'mgmt1', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'boot': {'priority': 'NotBootable'}},
                               {'id': 4, 'name': 'mgmt2', 'functionType': 'Ethernet', 'networkUri': 'ETH:mgmt_nw', 'portId': 'Auto', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'boot': {'priority': 'NotBootable'}},
                               {'id': 5, 'name': 'vmotion1', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'boot': {'priority': 'NotBootable'}},
                               {'id': 6, 'name': 'vmotion2', 'functionType': 'Ethernet', 'networkUri': 'ETH:vmotion_nw', 'portId': 'Auto', 'requestedVFs': 'Auto', 'requestedMbps': '2500', 'boot': {'priority': 'NotBootable'}}
                           ]
                           },
    'bootMode': {'complianceControl': 'Checked', 'manageMode': True, 'mode': 'UEFIOptimized', 'pxeBootPolicy': 'Auto', 'secureBoot': 'Unmanaged'},
    'boot': {'complianceControl': 'Checked', 'manageBoot': True, 'order': ['HardDisk']},
    'bios': {'complianceControl': 'Unchecked', 'manageBios': False, 'overriddenSettings': []},
    'localStorage': {'complianceControl': 'Unchecked', 'sasLogicalJBODs': [], 'controllers': []},
    'sanStorage': {}
}
]

profiles_OVTC29141 = [{"type": "ServerProfileV10", "name": "OVTC29141_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29141_SPT",
                       }]

profiles_OVTC29143 = [{"type": "ServerProfileV10", "name": "OVTC29143_SP",
                       "serverHardwareUri": 'SH:' + server_hardware_list[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29143_SPT",
                       }]

profiles_OVTC29144 = [{"type": "ServerProfileV10", "name": "OVTC29144_SP_1",
                       "serverHardwareUri": 'SH:' + server_hardware_list_different_Hw[0],
                       "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT",
                       }, {"type": "ServerProfileV10", "name": "OVTC29144_SP_2",
                           "serverHardwareUri": 'SH:' + server_hardware_list_different_Hw[1],
                           "serverProfileTemplateUri": "SPT:" + "OVTC29144_SPT_1",
                           }]

OVTC29145_hardware = [{'type': 'HypervisorClusterProfileV3', 'name': 'OVTC29145', 'server_hardware': ["SGH538YVJH, bay 11"]}]

appliance_ip = '10.1.2.111'
credentials = {'userName': 'Administrator', 'password': 'admin123'}

# List of Server names as seen in Oneview
servers = ['EB1301-BOTTOM, bay 3']

mgmt_nic = "vmnic1"

mgmt_net = {'ips': ['10.1.1.232', '10.1.1.233', '10.1.1.234', '10.1.1.235', '10.1.1.236'],
            'netmask': '255.255.252.0', 'gw': '10.1.0.1'
            }

mgmt_net_ipv6 = {'ips': ['fd17:3fc6:e357:6e4b:0:0:0:41', 'fd17:3fc6:e357:6e4b:0:0:0:42', 'fd17:3fc6:e357:6e4b:0:0:0:43'],
                 'netmask': '64'
                 }

target_vcenter = {'vc': '10.1.0.38', 'user': 'Administrator@vsphere.local', 'password': 'Orion!@#123',
                  'datacenter': 'Sushil_DC', 'cluster': 'AutoDeploy Cluster 1'
                  }

target_vcenter_ipv6 = {'vc': 'fd17:3fc6:e357:6e4b:0:0:0:23', 'user': 'Administrator@vsphere.local', 'password': 'Welcome123#',
                       'datacenter': 'Sushil_DC', 'cluster': 'Import_Cluster_C7K'
                       }

ipv6 = "False"

if ipv6 == "True":
    target_vcenter = target_vcenter_ipv6
    mgmt_net = mgmt_net_ipv6

autodeploy_configs = {
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

# Sample Server Profile payload for BL460c Gen10 with initialization of the Local Disk Array
sp_bl460c_gen10 = {
    "type": "ServerProfileV10",
    "name": "",
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "Deployment Network", "functionType": "Ethernet", "networkUri": "net_147", "portId": "Auto",
             "boot": {"priority": "Primary", "ethernetBootType": "PXE"}
             },
            {"id": 2, "name": "Management Network", "functionType": "Ethernet", "networkUri": "mgmt_nw", "portId": "Auto"},
            {"id": 3, "name": "Vmotion Network", "functionType": "Ethernet", "networkUri": "vmotion_nw", "portId": "Auto"}
        ]
    },
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False
    },
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"manageBios": False},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {"deviceSlot": "Embedded", "mode": "Mixed", "initialize": True, "importConfiguration": False,
                "logicalDrives": [
                    {"name": "Boot Volume", "raidLevel": "RAID0", "bootable": True, "numPhysicalDrives": 1
                     }
                ]
             }
        ]
    },
    "sanStorage": {"manageSanStorage": False, "volumeAttachments": [], "sanSystemCredentials": [],
                   "reapplyState": "NotApplying"
                   },
    "osDeploymentSettings": None
}

# Sample Server Profile payload for BL460c Gen9 with initialization of the Local Disk Array and SAN attached Volume
sp_bl460c_gen9_san = {
    "type": "ServerProfileV10",
    "name": "",
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "Deployment Network", "functionType": "Ethernet", "networkUri": "net_147", "portId": "Auto",
             "boot": {"priority": "Primary", "ethernetBootType": "PXE"}
             },
            {"id": 2, "name": "Management Network", "functionType": "Ethernet", "networkUri": "mgmt_nw", "portId": "Auto"},
            {"id": 3, "name": "FC", "functionType": "FibreChannel", "networkUri": "fc", "portId": "Auto"},
            {"id": 4, "name": "Vmotion Network", "functionType": "Ethernet", "networkUri": "vmotion_nw", "portId": "Auto"}
        ]
    },
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareBaselineUri": None
    },
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"manageBios": False},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {"deviceSlot": "Embedded", "mode": "RAID", "initialize": True, "importConfiguration": False,
                "logicalDrives": [
                    {"name": "Boot Volume", "raidLevel": "RAID0", "bootable": True, "numPhysicalDrives": 1
                     }
                ]
             }
        ]
    },
    "osDeploymentSettings": None,
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "VMware (ESXi)",
        "sanSystemCredentials": [],
        "volumeAttachments": [
            {
                "id": 1,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 3,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                        "targets": []
                    }
                ],
                "volumeUri": "/rest/storage-volumes/C9EDF15E-8FFC-4238-A858-A95300DFE074",
                "volume": None,
                "volumeStorageSystemUri": "/rest/storage-systems/7CE603P6V5",
                "bootVolumePriority": "NotBootable"
            }
        ]
    }
}


sp_bl460c_gen9 = {
    "type": "ServerProfileV10",
    "name": "",
    "connectionSettings": {
        "connections": [
            {"id": 1, "name": "Deployment Network", "functionType": "Ethernet", "networkUri": "net_147", "portId": "Auto",
             "boot": {"priority": "Primary", "ethernetBootType": "PXE"}
             },
            {"id": 2, "name": "Management Network", "functionType": "Ethernet", "networkUri": "mgmt_nw", "portId": "Auto"},
            {"id": 3, "name": "Vmotion Network", "functionType": "Ethernet", "networkUri": "vmotion_nw", "portId": "Auto"}
        ]
    },
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareBaselineUri": None
    },
    "bootMode": {"manageMode": True, "mode": "UEFIOptimized"},
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bios": {"manageBios": False},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": [
            {"deviceSlot": "Embedded", "mode": "RAID", "initialize": True, "importConfiguration": False,
                "logicalDrives": [
                    {"name": "Boot Volume", "raidLevel": "RAID0", "bootable": True, "numPhysicalDrives": 1
                     }
                ]
             }
        ]
    },
    "sanStorage": {"manageSanStorage": False, "volumeAttachments": [], "sanSystemCredentials": [],
                   "reapplyState": "NotApplying"
                   },
    "osDeploymentSettings": None
}

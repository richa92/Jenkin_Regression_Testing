"""
Data variable file for CLRM iSCSI test cases
"""

import copy

# ===============================================================================
#  User Credential
# ===============================================================================
admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}
OV_IP = '10.1.1.21'
APPLIANCE_IP = OV_IP
vCenterIp = "15.146.41.132"
vCenterUsername = 'administrator@vsphere.local'
VcenterPassword = 'Welcome123#'

# ===============================================================================
#  Resource info
# ===============================================================================

HCP_TYPE = "HypervisorClusterProfileV3"
SPT_TYPE = "ServerProfileTemplateV6"
setup = {}
setup["tbird122"] = {"ServerHardware": ["SGH737XX1T, bay 1", "SGH737XX1T, bay 5"],
                     "ServerHardwareType": ["SY 480 Gen9 1"],
                     "EG": "EG-3enc"}
setup["tbird21"] = {"ServerHardware": ["SGH538YVJH, bay 6", "SGH538YVJH, bay 5"],
                    "ServerHardwareType": ["SY 480 Gen10 1"],
                    "EG": "EG"}
network = {"mgmt": "mgmt_nw",
           "i3s_net": "i3s_deploy_nw",
           "general2": "internal_net_1",
           "tunnel": "tunneled_nw",
           "vmotion1": "vmotion_nw",
           "vmotion2": "net_147",
           "untagged": "untagged_nw",
           "ft": "ft_nw",
           "ft2": "ft_net2",
           "production": "net_146",
           "iscsi": "iscsi_nw",
           "fc1": "3par_fc_nw1",
           "ns1": "ns_mgmt_vm_prod",
           "ns2": "Netset_Production1"}
# ===============================================================================
#  set up
# ===============================================================================
setupName = "tbird21"

SHT_TYPE = setup[setupName]["ServerHardwareType"]
server_hardware = setup[setupName]["ServerHardware"]
EG = setup[setupName]["EG"]


storage_systems = [{"name": "CLRM-QA-VSA", "family": "StoreVirtual", "hostname": "10.1.42.10",
                    "credentials": {"username": "admin", "password": "admin123"}}]
update_storage_systems = [{'type': 'StorageSystemV5', 'name': 'CLRM-QA-VSA', 'family': 'StoreVirtual',
                           "hostname": '10.1.42.10', 'credentials': {'username': 'admin', 'password': 'admin123'},
                           "ports": [{"expectedNetworkUri": "ETH:iscsi_nw", "expectedNetworkName": "iscsi_nw",
                                      "mode": "Managed", "name": "10.1.42.10"}]}]
storage_pools = [{"storageSystemUri": "CLRM-QA-VSA", "name": "CLRM-QA-VSA", "isManaged": True}]
storage_volumes = [{"properties": {"name": "vsa_vol1", "description": "", "storagePool": "CLRM-QA-VSA",
                                   "size": 11000000000, "provisioningType": "Thin",
                                   "dataProtectionLevel": "NetworkRaid10Mirror2Way", "isShareable": True},
                    "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "vsa_vol2", "description": "", "storagePool": "CLRM-QA-VSA",
                                   "size": 11000000000, "provisioningType": "Thin",
                                   "dataProtectionLevel": "NetworkRaid10Mirror2Way", "isShareable": True},
                    "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "vsa_vol3", "description": "", "storagePool": "CLRM-QA-VSA",
                                   "size": 11000000000, "provisioningType": "Thin",
                                   "dataProtectionLevel": "NetworkRaid10Mirror2Way", "isShareable": True},
                    "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "vsa_vol4", "description": "", "storagePool": "CLRM-QA-VSA",
                                   "size": 11000000000, "provisioningType": "Thin",
                                   "dataProtectionLevel": "NetworkRaid10Mirror2Way", "isShareable": True},
                    "templateUri": "ROOT", "isPermanent": True}]

storage = {"storageSystem": "CLRM-QA-VSA", "storagePool": "CLRM-QA-VSA",
           "vol": ["vsa_vol1", "vsa_vol2", "vsa_vol3", "vsa_vol4"]}

# ===============================================================================
#  CLRM information
# ===============================================================================
vCenter_version = "6.5.0"
vCenter = [{'username': vCenterUsername, 'password': VcenterPassword,
            'type': 'HypervisorManagerV2', 'name': vCenterIp,
            'port': '443', 'version': vCenter_version}]

data_center = 'DC_iSCSI'

os_deployment_plan = '/rest/os-deployment-plans/ce46242f-ad02-4961-b704-988e2aa2e00c'
deploymentCustomArgs = [{"argumentName": "SSH", "argumentValue": "enabled"},
                        {"argumentName": "DomainName", "argumentValue": "lab.local"},
                        {"argumentName": "Hostname", "argumentValue": "{enclosurebay}{serialnumber}"}]


# ===============================================================================
# Template payload
# ===============================================================================
SPT_payload_122 = [{"name": "SPT_iscsi", "type": SPT_TYPE,
                    "serverProfileDescription": "", "serverHardwareTypeUri": "SHT:" + SHT_TYPE[0],
                    "enclosureGroupUri": "EG:" + EG, "serialNumberType": "Virtual", "macType": "Virtual",
                    "wwnType": "Virtual", "description": "", "affinity": "Bay",
                    "connectionSettings": {"manageConnections": True, "complianceControl": "Checked",
                                           "connections": [{"id": 1, "name": "mgmt_conn", "functionType": "Ethernet",
                                                            "portId": "Mezz 3:1-c", "requestedMbps": "2500",
                                                            "networkUri": "ETH:" + network["mgmt"]},
                                                           {"id": 2, "name": "iscsi_conn", "functionType": "Ethernet",
                                                            "portId": "Mezz 3:1-b", "requestedMbps": "2500",
                                                            "networkUri": "ETH:" + network["iscsi"]},
                                                           {"id": 3, "name": "ns_conn", "functionType": "Ethernet",
                                                            "portId": "Mezz 3:2-c", "requestedMbps": "2500",
                                                            "networkUri": "NS:" + network["ns1"]}]},
                    "boot": {"manageBoot": True, "order": ["HardDisk"]},
                    "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                    "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                                 "firmwareInstallType": None},
                    "bios": {"manageBios": False, "overriddenSettings": []},
                    "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                    "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                   "volumeAttachments": [{"id": 1,
                                                          "volumeStorageSystemUri": "SSYS:" + storage["storageSystem"],
                                                          "bootVolumePriority": "NotBootable",
                                                          "lunType": "Auto",
                                                          "volumeUri": "v:" + storage["vol"][0],
                                                          "storagePaths": [{"isEnabled": True, "connectionId": 2,
                                                                            "targetSelector": "Auto", "targets": []}]
                                                          }]}}]

SPT_payload_21 = [{"name": "SPT_iscsi", "type": SPT_TYPE,
                   "serverProfileDescription": "", "serverHardwareTypeUri": "SHT:" + SHT_TYPE[0],
                   "enclosureGroupUri": "EG:" + EG, "serialNumberType": "Virtual", "macType": "Virtual",
                   "wwnType": "Virtual", "description": "", "affinity": "Bay",
                   "connectionSettings": {"manageConnections": True, "complianceControl": "Checked",
                                          "connections": [{"id": 1, "name": "mgmt_conn", "functionType": "Ethernet",
                                                           "portId": "Mezz 3:1-c", "requestedMbps": "2500",
                                                           "networkUri": "ETH:" + network["mgmt"]},
                                                          {"id": 2, "name": "iscsi", "functionType": "Ethernet",
                                                           "portId": "Mezz 3:1-b", "requestedMbps": "2500",
                                                           "networkUri": "ETH:" + network["iscsi"]},
                                                          {"id": 3, "name": "conn_prod1", "functionType": "Ethernet",
                                                           "portId": "Mezz 3:1-d", "requestedMbps": "2500",
                                                           "networkUri": "NS:" + network["ns2"]}]},
                   "boot": {"manageBoot": True, "order": ["HardDisk"]},
                   "bootMode": {"manageMode": True, "mode": "UEFIOptimized", "pxeBootPolicy": "Auto"},
                   "firmware": {"manageFirmware": False, "firmwareBaselineUri": "", "forceInstallFirmware": False,
                                "firmwareInstallType": None},
                   "bios": {"manageBios": False, "overriddenSettings": []},
                   "hideUnusedFlexNics": True, "iscsiInitiatorNameType": "AutoGenerated",
                   "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                   "sanStorage": {"hostOSType": "VMware (ESXi)", "manageSanStorage": True,
                                  "volumeAttachments": [{"id": 1,
                                                         "volumeStorageSystemUri": "SSYS:" + storage["storageSystem"],
                                                         "bootVolumePriority": "NotBootable",
                                                         "lunType": "Auto",
                                                         "volumeUri": "v:" + storage["vol"][0],
                                                         "storagePaths": [{"isEnabled": True, "connectionId": 2,
                                                                           "targetSelector": "Auto", "targets": []}]
                                                         }]}}]
SPT_setup = {"tbird122": SPT_payload_122,
             "tbird21": SPT_payload_21}
SPT_payload = copy.deepcopy(SPT_setup[setupName])
# ===============================================================================
#  test cases payload
# ===============================================================================

SPT_iSCSI_Vol_2 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_2[0]["name"] = "SPT_iSCSI_Vol_2"


SPT_iSCSI_Vol_2_update = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_2_update[0]["name"] = "SPT_iSCSI_Vol_2"
SPT_iSCSI_Vol_2_update[0]["sanStorage"]["volumeAttachments"] = [{"id": 1,
                                                                 "volumeStorageSystemUri": "SSYS:" + storage["storageSystem"],
                                                                 "isBootVolume": False, "lunType": "Auto",
                                                                 "volumeUri": "v:" + storage["vol"][2],
                                                                 "storagePaths": [{"isEnabled": True,
                                                                                   "connectionId": 2,
                                                                                   "targetSelector": "Auto",
                                                                                   "targets": []}]}]

HCP_iSCSI_Vol_2 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_2', 'path': data_center, 'vcenter': vCenterIp,
                    'profile_name': 'SPT_iSCSI_Vol_2', 'hypervisor_type': 'Vmware',
                    'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                    'deploymentCustomArgs': deploymentCustomArgs,
                    'server_hardware': [server_hardware[0]],
                    'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                         'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks',
                                         'distributed_switch_version': vCenter_version},
                    'shared_volume': [{'name': storage["vol"][1], 'volumeFileSystemType': 'VMFS'}]}]

HCP_iSCSI_Vol_2_update = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_2', 'server_hardware': [server_hardware[1]],
                           'shared_volume': [{'name': storage["vol"][3], 'volumeFileSystemType': 'VMFS'},
                                             {'name': storage["vol"][2], 'volumeFileSystemType': 'VMFS'}]}]

SPT_iSCSI_Vol_21 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_21[0]["name"] = "SPT_iSCSI_Vol_21"

HCP_iSCSI_Vol_21 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_21', 'path': data_center, 'vcenter': vCenterIp,
                     'profile_name': 'SPT_iSCSI_Vol_21', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                     'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs,
                     'server_hardware': [server_hardware[0]],
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                          'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks',
                                          'distributed_switch_version': vCenter_version},
                     'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'}]}]

SPT_iSCSI_Vol_6 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_6[0]["name"] = "SPT_iSCSI_Vol_6"

HCP_iSCSI_Vol_6 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_6', 'path': data_center, 'vcenter': vCenterIp,
                    'profile_name': 'SPT_iSCSI_Vol_6', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                    'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs, 'server_hardware': [server_hardware[1]],
                    'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                         'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': vCenter_version},
                    'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'},
                                      {'name': storage["vol"][2], 'volumeFileSystemType': 'VMFS'}]}]

HCP_iSCSI_Vol_6_update = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_6', 'del_shared_volume': [storage["vol"][1]]}]

SPT_iSCSI_Vol_25 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_25[0]["name"] = "SPT_iSCSI_Vol_25"
HCP_iSCSI_Vol_25 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_25', 'path': data_center, 'vcenter': vCenterIp,
                     'profile_name': 'SPT_iSCSI_Vol_25', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                     'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs, 'server_hardware': [server_hardware[1]],
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                          'distributed_switch_usage': 'AllNetworks', 'distributed_switch_version': vCenter_version},
                     'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'}]}]

SPT_iSCSI_Vol_12 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_12[0]["name"] = "SPT_iSCSI_Vol_12"
SPT_iSCSI_Vol_12_update = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_12_update[0]["name"] = "SPT_iSCSI_Vol_12"
SPT_iSCSI_Vol_12_update[0]["sanStorage"]["volumeAttachments"] = []
HCP_iSCSI_Vol_12 = [{'type': 'HypervisorClusterProfileV3', 'name': 'HCP_iSCSI_Vol_12', 'path': data_center,
                     'vcenter': vCenterIp, 'profile_name': SPT_iSCSI_Vol_12[0]["name"], 'hypervisor_type': 'Vmware',
                     'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                     'deploymentCustomArgs':deploymentCustomArgs,
                     'server_hardware': [server_hardware[0]],
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard',
                                          'multi_nic_vmotion': 'true'},
                     'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'},
                                       {'name': storage["vol"][1], 'volumeFileSystemType': 'VMFS'}]}]

SPT_iSCSI_Vol_7 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_7[0]["name"] = "SPT_iSCSI_Vol_7"
HCP_iSCSI_Vol_7 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_7', 'path': data_center, 'vcenter': "vcsa3.lab.local",
                    'profile_name': 'SPT_iSCSI_Vol_7', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                    'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs,
                    'server_hardware': [server_hardware[0], server_hardware[1]],
                    'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                         'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks',
                                         'distributed_switch_version': vCenter_version},
                    'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'},
                                      {'name': storage["vol"][2], 'volumeFileSystemType': 'VMFS'}]}]

HCP_iSCSI_Vol_7_update = [{'type': 'HypervisorClusterProfileV3', 'name': 'HCP_iSCSI_Vol_7', 'HostProfileUris': [server_hardware[1]]}]
HCP_iSCSI_Vol_1 = copy.deepcopy(HCP_iSCSI_Vol_7)
HCP_iSCSI_Vol_1[0]['name'] = "HCP_iSCSI_Vol_1"

SPT_iSCSI_Vol_24 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_24[0]["name"] = "SPT_iSCSI_Vol_24"
HCP_iSCSI_Vol_24 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_24', 'path': data_center, 'vcenter': vCenterIp,
                     'profile_name': 'SPT_iSCSI_Vol_24', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                     'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs,
                     'server_hardware': [server_hardware[0]],
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                          'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks',
                                          'distributed_switch_version': '6.0.0'},
                     'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'}]}]

SPT_iSCSI_Vol_5 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_5[0]["name"] = "SPT_iSCSI_Vol_5"
HCP_iSCSI_Vol_5 = [{'type': HCP_TYPE, 'name': 'HCP_iSCSI_Vol_5', 'path': data_center, 'vcenter': vCenterIp,
                    'profile_name': 'SPT_iSCSI_Vol_5', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                    'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs,
                    'server_hardware': [server_hardware[0]],
                    'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed',
                                         'multi_nic_vmotion': 'true', 'distributed_switch_usage': 'GeneralNetworks',
                                         'distributed_switch_version': vCenter_version},
                    'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'}]}]

HCP_iSCSI_Vol_5_update = {"name": "vsa_vol1", "description": "Increasing Capacity", "provisionedCapacity": "15211160064"}

SPT_iSCSI_Vol_8 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_8[0]["name"] = "SPT_iSCSI_Vol_8"

HCP_iSCSI_Vol_30 = [{'type': HCP_TYPE, 'name': 'iSCSI_Vol_30', 'path': data_center, 'vcenter': vCenterIp,
                     'profile_name': 'SPT_iSCSI_Vol_8', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                     'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs, 'server_hardware': [server_hardware[0]],
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Distributed', 'multi_nic_vmotion': 'true',
                                          'distributed_switch_usage': 'GeneralNetworks', 'distributed_switch_version': vCenter_version},
                     'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'}]}]

HCP_iSCSI_Vol_30_update = [{'type': HCP_TYPE, 'name': 'iSCSI_Vol_30', 'shared_volume': [{'name': storage["vol"][2], 'volumeFileSystemType': 'VMFS'}]}]
added_volume = HCP_iSCSI_Vol_30_update[0]['shared_volume'][0]['name']


SPT_iSCSI_Vol_10 = copy.deepcopy(SPT_payload)
SPT_iSCSI_Vol_10[0]["name"] = "SPT_iSCSI_Vol_10"
vswitch_name = "iscsi_nw"

HCP_iSCSI_Vol_31 = [{'type': HCP_TYPE, 'name': 'iSCSI_Vol_31', 'path': data_center, 'vcenter': vCenterIp,
                     'profile_name': 'SPT_iSCSI_Vol_10', 'hypervisor_type': 'Vmware', 'deployment_uri': os_deployment_plan,
                     'server_password': 'hpVSE123#', 'deploymentCustomArgs': deploymentCustomArgs, 'server_hardware': [server_hardware[0]],
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'},
                     'shared_volume': [{'name': storage["vol"][0], 'volumeFileSystemType': 'VMFS'}]}]

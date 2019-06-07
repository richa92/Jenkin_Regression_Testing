"""
Data variable file for OOB test cases
"""
import copy
# ===============================================================================
#  User Credential
# ===============================================================================
admin_credentials = {"userName": "Administrator", "password": "admin123"}
OV_credentials = {"userName": "Administrator", "password": "admin123"}
ov_ip = "10.1.1.21"
Appliance = ov_ip
vCenterIp = "vcsa3.lab.local"
vCenterCredentials = {"user": "administrator@vsphere.local",
                      "password": "Welcome123#"}
target_vcenter = {'vc': vCenterIp, 'user': vCenterCredentials["user"],
                  'password': vCenterCredentials["password"],
                  'datacenter': 'DC1_Reg', 'cluster': 'Import_Cluster'
                  }
esxi_configs = {
    'user': 'root',
    'password': "hpVSE123#"
}
autodeploy_configs = {
    'user': 'root',
    'password': "hpVSE123#"
}
mgmt_net = ''
mgmt_nic = ''
data_center = "DC1_Reg"
hypervisorClusterSettings = {
    "type": "Vmware",
    "drsEnabled": True,
    "haEnabled": False,
    "multiNicVMotion": False,
    "virtualSwitchType": "Standard"
}
virtualSwitchConfigPolicy = {
    "manageVirtualSwitches": True,
    "configurePortGroups": True
}
# ===============================================================================
#  Resource info
# ===============================================================================
enclosure_type = "Synergy"
HCP_TYPE = "HypervisorClusterProfileV3"
SPT_TYPE = "ServerProfileTemplateV7"
osDeploymentPlans = ["ESXi-6.7.0-U1"]

customAttribute = {"hostname": "sptNode",
                   "domain": "lab.local",
                   "password": "hpVSE123#"}
setup = {}
setup["tbird122"] = {"ServerHardware": ["SGH737XX1T, bay 1", "SGH737XX1T, bay 5"],
                     "ServerHardwareType": ["SY 480 Gen9 1"],
                     "EG": "EG-3enc"}
setup["tbird21"] = {"ServerHardware": ["SGH538YVJH, bay 6", "SGH538YVJH, bay 5", "SGH538YVJH, bay 8", "SGH538YVJH, bay 7"],
                    "ServerHardwareType": ["SY 480 Gen10 1", "SY 480 Gen9 1"],
                    "EG": "EG"}

storage = {"storageSystem": "CLRM-QA-VSA", "storagePool": "CLRM-QA-VSA", "vol": ["vsa_vol1", "vsa_vol2", "vsa_vol3"]}

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
vm_settings = {"datacenter": data_center,
               "clusterName": "Cluster",
               "guestname": "VM1",
               "guestmemory": 2048,
               "guestcpu": 1,
               "guestdatastore": "datastore1",
               "guestos": "windows7_64Guest"}
# ===============================================================================
#  CLRM information
# ===============================================================================

vcenter = [{"username": vCenterCredentials["user"],
            "version":"6.5.0", "password": vCenterCredentials["password"],
            "type": "HypervisorManagerV2", "name": vCenterIp, "port": "443"}]

os_deployment_plan = "/rest/os-deployment-plans/ce46242f-ad02-4961-b704-988e2aa2e00c"
deploymentCustomArgs = [{"argumentName": "SSH", "argumentValue": "enabled"},
                        {"argumentName": "DomainName", "argumentValue": "lab.local"},
                        {"argumentName": "Hostname", "argumentValue": "{enclosurebay}{serialnumber}"}]

# ===============================================================================
#  set up
# ===============================================================================
setupName = "tbird21"
SHT_TYPE = setup[setupName]["ServerHardwareType"]
hardwares = setup[setupName]["ServerHardware"]
EG = setup[setupName]["EG"]
# ===============================================================================
# Template payload
# ===============================================================================
osdp_connections_21 = {"manageConnections": True,
                       "connections": [{"id": 1,
                                        "name": "Deployment Network A", "functionType": "Ethernet",
                                        "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                                        "networkUri": "ETH:" + network["i3s_net"],
                                        "requestedVFs": "Auto",
                                        "ipv4": {"ipAddressSource": "SubnetPool"},
                                        "boot": {"bootVolumeSource": "UserDefined",
                                                 "priority": "Primary",
                                                 "ethernetBootType": "iSCSI",
                                                 "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                           "firstBootTargetIp": None, "secondBootTargetIp": "",
                                                           "secondBootTargetPort": ""
                                                           }}},
                                       {"id": 2,
                                        "name": "", "functionType": "Ethernet",
                                        "portId": "Auto", "requestedMbps": "2500",
                                        "networkUri": "ETH:" + network["mgmt"]}
                                       ]}
osdp_connections_122 = {"manageConnections": True,
                        "connections": [{"id": 1,
                                         "name": "Deployment Network A", "functionType": "Ethernet",
                                         "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                                         "networkUri": "ETH:" + network["i3s_net"],
                                         "requestedVFs": "Auto",
                                         "ipv4": {"ipAddressSource": "SubnetPool"},
                                         "boot": {"bootVolumeSource": "UserDefined",
                                                  "priority": "Primary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                            "firstBootTargetIp": None, "secondBootTargetIp": "",
                                                            "secondBootTargetPort": ""
                                                            }}},
                                        {"id": 2,
                                         "name": "Deployment Network B", "functionType": "Ethernet",
                                         "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                                         "networkUri": "ETH:" + network["i3s_net"],
                                         "requestedVFs": "Auto",
                                         "ipv4": {"ipAddressSource": "SubnetPool"},
                                         "boot": {"bootVolumeSource": "UserDefined",
                                                  "priority": "Secondary",
                                                  "ethernetBootType": "iSCSI",
                                                  "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                                            "firstBootTargetIp": None, "secondBootTargetIp": "",
                                                            "secondBootTargetPort": ""
                                                            }}},
                                        {"id": 3,
                                         "name": "", "functionType": "Ethernet",
                                         "portId": "Auto", "requestedMbps": "2500",
                                         "networkUri": "ETH:" + network["mgmt"],
                                         "requestedVFs": "0", "ipv4": {},
                                         "boot": {"priority": "NotBootable", "iscsi": {}}},
                                        {"id": 4,
                                         "name": "", "functionType": "Ethernet",
                                         "portId": "Auto", "requestedMbps": "2500",
                                         "networkUri": "ETH:" + network["mgmt"],
                                         "requestedVFs": "0", "ipv4": {},
                                         "boot": {"priority": "NotBootable", "iscsi": {}}}]}
os_deployment_21 = {"osDeploymentPlanUri": osDeploymentPlans[0],
                    "osCustomAttributes": [{"name": "DomainName", "value": customAttribute["domain"], "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                           {"name": "Hostname", "value": customAttribute["hostname"], "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                           {"name": "ManagementNIC.connectionid", "value": "2"},
                                           {"name": "ManagementNIC.networkuri", "value": "ETH:" + network["mgmt"]},
                                           {"name": "ManagementNIC.constraint", "value": "auto"},
                                           {"name": "ManagementNIC.vlanid", "value": "0"},
                                           {"name": "Password", "value": customAttribute["password"]},
                                           {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]}

os_deployment_122 = {"osDeploymentPlanUri": osDeploymentPlans[0],
                     "osCustomAttributes": [{"name": "DomainName", "value": customAttribute["domain"], "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                            {"name": "Hostname", "value": customAttribute["hostname"], "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                            {"name": "ManagementNIC.connectionid", "value": "3"},
                                            {"name": "ManagementNIC.networkuri", "value": "ETH:" + network["mgmt"]},
                                            {"name": "ManagementNIC.constraint", "value": "auto"},
                                            {"name": "ManagementNIC.vlanid", "value": "0"},
                                            {"name": "ManagementNIC2.connectionid", "value": "4"},
                                            {"name": "ManagementNIC2.networkuri", "value": "ETH:" + network["mgmt"]},
                                            {"name": "ManagementNIC2.constraint", "value": "auto"},
                                            {"name": "ManagementNIC2.vlanid", "value": "0"},
                                            {"name": "Password", "value": customAttribute["password"]},
                                            {"name": "SSH", "value": "enabled", "constraints": "{\"options\":[\"enabled\"]}", "type": "option"}]}

SPT_payload_122 = [{"name": "SPT_payload", "type": SPT_TYPE,
                    "serverProfileDescription": "", "serverHardwareTypeUri": "SHT:" + SHT_TYPE[1],
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
                                   "volumeAttachments": []}}]

SPT_payload_21 = [{"name": "SPT_payload", "type": SPT_TYPE,
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
                                  "volumeAttachments": []}}]
SPT_setup = {"tbird122": SPT_payload_122,
             "tbird21": SPT_payload_21}
osdp_connection_setup = {"tbird122": osdp_connections_122,
                         "tbird21": osdp_connections_21}
osdp_setup = {"tbird122": os_deployment_122,
              "tbird21": os_deployment_21}
SPT_payload = copy.deepcopy(SPT_setup[setupName])
osdp_connection = copy.deepcopy(osdp_connection_setup[setupName])
osdp = copy.deepcopy(osdp_setup[setupName])

SPT_OOB = copy.deepcopy(SPT_payload)
SPT_OOB[0]["name"] = "SPT_OOB"

SPT_OVTC28489 = copy.deepcopy(SPT_payload)
SPT_OVTC28489[0]["name"] = "SPT_OVTC28489"
SPT_OVTC28489[0]["serverHardwareTypeUri"] = "SHT:" + SHT_TYPE[0]
SPT_OVTC28489[0]["osDeploymentSettings"] = osdp
SPT_OVTC28489[0]["connectionSettings"] = osdp_connection

cluster_payload_tbird = [{'type': 'HypervisorClusterProfileV3', 'name': 'HCP', 'path': data_center,
                          'vcenter': vCenterIp, 'profile_name': SPT_OOB[0]["name"], 'hypervisor_type': 'Vmware',
                          'deployment_uri': os_deployment_plan, 'server_password': 'hpVSE123#',
                          'deploymentCustomArgs':deploymentCustomArgs,
                          'server_hardware': [hardwares[0]],
                          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard',
                                               'multi_nic_vmotion': 'true'},
                          'shared_volume': []}]

CLRM_setup = {"tbird122": cluster_payload_tbird,
              "tbird21": cluster_payload_tbird}
CLRM_payload = copy.deepcopy(CLRM_setup[setupName])
# ===============================================================================
#  test cases payload
# ===============================================================================

oob_host_ip_change = copy.deepcopy(CLRM_payload)
oob_host_ip_change[0]["name"] = "HCP_OOB_host_ip_change"
oob_host_ip_change_alert = '.*One or more hypervisors in the hypervisor cluster are disconnected.*'
profiles_OVTC28489 = [{"type": "ServerProfileV10", "name": "OVTC28489_SP",
                       "serverHardwareUri": 'SH:' + hardwares[0],
                       "serverProfileTemplateUri": "SPT:" + "SPT_OVTC28489",
                       "osDeploymentSettings": osdp
                       }]
OVTC28489_SH_list = [hardwares[0]]

SPT_OVTC28490 = copy.deepcopy(SPT_payload)
SPT_OVTC28490[0]["name"] = "SPT_OVTC28490"
SPT_OVTC28490[0]["serverHardwareTypeUri"] = "SHT:" + SHT_TYPE[0]
SPT_OVTC28490[0]["osDeploymentSettings"] = osdp
SPT_OVTC28490[0]["connectionSettings"] = osdp_connection
profiles_OVTC28490 = [{"type": "ServerProfileV10", "name": "OVTC28490_SP",
                       "serverHardwareUri": 'SH:' + hardwares[0],
                       "serverProfileTemplateUri": "SPT:" + "SPT_OVTC28490",
                       "osDeploymentSettings": osdp}]
OVTC28490_SH_list = [hardwares[0]]

OVTC45267_cluster = copy.deepcopy(CLRM_payload)
OVTC45267_cluster[0]["name"] = "OVTC45267"

profiles_OVTC45340 = [{"type": "ServerProfileV11", "name": "OVTC45340_SP",
                       "serverHardwareUri": 'SH:' + hardwares[0],
                       "serverProfileTemplateUri": "SPT:" + "SPT_OVTC28489",
                       "osDeploymentSettings": osdp
                       }]

OVTC47900 = copy.deepcopy(CLRM_payload)
OVTC47900[0]["name"] = "OVTC47900"
oob_host_disconnected_alert = '.*One or more hypervisor profiles associated with the hypervisor cluster profile are in error state.*'

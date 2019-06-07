import copy
import environment_data as env

# single network

spt_conn_settings = {"connections": copy.deepcopy(env.deploy_conns) +
                     copy.deepcopy(env.mgmt_conns),
                     "manageConnections": True,
                     "complianceControl": "CheckedMinimum"}

sp_conn_settings = {"reapplyState": "NotApplying",
                    "connections": copy.deepcopy(env.deploy_conns) +
                    copy.deepcopy(env.mgmt_conns)}

more_mgmt_conns = [{"id": 6, "name": "Management Network C",
                    "functionType": "Ethernet",
                    "networkUri": "ETH:" + env.networks["p_nw2"],
                    "portId": "Auto", "requestedMbps": "2500",
                    "lagName": None, "isolatedTrunk": False,
                    "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable", "iscsi": {}}},
                   {"id": 7, "name": "Management Network D",
                    "functionType": "Ethernet",
                    "networkUri": "ETH:" + env.networks["p_nw2"],
                    "portId": "Auto", "requestedMbps": "2500",
                    "lagName": None, "isolatedTrunk": False,
                    "requestedVFs": "0", "ipv4": {},
                    "boot": {"priority": "NotBootable", "iscsi": {}}}]

spt_with_more_mgmt_conns = {"connections": copy.deepcopy(env.deploy_conns) +
                            copy.deepcopy(env.mgmt_conns) +
                            copy.deepcopy(more_mgmt_conns),
                            "manageConnections": True,
                            "complianceControl": "CheckedMinimum"}

sp_with_more_mgmt_conns = {"reapplyState": "NotApplying",
                           "connections": copy.deepcopy(env.deploy_conns) +
                           copy.deepcopy(env.mgmt_conns) +
                           copy.deepcopy(more_mgmt_conns)}

spt_conns_with_new_mgmt_conn = {"connections": copy.deepcopy(env.deploy_conns) +
                                copy.deepcopy(env.mgmt_conns) +
                                copy.deepcopy(env.new_mgmt_conn),
                                "manageConnections": True,
                                "complianceControl": "CheckedMinimum"}

sp_conns_with_new_mgmt_conn = {"reapplyState": "NotApplying",
                               "connections": copy.deepcopy(env.deploy_conns) +
                               copy.deepcopy(env.mgmt_conns) +
                               copy.deepcopy(env.new_mgmt_conn)}

spt_conns_with_extra1_mgmt_conn = {"connections": copy.deepcopy(env.deploy_conns) +
                                   copy.deepcopy(env.mgmt_conns) +
                                   copy.deepcopy(env.change_new_mgmt_conn),
                                   "manageConnections": True,
                                   "complianceControl": "CheckedMinimum"}

sp_conns_with_extra1_mgmt_conn = {"reapplyState": "NotApplying",
                                  "connections": copy.deepcopy(env.deploy_conns) +
                                  copy.deepcopy(env.mgmt_conns) +
                                  copy.deepcopy(env.change_new_mgmt_conn)}

spt_osds = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
            "complianceControl": "Checked",
            "osCustomAttributes": copy.deepcopy(env.osCustomAttributes)}

sp_osds = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
           "osVolumeUri": None,
           "osCustomAttributes": copy.deepcopy(env.osCustomAttributes)}

# To change the deployment setting network to a different network
diff_osCustomAttributes = [{"name": "DomainName", "value": "lab.local",
                            "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                           {"name": "Hostname", "value": "MultiNicSPT",
                            "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                           {"name": "ManagementNIC.connectionid", "value": "6"},
                           {"name": "ManagementNIC.dhcp", "value": "False"},
                           {"name": "ManagementNIC.ipv4disable", "value": "False"},
                           {"name": "ManagementNIC.networkuri", "value": "ETH:" + env.networks["p_nw2"]},
                           {"name": "ManagementNIC.constraint", "value": "auto"},
                           {"name": "ManagementNIC.vlanid", "value": "0"},
                           {"name": "ManagementNIC2.connectionid", "value": "7"},
                           {"name": "ManagementNIC2.dhcp", "value": "False"},
                           {"name": "ManagementNIC2.ipv4disable", "value": "False"},
                           {"name": "ManagementNIC2.networkuri", "value": "ETH:" + env.networks["p_nw2"]},
                           {"name": "ManagementNIC2.constraint", "value": "auto"},
                           {"name": "ManagementNIC2.vlanid", "value": "0"},
                           {"name": "Password", "value": "admin123"},
                           {"name": "SSH", "value": "enabled",
                            "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

# To change the SPT deployment setting network to a different network
spt_osds_with_diff_nws = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                          "complianceControl": "Checked",
                          "osCustomAttributes": copy.deepcopy(diff_osCustomAttributes)}

# To change the deployment SP setting network to a different network
sp_osds_with_diff_nws = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                         "osVolumeUri": None,
                         "osCustomAttributes": copy.deepcopy(diff_osCustomAttributes)}

mgmt_conns_with_diff_name = [{"id": 3, "name": "Management Network A1",
                              "functionType": "Ethernet",
                              "networkUri": "ETH:" + env.networks["p_nw1"],
                              "portId": "Auto", "requestedMbps": "2500",
                              "lagName": None, "isolatedTrunk": False,
                              "requestedVFs": "0", "ipv4": {},
                              "boot": {"priority": "NotBootable", "iscsi": {}}},
                             {"id": 4, "name": "Management Network B1",
                              "functionType": "Ethernet",
                              "networkUri": "ETH:" + env.networks["p_nw1"],
                              "portId": "Auto", "requestedMbps": "2500",
                              "lagName": None, "isolatedTrunk": False,
                              "requestedVFs": "0", "ipv4": {},
                              "boot": {"priority": "NotBootable", "iscsi": {}}},
                             {"id": 5, "name": "Storage Network",
                              "functionType": "FibreChannel",
                              "networkUri": "FC:" + env.networks["fc_nw"],
                              "portId": "Auto", "requestedMbps": "2500",
                              "lagName": None, "ipv4": {},
                              "boot": {"priority": "NotBootable", "iscsi": {}}}]

conns_with_diff_mgmt_nw_names = copy.deepcopy(env.deploy_conns) + copy.deepcopy(mgmt_conns_with_diff_name)

conns_with_extra_mgmt_nw = copy.deepcopy(env.deploy_conns) + copy.deepcopy(env.mgmt_conns) + copy.deepcopy(env.new_mgmt_conn)

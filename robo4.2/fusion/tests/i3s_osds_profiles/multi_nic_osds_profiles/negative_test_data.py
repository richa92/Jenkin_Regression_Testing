import copy
import environment_data as env

# diff networks for diff connections
negative_mgmt_conns = [{"id": 3, "name": "Management Network A",
                        "functionType": "Ethernet",
                        "networkUri": "ETH:" + env.networks["p_nw1"],
                        "portId": "Auto", "requestedMbps": "2500",
                        "lagName": None, "isolatedTrunk": False,
                        "requestedVFs": "0", "ipv4": {},
                        "boot": {"priority": "NotBootable", "iscsi": {}}},
                       {"id": 4, "name": "Management Network B",
                        "functionType": "Ethernet",
                        "networkUri": "ETH:" + env.networks["p_nw2"],
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

spt_negative_conn_settings = {"connections": copy.deepcopy(env.deploy_conns) +
                              copy.deepcopy(negative_mgmt_conns),
                              "manageConnections": True,
                              "complianceControl": "CheckedMinimum"}

sp_negative_conn_settings = {"reapplyState": "NotApplying",
                             "connections": copy.deepcopy(env.deploy_conns) +
                             copy.deepcopy(negative_mgmt_conns)}

# osCustomAttributes for negative scenario (diff networks for different nics)
negative_oscas = [
    {"name": "DomainName", "value": "lab.local",
     "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
    {"name": "Hostname", "value": "MultiNicSPT",
     "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
    {"name": "ManagementNIC.connectionid", "value": "3"},
    {"name": "ManagementNIC.dhcp", "value": "False"},
    {"name": "ManagementNIC.ipv4disable", "value": "False"},
    {"name": "ManagementNIC.networkuri", "value": "ETH:" + env.networks["p_nw1"]},
    {"name": "ManagementNIC.constraint", "value": "auto"},
    {"name": "ManagementNIC.vlanid", "value": "0"},
    {"name": "ManagementNIC2.connectionid", "value": "4"},
    {"name": "ManagementNIC2.dhcp", "value": "False"},
    {"name": "ManagementNIC2.ipv4disable", "value": "False"},
    {"name": "ManagementNIC2.networkuri", "value": "ETH:" + env.networks["p_nw2"]},
    {"name": "ManagementNIC2.constraint", "value": "auto"},
    {"name": "ManagementNIC2.vlanid", "value": "0"},
    {"name": "Password", "value": "admin123"},
    {"name": "SSH", "value": "enabled",
     "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

spt_ntive_osds = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                  "complianceControl": "Checked",
                  "osCustomAttributes": copy.deepcopy(negative_oscas)}

sp_ntive_osds = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                 "osVolumeUri": None,
                 "osCustomAttributes": copy.deepcopy(negative_oscas)}

osca_with_nw_as_none = [
    {"name": "DomainName", "value": "lab.local",
     "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
    {"name": "Hostname", "value": "MultiNicSPT",
     "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
    {"name": "ManagementNIC.connectionid", "value": "3"},
    {"name": "ManagementNIC.dhcp", "value": "False"},
    {"name": "ManagementNIC.ipv4disable", "value": "False"},
    {"name": "ManagementNIC.networkuri", "value": None},
    {"name": "ManagementNIC.constraint", "value": "auto"},
    {"name": "ManagementNIC.vlanid", "value": "0"},
    {"name": "ManagementNIC2.connectionid", "value": "4"},
    {"name": "ManagementNIC2.dhcp", "value": "False"},
    {"name": "ManagementNIC2.ipv4disable", "value": "False"},
    {"name": "ManagementNIC2.networkuri", "value": None},
    {"name": "ManagementNIC2.constraint", "value": "auto"},
    {"name": "ManagementNIC2.vlanid", "value": "0"},
    {"name": "Password", "value": "admin123"},
    {"name": "SSH", "value": "enabled",
     "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

spt_osds_with_nw_as_none = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                            "complianceControl": "Checked",
                            "osCustomAttributes": copy.deepcopy(osca_with_nw_as_none)}

sp_osds_with_nw_as_none = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                           "osVolumeUri": None,
                           "osCustomAttributes": copy.deepcopy(osca_with_nw_as_none)}

osds_with_nws_from_diff_netset = [
    {"name": "DomainName", "value": "lab.local",
     "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
    {"name": "Hostname", "value": "MultiNicSPT",
     "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
    {"name": "ManagementNIC.connectionid", "value": "3"},
    {"name": "ManagementNIC.dhcp", "value": "False"},
    {"name": "ManagementNIC.ipv4disable", "value": "False"},
    {"name": "ManagementNIC.networkuri", "value": "ETH:" + env.networks["p_nw1"]},
    {"name": "ManagementNIC.constraint", "value": "auto"},
    {"name": "ManagementNIC.vlanid", "value": "0"},
    {"name": "ManagementNIC2.connectionid", "value": "4"},
    {"name": "ManagementNIC2.dhcp", "value": "False"},
    {"name": "ManagementNIC2.ipv4disable", "value": "False"},
    {"name": "ManagementNIC2.networkuri", "value": "ETH:" + env.networks["p_nw5"]},
    {"name": "ManagementNIC2.constraint", "value": "auto"},
    {"name": "ManagementNIC2.vlanid", "value": "0"},
    {"name": "Password", "value": "admin123"},
    {"name": "SSH", "value": "enabled",
     "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

spt_ntive_osds_with_nws_from_diff_netset = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                                            "complianceControl": "Checked",
                                            "osCustomAttributes": copy.deepcopy(osds_with_nws_from_diff_netset)}

sp_ntive_osds_with_nws_from_diff_netset = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                                           "osVolumeUri": None,
                                           "osCustomAttributes": copy.deepcopy(osds_with_nws_from_diff_netset)}

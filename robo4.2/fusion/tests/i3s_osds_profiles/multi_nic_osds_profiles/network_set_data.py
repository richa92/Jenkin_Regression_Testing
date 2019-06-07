import copy
import environment_data as env

# Network Set data

netset_as_mgmt_conns = [{"id": 3, "name": "Management Network A",
                         "functionType": "Ethernet",
                         "networkUri": "NS:network_set1",
                         "portId": "Auto", "requestedMbps": "2500",
                         "lagName": None, "isolatedTrunk": False,
                         "requestedVFs": "0", "ipv4": {},
                         "boot": {"priority": "NotBootable", "iscsi": {}}},
                        {"id": 4, "name": "Management Network B",
                         "functionType": "Ethernet",
                         "networkUri": "NS:network_set1",
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

spt_conn_settings_with_netset = {"manageConnections": True,
                                 "complianceControl": "CheckedMinimum",
                                 "connections": copy.deepcopy(env.deploy_conns) +
                                 copy.deepcopy(netset_as_mgmt_conns)}

sp_conn_settings_with_netset = {"reapplyState": "NotApplying",
                                "connections": copy.deepcopy(env.deploy_conns) +
                                copy.deepcopy(netset_as_mgmt_conns)}

more_netsets_as_mgmt_conns = [
    {"id": 6, "name": "Management Network C",
     "functionType": "Ethernet",
     "networkUri": "NS:network_set2",
     "portId": "Auto", "requestedMbps": "2500",
     "lagName": None, "isolatedTrunk": False,
     "requestedVFs": "0", "ipv4": {},
     "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 7, "name": "Management Network D",
     "functionType": "Ethernet",
     "networkUri": "NS:network_set2",
     "portId": "Auto", "requestedMbps": "2500",
     "lagName": None, "isolatedTrunk": False,
     "requestedVFs": "0", "ipv4": {},
     "boot": {"priority": "NotBootable", "iscsi": {}}}]

spt_with_more_netset_mgmt_conns = {"connections": copy.deepcopy(env.deploy_conns) +
                                   copy.deepcopy(netset_as_mgmt_conns) +
                                   copy.deepcopy(more_netsets_as_mgmt_conns),
                                   "manageConnections": True,
                                   "complianceControl": "CheckedMinimum"}

sp_with_more_netset_mgmt_conns = {"reapplyState": "NotApplying",
                                  "connections": copy.deepcopy(env.deploy_conns) +
                                  copy.deepcopy(netset_as_mgmt_conns) +
                                  copy.deepcopy(more_netsets_as_mgmt_conns)}

diff_osCustomAttributes_of_netset = [{"name": "DomainName", "value": "lab.local",
                                      "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                     {"name": "Hostname", "value": "MultiNicSPT",
                                      "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                     {"name": "ManagementNIC.connectionid", "value": "3"},
                                     {"name": "ManagementNIC.dhcp", "value": "False"},
                                     {"name": "ManagementNIC.ipv4disable", "value": "False"},
                                     {"name": "ManagementNIC.networkuri", "value": "ETH:" + env.networks["p_nw2"]},
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

spt_osds_with_diff_nws_of_netset = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                                    "complianceControl": "Checked",
                                    "osCustomAttributes": copy.deepcopy(diff_osCustomAttributes_of_netset)}

sp_osds_with_diff_nws_of_netset = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                                   "osVolumeUri": None,
                                   "osCustomAttributes": copy.deepcopy(diff_osCustomAttributes_of_netset)}

os_cas_of_more_netset = [{"name": "DomainName", "value": "lab.local",
                          "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                         {"name": "Hostname", "value": "MultiNicSPT",
                          "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                         {"name": "ManagementNIC.connectionid", "value": "6"},
                         {"name": "ManagementNIC.dhcp", "value": "False"},
                         {"name": "ManagementNIC.ipv4disable", "value": "False"},
                         {"name": "ManagementNIC.networkuri", "value": "ETH:" + env.networks["p_nw3"]},
                         {"name": "ManagementNIC.constraint", "value": "auto"},
                         {"name": "ManagementNIC.vlanid", "value": "0"},
                         {"name": "ManagementNIC2.connectionid", "value": "7"},
                         {"name": "ManagementNIC2.dhcp", "value": "False"},
                         {"name": "ManagementNIC2.ipv4disable", "value": "False"},
                         {"name": "ManagementNIC2.networkuri", "value": "ETH:" + env.networks["p_nw3"]},
                         {"name": "ManagementNIC2.constraint", "value": "auto"},
                         {"name": "ManagementNIC2.vlanid", "value": "0"},
                         {"name": "Password", "value": "admin123"},
                         {"name": "SSH", "value": "enabled",
                          "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

spt_osds_of_more_netset = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                           "complianceControl": "Checked",
                           "osCustomAttributes": copy.deepcopy(os_cas_of_more_netset)}

sp_osds_of_more_netset = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                          "osVolumeUri": None,
                          "osCustomAttributes": copy.deepcopy(os_cas_of_more_netset)}

netset_mgmt_conns_with_diff_name = [
    {"id": 3, "name": "Management Network A1",
     "functionType": "Ethernet",
     "networkUri": "NS:network_set1",
     "portId": "Auto", "requestedMbps": "2500",
               "lagName": None, "isolatedTrunk": False,
               "requestedVFs": "0", "ipv4": {},
               "boot": {"priority": "NotBootable", "iscsi": {}}},
    {"id": 4, "name": "Management Network B1",
     "functionType": "Ethernet",
     "networkUri": "NS:network_set1",
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

netset_conns_with_diff_mgmt_nw_names = copy.deepcopy(env.deploy_conns) + copy.deepcopy(netset_mgmt_conns_with_diff_name)

netset_conns_with_extra_mgmt_nw = copy.deepcopy(env.deploy_conns) + copy.deepcopy(netset_as_mgmt_conns) + copy.deepcopy(env.new_mgmt_conn)

spt_netset_conns_with_new_mgmt_conn = {"connections": copy.deepcopy(env.deploy_conns) +
                                       copy.deepcopy(netset_as_mgmt_conns) +
                                       copy.deepcopy(env.new_mgmt_conn),
                                       "manageConnections": True,
                                       "complianceControl": "CheckedMinimum"}

sp_netset_conns_with_new_mgmt_conn = {"reapplyState": "NotApplying",
                                      "connections": copy.deepcopy(env.deploy_conns) +
                                      copy.deepcopy(netset_as_mgmt_conns) +
                                      copy.deepcopy(env.new_mgmt_conn)}

spt_netset_conns_with_diff_new_mgmt_conn = {"connections": copy.deepcopy(env.deploy_conns) +
                                            copy.deepcopy(netset_as_mgmt_conns) +
                                            copy.deepcopy(env.change_new_mgmt_conn),
                                            "manageConnections": True,
                                            "complianceControl": "CheckedMinimum"}


change_netset_in_mgmt_conns = [{"id": 3, "name": "Management Network A",
                                "functionType": "Ethernet",
                                "networkUri": "NS:network_set2",
                                "portId": "Auto", "requestedMbps": "2500",
                                "lagName": None, "isolatedTrunk": False,
                                "requestedVFs": "0", "ipv4": {},
                                "boot": {"priority": "NotBootable", "iscsi": {}}},
                               {"id": 4, "name": "Management Network B",
                                "functionType": "Ethernet",
                                "networkUri": "NS:network_set2",
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

spt_change_netset_in_mgmt_conns = {"manageConnections": True,
                                   "complianceControl": "CheckedMinimum",
                                   "connections": copy.deepcopy(env.deploy_conns) +
                                   copy.deepcopy(change_netset_in_mgmt_conns)}

os_cas_with_changed_mgmt_netset_conn = [{"name": "DomainName", "value": "lab.local",
                                         "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                                        {"name": "Hostname", "value": "MultiNicSPT",
                                         "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                                        {"name": "ManagementNIC.connectionid", "value": "3"},
                                        {"name": "ManagementNIC.dhcp", "value": "False"},
                                        {"name": "ManagementNIC.ipv4disable", "value": "False"},
                                        {"name": "ManagementNIC.networkuri", "value": "ETH:" + env.networks["p_nw3"]},
                                        {"name": "ManagementNIC.constraint", "value": "auto"},
                                        {"name": "ManagementNIC.vlanid", "value": "0"},
                                        {"name": "ManagementNIC2.connectionid", "value": "4"},
                                        {"name": "ManagementNIC2.dhcp", "value": "False"},
                                        {"name": "ManagementNIC2.ipv4disable", "value": "False"},
                                        {"name": "ManagementNIC2.networkuri", "value": "ETH:" + env.networks["p_nw3"]},
                                        {"name": "ManagementNIC2.constraint", "value": "auto"},
                                        {"name": "ManagementNIC2.vlanid", "value": "0"},
                                        {"name": "Password", "value": "admin123"},
                                        {"name": "SSH", "value": "enabled",
                                         "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

spt_osds_with_changed_mgmt_netset_conn = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                                          "complianceControl": "Checked",
                                          "osCustomAttributes": copy.deepcopy(os_cas_with_changed_mgmt_netset_conn)}

sp_osds_with_changed_mgmt_netset_conn = {"osDeploymentPlanUri": "dpWith2Nic_Nic1StaticAndDhcpNic2Static",
                                         "osVolumeUri": None,
                                         "osCustomAttributes": copy.deepcopy(os_cas_with_changed_mgmt_netset_conn)}

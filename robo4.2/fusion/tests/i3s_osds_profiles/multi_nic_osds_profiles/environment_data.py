
# Setup details
admin_credentials = {"userName": "Administrator", "password": "admin123"}

osdps = [{"name": "dpWith1Nic_StaticAndDhcpNic_TeamNic"}]

networks = {"iscsi": "i3s_deploy_nw",
            "p_nw1": "private_nw1",
            "p_nw2": "private_nw2",
            "p_nw3": "private_nw3",
            "p_nw4": "private_nw4",
            "p_nw5": "private_nw5",
            "fc_nw": "fc_nw1"}

egs = {"enclosureGroupUri": "EG-3enc"}

servers = {"serverHardwareUri": "SGH737XX1T, bay 6", "serverHardwareTypeUri": "SY 480 Gen9 1"}

netsets = ["network_set1", "network_set2", "network_set3", "network_set4"]

# Add private_nw5 to network-set
update_network_set = [{"name": "network_set1",
                       "networkUris": [],
                       "add_networkUris": ["private_nw5"],
                       "connectionTemplateUri": "",
                       "type": "network-setV4",
                       "nativeNetworkUri": None,
                       "uri": ''}]

# Delete private_nw5 to network-set
revert_network_set = [{"name": "network_set1",
                       "networkUris": [],
                       "'delete_networkUris": ["private_nw5"],
                       "connectionTemplateUri": "",
                       "type": "network-setV4",
                       "nativeNetworkUri": None,
                       "uri": ''}]

# Default Deployment connections
deploy_conns = [{"id": 1, "name": "Deployment Network A",
                 "functionType": "Ethernet",
                 "networkUri": "ETH:" + networks["iscsi"],
                 "portId": "Mezz 3:1-a", "requestedMbps": "2500",
                 "requestedVFs": "Auto",
                 "ipv4": {"ipAddressSource": "SubnetPool"},
                 "boot": {"priority": "Primary", "ethernetBootType": "iSCSI",
                          "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                    "firstBootTargetIp": None,
                                    "secondBootTargetIp": "",
                                    "secondBootTargetPort": ""},
                          "bootVolumeSource": "UserDefined"}},
                {"id": 2, "name": "Deployment Network B",
                 "functionType": "Ethernet",
                 "networkUri": "ETH:" + networks["iscsi"],
                 "portId": "Mezz 3:2-a", "requestedMbps": "2500",
                 "requestedVFs": "Auto",
                 "ipv4": {"ipAddressSource": "SubnetPool"},
                 "boot": {"priority": "Secondary", "ethernetBootType": "iSCSI",
                          "iscsi": {"initiatorNameSource": "ProfileInitiatorName",
                                    "firstBootTargetIp": None,
                                    "secondBootTargetIp": "",
                                    "secondBootTargetPort": ""},
                          "bootVolumeSource": "UserDefined"}}]

# Default management connections
mgmt_conns = [{"id": 3, "name": "Management Network A",
               "functionType": "Ethernet",
               "networkUri": "ETH:" + networks["p_nw1"],
               "portId": "Auto", "requestedMbps": "2500",
               "lagName": None, "isolatedTrunk": False,
               "requestedVFs": "0", "ipv4": {},
               "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 4, "name": "Management Network B",
               "functionType": "Ethernet",
               "networkUri": "ETH:" + networks["p_nw1"],
               "portId": "Auto", "requestedMbps": "2500",
               "lagName": None, "isolatedTrunk": False,
               "requestedVFs": "0", "ipv4": {},
               "boot": {"priority": "NotBootable", "iscsi": {}}},
              {"id": 5, "name": "Storage Network",
               "functionType": "FibreChannel",
               "networkUri": "FC:" + networks["fc_nw"],
               "portId": "Auto", "requestedMbps": "2500",
               "lagName": None, "ipv4": {},
               "boot": {"priority": "NotBootable", "iscsi": {}}}]

# Default osCustomAttributes
osCustomAttributes = [{"name": "DomainName", "value": "lab.local",
                       "constraints": "{\"helpText\":\"\"}", "type": "fqdn"},
                      {"name": "Hostname", "value": "MultiNicSPT",
                       "constraints": "{\"helpText\":\"\"}", "type": "hostname"},
                      {"name": "ManagementNIC.connectionid", "value": "3"},
                      {"name": "ManagementNIC.dhcp", "value": "False"},
                      {"name": "ManagementNIC.ipv4disable", "value": "False"},
                      {"name": "ManagementNIC.networkuri", "value": "ETH:" + networks["p_nw1"]},
                      {"name": "ManagementNIC.constraint", "value": "auto"},
                      {"name": "ManagementNIC.vlanid", "value": "0"},
                      {"name": "ManagementNIC2.connectionid", "value": "4"},
                      {"name": "ManagementNIC2.dhcp", "value": "False"},
                      {"name": "ManagementNIC2.ipv4disable", "value": "False"},
                      {"name": "ManagementNIC2.networkuri", "value": "ETH:" + networks["p_nw1"]},
                      {"name": "ManagementNIC2.constraint", "value": "auto"},
                      {"name": "ManagementNIC2.vlanid", "value": "0"},
                      {"name": "Password", "value": "admin123"},
                      {"name": "SSH", "value": "enabled",
                       "constraints": "{\"options\":[\"enabled\",\"disabled\"]}", "type": "option"}]

# Extra mgmt connection
new_mgmt_conn = [{"id": 6, "name": "Management Network E",
                  "functionType": "Ethernet",
                  "networkUri": "ETH:" + networks["p_nw3"],
                  "portId": "Auto", "requestedMbps": "2500",
                  "lagName": None, "isolatedTrunk": False,
                  "requestedVFs": "0", "ipv4": {},
                  "boot": {"priority": "NotBootable", "iscsi": {}}}]

change_new_mgmt_conn = [{"id": 6, "name": "Management Network E",
                         "functionType": "Ethernet",
                         "networkUri": "ETH:" + networks["p_nw3"],
                         "portId": "Auto", "requestedMbps": "2500",
                         "lagName": None, "isolatedTrunk": False,
                         "requestedVFs": "0", "ipv4": {},
                         "boot": {"priority": "NotBootable", "iscsi": {}}}]

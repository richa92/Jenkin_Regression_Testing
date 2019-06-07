from robot.libraries.BuiltIn import BuiltIn

Appliance_Name = 'OneViewHellfireOvst'
datacenter = 'DCV'
cluster_name = 'hellfirecluster123'
cluster_path = datacenter + '/' + cluster_name
vc_ip = '10.10.0.62'
vc_user = 'Administrator@vsphere.local'
vc_password = 'Hellfire!234'
vc_port = 443
service_access = "Disabled"
app_username = "Administrator"
app_init_password = "admin"
app_password = "hellfire"
new_appliance_ip = "10.10.4.180"
gateway_ip = "10.10.0.1"
OV_ovaloc = "http://10.10.0.130/OVST_OV/HP_OneView_VM.ova"
OV_ovf_network = "VM Network"
OV_network = "10.x mgmt"
debug_log = False
ov_net_details = [["10.10.4.181", "255.255.192.0", "10.10.0.1", ["10.10.0.22", "10.10.0.21"], "hellfire.local"]]
svmc_name = "SvmcOvstDoNotDelete"
svmc_net_details = [["10.10.4.61", "255.255.192.0", "10.10.0.1", ["10.10.0.22"], "hpe.com"]]
svmcloc = "http://10.10.0.130/OVST_OV/OVST_SVMC/hpe-svmc.ova"
svmc_ovf_network = "mgmtVMNetwork"
svmc_network = "10.x mgmt"
svmc_root_username = "root"
svmc_root_password = "hpinvent"
datacenter_svmc = "JumpStation-DC"
datastore_svmc = "QA-JS1-DataStore-1"
cluster_svmc = None
svmc_root_user = "root"
svmc_root_pw = "hpinvent"
ov_waitforip = True
svmc_waitforip = True
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}
firmware_bundles = [{'SPPFileName': 'SPP2016020.2015_1204.63.iso',
                     'SPPFilePath': 'ftp://wpstwork4.vse.rdlabs.hpecorp.net/firmware/SPP/2016.02.0\ Gen9Snap5/Released/',
                     'SPPFileMD5': 'f8eb9835e5698b9daaea4e66eaa964db',
                     'FirmwareBundleURI': '/rest/firmware-drivers/SPP2016020_2015_1204_63',
                     }
                    ]
spp_remote_path = "http://10.10.0.130/sw/HPE_HC_SP-20170419-00.iso"
spp_local_path = "C:\Users\Administrator\Documents"

# #####################################
admin_credentials = {'userName': 'Administrator', 'password': 'hellfire', "authLoginDomain": "LOCAL", "loginMsgAck": None}

# #####################################
users = [{"type": "UserAndRoles", "userName": "user", "fullName": "", "password": "dcsdcsdcs", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "roles": ["Read only"]}
         ]

# #########PREREQUISITES###############
ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'mgmt', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'vlanId': '70', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'vMotion', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'vlanId': '102', 'purpose': 'VMMigration'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'FaultTolerence', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'vlanId': '103', 'purpose': 'FaultTolerance'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'Production', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'vlanId': '104', 'purpose': 'General'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'iSCSI', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'vlanId': '101', 'purpose': 'ISCSI'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'Prod_rem_test', 'connectionTemplateUri': None, 'privateNetwork': 'true', 'type': 'ethernet-networkV300', 'vlanId': '300', 'purpose': 'General'}
                     ]

network_sets = [{'name': 'Production_set', 'type': 'network-setV300', 'networkUris': ['Production'], 'nativeNetworkUri': None},
                # {'name': 'All_Net_Sets', 'type': 'network-setV300', 'networkUris': ['mgmt', 'Production', 'vMotion', 'iSCSI', 'FaultTolerence'], 'nativeNetworkUri': None},
                {'name': 'netset1', 'type': 'network-setV300', 'networkUris': ['Production', 'iSCSI'], 'nativeNetworkUri': None}
                ]

network_sets_update_add = [{'name': 'netset1', 'add_networkUris': ['Prod_rem_test']}]

network_sets_update_delete = [{'name': 'netset1', 'delete_networkUris': ['Prod_rem_test']}]

server_hardwares = [{"hostname": "10.10.1.9", "username": "Administrator", "password": "Hellfire!234", "force": True, "licensingIntent": "OneView", "configurationState": "Managed"},
                    {"hostname": "10.10.1.33", "username": "Administrator", "password": "Hellfire!234", "force": True, "licensingIntent": "OneView", "configurationState": "Managed"},
                    {"hostname": "10.10.1.59", "username": "Administrator", "password": "Hellfire!234", "force": True, "licensingIntent": "OneView", "configurationState": "Managed"}
                    ]

server_profile_templates = [{"type": "ServerProfileTemplateV400",
                             "name": "SPT_Hellfire_cluster",
                             "description": "",
                             "serverProfileDescription": "",
                             "serverHardwareTypeUri": "SHT:DL380 Gen9 1",
                             "affinity": None,
                             "hideUnusedFlexNics": True,
                             "macType": "Physical",
                             "wwnType": "Physical",
                             "serialNumberType": "Physical",
                             "iscsiInitiatorNameType": "AutoGenerated",
                             "firmware": {"manageFirmware": False,
                                          "firmwareInstallType": None,
                                          "forceInstallFirmware": False,
                                          "firmwareBaselineUri": None
                                          },
                             "connections": [{"id": 1,
                                              "name": "",
                                              "functionType": "Ethernet",
                                              "networkUri": "NS:netset1",
                                              "portId": "Flb 1:1",
                                              "requestedVFs": "Auto"
                                              },
                                             {"id": 2,
                                              "name": "",
                                              "functionType": "Ethernet",
                                              "networkUri": "NS:netset1",
                                              "portId": "Flb 1:2",
                                              "requestedVFs": "Auto"
                                              },
                                             {"id": 3,
                                              "name": "",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:mgmt",
                                              "portId": "Lom 1:1",
                                              "requestedVFs": "Auto"
                                              },
                                             {"id": 4,
                                              "name": "",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:mgmt",
                                              "portId": "Lom 1:3",
                                              "requestedVFs": "Auto"
                                              },
                                             {"id": 5,
                                              "name": "",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:vMotion",
                                              "portId": "Lom 1:2",
                                              "requestedVFs": "Auto"
                                              },
                                             {"id": 6,
                                              "name": "",
                                              "functionType": "Ethernet",
                                              "networkUri": "ETH:vMotion",
                                              "portId": "Lom 1:4",
                                              "requestedVFs": "Auto"
                                              }
                                             ],
                             "bootMode": None,
                             "boot": {"manageBoot": False,
                                      "order": []
                                      },
                             "bios": {"manageBios": False,
                                      "overriddenSettings": []
                                      },
                             "localStorage": {"sasLogicalJBODs": [],
                                              "controllers": []
                                              },
                             "sanStorage": {"manageSanStorage": True,
                                            "hostOSType": "VMware (ESXi)",
                                            "volumeAttachments": []
                                            },
                             "category": "server-profile-templates"
                             }
                            ]

ipv4_subnet = [{'type': 'Subnet',
                'networkId': '10.10.0.0',
                'subnetmask': '255.255.192.0',
                'gateway': '10.10.0.1',
                'dnsServers': ['10.10.0.22', '10.10.0.21'],
                'domain': 'hellfire.local'
                },
               {'type': 'Subnet',
                'networkId': '172.16.0.0',
                'subnetmask': '255.255.192.0',
                'gateway': '172.16.0.1',
                'dnsServers': ['10.10.0.22', '10.10.0.21'],
                'domain': 'hellfire.local'
                },
               {'type': 'Subnet',
                'networkId': '192.168.0.0',
                'subnetmask': '255.255.192.0',
                'gateway': '192.168.0.1',
                'dnsServers': ['10.10.0.22', '10.10.0.21'],
                'domain': 'hellfire.local'
                }
               ]

ipv4_ranges = [{'type': 'Range', 'name': 'IPV4', 'startAddress': '10.10.4.161', 'endAddress': '10.10.4.190', 'subnetUri': '10.10.0.0'},
               {'type': 'Range', 'name': 'IPV4_iSCSI', 'startAddress': '172.16.4.151', 'endAddress': '172.16.4.180', 'subnetUri': '172.16.0.0'},
               {'type': 'Range', 'name': 'IPV4_vMotion', 'startAddress': '192.168.4.151', 'endAddress': '192.168.4.200', 'subnetUri': '192.168.0.0'}
               ]

subnet_association = [{'network type': 'ethernet-networkV300', 'name': 'mgmt', 'subnetUri': '10.10.0.0'},
                      {'network type': 'ethernet-networkV300', 'name': 'iSCSI', 'subnetUri': '172.16.0.0'},
                      {'network type': 'ethernet-networkV300', 'name': 'vMotion', 'subnetUri': '192.168.0.0'}
                      ]

# #####################################
hypervisor_managers = [{'username': 'Administrator@vsphere.local', 'password': 'Hellfire!234', 'type': 'HypervisorManager', 'name': '10.10.0.62'}
                       ]

######################################
cluster_profile = [{"name": "hellfirecluster123",
                    "type": "HypervisorClusterProfile",
                    "vcenter": "10.10.0.62",
                    "cluster_settings": {"virtual_switch_type": "Standard",
                                         "cluster_settings_type": "Vmware",
                                         "multi_nic_vmotion": "true",
                                         "drsEnabled": "true",
                                         "haEnabled": "true"
                                         },
                    "ip_pool": "IPV4",
                    "network": "mgmt",
                    "path": "DCV",
                    "hypervisor_type": "Vmware",
                    "profile_name": "SPT_Hellfire_cluster",
                    "deployment_manager_type": "UserManaged",
                    "virtualSwitchConfigPolicy": {"customVirtualSwitches": "false", "configurePortGroups": "true", "manageVirtualSwitches": "true", "createVmPortgroup": ["ISCSI", "Management", "VMMigration"]},
                    "server_hardware": ['ILOSGH612X538', 'ILOSGH601VSPB']
                    }
                   ]

cluster_profile_remediation = [{"name": "hellfirecluster123", "remediate": True}]

##############################################################################
# SDiRM#
##############################################################################
sdi_system_profiles = [{"Name": "OVST-VSA-test1234",
                        "ntpServers": [],
                        "SystemNodes": [{"connections": [{"isIPAutoGenerated": "True",
                                                          "networkUri": "ETH:mgmt",
                                                          "purpose": "Management"
                                                          }
                                                         ],
                                         "logicalDisks": [{"logicalDiskId": "600508B1001C8B1F24CD88D14178F6D6",
                                                           "diskCapacity": "536870912000",
                                                           "purpose": "boot",
                                                           "diskType": "HDD"
                                                           },
                                                          {"logicalDiskId": "600508B1001CFDD6549464359B3BDEF2",
                                                           "diskCapacity": "663314497536",
                                                           "purpose": "data",
                                                           "diskType": "HDD"
                                                           }
                                                          ],
                                         "name": "10-10-1-9-VSA1234",
                                         "hostingHypervisorHostProfileUri": "hellfirecluster123-node1"
                                         }
                                        ],
                        "CpuCount": "None",
                        "SystemVersion": 13.5,
                        "MemoryAllocation": "None",
                        "users": [{"username": "admin",
                                   "password": "secret",
                                   "purpose": "Administrator"
                                   }
                                  ],
                        "Locale": "en-US",
                        "SystemType": "StoreVirtualVsaCluster",
                        "SoftwareSpecificAttributes": {"svmc": {"userName": "Admin",
                                                                "password": "admin",
                                                                "ipAddress": "10.10.4.61"
                                                                },
                                                       "vips": [{"isIPAutoGenerated": "True",
                                                                 "subnetMask": "None",
                                                                 "networkUri": "ETH:iSCSI",
                                                                 "ipAddress": "None"
                                                                 }
                                                                ],
                                                       "quorum": {"userName": "",
                                                                  "ipAddress": "None",
                                                                  "password": "",
                                                                  "type": "null",
                                                                  "path": "None"
                                                                  },
                                                       "imageUri": "http://10.10.0.130/OVST_OV/OVST_VSA/VSA_Latest/VSA.ovf"
                                                       },
                        "hostingHypervisorClusterProfileUri": "hellfirecluster123",
                        "isCpuAndMemoryAutoManaged": "True"
                        }
                       ]

sdi_system_profiles_ilo = [{"Name": "OVST-VSA-test-1",
                            "ntpServers": [],
                            "SystemNodes": [{"connections": [{"isIPAutoGenerated": "True",
                                                              "networkUri": "ETH:mgmt",
                                                              "purpose": "Management"
                                                              },
                                                             {"isIPAutoGenerated": "True",
                                                              "networkUri": "ETH:iSCSI",
                                                              "purpose": "ISCSI"
                                                              }
                                                             ],
                                             "logicalDisks": [{"ilo_ipAddress": "10.10.1.9",
                                                               "UserName": "Administrator",
                                                               "Password": "Hellfire!234",
                                                               "diskType": "HDD"
                                                               }
                                                              ],
                                             "name": "10-10-1-9-VSA-1",
                                             "hostingHypervisorHostProfileUri": "Auto"
                                             },
                                            {"connections": [{"isIPAutoGenerated": "True",
                                                              "networkUri": "ETH:mgmt",
                                                              "purpose": "Management"
                                                              },
                                                             {"isIPAutoGenerated": "True",
                                                              "networkUri": "ETH:iSCSI",
                                                              "purpose": "ISCSI"
                                                              }
                                                             ],
                                             "logicalDisks": [{"ilo_ipAddress": "10.10.1.33",
                                                               "UserName": "Administrator",
                                                               "Password": "Hellfire!234",
                                                               "diskType": "HDD"
                                                               }
                                                              ],
                                             "name": "10-10-1-33-VSA-1",
                                             "hostingHypervisorHostProfileUri": "Auto"
                                             }
                                            ],
                            "CpuCount": "None",
                            "SystemVersion": 13.5,
                            "MemoryAllocation": "None",
                            "users": [{"username": "admin",
                                       "password": "secret",
                                       "purpose": "Administrator"
                                       }
                                      ],
                            "Locale": "en-US",
                            "SystemType": "StoreVirtualVsaCluster",
                            "SoftwareSpecificAttributes": {"svmc": {"userName": "Admin",
                                                                    "password": "admin",
                                                                    "ipAddress": "10.10.4.61"
                                                                    },
                                                           "vips": [{"isIPAutoGenerated": True,
                                                                     "subnetMask": "null",
                                                                     "networkUri": "ETH:iSCSI",
                                                                     "ipAddress": "null"
                                                                     }
                                                                    ],
                                                           "quorum": {"path": "172.16.0.61:/var/nfs/vsaquorumdir",
                                                                      "type": "Witness",
                                                                      "ipAddress": "null",
                                                                      "userName": "user",
                                                                      "password": "password"
                                                                      # ,"userName": "",
                                                                      # "ipAddress": "null",
                                                                      # "password": "",
                                                                      # "type": "None",
                                                                      # "path": "null"
                                                                      },
                                                           "imageUri": "http://10.10.0.130/OVST_OV/OVST_VSA/VSA_Latest/VSA.ovf"
                                                           },
                            "hostingHypervisorClusterProfileUri": "hellfirecluster123",
                            "isCpuAndMemoryAutoManaged": "True"
                            }
                           ]

################################################

infrastructure_vms = [{"type": "InfrastructureVm",
                       "uri": None,
                       "name": "vm-1",
                       "description": "Testing vm creation.",
                       "imageUrl": "http://10.10.0.130/sw/centos.iso",
                       "imageParameters": {},
                       "memoryMB": 3044,
                       "numCPUs": 1,
                       "startupPriority": None,
                       "infrastructureType": "VSA",
                       "ownerCallbackEndpoint": "owner service endpoint",
                       "affinity": "Hypervisor",
                       "hypervisorProfileUri": "/rest/hypervisor-host-profiles/{id}",
                       "networks": {"VM Network": "ETH:mgmt"
                                    },
                       "disks": [{"id": None,
                                   "backingDiskId": "{datastore-name}",
                                   "diskType": "Virtual",
                                   "provisionType": "Thin",
                                   "capacityKB": 30720,
                                   "bootable": "true",
                                   "virtualDiskFilePath": None,
                                   "controllerBusType": None,
                                   "controllerBusNumber": None,
                                   "controllerPortNumber": None
                                  }
                                 ]
                       }
                      ]

# #####################################################
ilo_ips = [{'ilo_ip': '10.10.1.9', 'username': 'Administrator', 'password': 'Hellfire!234', 'device': 'cdrom', 'image_url': 'http://10.10.0.130/OVST_OV/OVST_ESXi_IMAGES/VMware_ESXi_6.0_U1_V_dhcp.iso'}, {'ilo_ip': '10.10.1.33', 'username': 'Administrator', 'password': 'Hellfire!234', 'device': 'cdrom', 'image_url': 'http://10.10.0.130/OVST_OV/OVST_ESXi_IMAGES/VMware_ESXi_6.0_U1_V_dhcp.iso'}, {'ilo_ip': '10.10.1.59', 'username': 'Administrator', 'password': 'Hellfire!234', 'device': 'cdrom', 'image_url': 'http://10.10.0.130/OVST_OV/OVST_ESXi_IMAGES/VMware_ESXi_6.0_U1_V_dhcp.iso'}]

ilo_ips_to_add = [{'ilo_ip': '10.10.1.59', 'username': 'Administrator', 'password': 'Hellfire!234', 'device': 'cdrom', 'image_url': 'http://10.10.0.130/OVST_OV/OVST_ESXi_IMAGES/VMware_ESXi_6.0_U1_V_dhcp.iso'}]

Hosts = [{'host_name': '10.10.4.191', 'host_user_name': 'root', 'host_password': 'vmware6'}, {'host_name': '10.10.4.192', 'host_user_name': 'root', 'host_password': 'vmware6'}]

Hosts_to_update = [{'host_name': '10.10.4.193', 'host_user_name': 'root', 'host_password': 'vmware6'}]

storage_volumes = [{"properties": {"name": 'VOLUME_VSA1', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 966367641600, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Full",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA2', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA3', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA4', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA5', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA6', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA7', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA8', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA9', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA10', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA11', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA12', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA13', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA14', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA15', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA16', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA17', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA18', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA19', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    },
                   {"properties": {"name": 'VOLUME_VSA20', "description": "", "storagePool": 'OVST-VSA-test-1',
                                   "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                   "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                    "templateUri": "ROOT", "isPermanent": True,
                    }
                   ]

storage_volumes_1 = [{"properties": {"name": 'VOLUME_VSA21', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA22', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA23', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA24', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA25', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA26', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA27', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA28', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA29', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      },
                     {"properties": {"name": 'VOLUME_VSA30', "description": "", "storagePool": 'OVST-VSA-test-1',
                                     "size": 70368744177664, "dataProtectionLevel": "NetworkRaid10Mirror2Way", "provisioningType": "Thin",
                                     "isShareable": True, "isAdaptiveOptimizationEnabled": True},
                      "templateUri": "ROOT", "isPermanent": True,
                      }
                     ]

param = "?suppressDeviceUpdates=false"

cluster_update_add_volumes = [{'type': 'HypervisorClusterProfile', 'name': 'hellfirecluster123',
                               'shared_volume': [{'name': 'VOLUME_VSA1', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA2', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA3', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA4', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA5', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA6', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA7', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA8', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA9', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA10', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA11', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA12', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA13', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA14', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA15', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA16', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA17', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA18', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA19', 'volumeFileSystemType': 'VMFS'},
                                                 {'name': 'VOLUME_VSA20', 'volumeFileSystemType': 'VMFS'}]
                               }
                              ]

cluster_update_add_volumes_1 = [{'type': 'HypervisorClusterProfile', 'name': 'hellfirecluster123',
                                 'shared_volume': [{'name': 'VOLUME_VSA21', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA22', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA23', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA24', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA25', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA26', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA27', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA28', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA29', 'volumeFileSystemType': 'VMFS'},
                                                   {'name': 'VOLUME_VSA30', 'volumeFileSystemType': 'VMFS'}]
                                 }
                                ]

cluster_update_delete_volumes = [{'type': 'HypervisorClusterProfile', 'name': 'hellfirecluster123',
                                  'del_shared_volume': ['VOLUME_VSA1', 'VOLUME_VSA2', 'VOLUME_VSA3', 'VOLUME_VSA4', 'VOLUME_VSA5', 'VOLUME_VSA6', 'VOLUME_VSA7', 'VOLUME_VSA8', 'VOLUME_VSA9', 'VOLUME_VSA10',
                                                        'VOLUME_VSA11', 'VOLUME_VSA12', 'VOLUME_VSA13', 'VOLUME_VSA14', 'VOLUME_VSA15', 'VOLUME_VSA16', 'VOLUME_VSA17', 'VOLUME_VSA18', 'VOLUME_VSA19', 'VOLUME_VSA20']}]

cluster_update_delete_volumes_1 = [{'type': 'HypervisorClusterProfile', 'name': 'hellfirecluster123',
                                    'del_shared_volume': ['VOLUME_VSA1', 'VOLUME_VSA2', 'VOLUME_VSA3', 'VOLUME_VSA4', 'VOLUME_VSA5', 'VOLUME_VSA6', 'VOLUME_VSA7', 'VOLUME_VSA8', 'VOLUME_VSA9', 'VOLUME_VSA10',
                                                          'VOLUME_VSA11', 'VOLUME_VSA12', 'VOLUME_VSA13', 'VOLUME_VSA14', 'VOLUME_VSA15', 'VOLUME_VSA16', 'VOLUME_VSA17', 'VOLUME_VSA18', 'VOLUME_VSA19', 'VOLUME_VSA20',
                                                          'VOLUME_VSA21', 'VOLUME_VSA22', 'VOLUME_VSA23', 'VOLUME_VSA24', 'VOLUME_VSA25', 'VOLUME_VSA26', 'VOLUME_VSA27', 'VOLUME_VSA28', 'VOLUME_VSA29', 'VOLUME_VSA30']}]

host_power_update_inmaintenance = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'InMaintenance'}}]

host_power_update_exitmaintenance = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'ExitMaintenance'}}]

host_power_update_exitmaintenance_1 = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'ExitMaintenance'}}]

host_power_update_poweroff = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'Off'}}]

host_power_update_poweron = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'On'}}]

host_power_update_poweroff_1 = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'Off'}}]

host_power_update_poweron_1 = [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'On'}}]

cluster_profile_add_host = [{'type': 'HypervisorClusterProfile', 'name': 'hellfirecluster123', 'server_hardware': ['ILOSGH630W4N1']}]

cluster_profile_delete_host = [{'type': 'HypervisorClusterProfile', 'name': 'hellfirecluster123', 'HostProfileUris': ['ILOSGH630W4N1']}]

sdi_system_profiles_ilo_node_addition = [{'Name': 'OVST-VSA-test-1',
                                          'AddSystemNodes': [{"connections": [{"isIPAutoGenerated": "True",
                                                                               "networkUri": "ETH:mgmt",
                                                                               "purpose": "Management"
                                                                               },
                                                                              {"isIPAutoGenerated": "True",
                                                                               "networkUri": "ETH:iSCSI",
                                                                               "purpose": "ISCSI"
                                                                               }
                                                                              ],
                                                              "logicalDisks": [{"ilo_ipAddress": "10.10.1.59",
                                                                                "UserName": "Administrator",
                                                                                "Password": "Hellfire!234",
                                                                                "diskType": "HDD"
                                                                                }
                                                                               ],
                                                              "name": "10-10-1-59-VSA-1",
                                                              "hostingHypervisorHostProfileUri": "Auto"
                                                              }]
                                          }]

sdi_system_profiles_ilo_node_deletion = [{'Name': 'OVST-VSA-test-1', 'DeleteSystemNodes': ['10-10-1-59-VSA-1']}
                                         ]

support_dump_users = [{"errorCode": "CI", "encrypt": False, "userName": "administrator"}]

vms_to_delete = ['Hellfire_OVST_VM_1', 'Hellfire_OVST_VM_2', 'Hellfire_OVST_VM_3', 'Hellfire_OVST_VM_4', 'Hellfire_OVST_VM_5']

CHO_node_maintenance = [[{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'InMaintenance'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'ExitMaintenance'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'Off'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node3'], 'hhp_settings': {'power_state': 'On'}}],
                        [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node2'], 'hhp_settings': {'power_state': 'InMaintenance'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node2'], 'hhp_settings': {'power_state': 'ExitMaintenance'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node2'], 'hhp_settings': {'power_state': 'Off'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node2'], 'hhp_settings': {'power_state': 'On'}}],
                        [{'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node1'], 'hhp_settings': {'power_state': 'InMaintenance'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node1'], 'hhp_settings': {'power_state': 'ExitMaintenance'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node1'], 'hhp_settings': {'power_state': 'Off'}},
                        {'name': 'hellfirecluster123', 'HypervisorHostProfileNames': ['hellfirecluster123-node1'], 'hhp_settings': {'power_state': 'On'}}]]

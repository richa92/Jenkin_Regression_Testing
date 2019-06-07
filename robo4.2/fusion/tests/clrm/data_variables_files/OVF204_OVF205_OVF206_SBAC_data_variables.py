admin_credentials = {"userName": "Administrator", "password": "vsbqa*help", "authLoginDomain": "LOCAL", "loginMsgAck": None}

User1_credentials = {'userName': 'User1', 'password': 'vsbqa*help', "authLoginDomain": "LOCAL", "loginMsgAck": None}

scopes = [{"name": "Scope1",
           "description": "",
           "type": "ScopeV3",
           "addedResourceUris": [],
           "removedResourceUris": []
           },
          ]

users = [{"type": "UserAndPermissions", "userName": "User1", "fullName": "", "password": "vsbqa*help", "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Read only", "scopeUri": None}]}]

AFR = "ACTION_FORBIDDEN_BY_ROLE"
CFS = "CREATE_FORBIDDEN_ON_SCOPES"

SBAC_HM_1 = [{'username': 'dcs', 'password': 'dcs', 'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'port': '443', "displayName": "172.18.13.11", "initialScopeUris": []}]

SBAC_HM_1_Update = [{'type': 'HypervisorManagerV2', 'name': '172.18.13.11', 'username': 'dcs', 'password': 'dcs', 'port': '443', 'version': '5.1.0', 'virtualSwitchType': 'Distributed', 'multiNicVMotion': 'false', 'distributedSwitchUsage': 'GeneralNetworks', 'distributedSwitchVersion': '5.1.0', 'hypervisor_type': 'Vmware'}]

ethernet_networks = [{'smartLink': 'true', 'ethernetNetworkType': 'Untagged', 'name': 'corp', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '80', 'purpose': 'Management'},
                     {'smartLink': 'true', 'ethernetNetworkType': 'Tagged', 'name': 'icsp', 'connectionTemplateUri': None, 'privateNetwork': 'false', 'type': 'ethernet-networkV4', 'vlanId': '70', 'purpose': 'General'}]

uplink_sets = {'uplink1': {'name': 'upl_corp',
                           'ethernetNetworkType': 'Untagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['corp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.2', 'speed': 'Auto'}]
                           },
               'uplink2': {'name': 'upl_icsp',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['icsp'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]
                           }
               }

ligs = {'name': 'lig',
        'type': 'logical-interconnect-groupV4',
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [{'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                    {'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}
                                    ],
        'uplinkSets': [uplink_sets['uplink1'].copy(), uplink_sets['uplink2'].copy()],
        'internalNetworkUris': []
        }

enc_groups = {'name': 'enclgrp',
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig'},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
               ],
              }

enclosures = [{'hostname': '172.18.1.11', 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None},
              {'hostname': "172.18.1.13", 'username': 'dcs', 'password': 'dcs', 'enclosureGroupUri': 'EG:enclgrp', 'force': True, 'licensingIntent': 'OneViewNoiLO', 'firmwareBaselineUri': None}
              ]

server_profile_templates = [{'name': 'SPT1', 'type': 'ServerProfileTemplateV5', 'serverProfileDescription': '', 'serverHardwareTypeUri': 'SHT:BL460c Gen8 1', 'enclosureGroupUri': 'EG:enclgrp', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{"id": 1, "name": "icsp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:icsp'},
                                                                    {"id": 2, "name": "corp_conn", "functionType": "Ethernet", "portId": "Auto", "requestedMbps": "2500", "networkUri": 'ETH:corp'}
                                                                    ]
                                                    },
                             'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                             'bootMode': None,
                             'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             'hideUnusedFlexNics': True, 'iscsiInitiatorNameType': 'AutoGenerated',
                             'localStorage': {'sasLogicalJBODs': [], 'controllers': []}, 'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': False, 'volumeAttachments': []}}]

ipv4_subnet = [{'type': 'Subnet',
                'networkId': '15.146.152.0',
                'subnetmask': '255.255.248.0',
                'gateway': '15.146.152.1',
                'dnsServers': ['16.110.135.51',
                               '16.110.135.52'],
                'domain': 'hpe.com'},
               {'type': 'Subnet',
                'networkId': '172.18.0.0',
                'subnetmask': '255.255.248.0',
                'gateway': '172.18.0.1',
                'dnsServers': ['16.110.135.51', '16.110.135.51'],
                'domain': 'hpe.com'
                }
               ]

subnet_association = [{'network type': 'ethernet-networkV4', 'name': 'corp', 'subnetUri': '15.146.152.0'},
                      {'network type': 'ethernet-networkV4', 'name': 'icsp', 'subnetUri': '172.18.0.0'}
                      ]

deployment_managers = [{'username': 'dcs', 'password': 'dcs', 'type': 'DeploymentManager', 'name': '172.18.9.1', 'port': '443'}]

SBAC_Cluster_1 = [{'type': 'HypervisorClusterProfileV3', 'name': 'SBAC_Cluster_1', 'path': 'DC1', 'vcenter': '172.18.13.11', 'deployment_manager_type': 'ICSP',
                   'profile_name': 'SPT1', 'hypervisor_type': 'Vmware', 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                   'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}}
                  ]

SBAC_Cluster_1_Update = [{'type': 'HypervisorClusterProfileV3', 'name': 'SBAC_Cluster_1', 'path': 'DC1', 'vcenter': '172.18.13.11',
                          'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'false'}}
                         ]

SBAC_HHP_Cluster = [{'type': 'HypervisorClusterProfileV3', 'name': 'SBAC_HHP_Cluster_1', 'path': 'DC1', 'vcenter': '172.18.13.11', 'deployment_manager_type': 'ICSP',
                     'profile_name': 'SPT1', 'hypervisor_type': 'Vmware', 'deployment_uri': '/rest/os-deployment-build-plans/800001', 'server_password': 'iso*help',
                     'cluster_settings': {'cluster_settings_type': 'Vmware', 'virtual_switch_type': 'Standard', 'multi_nic_vmotion': 'true'}, 'server_hardware': ['Encl1, bay 8', 'Encl1, bay 11']}
                    ]

SBAC_HHP_Cluster_Update = [{'type': 'HypervisorClusterProfileV3', 'name': 'SBAC_HHP_Cluster_1', 'hhp_settings': {'redeploy': 'true'}}
                           ]

add_resource_to_scope = ['HM:172.18.13.11']

delete_resource_from_scope = []


admin_credentials = {'userName': 'Administrator', 'password': 'admin123'}

ilo_credentials = {'userName': 'Administrator', 'password': 'admin123'}

osdps = {'name': 'dp1With1Nic_StaticAndDhcpNic'}

# Add storage nws
networks = {'iscsi': 'i3s_deploy_nw', 'mgmt': 'mgmt_nw', 'fc_nw': 'fc_nw1', 'vsa_nw': 'iscsi_nw'}

egs = {'enclosureGroupUri': 'EG-3enc'}

servers = {'serverHardwareUri': 'SGH736WS9C, bay 1', 'serverHardwareTypeUri': 'SY 480 Gen9 2'}

storage_volumes = [{"properties": {"name": "fc_svol1", "description": "", "storagePool": "QA_test_R5", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "QA_test_R5"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "fc_pvol1", "description": "", "storagePool": "QA_test_R5", "size": 1000000000, "provisioningType": "Thin", "isShareable": False, "snapshotPool": "QA_test_R5"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "iscsi_svol1", "description": "", "storagePool": "CLRM-QA-VSA", "size": 11073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'ROOT', "isPermanent": True},
                   {"properties": {"name": "iscsi_pvol1", "description": "", "storagePool": "CLRM-QA-VSA", "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": False, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'ROOT', "isPermanent": True},
                   {"properties": {"name": "fc_svol2", "description": "", "storagePool": "QA_test_R5", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "QA_test_R5"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "fc_pvol2", "description": "", "storagePool": "QA_test_R5", "size": 11000000000, "provisioningType": "Thin", "isShareable": False, "snapshotPool": "QA_test_R5"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "iscsi_svol2", "description": "", "storagePool": "CLRM-QA-VSA", "size": 11073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'ROOT', "isPermanent": True},
                   {"properties": {"name": "iscsi_pvol2", "description": "", "storagePool": "CLRM-QA-VSA", "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": False, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'ROOT', "isPermanent": True},
                   {"properties": {"name": "fc_svol3", "description": "", "storagePool": "QA_test_R5", "size": 11000000000, "provisioningType": "Thin", "isShareable": True, "snapshotPool": "QA_test_R5"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "fc_pvol3", "description": "", "storagePool": "QA_test_R5", "size": 11000000000, "provisioningType": "Thin", "isShareable": False, "snapshotPool": "QA_test_R5"}, "templateUri": "ROOT", "isPermanent": True},
                   {"properties": {"name": "iscsi_svol3", "description": "", "storagePool": "CLRM-QA-VSA", "size": 11073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": True, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'ROOT', "isPermanent": True},
                   {"properties": {"name": "iscsi_pvol3", "description": "", "storagePool": "CLRM-QA-VSA", "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": False, "isAdaptiveOptimizationEnabled": True}, "templateUri": 'ROOT', "isPermanent": True},
                   ]


storage_volumes1 = [{"properties": {"name": "fc_pvol23"}}, {"properties": {"name": "iscsi_pvol23"}}]


fc_volumes = [{'id': 1,
               "volumeStorageSystemUri": 'SYSS:test',
               'lunType': 'Auto',
               "volumeUri": "vol:fc_svol1",
               'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
               },
              {'id': 2,
               "volumeStorageSystemUri": 'SYSS:test',
               'lunType': 'Auto',
               "volumeUri": "vol:fc_pvol1",
               'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
               }]

fc_volumes_add1 = [{'id': 3,
                    "volumeStorageSystemUri": 'SYSS:test',
                    'lunType': 'Auto',
                    "volumeUri": "vol:fc_svol2",
                    'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                    },
                   {'id': 4,
                    "volumeStorageSystemUri": 'SYSS:test',
                    'lunType': 'Auto',
                    "volumeUri": "vol:fc_pvol2",
                    'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                    }]

fc_volumes_add2 = [{'id': 5,
                    "volumeStorageSystemUri": 'SYSS:test',
                    'lunType': 'Auto',
                    "volumeUri": "vol:fc_svol3",
                    'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                    },
                   {'id': 6,
                    "volumeStorageSystemUri": 'SYSS:test',
                    'lunType': 'Auto',
                    "volumeUri": "vol:fc_pvol3",
                    'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                    }]


fc_volumes_spt = [{'id': 1,
                   "volumeStorageSystemUri": 'SYSS:test',
                   'lunType': 'Auto',
                   "volumeUri": "vol:fc_svol1",
                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                   },
                  {'id': 2,
                   "volumeStorageSystemUri": 'SYSS:test',
                   'lunType': 'Auto',
                   "volumeUri": None,
                   'volume': {"properties": {"name": "fc_pvol21", "description": "", "storagePool": "storagePool:QA_test_R5", "size": 1000000000, "provisioningType": "Thin", "isShareable": False}, "templateUri": None, "isPermanent": True},
                   'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                   }]

fc_volumes_spt_add1 = [{'id': 3,
                        "volumeStorageSystemUri": 'SYSS:test',
                        'lunType': 'Auto',
                        "volumeUri": "vol:fc_svol2",
                        'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        },
                       {'id': 4,
                        "volumeStorageSystemUri": 'SYSS:test',
                        'lunType': 'Auto',
                        "volumeUri": None,
                        'volume': {"properties": {"name": "fc_pvol22", "description": "", "storagePool": "storagePool:QA_test_R5", "size": 1000000000, "provisioningType": "Thin", "isShareable": False}, "templateUri": None, "isPermanent": True},
                        'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        }]

fc_volumes_spt_add2 = [{'id': 5,
                        "volumeStorageSystemUri": 'SYSS:test',
                        'lunType': 'Auto',
                        "volumeUri": "vol:fc_svol3",
                        'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        },
                       {'id': 6,
                        "volumeStorageSystemUri": 'SYSS:test',
                        'lunType': 'Auto',
                        "volumeUri": None,
                        'volume': {"properties": {"name": "fc_pvol23", "description": "", "storagePool": "storagePool:QA_test_R5", "size": 1000000000, "provisioningType": "Thin", "isShareable": False}, "templateUri": None, "isPermanent": True},
                        'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                        }]

sanStorage_volumes = {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                      'volumeAttachments': fc_volumes}

sanStorage_volumes_add1 = {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                           'volumeAttachments': fc_volumes + fc_volumes_add1}

sanStorage_volumes_add2 = {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                           'volumeAttachments': fc_volumes_add2}

sanStorage_volumes_spt = {'complianceControl': 'Checked', 'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                          'volumeAttachments': fc_volumes_spt}

sanStorage_volumes_add1_spt = {'complianceControl': 'Checked', 'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': fc_volumes_spt_add1}

sanStorage_volumes_add2_spt = {'complianceControl': 'Checked', 'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': fc_volumes_spt_add2}

iscsi_volumes = [{'id': 1,
                  "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                  'lunType': 'Auto',
                  "volumeUri": "vol:iscsi_svol1",
                  'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                  },
                 {'id': 2,
                  "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                  'lunType': 'Auto',
                  "volumeUri": "vol:iscsi_pvol1",
                  'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                  }]

iscsi_volumes_add1 = [{'id': 3,
                       "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                       'lunType': 'Auto',
                       "volumeUri": "vol:iscsi_svol2",
                       'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                       },
                      {'id': 4,
                       "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                       'lunType': 'Auto',
                       "volumeUri": "vol:iscsi_pvol2",
                       'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                       }]

iscsi_volumes_add2 = [{'id': 5,
                       "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                       'lunType': 'Auto',
                       "volumeUri": "vol:iscsi_svol3",
                       'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                       },
                      {'id': 6,
                       "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                       'lunType': 'Auto',
                       "volumeUri": "vol:iscsi_pvol3",
                       'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                       }]


iscsi_volumes_spt = [{'id': 1,
                      "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                      'lunType': 'Auto',
                      "volumeUri": "vol:iscsi_svol1",
                      'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                      },
                     {'id': 2,
                      "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                      'lunType': 'Auto',
                                 "volumeUri": None,
                      'volume': {"properties": {"name": "iscsi_pvol21", "description": "", "storagePool": "storagePool:CLRM-QA-VSA", "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": False, "isAdaptiveOptimizationEnabled": True}, "templateUri": None, "isPermanent": True},
                      'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                      }]

iscsi_volumes_spt_add1 = [{'id': 3,
                           "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                           'lunType': 'Auto',
                           "volumeUri": "vol:iscsi_svol2",
                           'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                           },
                          {'id': 4,
                           "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                           'lunType': 'Auto',
                           "volumeUri": None,
                           'volume': {"properties": {"name": "iscsi_pvol22", "description": "", "storagePool": "storagePool:CLRM-QA-VSA", "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": False, "isAdaptiveOptimizationEnabled": True}, "templateUri": None, "isPermanent": True},
                           'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                           }]

iscsi_volumes_spt_add2 = [{'id': 5,
                           "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                           'lunType': 'Auto',
                           "volumeUri": "vol:iscsi_svol3",
                           'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                           },
                          {'id': 6,
                           "volumeStorageSystemUri": 'SYSS:CLRM-QA-VSA',
                           'lunType': 'Auto',
                           "volumeUri": None,
                           'volume': {"properties": {"name": "iscsi_pvol23", "description": "", "storagePool": "storagePool:CLRM-QA-VSA", "size": 1073741824, "dataProtectionLevel": "NetworkRaid5SingleParity", "provisioningType": "Thin", "isShareable": False, "isAdaptiveOptimizationEnabled": True}, "templateUri": None, "isPermanent": True},
                           'storagePaths': [{'isEnabled': True, 'connectionId': 4, 'targetSelector': 'Auto', 'targets': []}]
                           }]

iscsi_volumes_settings = {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                          'volumeAttachments': iscsi_volumes,
                          'sanSystemCredentials': [{'storageSystemUri': 'SSYS:CLRM-QA-VSA', 'chapLevel': 'None', 'chapSource': 'AutoGenerated'}]}

iscsi_volumes_settings_add1 = {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': iscsi_volumes_add1,
                               'sanSystemCredentials': [{'storageSystemUri': 'SSYS:CLRM-QA-VSA', 'chapLevel': 'None', 'chapSource': 'AutoGenerated'}]}

iscsi_volumes_settings_add2 = {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                               'volumeAttachments': iscsi_volumes_add2,
                               'sanSystemCredentials': [{'storageSystemUri': 'SSYS:CLRM-QA-VSA', 'chapLevel': 'None', 'chapSource': 'AutoGenerated'}]}

iscsi_volumes_settings_spt = {'complianceControl': 'Checked', 'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                              'volumeAttachments': iscsi_volumes_spt,
                              'sanSystemCredentials': [{'storageSystemUri': 'SSYS:CLRM-QA-VSA', 'chapLevel': 'None'}]}

iscsi_volumes_settings_add1_spt = {'complianceControl': 'Checked', 'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                   'volumeAttachments': iscsi_volumes_spt_add1,
                                   'sanSystemCredentials': [{'storageSystemUri': 'SSYS:CLRM-QA-VSA', 'chapLevel': 'None'}]}

iscsi_volumes_settings_add2_spt = {'complianceControl': 'Checked', 'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                   'volumeAttachments': iscsi_volumes_spt_add2,
                                   'sanSystemCredentials': [{'storageSystemUri': 'SSYS:CLRM-QA-VSA', 'chapLevel': 'None'}]}


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
                          "bootVolumeSource": "UserDefined"}},
                {"id": 3, "name": "Management Network A",
                 "functionType": "Ethernet",
                 "networkUri": "ETH:" + networks["mgmt"],
                 "portId": "Auto", "requestedMbps": "2500",
                 "lagName": None, "isolatedTrunk": False,
                 "requestedVFs": "0", "ipv4": {},
                 "boot": {"priority": "NotBootable", "iscsi": {}}}
                ]


vsa_conns = [{"id": 4, "name": "Storage Network A",
              "functionType": "Ethernet",
              "networkUri": "ETH:" + networks['vsa_nw'],
              "portId": "Auto", "requestedMbps": "2500",
              "lagName": None, "isolatedTrunk": False,
              "requestedVFs": "0", "ipv4": {},
              "boot": {"priority": "NotBootable", "iscsi": {}}}]

fc_conns = [{"id": 4, "name": "Storage Network B",
             "functionType": "FibreChannel",
             "networkUri": "FC:" + networks["fc_nw"],
             "portId": "Auto", "requestedMbps": "2500",
             "lagName": None, "ipv4": {},
             "boot": {"priority": "NotBootable", "iscsi": {}}}]


sp_with_fc_conns = {"reapplyState": "NotApplying",
                    "connections": deploy_conns + fc_conns}

spt_with_fc_conns = {"manageConnections": True,
                     "connections": deploy_conns + fc_conns}

sp_with_vsa_conns = {"reapplyState": "NotApplying",
                     "connections": deploy_conns + vsa_conns}

spt_with_vsa_conns = {"manageConnections": True,
                      "connections": deploy_conns + vsa_conns}

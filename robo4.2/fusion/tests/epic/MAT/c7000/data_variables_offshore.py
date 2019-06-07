from DynamicData import DynamicData

DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

firmware = {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None}
# firmware = {'manageFirmware': True, 'forceInstallFirmware': True, 'firmwareInstallType': 'FirmwareOnlyOfflineMode'}

licenses = [{'key': 'ACLA C9MA H9P9 CHUZ V7B5 HWWB Y9JL KMPL 5R2H 6DRM DXAU 2CSM GHTG L762 BCV6 EEFY KJVT D5KM EFVW DT5J 69UM NY2G 9K2P 3E22 MKQU 3UFZ TZZX AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863919 HPOV-NFR1 HP_OneView_16_Seat_NFR H592ADTYDJJD"_3PXQT-HWSHJ-7RBW9-ZW3WG-XC2W2'},
            {'key': 'YCLE B9MA H9PY GHU3 U7B5 HWW5 Y9JL KMPL NRSF 4ERM DXAU 2CSM GHTG L762 DK5Y HHF9 KJVT D5KM EFVW DT5J 89MK PZ2G 9K2P 3E22 MKYU 3UFZ TZZ7 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424863952 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR YHUAADTYEC5H"'},
            {'key': 'QCLA A9MA H9PA KHW3 V7B5 HWWB Y9JL KMPL BRKD 8FBM DXAU 2CSM GHTG L762 XKJ3 VBF4 KJVT D5KM EFRW DS5R A9E9 52KG 9K2P 3E22 UKYU 3UFZ TZZ7 MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863966 HPOV-NFR1 HP_OneView_16_Seat_NFR 7EA7ADTYED49"_3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
            {'key': 'YCLC C9MA H9P9 8HW3 U7B5 HWW5 Y9JL KMPL LRGB 7ABQ DXAU 2CSM GHTG L762 QGFZ EEZM KJVT D5KM EFRW DS5R M94M N5KG 9K2P 3E22 AKYU LUV5 TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424864041 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR HY95ADTYTCHT"'}]

spp_name = 'SPP2018020_2018_0116_67'
FirmwareVersion = '2018.02.0'

updated_spp_name = DD.spp_name_withunderscore(spp_name)

spp_local_dir = 'D:/SPP/'

users_name = [{'name': 'appliance', 'role': 'Infrastructure administrator'},
              {'name': 'network', 'role': 'Network administrator'},
              {'name': 'server', 'role': 'Server administrator'},
              {'name': 'storage', 'role': 'Storage administrator'},
              {'name': 'readonly', 'role': 'Read only'}]

networkadmin_credentials = {'userName': 'network', 'password': 'Cosmos123'}

storageadmin_credentials = {'userName': 'storage', 'password': 'Cosmos123'}

serveradmin_credentials = {'userName': 'server', 'password': 'Cosmos123'}

sans = [{'Type': 'Brocade Network Advisor',
         'Host': '172.25.9.29',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'password', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '172.25.9.234',
         'SnmpPort': 161,
         'SnmpUserName': 'fcoeusr1',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authpass',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privpass'}]

ethernet_networks = [{'name': 'Eth_1071', 'type': 'ethernet-networkV4', 'vlanId': 1071, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'Eth_1072', 'type': 'ethernet-networkV4', 'vlanId': 1072, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'Eth_1073', 'type': 'ethernet-networkV4', 'vlanId': 1073, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'Eth_1074', 'type': 'ethernet-networkV4', 'vlanId': 1074, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False}]

fc_networks = [{'name': 'FC1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:NFV-BNA-SW1', 'fabricType': 'FabricAttach'},
               {'name': 'FC2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:NFV-BNA-SW2', 'fabricType': 'FabricAttach'},]

fcoe_networks = [{'name': 'FCOE1', 'type': 'fcoe-networkV4', 'vlanId': 1095, 'managedSanUri': 'FCSan:VSAN1095'},
                 {'name': 'FCOE2', 'type': 'fcoe-networkV4', 'vlanId': 1100, 'managedSanUri': 'FCSan:VSAN1100'}]

network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['Eth_1071', 'Eth_1072', 'Eth_1073', 'Eth_1074'], 'nativeNetworkUri': None}]

uplink_sets = {'Fc2': {'name': 'Fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                'networkUris': ['FC2'], 'mode': 'Auto',
                                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
               'Fc1': {'name': 'Fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                 'networkUris': ['FC1'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
               'ETH': {'name': 'ETH', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                 'networkUris': ['Eth_1071', 'Eth_1072', 'Eth_1073', 'Eth_1074'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'},
                                                            {'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
               'FCOE1': {'name': 'FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                  'networkUris': ['FCOE1'], 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'port': 'X2', 'speed': 'Auto'}]},
               'FCOE2': {'name': 'FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                  'networkUris': ['FCOE2'], 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '4', 'port': 'X2', 'speed': 'Auto'}]},
               }

ligs = [{'name': 'Lig1', 'type': 'logical-interconnect-groupV5', 'enclosureType': 'C7000', 'ethernetSettings': None, 'description': None,
         'uplinkSets': [uplink_sets['Fc2'].copy(),
                        uplink_sets['Fc1'].copy(),
                        uplink_sets['ETH'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}],
         'internalNetworkUris': [],
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}},
        {'name': 'Lig2', 'type': 'logical-interconnect-groupV5', 'enclosureType': 'C7000', 'ethernetSettings': None, 'description': None,
         'uplinkSets': [uplink_sets['FCOE1'].copy(),
                        uplink_sets['FCOE2'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}],
         'internalNetworkUris': [],
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}}]

expected_lig = [{"name": "Lig1", "type": "logical-interconnect-groupV5", "enclosureType": "C7000",
                 "uplinkSets": [{"name": "Fc2", "networkUris": ["FC:FC2"]},
                                {"name": "Fc1", "networkUris": ["FC:FC1"]},
                                {"name": "ETH", "networkUris": ["ETH:Eth_1071","ETH:Eth_1072","ETH:Eth_1073","ETH:Eth_1074"]}],
                 "internalNetworkUris": []},
                {"name": "Lig2", "type": "logical-interconnect-groupV5", "enclosureType": "C7000",
                 "uplinkSets": [{"name": "FCOE1", "networkUris": ["FCOE:FCOE1"]},
                                {"name": "FCOE2", "networkUris": ["FCOE:FCOE2"]}],
                 "internalNetworkUris": []}]

enc_groups = [{'name': 'EGR71', 'enclosureCount': 1,
               'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:Lig1'},
                                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:Lig1'},
                                           {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Lig2'},
                                           {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:Lig2'}],
               'ipAddressingMode': None, 'ipRangeUris': [], 'powerMode': None}]

storage_systems = [{'name': 'COSMOS-P7400-9.110', 'family': 'StoreServ', "hostname": "172.25.9.110",
                    "credentials": {"username": "cosmos", "password": "Nextgen9"}, "serialNumber": "1644257",
                    'deviceSpecificAttributes': {'managedDomain': 'COSMOS', 'managedPools': []}},
                    {'name': 'NFV-8200-9.140', 'family': 'StoreServ', "hostname": "172.25.9.140",
                    "credentials": {"username": "cosmos", "password": "Nextgen9"}, "serialNumber": "MXN6102BVY",
                    'deviceSpecificAttributes': {'managedDomain': 'NFV-Cosmos', 'managedPools': []}}]

storage_pools = [{"storageSystemUri": 'COSMOS-P7400-9.110', "name": 'cosmos-cpg', "isManaged": True},
                 {"storageSystemUri": 'NFV-8200-9.140', "name": 'RAID0', "isManaged": True}]

existing_storage_volumes = [{"storageSystemUri": "NFV-8200-9.140", "name": "Me71Bay2Win2012"},
                            {"storageSystemUri": "NFV-8200-9.140", "name": "ME71BAY4Win2016"},
                            {"storageSystemUri": "COSMOS-P7400-9.110", "name": "ME71Bay3Sles12sp2"},
                            {"storageSystemUri": "COSMOS-P7400-9.110", "name": "ME71Bay6Esxi6.5"}]

encl = [{"enclosureGroupUri": "EG:EGR71",
         "name": "SGH747C0LP",
         "hostname": "172.25.71.11",
         "username": "Admin",
         "password": "Insight7",
         "licensingIntent": "OneView",
         "updateFirmwareOn": "EnclosureOnly",
         "forceInstallFirmware": firmware['forceInstallFirmware'],
         "force": True}]

dl_servers = [{"name": "ILOUSE449FPLH", "hostname": "172.25.8.20", "username": "Admin", "password": "admin123", "force": True,
               "licensingIntent": "OneViewNoiLO", "configurationState": "Managed"}]

dlserver_profiles = [{'serverHardwareUri': 'SH:ILOUSE449FPLH', 'name': 'DL_380_Gen9_Win2016',
                      'connectionSettings': {'connections': []},
                      'boot': {'manageBoot': False, 'order': []},
                      'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                      'localStorage': {'sasLogicalJBODs': [],
                                       'controllers': [{'logicalDrives': [],
                                                        'deviceSlot': 'Embedded',
                                                        'mode': 'RAID',
                                                        'initialize': False,
                                                        'importConfiguration': True}]},
                      'bios': {'manageBios': False, 'overriddenSettings': []}}]

server_profile_data = [{'name': 'Me71Bay1Rhel7.4', 'serverHardwareUri': 'SH:SGH747C0LP, bay 1', 'enclosureGroupUri': 'EGR71',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1071', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1072', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Secondary'}},
                                                               ]},
                        "sanStorage": {"manageSanStorage": False, "volumeAttachments": [], "sanSystemCredentials": [], "reapplyState": "NotApplying"},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {"sasLogicalJBODs": [],"controllers": [{"deviceSlot": "Embedded", "mode": "HBA","initialize": False,"importConfiguration": False,"logicalDrives": []}],"reapplyState": "NotApplying"
                       }},

                       {'name': 'Me71Bay2Win2012', 'serverHardwareUri': 'SH:SGH747C0LP, bay 2', 'enclosureGroupUri': 'EGR71',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1073', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1074', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Secondary'}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC1', 'functionType': 'FibreChannel',
                                                                'boot': {"priority": "Primary", "bootVolumeSource": "ManagedVolume"}},
                                                               {'id': 4, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC2', 'functionType': 'FibreChannel',
                                                                'boot': {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}},
                                                               ]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:Me71Bay2Win2012',
                                                              'lunType': 'Manual', 'lun': 1, 'isBootVolume': True,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []},
                        "localStorage": {"sasLogicalJBODs": [], "controllers": [], "reapplyState": "NotApplying"}},

                       {'name': 'ME71BAY3Sles12sp3', 'serverHardwareUri': 'SH:SGH747C0LP, bay 3', 'enclosureGroupUri': 'EGR71',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1072', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1073', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Secondary'}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE1', 'functionType': 'FibreChannel', "macType": "UserDefined", "wwpnType": "UserDefined", "mac": "CA:41:4E:F0:00:08",
                                                                "wwnn": "10:00:36:b7:16:30:00:05", "wwpn": "10:00:36:b7:16:30:00:04",
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE2', 'functionType': 'FibreChannel', "macType": "UserDefined", "wwpnType": "UserDefined", "mac": "CA:41:4E:F0:00:09",
                                                                "wwnn": "10:00:36:b7:16:30:00:07", "wwpn": "10:00:36:b7:16:30:00:06",
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               ]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:ME71Bay3Sles12sp2',
                                                              'lunType': 'Manual', 'lun': 1, 'isBootVolume': True,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {"sasLogicalJBODs": [], "controllers": [], "reapplyState": "NotApplying"}},

                       {'name': 'ME71BAY4Win2016', 'serverHardwareUri': 'SH:SGH747C0LP, bay 4', 'enclosureGroupUri': 'EGR71',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1072', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1074', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Secondary'}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC1', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 4, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC2', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               ]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:ME71BAY4Win2016', 'isBootVolume': True,
                                                              'lunType': 'Manual', 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {"sasLogicalJBODs": [], "controllers": [], "reapplyState": "NotApplying"}},

                       {'name': 'Me71BAY5Esxi6.0', 'serverHardwareUri': 'SH:SGH747C0LP, bay 5', 'enclosureGroupUri': 'EGR71',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1071', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1072', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Secondary'}},
                                                               ]},
                        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                        'bios': {'manageBios': False, 'overriddenSettings': [], "reapplyState": "NotApplying"},
                        'localStorage': {'sasLogicalJBODs': [],
                                         'controllers': [{'logicalDrives': [],
                                                          'deviceSlot': 'Embedded',
                                                          'mode': 'RAID',
                                                          'initialize': False,
                                                          'importConfiguration': True}]}},

                       {'name': 'Me71BAY6Esxi6.5', 'serverHardwareUri': 'SH:SGH747C0LP, bay 6', 'enclosureGroupUri': 'EGR71',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1071', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1073', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Secondary'}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE1', 'functionType': 'FibreChannel', "macType": "UserDefined", "wwpnType": "UserDefined", "mac": "CA:41:4E:F0:00:12",
                                                                "wwnn": "10:00:36:b7:16:30:00:0d", "wwpn": "10:00:36:b7:16:30:00:0C",
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE2', 'functionType': 'FibreChannel', "macType": "UserDefined", "wwpnType": "UserDefined", "mac": "CA:41:4E:F0:00:13",
                                                                "wwnn": "10:00:36:b7:16:30:00:0e", "wwpn": "10:00:36:b7:16:30:00:0f",
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}
                                                               ]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:ME71Bay6Esxi6.5', 'isBootVolume': True,
                                                              'lunType': 'Manual', 'lun': 0,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3},
                                                                               {'isEnabled': True, 'connectionId': 4}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {"sasLogicalJBODs": [], "controllers": [], "reapplyState": "NotApplying"}},
                       ]


# SPP data
spp_local_path = DD.get_spp_path(spp_name, spp_local_dir)
expected_spp = DD.expected_spp_data(spp_name)

# Users data
users = DD.users_data(users_name)
expected_users = DD.expected_users_data(users_name)

# Enclosure Group data
expected_encgroups = DD.make_expected_enc_group_data(enc_groups)

# SAN managers data
san_managers = DD.create_san_manager_data(sans)
expected_san_managers = DD.get_expected_san_manager_data(sans)

# Ethernet Networks data
expected_ethernet_networks = DD.get_expected_ethernet_data(ethernet_networks)

# Fiber channel Networks data
expected_fc_networks = DD.get_expected_fcnet_data(fc_networks)

# FCoE Networks data
expected_fcoe_networks = DD.get_expected_fcoenet_data(fcoe_networks)

# Network Set data
expected_network_sets = DD.get_expected_network_set_data(network_sets)

# Storage Systems data
expected_storage_systems = DD.expected_storage_system(storage_systems)

# Storage Volumes data
storage_volumes_add = DD.existing_storage_volumes(existing_storage_volumes)
expected_existing_storage_volumes = DD.expected_storage_volumes(existing_storage_volumes)

# Enclosure Data
enclosures = DD.make_enclosure_data(encl, updated_spp_name)
expected_enclosures = DD.make_expected_enclousre_data(encl, updated_spp_name)

# DL Server Data
expected_dl_servers = DD.make_expected_dlserver_data(dl_servers)

# DL Server Profile Data
dl_server_profiles = DD.make_dlserver_profile_data(dlserver_profiles, updated_spp_name, firmware)
expected_dl_server_profiles = DD.make_expected_dlserver_profile_data(dlserver_profiles, updated_spp_name, firmware)

# Server Profile data
server_profiles = DD.make_server_profile_data(server_profile_data, updated_spp_name, firmware)
expected_server_profiles = DD.make_expected_server_profile_data(server_profile_data, updated_spp_name, firmware)

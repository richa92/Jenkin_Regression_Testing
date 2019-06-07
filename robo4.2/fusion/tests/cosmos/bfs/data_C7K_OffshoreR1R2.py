"""
    BFS datafile for offshore C7K environment
"""

from DynamicData import DynamicData
import copy

DD = DynamicData()

spp = "/rest/firmware-drivers/SPP2019030_2019_0206_85"

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

ilo_credentials = {'username': 'Admin', 'password': 'admin123'}

dhcpservers = [{'ip': '172.25.64.60', 'vlanid': '1064', 'scope': '172.25.64.0', 'username': 'Administrator', 'password': 'Cosmos123'}, ]

firmware = {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareBaselineUri': None}

update_firmware = {'manageFirmware': True, 'forceInstallFirmware': True, 'firmwareInstallType': 'FirmwareAndOSDrivers', 'firmwareBaselineUri': spp}

unassign = True
critical = 'Critical'
ok = 'OK'

timeandlocale = {'localeDisplayName': 'English (United States)', 'locale': 'en_US.UTF-8', 'dateTime': '2019-01-23T05:59:25.238Z', 'ntpServers': [], 'timezone': 'UTC', 'type': 'TimeAndLocale'}

appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "eth0",
        "macAddress": "00:50:56:a1:d1:82",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.255.0",
        "ipv4Gateway": "172.25.64.1",
        "ipv4NameServers": [],
        "app1Ipv4Addr": "172.25.64.197",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ci-005056a1d182",
        "confOneNode": True,
        "domainName": "",
        "aliasDisabled": False
    }
    ]}

sans = [{'Type': 'Brocade Network Advisor',
         'Host': '172.25.9.89',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'password', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '172.25.9.24',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'},
        {'Type': 'HPE',
         'Host': '172.25.9.26',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'}]

licenses = [{'key': 'ABAG AQEA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 DMF5 GRRM KJVT D5KM EFVW TSNJ XFU9 4ZSK E828 LFK6 FKA6 DU5N TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8UW BGB5 C324 SFUZ CMSB VNTJ ESB7 KVGR UNPC H4N5 NGHL 97D4 "EG3188881 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic ED4UATGCG2A9"_3JMZZ-RB9CN-DQD7H-CPB8P-M7WW2'},
            {'key': 'QCLG C9MA H9PQ 8HUZ U7B5 HWW5 Y9JL KMPL KRWA NBZY DXAU 2CSM GHTG L762 DNV7 GQFQ KJVT D5KM EFVW DT5J LFM8 76S8 C8SN YGSG Y8JC QUXV XZKH ABB4 NV2C LHXU VLXL HFMP J8TG 2VEB LK4U R6UF S7QS TRRL GX96 CMH4 6MPA M8LC KZU7 WE4X YN9X CDNB NT35 GH9J JGTJ QCV6 3EJF N975 "OV_NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR EY67ATGDTH6C"'}]

ethernet_networks = [{'name': 'Eth1_1064', 'type': 'ethernet-networkV4', 'vlanId': 1064, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'Eth2_1064', 'type': 'ethernet-networkV4', 'vlanId': 1064, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     ]

fc_networks = [{'name': 'fc1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:Switch-71-10:00:50:eb:1a:03:a5:60', 'fabricType': 'FabricAttach'},
               {'name': 'fc2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:Switch-71-10:00:50:eb:1a:03:a5:61', 'fabricType': 'FabricAttach'}]

fcoe_networks = [{'name': 'fcoe_1071', 'type': 'fcoe-networkV4', 'vlanId': 1071, 'managedSanUri': 'FCSan:VSAN1071'},
                 {'name': 'fcoe_1081', 'type': 'fcoe-networkV4', 'vlanId': 1081, 'managedSanUri': 'FCSan:VSAN1081'}]

iscsi_networks = [{"vlanId": "1061", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI1", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"}]

storage_systems = [{'name': 'COSMOS-7400-9.125', 'family': 'StoreServ', "hostname": "172.25.9.125", "credentials": {"username": "cosmos", "password": "Nextgen9"}, "serialNumber": "1615657", 'deviceSpecificAttributes': {'managedDomain': 'Cosmos-Automation', 'managedPools': []}},
                   {'name': 'COSMOS-8200-9.156', 'family': 'StoreServ', "hostname": "172.25.9.156", "credentials": {"username": "cosmos", "password": "Nextgen9"}, "serialNumber": "2M26200355", 'deviceSpecificAttributes': {'managedDomain': 'Cosmos-QA', 'managedPools': []}},
                   {"name": "Cosmos_HWVSAClust", "family": "StoreVirtual", "hostname": "172.25.15.4", "credentials": {"username": "admin", "password": "Cosmos123"},
                    "ports": [{"type": "StorageTargetPortV4", "name": "172.25.15.4", "address": "172.25.15.4", "tcpPort": 3260, "actualSanUri": None, "actualSanName": None,
                               "expectedNetworkUri": "ETH:iSCSI1", "expectedNetworkName": "iSCSI1", "expectedSanUri": None, "expectedSanName": None,
                               "mode": "Managed", "protocolType": "iSCSI", "deviceSpecificAttributes": {"ipV4NetMask": "255.255.255.0"}, "label": None, "groupName": None}]}]

storage_pools = [{"storageSystemUri": "COSMOS-7400-9.125", "name": "Automation-CPG", "isManaged": True},
                 {"storageSystemUri": "COSMOS-8200-9.156", "name": "TBFC_r5", "isManaged": True},
                 {"storageSystemUri": "Cosmos_HWVSAClust", "name": "Cosmos_HWVSAClust", "isManaged": True}]

storage_volumes = [{"storageSystemUri": "COSMOS-8200-9.156", "name": "ESX65U2_650_FC_Run2"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "ESX65U2_650_FC_Run2_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "esx67u1_630_fcoe_run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "esx67u1_630_fcoe_run1_vol2"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "esxi67u1_630_fc_vol"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "esxi67u1_630_fc_run2_vol2"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "esxi67_650_fc_run2"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "esxi67_650_fc_run2_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "esxi67_650_fcoe_run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "esxi67_650_fcoe_run1_vol2"},
                   {"storageSystemUri": "Cosmos_HWVSAClust", "name": "esxi67_650_iscsi_run2"},
                   {"storageSystemUri": "Cosmos_HWVSAClust", "name": "rhel76_650_iscsi_run2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "RHEL7.5_536_FCoE_Run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "RHEL7.5_536_FCoE_Run1_vol2"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "RHEL7.5_650_FC_Run1"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "RHEL7.5_650_FC_Run1_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "RHEL610_536_FCoE_Run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "RHEL610_536_FCoE_Run1_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "Rhel76_536_FCOE_Run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "Rhel76_536_FCOE_Run1_vol2"},
                   {"storageSystemUri": "Cosmos_HWVSAClust", "name": "RHEL76_630_ISCSI_test"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "rhel76_fc_630_run2"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "rhel76_fc_630_run2_vol2"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "rhel76_fc_650_run2"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "rhel76_fc_650_run2_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "rhel76_fcoe_630_run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "rhel76_fcoe_630_run1_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "rhel76_fcoe_650_run2"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "rhel76_fcoe_650_run2_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "Suse12SP3_536_fcoe_vol"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "Suse12SP3_536_fcoe_run1_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "Suse12SP4_536_fcoe_vol"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "Suse12SP4_536_fcoe_run1_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "SuSE15_536_FCoE_Run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "SuSE15_536_FCoE_Run1_vol2"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "SuSE15_630_FC_Run2"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "SuSE15_630_FC_Run2_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "Suse15_650_fcoe_run1"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "SuSE15_650_FCoE_Run1_vol2"},
                   {"storageSystemUri": "COSMOS-7400-9.125", "name": "SuSE15_630_FCoE_run2"}, {"storageSystemUri": "COSMOS-7400-9.125", "name": "SuSE15_630_FCoE_Run2_vol2"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "Suse15_650_fc_vol"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "Suse15_650_fc_run2_vol2"},
                   {"storageSystemUri": "Cosmos_HWVSAClust", "name": "Suse15_650_iscsi_vol"},
                   {"storageSystemUri": "COSMOS-8200-9.156", "name": "esx65u2_630_fcoe_vol"}, {"storageSystemUri": "COSMOS-8200-9.156", "name": "esx65u2_630_fcoe_vol2"}]

uplink_sets = {
    '81_FC1': {'name': 'FC1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},

    '81_FC2': {'name': 'FC2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},

    '81_FC3': {'name': 'FC1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'}]},

    '81_FC4': {'name': 'FC2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '4', 'port': 'X3', 'speed': 'Auto'}]},

    '81_FCOE1': {'name': 'FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1081'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},

    '81_FCOE2': {'name': 'FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1071'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},

    '81_FCOE3': {'name': 'FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1081'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},

    '81_FCOE4': {'name': 'FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1071'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}]},

    '81_Eth1': {'name': 'Eth1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Eth1_1064'], 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]},

    '81_Eth2': {'name': 'Eth2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Eth2_1064'], 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},

    '86_Eth1': {'name': 'Eth1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Eth1_1064'], 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]},

    '86_Eth2': {'name': 'Eth2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Eth2_1064'], 'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},

    '86_FCOE1': {'name': 'FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1081'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},

    '86_FCOE2': {'name': 'FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1071'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},

    '86_FCOE3': {'name': 'FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1081'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},

    '86_FCOE4': {'name': 'FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe_1071'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}]},

    '86_iscsi': {'name': 'iscsi1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['iSCSI1'], 'mode': 'Auto',
                 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X4', 'speed': 'Auto'},
                                            {'bay': '4', 'port': 'X4', 'speed': 'Auto'},
                                            ]},
    '86_FC1': {'name': 'FC1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},

    '86_FC2': {'name': 'FC2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},

    '86_FC3': {'name': 'FC1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'}]},

    '86_FC4': {'name': 'FC2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2'], 'mode': 'Auto',
               'logicalPortConfigInfos': [{'bay': '4', 'port': 'X3', 'speed': 'Auto'}]}, }

ligs = [{'name': 'LIG81_Run1', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['81_Eth1'].copy(), uplink_sets['81_Eth2'].copy(), uplink_sets['81_FCOE1'].copy(), uplink_sets['81_FCOE2'].copy(),
                        uplink_sets['81_FC1'].copy(), uplink_sets['81_FC2'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}], },

        {'name': 'LIG81_Run2', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['81_FCOE3'].copy(), uplink_sets['81_FCOE4'].copy(), uplink_sets['81_FC3'].copy(), uplink_sets['81_FC4'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}], },

        {'name': 'LIG86_Run1', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['86_Eth1'].copy(), uplink_sets['86_Eth2'].copy(), uplink_sets['86_FCOE1'].copy(), uplink_sets['86_FCOE2'].copy(),
                        uplink_sets['86_FC1'].copy(), uplink_sets['86_FC2'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}], },
        {'name': 'LIG86_Run2', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['86_FCOE3'].copy(), uplink_sets['86_FCOE4'].copy(),
                        uplink_sets['86_FC3'].copy(), uplink_sets['86_FC4'].copy(), uplink_sets['86_iscsi'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}], }]

expected_lig = [{'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'LIG81_Run1', 'state': 'Active', 'status': None, 'category': 'logical-interconnect-groups', 'uri': 'LIG:LIG81_Run1',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'LIG81_Run2', 'state': 'Active', 'status': None, 'category': 'logical-interconnect-groups', 'uri': 'LIG:LIG81_Run2',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}},
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'LIG86_Run1', 'state': 'Active', 'status': None, 'category': 'logical-interconnect-groups', 'uri': 'LIG:LIG86_Run1',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}},
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'LIG86_Run2', 'state': 'Active', 'status': None, 'category': 'logical-interconnect-groups', 'uri': 'LIG:LIG86_Run2',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, }]

encgroups_add = [{'name': 'EG81', 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG81_Run1'},
                                                              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG81_Run1'},
                                                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG81_Run2'},
                                                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG81_Run2'}],
                  'configurationScript': '', 'ipAddressingMode': None, 'powerMode': None, 'ipRangeUris': [], 'enclosureCount': 1, 'osDeploymentSettings': None, },
                 {'name': 'EG86', 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG86_Run1'},
                                                              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG86_Run1'},
                                                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG86_Run2'},
                                                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG86_Run2'}],
                  'configurationScript': '', 'ipAddressingMode': None, 'powerMode': None, 'ipRangeUris': [], 'enclosureCount': 1, 'osDeploymentSettings': None, }]

logical_enclosure = [{'name': 'BFS-AuT-Encl_81-01', 'enclosureUris': ['ENC:BFS-AuT-Encl_81-01'], 'enclosureGroupUri': 'EG:EG81'},
                     {'name': 'BFS-AuT-Encl_86-01', 'enclosureUris': ['ENC:BFS-AuT-Encl_86-01'], 'enclosureGroupUri': 'EG:EG86'}]

logical_interconnect = [{"name": "ENCL-81-LIG81_Run2"}, {"name": "ENCL-81-LIG81_Run2"}, {"name": "ENCL-86-LIG86_Run2"}, {"name": "ENCL-86-LIG86_Run2"}]

encl_names_firmware_update = [{'name': 'BFS-AuT-Encl_81-01'}, {'name': 'BFS-AuT-Encl_86-01'}]

encl = [{"enclosureGroupUri": "EG:EG81", "name": "BFS-AuT-Encl_81-01", "hostname": "172.25.81.11", "username": "Admin", "password": "Insight7",
         "licensingIntent": "OneViewNoiLO", "updateFirmwareOn": None, 'firmwareBaselineUri': None, "forceInstallFirmware": False, "force": True},
        {"enclosureGroupUri": "EG:EG86", "name": "BFS-AuT-Encl_86-01", "hostname": "172.25.86.11", "username": "Admin", "password": "Insight7",
         "licensingIntent": "OneViewNoiLO", 'firmwareBaselineUri': None, "updateFirmwareOn": None, "forceInstallFirmware": False, "force": True}]

custom_spp = {"baselineUri": "/rest/firmware-drivers/{baseSPPName}",
              "hotfixUris": ["/rest/firmware-drivers/{hotfixName2}"],
              "customBaselineName": "5_00"}

licenses = [{'key': 'ABAG AQEA H9PQ 8HV2 V7B5 HWWB Y9JL KMPL B89H MZVU DXAU 2CSM GHTG L762 DMF5 GRRM KJVT D5KM EFVW TSNJ XFU9 4ZSK E828 LFK6 FKA6 DU5N TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8UW BGB5 C324 SFUZ CMSB VNTJ ESB7 KVGR UNPC H4N5 NGHL 97D4 "EG3188881 KEY-E5Y35A#FUSION HP_OV_3yr_24x7_Supp_Phys_Flex_Lic ED4UATGCG2A9"_3JMZZ-RB9CN-DQD7H-CPB8P-M7WW2'},
            {'key': 'QCLG C9MA H9PQ 8HUZ U7B5 HWW5 Y9JL KMPL KRWA NBZY DXAU 2CSM GHTG L762 DNV7 GQFQ KJVT D5KM EFVW DT5J LFM8 76S8 C8SN YGSG Y8JC QUXV XZKH ABB4 NV2C LHXU VLXL HFMP J8TG 2VEB LK4U R6UF S7QS TRRL GX96 CMH4 6MPA M8LC KZU7 WE4X YN9X CDNB NT35 GH9J JGTJ QCV6 3EJF N975 "OV_NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR EY67ATGDTH6C"'}]

# Enclosure Group data
expected_encgroups_add = DD.make_expected_enc_group_data(encgroups_add)

# SAN managers data
san_managers = DD.create_san_manager_data(sans)
expected_san_managers = DD.get_expected_san_manager_data(sans)

# Ethernet Networks data
expected_ethernet_networks = DD.get_expected_ethernet_data(ethernet_networks)

# Fiber channel Networks data
expected_fc_networks = DD.get_expected_fcnet_data(fc_networks)

# FCoE Networks data
expected_fcoe_networks = DD.get_expected_fcoenet_data(fcoe_networks)

# iSCSI Network data
expected_iscsi_networks = DD.get_expected_iscsi_data(iscsi_networks)

# Storage Systems data
expected_storage_systems = DD.expected_storage_system(storage_systems)

# Storage Volumes data
existing_storage_volumes = DD.existing_storage_volumes(storage_volumes)
expected_existing_storage_volumes = DD.expected_storage_volumes(storage_volumes)
delete_storage_volumes_from_OV_only = DD.existing_storage_volumes(storage_volumes)

# Enclosure Data
enclosures = DD.make_enclosure_data(encl)
expected_enclosures = DD.make_expected_enclosure_data(encl)

efuse_interconnect_a_side = [{'host': '172.25.81.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 1, 'inter_name': 'BFS-AuT-Encl_81-01, interconnect 1'},
                             {'host': '172.25.86.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 1, 'inter_name': 'BFS-AuT-Encl_86-01, interconnect 1'},
                             {'host': '172.25.81.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 3, 'inter_name': 'BFS-AuT-Encl_81-01, interconnect 3'},
                             {'host': '172.25.86.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 3, 'inter_name': 'BFS-AuT-Encl_86-01, interconnect 3'}
                             ]

efuse_interconnect_b_side = [{'host': '172.25.81.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 2, 'inter_name': 'BFS-AuT-Encl_81-01, interconnect 2'},
                             {'host': '172.25.86.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 2, 'inter_name': 'BFS-AuT-Encl_86-01, interconnect 2'},
                             {'host': '172.25.81.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 4, 'inter_name': 'BFS-AuT-Encl_81-01, interconnect 4'},
                             {'host': '172.25.86.11', 'user': 'Admin', 'password': 'Insight7', 'device': 'INTERCONNECT', 'bay_number': 4, 'inter_name': 'BFS-AuT-Encl_86-01, interconnect 4'}]

failure_uplink = {'interconnect_a_side': [{"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "Eth1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                           "portId": "X5", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "Eth1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                           "portId": "X5", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "iscsi1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                           "portId": "X4", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X4"}
                                          ],
                  'interconnect_b_side': [{"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "Eth2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                           "portId": "X5", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "Eth2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                           "portId": "X5", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "FC2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "iscsi1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                           "portId": "X4", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X4"}
                                          ],
                  }

interconnect_aside_disable = DD.make_uplink_disable(failure_uplink['interconnect_a_side'], critical)
interconnect_aside_enable = DD.make_uplink_enable(failure_uplink['interconnect_a_side'], ok)
interconnect_bside_disable = DD.make_uplink_disable(failure_uplink['interconnect_b_side'], critical)
interconnect_bside_enable = DD.make_uplink_enable(failure_uplink['interconnect_b_side'], ok)

failure_downlink_run1 = {'interconnect_a_side_run1': [{"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"}
                                                      ],
                         'interconnect_b_side_run1': [{"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"}
                                                      ],
                         }
run1_interconnect_down_aside_disable = DD.make_downlink_disable(failure_downlink_run1['interconnect_a_side_run1'], critical)
run1_interconnect_down_aside_enable = DD.make_downlink_enable(failure_downlink_run1['interconnect_a_side_run1'], ok)
run1_interconnect_down_bside_disable = DD.make_downlink_disable(failure_downlink_run1['interconnect_b_side_run1'], critical)
run1_interconnect_down_bside_enable = DD.make_downlink_enable(failure_downlink_run1['interconnect_b_side_run1'], ok)

failure_downlink_run2 = {'interconnect_a_side_run2': [{"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 1",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 3",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 1",
                                                       "portId": "d15", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d15"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                      {"associatedUplinkSetUri": "FCOE1", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 3",
                                                       "portId": "d15", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d15"}
                                                      ],
                         'interconnect_b_side_run2': [{"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 2",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_81-01, interconnect 4",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 2",
                                                       "portId": "d15", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d15"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                      {"associatedUplinkSetUri": "FCOE2", "interconnectName": "BFS-AuT-Encl_86-01, interconnect 4",
                                                       "portId": "d15", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d15"}
                                                      ],
                         }
run2_interconnect_down_aside_disable = DD.make_downlink_disable(failure_downlink_run2['interconnect_a_side_run2'], critical)
run2_interconnect_down_aside_enable = DD.make_downlink_enable(failure_downlink_run2['interconnect_a_side_run2'], ok)
run2_interconnect_down_bside_disable = DD.make_downlink_disable(failure_downlink_run2['interconnect_b_side_run2'], critical)
run2_interconnect_down_bside_enable = DD.make_downlink_enable(failure_downlink_run2['interconnect_b_side_run2'], ok)

############################################################################################
# Rhel76_630_FC_Run2
############################################################################################
rhel76_630_fc_run2_profile_data = [{'name': 'Rhel76_630_FC_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 10', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:08', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:09', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:10', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:11', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                    "boot": {"order": ["HardDisk"], "manageBoot": True},
                                    "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                    'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_fc_630_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                         'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_630_fc_run2_profile = DD.make_server_profile_data(rhel76_630_fc_run2_profile_data, firmware)
rhel76_630_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_630_fc_run2_profile_data, firmware)
rhel76_630_fc_run2_profile_add_volume_data = copy.deepcopy(rhel76_630_fc_run2_profile_data)
rhel76_630_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_630_fc_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:rhel76_fc_630_run2_vol2")
rhel76_630_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_630_fc_run2_profile_add_volume_data, firmware)
rhel76_630_fc_run2_profile_update_spp = DD.make_server_profile_data(rhel76_630_fc_run2_profile_add_volume_data, update_firmware)
rhel76_630_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_630_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Rhel76_630_FCOE_Run1
############################################################################################
rhel76_630_fcoe_run1_profile_data = [{'name': 'Rhel76_630_FCOE_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 3', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:1C', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:1D', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:1E', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:1F', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_fcoe_630_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_630_fcoe_run1_profile = DD.make_server_profile_data(rhel76_630_fcoe_run1_profile_data, firmware)
rhel76_630_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(rhel76_630_fcoe_run1_profile_data, firmware)
rhel76_630_fcoe_run1_profile_add_volume_data = copy.deepcopy(rhel76_630_fcoe_run1_profile_data)
rhel76_630_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_630_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:rhel76_fcoe_630_run1_vol2")
rhel76_630_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_630_fcoe_run1_profile_add_volume_data, firmware)
rhel76_630_fcoe_run1_profile_update_spp = DD.make_server_profile_data(rhel76_630_fcoe_run1_profile_add_volume_data, update_firmware)
rhel76_630_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_630_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# Rhel76_630_Iscsi_run2
############################################################################################
rhel76_630_iscsi_run2_profile_data = [{'name': 'Rhel76_630_Iscsi_run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 15', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:14', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:15', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:iSCSI1', "macType": "UserDefined", "mac": "82:E6:A2:80:00:16", "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.93", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"},
                                                                               "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {'id': 4, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:iSCSI1', "macType": "UserDefined", "mac": "82:E6:A2:80:00:17", "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.94", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"},
                                                                               "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}], },
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'IPv4'},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL76_630_ISCSI_test", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:Cosmos_HWVSAClust',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_630_iscsi_run2_profile = DD.make_server_profile_data(rhel76_630_iscsi_run2_profile_data, firmware)
rhel76_630_iscsi_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_630_iscsi_run2_profile_data, firmware)
rhel76_630_iscsi_run2_profile_update_spp = DD.make_server_profile_data(rhel76_630_iscsi_run2_profile_data, update_firmware)
rhel76_630_iscsi_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_630_iscsi_run2_profile_data, update_firmware)

############################################################################################
#  Rhel76_650_FC_Run2
############################################################################################
rhel76_650_fc_run2_profile_data = [{'name': 'Rhel76_650_FC_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 4', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:48', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:49', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:4A', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:4B', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                    "boot": {"order": ["HardDisk"], "manageBoot": True},
                                    "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                    'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_fc_650_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                         'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_650_fc_run2_profile = DD.make_server_profile_data(rhel76_650_fc_run2_profile_data, firmware)
rhel76_650_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_650_fc_run2_profile_data, firmware)
rhel76_650_fc_run2_profile_add_volume_data = copy.deepcopy(rhel76_650_fc_run2_profile_data)
rhel76_650_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_650_fc_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:rhel76_fc_650_run2_vol2")
rhel76_650_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_650_fc_run2_profile_add_volume_data, firmware)
rhel76_650_fc_run2_profile_update_spp = DD.make_server_profile_data(rhel76_650_fc_run2_profile_add_volume_data, update_firmware)
rhel76_650_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_650_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Rhel76_650_FCOE_Run2
############################################################################################
rhel76_650_fcoe_run2_profile_data = [{'name': 'Rhel76_650_FCOE_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 2', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:20', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:21', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:22', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:23', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_fcoe_650_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_650_fcoe_run2_profile = DD.make_server_profile_data(rhel76_650_fcoe_run2_profile_data, firmware)
rhel76_650_fcoe_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_650_fcoe_run2_profile_data, firmware)
rhel76_650_fcoe_run2_profile_add_volume_data = copy.deepcopy(rhel76_650_fcoe_run2_profile_data)
rhel76_650_fcoe_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_650_fcoe_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:rhel76_fcoe_650_run2_vol2")
rhel76_650_fcoe_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_650_fcoe_run2_profile_add_volume_data, firmware)
rhel76_650_fcoe_run2_profile_update_spp = DD.make_server_profile_data(rhel76_650_fcoe_run2_profile_add_volume_data, update_firmware)
rhel76_650_fcoe_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_650_fcoe_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Rhel76_650_Iscsi_run2
############################################################################################
rhel76_650_iscsi_run2_profile_data = [{'name': 'Rhel76_650_Iscsi_run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 5', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:44', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:45', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'networkUri': 'ETH:iSCSI1', "macType": "UserDefined", "mac": "82:E6:A2:80:00:46", "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.95", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"},
                                                                               "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {'id': 4, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:iSCSI1', "macType": "UserDefined", "mac": "82:E6:A2:80:00:47", "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.96", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"},
                                                                               "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}], },
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'IPv4'},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_650_iscsi_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:Cosmos_HWVSAClust',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_650_iscsi_run2_profile = DD.make_server_profile_data(rhel76_650_iscsi_run2_profile_data, firmware)
rhel76_650_iscsi_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_650_iscsi_run2_profile_data, firmware)
rhel76_650_iscsi_run2_profile_update_spp = DD.make_server_profile_data(rhel76_650_iscsi_run2_profile_data, update_firmware)
rhel76_650_iscsi_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_650_iscsi_run2_profile_data, update_firmware)

############################################################################################
# Esxi67_650_FC_Run2
############################################################################################
esxi67_650_fc_run2_profile_data = [{'name': 'Esxi67_650_FC_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 6', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:50', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:51', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:52', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:53', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                    "boot": {"order": ["HardDisk"], "manageBoot": True},
                                    "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                    'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esxi67_650_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                         'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esxi67_650_fc_run2_profile = DD.make_server_profile_data(esxi67_650_fc_run2_profile_data, firmware)
esxi67_650_fc_run2_profile_expected = DD.make_expected_server_profile_data(esxi67_650_fc_run2_profile_data, firmware)
esxi67_650_fc_run2_profile_add_volume_data = copy.deepcopy(esxi67_650_fc_run2_profile_data)
esxi67_650_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(esxi67_650_fc_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:esxi67_650_fc_run2_vol2")
esxi67_650_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(esxi67_650_fc_run2_profile_add_volume_data, firmware)
esxi67_650_fc_run2_profile_update_spp = DD.make_server_profile_data(esxi67_650_fc_run2_profile_add_volume_data, update_firmware)
esxi67_650_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(esxi67_650_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Esxi67_650_FCOE_Run1
############################################################################################
esxi67_650_fcoe_run1_profile_data = [{'name': 'Esxi67_650_FCOE_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 6', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:04', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:05', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:06', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:07', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esxi67_650_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esxi67_650_fcoe_run1_profile = DD.make_server_profile_data(esxi67_650_fcoe_run1_profile_data, firmware)
esxi67_650_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(esxi67_650_fcoe_run1_profile_data, firmware)
esxi67_650_fcoe_run1_profile_add_volume_data = copy.deepcopy(esxi67_650_fcoe_run1_profile_data)
esxi67_650_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esxi67_650_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:esxi67_650_fcoe_run1_vol2")
esxi67_650_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esxi67_650_fcoe_run1_profile_add_volume_data, firmware)
esxi67_650_fcoe_run1_profile_update_spp = DD.make_server_profile_data(esxi67_650_fcoe_run1_profile_add_volume_data, update_firmware)
esxi67_650_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(esxi67_650_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# SuSE15_630_FCoE_Run2
############################################################################################
SuSE15_630_FCoE_Run2_profile_data = [{'name': 'SuSE15_630_FCoE_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 2', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:24', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:25', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:26', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:27', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SuSE15_630_FCoE_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

SuSE15_630_FCoE_Run2_profile = DD.make_server_profile_data(SuSE15_630_FCoE_Run2_profile_data, firmware)
SuSE15_630_FCoE_Run2_profile_expected = DD.make_expected_server_profile_data(SuSE15_630_FCoE_Run2_profile_data, firmware)
SuSE15_630_FCoE_Run2_profile_add_volume_data = copy.deepcopy(SuSE15_630_FCoE_Run2_profile_data)
SuSE15_630_FCoE_Run2_profile_add_volume = DD.make_server_profile_add_volume_data(SuSE15_630_FCoE_Run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:SuSE15_630_FCoE_Run2_vol2")
SuSE15_630_FCoE_Run2_profile_add_volume_expected = DD.make_expected_server_profile_data(SuSE15_630_FCoE_Run2_profile_add_volume_data, firmware)
SuSE15_630_FCoE_Run2_profile_update_spp = DD.make_server_profile_data(SuSE15_630_FCoE_Run2_profile_add_volume_data, update_firmware)
SuSE15_630_FCoE_Run2_profile_update_spp_expected = DD.make_expected_server_profile_data(SuSE15_630_FCoE_Run2_profile_add_volume_data, update_firmware)

############################################################################################
# SuSE15_630_FC_Run2
############################################################################################
SuSE15_630_FC_Run2_profile_data = [{'name': 'SuSE15_630_FC_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 3', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:4C', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:4D', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:4E', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:4F', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                    "boot": {"order": ["HardDisk"], "manageBoot": True},
                                    "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                    'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SuSE15_630_FC_Run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                         'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

SuSE15_630_FC_Run2_profile = DD.make_server_profile_data(SuSE15_630_FC_Run2_profile_data, firmware)
SuSE15_630_FC_Run2_profile_expected = DD.make_expected_server_profile_data(SuSE15_630_FC_Run2_profile_data, firmware)
SuSE15_630_FC_Run2_profile_add_volume_data = copy.deepcopy(SuSE15_630_FC_Run2_profile_data)
SuSE15_630_FC_Run2_profile_add_volume = DD.make_server_profile_add_volume_data(SuSE15_630_FC_Run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:SuSE15_630_FC_Run2_vol2")
SuSE15_630_FC_Run2_profile_add_volume_expected = DD.make_expected_server_profile_data(SuSE15_630_FC_Run2_profile_add_volume_data, firmware)
SuSE15_630_FC_Run2_profile_update_spp = DD.make_server_profile_data(SuSE15_630_FC_Run2_profile_add_volume_data, update_firmware)
SuSE15_630_FC_Run2_profile_update_spp_expected = DD.make_expected_server_profile_data(SuSE15_630_FC_Run2_profile_add_volume_data, update_firmware)

############################################################################################
# ESX67U1_650_ISCSI_Run2
############################################################################################
ESX67U1_650_iSCSI_Run2_profile_data = [{'name': 'ESX67U1_650_iSCSI_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 6', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:60', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:61', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:62', 'macType': 'UserDefined', 'networkUri': 'ETH:iSCSI1', "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.97", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"}, 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:2-b", 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:63', 'macType': 'UserDefined', "networkUri": "ETH:iSCSI1", "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.98", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"}, "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'IPv4'},
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esxi67_650_iscsi_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:Cosmos_HWVSAClust',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

ESX67U1_650_iSCSI_Run2_profile = DD.make_server_profile_data(ESX67U1_650_iSCSI_Run2_profile_data, firmware)
ESX67U1_650_iSCSI_Run2_profile_expected = DD.make_expected_server_profile_data(ESX67U1_650_iSCSI_Run2_profile_data, firmware)
ESX67U1_650_iSCSI_Run2_profile_update_spp = DD.make_server_profile_data(ESX67U1_650_iSCSI_Run2_profile_data, update_firmware)
ESX67U1_650_iSCSI_Run2_profile_update_spp_expected = DD.make_expected_server_profile_data(ESX67U1_650_iSCSI_Run2_profile_data, update_firmware)

############################################################################################
# ESX65U2_650_FC_Run2
############################################################################################
ESX65U2_650_FC_Run2_profile_data = [{'name': 'ESX65U2_650_FC_Run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 9', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                     'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:54', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                            {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:55', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                            {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:56', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                            {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:57', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                     'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                     "boot": {"order": ["HardDisk"], "manageBoot": True},
                                     "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                     'bios': {'manageBios': False, 'overriddenSettings': []},
                                     'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                     'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                     'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                   'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:ESX65U2_650_FC_Run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                          'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

ESX65U2_650_FC_Run2_profile = DD.make_server_profile_data(ESX65U2_650_FC_Run2_profile_data, firmware)
ESX65U2_650_FC_Run2_profile_expected = DD.make_expected_server_profile_data(ESX65U2_650_FC_Run2_profile_data, firmware)
ESX65U2_650_FC_Run2_profile_add_volume_data = copy.deepcopy(ESX65U2_650_FC_Run2_profile_data)
ESX65U2_650_FC_Run2_profile_add_volume = DD.make_server_profile_add_volume_data(ESX65U2_650_FC_Run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:ESX65U2_650_FC_Run2_vol2")
ESX65U2_650_FC_Run2_profile_add_volume_expected = DD.make_expected_server_profile_data(ESX65U2_650_FC_Run2_profile_add_volume_data, firmware)
ESX65U2_650_FC_Run2_profile_update_spp = DD.make_server_profile_data(ESX65U2_650_FC_Run2_profile_data, update_firmware)
ESX65U2_650_FC_Run2_profile_update_spp_expected = DD.make_expected_server_profile_data(ESX65U2_650_FC_Run2_profile_data, update_firmware)

############################################################################################
# Esxi67u1_630_FCOE_Run1
############################################################################################
esxi67u1_630_fcoe_run1_profile_data = [{'name': 'Esxi67U1_630_fcoe_run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 4', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:58', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:59', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:5A', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '5000', 'mac': '82:E6:A2:80:00:5B', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter',
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx67u1_630_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esxi67u1_630_fcoe_run1_profile = DD.make_server_profile_data(esxi67u1_630_fcoe_run1_profile_data, firmware)
esxi67u1_630_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(esxi67u1_630_fcoe_run1_profile_data, firmware)
esxi67u1_630_fcoe_run1_profile_add_volume_data = copy.deepcopy(esxi67u1_630_fcoe_run1_profile_data)
esxi67u1_630_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esxi67u1_630_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:esx67u1_630_fcoe_run1_vol2")
esxi67u1_630_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esxi67u1_630_fcoe_run1_profile_add_volume_data, firmware)
esxi67u1_630_fcoe_run1_profile_update_spp = DD.make_server_profile_data(esxi67u1_630_fcoe_run1_profile_add_volume_data, update_firmware)
esxi67u1_630_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(esxi67u1_630_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# RHEL7.5_650_FC_Run1
############################################################################################
RHEL75_650_FC_Run1_profile_data = [{'name': 'RHEL7.5_650_FC_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 1', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:70', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:71', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:72', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:73', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                    "boot": {"order": ["HardDisk"], "manageBoot": True},
                                    "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                    'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL7.5_650_FC_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                         'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

RHEL75_650_FC_Run1_profile = DD.make_server_profile_data(RHEL75_650_FC_Run1_profile_data, firmware)
RHEL75_650_FC_Run1_profile_expected = DD.make_expected_server_profile_data(RHEL75_650_FC_Run1_profile_data, firmware)
RHEL75_650_FC_Run1_profile_add_volume_data = copy.deepcopy(RHEL75_650_FC_Run1_profile_data)
RHEL75_650_FC_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(RHEL75_650_FC_Run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:RHEL7.5_650_FC_Run1_vol2")
RHEL75_650_FC_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(RHEL75_650_FC_Run1_profile_add_volume_data, firmware)
RHEL75_650_FC_Run1_profile_update_spp = DD.make_server_profile_data(RHEL75_650_FC_Run1_profile_add_volume_data, update_firmware)
RHEL75_650_FC_Run1_profile_update_spp_expected = DD.make_expected_server_profile_data(RHEL75_650_FC_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# Sles12 SP4_536_FCOE_Run1
############################################################################################
suse12SP4_536_fcoe_run1_profile_data = [{'name': 'Suse12SP4_536_fcoe_run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 3', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:88', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:89', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:8A', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:8B', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Suse12SP4_536_fcoe_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

suse12SP4_536_fcoe_run1_profile = DD.make_server_profile_data(suse12SP4_536_fcoe_run1_profile_data, firmware)
suse12SP4_536_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(suse12SP4_536_fcoe_run1_profile_data, firmware)
suse12SP4_536_fcoe_run1_profile_add_volume_data = copy.deepcopy(suse12SP4_536_fcoe_run1_profile_data)
suse12SP4_536_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(suse12SP4_536_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:Suse12SP4_536_fcoe_run1_vol2")
suse12SP4_536_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(suse12SP4_536_fcoe_run1_profile_add_volume_data, firmware)
suse12SP4_536_fcoe_run1_profile_update_spp = DD.make_server_profile_data(suse12SP4_536_fcoe_run1_profile_add_volume_data, update_firmware)
suse12SP4_536_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(suse12SP4_536_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# Sles12 SP3_536_FCOE_Run1
############################################################################################
suse12SP3_536_fcoe_run1_profile_data = [{'name': 'Suse12SP3_536_fcoe_run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 5', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '1A:32:CC:A0:00:00', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '1A:32:CC:A0:00:01', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'mac': '1A:32:CC:A0:00:02', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000', 'mac': '1A:32:CC:A0:00:03', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Suse12SP3_536_fcoe_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

suse12SP3_536_fcoe_run1_profile = DD.make_server_profile_data(suse12SP3_536_fcoe_run1_profile_data, firmware)
suse12SP3_536_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(suse12SP3_536_fcoe_run1_profile_data, firmware)
suse12SP3_536_fcoe_run1_profile_add_volume_data = copy.deepcopy(suse12SP3_536_fcoe_run1_profile_data)
suse12SP3_536_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(suse12SP3_536_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:Suse12SP3_536_fcoe_run1_vol2")
suse12SP3_536_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(suse12SP3_536_fcoe_run1_profile_add_volume_data, firmware)
suse12SP3_536_fcoe_run1_profile_update_spp = DD.make_server_profile_data(suse12SP3_536_fcoe_run1_profile_add_volume_data, update_firmware)
suse12SP3_536_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(suse12SP3_536_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# SuSE15_536_FCoE_Run1
############################################################################################
SuSE15_536_FCoE_Run1_profile_data = [{'name': 'SuSE15_536_FCoE_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 6', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:28', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:29', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:2A', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:2B', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SuSE15_536_FCoE_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

SuSE15_536_FCoE_Run1_profile = DD.make_server_profile_data(SuSE15_536_FCoE_Run1_profile_data, firmware)
SuSE15_536_FCoE_Run1_profile_expected = DD.make_expected_server_profile_data(SuSE15_536_FCoE_Run1_profile_data, firmware)
SuSE15_536_FCoE_Run1_profile_add_volume_data = copy.deepcopy(SuSE15_536_FCoE_Run1_profile_data)
SuSE15_536_FCoE_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(SuSE15_536_FCoE_Run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:SuSE15_536_FCoE_Run1_vol2")
SuSE15_536_FCoE_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(SuSE15_536_FCoE_Run1_profile_add_volume_data, firmware)
SuSE15_536_FCoE_Run1_profile_update_spp = DD.make_server_profile_data(SuSE15_536_FCoE_Run1_profile_add_volume_data, update_firmware)
SuSE15_536_FCoE_Run1_profile_update_spp_expected = DD.make_expected_server_profile_data(SuSE15_536_FCoE_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# Sles15_650_FCOE_Run1
############################################################################################
suse15_650_fcoe_run1_profile_data = [{'name': 'Suse15_650_fcoe_run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 2', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:94', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:95', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:96', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:97', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Suse15_650_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

suse15_650_fcoe_run1_profile = DD.make_server_profile_data(suse15_650_fcoe_run1_profile_data, firmware)
suse15_650_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(suse15_650_fcoe_run1_profile_data, firmware)
suse15_650_fcoe_run1_profile_add_volume_data = copy.deepcopy(suse15_650_fcoe_run1_profile_data)
suse15_650_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(suse15_650_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:SuSE15_650_FCoE_Run1_vol2")
suse15_650_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(suse15_650_fcoe_run1_profile_add_volume_data, firmware)
suse15_650_fcoe_run1_profile_update_spp = DD.make_server_profile_data(suse15_650_fcoe_run1_profile_add_volume_data, update_firmware)
suse15_650_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(suse15_650_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# RHEL610_536_FCoE_Run1
############################################################################################
RHEL610_536_FCoE_Run1_profile_data = [{'name': 'RHEL610_536_FCoE_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 5', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:8C', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:8D', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:8E', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:8F', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL610_536_FCoE_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

RHEL610_536_FCoE_Run1_profile = DD.make_server_profile_data(RHEL610_536_FCoE_Run1_profile_data, firmware)
RHEL610_536_FCoE_Run1_profile_expected = DD.make_expected_server_profile_data(RHEL610_536_FCoE_Run1_profile_data, firmware)
RHEL610_536_FCoE_Run1_profile_add_volume_data = copy.deepcopy(RHEL610_536_FCoE_Run1_profile_data)
RHEL610_536_FCoE_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(RHEL610_536_FCoE_Run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:RHEL610_536_FCoE_Run1_vol2")
RHEL610_536_FCoE_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(RHEL610_536_FCoE_Run1_profile_add_volume_data, firmware)
RHEL610_536_FCoE_Run1_profile_update_spp = DD.make_server_profile_data(RHEL610_536_FCoE_Run1_profile_add_volume_data, update_firmware)
RHEL610_536_FCoE_Run1_profile_update_spp_expected = DD.make_expected_server_profile_data(RHEL610_536_FCoE_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# RHEL7.5_536_FCoE_Run1
############################################################################################
Rhel75_536_FCoE_Run1_profile_data = [{'name': 'RHEL7.5_536_FCoE_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 4', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:38', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:39', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:3A', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:3B', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL7.5_536_FCoE_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

Rhel75_536_FCoE_Run1_profile = DD.make_server_profile_data(Rhel75_536_FCoE_Run1_profile_data, firmware)
Rhel75_536_FCoE_Run1_profile_expected = DD.make_expected_server_profile_data(Rhel75_536_FCoE_Run1_profile_data, firmware)
Rhel75_536_FCoE_Run1_profile_add_volume_data = copy.deepcopy(Rhel75_536_FCoE_Run1_profile_data)
Rhel75_536_FCoE_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(Rhel75_536_FCoE_Run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:RHEL7.5_536_FCoE_Run1_vol2")
Rhel75_536_FCoE_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(Rhel75_536_FCoE_Run1_profile_add_volume_data, firmware)
Rhel75_536_FCoE_Run1_profile_update_spp = DD.make_server_profile_data(Rhel75_536_FCoE_Run1_profile_add_volume_data, update_firmware)
Rhel75_536_FCoE_Run1_profile_update_spp_expected = DD.make_expected_server_profile_data(Rhel75_536_FCoE_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# Esxi67u1_630_FC_Run2
############################################################################################
esxi67u1_630_fc_run2_profile_data = [{'name': 'esxi67u1_630_fc_run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 5', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:7C', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:7D', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:7E', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:7F', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esxi67u1_630_fc_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esxi67u1_630_fc_run2_profile = DD.make_server_profile_data(esxi67u1_630_fc_run2_profile_data, firmware)
esxi67u1_630_fc_run2_profile_expected = DD.make_expected_server_profile_data(esxi67u1_630_fc_run2_profile_data, firmware)
esxi67u1_630_fc_run2_profile_add_volume_data = copy.deepcopy(esxi67u1_630_fc_run2_profile_data)
esxi67u1_630_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(esxi67u1_630_fc_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:esxi67u1_630_fc_run2_vol2")
esxi67u1_630_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(esxi67u1_630_fc_run2_profile_add_volume_data, firmware)
esxi67u1_630_fc_run2_profile_update_spp = DD.make_server_profile_data(esxi67u1_630_fc_run2_profile_add_volume_data, update_firmware)
esxi67u1_630_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(esxi67u1_630_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Sles15_650_FC_Run2
############################################################################################
suse15_650_fc_run2_profile_data = [{'name': 'Suse15_650_fc_run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_81-01, bay 1', 'enclosureGroupUri': 'EG:EG81', 'description': '', 'affinity': 'Bay',
                                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:2C', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:2D', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                           {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:2E', 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                           {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:2F', 'macType': 'UserDefined', "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                    "boot": {"order": ["HardDisk"], "manageBoot": True},
                                    "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                    'bios': {'manageBios': False, 'overriddenSettings': []},
                                    'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                    'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                    'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                  'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Suse15_650_fc_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                         'volumeStorageSystemUri': 'SSYS:COSMOS-8200-9.156',
                                                                         'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

suse15_650_fc_run2_profile = DD.make_server_profile_data(suse15_650_fc_run2_profile_data, firmware)
suse15_650_fc_run2_profile_expected = DD.make_expected_server_profile_data(suse15_650_fc_run2_profile_data, firmware)
suse15_650_fc_run2_profile_add_volume_data = copy.deepcopy(suse15_650_fc_run2_profile_data)
suse15_650_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(suse15_650_fc_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-8200-9.156', "SVOL:Suse15_650_fc_run2_vol2")
suse15_650_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(suse15_650_fc_run2_profile_add_volume_data, firmware)
suse15_650_fc_run2_profile_update_spp = DD.make_server_profile_data(suse15_650_fc_run2_profile_add_volume_data, update_firmware)
suse15_650_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(suse15_650_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Suse15 650_ISCSI_Run2
############################################################################################
suse15_650_iscsi_run2_profile_data = [{'name': 'Suse15_650_iscsi_run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 7', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:80', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '82:E6:A2:80:00:81', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 1:1-b', 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:82', 'macType': 'UserDefined', 'networkUri': 'ETH:iSCSI1', "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.75", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"}, 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Mezz 1:2-b", 'requestedMbps': '4000', 'mac': '82:E6:A2:80:00:83', 'macType': 'UserDefined', "networkUri": "ETH:iSCSI1", "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "172.25.61.76", "subnetMask": "255.255.255.0", "gateway": "172.25.61.1"}, "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'IPv4'},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Suse15_650_iscsi_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:Cosmos_HWVSAClust',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

suse15_650_iscsi_run2_profile = DD.make_server_profile_data(suse15_650_iscsi_run2_profile_data, firmware)
suse15_650_iscsi_run2_profile_expected = DD.make_expected_server_profile_data(suse15_650_iscsi_run2_profile_data, firmware)
suse15_650_iscsi_run2_profile_update_spp = DD.make_server_profile_data(suse15_650_iscsi_run2_profile_data, update_firmware)
suse15_650_iscsi_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(suse15_650_iscsi_run2_profile_data, update_firmware)

############################################################################################
# Rhel76_536_FCOE_Run1
############################################################################################
Rhel76_536_FCOE_Run1_profile_data = [{'name': 'Rhel76_536_FCOE_Run1', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 2', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '1A:32:CC:A0:00:08', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '1A:32:CC:A0:00:09', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth2_1064', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500', 'mac': '1A:32:CC:A0:00:0A', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500', 'mac': '1A:32:CC:A0:00:0B', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Rhel76_536_FCOE_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

Rhel76_536_FCOE_Run1_profile = DD.make_server_profile_data(Rhel76_536_FCOE_Run1_profile_data, firmware)
Rhel76_536_FCOE_Run1_profile_expected = DD.make_expected_server_profile_data(Rhel76_536_FCOE_Run1_profile_data, firmware)
Rhel76_536_FCOE_Run1_profile_add_volume_data = copy.deepcopy(Rhel76_536_FCOE_Run1_profile_data)
Rhel76_536_FCOE_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(Rhel76_536_FCOE_Run1_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:Rhel76_536_FCOE_Run1_vol2")
Rhel76_536_FCOE_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(Rhel76_536_FCOE_Run1_profile_add_volume_data, firmware)
Rhel76_536_FCOE_Run1_profile_update_spp = DD.make_server_profile_data(Rhel76_536_FCOE_Run1_profile_add_volume_data, update_firmware)
Rhel76_536_FCOE_Run1_profile_update_spp_expected = DD.make_expected_server_profile_data(Rhel76_536_FCOE_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# Esxi65u2_630_FCOE_Run2
############################################################################################
esx65u2_630_fcoe_run2_profile_data = [{'name': 'esx65u2_630_fcoe_run2', 'serverHardwareUri': 'SH:BFS-AuT-Encl_86-01, bay 3', 'enclosureGroupUri': 'EG:EG86', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'mac': '5E:B7:89:C0:00:10', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500', 'mac': '5E:B7:89:C0:00:11', 'macType': 'UserDefined', 'networkUri': 'ETH:Eth1_1064', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1-b', 'requestedMbps': '4000', 'mac': '5E:B7:89:C0:00:12', 'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe_1081', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2-b", 'requestedMbps': '4000', 'mac': '5E:B7:89:C0:00:13', 'macType': 'UserDefined', "networkUri": "FCOE:fcoe_1071", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen9:1:HP FlexFabric 20Gb 2-port 630M Adapter:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx65u2_630_fcoe_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:COSMOS-7400-9.125',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esx65u2_630_fcoe_run2_profile = DD.make_server_profile_data(esx65u2_630_fcoe_run2_profile_data, firmware)
esx65u2_630_fcoe_run2_profile_expected = DD.make_expected_server_profile_data(esx65u2_630_fcoe_run2_profile_data, firmware)
esx65u2_630_fcoe_run2_profile_add_volume_data = copy.deepcopy(esx65u2_630_fcoe_run2_profile_data)
esx65u2_630_fcoe_run2_profile_add_volume = DD.make_server_profile_add_volume_data(esx65u2_630_fcoe_run2_profile_add_volume_data, firmware, 'SSYS:COSMOS-7400-9.125', "SVOL:esx65u2_630_fcoe_vol2")
esx65u2_630_fcoe_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(esx65u2_630_fcoe_run2_profile_add_volume_data, firmware)
esx65u2_630_fcoe_run2_profile_update_spp = DD.make_server_profile_data(esx65u2_630_fcoe_run2_profile_add_volume_data, update_firmware)
esx65u2_630_fcoe_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(esx65u2_630_fcoe_run2_profile_add_volume_data, update_firmware)

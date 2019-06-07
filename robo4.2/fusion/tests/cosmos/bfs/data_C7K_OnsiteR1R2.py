"""
    BFS datafile for onsite C7K environment
"""

from DynamicData import DynamicData
import copy

DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

ilo_credentials = {'username': 'Admin', 'password': 'Cosmos123'}

dhcpservers = [{'ip': '10.146.0.11', 'vlanid': '1146', 'scope': '10.146.0.0', 'username': 'Administrator', 'password': 'Cosmos123'}, ]

gen10snap = '/rest/firmware-drivers/5_00'

firmware = {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareBaselineUri': None}

update_firmware = {'manageFirmware': True, 'forceInstallFirmware': True, 'firmwareInstallType': 'FirmwareAndOSDrivers', 'firmwareBaselineUri': gen10snap}

unassign = True
critical = 'Critical'
ok = 'OK'

# Appliance Data
appliance = {
    'type': "ApplianceNetworkConfigurationV2",
    'applianceNetworks':
    [{
        "device": "eth0",
        "macAddress": "00:50:56:89:8c:d5",
        "interfaceName": "Appliance",
        "activeNode": 1,
        "unconfigure": False,
        "ipv4Type": "STATIC",
        "ipv4Subnet": "255.255.0.0",
        "ipv4Gateway": "10.120.0.1",
        "ipv4NameServers": [],
        "app1Ipv4Addr": "10.120.12.58",
        "ipv6Type": "UNCONFIGURE",
        "hostname": "ci-005056898cd5",
        "confOneNode": True,
        "domainName": "",
        "aliasDisabled": False
    }]
}

licenses = [{'key': 'ACLA C9MA H9P9 CHUZ V7B5 HWWB Y9JL KMPL 5R2H 6DRM DXAU 2CSM GHTG L762 BCV6 EEFY KJVT D5KM EFVW DT5J 69UM NY2G 9K2P 3E22 MKQU 3UFZ TZZX AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U \
            R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863919 HPOV-NFR1 HP_OneView_16_Seat_NFR H592ADTYDJJD"_3PXQT-HWSHJ-7RBW9-ZW3WG-XC2W2'},
            {'key': 'QCLA A9MA H9PA KHW3 V7B5 HWWB Y9JL KMPL BRKD 8FBM DXAU 2CSM GHTG L762 XKJ3 VBF4 KJVT D5KM EFRW DS5R A9E9 52KG 9K2P 3E22 UKYU 3UFZ TZZ7 MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U \
            R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863966 HPOV-NFR1 HP_OneView_16_Seat_NFR 7EA7ADTYED49"_3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
            {'key': 'YCLE B9MA H9PY GHU3 U7B5 HWW5 Y9JL KMPL NRSF 4ERM DXAU 2CSM GHTG L762 DK5Y HHF9 KJVT D5KM EFVW DT5J 89MK PZ2G 9K2P 3E22 MKYU 3UFZ TZZ7 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U \
            R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424863952 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR YHUAADTYEC5H"'},
            {'key': 'YCLC C9MA H9P9 8HW3 U7B5 HWW5 Y9JL KMPL LRGB 7ABQ DXAU 2CSM GHTG L762 QGFZ EEZM KJVT D5KM EFRW DS5R M94M N5KG 9K2P 3E22 AKYU LUV5 TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U \
            R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424864041 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR HY95ADTYTCHT"'}
            ]

cleanup_oa = [{'hostname': '10.145.1.21', 'username': 'Administrator', 'password': 'Cosmos123'},
              {'hostname': '10.145.2.21', 'username': 'Administrator', 'password': 'Cosmos123'},
              {'hostname': '10.145.3.21', 'username': 'Administrator', 'password': 'Cosmos123'}]

cleanup_ilo = [{'ilo': '10.145.1.31', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.32', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.33', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.34', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.35', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.36', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.37', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.38', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.39', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.40', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.1.41', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.2.31', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.2.32', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.2.34', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.2.35', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.2.36', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.31', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.32', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.33', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.34', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.35', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.36', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.37', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.145.3.38', 'username': 'Admin', 'password': 'Cosmos123'}]

cleanup_zone = [{'sanName': 'C7K-Auto-Reg-SW1-10:00:50:eb:1a:27:98:7a'},
                {'sanName': 'C7K-Auto-Reg-SW2-10:00:50:eb:1a:27:98:7b'},
                {'sanName': 'VSAN3205'},
                {'sanName': 'VSAN3206'}]

sans = [{'Type': 'Brocade Network Advisor',
         'Host': '10.120.1.75',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'Cosmos123', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '10.120.1.72',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'}]

ethernet_networks = [{'name': 'eth1', 'type': 'ethernet-networkV4', 'vlanId': 1146, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'eth2', 'type': 'ethernet-networkV4', 'vlanId': 1146, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'eth3', 'type': 'ethernet-networkV4', 'vlanId': 1146, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False},
                     {'name': 'eth4', 'type': 'ethernet-networkV4', 'vlanId': 1146, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False}]

fc_networks = [{'name': 'fc1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:C7K-Auto-Reg-SW1-10:00:50:eb:1a:27:98:7a', 'fabricType': 'FabricAttach'},
               {'name': 'fc2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:C7K-Auto-Reg-SW2-10:00:50:eb:1a:27:98:7b', 'fabricType': 'FabricAttach'},
               {'name': 'fc3', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:C7K-Auto-Reg-SW1-10:00:50:eb:1a:27:98:7a', 'fabricType': 'FabricAttach'},
               {'name': 'fc4', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:C7K-Auto-Reg-SW2-10:00:50:eb:1a:27:98:7b', 'fabricType': 'FabricAttach'}]

fcoe_networks = [{'name': 'fcoe1', 'type': 'fcoe-networkV4', 'vlanId': 3205, 'managedSanUri': 'FCSan:VSAN3205'},
                 {'name': 'fcoe2', 'type': 'fcoe-networkV4', 'vlanId': 3206, 'managedSanUri': 'FCSan:VSAN3206'},
                 {'name': 'fcoe3', 'type': 'fcoe-networkV4', 'vlanId': 3205, 'managedSanUri': 'FCSan:VSAN3205'},
                 {'name': 'fcoe4', 'type': 'fcoe-networkV4', 'vlanId': 3206, 'managedSanUri': 'FCSan:VSAN3206'}]

iscsi_networks = [{"vlanId": "1120", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI1", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"},
                  {"vlanId": "1120", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI2", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"}]

uplink_sets = {
    'lig1-fc1': {'name': 'lig1-fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc1'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
    'lig1-fc2': {'name': 'lig1-fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc2'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
    'lig1-eth1': {'name': 'lig1-eth1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth1'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]},
    'lig1-eth2': {'name': 'lig1-eth2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth2'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
    'lig1-fcoe1': {'name': 'lig1-fcoe1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe1'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
    'lig1-fcoe2': {'name': 'lig1-fcoe2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe2'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
    'lig1-iscsi1': {'name': 'lig1-iscsi1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['iSCSI1'],
                    'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X6', 'speed': 'Auto'}, {'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
    'lig1-fc3': {'name': 'lig1-fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc3'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},
    'lig1-fc4': {'name': 'lig1-fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc4'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '4', 'port': 'X2', 'speed': 'Auto'}]},
    'lig1-eth3': {'name': 'lig1-eth3', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth3'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]},
    'lig1-eth4': {'name': 'lig1-eth4', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth4'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '4', 'port': 'Q2.1', 'speed': 'Auto'}]},
    'lig1-fcoe3': {'name': 'lig1-fcoe3', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe3'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'}]},
    'lig1-fcoe4': {'name': 'lig1-fcoe4', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe4'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '4', 'port': 'X3', 'speed': 'Auto'}]},
    'lig2-fc1': {'name': 'lig2-fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc1'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
    'lig2-fc2': {'name': 'lig2-fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc2'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},
    'lig2-eth1': {'name': 'lig2-eth1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth1'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'}]},
    'lig2-eth2': {'name': 'lig2-eth2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth2'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}]},
    'lig2-fcoe1': {'name': 'lig2-fcoe1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe1'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
    'lig2-fcoe2': {'name': 'lig2-fcoe2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe2'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
    'lig2-fcoe3': {'name': 'lig2-fcoe3', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe3'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'}]},
    'lig2-fcoe4': {'name': 'lig2-fcoe4', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe4'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '4', 'port': 'X1', 'speed': 'Auto'}]},
    'lig2_iscsi1': {'name': 'lig2_iscsi1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['iSCSI1'],
                    'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': 'X5', 'speed': 'Auto'}, {'bay': '4', 'port': 'X5', 'speed': 'Auto'}]},
    'lig3-fc5': {'name': 'lig3-fc5', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc1'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
    'lig3-fc6': {'name': 'lig3-fc6', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc2'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},
    'lig3-eth1': {'name': 'lig3-eth1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth1'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}]},
    'lig3-eth2': {'name': 'lig3-eth2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth2'],
                  'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
    'lig3-fcoe1': {'name': 'lig3-fcoe1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe1'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
    'lig3-fcoe2': {'name': 'lig3-fcoe2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe2'],
                   'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
    'lig3-fc1': {'name': 'lig3-fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc1'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'}]},
    'lig3-fc2': {'name': 'lig3-fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc2'],
                 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '4', 'port': '1', 'speed': 'Auto'}]}, }

ligs = [{'name': 'lig1run1', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['lig1-fc1'].copy(), uplink_sets['lig1-fc2'].copy(),
                        uplink_sets['lig1-eth1'].copy(), uplink_sets['lig1-eth2'].copy(),
                        uplink_sets['lig1-fcoe1'].copy(), uplink_sets['lig1-fcoe2'].copy(), uplink_sets['lig1-iscsi1'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}, ], },
        {'name': 'lig1run2', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['lig1-fc3'].copy(), uplink_sets['lig1-fc4'].copy(),
                        uplink_sets['lig1-eth3'].copy(), uplink_sets['lig1-eth4'].copy(),
                        uplink_sets['lig1-fcoe3'].copy(), uplink_sets['lig1-fcoe4'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}], },
        {'name': 'lig2run1', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['lig2-fc1'].copy(), uplink_sets['lig2-fc2'].copy(),
                        uplink_sets['lig2-eth1'].copy(), uplink_sets['lig2-eth2'].copy(),
                        uplink_sets['lig2-fcoe1'].copy(), uplink_sets['lig2-fcoe2'].copy(), ],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1}, ]},
        {'name': 'lig2run2', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['lig2-fcoe3'].copy(), uplink_sets['lig2-fcoe4'].copy(), uplink_sets['lig2_iscsi1'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP VC Flex-10/10D Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC Flex-10/10D Module', 'enclosureIndex': 1}]},
        {'name': 'lig3run1', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['lig3-fc5'].copy(), uplink_sets['lig3-fc6'].copy(),
                        uplink_sets['lig3-eth1'].copy(), uplink_sets['lig3-eth2'].copy(),
                        uplink_sets['lig3-fcoe1'].copy(), uplink_sets['lig3-fcoe2'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module', 'enclosureIndex': 1}, ]},
        {'name': 'lig3run2', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         'description': None,
         'uplinkSets': [uplink_sets['lig3-fc1'].copy(), uplink_sets['lig3-fc2'].copy()],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'HP VC 16Gb 24-Port FC Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC 16Gb 24-Port FC Module', 'enclosureIndex': 1}, ]}]

expected_lig = [{'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'lig1run1', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:lig1run1',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'lig1run2', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:lig1run2',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'lig2run1', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:lig2run1',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'lig2run2', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:lig2run2',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'lig3run1', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:lig3run1',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'type': 'logical-interconnect-groupV7', 'enclosureType': 'C7000', 'enclosureIndexes': [1], 'name': 'lig3run2', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:lig3run2',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, }]

encgroups_add = [{'name': 'encgrp1', 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig1run1'},
                                                                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig1run1'},
                                                                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:lig1run2'},
                                                                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:lig1run2'}],
                  'configurationScript': '', 'ipAddressingMode': None, 'powerMode': None, 'ipRangeUris': [], 'enclosureCount': 1, 'osDeploymentSettings': None},
                 {'name': 'encgrp2', 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig2run1'},
                                                                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig2run1'},
                                                                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:lig2run2'},
                                                                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:lig2run2'}],
                  'configurationScript': '', 'ipAddressingMode': None, 'powerMode': None, 'ipRangeUris': [], 'enclosureCount': 1, 'osDeploymentSettings': None},
                 {'name': 'encgrp3', 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig3run1'},
                                                                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig3run1'},
                                                                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:lig3run2'},
                                                                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:lig3run2'}, ],
                  'configurationScript': '', 'ipAddressingMode': None, 'powerMode': None, 'ipRangeUris': [], 'enclosureCount': 1, 'osDeploymentSettings': None}]

logical_enclosure = [{'name': '2SN748014X', 'enclosureUris': ['ENC:2SN748014X'], 'enclosureGroupUri': 'EG:encgrp1'},
                     {'name': '2SN748014Y', 'enclosureUris': ['ENC:2SN748014Y'], 'enclosureGroupUri': 'EG:encgrp2'},
                     {'name': '2SN748014Z', 'enclosureUris': ['ENC:2SN748014Z'], 'enclosureGroupUri': 'EG:encgrp3'}]

logical_interconnect = [{"name": "2SN748014X-lig1"}, {"name": "2SN748014Y-lig2"}, {"name": "2SN748014Z-lig3"}]

update_logical_enclosure_from_group = [{"name": "2SN748014X"}, {"name": "2SN748014Y"}, {"name": "2SN748014Z"}]

storage_systems = [{'name': 'cosmos3par', 'family': 'StoreServ', "hostname": "10.120.1.77",
                    "credentials": {"username": "cosmos", "password": "Insight7"}, "serialNumber": "2M2620035D",
                    'deviceSpecificAttributes': {'managedDomain': 'Automation-C7K', 'managedPools': []}},
                   {'name': 'cosmos-vsa-cluster', 'family': 'StoreVirtual', "hostname": "10.120.0.204",
                    "credentials": {"username": "cosmosvsa", "password": "Cosmos123"},
                    "ports": [{"type": "StorageTargetPortV4", "name": "10.120.0.204", "address": "10.120.0.204", "expectedNetworkUri": "ETH:iSCSI1", "expectedNetworkName": "iSCSI1",
                               "expectedNetworkName": "iSCSI1", "mode": "Managed", "protocolType": "iSCSI"}]}]

storage_pools = [{"storageSystemUri": 'cosmos3par', "name": 'R1-Automation-CPG', "isManaged": True},
                 {"storageSystemUri": 'cosmos3par', "name": 'FC_r1', "isManaged": True}]

storage_volumes = [{"storageSystemUri": "cosmos3par", "name": "win2016_650_fc_vol_run1"}, {"storageSystemUri": "cosmos3par", "name": "win2016_650_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "Win2016_FC_630_Vol_Run1"}, {"storageSystemUri": "cosmos3par", "name": "Win2016_FC_630_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "Win2016_630_fcoe_vol_run1"}, {"storageSystemUri": "cosmos3par", "name": "Win2016_630_fcoe_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "Win2016_536_fcoe_vol_run1"}, {"storageSystemUri": "cosmos3par", "name": "Win2016_536_fcoe_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2016_fcoe_650_vol_run1"}, {"storageSystemUri": "cosmos3par", "name": "win2016_fcoe_650_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "esx67u1_536_fcoe_run1"}, {"storageSystemUri": "cosmos3par", "name": "esx67u1_536_fcoe_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "esx67u1_LPe1605_fc_run2"}, {"storageSystemUri": "cosmos3par", "name": "esx67u1_LPe1605_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "esx67u1_qmh2672_fc_run2"}, {"storageSystemUri": "cosmos3par", "name": "esx67u1_qmh2672_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "esx65u1_536_fcoe_run1"}, {"storageSystemUri": "cosmos3par", "name": "esx65u1_536_fcoe_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "rhel76_LPe1605_fc_run2"}, {"storageSystemUri": "cosmos3par", "name": "rhel76_LPe1605_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "rhel76_QMH2672_fc_run2"}, {"storageSystemUri": "cosmos3par", "name": "rhel76_QMH2672_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "sles15_LPe1605_fc_run2"}, {"storageSystemUri": "cosmos3par", "name": "sles15_LPe1605_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "sles15_QMH2672_fc_run2"}, {"storageSystemUri": "cosmos3par", "name": "sles15_QMH2672_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2012R2_650FLB_fc_run1"}, {"storageSystemUri": "cosmos3par", "name": "win2012R2_650FLB_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2012R2_536FLB_fc_run1"}, {"storageSystemUri": "cosmos3par", "name": "win2012R2_536FLB_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "esx65u2_536_fcoe_run1"}, {"storageSystemUri": "cosmos3par", "name": "esx65u2_536_fcoe_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2019_630_fc_vol_run_1"}, {"storageSystemUri": "cosmos3par", "name": "win2019_630_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "FCOE_Win2019_630_Run1_Vol"}, {"storageSystemUri": "cosmos3par", "name": "FCOE_Win2019_630_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2019_650_fc_vol_run_1"}, {"storageSystemUri": "cosmos3par", "name": "win2019_650_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2019_650_fcoe_vol_run_1"}, {"storageSystemUri": "cosmos3par", "name": "win2019_650_fcoe_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2019_lpe1605_fc_vol_run_2"}, {"storageSystemUri": "cosmos3par", "name": "win2019_lpe1605_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2019_qmh2672_fc_run_2"}, {"storageSystemUri": "cosmos3par", "name": "win2019_qmh2672_fc_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "win2019_536_fcoe_vol_run_1"}, {"storageSystemUri": "cosmos3par", "name": "win2019_536_fcoe_vol2"},
                   {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2019_630_iscsi_run_1"}, {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2019_630_iscsi_vol2"},
                   {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2019_650_iscsi_run_1"}, {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2019_650_iscsi_vol2"},
                   {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2016_650_iscsi_run_1"}, {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2016_650_iscsi_vol2"},
                   {"storageSystemUri": "cosmos3par", "name": "esx60u3_536_fcoe_run1"}, {"storageSystemUri": "cosmos3par", "name": "esx60u3_536_fcoe_vol2"}]

encl_names_firmware_update = [{'name': '2SN748014X'}, {'name': '2SN748014Y'}, {'name': '2SN748014Z'}]

encl = [{"enclosureGroupUri": "EG:encgrp1", "name": "2SN748014X", "hostname": "10.145.1.21", "username": "Administrator", "password": "Cosmos123",
         "licensingIntent": "OneViewNoiLO", "updateFirmwareOn": None, 'firmwareBaselineUri': None, "forceInstallFirmware": False, "force": True},
        {"enclosureGroupUri": "EG:encgrp2", "name": "2SN748014Y", "hostname": "10.145.2.21", "username": "Administrator", "password": "Cosmos123",
         "licensingIntent": "OneViewNoiLO", 'firmwareBaselineUri': None, "updateFirmwareOn": None, "forceInstallFirmware": False, "force": True},
        {"enclosureGroupUri": "EG:encgrp3", "name": "2SN748014Z", "hostname": "10.145.3.21", "username": "Administrator", "password": "Cosmos123",
         "licensingIntent": "OneViewNoiLO", 'firmwareBaselineUri': None, "updateFirmwareOn": None, "forceInstallFirmware": False, "force": True}]

custom_spp = {"baselineUri": "/rest/firmware-drivers/{baseSPPName}",
              "hotfixUris": ["/rest/firmware-drivers/{hotfixName2}"],
              "customBaselineName": "5_00"}

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

efuse_interconnect_a_side = [{'host': '10.145.1.22', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 1, 'inter_name': '2SN748014X, interconnect 1'},
                             {'host': '10.145.1.22', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 3, 'inter_name': '2SN748014X, interconnect 3'},
                             {'host': '10.145.2.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 1, 'inter_name': '2SN748014Y, interconnect 1'},
                             {'host': '10.145.2.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 3, 'inter_name': '2SN748014Y, interconnect 3'},
                             {'host': '10.145.3.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 1, 'inter_name': '2SN748014Z, interconnect 1'},
                             {'host': '10.145.3.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 3, 'inter_name': '2SN748014Z, interconnect 3'}]

efuse_interconnect_b_side = [{'host': '10.145.1.22', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 2, 'inter_name': '2SN748014X, interconnect 2'},
                             {'host': '10.145.1.22', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 4, 'inter_name': '2SN748014X, interconnect 4'},
                             {'host': '10.145.2.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 2, 'inter_name': '2SN748014Y, interconnect 2'},
                             {'host': '10.145.2.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 4, 'inter_name': '2SN748014Y, interconnect 4'},
                             {'host': '10.145.3.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 2, 'inter_name': '2SN748014Z, interconnect 2'},
                             {'host': '10.145.3.21', 'user': 'Administrator', 'password': 'Cosmos123', 'device': 'INTERCONNECT', 'bay_number': 4, 'inter_name': '2SN748014Z, interconnect 4'}]

failure_uplink = {'interconnect_a_side': [{"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig1-fcoe1", "interconnectName": "2SN748014X, interconnect 1",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig1-eth1", "interconnectName": "2SN748014X, interconnect 1",
                                           "portId": "X5", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "lig1-iscsi1", "interconnectName": "2SN748014X, interconnect 1",
                                           "portId": "X6", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X6"},
                                          {"associatedUplinkSetUri": "lig1-eth3", "interconnectName": "2SN748014X, interconnect 3",
                                           "portId": "Q1.1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q1.1"},
                                          {"associatedUplinkSetUri": "lig1-fc3", "interconnectName": "2SN748014X, interconnect 3",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig1-fcoe3", "interconnectName": "2SN748014X, interconnect 3",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig2-eth1", "interconnectName": "2SN748014Y, interconnect 1",
                                           "portId": "Q1.1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q1.1"},
                                          {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 1",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig2-fcoe1", "interconnectName": "2SN748014Y, interconnect 1",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig2-fcoe3", "interconnectName": "2SN748014Y, interconnect 3",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig2_iscsi1", "interconnectName": "2SN748014Y, interconnect 3",
                                           "portId": "X5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig3-fcoe1", "interconnectName": "2SN748014Z, interconnect 1",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig3-eth1", "interconnectName": "2SN748014Z, interconnect 1",
                                           "portId": "X5", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                           "portId": "1", "capability": ["FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "1"}],
                  'interconnect_b_side': [{"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                           "portId": "X2", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X2"},
                                          {"associatedUplinkSetUri": "lig1-fcoe2", "interconnectName": "2SN748014X, interconnect 2",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig1-iscsi1", "interconnectName": "2SN748014X, interconnect 2",
                                           "portId": "X5", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "lig1-eth2", "interconnectName": "2SN748014X, interconnect 2",
                                           "portId": "X6", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X6"},
                                          {"associatedUplinkSetUri": "lig1-eth4", "interconnectName": "2SN748014X, interconnect 4",
                                           "portId": "Q2.1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q2.1"},
                                          {"associatedUplinkSetUri": "lig1-fc4", "interconnectName": "2SN748014X, interconnect 4",
                                           "portId": "X2", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X2"},
                                          {"associatedUplinkSetUri": "lig1-fcoe4", "interconnectName": "2SN748014X, interconnect 4",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig2-eth2", "interconnectName": "2SN748014Y, interconnect 2",
                                           "portId": "Q2.1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q2.1"},
                                          {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 2",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig2-fcoe2", "interconnectName": "2SN748014Y, interconnect 2",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig2-fcoe4", "interconnectName": "2SN748014Y, interconnect 4",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig2_iscsi1", "interconnectName": "2SN748014Y, interconnect 4",
                                           "portId": "X5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                           "portId": "X1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "X1"},
                                          {"associatedUplinkSetUri": "lig3-fcoe2", "interconnectName": "2SN748014Z, interconnect 2",
                                           "portId": "X3", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "X3"},
                                          {"associatedUplinkSetUri": "lig3-eth2", "interconnectName": "2SN748014Z, interconnect 2",
                                           "portId": "X5", "capability": ["Ethernet"], "configPortTypes": ["Ethernet"], "portName": "X5"},
                                          {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                           "portId": "1", "capability": ["FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "1"}]}

interconnect_aside_disable = DD.make_uplink_disable(failure_uplink['interconnect_a_side'], critical)
interconnect_aside_enable = DD.make_uplink_enable(failure_uplink['interconnect_a_side'], ok)
interconnect_bside_disable = DD.make_uplink_disable(failure_uplink['interconnect_b_side'], critical)
interconnect_bside_enable = DD.make_uplink_enable(failure_uplink['interconnect_b_side'], ok)

run1_failure_downlink = {'interconnect_a_side': [{"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d7", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d8", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d8"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 1",
                                                  "portId": "d11", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d11"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d7", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d8", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d8"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                 {"associatedUplinkSetUri": "lig1-fc1", "interconnectName": "2SN748014X, interconnect 3",
                                                  "portId": "d11", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d11"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 1",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 1",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 1",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 1",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 1",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 3",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 3",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 3",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 3",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig2-fc1", "interconnectName": "2SN748014Y, interconnect 3",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"}],
                         'interconnect_b_side': [{"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d7", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d8", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d8"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 2",
                                                  "portId": "d11", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d11"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d7", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d8", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d8"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d9", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d9"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d10", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d10"},
                                                 {"associatedUplinkSetUri": "lig1-fc2", "interconnectName": "2SN748014X, interconnect 4",
                                                  "portId": "d11", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d11"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 2",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 2",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 2",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 2",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 2",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 4",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 4",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 4",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 4",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig2-fc2", "interconnectName": "2SN748014Y, interconnect 4",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"}]}

run1_interconnect_down_aside_disable = DD.make_downlink_disable(run1_failure_downlink['interconnect_a_side'], critical)
run1_interconnect_down_aside_enable = DD.make_downlink_enable(run1_failure_downlink['interconnect_a_side'], ok)
run1_interconnect_down_bside_disable = DD.make_downlink_disable(run1_failure_downlink['interconnect_b_side'], critical)
run1_interconnect_down_bside_enable = DD.make_downlink_enable(run1_failure_downlink['interconnect_b_side'], ok)

run2_failure_downlink = {'interconnect_a_side': [{"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d7", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig3-fc5", "interconnectName": "2SN748014Z, interconnect 1",
                                                  "portId": "d8", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d8"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d1", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d2", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d3", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d4", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d5", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d6", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d7", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig3-fc1", "interconnectName": "2SN748014Z, interconnect 3",
                                                  "portId": "d8", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d8"}],
                         'interconnect_b_side': [{"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d5", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d6", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d7", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig3-fc6", "interconnectName": "2SN748014Z, interconnect 2",
                                                  "portId": "d8", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "d8"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d1", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d1"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d2", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d2"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d3", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d3"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d4", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d4"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d5", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d5"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d6", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d6"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d7", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d7"},
                                                 {"associatedUplinkSetUri": "lig3-fc2", "interconnectName": "2SN748014Z, interconnect 4",
                                                  "portId": "d8", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                                  "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "d8"}]}

run2_interconnect_down_aside_disable = DD.make_downlink_disable(run2_failure_downlink['interconnect_a_side'], critical)
run2_interconnect_down_aside_enable = DD.make_downlink_enable(run2_failure_downlink['interconnect_a_side'], ok)
run2_interconnect_down_bside_disable = DD.make_downlink_disable(run2_failure_downlink['interconnect_b_side'], critical)
run2_interconnect_down_bside_enable = DD.make_downlink_enable(run2_failure_downlink['interconnect_b_side'], ok)

############################################################################################
# ESX6.7U1_LPe1605_FC
############################################################################################
esx67u1_LPe1605_fc_run2_profile_data = [{'name': 'esx67u1_LPe1605_fc_run2', 'serverHardwareUri': 'SH:2SN748014Z, bay 8', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                 'mac': '3E:B5:AE:50:00:14',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                 'mac': '3E:B5:AE:50:00:15',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                 'mac': '3E:B5:AE:50:00:16',
                                                                                 'macType': 'UserDefined', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary',
                                                                                                                                            'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                 'mac': '3E:B5:AE:50:00:17',
                                                                                 'macType': 'UserDefined', "networkUri": "FC:fc2",
                                                                                 "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
                                         "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx67u1_LPe1605_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esx67u1_LPe1605_fc_run2_profile_data = DD.make_server_profile_data(esx67u1_LPe1605_fc_run2_profile_data, firmware)
esx67u1_LPe1605_fc_run2_profile_data_expected = DD.make_expected_server_profile_data(esx67u1_LPe1605_fc_run2_profile_data, firmware)
esx67u1_LPe1605_fc_run2_profile_add_volume_data = copy.deepcopy(esx67u1_LPe1605_fc_run2_profile_data)
esx67u1_LPe1605_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(esx67u1_LPe1605_fc_run2_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:esx67u1_LPe1605_fc_vol2")
esx67u1_LPe1605_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(esx67u1_LPe1605_fc_run2_profile_add_volume_data, firmware)
esx67u1_LPe1605_fc_run2_profile_update_spp = DD.make_server_profile_data(esx67u1_LPe1605_fc_run2_profile_add_volume_data, update_firmware)
esx67u1_LPe1605_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(esx67u1_LPe1605_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# ESX6.7U1_536_FCOE
############################################################################################
esx67u1_536_fcoe_run1_profile_data = [{'name': 'esx67u1_536_fcoe_run1', 'serverHardwareUri': 'SH:2SN748014Y, bay 5', 'enclosureGroupUri': 'EG:encgrp2', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:08',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:09',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:0A',
                                                                               'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:0B',
                                                                               'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                               "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                       "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx67u1_536_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4,
                                                                                                                                                                "targetSelector": "Auto"}]}]}}]

esx67u1_536_fcoe_run1_profile_data = DD.make_server_profile_data(esx67u1_536_fcoe_run1_profile_data, firmware)
esx67u1_536_fcoe_run1_profile_data_expected = DD.make_expected_server_profile_data(esx67u1_536_fcoe_run1_profile_data, firmware)
esx67u1_536_fcoe_run1_profile_add_volume_data = copy.deepcopy(esx67u1_536_fcoe_run1_profile_data)
esx67u1_536_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esx67u1_536_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:esx67u1_536_fcoe_vol2")
esx67u1_536_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esx67u1_536_fcoe_run1_profile_add_volume_data, firmware)
esx67u1_536_fcoe_run1_profile_update_spp = DD.make_server_profile_data(esx67u1_536_fcoe_run1_profile_add_volume_data, update_firmware)
esx67u1_536_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(esx67u1_536_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
#  Win2012R2_536Flb_FC_Run1 profile test data for gen10 server 536FLB. OS is Win 2012 R2
############################################################################################

win2012r2_536flb_fc_run1_profile_data = [{'name': 'Win2012R2_536Flb_FC_Run1', 'serverHardwareUri': 'SH:2SN748014Y, bay 2', 'enclosureGroupUri': 'EG:encgrp2', 'description': '', 'affinity': 'Bay',
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:30',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:31',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                  'networkUri': 'FC:fc1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                                  "networkUri": "FC:fc2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2012R2_536FLB_fc_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2012r2_536flb_fc_run1_profile = DD.make_server_profile_data(win2012r2_536flb_fc_run1_profile_data, firmware)
win2012r2_536flb_fc_run1_profile_expected = DD.make_expected_server_profile_data(win2012r2_536flb_fc_run1_profile_data, firmware)
win2012r2_536flb_fc_run1_profile_add_volume_data = copy.deepcopy(win2012r2_536flb_fc_run1_profile_data)
win2012r2_536flb_fc_run1_profile_add_volume = DD.make_server_profile_add_volume_data(win2012r2_536flb_fc_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2012R2_536FLB_fc_vol2")
win2012r2_536flb_fc_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2012r2_536flb_fc_run1_profile_add_volume_data, firmware)
win2012r2_536flb_fc_run1_profile_update_spp = DD.make_server_profile_data(win2012r2_536flb_fc_run1_profile_add_volume_data, update_firmware)
win2012r2_536flb_fc_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2012r2_536flb_fc_run1_profile_add_volume_data, update_firmware)

############################################################################################
#  Win2012R2_650Flb_FC_Run1 profile test data for gen10 server 650FLB. OS is Win 2012 R2
############################################################################################

win2012r2_650flb_fc_run1_profile_data = [{'name': 'Win2012R2_650Flb_FC_Run1', 'serverHardwareUri': 'SH:2SN748014Y, bay 1', 'enclosureGroupUri': 'EG:encgrp2', 'description': '', 'affinity': 'Bay',
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:2C',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:2D',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                  'networkUri': 'FC:fc1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                                  "networkUri": "FC:fc2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2012R2_650FLB_fc_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2012r2_650flb_fc_run1_profile = DD.make_server_profile_data(win2012r2_650flb_fc_run1_profile_data, firmware)
win2012r2_650flb_fc_run1_profile_expected = DD.make_expected_server_profile_data(win2012r2_650flb_fc_run1_profile_data, firmware)
win2012r2_650flb_fc_run1_profile_add_volume_data = copy.deepcopy(win2012r2_650flb_fc_run1_profile_data)
win2012r2_650flb_fc_run1_profile_add_volume = DD.make_server_profile_add_volume_data(win2012r2_650flb_fc_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2012R2_650FLB_fc_vol2")
win2012r2_650flb_fc_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2012r2_650flb_fc_run1_profile_add_volume_data, firmware)
win2012r2_650flb_fc_run1_profile_update_spp = DD.make_server_profile_data(win2012r2_650flb_fc_run1_profile_add_volume_data, update_firmware)
win2012r2_650flb_fc_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2012r2_650flb_fc_run1_profile_add_volume_data, update_firmware)

############################################################################################
#  Rhel76_LPe1605_FC_Run2 profile test data for gen10 server LPe1605. OS is RHEL 7.6
############################################################################################

rhel76_LPe1605_fc_run2_profile_data = [{'name': 'Rhel76_LPe1605_FC_Run2', 'serverHardwareUri': 'SH:2SN748014Z, bay 3', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:24',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:25',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_LPe1605_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_LPe1605_fc_run2_profile = DD.make_server_profile_data(rhel76_LPe1605_fc_run2_profile_data, firmware)
rhel76_LPe1605_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_LPe1605_fc_run2_profile_data, firmware)
rhel76_LPe1605_fc_run2_profile_add_volume_data = copy.deepcopy(rhel76_LPe1605_fc_run2_profile_data)
rhel76_LPe1605_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_LPe1605_fc_run2_profile_add_volume_data, firmware, "SSYS:cosmos3par", "SVOL:rhel76_LPe1605_fc_vol2")
rhel76_LPe1605_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_LPe1605_fc_run2_profile_add_volume_data, firmware)
rhel76_LPe1605_fc_run2_profile_update_spp = DD.make_server_profile_data(rhel76_LPe1605_fc_run2_profile_add_volume_data, update_firmware)
rhel76_LPe1605_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_LPe1605_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
#  Rhel76_QMH2672_FC_Run2 profile test data for gen10 server QMH2672. OS is RHEL 7.6
############################################################################################

rhel76_QMH2672_fc_run2_profile_data = [{'name': 'RHEL76_QMH2672_FC_Run2', 'serverHardwareUri': 'SH:2SN748014Z, bay 4', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:28',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:29',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP QMH2672 16Gb FC HBA for BladeSystem c-Class',
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76_QMH2672_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel76_QMH2672_fc_run2_profile = DD.make_server_profile_data(rhel76_QMH2672_fc_run2_profile_data, firmware)
rhel76_QMH2672_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_QMH2672_fc_run2_profile_data, firmware)
rhel76_QMH2672_fc_run2_profile_add_volume_data = copy.deepcopy(rhel76_QMH2672_fc_run2_profile_data)
rhel76_QMH2672_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_QMH2672_fc_run2_profile_add_volume_data, firmware, "SSYS:cosmos3par", "SVOL:rhel76_QMH2672_fc_vol2")
rhel76_QMH2672_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_QMH2672_fc_run2_profile_add_volume_data, firmware)
rhel76_QMH2672_fc_run2_profile_update_spp = DD.make_server_profile_data(rhel76_QMH2672_fc_run2_profile_add_volume_data, update_firmware)
rhel76_QMH2672_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(rhel76_QMH2672_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
#  Sles15_QMH2672_FC_Run2 profile test data for gen10 server QMH2672. OS is Sles 15
############################################################################################

sles15_QMH2672_fc_run2_profile_data = [{'name': 'Sles15_QMH2672_FC_Run2', 'serverHardwareUri': 'SH:2SN748014Z, bay 5', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:20',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:21',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP QMH2672 16Gb FC HBA for BladeSystem c-Class',
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:sles15_QMH2672_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

sles15_QMH2672_fc_run2_profile = DD.make_server_profile_data(sles15_QMH2672_fc_run2_profile_data, firmware)
sles15_QMH2672_fc_run2_profile_expected = DD.make_expected_server_profile_data(sles15_QMH2672_fc_run2_profile_data, firmware)
sles15_QMH2672_fc_run2_profile_add_volume_data = copy.deepcopy(sles15_QMH2672_fc_run2_profile_data)
sles15_QMH2672_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(sles15_QMH2672_fc_run2_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:sles15_QMH2672_fc_vol2")
sles15_QMH2672_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(sles15_QMH2672_fc_run2_profile_add_volume_data, firmware)
sles15_QMH2672_fc_run2_profile_update_spp = DD.make_server_profile_data(sles15_QMH2672_fc_run2_profile_add_volume_data, update_firmware)
sles15_QMH2672_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(sles15_QMH2672_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
#  Sles15_LPe1605_FC_Run2 profile test data for gen10 server LPe1605. OS is Sles 15
############################################################################################

sles15_LPe1605_fc_run2_profile_data = [{'name': 'Sles15_LPe1605_FC_Run2', 'serverHardwareUri': 'SH:2SN748014Z, bay 6', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:6C',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:6D',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:sles15_LPe1605_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

sles15_LPe1605_fc_run2_profile = DD.make_server_profile_data(sles15_LPe1605_fc_run2_profile_data, firmware)
sles15_LPe1605_fc_run2_profile_expected = DD.make_expected_server_profile_data(sles15_LPe1605_fc_run2_profile_data, firmware)
sles15_LPe1605_fc_run2_profile_add_volume_data = copy.deepcopy(sles15_LPe1605_fc_run2_profile_data)
sles15_LPe1605_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(sles15_LPe1605_fc_run2_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:sles15_LPe1605_fc_vol2")
sles15_LPe1605_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(sles15_LPe1605_fc_run2_profile_add_volume_data, firmware)
sles15_LPe1605_fc_run2_profile_update_spp = DD.make_server_profile_data(sles15_LPe1605_fc_run2_profile_add_volume_data, update_firmware)
sles15_LPe1605_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(sles15_LPe1605_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# Run1 Test Case with 650 FLB. OS is windows 2016
############################################################################################

win2016_fcoe_650_run1_data = [{'name': 'win2016_fcoe_650_run1', 'serverHardwareUri': 'SH:2SN748014X, bay 9', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                               'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                       'mac': '3E:B5:AE:50:00:44',
                                                                       'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                      {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                       'mac': '3E:B5:AE:50:00:45',
                                                                       'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                      {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000',
                                                                       'mac': '3E:B5:AE:50:00:46',
                                                                       'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1', "wwnn": "10:00:da:df:6a:20:00:4d",
                                                                       "wwpn": "10:00:da:df:6a:20:00:4c",
                                                                       'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                      {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000',
                                                                       'mac': '3E:B5:AE:50:00:47',
                                                                       'macType': 'UserDefined', "networkUri": "FCOE:fcoe2", "wwnn": "10:00:da:df:6a:20:00:4f",
                                                                       "wwpn": "10:00:da:df:6a:20:00:4e",
                                                                       "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                               'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                               "boot": {"order": ["HardDisk"], "manageBoot": True},
                               'bios': {'manageBios': False, 'overriddenSettings': []},
                               "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4"},
                               'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                               'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                               'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                             'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2016_fcoe_650_vol_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                    'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                     {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2016_fcoe_650_run1 = DD.make_server_profile_data(win2016_fcoe_650_run1_data, firmware)
win2016_fcoe_650_run1_expected = DD.make_expected_server_profile_data(win2016_fcoe_650_run1_data, firmware)
win2016_fcoe_650_run1_volume_data = copy.deepcopy(win2016_fcoe_650_run1_data)
win2016_fcoe_650_run1_volume_expected = DD.make_expected_server_profile_data(win2016_fcoe_650_run1_volume_data, firmware)
win2016_fcoe_650_run1_volume = DD.make_server_profile_add_volume_data(win2016_fcoe_650_run1_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2016_fcoe_650_vol2")
win2016_fcoe_650_run1_spp = DD.make_server_profile_data(win2016_fcoe_650_run1_volume_data, update_firmware)
win2016_fcoe_650_run1_spp_expected = DD.make_expected_server_profile_data(win2016_fcoe_650_run1_volume_data, update_firmware)

############################################################################################
# Run1 Test Case with 536 FLB. OS is windows 2016 and FCOE Connection
############################################################################################

win2016_536_fcoe_run1_data = [{'name': 'Win2016_536_FCOE_Run1', 'serverHardwareUri': 'SH:2SN748014Y, bay 4', 'enclosureGroupUri': 'EG:encgrp2', 'description': '', 'affinity': 'Bay',
                               'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                       'mac': '3E:B5:AE:50:00:5E',
                                                                       'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                      {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                       'mac': '3E:B5:AE:50:00:5F',
                                                                       'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                      {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000',
                                                                       'mac': '3E:B5:AE:50:00:60',
                                                                       'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1', "wwnn": "10:00:da:df:6a:20:00:71",
                                                                       "wwpn": "10:00:da:df:6a:20:00:70",
                                                                       'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                      {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000',
                                                                       'mac': '3E:B5:AE:50:00:61',
                                                                       'macType': 'UserDefined', "networkUri": "FCOE:fcoe2", "wwnn": "10:00:da:df:6a:20:00:73",
                                                                       "wwpn": "10:00:da:df:6a:20:00:72",
                                                                       "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                               'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter',
                               "boot": {"order": ["HardDisk"], "manageBoot": True},
                               'bios': {'manageBios': False, 'overriddenSettings': []},
                               "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4"},
                               'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                               'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                               'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                             'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Win2016_536_fcoe_vol_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                    'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                     {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2016_fcoe_536_run1 = DD.make_server_profile_data(win2016_536_fcoe_run1_data, firmware)
win2016_fcoe_536_run1_expected = DD.make_expected_server_profile_data(win2016_536_fcoe_run1_data, firmware)
win2016_fcoe_536_run1_volume_data = copy.deepcopy(win2016_536_fcoe_run1_data)
win2016_fcoe_536_run1_volume = DD.make_server_profile_add_volume_data(win2016_fcoe_536_run1_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:Win2016_536_fcoe_vol2")
win2016_fcoe_536_run1_spp = DD.make_server_profile_data(win2016_fcoe_536_run1_volume_data, update_firmware)
win2016_fcoe_536_run1_spp_expected = DD.make_expected_server_profile_data(win2016_fcoe_536_run1_volume_data, update_firmware)
win2016_fcoe_536_run1_volume_expected = DD.make_expected_server_profile_data(win2016_fcoe_536_run1_volume_data, firmware)

############################################################################################
# Run1 Test Case with 630 FLB. OS is windows 2016 with FCOE Connection
############################################################################################

win2016_630_fcoe_run1_data = [{'name': 'Win2016_630_FCOE_Run1', 'serverHardwareUri': 'SH:2SN748014X, bay 4', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                               'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                       'mac': '3E:B5:AE:50:00:34',
                                                                       'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                      {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                       'mac': '3E:B5:AE:50:00:35',
                                                                       'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                      {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000',
                                                                       'mac': '3E:B5:AE:50:00:36',
                                                                       'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1', "wwnn": "10:00:da:df:6a:20:00:3d",
                                                                       "wwpn": "10:00:da:df:6a:20:00:3c",
                                                                       'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                      {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000',
                                                                       'mac': '3E:B5:AE:50:00:37',
                                                                       'macType': 'UserDefined', "networkUri": "FCOE:fcoe2", "wwnn": "10:00:da:df:6a:20:00:3f",
                                                                       "wwpn": "10:00:da:df:6a:20:00:3e",
                                                                       "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                               'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                               "boot": {"order": ["HardDisk"], "manageBoot": True},
                               'bios': {'manageBios': False, 'overriddenSettings': []},
                               "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4"},
                               'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                               'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                               'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                             'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Win2016_630_fcoe_vol_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                    'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                     {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2016_fcoe_630_run1 = DD.make_server_profile_data(win2016_630_fcoe_run1_data, firmware)
win2016_fcoe_630_run1_expected = DD.make_expected_server_profile_data(win2016_630_fcoe_run1_data, firmware)
win2016_fcoe_630_run1_volume_data = copy.deepcopy(win2016_630_fcoe_run1_data)
win2016_fcoe_630_run1_volume = DD.make_server_profile_add_volume_data(win2016_fcoe_630_run1_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:Win2016_630_fcoe_vol2")
win2016_fcoe_630_run1_spp = DD.make_server_profile_data(win2016_fcoe_630_run1_volume_data, update_firmware)
win2016_fcoe_630_run1_spp_expected = DD.make_expected_server_profile_data(win2016_fcoe_630_run1_volume_data, update_firmware)
win2016_fcoe_630_run1_volume_expected = DD.make_expected_server_profile_data(win2016_fcoe_630_run1_volume_data, firmware)

############################################################################################
# Run1 Test Case with 630 FLB with FC. OS is windows 2016
############################################################################################

win2016_fc_630_run1_data = [{'name': 'Win2016_FC_630_Run1', 'serverHardwareUri': 'SH:2SN748014X, bay 5', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                     'mac': '3E:B5:AE:50:00:40',
                                                                     'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                     'mac': '3E:B5:AE:50:00:41',
                                                                     'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000',
                                                                     'mac': '3E:B5:AE:50:00:42',
                                                                     'macType': 'UserDefined', 'networkUri': 'FC:fc1', "wwnn": "10:00:da:df:6a:20:00:49",
                                                                     "wwpn": "10:00:da:df:6a:20:00:48",
                                                                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000',
                                                                     'mac': '3E:B5:AE:50:00:43',
                                                                     'macType': 'UserDefined', "networkUri": "FC:fc2", "wwnn": "10:00:da:df:6a:20:00:4b",
                                                                     "wwpn": "10:00:da:df:6a:20:00:4a",
                                                                     "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                             'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                             "boot": {"order": ["HardDisk"], "manageBoot": True},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4"},
                             'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                             'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                             'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                           'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Win2016_FC_630_Vol_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                  'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                   {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2016_fc_630_run1 = DD.make_server_profile_data(win2016_fc_630_run1_data, firmware)
win2016_fc_630_run1_expected = DD.make_expected_server_profile_data(win2016_fc_630_run1_data, firmware)
win2016_fc_630_run1_volume_data = copy.deepcopy(win2016_fc_630_run1_data)
win2016_fc_630_run1_volume = DD.make_server_profile_add_volume_data(win2016_fc_630_run1_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:Win2016_FC_630_vol2")
win2016_fc_630_run1_spp = DD.make_server_profile_data(win2016_fc_630_run1_volume_data, update_firmware)
win2016_fc_630_run1_spp_expected = DD.make_expected_server_profile_data(win2016_fc_630_run1_volume_data, update_firmware)
win2016_fc_630_run1_volume_expected = DD.make_expected_server_profile_data(win2016_fc_630_run1_volume_data, firmware)

############################################################################################
# Run1 Test Case with 630 FLB. OS is windows 2016
############################################################################################

win2016_650_fc_run1_data = [{'name': 'win2016_650_fc_run1', 'serverHardwareUri': 'SH:2SN748014X, bay 10', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                             'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                     'mac': '3E:B5:AE:50:00:4C',
                                                                     'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                     'mac': '3E:B5:AE:50:00:4D', 'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '4000',
                                                                     'mac': '3E:B5:AE:50:00:4E',
                                                                     'macType': 'UserDefined', 'networkUri': 'FC:fc1', "wwnn": "10:00:da:df:6a:20:00:55",
                                                                     "wwpn": "10:00:da:df:6a:20:00:54",
                                                                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                    {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '4000',
                                                                     'mac': '3E:B5:AE:50:00:4F',
                                                                     'macType': 'UserDefined', "networkUri": "FC:fc2", "wwnn": "10:00:da:df:6a:20:00:57",
                                                                     "wwpn": "10:00:da:df:6a:20:00:56",
                                                                     "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                             'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                             "boot": {"order": ["HardDisk"], "manageBoot": True},
                             'bios': {'manageBios': False, 'overriddenSettings': []},
                             "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4"},
                             'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                             'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                             'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                           'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2016_650_fc_vol_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                  'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                   {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2016_650_fc_run1 = DD.make_server_profile_data(win2016_650_fc_run1_data, firmware)
win2016_650_fc_run1_expected = DD.make_expected_server_profile_data(win2016_650_fc_run1_data, firmware)
win2016_650_fc_run1_volume_data = copy.deepcopy(win2016_650_fc_run1_data)
win2016_650_fc_run1_volume = DD.make_server_profile_add_volume_data(win2016_650_fc_run1_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2016_650_fc_vol2")
win2016_650_fc_run1_spp = DD.make_server_profile_data(win2016_650_fc_run1_volume_data, update_firmware)
win2016_650_fc_run1_spp_expected = DD.make_expected_server_profile_data(win2016_650_fc_run1_volume_data, update_firmware)
win2016_650_fc_run1_volume_expected = DD.make_expected_server_profile_data(win2016_650_fc_run1_volume_data, firmware)

############################################################################################
# ESX6.7U1_QMH2672_FC
############################################################################################
esx67u1_qmh2672_fc_run2_profile_data = [{'name': 'esx67u1_qmh2672_fc_run2', 'serverHardwareUri': 'SH:2SN748014Z, bay 7', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                 'mac': '3E:B5:AE:50:00:70',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                 'mac': '3E:B5:AE:50:00:71',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                 'mac': '3E:B5:AE:50:00:72',
                                                                                 'macType': 'UserDefined', 'networkUri': 'FC:fc1',
                                                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                 'mac': '3E:B5:AE:50:00:73',
                                                                                 'macType': 'UserDefined', "networkUri": "FC:fc2",
                                                                                 "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP QMH2672 16Gb FC HBA for BladeSystem c-Class',
                                         "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx67u1_qmh2672_fc_run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esx67u1_qmh2672_fc_run2_profile_data = DD.make_server_profile_data(esx67u1_qmh2672_fc_run2_profile_data, firmware)
esx67u1_qmh2672_fc_run2_profile_data_expected = DD.make_expected_server_profile_data(esx67u1_qmh2672_fc_run2_profile_data, firmware)
esx67u1_qmh2672_fc_run2_profile_add_volume_data = copy.deepcopy(esx67u1_qmh2672_fc_run2_profile_data)
esx67u1_qmh2672_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(esx67u1_qmh2672_fc_run2_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:esx67u1_qmh2672_fc_vol2")
esx67u1_qmh2672_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(esx67u1_qmh2672_fc_run2_profile_add_volume_data, firmware)
esx67u1_qmh2672_fc_run2_profile_update_spp = DD.make_server_profile_data(esx67u1_qmh2672_fc_run2_profile_add_volume_data, update_firmware)
esx67u1_qmh2672_fc_run2_profile_update_spp_expected = DD.make_expected_server_profile_data(esx67u1_qmh2672_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# ESX6.5U2_536_FCOE
############################################################################################
esx65u2_536_fcoe_run1_profile_data = [{'name': 'esx65u2_536_fcoe_run1', 'serverHardwareUri': 'SH:2SN748014Y, bay 6', 'enclosureGroupUri': 'EG:encgrp2', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:74',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:75',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:76',
                                                                               'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:77',
                                                                               'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                               "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                       "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx65u2_536_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                             {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esx65u2_536_fcoe_run1_profile_data = DD.make_server_profile_data(esx65u2_536_fcoe_run1_profile_data, firmware)
esx65u2_536_fcoe_run1_profile_data_expected = DD.make_expected_server_profile_data(esx65u2_536_fcoe_run1_profile_data, firmware)
esx65u2_536_fcoe_run1_profile_add_volume_data = copy.deepcopy(esx65u2_536_fcoe_run1_profile_data)
esx65u2_536_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esx65u2_536_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:esx65u2_536_fcoe_vol2")
esx65u2_536_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esx65u2_536_fcoe_run1_profile_add_volume_data, firmware)
esx65u2_536_fcoe_run1_profile_update_spp = DD.make_server_profile_data(esx65u2_536_fcoe_run1_profile_add_volume_data, update_firmware)
esx65u2_536_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(esx65u2_536_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# ESX6.5U1_536_FCOE
############################################################################################
esx65u1_536_fcoe_run1_profile_data = [{'name': 'esx65u1_536_fcoe_run1', 'serverHardwareUri': 'SH:2SN748014Z, bay 1', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:84',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:85',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:86',
                                                                               'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:87',
                                                                               'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                               "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
                                       "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx65u1_536_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                             {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]
esx65u1_536_fcoe_run1_profile_data = DD.make_server_profile_data(esx65u1_536_fcoe_run1_profile_data, firmware)
esx65u1_536_fcoe_run1_profile_data_expected = DD.make_expected_server_profile_data(esx65u1_536_fcoe_run1_profile_data, firmware)
esx65u1_536_fcoe_run1_profile_add_volume_data = copy.deepcopy(esx65u1_536_fcoe_run1_profile_data)
esx65u1_536_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esx65u1_536_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:esx65u1_536_fcoe_vol2")
esx65u1_536_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esx65u1_536_fcoe_run1_profile_add_volume_data, firmware)
esx65u1_536_fcoe_run1_profile_update_spp = DD.make_server_profile_data(esx65u1_536_fcoe_run1_profile_add_volume_data, update_firmware)
esx65u1_536_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(esx65u1_536_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# ESX6.0U3_536_FCOE
############################################################################################
esx60u3_536_fcoe_run1_profile_data = [{'name': 'esx60u3_536_fcoe_run1', 'serverHardwareUri': 'SH:2SN748014Z, bay 2', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:94',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:95',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:96',
                                                                               'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:97',
                                                                               'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                               "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP QMH2672 16Gb FC HBA for BladeSystem c-Class',
                                       "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                       "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:esx60u3_536_fcoe_run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                             {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]
esx60u3_536_fcoe_run1_profile_data = DD.make_server_profile_data(esx60u3_536_fcoe_run1_profile_data, firmware)
esx60u3_536_fcoe_run1_profile_data_expected = DD.make_expected_server_profile_data(esx60u3_536_fcoe_run1_profile_data, firmware)
esx60u3_536_fcoe_run1_profile_add_volume_data = copy.deepcopy(esx60u3_536_fcoe_run1_profile_data)
esx60u3_536_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esx60u3_536_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:esx60u3_536_fcoe_vol2")
esx60u3_536_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esx60u3_536_fcoe_run1_profile_add_volume_data, firmware)
esx60u3_536_fcoe_run1_profile_update_spp = DD.make_server_profile_data(esx60u3_536_fcoe_run1_profile_add_volume_data, update_firmware)
esx60u3_536_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(esx60u3_536_fcoe_run1_profile_add_volume_data, update_firmware)

#########################################################################################################
#  win2019_630_fc_run_1 profile test data for fc connection with gen10 server 630FLB OS is Windows 2019
#########################################################################################################

win2019_630_fc_run_1_profile_data = [{'name': 'win2019_630_fc_run_1', 'serverHardwareUri': 'SH:2SN748014X, bay 2', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                              'mac': '3E:B5:AE:50:00:1C',
                                                                              'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                              'mac': '3E:B5:AE:50:00:1D',
                                                                              'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                              'networkUri': 'FC:fc1',
                                                                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                              "networkUri": "FC:fc2",
                                                                              "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter',
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_630_fc_vol_run_1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                            {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_630_fc_run_1_profile = DD.make_server_profile_data(win2019_630_fc_run_1_profile_data, firmware)
win2019_630_fc_run_1_profile_expected = DD.make_expected_server_profile_data(win2019_630_fc_run_1_profile_data, firmware)
win2019_630_fc_run_1_profile_add_volume_data = copy.deepcopy(win2019_630_fc_run_1_profile_data)
win2019_630_fc_run_1_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_630_fc_run_1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2019_630_fc_vol2")
win2019_630_fc_run_1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_630_fc_run_1_profile_add_volume_data, firmware)
win2019_630_fc_run_1_profile_update_spp = DD.make_server_profile_data(win2019_630_fc_run_1_profile_add_volume_data, update_firmware)
win2019_630_fc_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_630_fc_run_1_profile_add_volume_data, update_firmware)

############################################################################################################
#  win2019_630_fcoe_run1 profile test data for fcoe connection with gen10 server 630FLB OS is Windows 2019
############################################################################################################

win2019_630_fcoe_run1_profile_data = [{'name': 'win2019_630_fcoe_run1', 'serverHardwareUri': 'SH:2SN748014X, bay 1', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:00',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:01',
                                                                               'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:02',
                                                                               'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                               'mac': '3E:B5:AE:50:00:03',
                                                                               'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                               "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:FCOE_Win2019_630_Run1_Vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                             {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_630_fcoe_run1_profile = DD.make_server_profile_data(win2019_630_fcoe_run1_profile_data, firmware)
win2019_630_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(win2019_630_fcoe_run1_profile_data, firmware)
win2019_630_fcoe_run1_profile_add_volume_data = copy.deepcopy(win2019_630_fcoe_run1_profile_data)
win2019_630_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_630_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:FCOE_Win2019_630_vol2")
win2019_630_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_630_fcoe_run1_profile_add_volume_data, firmware)
win2019_630_fcoe_run1_profile_update_spp = DD.make_server_profile_data(win2019_630_fcoe_run1_profile_add_volume_data, update_firmware)
win2019_630_fcoe_run1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_630_fcoe_run1_profile_add_volume_data, update_firmware)

#########################################################################################################
#  win2019_650_fc_run_1 profile test data for fc connection with gen10 server 630FLB OS is Windows 2019
#########################################################################################################

win2019_650_fc_run_1_profile_data = [{'name': 'win2019_650_fc_run_1', 'serverHardwareUri': 'SH:2SN748014X, bay 7', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                              'mac': '3E:B5:AE:50:00:10',
                                                                              'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                              'mac': '3E:B5:AE:50:00:11',
                                                                              'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                             {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                              'networkUri': 'FC:fc1',
                                                                              'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                             {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                              "networkUri": "FC:fc2",
                                                                              "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                      "boot": {"order": ["HardDisk"], "manageBoot": True},
                                      'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter',
                                      'bios': {'manageBios': False, 'overriddenSettings': []},
                                      "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                      'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                      'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                      'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                    'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_650_fc_vol_run_1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                           'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                           'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                            {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_650_fc_run_1_profile = DD.make_server_profile_data(win2019_650_fc_run_1_profile_data, firmware)
win2019_650_fc_run_1_profile_expected = DD.make_expected_server_profile_data(win2019_650_fc_run_1_profile_data, firmware)
win2019_650_fc_run_1_profile_add_volume_data = copy.deepcopy(win2019_650_fc_run_1_profile_data)
win2019_650_fc_run_1_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_650_fc_run_1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2019_650_fc_vol2")
win2019_650_fc_run_1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_650_fc_run_1_profile_add_volume_data, firmware)
win2019_650_fc_run_1_profile_update_spp = DD.make_server_profile_data(win2019_650_fc_run_1_profile_add_volume_data, update_firmware)
win2019_650_fc_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_650_fc_run_1_profile_add_volume_data, update_firmware)

############################################################################################################
#  win2019_650_fcoe_run_1 profile test data for fcoe connection with gen10 server 650FLB OS is Windows 2019
############################################################################################################

win2019_650_fcoe_run_1_profile_data = [{'name': 'win2019_650_fcoe_run_1', 'serverHardwareUri': 'SH:2SN748014X, bay 6', 'enclosureGroupUri': 'EG:encgrp1', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:48',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:49',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:4A',
                                                                                'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:4B',
                                                                                'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_650_fcoe_vol_run_1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_650_fcoe_run_1_profile = DD.make_server_profile_data(win2019_650_fcoe_run_1_profile_data, firmware)
win2019_650_fcoe_run_1_profile_expected = DD.make_expected_server_profile_data(win2019_650_fcoe_run_1_profile_data, firmware)
win2019_650_fcoe_run_1_profile_add_volume_data = copy.deepcopy(win2019_650_fcoe_run_1_profile_data)
win2019_650_fcoe_run_1_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_650_fcoe_run_1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2019_650_fcoe_vol2")
win2019_650_fcoe_run_1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_650_fcoe_run_1_profile_add_volume_data, firmware)
win2019_650_fcoe_run_1_profile_update_spp = DD.make_server_profile_data(win2019_650_fcoe_run_1_profile_add_volume_data, update_firmware)
win2019_650_fcoe_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_650_fcoe_run_1_profile_add_volume_data, update_firmware)

##############################################################################################################
#  win2019_lpe1605_fc_run_2 profile test data for fc connection with gen10 server LPe1605 OS is Windows 2019
##############################################################################################################

win2019_lpe1605_fc_run_2_profile_data = [{'name': 'win2019_lpe1605_fc_run_2', 'serverHardwareUri': 'SH:2SN748014Z, bay 1', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:38',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:39',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                  'networkUri': 'FC:fc1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                  "networkUri": "FC:fc2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_lpe1605_fc_vol_run_2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_lpe1605_fc_run_2_profile = DD.make_server_profile_data(win2019_lpe1605_fc_run_2_profile_data, firmware)
win2019_lpe1605_fc_run_2_profile_expected = DD.make_expected_server_profile_data(win2019_lpe1605_fc_run_2_profile_data, firmware)
win2019_lpe1605_fc_run_2_profile_add_volume_data = copy.deepcopy(win2019_lpe1605_fc_run_2_profile_data)
win2019_lpe1605_fc_run_2_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_lpe1605_fc_run_2_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2019_lpe1605_fc_vol2")
win2019_lpe1605_fc_run_2_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_lpe1605_fc_run_2_profile_add_volume_data, firmware)
win2019_lpe1605_fc_run_2_profile_update_spp = DD.make_server_profile_data(win2019_lpe1605_fc_run_2_profile_add_volume_data, update_firmware)
win2019_lpe1605_fc_run_2_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_lpe1605_fc_run_2_profile_add_volume_data, update_firmware)

##############################################################################################################
#  win2019_qmh2672_fc_run_2 profile test data for fc connection with gen10 server qmh2672 OS is Windows 2019
##############################################################################################################

win2019_qmh2672_fc_run_2_profile_data = [{'name': 'win2019_qmh2672_fc_run_2', 'serverHardwareUri': 'SH:2SN748014Z, bay 2', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:3C',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '3E:B5:AE:50:00:3D',
                                                                                  'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                                  'networkUri': 'FC:fc1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'requestedMbps': 'Auto',
                                                                                  "networkUri": "FC:fc2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP QMH2672 16Gb FC HBA for BladeSystem c-Class',
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_qmh2672_fc_run_2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_qmh2672_fc_run_2_profile = DD.make_server_profile_data(win2019_qmh2672_fc_run_2_profile_data, firmware)
win2019_qmh2672_fc_run_2_profile_expected = DD.make_expected_server_profile_data(win2019_qmh2672_fc_run_2_profile_data, firmware)
win2019_qmh2672_fc_run_2_profile_add_volume_data = copy.deepcopy(win2019_qmh2672_fc_run_2_profile_data)
win2019_qmh2672_fc_run_2_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_qmh2672_fc_run_2_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2019_qmh2672_fc_vol2")
win2019_qmh2672_fc_run_2_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_qmh2672_fc_run_2_profile_add_volume_data, firmware)
win2019_qmh2672_fc_run_2_profile_update_spp = DD.make_server_profile_data(win2019_qmh2672_fc_run_2_profile_add_volume_data, update_firmware)
win2019_qmh2672_fc_run_2_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_qmh2672_fc_run_2_profile_add_volume_data, update_firmware)

##############################################################################################################
#  win2019_536_fcoe_run_1 profile test data for fcoe connection with gen10 server 536FLB OS is Windows 2019
##############################################################################################################

win2019_536_fcoe_run_1_profile_data = [{'name': 'win2019_536_fcoe_run1', 'serverHardwareUri': 'SH:2SN748014Z, bay 4', 'enclosureGroupUri': 'EG:encgrp3', 'description': '', 'affinity': 'Bay',
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:50',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:51',
                                                                                'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:52',
                                                                                'macType': 'UserDefined', 'networkUri': 'FCOE:fcoe1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Flb 1:2-b", 'requestedMbps': '2500',
                                                                                'mac': '3E:B5:AE:50:00:53',
                                                                                'macType': 'UserDefined', "networkUri": "FCOE:fcoe2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP QMH2672 16Gb FC HBA for BladeSystem c-Class',
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_536_fcoe_vol_run_1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'volumeStorageSystemUri': 'SSYS:cosmos3par',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_536_fcoe_run_1_profile = DD.make_server_profile_data(win2019_536_fcoe_run_1_profile_data, firmware)
win2019_536_fcoe_run_1_profile_expected = DD.make_expected_server_profile_data(win2019_536_fcoe_run_1_profile_data, firmware)
win2019_536_fcoe_run_1_profile_add_volume_data = copy.deepcopy(win2019_536_fcoe_run_1_profile_data)
win2019_536_fcoe_run_1_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_536_fcoe_run_1_profile_add_volume_data, firmware, 'SSYS:cosmos3par', "SVOL:win2019_536_fcoe_vol2")
win2019_536_fcoe_run_1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_536_fcoe_run_1_profile_add_volume_data, firmware)
win2019_536_fcoe_run_1_profile_update_spp = DD.make_server_profile_data(win2019_536_fcoe_run_1_profile_add_volume_data, update_firmware)
win2019_536_fcoe_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_536_fcoe_run_1_profile_add_volume_data, update_firmware)

##############################################################################################################
#  win2019_630_iscsi_run_1 profile test data for iscsi connection with gen10 server 630FLB OS is Windows 2019
##############################################################################################################

win2019_630_iscsi_run_1_profile_data = [{'name': 'win2019_630_iscsi_run_1', 'serverHardwareUri': 'SH:2SN748014X, bay 3', 'enclosureGroupUri': 'EG:encgrp1',
                                         "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgzrvq025",
                                         "iscsiInitiatorNameType": "UserDefined", 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                 'mac': '3A:1F:9D:60:00:4B',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                 'mac': '3A:1F:9D:60:00:4C',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                 'networkUri': 'ETH:iSCSI1',
                                                                                 "ipv4": {"ipAddressSource": "DHCP"},
                                                                                 "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                                                                                 "networkUri": "ETH:iSCSI1",
                                                                                 "ipv4": {"ipAddressSource": "DHCP"},
                                                                                 "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 630FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_630_iscsi_run_1", 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:cosmos-vsa-cluster', 'bootVolumePriority': 'Primary',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]
win2019_630_iscsi_run_1_profile = DD.make_server_profile_data(win2019_630_iscsi_run_1_profile_data, firmware)
win2019_630_iscsi_run_1_profile_expected = DD.make_expected_server_profile_data(win2019_630_iscsi_run_1_profile_data, firmware)
win2019_630_iscsi_run_1_profile_update_spp = DD.make_server_profile_data(win2019_630_iscsi_run_1_profile_data, update_firmware)
win2019_630_iscsi_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_630_iscsi_run_1_profile_data, update_firmware)


##############################################################################################################
#  win2019_650_iscsi_run_1 profile test data for iscsi connection with gen10 server 650FLB OS is Windows 2019
##############################################################################################################

win2019_650_iscsi_run_1_profile_data = [{'name': 'win2019_650_iscsi_run_1', 'serverHardwareUri': 'SH:2SN748014X, bay 8', 'enclosureGroupUri': 'EG:encgrp1',
                                         "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcg5ksf01c",
                                         "iscsiInitiatorNameType": "UserDefined", 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                 'mac': 'FE:13:83:30:00:1E',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                 'mac': 'FE:13:83:30:00:1F',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                 'mac': 'FE:13:83:30:00:20',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:iSCSI1', "ipv4": {"ipAddressSource": "DHCP"},
                                                                                 "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                                                                                 'mac': 'FE:13:83:30:00:21',
                                                                                 'macType': 'UserDefined', "networkUri": "ETH:iSCSI1", "ipv4": {"ipAddressSource": "DHCP"},
                                                                                 "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 650M Adapter',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019_650_iscsi_run_1", 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:cosmos-vsa-cluster', 'bootVolumePriority': 'Primary',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]
win2019_650_iscsi_run_1_profile = DD.make_server_profile_data(win2019_650_iscsi_run_1_profile_data, firmware)
win2019_650_iscsi_run_1_profile_expected = DD.make_expected_server_profile_data(win2019_650_iscsi_run_1_profile_data, firmware)
win2019_650_iscsi_run_1_profile_update_spp = DD.make_server_profile_data(win2019_650_iscsi_run_1_profile_data, update_firmware)
win2019_650_iscsi_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2019_650_iscsi_run_1_profile_data, update_firmware)

##############################################################################################################
#  win2016_650_iscsi_run_1 profile test data for iscsi connection with gen10 server 650FLB OS is Windows 2016
##############################################################################################################

win2016_650_iscsi_run_1_profile_data = [{'name': 'win2016_650_iscsi_run_1', 'serverHardwareUri': 'SH:2SN748014X, bay 11', 'enclosureGroupUri': 'EG:encgrp1',
                                         "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcg5ksf01a",
                                         "iscsiInitiatorNameType": "UserDefined", 'description': '', 'affinity': 'Bay',
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                                 'mac': 'FE:13:83:30:00:18',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                                 'mac': 'FE:13:83:30:00:19',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:eth2', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                                 'mac': 'FE:13:83:30:00:1A',
                                                                                 'macType': 'UserDefined', 'networkUri': 'ETH:iSCSI1', "ipv4": {"ipAddressSource": "DHCP"},
                                                                                 "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500",
                                                                                 'mac': 'FE:13:83:30:00:1B',
                                                                                 'macType': 'UserDefined', "networkUri": "ETH:iSCSI1", "ipv4": {"ipAddressSource": "DHCP"},
                                                                                 "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                                         'serverHardwareTypeUri': 'SHT:BL460c Gen10:Flb1:HP FlexFabric 20Gb 2-port 650FLB Adapter:1:HP FlexFabric 20Gb 2-port 630M Adapter',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2016_650_iscsi_run_1", 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:cosmos-vsa-cluster', 'bootVolumePriority': 'Primary',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]
win2016_650_iscsi_run_1_profile = DD.make_server_profile_data(win2016_650_iscsi_run_1_profile_data, firmware)
win2016_650_iscsi_run_1_profile_expected = DD.make_expected_server_profile_data(win2016_650_iscsi_run_1_profile_data, firmware)
win2016_650_iscsi_run_1_profile_update_spp = DD.make_server_profile_data(win2016_650_iscsi_run_1_profile_data, update_firmware)
win2016_650_iscsi_run_1_profile_update_spp_expected = DD.make_expected_server_profile_data(win2016_650_iscsi_run_1_profile_data, update_firmware)

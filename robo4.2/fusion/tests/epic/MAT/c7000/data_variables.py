from DynamicData import DynamicData

DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

firmware = {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None}
# firmware = {'manageFirmware': True, 'forceInstallFirmware': True, 'firmwareInstallType': 'FirmwareOnlyOfflineMode'}

licenses = [{'key': 'ACLA C9MA H9P9 CHUZ V7B5 HWWB Y9JL KMPL 5R2H 6DRM DXAU 2CSM GHTG L762 BCV6 EEFY KJVT D5KM EFVW DT5J 69UM NY2G 9K2P 3E22 MKQU 3UFZ TZZX AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863919 HPOV-NFR1 HP_OneView_16_Seat_NFR H592ADTYDJJD"_3PXQT-HWSHJ-7RBW9-ZW3WG-XC2W2'},
            {'key': 'YCLE B9MA H9PY GHU3 U7B5 HWW5 Y9JL KMPL NRSF 4ERM DXAU 2CSM GHTG L762 DK5Y HHF9 KJVT D5KM EFVW DT5J 89MK PZ2G 9K2P 3E22 MKYU 3UFZ TZZ7 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424863952 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR YHUAADTYEC5H"'},
            {'key': 'QCLA A9MA H9PA KHW3 V7B5 HWWB Y9JL KMPL BRKD 8FBM DXAU 2CSM GHTG L762 XKJ3 VBF4 KJVT D5KM EFRW DS5R A9E9 52KG 9K2P 3E22 UKYU 3UFZ TZZ7 MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863966 HPOV-NFR1 HP_OneView_16_Seat_NFR 7EA7ADTYED49"_3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
            {'key': 'YCLC C9MA H9P9 8HW3 U7B5 HWW5 Y9JL KMPL LRGB 7ABQ DXAU 2CSM GHTG L762 QGFZ EEZM KJVT D5KM EFRW DS5R M94M N5KG 9K2P 3E22 AKYU LUV5 TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424864041 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR HY95ADTYTCHT"'}]

spp_name = 'SPP2017100.2017_0815.44'
FirmwareVersion = '2017.10.0'

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
         'Host': '10.0.5.20',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'Cosmos123', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '10.0.5.12',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'},
        {'Type': 'HPE',
         'Host': '10.0.5.13',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'}]

ethernet_networks = [{'name': 'vlan1047', 'type': 'ethernet-networkV4', 'vlanId': 1047, 'purpose': 'General', 'smartLink': False, 'privateNetwork': False},
                     {'name': 'vlan1048', 'type': 'ethernet-networkV4', 'vlanId': 1048, 'purpose': 'Management', 'smartLink': False, 'privateNetwork': False},
                     {'name': 'vlan1049', 'type': 'ethernet-networkV4', 'vlanId': 1049, 'purpose': 'Management', 'smartLink': False, 'privateNetwork': False},
                     {'name': 'vlan1050', 'type': 'ethernet-networkV4', 'vlanId': 1050, 'purpose': 'Management', 'smartLink': False, 'privateNetwork': False}]

fc_networks = [{'name': 'FA-SAN1-lom-a', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                # 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW1', 'fabricType': 'FabricAttach'},
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW1', 'fabricType': 'FabricAttach'},
               {'name': 'FA-SAN1-lom-b', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                # 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW2', 'fabricType': 'FabricAttach'},
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW2', 'fabricType': 'FabricAttach'},
               {'name': 'FA-SAN1-mez1-a', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                # 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW1', 'fabricType': 'FabricAttach'},
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW1', 'fabricType': 'FabricAttach'},
               {'name': 'FA-SAN1-mez1-b', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                # 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW2', 'fabricType': 'FabricAttach'},
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:EPIC-SanSW2', 'fabricType': 'FabricAttach'},
               {'name': '3par-a', 'type': 'fc-networkV4', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'},
               {'name': '3par-b', 'type': 'fc-networkV4', 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'DirectAttach'}]

fcoe_networks = [{'name': 'FCOE-3601', 'type': 'fcoe-networkV4', 'vlanId': 3601, 'managedSanUri': 'FCSan:VSAN3601'},
                 {'name': 'FCOE-3602', 'type': 'fcoe-networkV4', 'vlanId': 3602, 'managedSanUri': 'FCSan:VSAN3602'}]

network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['vlan1047', 'vlan1048', 'vlan1049', 'vlan1050'], 'nativeNetworkUri': None}]

uplink_sets = {'lig2-net-lom': {'name': 'lig2-net-lom', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                'networkUris': ['vlan1047', 'vlan1048', 'vlan1049', 'vlan1050'], 'mode': 'Auto',
                                'logicalPortConfigInfos': [{'bay': '1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                           {'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}]},
               'lig2-fa-lom-a': {'name': 'lig2-fa-lom-a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                 'networkUris': ['FA-SAN1-lom-a'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                            {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
               'lig2-fa-lom-b': {'name': 'lig2-fa-lom-b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                 'networkUris': ['FA-SAN1-lom-b'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                            #                                                           {'bay': '2', 'port': 'X2', 'speed': 'Auto'}
                                                            ]},
               'lig2-fa-mez1-a': {'name': 'lig2-fa-mez1-a', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                  'networkUris': ['FA-SAN1-mez1-a'], 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '3', 'port': '1', 'speed': 'Auto'},
                                                             {'bay': '3', 'port': '2', 'speed': 'Auto'}]},
               'lig2-fa-mez1-b': {'name': 'lig2-fa-mez1-b', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                                  'networkUris': ['FA-SAN1-mez1-b'], 'mode': 'Auto',
                                  'logicalPortConfigInfos': [{'bay': '4', 'port': '1', 'speed': 'Auto'},
                                                             {'bay': '4', 'port': '2', 'speed': 'Auto'}]},
               'lig2-net-mez2': {'name': 'lig2-net-mez2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                 'networkUris': ['vlan1047', 'vlan1048', 'vlan1049', 'vlan1050'], 'mode': 'Auto',
                                 'logicalPortConfigInfos': [{'bay': '5', 'port': 'X1', 'speed': 'Auto'},
                                                            {'bay': '5', 'port': 'X2', 'speed': 'Auto'},
                                                            {'bay': '6', 'port': 'X1', 'speed': 'Auto'},
                                                            {'bay': '6', 'port': 'X2', 'speed': 'Auto'}]},
               'lig2-fcoe-lom-a': {'name': 'lig2-fcoe-lom-a', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                   'networkUris': ['FCOE-3601'], 'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
               'lig2-fcoe-lom-b': {'name': 'lig2-fcoe-lom-b', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                                   'networkUris': ['FCOE-3602'], 'mode': 'Auto',
                                   'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]}}

ligs = [{'name': 'lig2-1', 'type': 'logical-interconnect-groupV4', 'enclosureType': 'C7000', 'ethernetSettings': None, 'description': None,
         'uplinkSets': [uplink_sets['lig2-net-lom'].copy(),
                        uplink_sets['lig2-fa-lom-a'].copy(),
                        uplink_sets['lig2-fa-lom-b'].copy(),
                        uplink_sets['lig2-fa-mez1-a'].copy(),
                        uplink_sets['lig2-fa-mez1-b'].copy(),
                        uplink_sets['lig2-fcoe-lom-a'].copy(),
                        uplink_sets['lig2-fcoe-lom-b'].copy()],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 2, 'enclosure': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module', 'enclosureIndex': 1},
                                     {'bay': 3, 'enclosure': 1, 'type': 'HP VC 8Gb 24-Port FC Module', 'enclosureIndex': 1},
                                     {'bay': 4, 'enclosure': 1, 'type': 'HP VC 8Gb 24-Port FC Module', 'enclosureIndex': 1}],
         'internalNetworkUris': [],
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}},
        {'name': 'lig2-2', 'type': 'logical-interconnect-groupV4', 'enclosureType': 'C7000', 'ethernetSettings': None, 'description': None,
         'uplinkSets': [uplink_sets['lig2-net-mez2'].copy()],
         'interconnectMapTemplate': [{'bay': 5, 'enclosure': 1, 'type': 'HP VC Flex-10/10D Module', 'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 1, 'type': 'HP VC Flex-10/10D Module', 'enclosureIndex': 1}],
         'internalNetworkUris': [],
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough', 'downlinkClassificationType': None, 'uplinkClassificationType': None, 'qosTrafficClassifiers': None, 'description': None, 'status': None, 'name': None, 'state': None, 'category': 'qos-aggregated-configuration', 'created': None, 'modified': None, 'eTag': None, 'uri': None}, 'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None, 'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None, 'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}}]

expected_lig = [{"name": "lig2-2", "type": "logical-interconnect-groupV4", "enclosureType": "C7000",
                 "uplinkSets": [{"name": "lig2-net-mez2", "networkUris": ["ETH:vlan1047", "ETH:vlan1048", "ETH:vlan1049", "ETH:vlan1050"]}],
                 "internalNetworkUris": []},
                {"name": "lig2-1", "type": "logical-interconnect-groupV4", "enclosureType": "C7000",
                 "uplinkSets": [{"name": "lig2-net-lom", "networkUris": ["ETH:vlan1047", "ETH:vlan1048", "ETH:vlan1049", "ETH:vlan1050"]},
                                {"name": "lig2-fa-lom-a", "networkUris": ["FC:FA-SAN1-lom-a"]},
                                {"name": "lig2-fa-lom-b", "networkUris": ["FC:FA-SAN1-lom-b"]},
                                {"name": "lig2-fa-mez1-a", "networkUris": ["FC:FA-SAN1-mez1-a"]},
                                {"name": "lig2-fa-mez1-b", "networkUris": ["FC:FA-SAN1-mez1-b"]},
                                {"name": "lig2-fcoe-lom-a", "networkUris": ["FCOE:FCOE-3601"]},
                                {"name": "lig2-fcoe-lom-b", "networkUris": ["FCOE:FCOE-3602"]}],
                 "internalNetworkUris": []}]

enc_groups = [{'name': 'encgrp-fwi2', 'enclosureCount': 1, 'configurationScript': 'SET RACK NAME "OVA"',
               'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:lig2-1'},
                                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:lig2-1'},
                                           {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:lig2-1'},
                                           {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:lig2-1'},
                                           {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:lig2-2'},
                                           {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:lig2-2'},
                                           {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                                           {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': None, 'ipRangeUris': [], 'powerMode': None}]

storage_systems = [{'name': 'epic3par7200', 'family': 'StoreServ', "hostname": "10.0.5.5",
                    "credentials": {"username": "fwi", "password": "Cosmos123"}, "serialNumber": "1675718",
                    'deviceSpecificAttributes': {'managedDomain': 'EPIC-c7kME2', 'managedPools': []}}]

storage_pools = [{"storageSystemUri": 'epic3par7200', "name": 'EPIC-c7kME2-CPG-R0', "isManaged": True},
                 {"storageSystemUri": 'epic3par7200', "name": 'FC_r6', "isManaged": True}]

existing_storage_volumes = [{"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay1Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay2Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay3Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay8Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay9Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay10Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay11Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay12Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay13Vol-prm"},
                            {"storageSystemUri": "epic3par7200", "name": "EPIC-ME2-Bay11FCoEbootVol-prm"}]

storage_volumes = [  # new private no template
    {"properties": {"description": "EPIC-ME2-Bay1Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay1Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay2Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay2Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay3Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay3Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay8Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay8Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay9Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay9Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay10Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay10Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay11Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay11Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay12Vol-prm", "isShareable": False, "name": "EPIC-ME2-Bay12Vol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"},
    {"properties": {"description": "EPIC-ME2-Bay11FCoEbootVol-prm", "isShareable": False, "name": "EPIC-ME2-Bay11FCoEbootVol-prm",
                                   "provisioningType": "Thin", "size": 53687091200, "storagePool": "EPIC-c7kME2-CPG-R0"}, "templateUri": "ROOT"}]

encl = [{"enclosureGroupUri": "EG:encgrp-fwi2",
         "name": "EPIC-ME2",
         "hostname": "10.47.4.31",
         "username": "Administrator",
         "password": "Cosmos123",
         "licensingIntent": "OneViewNoiLO",
         "updateFirmwareOn": "EnclosureOnly",
         "forceInstallFirmware": firmware['forceInstallFirmware'],
         "force": True}]

dl_servers = [{"name": "ILOMXQ525031G", "hostname": "10.47.3.24", "username": "Administrator", "password": "Cosmos123", "force": True,
               "licensingIntent": "OneViewNoiLO", "configurationState": "Managed"}]

dlserver_profiles = [{'serverHardwareUri': 'SH:ILOMXQ525031G', 'name': 'DL_Profile',
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

server_profile_data = [{'name': 'EPIC-ME2bay1', 'serverHardwareUri': 'SH:EPIC-ME2, bay 1', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                'networkUri': 'FC:FA-SAN1-mez1-a', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20110002AC0127C6', 'lun': '1'}]}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto',
                                                                'networkUri': 'FC:FA-SAN1-mez1-b', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC0127C6', 'lun': '1'}]}},
                                                               {'id': 4, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Flb 1:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Flb 1:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1050', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:EPIC-ME2-Bay1Vol-prm',
                                                              'lunType': 'Manual', 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 2},
                                                                               {'isEnabled': True, 'connectionId': 3}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       #                                             {'name': 'EPIC-ME2bay2', 'serverHardwareUri': 'SH:EPIC-ME2, bay 2', 'enclosureGroupUri': 'encgrp-fwi2',
                       #                                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                       #                                              'boot': {'manageBoot': True, 'order': ['HardDisk']},
                       #                                              'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                       #                                                               'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                       #                                                               'boot': {'priority': 'Primary'}},
                       #                                                              {'id': 2, 'name': None, 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                       #                                                               'networkUri': 'FC:FA-SAN1-mez1-a', 'functionType': 'FibreChannel',
                       #                                                               'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20110002AC0127C6', 'lun': '1'}]}},
                       #                                                              {'id': 3, 'name': None, 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto',
                       #                                                               'networkUri': 'FC:FA-SAN1-mez1-b', 'functionType': 'FibreChannel',
                       #                                                               'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC0127C6', 'lun': '1'}]}},
                       #                                                              {'id': 4, 'name': None, 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500',
                       #                                                               'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                       #                                                               'boot': {'priority': 'NotBootable'}},
                       #                                                              {'id': 5, 'name': None, 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500',
                       #                                                               'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                       #                                                               'boot': {'priority': 'NotBootable'}},
                       #                                                              {'id': 6, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                       #                                                               'networkUri': 'ETH:vlan1050', 'functionType': 'Ethernet',
                       #                                                               'boot': {'priority': 'NotBootable'}},
                       #                                                              {'id': 7, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                       #                                                               'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                       #                                                               'boot': {'priority': 'NotBootable'}},
                       #                                                              {'id': 8, 'name': None, 'portId': 'Flb 1:2-c', 'requestedMbps': '2500',
                       #                                                               'networkUri': 'ETH:vlan1050', 'functionType': 'Ethernet',
                       #                                                               'boot': {'priority': 'NotBootable'}}]},
                       #                                              'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                       #                                                             'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:EPIC-ME2-Bay2Vol-prm',
                       #                                                                                    'lunType': 'Manual', 'lun': 1,
                       #                                                                                    'storagePaths': [{'isEnabled': True, 'connectionId': 2},
                       #                                                                                                     {'isEnabled': True, 'connectionId': 3}]}]},
                       #                                              'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'EPIC-ME2bay3', 'serverHardwareUri': 'SH:EPIC-ME2, bay 3', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                'networkUri': 'FC:FA-SAN1-mez1-a', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto',
                                                                'networkUri': 'FC:FA-SAN1-mez1-b', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 8, 'name': None, 'portId': 'Mezz 2:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                        'bios': {'manageBios': False, 'overriddenSettings': []},
                        'localStorage': {'sasLogicalJBODs': [],
                                         'controllers': [{'logicalDrives': [{'name': 'EPICME2_Bay3Boot',
                                                                             'raidLevel': 'RAID0',
                                                                             'bootable': True,
                                                                             'numPhysicalDrives': 1,
                                                                             'driveTechnology': 'SasHdd',
                                                                             'sasLogicalJBODId': None}],
                                                          'deviceSlot': 'Embedded',
                                                          'mode': 'RAID',
                                                          'initialize': True,
                                                          'importConfiguration': False}]}},
                       {'name': 'EPIC-ME2bay8', 'serverHardwareUri': 'SH:EPIC-ME2, bay 8', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': None,
                        'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'HardDisk', 'PXE']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FA-SAN1-lom-a', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20110002AC0127C6', 'lun': '1'}]}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FA-SAN1-lom-b', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC0127C6', 'lun': '1'}]}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 2:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1050', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:EPIC-ME2-Bay8Vol-prm',
                                                              'lunType': 'Manual', 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 2},
                                                                               {'isEnabled': True, 'connectionId': 3}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'EPIC-ME2bay9', 'serverHardwareUri': 'SH:EPIC-ME2, bay 9', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE-3601', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE-3602', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 4, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 2:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:EPIC-ME2-Bay9Vol-prm', 'isBootVolume': True,
                                                              'lunType': 'Manual', 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 2},
                                                                               {'isEnabled': True, 'connectionId': 3}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'EPIC-ME2bay10', 'serverHardwareUri': 'SH:EPIC-ME2, bay 10', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 4, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1050', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'ME2-Tester'},
                                                                            {'id': 'AdminPhone', 'value': '123-123-4321'}]},
                        'localStorage': {'sasLogicalJBODs': [],
                                         'controllers': [{'logicalDrives': [],
                                                          'deviceSlot': 'Embedded',
                                                          'mode': 'HBA',
                                                          'initialize': True,
                                                          'importConfiguration': False}]}},
                       {'name': 'EPIC-ME2bay11', 'serverHardwareUri': 'SH:EPIC-ME2, bay 11', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE-3601', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOE-3602', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto',
                                                                'networkUri': 'FC:FA-SAN1-mez1-a', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto',
                                                                'networkUri': 'FC:FA-SAN1-mez1-b', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Flb 1:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 8, 'name': None, 'portId': 'Flb 1:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:EPIC-ME2-Bay11FCoEbootVol-prm', 'isBootVolume': True,
                                                              'lunType': 'Manual', 'lun': 0,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 2},
                                                                               {'isEnabled': True, 'connectionId': 3}]},
                                                             {'id': 2, 'volumeUri': 'SVOL:EPIC-ME2-Bay11Vol-prm', 'isBootVolume': False,
                                                              'lunType': 'Manual', 'lun': 2,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 4},
                                                                               {'isEnabled': True, 'connectionId': 5}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'EPIC-ME2bay13', 'serverHardwareUri': 'SH:EPIC-ME2, bay 13', 'enclosureGroupUri': 'encgrp-fwi2',
                        'bootMode': None,
                        'boot': {'manageBoot': True, 'order': ['HardDisk', 'PXE']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Flb 1:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'Primary'}},
                                                               {'id': 2, 'name': None, 'portId': 'Flb 1:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FA-SAN1-lom-a', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '20110002AC0127C6', 'lun': '1'}]}},
                                                               {'id': 3, 'name': None, 'portId': 'Flb 1:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FA-SAN1-lom-b', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '21120002AC0127C6', 'lun': '1'}]}},
                                                               {'id': 4, 'name': None, 'portId': 'Flb 1:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Flb 1:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Flb 1:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Flb 1:1-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 8, 'name': None, 'portId': 'Flb 1:2-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:vlan1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:EPIC-ME2-Bay13Vol-prm', 'isBootVolume': False,
                                                              'lunType': 'Manual', 'lun': 1,
                                                                                   'storagePaths': [{'isEnabled': True, 'connectionId': 2},
                                                                                                    {'isEnabled': True, 'connectionId': 3}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}}
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

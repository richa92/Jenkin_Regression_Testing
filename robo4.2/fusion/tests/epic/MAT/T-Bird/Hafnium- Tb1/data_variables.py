from dynamic_data import DynamicData

DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

potash_url = 'http://hf-cit.us.rdlabs.hpecorp.net:9300/r1.1.0/Potash/development/fv1-1.1.0-34/hpe_icm_fv1-1.1.0-34-2017-04-19-D.pkg'

potash_pkg = DD.get_hafnium_pkg_name(potash_url)

expected_fw = DD.get_hafnium_version(potash_url)

interconnects = [{'name': 'EPICTBIRD1, interconnect 3', 'ipAddress': '10.49.12.15'},
                 {'name': 'EPICTBIRD1, interconnect 6', 'ipAddress': '10.49.12.13'}]

firmware = {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None}
# firmware = {'manageFirmware': True, 'forceInstallFirmware': True, 'firmwareInstallType': 'FirmwareOnlyOfflineMode'}

spp_name = 'SPP2017070.2017_0608.153'

updated_spp_name = DD.spp_name_withunderscore(spp_name)

spp_local_dir = 'D:/SPP/'

licenses = [{'key': 'ACLA C9MA H9P9 CHUZ V7B5 HWWB Y9JL KMPL 5R2H 6DRM DXAU 2CSM GHTG L762 BCV6 EEFY KJVT D5KM EFVW DT5J 69UM NY2G 9K2P 3E22 MKQU 3UFZ TZZX AB6X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863919 HPOV-NFR1 HP_OneView_16_Seat_NFR H592ADTYDJJD"_3PXQT-HWSHJ-7RBW9-ZW3WG-XC2W2'},
            {'key': 'YCLE B9MA H9PY GHU3 U7B5 HWW5 Y9JL KMPL NRSF 4ERM DXAU 2CSM GHTG L762 DK5Y HHF9 KJVT D5KM EFVW DT5J 89MK PZ2G 9K2P 3E22 MKYU 3UFZ TZZ7 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424863952 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR YHUAADTYEC5H"'},
            {'key': 'QCLA A9MA H9PA KHW3 V7B5 HWWB Y9JL KMPL BRKD 8FBM DXAU 2CSM GHTG L762 XKJ3 VBF4 KJVT D5KM EFRW DS5R A9E9 52KG 9K2P 3E22 UKYU 3UFZ TZZ7 MB5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR YT9J 4NUG 2NJN J9UF "424863966 HPOV-NFR1 HP_OneView_16_Seat_NFR 7EA7ADTYED49"_3Q7Z5-2HDVR-CC6R8-6BJQM-9S84B'},
            {'key': 'YCLC C9MA H9P9 8HW3 U7B5 HWW5 Y9JL KMPL LRGB 7ABQ DXAU 2CSM GHTG L762 QGFZ EEZM KJVT D5KM EFRW DS5R M94M N5KG 9K2P 3E22 AKYU LUV5 TZZX 9B5X 82Z5 WHEF D9ED 3RUX BJS2 XFXC T84U R42A 58S5 XA2D WXAP GMTQ 4YLB MM2S CZU7 2E4X E8EW BGB5 BWPD CAAR 2T9J MNEG 2NJN J9UF "424864041 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR HY95ADTYTCHT"'}]

users_name = [{'name': 'appliance', 'role': 'Infrastructure administrator'},
              {'name': 'network', 'role': 'Network administrator'},
              {'name': 'server', 'role': 'Server administrator'},
              {'name': 'storage', 'role': 'Storage administrator'},
              {'name': 'readonly', 'role': 'Read only'}]

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

ethernet_networks = [{'name': 'Eth_1047', 'type': 'ethernet-networkV4', 'vlanId': 1047, 'purpose': 'General',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'Eth_1048', 'type': 'ethernet-networkV4', 'vlanId': 1048, 'purpose': 'General',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'Eth_1049', 'type': 'ethernet-networkV4', 'vlanId': 1049, 'purpose': 'General',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'Eth_1050', 'type': 'ethernet-networkV4', 'vlanId': 1050, 'purpose': 'General',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'ISCSI_1021', 'type': 'ethernet-networkV4', 'vlanId': 1021, 'purpose': 'General',
                      'smartLink': False, 'privateNetwork': False},
                     {'name': 'ISCSI_1022', 'type': 'ethernet-networkV4', 'vlanId': 1022, 'purpose': 'General',
                      'smartLink': False, 'privateNetwork': False}]

fc_networks = [{'name': 'FC-A', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'managedSanUri': 'FCSan:EPIC-SanSW1', 'fabricType': 'FabricAttach'},
               {'name': 'FC-B', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'managedSanUri': 'FCSan:EPIC-SanSW2', 'fabricType': 'FabricAttach'}]

fcoe_networks = [{'name': 'FCOe3601', 'type': 'fcoe-networkV4', 'vlanId': 3601, 'managedSanUri': 'FCSan:VSAN3601'},
                 {'name': 'FCOe3602', 'type': 'fcoe-networkV4', 'vlanId': 3602, 'managedSanUri': 'FCSan:VSAN3602'}]

network_sets = [{'name': 'netset1', 'type': 'network-setV4', 'networkUris': ['Eth_1047', 'Eth_1048', 'Eth_1049',
                                                                             'Eth_1050', 'ISCSI_1021', 'ISCSI_1022'],
                 'nativeNetworkUri': None}]

ligs = [{'name': 'LIG_potash', 'type': 'logical-interconnect-groupV4', 'enclosureType': 'SY12000',
         'ethernetSettings': None, 'description': None,
         'uplinkSets': [],
         'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                                      'enclosureIndex': 1},
                                     {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                                      'enclosureIndex': 1}],
         'internalNetworkUris': [], 'interconnectBaySet': 3, 'redundancyType': 'Redundant',
         'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough',
                                                  'downlinkClassificationType': None, 'uplinkClassificationType': None,
                                                  'qosTrafficClassifiers': None, 'description': None, 'status': None,
                                                  'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                                                  'created': None, 'modified': None, 'eTag': None, 'uri': None},
                              'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
                              'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
                              'eTag': None, 'modified': None, 'created': None,
                              'category': 'qos-aggregated-configuration', 'uri': None}}]

expected_ligs = [{"name": "LIG_potash", "type": "logical-interconnect-groupV4", "enclosureType": "SY12000",
                  "uplinkSets": [],
                  "internalNetworkUris": []}]

uplink_sets = {'Eth_uplink': {'name': 'Eth_uplink', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                              'networkUris': ['Eth_1047', 'Eth_1048', 'Eth_1049', 'Eth_1050', 'ISCSI_1021',
                                              'ISCSI_1022'], 'mode': 'Auto',
                              'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                         {'bay': '6', 'port': 'Q1', 'speed': 'Auto'}]},
               'FCOE3601': {'name': 'FCOE3601', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                            'networkUris': ['FCOe3601'], 'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q4', 'speed': 'Auto'}]},
               'FCOE3602': {'name': 'FCOE3602', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
                            'networkUris': ['FCOe3602'], 'mode': 'Auto',
                            'logicalPortConfigInfos': [{'bay': '6', 'port': 'Q4', 'speed': 'Auto'}]},
               'FC-A': {'name': 'FC-A', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                        'networkUris': ['FC-A'], 'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '3', 'port': 'Q5.1', 'speed': 'Auto'}]},
               'FC-B': {'name': 'FC-B', 'networkType': 'FibreChannel', 'ethernetNetworkType': None,
                        'networkUris': ['FC-B'], 'mode': 'Auto',
                        'logicalPortConfigInfos': [{'bay': '6', 'port': 'Q5.1', 'speed': 'Auto'}]}}

update_ligs = [{'name': 'LIG_potash', 'type': 'logical-interconnect-groupV4', 'enclosureType': 'SY12000',
                'ethernetSettings': None, 'description': None,
                'uplinkSets': [uplink_sets['Eth_uplink'].copy(),
                               uplink_sets['FCOE3601'].copy(),
                               uplink_sets['FCOE3602'].copy(),
                               uplink_sets['FC-A'].copy(),
                               uplink_sets['FC-B'].copy()],
                'interconnectMapTemplate': [{'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                                             'bay': 3, 'enclosure': 1, 'enclosureIndex': 1},
                                            {'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                                             'bay': 6, 'enclosure': 1, 'enclosureIndex': 1}],
                'internalNetworkUris': [], 'interconnectBaySet': 3, 'redundancyType': 'Redundant', 'enclosureIndexes': [1],
                'qosConfiguration': {'activeQosConfig': {'type': 'QosConfiguration', 'configType': 'Passthrough',
                                                         'downlinkClassificationType': None, 'uplinkClassificationType': None,
                                                         'qosTrafficClassifiers': None, 'description': None, 'status': None,
                                                         'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                                                         'created': None, 'modified': None, 'eTag': None, 'uri': None},
                                     'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
                                     'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
                                     'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration', 'uri': None}}]

expected_ligs_updated = [{"name": "LIG_potash", "type": "logical-interconnect-groupV4", "enclosureType": "SY12000",
                          "uplinkSets": [{"name": "Eth_uplink", "networkUris": ["ETH:Eth_1047", "ETH:Eth_1048",
                                                                                "ETH:Eth_1049", "ETH:Eth_1050",
                                                                                "ETH:ISCSI_1021", "ETH:ISCSI_1022"]},
                                         {"name": "FCOE3601", "networkUris": ["FCOE:FCOe3601"]},
                                         {"name": "FCOE3602", "networkUris": ["FCOE:FCOe3602"]},
                                         {"name": "FC-A", "networkUris": ["FC:FC-A"]},
                                         {"name": "FC-B", "networkUris": ["FC:FC-B"]}],
                          "internalNetworkUris": []}]

enc_groups = [{'name': 'EG-TB1', 'enclosureCount': 1,
               'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_potash'},
                                           {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_potash'}],
               'ipAddressingMode': 'DHCP', 'ipRangeUris': [], 'powerMode': 'RedundantPowerFeed'}]

update_logical_enclosure_from_group = {'name': 'LE-TB1'}

edit_li_telemetry_config = {'name': 'LE-TB1-LIG_potash', 'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 20, 'sampleInterval': 200,
                            'description': None, 'status': None, 'state': None, 'category': 'telemetry-configurations',
                            'uri': '/rest/logical-interconnects'}

update_logical_interconnect_from_group = {'name': 'LE-TB1-LIG_potash'}

li_state = {"name": "LE-TB1-LIG_potash"}

storage_systems = [{'name': 'epic3par7200', 'family': 'StoreServ', "hostname": "10.0.5.5",
                    "credentials": {"username": "fwi", "password": "Cosmos123"}, "serialNumber": "1675718",
                    'deviceSpecificAttributes': {'managedDomain': 'EPIC-TB1', 'managedPools': []}}]

storage_pools = [{"storageSystemUri": 'epic3par7200', "name": 'FC_r0', "isManaged": True},
                 {"storageSystemUri": 'epic3par7200', "name": 'FC_r1', "isManaged": True}]

storage_volume_templates = [{"name": "TB1-private-thin", "description": "", "rootTemplateUri": "SVT:TB1-private-thin", "description": "private non-boot volume template",
                             "properties": {"name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                                     "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                                            "description": {"title": "Description", "description": "A description for the volume",
                                                            "type": "string", "minLength": 0, "maxLength": 2000, "default": "", "meta": {"locked": False}},
                                            "storagePool": {"title": "Storage Pool", "description": "A common provisioning group URI reference",
                                                            "type": "string", "required": True, "format": "x-uri-reference",
                                                            "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                                            "default": "FC_r1"},
                                            "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                                                     "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                                                     "meta": {"locked": False, "semanticType": "capacity"}, "default": 1073741824, },
                                            "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                                            "type": "boolean", "meta": {"locked": False}, "default": False, },
                                            "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                                                 "type": "string", "enum": ["Thin", "Full"], "meta":{"locked": True, "createOnly": True},
                                                                 "default": "Thin"},
                                            "snapshotPool": {"title": "Snaphot Pool", "description": "A URI referenceto the common provisioning group used to create snapshots",
                                                             "type": "string", "format": "x-uri-reference", "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                                             "default": "FC_r1"}}}]

expected_storage_volume_templates = [{"category": "storage-volume-templates", "name": "TB1-private-thin", "status": "OK", "state": "Configured", "type": "StorageVolumeTemplateV5", "uri": "SVT:TB1-private-thin",
                                      "properties": {"name": {"title": "Volume name", "description": "A volume name between 1 and 100 characters",
                                                              "type": "string", "minLength": 1, "maxLength": 100, "required": True, "meta": {"locked": False}},
                                                     "description": {"title": "Description", "description": "A description for the volume",
                                                                     "type": "string", "minLength": 0, "maxLength": 2000, "default": "", "meta": {"locked": False}},
                                                     "storagePool": {"title": "Storage Pool", "description": "A common provisioning group URI reference",
                                                                     "type": "string", "required": True, "format": "x-uri-reference",
                                                                     "meta": {"locked": False, "createOnly": True, "semanticType": "device-storage-pool"},
                                                                     "default": "SPOOL:FC_r1"},
                                                     "size": {"title": "Capacity", "description": "The capacity of the volume in bytes",
                                                              "type": "integer", "required": True, "minimum": 1073741824, "maximum": 17592186044416,
                                                              "meta": {"locked": False, "semanticType": "capacity"}, "default": 1073741824, },
                                                     "isShareable": {"title": "Is Shareable", "description": "The shareability of the volume",
                                                                     "type": "boolean", "meta": {"locked": False}, "default": False, },
                                                     "provisioningType": {"title": "Provisioning Type", "description": "The provisioning type for the volume",
                                                                          "type": "string", "enum": ["Thin", "Full"], "meta":{"locked": True, "createOnly": True},
                                                                          "default": "Thin"},
                                                     "snapshotPool": {"title": "Snaphot Pool", "description": "A URI referenceto the common provisioning group used to create snapshots",
                                                                      "type": "string", "format": "x-uri-reference", "meta": {"locked": True, "semanticType": "device-snapshot-storage-pool"},
                                                                      "default": "SPOOL:FC_r1"}}}]

storage_volumes = [  # new private no template
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "TB1-notemplate-priv",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_r1"}, "templateUri": "ROOT"},
    # new private with template
    {"properties": {"description": "non-boot private volume", "isShareable": False, "name": "TB1-withtemplate-priv",
                                   "size": 5368709120, "storagePool": "FC_r1"}, "templateUri": "TB1-private-thin"},
    # shared volume
    {"properties": {"description": "shared volume", "isShareable": True, "name": "TB1-shared",
                                   "provisioningType": "Full", "size": 5368709120, "storagePool": "FC_r1"}, "templateUri": "ROOT", "isPermanent": True}]

expected_storage_volumes = [{'isShareable': False, 'name': 'TB1-notemplate-priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FC_r1', 'type': 'StorageVolumeV5'},
                            {'isShareable': False, 'name': 'TB1-withtemplate-priv', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FC_r1', 'type': 'StorageVolumeV5'},
                            {'isShareable': True, 'name': 'TB1-shared', 'state': 'Managed', 'status': 'OK', 'storagePoolUri': 'SPOOL:FC_r1', 'type': 'StorageVolumeV5'}]

existing_storage_volumes = [{"storageSystemUri": "epic3par7200", "name": "TB1-480gen10-bay3"},
                            {"storageSystemUri": "epic3par7200", "name": "TB1-480gen9-bay10-FC"},
                            {"storageSystemUri": "epic3par7200", "name": "TB1-660gen9-bay2-FC-esxi6.5"}]

logical_enclosure = [{'name': 'LE-TB1', 'enclosureUris': ['ENC:EPICTBIRD1'], 'enclosureGroupUri': 'EG:EG-TB1'}]

server_profile_data = [{'name': 'TB1-660gen9-bay2-FC-esxi6.5', 'serverHardwareUri': 'SH:EPICTBIRD1, bay 2', 'enclosureGroupUri': 'EG-TB1',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 2, 'name': None, 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC-A', 'functionType': 'FibreChannel',
                                                                'macType': 'UserDefined', 'mac': '0A:0C:43:60:00:2E', 'wwpnType': 'UserDefined', 'wwpn': '10:00:0a:75:51:80:00:10', 'wwnn': '10:00:0a:75:51:80:00:11',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 8, 'name': None, 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC-B', 'functionType': 'FibreChannel',
                                                                'macType': 'UserDefined', 'mac': '0A:0C:43:60:00:2F', 'wwpnType': 'UserDefined', 'wwpn': '10:00:0a:75:51:80:00:12', 'wwnn': '10:00:0a:75:51:80:00:13',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                        'sanStorage': {'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:TB1-660gen9-bay2-FC-esxi6.5', 'isBootVolume': True,
                                                              'lunType': 'Auto',  # 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 7},
                                                                               {'isEnabled': True, 'connectionId': 8}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'TB1-480gen10-bay3-FCoE', 'serverHardwareUri': 'SH:EPICTBIRD1, bay 3', 'enclosureGroupUri': 'EG-TB1',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 2, 'name': None, 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOe3601', 'functionType': 'FibreChannel',
                                                                'macType': 'UserDefined', 'mac': '6E:42:08:00:00:06', 'wwpnType': 'UserDefined', 'wwpn': '10:00:a2:2f:10:90:00:00', 'wwnn': '10:00:a2:2f:10:90:00:01',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 8, 'name': None, 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FCOE:FCOe3602', 'functionType': 'FibreChannel',
                                                                'macType': 'UserDefined', 'mac': '6E:42:08:00:00:07', 'wwpnType': 'UserDefined', 'wwpn': '10:00:a2:2f:10:90:00:02', 'wwnn': '10:00:a2:2f:10:90:00:03',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                        'sanStorage': {'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:TB1-480gen10-bay3', 'isBootVolume': True,
                                                              'lunType': 'Auto',  # 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 7},
                                                                               {'isEnabled': True, 'connectionId': 8}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'TB1-660gen9-bay6-ISCSI', 'serverHardwareUri': 'SH:EPICTBIRD1, bay 6', 'enclosureGroupUri': 'EG-TB1',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'requestedMbps': '2500',  # 'portId': 'Auto',
                                                                'networkUri': 'ETH:ISCSI_1021', 'functionType': 'iSCSI',
                                                                'ipv4': {'ipAddressSource': 'DHCP'},
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                                         'iscsi': {'initiatorNameSource': 'UserDefined',
                                                                                   'firstBootTargetIp': '10.21.0.3', 'firstBootTargetPort': '3260',
                                                                                   'secondBootTargetIp': '', 'secondBootTargetPort': '',
                                                                                   'initiatorName': 'iqn.2015-02.com.hpe:oneview-vcg8uur005',
                                                                                   'bootTargetName': 'iqn.2000-05.com.3pardata:20220002ac0127c7:TB1660gen9bay6',
                                                                                   'bootTargetLun': '0'}}},
                                                               {'id': 2, 'name': None, 'requestedMbps': '2500',  # 'portId': 'Auto',
                                                                'networkUri': 'ETH:ISCSI_1022', 'functionType': 'iSCSI',
                                                                'ipv4': {'ipAddressSource': 'DHCP'},
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined',
                                                                         'iscsi': {'initiatorNameSource': 'UserDefined',
                                                                                   'firstBootTargetIp': '10.22.0.3', 'firstBootTargetPort': '3260',
                                                                                   'secondBootTargetIp': '', 'secondBootTargetPort': '',
                                                                                   'initiatorName': 'iqn.2015-02.com.hpe:oneview-vcg8uur005',
                                                                                   'bootTargetName': 'iqn.2000-05.com.3pardata:21220002ac0127c7:TB1660gen9bay6',
                                                                                   'bootTargetLun': '0'}}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Mezz 6:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 6:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 8, 'name': None, 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}}]},
                        'sanStorage': {'hostOSType': 'Windows 2012 / WS2012 R2', 'manageSanStorage': True,
                                       'volumeAttachments': []},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'TB1-480gen9-bay10-FC', 'serverHardwareUri': 'SH:EPICTBIRD1, bay 10', 'enclosureGroupUri': 'EG-TB1',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                        'boot': {'manageBoot': True, 'order': ['HardDisk']},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 2, 'name': None, 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 3, 'name': None, 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 4, 'name': None, 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 5, 'name': None, 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 6, 'name': None, 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500',
                                                                'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet',
                                                                'boot': {'priority': 'NotBootable'}},
                                                               {'id': 7, 'name': None, 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC-A', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                               {'id': 8, 'name': None, 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500',
                                                                'networkUri': 'FC:FC-B', 'functionType': 'FibreChannel',
                                                                'boot': {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                        'sanStorage': {'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                       'volumeAttachments': [{'id': 1, 'volumeUri': 'SVOL:TB1-480gen9-bay10-FC', 'isBootVolume': True,
                                                              'lunType': 'Auto',  # 'lun': 1,
                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 7},
                                                                               {'isEnabled': True, 'connectionId': 8}]}]},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}},
                       {'name': 'TB1-480gen9-bay9-NoStorage', 'serverHardwareUri': 'SH:EPICTBIRD1, bay 9', 'enclosureGroupUri': 'EG-TB1',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                        'boot': {'manageBoot': False},
                        'connectionSettings': {'connections': [{'id': 1, 'name': None, 'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet'},
                                                               {'id': 2, 'name': None, 'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet'},
                                                               {'id': 3, 'name': None, 'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet'},
                                                               {'id': 4, 'name': None, 'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet'},
                                                               {'id': 5, 'name': None, 'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet'},
                                                               {'id': 6, 'name': None, 'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet'},
                                                               {'id': 7, 'name': None, 'networkUri': 'ETH:Eth_1050', 'functionType': 'Ethernet'},
                                                               {'id': 8, 'name': None, 'networkUri': 'ETH:Eth_1050', 'functionType': 'Ethernet'}]},
                        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                        'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}}]

server_profile_templates = [{'name': 'TB1-620gen9-Template', 'type': 'ServerProfileTemplateV4', 'serverProfileDescription': '',
                             'serverHardwareTypeUri': 'SHT:SY 620 Gen9:6:Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:EG-TB1',
                             'serialNumberType': 'Virtual', 'macType': 'Virtual',
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                             'boot': {'manageBoot': False},
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': None, 'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet'},
                                                                    {'id': 2, 'name': None, 'networkUri': 'ETH:Eth_1047', 'functionType': 'Ethernet'},
                                                                    {'id': 3, 'name': None, 'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet'},
                                                                    {'id': 4, 'name': None, 'networkUri': 'ETH:Eth_1048', 'functionType': 'Ethernet'},
                                                                    {'id': 5, 'name': None, 'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet'},
                                                                    {'id': 6, 'name': None, 'networkUri': 'ETH:Eth_1049', 'functionType': 'Ethernet'},
                                                                    {'id': 7, 'name': None, 'networkUri': 'ETH:Eth_1050', 'functionType': 'Ethernet'},
                                                                    {'id': 8, 'name': None, 'networkUri': 'ETH:Eth_1050', 'functionType': 'Ethernet'}]},
                             'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
                             'bios': {'manageBios': False, 'overriddenSettings': []}, 'localStorage': {}}]

server_profiles_from_spt = [{'name': 'TB1-620gen9-bay1-fromTemplate', 'serverHardwareUri': 'EPICTBIRD1, bay 1', 'serverProfileTemplateUri': 'SPT:TB1-620gen9-Template', 'type': 'ServerProfileV8'}]

storage_volumes_to_delete = [{"name": "TB1-notemplate-priv", "storageSystemVolumeName": "TB1-notemplate-priv"},
                             {"name": "TB1-withtemplate-priv", "storageSystemVolumeName": "TB1-withtemplate-priv"},
                             {"name": "TB1-shared", "storageSystemVolumeName": "TB1-shared"}]

delete_storage_volumes_from_OV_only = [{'type': 'AddStorageVolumeV3', 'name': 'TB1-480gen10-bay3', 'description': '', 'storageSystemUri': 'epic3par7200', 'storageSystemVolumeName': 'TB1-480gen10-bay3', 'provisioningParameters': {'shareable': False}},
                                       {'type': 'AddStorageVolumeV3', 'name': 'TB1-480gen9-bay10-FC', 'description': '', 'storageSystemUri': 'epic3par7200', 'storageSystemVolumeName': 'TB1-480gen9-bay10-FC', 'provisioningParameters': {'shareable': False}}]

monitored_enclosures = [{'name': 'EPICTBIRD1', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'EPICTBIRD1',
                         'refreshState': 'NotRefreshing', 'state': 'Monitored', 'status': 'OK',
                         'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                        {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                        {'bayNumber': 7, 'devicePresence': 'Subsumed'}, {'bayNumber': 8, 'devicePresence': 'Subsumed'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Present'}, {'bayNumber': 11, 'devicePresence': 'Present'}, {'bayNumber': 12}],
                         'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                              {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                         'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                     {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                         'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                             {'bayNumber': 5, 'status': None, 'devicePresence': 'Absent'},
                                             {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                         'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                           {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                         'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                         {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}]}]

configured_enclosures = [{'name': 'EPICTBIRD1', 'type': 'EnclosureV7', 'enclosureType': 'SY12000', 'serialNumber': 'EPICTBIRD1',
                          'refreshState': 'NotRefreshing', 'state': 'Configured', 'status': 'OK',
                          'deviceBays': [{'bayNumber': 1, 'devicePresence': 'Present'}, {'bayNumber': 2, 'devicePresence': 'Present'}, {'bayNumber': 3, 'devicePresence': 'Present'},
                                         {'bayNumber': 4, 'devicePresence': 'Present'}, {'bayNumber': 5}, {'bayNumber': 6, 'devicePresence': 'Present'},
                                         {'bayNumber': 7, 'devicePresence': 'Subsumed'}, {'bayNumber': 8, 'devicePresence': 'Subsumed'}, {'bayNumber': 9, 'devicePresence': 'Present'}, {'bayNumber': 10, 'devicePresence': 'Present'}, {'bayNumber': 11, 'devicePresence': 'Present'}, {'bayNumber': 12}],
                          'interconnectBays': [{'bayNumber': 1, 'bayPowerState': 'Unknown'}, {'bayNumber': 2, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 3, 'bayPowerState': 'Unknown'}, {'bayNumber': 4, 'bayPowerState': 'Unknown'},
                                               {'bayNumber': 5, 'bayPowerState': 'Unknown'}, {'bayNumber': 6, 'bayPowerState': 'Unknown'}],
                          'fanBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 5, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 7, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 8, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 9, 'status': 'OK', 'devicePresence': 'Present'},
                                      {'bayNumber': 10, 'status': 'OK', 'devicePresence': 'Present'}],
                          'powerSupplyBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 3, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 4, 'status': 'OK', 'devicePresence': 'Present'},
                                              {'bayNumber': 5, 'status': None, 'devicePresence': 'Absent'},
                                              {'bayNumber': 6, 'status': 'OK', 'devicePresence': 'Present'}],
                          'applianceBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                            {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}],
                          'managerBays': [{'bayNumber': 1, 'status': 'OK', 'devicePresence': 'Present'},
                                          {'bayNumber': 2, 'status': 'OK', 'devicePresence': 'Present'}]}]

support_dump = [{"errorCode": "CI", "encrypt": False}]

le_support_dump = [{"name": "LE-TB1", "errorCode": "LESD1", "encrypt": True, "excludeApplianceDump": False}]

# SPP data
spp_local_path = DD.get_spp_path(spp_name, spp_local_dir)
expected_spp = DD.expected_spp_data(spp_name)

# Users data
users = DD.users_data(users_name)
expected_users = DD.expected_users_data(users_name)

# SAN managers data
san_managers = DD.create_san_manager_data(sans)
expected_san_managers = DD.get_expected_san_manager_data(sans)

# Ethernet Networks data
expected_ethernet_networks = DD.get_expected_ethernet_data(ethernet_networks)

# Fiber channel Networks data
expected_fc_networks = DD.get_expected_fcnet_data(fc_networks)

# FCoE Networks data
expected_fcoe_networks = DD.get_expected_fcoenet_data(fcoe_networks)

# Network Sets data
expected_networksets = DD.get_expected_network_set_data(network_sets)

# Enclosure Group data
expected_encgroups = DD.make_expected_enc_group_data(enc_groups)

# Storage Systems data
expected_storage_systems = DD.expected_storage_system(storage_systems)

# Storage Volumes data
storage_volumes_add = DD.existing_storage_volumes(existing_storage_volumes)
expected_existing_storage_volumes = DD.expected_storage_volumes(existing_storage_volumes)

# Logical Enclosure data
expected_logical_enclosure = DD.make_expected_logical_enclosure_data(logical_enclosure)

# Server Profile data
server_profiles = DD.make_server_profile_data(server_profile_data, firmware)
expected_server_profiles = DD.make_expected_server_profile_data(server_profile_data, firmware)
expected_server_profiles_from_spt = DD.make_expected_server_profile_from_spt_data(server_profiles_from_spt, server_profile_templates)

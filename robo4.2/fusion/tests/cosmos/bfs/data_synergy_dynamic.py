"""
    This module has been used to create json data
    will be used for generating json data
"""

from DynamicData_Synergy import DynamicData
import copy

DD = DynamicData()

admin_credentials = {'userName': 'Administrator', 'password': 'Cosmos123'}

ilo_credentials = {'username': 'Admin', 'password': 'Cosmos123'}

dhcpservers = [{'ip': '10.133.0.12', 'vlanid': '1133', 'scope': '10.133.0.0', 'username': 'Administrator', 'password': 'Cosmos123'}]

gen10snap = '/rest/firmware-drivers/bp-2019-03-21'

firmware = {'manageFirmware': False, 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareBaselineUri': None}

update_firmware = {'manageFirmware': True, 'forceInstallFirmware': True, 'firmwareInstallType': 'FirmwareAndOSDrivers', 'firmwareBaselineUri': gen10snap}

unassign = True
critical = 'Critical'
ok = 'OK'

cleanup_ilo = [{'ilo': '10.133.12.92', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.48', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.39', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.60', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.18', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.22', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.23', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.15', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.17', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.76', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.87', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.78', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.8', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.63', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.32', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.82', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.38', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.58', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.5', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.64', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.65', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.9', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.59', 'username': 'Admin', 'password': 'Cosmos123'},
               {'ilo': '10.133.12.29', 'username': 'Admin', 'password': 'Cosmos123'}]

cleanup_zone = [{'sanName': 'Syn-Auto-Fab1-10:00:50:eb:1a:87:fc:b9'},
                {'sanName': 'Syn-Auto-Fab2-10:00:50:eb:1a:87:fc:ba'},
                {'sanName': 'VSAN3701'},
                {'sanName': 'VSAN3702'}]

licenses = [{'key': '9B2G D9MA H9PA CHVZ V2B4 HWWV Y9JL KMPL B89H MZVU 6RMS 9HWE 92R6 3FZ3 CMRG HPMR MFVU A5K9 MHGK EKX9 HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 \
R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'YBKA D9MA H9P9 8HX3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE J2SP XNZ8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 \
            R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'},
            {'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 \
            R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'}]

sans = [{'Type': 'Brocade Network Advisor',
         'Host': '10.120.1.57',
         'Port': 5989,
         'Username': 'Administrator',
         'Password': 'Cosmos123', 'UseSsl': True},
        {'Type': 'HPE',
         'Host': '10.120.1.52',
         'SnmpPort': 161,
         'SnmpUserName': 'defaultUser',
         'SnmpAuthLevel': 'authpriv',
         'SnmpAuthProtocol': 'md5',
         'SnmpAuthString': 'authPass123',
         'SnmpPrivProtocol': 'aes',
         'SnmpPrivString': 'privPass123'}]

ethernet_networks = [{'name': 'eth1', 'type': 'ethernet-networkV4', 'vlanId': 1133, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False}]

fc_networks = [{'name': 'fc1', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:Syn-Auto-Fab1-10:00:50:eb:1a:87:fc:b9', 'fabricType': 'FabricAttach'},
               {'name': 'fc2', 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True,
                'connectionTemplateUri': None, 'managedSanUri': 'FCSan:Syn-Auto-Fab2-10:00:50:eb:1a:87:fc:ba', 'fabricType': 'FabricAttach'}, ]

fcoe_networks = [{'name': 'fcoe1', 'type': 'fcoe-networkV4', 'vlanId': 3701, 'managedSanUri': 'FCSan:VSAN3701'},
                 {'name': 'fcoe2', 'type': 'fcoe-networkV4', 'vlanId': 3702, 'managedSanUri': 'FCSan:VSAN3702'}]

iscsi_networks = [{"vlanId": "1121", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI1", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"},
                  {"vlanId": "1122", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI2", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"},
                  {"vlanId": "1120", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI3", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"},
                  {"vlanId": "1120", "ethernetNetworkType": "Tagged", "purpose": "ISCSI", "name": "iSCSI4", "smartLink": True, "privateNetwork": False, "type": "ethernet-networkV4"}]

uplink_sets = {
    'ETH': {'name': 'ETH', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['eth1', 'iSCSI1', 'iSCSI2', 'iSCSI3'],
            'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "1", 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}, {"enclosure": "1", 'bay': '3', 'port': 'Q2', 'speed': 'Auto'},
                                                       {"enclosure": "2", 'bay': '6', 'port': 'Q1', 'speed': 'Auto'}, {"enclosure": "2", 'bay': '6', 'port': 'Q2', 'speed': 'Auto'}]},
    'FC_A': {'name': 'FC_A', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc1'],
             'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "1", 'bay': '3', 'port': 'Q5:1', 'speed': 'Auto'}, {"enclosure": "1", 'bay': '3', 'port': 'Q6:1', 'speed': 'Auto'}]},
    'FC_B': {'name': 'FC_B', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc2'],
             'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "2", 'bay': '6', 'port': 'Q5:1', 'speed': 'Auto'}, {"enclosure": "2", 'bay': '6', 'port': 'Q6:1', 'speed': 'Auto'}]},
    'FCOE1': {'name': 'FCOE1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe1'],
              'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "1", 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}, {"enclosure": "1", 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}]},
    'FCOE2': {'name': 'FCOE2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['fcoe2'],
              'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "2", 'bay': '6', 'port': 'Q3', 'speed': 'Auto'}, {"enclosure": "2", 'bay': '6', 'port': 'Q4', 'speed': 'Auto'}]},
    'FC_Carbon_1': {'name': 'FC_Carbon_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc1'],
                    'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "-1", 'bay': '1', 'port': '1', 'speed': 'Auto'}]},
    'FC_Carbon_2': {'name': 'FC_Carbon_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': 'NotApplicable', 'networkUris': ['fc2'],
                    'mode': 'Auto', 'logicalPortConfigInfos': [{"enclosure": "-1", 'bay': '4', 'port': '1', 'speed': 'Auto'}]}}

ligs = [{"name": "Potash", "type": "logical-interconnect-groupV7", "enclosureType": "SY12000",
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True},
         "interconnectMapTemplate": [{"enclosureIndex": 3, "enclosure": 3, "bay": 6, "type": "Synergy 10Gb Interconnect Link Module"},
                                     {"enclosureIndex": 2, "bay": 6, "enclosure": 2, "type": "Virtual Connect SE 40Gb F8 Module for Synergy"},
                                     {"enclosureIndex": 1, "bay": 3, "enclosure": 1, "type": "Virtual Connect SE 40Gb F8 Module for Synergy"},
                                     {"enclosureIndex": 1, "bay": 6, "enclosure": 1, "type": "Synergy 20Gb Interconnect Link Module"},
                                     {"enclosureIndex": 3, "enclosure": 3, "bay": 3, "type": "Synergy 10Gb Interconnect Link Module"},
                                     {"enclosureIndex": 2, "bay": 3, "enclosure": 2, "type": "Synergy 20Gb Interconnect Link Module"},
                                     {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
         "interconnectBaySet": 3, "redundancyType": "HighlyAvailable", "telemetryConfiguration": {"enableTelemetry": True, "sampleCount": 12, "sampleInterval": 300},
         'uplinkSets': [uplink_sets['ETH'].copy(), uplink_sets['FC_A'].copy(), uplink_sets['FC_B'].copy(), uplink_sets['FCOE1'].copy(), uplink_sets['FCOE2'].copy()],
         "enclosureIndexes": [1, 2, 3]},
        {'name': 'carbon', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'SY12000',
         "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                              "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": False},
         'uplinkSets': [uplink_sets['FC_Carbon_1'].copy(), uplink_sets['FC_Carbon_2'].copy()], 'description': None, "interconnectBaySet": 1, "redundancyType": "Redundant", "enclosureIndexes": [-1],
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}, ], }, ]

expected_lig = [{'type': 'logical-interconnect-groupV7', 'enclosureType': 'SY12000', 'enclosureIndexes': [1, 2, 3], 'name': 'Potash', 'state': 'Active', 'status': None,
                 'category': 'logical-interconnect-groups', 'uri': 'LIG:Potash',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": True}, },
                {'name': 'carbon', 'type': 'logical-interconnect-groupV7', 'enclosureType': 'SY12000', 'state': 'Active', 'status': None, 'uri': 'LIG:carbon',
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV6", "enableFastMacCacheFailover": True, "enableIgmpSnooping": False, "enableNetworkLoopProtection": True,
                                      "enablePauseFloodProtection": True, "igmpIdleTimeoutInterval": 260, "interconnectType": "Ethernet", "macRefreshInterval": 5, "enableTaggedLldp": False}, }, ]

encgroups_add = [{'name': 'eg', 'interconnectBayMappings': [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:Potash'},
                                                            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:Potash'},
                                                            {'enclosureIndex': 2, 'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:carbon'},
                                                            {'enclosureIndex': 2, 'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:carbon'}],
                  'configurationScript': '', 'ipAddressingMode': "DHCP", 'enclosureCount': 3}, ]

storage_systems = [{'name': 'TBRack5-P7200C', 'family': 'StoreServ', "hostname": "10.120.1.59",
                    "credentials": {"username": "cosmos", "password": "Insight7"}, "serialNumber": "1675724",
                    'deviceSpecificAttributes': {'managedDomain': 'T01', 'managedPools': []}},
                   {'name': 'cosmos-vsa-cluster', 'family': 'StoreVirtual', "hostname": "10.120.0.204",
                    "credentials": {"username": "cosmosvsa", "password": "Cosmos123"},
                    "ports": [{"name": "10.120.0.204", "expectedNetworkUri": "ETH:iSCSI3",
                               "expectedNetworkName": "iSCSI3", "mode": "Managed"}]}]

storage_pools = [{"storageSystemUri": 'TBRack5-P7200C', "name": 'T01-FC-R1', "isManaged": True},
                 {"storageSystemUri": 'cosmos-vsa-cluster', "name": 'cosmos-vsa-cluster', "isManaged": True}]

storage_volumes = [{"storageSystemUri": "TBRack5-P7200C", "name": "rhel76-quartz16gb-fc"}, {"storageSystemUri": "TBRack5-P7200C", "name": "rhel76-quartz16gb-fc-vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "ESX65U2-Bronco-FC_Run1"}, {"storageSystemUri": "TBRack5-P7200C", "name": "ESX65U2-Bronco-FC_Run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Electron16GB-FC_run2_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Electron16GB-FC_run2_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "Win2019_Bronco_FC_Run1_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "Win2019_Bronco_FC_Run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "SLES12SP3_Quiz_FC_Run1_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "SLES12SP3_Quiz_FC_Run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL76-Bronco-FCoE_run1_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL76-Bronco-FCoE_run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Bronco-FCoE_run1_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Bronco-FCoE_run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "rhel76-quartz-fc"}, {"storageSystemUri": "TBRack5-P7200C", "name": "rhel7-quartz16gb-fc-vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "rhel75-bronco-fc"}, {"storageSystemUri": "TBRack5-P7200C", "name": "rhel75-bronco-fc-vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "rhel75-quartz-fc"}, {"storageSystemUri": "TBRack5-P7200C", "name": "rhel75-quartz-fc-vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "rhel75-bronco-fcoe"}, {"storageSystemUri": "TBRack5-P7200C", "name": "rhel75-bronco-fcoe-vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "Win2016-Bronco-FCoE_Run1"}, {"storageSystemUri": "TBRack5-P7200C", "name": "Win2016-Bronco-FCoE_Run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "ESX67U1-Bronco-FC_Run1"}, {"storageSystemUri": "TBRack5-P7200C", "name": "ESX67U1-Bronco-FC_Run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "ESXi65u2_fcoe_bronco_run1_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "ESXi65u2_fcoe_bronco_run1_vol2"},
                   {"storageSystemUri": "cosmos-vsa-cluster", "name": "iscsi-case12-rhel75"},
                   {"storageSystemUri": "cosmos-vsa-cluster", "name": "win2019-iscsi-bronco-vol"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "Esxi65U2-Quartz-FC-Run2"}, {"storageSystemUri": "TBRack5-P7200C", "name": "Esxi65U2-Quartz-FC-Run2-Vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "Win2012R2-Quiz-FC_Run1"}, {"storageSystemUri": "TBRack5-P7200C", "name": "Win2012R2-Quiz-FC_Run1_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "Sles12SP3_Quiz_FCOE_Run1"}, {"storageSystemUri": "TBRack5-P7200C", "name": "Sles12SP3-Quiz-FCOE-Run1-Vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "win2016-quartz16-fc-vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "win2016-quartz16-fc-vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL75-Electron-FC_Vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL75-Electron-FC_Vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Bronco-FC_Vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Bronco-FC_Vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL610-Quartz16GB-FC_Run2_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL610-Quartz16GB-FC_Run2_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Quartz16GB-FC_Run2_vol"}, {"storageSystemUri": "TBRack5-P7200C", "name": "SLES15-Quartz16GB-FC_Run2_vol2"},
                   {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL610-Electorn16GB-FC_Run2"}, {"storageSystemUri": "TBRack5-P7200C", "name": "RHEL610-Electorn16GB-FC_Run2_vol2"}]

logical_enclosure = [{'name': 'LE', 'enclosureUris': ['ENC:CN7545048H', 'ENC:CN75140CPT', 'ENC:CN7544044F'], 'enclosureGroupUri': 'EG:eg'}]

expected_logical_enclosure = [{'type': 'LogicalEnclosureV5', 'name': 'LE', 'status': 'OK', 'enclosureUris': ['ENC:CN7545048H', 'ENC:CN75140CPT', 'ENC:CN7544044F'], 'enclosureGroupUri': 'EG:eg'}]

efuse_interconnect = [{'encl_serial': 'CN75140CPT', 'interconnect_bay': 1}, {'encl_serial': 'CN7545048H', 'interconnect_bay': 3}]

icm_sidea = [{'name': 'CN75140CPT, interconnect 1'}, {'name': 'CN7545048H, interconnect 3'}]

le_names_firmware_update = [{'name': 'LE'}]

iometer_server_profile = {"server_details": [
    {"IOmeter_Target_profile_name": "fc_case08_bay07_rhel7.3", "target_disk": ['sda'], "IOmeter_Target_username": "root",
     "IOmeter_Target_password": "Cosmos123", "os_type": "rhel73"},
    {"IOmeter_Target_profile_name": "iscsi_case12_bay07_rhel7.4", "target_disk": ['sda'], "IOmeter_Target_username": "root",
     "IOmeter_Target_password": "Cosmos123", "os_type": "rhel74"},
    {"IOmeter_Target_profile_name": "fc_case10_bay6_sles11sp4", "target_disk": ['sda'], "IOmeter_Target_username": "root",
     "IOmeter_Target_password": "Cosmos123", "os_type": "sles11sp4"},
    {"IOmeter_Target_profile_name": "fcoe_case23_quiz_sles12_sp3", "target_disk": ['sda'], "IOmeter_Target_username": "root",
     "IOmeter_Target_password": "Cosmos123", "os_type": "sles12"}]}

win_os_servers_case46 = [{"name": "fc_case16_bay04_win2k16", 'serverHardwareUri': 'CN7545048H, bay 4'},
                         {"name": "iscsi_case46_win2016", 'serverHardwareUri': 'CN75140CPT, bay 3'}]

win_os_servers_case01 = [{"name": "fc_case16_bay04_win2k16", 'serverHardwareUri': 'CN7545048H, bay 4'},
                         {"name": "fc_nat_case01_win2016", 'serverHardwareUri': 'CN75140CPT, bay 5'}]

win_os_servers_fcoe_case01 = [{"name": "fc_case16_bay04_win2k16", 'serverHardwareUri': 'CN7545048H, bay 4'},
                              {"name": "fcoe_case1_bay2_win2016", 'serverHardwareUri': 'CN7544044F, bay 2'}]

stress_tool = {"username": "Administrator", "password": "Cosmos123", "etdpath": "C:\\Users\\Administrator\\Desktop\\ETD\\etdntmg.exe",
               "inipath": "C:\\Users\\Administrator\\Desktop\\ETD\\default1.ini", "DriverName": "K", "filename": "default1.ini",
               "dest": "\C$\Users\Administrator\Desktop\ETD", "source": "C:\Users\kushari\Desktop\default1.ini", "target": "K:\default1.ini"}

win_name = [{"shared_folder": "test"}]

tor_failover_a_side = [{"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE1/1/25', 'interconnect_port': 'Q1',
                        'interconnect_name': 'CN7545048H, interconnect 3'},
                       {"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE2/1/25', 'interconnect_port': 'Q2',
                        'interconnect_name': 'CN7545048H, interconnect 3'},
                       {"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE1/3/25', 'interconnect_port': 'Q3',
                        'interconnect_name': 'CN7545048H, interconnect 3'},
                       {"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE1/3/26', 'interconnect_port': 'Q4',
                        'interconnect_name': 'CN7545048H, interconnect 3'}]

tor_failover_b_side = [{"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE1/1/26', 'interconnect_port': 'Q1',
                        'interconnect_name': 'CN75140CPT, interconnect 6'},
                       {"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE2/1/26', 'interconnect_port': 'Q2',
                        'interconnect_name': 'CN75140CPT, interconnect 6'},
                       {"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE2/3/25', 'interconnect_port': 'Q3',
                        'interconnect_name': 'CN75140CPT, interconnect 6'},
                       {"switchIP": "10.120.1.52", "switchport": "22", "switchUsername": 'administrator', 'switchPassword': 'Cosmos123', 'PortName': 'FortyGigE2/3/26', 'interconnect_port': 'Q4',
                        'interconnect_name': 'CN75140CPT, interconnect 6'}]

failure_uplink = {'interconnect_a_side': [{"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3",
                                           "portId": "Q1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q1"},
                                          {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3",
                                           "portId": "Q2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q2"},
                                          {"associatedUplinkSetUri": "FC_A", "interconnectName": "CN7545048H, interconnect 3",
                                           "portId": "Q5:1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "Q5:1"},
                                          {"associatedUplinkSetUri": "FC_A", "interconnectName": "CN7545048H, interconnect 3",
                                           "portId": "Q6:1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "Q6:1"},
                                          {"associatedUplinkSetUri": "FCOE1", "interconnectName": "CN7545048H, interconnect 3",
                                           "portId": "Q3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q3"},
                                          {"associatedUplinkSetUri": "FCOE1", "interconnectName": "CN7545048H, interconnect 3",
                                           "portId": "Q4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q4"},
                                          {"associatedUplinkSetUri": "FC_Carbon_1", "interconnectName": "CN75140CPT, interconnect 1",
                                           "portId": "1", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                           "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "1"}],
                  'interconnect_b_side': [{"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6",
                                           "portId": "Q1", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q1"},
                                          {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6",
                                           "portId": "Q2", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q2"},
                                          {"associatedUplinkSetUri": "FC_B", "interconnectName": "CN75140CPT, interconnect 6",
                                           "portId": "Q5:1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "Q5:1"},
                                          {"associatedUplinkSetUri": "FC_B", "interconnectName": "CN75140CPT, interconnect 6",
                                           "portId": "Q6:1", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes": ["FibreChannel"], "portName": "Q6:1"},
                                          {"associatedUplinkSetUri": "FC_Carbon_2", "interconnectName": "CN75140CPT, interconnect 4",
                                           "portId": "1", "capability": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"],
                                           "configPortTypes": ["ConnectionDeployment", "FibreChannel", "ConnectionReservation"], "portName": "1"},
                                          {"associatedUplinkSetUri": "FCOE2", "interconnectName": "CN75140CPT, interconnect 6",
                                           "portId": "Q3", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q3"},
                                          {"associatedUplinkSetUri": "FCOE2", "interconnectName": "CN75140CPT, interconnect 6",
                                           "portId": "Q4", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["Ethernet", "EnetFcoe"], "portName": "Q4"}, ], }

interconnect_aside_disable = DD.make_uplink_disable(failure_uplink['interconnect_a_side'], critical)
interconnect_aside_enable = DD.make_uplink_enable(failure_uplink['interconnect_a_side'], ok)
interconnect_bside_disable = DD.make_uplink_disable(failure_uplink['interconnect_b_side'], critical)
interconnect_bside_enable = DD.make_uplink_enable(failure_uplink['interconnect_b_side'], ok)

failure_downlink = {'interconnect_a_side': [{"associatedUplinkSetUri": "FC_Carbon_1", "interconnectName": "CN75140CPT, interconnect 1",
                                             "portId": "d6", "capability": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"], "portName": "d6"},
                                            {"associatedUplinkSetUri": "FC_Carbon_1", "interconnectName": "CN75140CPT, interconnect 1",
                                             "portId": "d11", "capability": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"], "portName": "d11"},
                                            {"associatedUplinkSetUri": "FC_Carbon_1", "interconnectName": "CN75140CPT, interconnect 1",
                                             "portId": "d12", "capability": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"], "portName": "d12"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d1",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d1"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d2",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d2"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d3",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d3"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d4",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d4"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d15",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d15"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d17",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d17"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d18",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d18"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d19",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d19"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d20",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d20"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d21",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d21"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d22",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d22"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d23",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d23"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d24",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d24"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d25",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d25"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d26",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d26"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d27",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d27"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d28",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d28"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d31",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d31"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN7545048H, interconnect 3", "portId": "d32",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d32"}],
                    'interconnect_b_side': [{"associatedUplinkSetUri": "FC_Carbon_2", "interconnectName": "CN75140CPT, interconnect 4", "portId": "d6",
                                             "capability": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"], "portName": "d6"},
                                            {"associatedUplinkSetUri": "FC_Carbon_2", "interconnectName": "CN75140CPT, interconnect 4", "portId": "d11",
                                             "capability": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"], "portName": "d11"},
                                            {"associatedUplinkSetUri": "FC_Carbon_2", "interconnectName": "CN75140CPT, interconnect 4", "portId": "d12",
                                             "capability": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionDeployment", "FibreChannel"], "portName": "d12"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d3",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d3"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d5",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d5"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d6",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d6"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d7",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d7"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d8",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d8"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d9",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d9"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d10",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d10"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d11",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d11"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d12",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d12"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d13",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d13"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d14",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d14"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d15",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d15"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d16",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d16"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d25",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d25"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d26",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d26"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d27",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d27"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d28",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d28"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d31",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d31"},
                                            {"associatedUplinkSetUri": "ETH", "interconnectName": "CN75140CPT, interconnect 6", "portId": "d32",
                                             "capability": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                            "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"],
                                             "configPortTypes": ["ConnectionReservation", "ConnectionVirtualWWN", "Qbg", "SRIOV", "ConnectionDeployment",
                                                                 "iSCSI", "Ethernet", "ConnectionBandwidthConfiguration", "EnetFcoe"], "portName": "d32"}], }

interconnect_down_aside_disable = DD.make_downlink_disable(failure_downlink['interconnect_a_side'], critical)
interconnect_down_aside_enable = DD.make_downlink_enable(failure_downlink['interconnect_a_side'], ok)
interconnect_down_bside_disable = DD.make_downlink_disable(failure_downlink['interconnect_b_side'], critical)
interconnect_down_bside_enable = DD.make_downlink_enable(failure_downlink['interconnect_b_side'], ok)

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

############################################################################################
# rhel76-quartz16gb-fc-run2 bay12 profile test data for gen10 server Synergy 3830C 16Gb CNA OS is RHEL 7.6
############################################################################################

rhel76_quartz16gb_fc_run2_profile_data = [{'name': 'rhel76-quartz-fc-run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 12', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                           "iscsiInitiatorNameType": "AutoGenerated",
                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                   "macType": "UserDefined", "mac": "BA:07:CC:20:00:2C", 'networkUri': 'ETH:eth1',
                                                                                   'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                   "macType": "UserDefined", "mac": "BA:07:CC:20:00:2D", 'networkUri': 'ETH:eth1',
                                                                                   'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'networkUri': 'FC:fc1',
                                                                                   'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                  {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", "networkUri": "FC:fc2",
                                                                                   "boot": {"priority": "Secondary", 'bootVolumeSource': 'ManagedVolume'}}], },
                                           'serverHardwareTypeUri': 'SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                           "boot": {"order": ["HardDisk"], "manageBoot": True},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                           'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel76-quartz-fc", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]},
                                                                               ]}}]

rhel76_quartz16gb_fc_run2_profile = DD.make_server_profile_data(rhel76_quartz16gb_fc_run2_profile_data, firmware)
rhel76_quartz16gb_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel76_quartz16gb_fc_run2_profile_data, firmware)
rhel76_quartz16gb_fc_run2_profile_add_volume_data = copy.deepcopy(rhel76_quartz16gb_fc_run2_profile_data)
rhel76_quartz16gb_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel76_quartz16gb_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                      "SVOL:rhel7-quartz16gb-fc-vol2")
rhel76_quartz16gb_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel76_quartz16gb_fc_run2_profile_add_volume_data, firmware)
rhel76_quartz16gb_fc_run2_profile_spp = DD.make_server_profile_data(rhel76_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)
rhel76_quartz16gb_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(rhel76_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
#  SLES12SP3_Quiz_FC_Run1 Gen10
############################################################################################
sles12sp3_quiz_fc_run1_profile_data = [{'name': 'SLES12SP3_Quiz_FC_Run1', 'serverHardwareUri': 'SH:CN7544044F, bay 4', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                        "iscsiInitiatorNameType": "AutoGenerated",
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:4E', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:4F', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:50', 'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:51', "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 2820C 10Gb CNA',
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SLES12SP3_Quiz_FC_Run1_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

sles12sp3_quiz_fc_run1_profile = DD.make_server_profile_data(sles12sp3_quiz_fc_run1_profile_data, firmware)
sles12sp3_quiz_fc_run1_profile_expected = DD.make_expected_server_profile_data(sles12sp3_quiz_fc_run1_profile_data, firmware)
sles12sp3_quiz_fc_run1_profile_add_volume_data = copy.deepcopy(sles12sp3_quiz_fc_run1_profile_data)
sles12sp3_quiz_fc_run1_profile_add_volume = DD.make_server_profile_add_volume_data(sles12sp3_quiz_fc_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:SLES12SP3_Quiz_FC_Run1_vol2")
sles12sp3_quiz_fc_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(sles12sp3_quiz_fc_run1_profile_add_volume_data, firmware)
sles12sp3_quiz_fc_run1_profile_spp = DD.make_server_profile_data(sles12sp3_quiz_fc_run1_profile_add_volume_data, update_firmware)
sles12sp3_quiz_fc_run1_profile_spp_expected = DD.make_expected_server_profile_data(sles12sp3_quiz_fc_run1_profile_add_volume_data, update_firmware)

############################################################################################
# win2019_Bronco_fc_run1 gen9
############################################################################################
win2019_bronco_fc_run1_profile_data = [{'name': 'Win2019_Bronco_FC_Run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 2', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                        "iscsiInitiatorNameType": "AutoGenerated",
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:46', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:47', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'macType': 'UserDefined',
                                                                                'mac': '2A:79:6C:90:00:48', 'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'macType': 'UserDefined',
                                                                                'mac': '2A:79:6C:90:00:49', "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}},
                                                                               ], },
                                        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Win2019_Bronco_FC_Run1_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_bronco_fc_run1_profile = DD.make_server_profile_data(win2019_bronco_fc_run1_profile_data, firmware)
win2019_bronco_fc_run1_profile_expected = DD.make_expected_server_profile_data(win2019_bronco_fc_run1_profile_data, firmware)
win2019_bronco_fc_run1_profile_add_volume_data = copy.deepcopy(win2019_bronco_fc_run1_profile_data)
win2019_bronco_fc_run1_profile_add_volume = DD.make_server_profile_add_volume_data(win2019_bronco_fc_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:Win2019_Bronco_FC_Run1_vol2")
win2019_bronco_fc_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(win2019_bronco_fc_run1_profile_add_volume_data, firmware)
win2019_bronco_fc_run1_profile_spp = DD.make_server_profile_data(win2019_bronco_fc_run1_profile_add_volume_data, update_firmware)
win2019_bronco_fc_run1_profile_spp_expected = DD.make_expected_server_profile_data(win2019_bronco_fc_run1_profile_add_volume_data, update_firmware)

############################################################################################
# ESX65U2_Bronco_FC_Run1 Gen9
############################################################################################
esx65u2_bronco_fc_run1_profile_data = [{'name': 'ESX65U2-Bronco-FC_Run1', 'serverHardwareUri': 'SH:CN7545048H, bay 1', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                        "iscsiInitiatorNameType": "AutoGenerated",
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:04', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:05', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:06', 'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:07', "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:Synergy 3820C 10/20Gb CNA',
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:ESX65U2-Bronco-FC_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

esx65u2_bronco_fc_run1_profile = DD.make_server_profile_data(esx65u2_bronco_fc_run1_profile_data, firmware)
esx65u2_bronco_fc_run1_profile_expected = DD.make_expected_server_profile_data(esx65u2_bronco_fc_run1_profile_data, firmware)
esx65u2_bronco_fc_run1_profile_add_volume_data = copy.deepcopy(esx65u2_bronco_fc_run1_profile_data)
esx65u2_bronco_fc_run1_profile_add_volume = DD.make_server_profile_add_volume_data(esx65u2_bronco_fc_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:ESX65U2-Bronco-FC_Run1_vol2")
esx65u2_bronco_fc_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(esx65u2_bronco_fc_run1_profile_add_volume_data, firmware)
esx65u2_bronco_fc_run1_profile_spp = DD.make_server_profile_data(esx65u2_bronco_fc_run1_profile_add_volume_data, update_firmware)
esx65u2_bronco_fc_run1_profile_spp_expected = DD.make_expected_server_profile_data(esx65u2_bronco_fc_run1_profile_add_volume_data, update_firmware)

############################################################################################
#  SLES15-Electron16GB-FC_Run2 Gen10
############################################################################################
sles15_electron16gb_fc_run2_profile_data = [{'name': 'SLES15-Electron16GB-FC_Run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 6', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                             "iscsiInitiatorNameType": "AutoGenerated",
                                             'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                     'mac': '2A:79:6C:90:00:14', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                    {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                     'mac': '2A:79:6C:90:00:15', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                    {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                                                                     'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:16', 'networkUri': 'FC:fc1',
                                                                                     'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                    {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2",
                                                                                     'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:17', "networkUri": "FC:fc2",
                                                                                     "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                             'serverHardwareTypeUri': 'SHT:SY 480 Gen10:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA',
                                             "boot": {"order": ["HardDisk"], "manageBoot": True},
                                             'bios': {'manageBios': False, 'overriddenSettings': []},
                                             "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                             'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                             'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                             'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                           'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SLES15-Electron16GB-FC_run2_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                   {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

sles15_electron16gb_fc_run2_profile = DD.make_server_profile_data(sles15_electron16gb_fc_run2_profile_data, firmware)
sles15_electron16gb_fc_run2_profile_expected = DD.make_expected_server_profile_data(sles15_electron16gb_fc_run2_profile_data, firmware)
sles15_electron16gb_fc_run2_profile_add_volume_data = copy.deepcopy(sles15_electron16gb_fc_run2_profile_data)
sles15_electron16gb_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(sles15_electron16gb_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                        "SVOL:SLES15-Electron16GB-FC_run2_vol2")
sles15_electron16gb_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(sles15_electron16gb_fc_run2_profile_add_volume_data, firmware)
sles15_electron16gb_fc_run2_profile_spp = DD.make_server_profile_data(sles15_electron16gb_fc_run2_profile_add_volume_data, update_firmware)
sles15_electron16gb_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(sles15_electron16gb_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# rhel75_bronco_iscsi_run1 gen9
############################################################################################

rhel75_bronco_iscsi_run1_profile_data = [{'name': 'rhel75-bronco-iscsi-run1', 'serverHardwareUri': 'SH:CN7544044F, bay 7', 'description': '', 'affinity': 'Bay', 'enclosureGroupUri': 'EG:eg',
                                          'iscsiInitiatorName': 'iqn.2015-02.com.hpe:oneview-vcgekbi018', "iscsiInitiatorNameType": "UserDefined",
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                  "macType": "UserDefined", "mac": "A6:3F:C2:A0:00:2D", 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                  "macType": "UserDefined", "mac": "A6:3F:C2:A0:00:2E", 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                  'networkUri': 'ETH:iSCSI3', "macType": "UserDefined", "mac": "A6:3F:C2:A0:00:2F",
                                                                                  "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "10.120.4.125", "subnetMask": "255.255.0.0",
                                                                                           "gateway": "10.120.0.1"},
                                                                                  'boot': {'priority': 'Primary',
                                                                                           'iscsi': {"initiatorNameSource": "UserDefined",
                                                                                                     "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgekbi018", "mutualChapName": "",
                                                                                                     "bootTargetName": "iqn.2003-10.com.lefthandnetworks:cosmos-vsa-group:1651:iscsi-case12-rhel75",
                                                                                                     "bootTargetLun": "0", "firstBootTargetIp": "10.120.0.204", "firstBootTargetPort": "3260",
                                                                                                     "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": ""},
                                                                                           'bootVolumeSource': 'UserDefined'}},
                                                                                 {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                  "networkUri": "ETH:iSCSI3", "macType": "UserDefined", "mac": "A6:3F:C2:A0:00:30",
                                                                                  "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "10.120.4.126", "subnetMask": "255.255.0.0",
                                                                                           "gateway": "10.120.0.1"},
                                                                                  "boot": {'priority': 'Secondary',
                                                                                           'iscsi': {"initiatorNameSource": "UserDefined",
                                                                                                     "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgekbi018", "chapLevel": "None",
                                                                                                     "bootTargetName": "iqn.2003-10.com.lefthandnetworks:cosmos-vsa-group:1651:iscsi-case12-rhel75",
                                                                                                     "bootTargetLun": "0", "firstBootTargetIp": "10.120.0.204", "firstBootTargetPort": "3260",
                                                                                                     "secondBootTargetIp": "", "secondBootTargetPort": "", "chapName": "", "mutualChapName": ""},
                                                                                           'bootVolumeSource': 'UserDefined'}}]},
                                          'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA',
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4", "secureBoot": "Disabled"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'manageSanStorage': False, 'volumeAttachments': [],
                                                        }}]

rhel75_bronco_iscsi_run1_profile = DD.make_server_profile_data(rhel75_bronco_iscsi_run1_profile_data, firmware)
rhel75_bronco_iscsi_run1_profile_expected = DD.make_server_profile_data(rhel75_bronco_iscsi_run1_profile_data, firmware)
rhel75_bronco_iscsi_run1_profile_spp = DD.make_server_profile_data(rhel75_bronco_iscsi_run1_profile_data, update_firmware)
rhel75_bronco_iscsi_run1_profile_spp_expected = DD.make_expected_server_profile_data(rhel75_bronco_iscsi_run1_profile_data, update_firmware)

############################################################################################
# rhel75_bronco_fc_run1 gen9
############################################################################################
rhel75_bronco_fc_run1_profile_data = [{'name': 'rhel75-bronco-fc-run1', 'serverHardwareUri': 'SH:CN7544044F, bay 1', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                       "iscsiInitiatorNameType": "AutoGenerated",
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                               'mac': 'BA:07:CC:20:00:3A', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                               'mac': 'BA:07:CC:20:00:3B', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                               'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                                                                                "targets": [{"arrayWwpn": "20110002AC0127CC", "lun": "1"}]}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                               "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                                                                                "targets": [{"arrayWwpn": "21110002AC0127CC", "lun": "1"}]}}], },
                                       'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel75-bronco-fc", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                             {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel75_bronco_fc_run1_profile = DD.make_server_profile_data(rhel75_bronco_fc_run1_profile_data, firmware)
rhel75_bronco_fc_run1_profile_expected = DD.make_expected_server_profile_data(rhel75_bronco_fc_run1_profile_data, firmware)
rhel75_bronco_fc_run1_profile_add_volume_data = copy.deepcopy(rhel75_bronco_fc_run1_profile_data)
rhel75_bronco_fc_run1_profile_add_volume = DD.make_server_profile_add_volume_data(rhel75_bronco_fc_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:rhel75-bronco-fc-vol2")
rhel75_bronco_fc_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel75_bronco_fc_run1_profile_add_volume_data, firmware)
rhel75_bronco_fc_run1_profile_spp = DD.make_server_profile_data(rhel75_bronco_fc_run1_profile_add_volume_data, update_firmware)
rhel75_bronco_fc_run1_profile_spp_expected = DD.make_expected_server_profile_data(rhel75_bronco_fc_run1_profile_add_volume_data, update_firmware)

############################################################################################
# RHEL76-Bronco-FCoE_run1 gen9
############################################################################################
RHEL76_Bronco_FCoE_run1_profile_data = [{'name': 'RHEL76-Bronco-FCoE_run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 5', 'enclosureGroupUri': 'EG:eg', 'description': '',
                                         'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                 'mac': '1E:EC:A9:50:00:10', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                 'mac': '1E:EC:A9:50:00:11', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                 'macType': 'UserDefined', 'mac': '1E:EC:A9:50:00:12', 'networkUri': 'FCOE:fcoe1',
                                                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                 'macType': 'UserDefined', 'mac': '1E:EC:A9:50:00:13', "networkUri": "FCOE:fcoe2",
                                                                                 "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                         'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL76-Bronco-FCoE_run1_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

RHEL76_Bronco_FCoE_run1_profile = DD.make_server_profile_data(RHEL76_Bronco_FCoE_run1_profile_data, firmware)
RHEL76_Bronco_FCoE_run1_profile_expected = DD.make_expected_server_profile_data(RHEL76_Bronco_FCoE_run1_profile_data, firmware)
RHEL76_Bronco_FCoE_run1_profile_add_volume_data = copy.deepcopy(RHEL76_Bronco_FCoE_run1_profile_data)
RHEL76_Bronco_FCoE_run1_profile_add_volume = DD.make_server_profile_add_volume_data(RHEL76_Bronco_FCoE_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                    "SVOL:RHEL76-Bronco-FCoE_run1_vol2")
RHEL76_Bronco_FCoE_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(RHEL76_Bronco_FCoE_run1_profile_add_volume_data, firmware)
RHEL76_Bronco_FCoE_run1_profile_spp = DD.make_server_profile_data(RHEL76_Bronco_FCoE_run1_profile_add_volume_data, update_firmware)
RHEL76_Bronco_FCoE_run1_profile_spp_expected = DD.make_expected_server_profile_data(RHEL76_Bronco_FCoE_run1_profile_add_volume_data, update_firmware)

############################################################################################
# SLES15_Bronco_FCoE_run1 gen10
############################################################################################
SLES15_Bronco_FCoE_run1_profile_data = [{'name': 'SLES15-Bronco-FCoE_run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 12', 'enclosureGroupUri': 'EG:eg', 'description': '',
                                         'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                 'mac': '1E:EC:A9:50:00:14', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                 'mac': '1E:EC:A9:50:00:15', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                 'macType': 'UserDefined', 'mac': '1E:EC:A9:50:00:16', 'networkUri': 'FCOE:fcoe1',
                                                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                 'macType': 'UserDefined', 'mac': '1E:EC:A9:50:00:17', "networkUri": "FCOE:fcoe2",
                                                                                 "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}, ], },
                                         'serverHardwareTypeUri': 'SHT:SY 480 Gen10 :1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SLES15-Bronco-FCoE_run1_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

SLES15_Bronco_FCoE_run1_profile = DD.make_server_profile_data(SLES15_Bronco_FCoE_run1_profile_data, firmware)
SLES15_Bronco_FCoE_run1_profile_expected = DD.make_expected_server_profile_data(SLES15_Bronco_FCoE_run1_profile_data, firmware)
SLES15_Bronco_FCoE_run1_profile_add_volume_data = copy.deepcopy(SLES15_Bronco_FCoE_run1_profile_data)
SLES15_Bronco_FCoE_run1_profile_add_volume = DD.make_server_profile_add_volume_data(SLES15_Bronco_FCoE_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                    "SVOL:SLES15-Bronco-FCoE_run1_vol2")
SLES15_Bronco_FCoE_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(SLES15_Bronco_FCoE_run1_profile_add_volume_data, firmware)
SLES15_Bronco_FCoE_run1_profile_spp = DD.make_server_profile_data(SLES15_Bronco_FCoE_run1_profile_add_volume_data, update_firmware)
SLES15_Bronco_FCoE_run1_profile_spp_expected = DD.make_expected_server_profile_data(SLES15_Bronco_FCoE_run1_profile_add_volume_data, update_firmware)

############################################################################################
# rhel75_quartz16gb_fc_run2 gen9
############################################################################################

rhel75_quartz16gb_fc_run2_profile_data = [{'name': 'rhel75-quartz-fc-run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 7', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                           "iscsiInitiatorNameType": "AutoGenerated",
                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                   'mac': 'BA:07:CC:20:00:1C', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                   'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                   'mac': 'BA:07:CC:20:00:1D', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                   'boot': {'priority': 'NotBootable'}}, {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                                                                                                          'networkUri': 'FC:fc1',
                                                                                                                          'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined',
                                                                                                                                   "targets": [{"arrayWwpn": "20110002AC0127CC", "lun": "1"}]}},
                                                                                  {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", "networkUri": "FC:fc2",
                                                                                   "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                                                            "targets": [{"arrayWwpn": "21110002AC0127CC", "lun": "1"}]}}], },
                                           'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
                                           "boot": {"order": ["HardDisk"], "manageBoot": True},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                           'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel75-quartz-fc", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel75_quartz16gb_fc_run2_profile = DD.make_server_profile_data(rhel75_quartz16gb_fc_run2_profile_data, firmware)
rhel75_quartz16gb_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel75_quartz16gb_fc_run2_profile_data, firmware)
rhel75_quartz16gb_fc_run2_profile_add_volume_data = copy.deepcopy(rhel75_quartz16gb_fc_run2_profile_data)
rhel75_quartz16gb_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel75_quartz16gb_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:rhel75-quartz-fc-vol2")
rhel75_quartz16gb_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel75_quartz16gb_fc_run2_profile_add_volume_data, firmware)
rhel75_quartz16gb_fc_run2_profile_spp = DD.make_server_profile_data(rhel75_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)
rhel75_quartz16gb_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(rhel75_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# rhel75_bronco_fcoe_run1 gen9
############################################################################################
rhel75_bronco_fcoe_run1_profile_data = [{'name': 'rhel75-bronco-fcoe-run1', 'serverHardwareUri': 'SH:CN7545048H, bay 3', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                         "iscsiInitiatorNameType": "AutoGenerated",
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                 'mac': 'DA:D9:B2:40:00:06', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                 'mac': 'DA:D9:B2:40:00:07', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                 'macType': 'UserDefined', 'mac': 'DA:D9:B2:40:00:08', 'networkUri': 'FCOE:fcoe1',
                                                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                 'macType': 'UserDefined', 'mac': 'DA:D9:B2:40:00:09', "networkUri": "FCOE:fcoe2",
                                                                                 "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                         'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA',
                                         "boot": {"order": ["HardDisk", "CD", "USB", "PXE"], "manageBoot": True},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": None},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:rhel75-bronco-fcoe", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel75_bronco_fcoe_run1_profile = DD.make_server_profile_data(rhel75_bronco_fcoe_run1_profile_data, firmware)
rhel75_bronco_fcoe_run1_profile_expected = DD.make_expected_server_profile_data(rhel75_bronco_fcoe_run1_profile_data, firmware)
rhel75_bronco_fcoe_run1_profile_add_volume_data = copy.deepcopy(rhel75_bronco_fcoe_run1_profile_data)
rhel75_bronco_fcoe_run1_profile_add_volume = DD.make_server_profile_add_volume_data(rhel75_bronco_fcoe_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:rhel75-bronco-fcoe-vol2")
rhel75_bronco_fcoe_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel75_bronco_fcoe_run1_profile_add_volume_data, firmware)
rhel75_bronco_fcoe_run1_profile_spp = DD.make_server_profile_data(rhel75_bronco_fcoe_run1_profile_add_volume_data, update_firmware)
rhel75_bronco_fcoe_run1_profile_spp_expected = DD.make_expected_server_profile_data(rhel75_bronco_fcoe_run1_profile_add_volume_data, update_firmware)

############################################################################################
# WINDOW 2016-Bronco-FCoE_run1 gen9
############################################################################################
Win2016_Bronco_FCoE_Run1_profile_data = [{'name': 'Win2016-Bronco-FCoE_Run1', 'serverHardwareUri': 'SH:CN7544044F, bay 2', 'enclosureGroupUri': 'EG:eg', 'description': '',
                                          'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '2A:79:6C:90:00:1C', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '2A:79:6C:90:00:1D', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                  'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:1E', 'networkUri': 'FCOE:fcoe1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                  'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:1F', "networkUri": "FCOE:fcoe2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}, ], },
                                          'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA',
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Win2016-Bronco-FCoE_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

Win2016_Bronco_FCoE_Run1_profile = DD.make_server_profile_data(Win2016_Bronco_FCoE_Run1_profile_data, firmware)
Win2016_Bronco_FCoE_Run1_profile_expected = DD.make_expected_server_profile_data(Win2016_Bronco_FCoE_Run1_profile_data, firmware)
Win2016_Bronco_FCoE_Run1_profile_add_volume_data = copy.deepcopy(Win2016_Bronco_FCoE_Run1_profile_data)
Win2016_Bronco_FCoE_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(Win2016_Bronco_FCoE_Run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:Win2016-Bronco-FCoE_Run1_vol2")
Win2016_Bronco_FCoE_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(Win2016_Bronco_FCoE_Run1_profile_add_volume_data, firmware)
Win2016_Bronco_FCoE_Run1_profile_spp = DD.make_server_profile_data(Win2016_Bronco_FCoE_Run1_profile_add_volume_data, update_firmware)
Win2016_Bronco_FCoE_Run1_profile_spp_expected = DD.make_expected_server_profile_data(Win2016_Bronco_FCoE_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# ESX67U1-Bronco-FC_Run1_run1 gen9
############################################################################################
ESX67U1_Bronco_FC_Run1_profile_data = [{'name': 'ESX67U1_Bronco_FC_Run1', 'serverHardwareUri': 'SH:CN7545048H, bay 2', 'enclosureGroupUri': 'EG:eg', 'description': '',
                                        'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:08', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:09', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:10', 'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:11', "networkUri": "FC:fc2",
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}, ], },
                                        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 3820C 10/20Gb CNA',
                                        "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'bios': {'manageBios': False, 'overriddenSettings': []},
                                        "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                        'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:ESX67U1-Bronco-FC_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

ESX67U1_Bronco_FC_Run1_profile = DD.make_server_profile_data(ESX67U1_Bronco_FC_Run1_profile_data, firmware)
ESX67U1_Bronco_FC_Run1_profile_expected = DD.make_expected_server_profile_data(ESX67U1_Bronco_FC_Run1_profile_data, firmware)
ESX67U1_Bronco_FC_Run1_profile_add_volume_data = copy.deepcopy(ESX67U1_Bronco_FC_Run1_profile_data)
ESX67U1_Bronco_FC_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(ESX67U1_Bronco_FC_Run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:ESX67U1-Bronco-FC_Run1_vol2")
ESX67U1_Bronco_FC_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(ESX67U1_Bronco_FC_Run1_profile_add_volume_data, firmware)
ESX67U1_Bronco_FC_Run1_profile_spp = DD.make_server_profile_data(ESX67U1_Bronco_FC_Run1_profile_add_volume_data, update_firmware)
ESX67U1_Bronco_FC_Run1_profile_spp_expected = DD.make_expected_server_profile_data(ESX67U1_Bronco_FC_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# ESX65U2-Bronco-FCoE_Run1_run1 gen9
############################################################################################
ESXi65u2_fcoe_bronco_run1_profile_data = [{'name': 'ESXi65u2_fcoe_bronco_run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 1', 'enclosureGroupUri': 'EG:eg', 'description': '',
                                           'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                   'mac': '2A:79:6C:90:00:4A', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                   'mac': '2A:79:6C:90:00:4B', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                   'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:4C', 'networkUri': 'FCOE:fcoe1',
                                                                                   'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                  {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                   'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:4D', "networkUri": "FCOE:fcoe2",
                                                                                   "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}, ], },
                                           'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA',
                                           "boot": {"order": ["HardDisk"], "manageBoot": True},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                           'sanStorage':{'hostOSType': 'VMware (ESXi)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:ESXi65u2_fcoe_bronco_run1_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

ESXi65u2_fcoe_bronco_run1_profile = DD.make_server_profile_data(ESXi65u2_fcoe_bronco_run1_profile_data, firmware)
ESXi65u2_fcoe_bronco_run1_profile_expected = DD.make_expected_server_profile_data(ESXi65u2_fcoe_bronco_run1_profile_data, firmware)
ESXi65u2_fcoe_bronco_run1_profile_add_volume_data = copy.deepcopy(ESXi65u2_fcoe_bronco_run1_profile_data)
ESXi65u2_fcoe_bronco_run1_profile_add_volume = DD.make_server_profile_add_volume_data(ESXi65u2_fcoe_bronco_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                      "SVOL:ESXi65u2_fcoe_bronco_run1_vol2")
ESXi65u2_fcoe_bronco_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(ESXi65u2_fcoe_bronco_run1_profile_add_volume_data, firmware)
ESXi65u2_fcoe_bronco_run1_profile_spp = DD.make_server_profile_data(ESXi65u2_fcoe_bronco_run1_profile_add_volume_data, update_firmware)
ESXi65u2_fcoe_bronco_run1_profile_spp_expected = DD.make_expected_server_profile_data(ESXi65u2_fcoe_bronco_run1_profile_add_volume_data, update_firmware)

############################################################################################
# win2019-iscsi-bronco-run1 Gen10
############################################################################################
win2019_bronco_iscsi_run1_profile_data = [{'name': 'win2019-iscsi-bronco-run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 10', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                           "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgrpq601f",
                                           "iscsiInitiatorNameType": "UserDefined",
                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                   'mac': '2A:79:6C:90:00:66', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                   'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                   'mac': '2A:79:6C:90:00:67', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                   'boot': {'priority': 'NotBootable'}},
                                                                                  {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 3:1-b', 'requestedMbps': '4000',
                                                                                   'networkUri': 'ETH:iSCSI3', "ipv4": {"ipAddressSource": "DHCP"},
                                                                                   'mac': '2A:79:6C:90:00:68', 'macType': 'UserDefined',
                                                                                   "boot": {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                  {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Mezz 3:2-b", "requestedMbps": "4000",
                                                                                   "networkUri": "ETH:iSCSI3", "ipv4": {"ipAddressSource": "DHCP"},
                                                                                   'mac': '2A:79:6C:90:00:69', 'macType': 'UserDefined',
                                                                                   "boot": {'priority': 'Secondary', 'bootVolumeSource': 'ManagedVolume'}}]},
                                           'serverHardwareTypeUri': 'SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                           "boot": {"order": ["HardDisk"], "manageBoot": True},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'IPv4'},
                                           'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                           'sanStorage':{'hostOSType': 'Windows Server 2019', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2019-iscsi-bronco-vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2019_bronco_iscsi_run1_profile = DD.make_server_profile_data(win2019_bronco_iscsi_run1_profile_data, firmware)
win2019_bronco_iscsi_run1_profile_expected = DD.make_expected_server_profile_data(win2019_bronco_iscsi_run1_profile_data, firmware)
win2019_bronco_iscsi_run1_profile_spp = DD.make_server_profile_data(win2019_bronco_iscsi_run1_profile_data, update_firmware)
win2019_bronco_iscsi_run1_profile_spp_expected = DD.make_expected_server_profile_data(win2019_bronco_iscsi_run1_profile_data, update_firmware)

############################################################################################
# win2016_quartz_fc_run2 gen9
############################################################################################
win2016_quartz16_fc_run2_profile_data = [{'name': 'win2016-Quartz16-FC-Run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 5', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                          "iscsiInitiatorNameType": "AutoGenerated",
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '2A:79:6C:90:00:72', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'lagName': 'LAG1',
                                                                                  'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '2A:79:6C:90:00:73', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'lagName': 'LAG1',
                                                                                  'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'macType': 'UserDefined',
                                                                                  'mac': '2A:79:6C:90:00:74', 'networkUri': 'FC:fc1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", 'macType': 'UserDefined',
                                                                                  'mac': '2A:79:6C:90:00:75', "networkUri": "FC:fc2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                          'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'IPv4'},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:win2016-quartz16-fc-vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

win2016_quartz16_fc_run2_profile = DD.make_server_profile_data(win2016_quartz16_fc_run2_profile_data, firmware)
win2016_quartz16_fc_run2_profile_expected = DD.make_expected_server_profile_data(win2016_quartz16_fc_run2_profile_data, firmware)
win2016_quartz16_fc_run2_profile_add_volume_data = copy.deepcopy(win2016_quartz16_fc_run2_profile_data)
win2016_quartz16_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(win2016_quartz16_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:win2016-quartz16-fc-vol2")
win2016_quartz16_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(win2016_quartz16_fc_run2_profile_add_volume_data, firmware)
win2016_quartz16_fc_run2_profile_spp = DD.make_server_profile_data(win2016_quartz16_fc_run2_profile_add_volume_data, update_firmware)
win2016_quartz16_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(win2016_quartz16_fc_run2_profile_add_volume_data, update_firmware)

#############################################################################################
# rhel76_bronco_iscsi_run1 test data for gen9 server Synergy 3820C 16G. OS is RHEL76
#############################################################################################

rhel76_bronco_iscsi_run1_profile_data = [{'name': 'rhel76-bronco-iscsi-run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 7', 'description': '', 'affinity': 'Bay', 'enclosureGroupUri': 'EG:eg',
                                          'iscsiInitiatorName': 'iqn.2015-02.com.hpe:oneview-vcgrpq6006', "iscsiInitiatorNameType": "UserDefined",
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                  "macType": "UserDefined", "mac": "2A:79:6C:90:00:18", 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                  "macType": "UserDefined", "mac": "2A:79:6C:90:00:19", 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'iSCSI', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                  'networkUri': 'ETH:iSCSI3', "macType": "UserDefined", "mac": "2A:79:6C:90:00:1A",
                                                                                  "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "10.120.4.135", "subnetMask": "255.255.0.0",
                                                                                           "gateway": "10.120.0.1"},
                                                                                  'boot': {'priority': 'Primary',
                                                                                           'iscsi': {"initiatorNameSource": "UserDefined", "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgrpq6006",
                                                                                                     "bootTargetName": "iqn.2003-10.com.lefthandnetworks:cosmos-vsa-group:2952:iscsi-rhel76-bronco-run1",
                                                                                                     "bootTargetLun": "0", "firstBootTargetIp": "10.120.0.204", "firstBootTargetPort": "3260",
                                                                                                     "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "",
                                                                                                     "mutualChapName": ""}, 'bootVolumeSource': 'UserDefined'}},
                                                                                 {"id": 4, "name": "", "functionType": "iSCSI", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                  "networkUri": "ETH:iSCSI3", "macType": "UserDefined", "mac": "2A:79:6C:90:00:1B",
                                                                                  "ipv4": {"ipAddressSource": "UserDefined", "ipAddress": "10.120.4.136", "subnetMask": "255.255.0.0",
                                                                                           "gateway": "10.120.0.1"},
                                                                                  "boot": {'priority': 'Secondary',
                                                                                           'iscsi': {"initiatorNameSource": "UserDefined", "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgrpq6006",
                                                                                                     "bootTargetName": "iqn.2003-10.com.lefthandnetworks:cosmos-vsa-group:2952:iscsi-rhel76-bronco-run1",
                                                                                                     "bootTargetLun": "0", "firstBootTargetIp": "10.120.0.204", "firstBootTargetPort": "3260",
                                                                                                     "secondBootTargetIp": "", "secondBootTargetPort": "", "chapLevel": "None", "chapName": "",
                                                                                                     "mutualChapName": ""}, 'bootVolumeSource': 'UserDefined'}}]},
                                          'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "IPv4", "secureBoot": "Disabled"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'manageSanStorage': False, 'volumeAttachments': [],
                                                        }}]

rhel76_bronco_iscsi_run1_profile = DD.make_server_profile_data(rhel76_bronco_iscsi_run1_profile_data, firmware)
rhel76_bronco_iscsi_run1_profile_expected = DD.make_server_profile_data(rhel76_bronco_iscsi_run1_profile_data, firmware)
rhel76_bronco_iscsi_run1_profile_spp = DD.make_server_profile_data(rhel76_bronco_iscsi_run1_profile_data, update_firmware)
rhel76_bronco_iscsi_run1_profile_spp_expected = DD.make_expected_server_profile_data(rhel76_bronco_iscsi_run1_profile_data, update_firmware)

###########################################################################################
# Sles12SP3_Quiz_FCOE_Run1_profile_data
###########################################################################################
Sles12SP3_Quiz_FCOE_Run1_profile_data = [{'name': 'Sles12SP3_Quiz_FCOE_Run1', 'serverHardwareUri': 'SH:CN7544044F, bay 3', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                          "iscsiInitiatorNameType": "AutoGenerated",
                                          'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                  'mac': '2A:79:6C:90:00:20', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                  'mac': '2A:79:6C:90:00:21', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                 {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                  'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:22', 'networkUri': 'FCOE:fcoe1',
                                                                                  'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                 {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                  'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:23', "networkUri": "FCOE:fcoe2",
                                                                                  "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                          'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 2820C 10Gb CNA',
                                          "boot": {"order": ["HardDisk"], "manageBoot": True},
                                          'bios': {'manageBios': False, 'overriddenSettings': []},
                                          "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                          'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                          'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                          'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                        'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Sles12SP3-Quiz-FCOE-Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                               'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

Sles12SP3_Quiz_FCOE_Run1_profile = DD.make_server_profile_data(Sles12SP3_Quiz_FCOE_Run1_profile_data, firmware)
Sles12SP3_Quiz_FCOE_Run1_profile_expected = DD.make_expected_server_profile_data(Sles12SP3_Quiz_FCOE_Run1_profile_data, firmware)
Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_data = copy.deepcopy(Sles12SP3_Quiz_FCOE_Run1_profile_data)
Sles12SP3_Quiz_FCOE_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:Sles12SP3-Quiz-FCOE-Run1-Vol2")
Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_data, firmware)
Sles12SP3_Quiz_FCOE_Run1_profile_spp = DD.make_server_profile_data(Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_data, update_firmware)
Sles12SP3_Quiz_FCOE_Run1_profile_spp_expected = DD.make_expected_server_profile_data(Sles12SP3_Quiz_FCOE_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# Win2012R2-Quiz-FC_Run1 profile data
############################################################################################
Win2012R2_Quiz_FC_Run1_profile_data = [{'name': 'Win2012R2_Quiz_FC_Run1', 'serverHardwareUri': 'SH:CN7545048H, bay 4', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                        "iscsiInitiatorNameType": "AutoGenerated",
                                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:0C', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                'mac': '2A:79:6C:90:00:0D', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                'boot': {'priority': 'NotBootable'}},
                                                                               {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:0E', 'networkUri': 'FC:fc1',
                                                                                'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                               {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", 'requestedMbps': '2500',
                                                                                'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:0F', 'networkUri': 'FC:fc2',
                                                                                "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:Synergy 2820C 10Gb CNA', "boot": {"order": ["HardDisk"], "manageBoot": True},
                                        'bios': {'manageBios': False, 'overriddenSettings': []}, "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": 'Auto'},
                                        'hideUnusedFlexNics': True, 'osDeploymentSettings': None, 'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                        'sanStorage':{'hostOSType': 'Windows Server 2016', 'manageSanStorage': True,
                                                      'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Win2012R2-Quiz-FC_Run1", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                             'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                              {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

Win2012R2_Quiz_FC_Run1_profile = DD.make_server_profile_data(Win2012R2_Quiz_FC_Run1_profile_data, firmware)
Win2012R2_Quiz_FC_Run1_profile_expected = DD.make_expected_server_profile_data(Win2012R2_Quiz_FC_Run1_profile_data, firmware)
Win2012R2_Quiz_FC_Run1_profile_add_volume_data = copy.deepcopy(Win2012R2_Quiz_FC_Run1_profile_data)
Win2012R2_Quiz_FC_Run1_profile_add_volume = DD.make_server_profile_add_volume_data(Win2012R2_Quiz_FC_Run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                   "SVOL:Win2012R2-Quiz-FC_Run1_vol2")
Win2012R2_Quiz_FC_Run1_profile_add_volume_expected = DD.make_expected_server_profile_data(Win2012R2_Quiz_FC_Run1_profile_add_volume_data, firmware)
Win2012R2_Quiz_FC_Run1_profile_spp = DD.make_server_profile_data(Win2012R2_Quiz_FC_Run1_profile_add_volume_data, update_firmware)
Win2012R2_Quiz_FC_Run1_profile_spp_expected = DD.make_expected_server_profile_data(Win2012R2_Quiz_FC_Run1_profile_add_volume_data, update_firmware)

############################################################################################
# ESX65U2_QUARTZ_FC_RUN2 Bay11 Profile test data for Gen10 server synergy 3830 16GB FC HBA
############################################################################################

Esxi65U2_Quartz_fc_Run2_profile_data = [{'name': 'Esxi65U2_Quartz_fc_Run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 11', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                         "iscsiInitiatorNameType": "AutoGenerated",
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                 "macType": "UserDefined", "mac": "2A:79:6C:90:00:24", 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                 "macType": "UserDefined", "mac": "2A:79:6C:90:00:25", 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'networkUri': 'FC:fc1',
                                                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", "networkUri": "FC:fc2",
                                                                                 "boot": {"priority": "Secondary", 'bootVolumeSource': 'ManagedVolume'}}], },
                                         'serverHardwareTypeUri': 'SHT:SY 480 Gen10:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True}, 'bios': {'manageBios': False, 'overriddenSettings': []},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"}, 'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:Esxi65U2-Quartz-FC-Run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}, ]}}]

Esxi65U2_Quartz_fc_Run2_profile = DD.make_server_profile_data(Esxi65U2_Quartz_fc_Run2_profile_data, firmware)
Esxi65U2_Quartz_fc_Run2_profile_expected = DD.make_expected_server_profile_data(Esxi65U2_Quartz_fc_Run2_profile_data, firmware)
Esxi65U2_Quartz_fc_Run2_profile_add_volume_data = copy.deepcopy(Esxi65U2_Quartz_fc_Run2_profile_data)
Esxi65U2_Quartz_fc_Run2_profile_add_volume = DD.make_server_profile_add_volume_data(Esxi65U2_Quartz_fc_Run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                    "SVOL:Esxi65U2-Quartz-FC-Run2-Vol2")
Esxi65U2_Quartz_fc_Run2_profile_add_volume_expected = DD.make_expected_server_profile_data(Esxi65U2_Quartz_fc_Run2_profile_add_volume_data, firmware)
Esxi65U2_Quartz_fc_Run2_profile_spp = DD.make_server_profile_data(Esxi65U2_Quartz_fc_Run2_profile_add_volume_data, update_firmware)
Esxi65U2_Quartz_fc_Run2_profile_spp_expected = DD.make_expected_server_profile_data(Esxi65U2_Quartz_fc_Run2_profile_add_volume_data, update_firmware)

############################################################################################
# Gen10 server Synergy 3530C 16Gb Fibre Channel HBA. OS - RHEL 7.5 - Run2
############################################################################################
rhel75_electron_fc_run2_profile_data = [{'name': 'RHEL75-Electron-FC', 'serverHardwareUri': 'SH:CN75140CPT, bay 6', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                       'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'mac': '2A:79:6C:90:00:6E', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'mac': '2A:79:6C:90:00:6F', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                              {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                              {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2", "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                       'serverHardwareTypeUri': 'SHT:SY 480 Gen10:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA',
                                       "boot": {"order": ["HardDisk"], "manageBoot": True},
                                       'bios': {'manageBios': False, 'overriddenSettings': []},
                                       "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                                       'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                       'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                       'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                     'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL75-Electron-FC_Vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                            'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                            'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel75_electron_fc_run2_profile = DD.make_server_profile_data(rhel75_electron_fc_run2_profile_data, firmware)
rhel75_electron_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel75_electron_fc_run2_profile_data, firmware)
rhel75_electron_fc_run2_profile_add_volume_data = copy.deepcopy(rhel75_electron_fc_run2_profile_data)
rhel75_electron_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel75_electron_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:RHEL75-Electron-FC_Vol2")
rhel75_electron_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel75_electron_fc_run2_profile_add_volume_data, firmware)
rhel75_electron_fc_run2_profile_spp = DD.make_server_profile_data(rhel75_electron_fc_run2_profile_add_volume_data, update_firmware)
rhel75_electron_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(rhel75_electron_fc_run2_profile_add_volume_data, update_firmware)

###########################################################################################
# Gen10 server Synergy 3530C 16Gb Fibre Channel HBA. OS - RHEL 7.5 - Run2
###########################################################################################
SLES15_Bronco_FC_run1_profile_data = [{'name': 'SLES15-Bronco-FC_run1', 'serverHardwareUri': 'SH:CN75140CPT, bay 6', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                     'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'mac': '1E:EC:A9:50:00:14', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                            {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500', 'mac': '1E:EC:A9:50:00:15', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                            {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'networkUri': 'FC:fc1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                            {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 3:2-b", "networkUri": "FC:fc2", "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}], },
                                     'serverHardwareTypeUri': 'SHT: SY 480 Gen10 :1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA',
                                     "boot": {"order": ["HardDisk"], "manageBoot": True},
                                     'bios': {'manageBios': False, 'overriddenSettings': []},
                                     "bootMode":{"manageMode": True, "mode": "BIOS", "pxeBootPolicy": "Auto"},
                                     'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                     'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                     'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                   'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SLES15-Bronco-FC_Vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto', 'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'}, {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

SLES15_Bronco_FC_run1_profile = DD.make_server_profile_data(SLES15_Bronco_FC_run1_profile_data, firmware)
SLES15_Bronco_FC_run1_profile_expected = DD.make_expected_server_profile_data(SLES15_Bronco_FC_run1_profile_data, firmware)
SLES15_Bronco_FC_run1_profile_add_volume_data = copy.deepcopy(SLES15_Bronco_FC_run1_profile_data)
SLES15_Bronco_FC_run1_profile_add_volume = DD.make_server_profile_add_volume_data(SLES15_Bronco_FC_run1_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C', "SVOL:SLES15-Bronco-FC_Vol2")
SLES15_Bronco_FC_run1_profile_add_volume_expected = DD.make_expected_server_profile_data(SLES15_Bronco_FC_run1_profile_add_volume_data, firmware)
SLES15_Bronco_FC_run1_profile_spp = DD.make_server_profile_data(SLES15_Bronco_FC_run1_profile_add_volume_data, update_firmware)
SLES15_Bronco_FC_run1_profile_spp_expected = DD.make_expected_server_profile_data(SLES15_Bronco_FC_run1_profile_add_volume_data, update_firmware)

############################################################################################
# RHEL610-Quartz16GB-FC_Run2 gen9
############################################################################################
rhel610_quartz16gb_fc_run2_profile_data = [{'name': 'RHEL610-Quartz16GB-FC_Run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 2', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                             "iscsiInitiatorNameType": "AutoGenerated",
                                             'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                     'mac': '2A:79:6C:90:00:7F', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                     'boot': {'priority': 'NotBootable'}},
                                                                                     {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                      'mac': '2A:79:6C:90:00:80', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                      'boot': {'priority': 'NotBootable'}},
                                                                                     {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                                                                      'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:81', 'networkUri': 'FC:fc1',
                                                                                      'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                     {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2",
                                                                                      'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:82', "networkUri": "FC:fc2",
                                                                                      "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                             'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA', "boot": {"order": ["HardDisk"], "manageBoot": True},
                                             'bios': {'manageBios': False, 'overriddenSettings': []},
                                             "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", "secureBoot": "Disabled"},
                                             'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                             'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                             'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                           'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL610-Quartz16GB-FC_Run2_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                  'volumeStorageSystemUri': 'SSYS:TBRack5-P7200C',
                                                                                  'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                   {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

rhel610_quartz16gb_fc_run2_profile = DD.make_server_profile_data(rhel610_quartz16gb_fc_run2_profile_data, firmware)
rhel610_quartz16gb_fc_run2_profile_expected = DD.make_expected_server_profile_data(rhel610_quartz16gb_fc_run2_profile_data, firmware)
rhel610_quartz16gb_fc_run2_profile_add_volume_data = copy.deepcopy(rhel610_quartz16gb_fc_run2_profile_data)
rhel610_quartz16gb_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(rhel610_quartz16gb_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                       "SVOL:RHEL610-Quartz16GB-FC_Run2_vol2")
rhel610_quartz16gb_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(rhel610_quartz16gb_fc_run2_profile_add_volume_data, firmware)
rhel610_quartz16gb_fc_run2_profile_spp = DD.make_server_profile_data(rhel610_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)
rhel610_quartz16gb_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(rhel610_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# SLES15-Quartz16GB-FC_Run2 Gen9
############################################################################################
sles15_quartz16gb_fc_run2_profile_data = [{'name': 'SLES15-Quartz16GB-FC_Run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 3', 'enclosureGroupUri': 'EG:eg', 'description': '', 'affinity': 'Bay',
                                           "iscsiInitiatorNameType": "AutoGenerated",
                                           'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                   'mac': '2A:79:6C:90:00:87', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                   {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                    'mac': '2A:79:6C:90:00:88', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1', 'boot': {'priority': 'NotBootable'}},
                                                                                   {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                                                                    'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:89', 'networkUri': 'FC:fc1',
                                                                                    'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                   {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2",
                                                                                    'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:8A', "networkUri": "FC:fc2",
                                                                                    "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                           'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:Synergy 3820C 10/20Gb CNA',
                                           "boot": {"order": ["HardDisk"], "manageBoot": True},
                                           'bios': {'manageBios': False, 'overriddenSettings': []},
                                           "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                           'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                           'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                           'sanStorage':{'hostOSType': 'SuSE (10.x, 11.x, 12.x, 15.x)', 'manageSanStorage': True,
                                                         'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:SLES15-Quartz16GB-FC_Run2_vol", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                                'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                                 {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

sles15_quartz16gb_fc_run2_profile = DD.make_server_profile_data(sles15_quartz16gb_fc_run2_profile_data, firmware)
sles15_quartz16gb_fc_run2_profile_expected = DD.make_expected_server_profile_data(sles15_quartz16gb_fc_run2_profile_data, firmware)
sles15_quartz16gb_fc_run2_profile_add_volume_data = copy.deepcopy(sles15_quartz16gb_fc_run2_profile_data)
sles15_quartz16gb_fc_run2_profile_add_volume = DD.make_server_profile_add_volume_data(sles15_quartz16gb_fc_run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                      "SVOL:SLES15-Quartz16GB-FC_Run2_vol2")
sles15_quartz16gb_fc_run2_profile_add_volume_expected = DD.make_expected_server_profile_data(sles15_quartz16gb_fc_run2_profile_add_volume_data, firmware)
sles15_quartz16gb_fc_run2_profile_spp = DD.make_server_profile_data(sles15_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)
sles15_quartz16gb_fc_run2_profile_spp_expected = DD.make_expected_server_profile_data(sles15_quartz16gb_fc_run2_profile_add_volume_data, update_firmware)

############################################################################################
# RHEL610_Electron_FC_Run2
############################################################################################
RHEL610_Electorn16GB_FC_Run2_profile_data = [{'name': 'RHEL610-Electorn16GB-FC_Run2', 'serverHardwareUri': 'SH:CN75140CPT, bay 1', 'enclosureGroupUri': 'EG:eg', 'description': '',
                                         'affinity': 'Bay', "iscsiInitiatorNameType": "AutoGenerated",
                                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500',
                                                                                 'mac': '2A:79:6C:90:00:83', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'requestedMbps': '2500',
                                                                                 'mac': '2A:79:6C:90:00:84', 'macType': 'UserDefined', 'networkUri': 'ETH:eth1',
                                                                                 'boot': {'priority': 'NotBootable'}},
                                                                                {'id': 3, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1',
                                                                                 'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:85', 'networkUri': 'FC:fc1',
                                                                                 'boot': {'priority': 'Primary', 'bootVolumeSource': 'ManagedVolume'}},
                                                                                {"id": 4, "name": "", "functionType": "FibreChannel", "portId": "Mezz 1:2",
                                                                                 'macType': 'UserDefined', 'mac': '2A:79:6C:90:00:86', "networkUri": "FC:fc2",
                                                                                 "boot": {"priority": "Secondary", "bootVolumeSource": "ManagedVolume"}}]},
                                         'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3530C 16G HBA:3:Synergy 3820C 10/20Gb CNA',
                                         "boot": {"order": ["HardDisk"], "manageBoot": True},
                                         'bios': {'manageBios': False, 'overriddenSettings': []},
                                         "bootMode":{"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         'hideUnusedFlexNics': True, 'osDeploymentSettings': None,
                                         'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                                         'sanStorage':{'hostOSType': 'RHE Linux (5.x, 6.x, 7.x)', 'manageSanStorage': True,
                                                       'volumeAttachments': [{'id': 1, 'volumeUri': "SVOL:RHEL610-Electorn16GB-FC_Run2", 'bootVolumePriority': 'Primary', 'lunType': 'Auto',
                                                                              'storagePaths': [{'isEnabled': True, 'connectionId': 3, 'targetSelector': 'Auto'},
                                                                                               {"isEnabled": True, "connectionId": 4, "targetSelector": "Auto"}]}]}}]

RHEL610_Electorn16GB_FC_Run2_profile = DD.make_server_profile_data(RHEL610_Electorn16GB_FC_Run2_profile_data, firmware)
RHEL610_Electorn16GB_FC_Run2_profile_expected = DD.make_expected_server_profile_data(RHEL610_Electorn16GB_FC_Run2_profile_data, firmware)
RHEL610_Electorn16GB_FC_Run2_profile_add_volume_data = copy.deepcopy(RHEL610_Electorn16GB_FC_Run2_profile_data)
RHEL610_Electorn16GB_FC_Run2_profile_add_volume = DD.make_server_profile_add_volume_data(RHEL610_Electorn16GB_FC_Run2_profile_add_volume_data, firmware, 'SSYS:TBRack5-P7200C',
                                                                                    "SVOL:RHEL610-Electorn16GB-FC_Run2_vol2")
RHEL610_Electorn16GB_FC_Run2_profile_add_volume_expected = DD.make_expected_server_profile_data(RHEL610_Electorn16GB_FC_Run2_profile_add_volume_data, firmware)
RHEL610_Electorn16GB_FC_Run2_profile_spp = DD.make_server_profile_data(RHEL610_Electorn16GB_FC_Run2_profile_add_volume_data, update_firmware)
RHEL610_Electorn16GB_FC_Run2_profile_spp_expected = DD.make_expected_server_profile_data(RHEL610_Electorn16GB_FC_Run2_profile_add_volume_data, update_firmware)

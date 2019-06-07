import os
import sys

cwd = os.getcwd()
download_to_path = cwd


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

APPLIANCE_IP = '15.245.132.18'

appliance_cred = ['root', 'wpsthpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator'}], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator'}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'readonly', 'permissions': [{'roleName': 'Read only'}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]

ENC1 = 'FVT-PAAX63-EN2'
ENC2 = 'enc2'
LE = 'FVT-PAAX63-EN2'
LIG1 = 'LIG_Hill'

encs = [{'hostname': '15.245.129.62', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG_Hill', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]
server1_ip = '15.245.133.213'
server8_ip = '15.245.133.184'
Expected_Consistency_Status = 'CONSISTENT'
Server_name = 'FVT-PAAX63-EN2, bay 1'
Module_name = 'HP VC 16Gb 24-Port FC Module'
Module_name1 = 'HP VC 16Gb 24-Port FC TAA Module'
interconnectname_1 = 'FVT-PAAX63-EN2, interconnect 3'
interconnectname_2 = 'FVT-PAAX63-EN2, interconnect 4'
fc_firmwareVersion_snap6 = '3.05'
fc_firmwareVersion_snap5 = '3.01'
BAY5_IP = '15.186.27.232'
BAY6_IP = '15.186.13.104'
OA_HOST = '15.245.129.62'
OA_USER = 'Administrator'
OA_PASS = 'wpsthpvse1'
DEVICE = 'IOM'
BAY = '4'
Hill_Bay_Username = 'root'
Hill_Bay_Password = 'TZ26XCBG'
IC_Command = 'snmpconfig --show snmpv1'
IC_Match = 'Trap recipient: \d+.\d+.\d+.\d+'
SNMP_Match = 'SNMPv1:\w+'
ACTION = 'OFF'
Mode = 'PRESERVE_NETWORK'
admin_default_paswd = "admin"
factory_reset_sleep_time = '1800'
BACKUPFILE_DIR = "C:\\4.10_Gen10_Snap2_PB61\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\OVF269_Hill_TAA\\"
Snap6_SPP_Uri = '/rest/firmware-drivers/SPPgen9snap6_2016_0628_126'
Snap5_SPP_Uri = '/rest/firmware-drivers/SPP2016020_2015_1204_63'
LE_Update_Sleep_Time = '1500'
LI_Update_Sleep_Time = '900'
LE_Support_Dump_Time = '600'
Backup_Sleep_Time = '200'
Upload_Backup_Sleep_Time = '360'
Poweron_Server_Sleeptime = '600'
cmd_sleep_time = '20'
poweron_sleep_time = '300'
Command_Execute_Sleep_Time = '20'
Process_Sleep_Time = '100'
localfile = 'HPOneVIew-fullupdate-3.00.00-SNAPSHOT-0255853.bin'
version_Check = '3.00.00-0255853'
Upload_Sleep_Time = '4200'
SSH_SNMP_IP = '15.245.132.221'
SNMP_UserName = 'root'
SNMP_Password = 'rootpwd'
QUERY = 'SNMP/vcmtrap2.log'
Trap_File_Name = 'vcmtrap2.log'
Port_status_trap_name = 'Enterprise Specific Trap'
IC_restart_trap_name = 'Cold Start Trap'
cmd_sleep_time = '5'
update_from_group_time = '100'
Trap_Ips = ['Trap recipient: 1.1.1.1', 'Trap recipient: 2.2.2.2', 'Trap recipient: 3.3.3.3', 'Trap recipient: 4.4.4.4', 'Trap recipient: 5.5.5.5', 'Trap recipient: 6.6.6.6']
WWNN_UD = '1000665544332211'
WWPN_UD = '1000344455667788'
MAC_address_UD = '12-34-56-78-90-12'
Serial_number_UD = 'VCU1234567'
UUID_UD = '12345678-1234-1234-1237-123456789012'
startAddress_mac = '12-34-56-78-90-00'
endAddress_mac = '12-34-56-78-90-7F'
startAddress_check = '1000887766554433'
startAddress_wwn = '10:00:88:77:66:55:44:33'
endAddress_wwn = '10:00:88:77:66:55:44:B2'
startAddress_sn = 'VCU3456789'
endAddress_sn = 'VCU34567BS'
totalCount = '128'
freeIdCount = '128'
allocatedIdCount = '0'
US_Check = 'us_fc'
Port_Check = '5'
Alert_Message_Server_Profile = 'The interconnect module is not a part of any logical interconnect. One or more server profile connections is affected.'
Alert_Message_Delete_Port = 'For uplink set %s, uplink ports %s :%s are non operational.' % (US_Check, interconnectname_1, Port_Check)
INTERCONNECT_USER = 'root'
INTERCONNECT_PASS = '6KWDJF7J'
restart_mode = 'REBOOT'
IC_Inventory = 'Inventory'
IC_Configured = 'Configured'
Consistency_Status = 'CONSISTENT'
Inconsistency_Status = 'INCONSISTENT'
loggerlevel = r'INFO'   # use INFO|DEBUG

enet_hill_old = {'name': 'enet_hill',
                 'type': 'ethernet-networkV4',
                 'vlanId': None,
                 'purpose': 'General',
                 'smartLink': True,
                 'privateNetwork': False,
                 'connectionTemplateUri': None,
                 'ethernetNetworkType': 'Untagged'}

enet_hill = {"vlanId": "101",
             "purpose": "General",
             "name": "enet_hill",
             "smartLink": False,
             "privateNetwork": False,
             "connectionTemplateUri": None,
             "ethernetNetworkType": "Tagged",
             "type": "ethernet-networkV4"
             }

enet_V2 = {"vlanId": "10",
           "ethernetNetworkType": "Tagged",
           "purpose": "General",
           "name": "enet1",
           "smartLink": True,
           "privateNetwork": False,
           "connectionTemplateUri": None,
           "type": "ethernet-networkV4"
           }

fc1_hill = [{'type': 'fc-networkV4',
             'linkStabilityTime': 30,
             'autoLoginRedistribution': False,
             'name': 'fc1_hill',
             'connectionTemplateUri': None,
             'managedSanUri': None,
             'fabricType': 'FabricAttach'}]

fc2_hill = [{'type': 'fc-networkV4',
             'linkStabilityTime': 30,
             'autoLoginRedistribution': False,
             'name': 'fc2_hill',
             'connectionTemplateUri': None,
             'managedSanUri': None,
             'fabricType': 'FabricAttach'}]

fc3_hill = [{'type': 'fc-networkV4',
             'linkStabilityTime': 30,
             'autoLoginRedistribution': True,
             'name': 'fc3_hill',
             'connectionTemplateUri': None,
             'managedSanUri': None,
             'fabricType': 'FabricAttach'}]

fcNet_hill = [{'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc1_hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
              {'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc2_hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
              {'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc3_hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'},
              {'type': 'fc-networkV4',
               'linkStabilityTime': 30,
               'autoLoginRedistribution': True,
               'name': 'fc4_hill',
               'connectionTemplateUri': None,
               'managedSanUri': None,
               'fabricType': 'FabricAttach'}]

lig_uplink_sets = {'UplinkSet_1': {'name': 'us_eth', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['enet_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '2', 'enclosure': '1', 'port': 'X2', 'speed': 'Auto'}]},
                   'UplinkSet_2': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                              {'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                   'UplinkSet_3': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                              {'bay': '4', 'enclosure': '1', 'port': '5', 'speed': 'Auto'}]}
                   }

# Manual Login Redistribution Bay Port Format Conversion as below:
bay_port_detail = {}
for i in 'UplinkSet_2', 'UplinkSet_3':
    tlist = []
    for j in lig_uplink_sets[i]['logicalPortConfigInfos']:
        tlist.append(int(j['port']))
        bay_port_detail[int(j['bay'])] = tlist

# Based on the Uplink port connection the following output should change
mlr_initial_output = {'3.1': 1, '3.2': 1, '4.1': 1, '4.5': 1}
mlr_final_output = {'3.1': 0, '3.2': 2, '4.1': 0, '4.5': 2}
interconnect_ports_to_disable = [3.1, 4.1]
api_version = 500

edit_interconnect_port_payload_keys = ["associatedUplinkSetUri", "interconnectName", "portType", "portId", "portHealthStatus", "capability", "configPortTypes", "enabled", "portName", "portStatus", "type"]

# 'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(),lig_uplink_sets['UplinkSet_2'].copy(),lig_uplink_sets['UplinkSet_3'].copy()],
lig_uplink_config = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_3': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc3_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]},
                     'UplinkSet_4': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc4_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]}
                     }

lig_uplink_server = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_3': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_4': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '5', 'speed': 'Auto'}]},
                     'UplinkSet_5': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}, {'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_6': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}, {'bay': '4', 'enclosure': '1', 'port': '5', 'speed': 'Auto'}]},
                     'UplinkSet_7': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_8': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_9': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Speed8G'}]},
                     'UplinkSet_10': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Speed8G'}]},
                     'UplinkSet_11': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '1', 'speed': 'Speed8G'}]},
                     'UplinkSet_12': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Speed8G'}]},
                     'UplinkSet_13': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Speed8G'}]},
                     'UplinkSet_14': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '5', 'speed': 'Speed16G'}]},
                     'UplinkSet_15': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Speed8G'}]},
                     'UplinkSet_16': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '5', 'speed': 'Speed16G'}]},
                     'UplinkSet_17': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': []},
                     'UplinkSet_18': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': []}
                     }

lig_hill = {'name': 'LIG_Hill',
            'type': 'logical-interconnect-groupV400',
            'enclosureType': 'C7000',
            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
            'uplinkSets': [],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.245.132.221', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
            'qosConfiguration': None}

lig_hill_new = {'name': 'LIG_Hill',
                'type': 'logical-interconnect-groupV4',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_sets['UplinkSet_2'].copy(), lig_uplink_sets['UplinkSet_3'].copy()], 'stackingMode': 'Enclosure',
                'ethernetSettings': None,
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.245.132.221', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': True, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                'qosConfiguration': None}

lig_hill_edit = {'name': 'LIG_Hill',
                 'type': 'logical-interconnect-groupV4',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'}],
                 'uplinkSets': [],
                 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.245.132.42', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': True, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                 'qosConfiguration': None}

lig_hill_trap6 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [], 'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '1.1.1.1', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '2.2.2.2', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '3.3.3.3', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '4.4.4.4', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '5.5.5.5', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '6.6.6.6', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}], 'snmpAccess': [], 'enabled': True, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                  'qosConfiguration': None}

lig_hill_config = {'name': 'LIG_Hill',
                   'type': 'logical-interconnect-groupV400',
                   'enclosureType': 'C7000',
                   'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                   'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_2'].copy(),
                                  lig_uplink_config['UplinkSet_3'].copy(), lig_uplink_config['UplinkSet_4'].copy()],
                   'stackingMode': 'Enclosure',
                   'ethernetSettings': None,
                   'state': 'Active',
                   'telemetryConfiguration': None,
                   'snmpConfiguration': None,
                   'qosConfiguration': None}

lig_hill_edit1 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_2'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit2 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_3'].copy(), lig_uplink_server['UplinkSet_4'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit3 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_5'].copy(), lig_uplink_server['UplinkSet_6'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit4 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_7'].copy(), lig_uplink_server['UplinkSet_8'].copy()],
                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': None,
                                  'qosConfiguration': None}

lig_hill_edit5 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_9'].copy(), lig_uplink_server['UplinkSet_10'].copy()],
                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': None,
                                  'qosConfiguration': None}

lig_hill_edit6 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_11'].copy(), lig_uplink_server['UplinkSet_12'].copy()],
                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': None,
                                  'qosConfiguration': None}

lig_hill_edit7 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_13'].copy(), lig_uplink_server['UplinkSet_14'].copy()],
                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': None,
                                  'qosConfiguration': None}

lig_hill_edit8 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_15'].copy(), lig_uplink_server['UplinkSet_16'].copy()],
                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': None,
                                  'qosConfiguration': None}

lig_hill_edit9 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV400',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 7, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_17'].copy(), lig_uplink_server['UplinkSet_18'].copy()],
                  'stackingMode': 'Enclosure',
                                  'ethernetSettings': None,
                                  'state': 'Active',
                                  'telemetryConfiguration': None,
                                  'snmpConfiguration': None,
                                  'qosConfiguration': None}

# Bay number to get the port statistics of the FC module in interconnect page
# The number is applicable to the interconnect number in interconnect page
fc_bay_num = lig_uplink_sets['UplinkSet_2']['logicalPortConfigInfos'][0]['bay']
portno_for_statistics = [lig_uplink_sets['UplinkSet_2']['logicalPortConfigInfos'][0]['port'], lig_uplink_sets['UplinkSet_2']['logicalPortConfigInfos'][1]['port']]

enc_group_V200 = {'name': 'EG_Hill',
                  'type': 'EnclosureGroupV200',
                  'enclosureTypeUri': '/rest/enclosure-types/c7000',
                  'stackingMode': 'Enclosure',
                                  'interconnectBayMappingCount': 8,
                                  'configurationScript': None,
                                  'interconnectBayMappings':
                                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                                   {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                                   {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                                   {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                                   {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                                   {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                                   {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}

enc_group_hill = {'name': 'EG_Hill',
                  'interconnectBayMappings':
                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 7, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
                  'ipRangeUris': [],
                  'enclosureCount': 1,
                  'powerMode': None,
                  'configurationScript': None,
                  'ambientTemperatureMode': 'Standard'}

encs_m = {'hostname': '15.245.129.62', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': None, 'licensingIntent': 'OneViewStandard', 'state': 'Monitored'}

encs_fwupdate = [{'hostname': '15.186.27.232', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_Hill', 'force': False, 'licensingIntent': 'OneView', 'firmwareBaselineUri': Snap6_SPP_Uri, 'forceInstallFirmware': True, 'updateFirmwareOn': 'EnclosureOnly'}]

enclosure_preview = {"hostname": "15.245.129.62", "username": "Administrator", "password": "wpsthpvse1", "ligPrefix": "LIG_Hill", "force": True, "logicalInterconnectGroupNeeded": True}

uplink_sets = {'us_eth': {'name': 'us_eth',
                          'ethernetNetworkType': 'Tagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['enet_hill'],
                          'fcNetworkUris': [],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'NotSupported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '1', 'port': 'X1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc': {'name': 'us_fc',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': [],
                         'fcNetworkUris': ['fc1_hill'],
                         'fcoeNetworkUris': [],
                         'lacpTimer': 'Short',
                         'logicalInterconnectUri': None,
                         'primaryPortLocation': None,
                         'manualLoginRedistributionState': 'Supported',
                         'connectionMode': 'Auto',
                         'nativeNetworkUri': None,
                         'portConfigInfos': [{'bay': '3', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                             {'bay': '3', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc_1': {'name': 'us_fc_1',
                           'ethernetNetworkType': 'NotApplicable',
                           'networkType': 'FibreChannel',
                           'networkUris': [],
                           'fcNetworkUris': ['fc2_hill'],
                           'fcoeNetworkUris': [],
                           'lacpTimer': 'Short',
                           'logicalInterconnectUri': None,
                           'primaryPortLocation': None,
                           'manualLoginRedistributionState': 'Supported',
                           'connectionMode': 'Auto',
                           'nativeNetworkUri': None,
                           'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': '5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc_new': {'name': 'us_fc_new',
                             'ethernetNetworkType': 'NotApplicable',
                             'networkType': 'FibreChannel',
                             'networkUris': [],
                             'fcNetworkUris': [],
                             'fcoeNetworkUris': [],
                             'lacpTimer': 'Short',
                             'logicalInterconnectUri': None,
                             'primaryPortLocation': None,
                             'manualLoginRedistributionState': 'Supported',
                             'connectionMode': 'Auto',
                             'nativeNetworkUri': None,
                             'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc_mk': {'name': 'us_fc_mk',
                            'ethernetNetworkType': 'NotApplicable',
                            'networkType': 'FibreChannel',
                            'networkUris': [],
                            'fcNetworkUris': ['fc3_hill'],
                            'fcoeNetworkUris': [],
                            'lacpTimer': 'Short',
                            'logicalInterconnectUri': None,
                            'primaryPortLocation': None,
                            'manualLoginRedistributionState': 'Supported',
                            'connectionMode': 'Auto',
                            'nativeNetworkUri': None,
                            'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc1': {'name': 'us_fc1',
                          'ethernetNetworkType': 'NotApplicable',
                          'networkType': 'FibreChannel',
                          'networkUris': [],
                          'fcNetworkUris': [fc1_hill],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'Supported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc2': {'name': 'us_fc2',
                          'ethernetNetworkType': 'NotApplicable',
                          'networkType': 'FibreChannel',
                          'networkUris': [],
                          'fcNetworkUris': ['fc2_hill'],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'Supported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '3', 'port': '3', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc3': {'name': 'us_fc3',
                          'ethernetNetworkType': 'NotApplicable',
                          'networkType': 'FibreChannel',
                          'networkUris': [],
                          'fcNetworkUris': ['fc3_hill'],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'Supported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
               'us_fc4': {'name': 'us_fc4',
                          'ethernetNetworkType': 'NotApplicable',
                          'networkType': 'FibreChannel',
                          'networkUris': [],
                          'fcNetworkUris': ['fc4_hill'],
                          'fcoeNetworkUris': [],
                          'lacpTimer': 'Short',
                          'logicalInterconnectUri': None,
                          'primaryPortLocation': None,
                          'manualLoginRedistributionState': 'Supported',
                          'connectionMode': 'Auto',
                          'nativeNetworkUri': None,
                          'portConfigInfos': [{'bay': '4', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]}
               }

uplink_sets_edit = {'us_eth': {'name': 'us_eth',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['enet_hill'],
                               'fcNetworkUris': [],
                               'fcoeNetworkUris': [],
                               'lacpTimer': 'Short',
                               'logicalInterconnectUri': None,
                               'primaryPortLocation': None,
                               'manualLoginRedistributionState': 'NotSupported',
                               'connectionMode': 'Auto',
                               'nativeNetworkUri': None,
                               'portConfigInfos': [{'bay': '1', 'port': 'X5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                    'us_fc': {'name': US_Check,
                              'ethernetNetworkType': 'NotApplicable',
                              'networkType': 'FibreChannel',
                              'networkUris': [],
                              'fcNetworkUris': ['fc1_hill'],
                              'fcoeNetworkUris': [],
                              'lacpTimer': 'Short',
                              'logicalInterconnectUri': None,
                              'primaryPortLocation': None,
                              'manualLoginRedistributionState': 'Supported',
                              'connectionMode': 'Auto',
                              'nativeNetworkUri': None,
                              'portConfigInfos': [{'bay': '5', 'port': Port_Check, 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                                  {'bay': '5', 'port': '3', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]}
                    }

uplink_sets_edit1 = {'us_fc': {'name': US_Check,
                               'ethernetNetworkType': 'NotApplicable',
                               'networkType': 'FibreChannel',
                               'networkUris': [],
                               'fcNetworkUris': ['fc1_hill'],
                               'fcoeNetworkUris': [],
                               'lacpTimer': 'Short',
                               'logicalInterconnectUri': None,
                               'primaryPortLocation': None,
                               'manualLoginRedistributionState': 'Supported',
                               'connectionMode': 'Auto',
                               'nativeNetworkUri': None,
                               'portConfigInfos': [{'bay': '3', 'port': '1', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1},
                                                   {'bay': '3', 'port': '2', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}]}
                     }

uplink_sets_server8 = {'us_fc1': {'name': 'us_fc1',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc1_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '3', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                       'us_fc2': {'name': 'us_fc2',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc2_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                       'us_fc3': {'name': 'us_fc1',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc1_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '3', 'enclosure': ENC1, 'port': '1', 'desiredSpeed': 'Auto'}, {'bay': '3', 'enclosure': ENC1, 'port': '5', 'desiredSpeed': 'Auto'}]},
                       'us_fc4': {'name': 'us_fc2',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc2_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '4', 'enclosure': ENC1, 'port': '1', 'desiredSpeed': 'Auto'}, {'bay': '4', 'enclosure': ENC1, 'port': '5', 'desiredSpeed': 'Auto'}]},
                       'us_fc5': {'name': 'us_fc1',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc1_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                       'us_fc6': {'name': 'us_fc2',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc2_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '4', 'port': '5', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                       'us_fc7': {'name': 'us_fc1',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc1_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc8': {'name': 'us_fc2',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc2_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '4', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc9': {'name': 'us_fc3',
                                  'ethernetNetworkType': 'NotApplicable',
                                  'networkType': 'FibreChannel',
                                  'networkUris': [],
                                  'fcNetworkUris': ['fc1_hill'],
                                  'fcoeNetworkUris': [],
                                  'lacpTimer': 'Short',
                                  'logicalInterconnectUri': None,
                                  'primaryPortLocation': None,
                                  'manualLoginRedistributionState': 'Supported',
                                  'connectionMode': 'Auto',
                                  'nativeNetworkUri': None,
                                  'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc10': {'name': 'us_fc4',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc2_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': [{'bay': '4', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc11': {'name': 'us_fc3',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc1_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc12': {'name': 'us_fc4',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc2_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': [{'bay': '4', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc13': {'name': 'us_fc3',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc1_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': [{'bay': '3', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc14': {'name': 'us_fc4',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc2_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': [{'bay': '4', 'port': '5', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},
                       'us_fc15': {'name': 'us_fc3',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc1_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': []},
                       'us_fc16': {'name': 'us_fc4',
                                   'ethernetNetworkType': 'NotApplicable',
                                   'networkType': 'FibreChannel',
                                   'networkUris': [],
                                   'fcNetworkUris': ['fc2_hill'],
                                   'fcoeNetworkUris': [],
                                   'lacpTimer': 'Short',
                                   'logicalInterconnectUri': None,
                                   'primaryPortLocation': None,
                                   'manualLoginRedistributionState': 'Supported',
                                   'connectionMode': 'Auto',
                                   'nativeNetworkUri': None,
                                   'portConfigInfos': []}
                       }

server_profiles_gen8 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 9',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                         'name': 'Profile_server8', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                   'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                 'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                ]},
                         #'bootMode':{'manageMode': True, 'mode': 'UEFI', 'secureBoot':'Disabled','pxeBootPolicy':'Auto'}
                         'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]


# The below profile is used for MLR test case
server_profiles_gen8_enc1_bay1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                   'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                   'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                                   'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                           'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                          {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                           'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                                          ]},
                                   'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_gen8_bay1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                              'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                              'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                              'connectionSettings': {'connections': []},
                              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_gen9 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                         'boot': None, 'bootMode': {'manageMode': False}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_edit1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Physical',
                          'name': 'SP_Config1', 'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'boot': {'priority': 'NotBootable'}, 'macType': 'UserDefined', 'mac': MAC_address_UD, 'wwpn': '', 'wwnn': ''},
                                                                 {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                  'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': WWPN_UD, 'wwnn': WWNN_UD}
                                                                 ]},
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':Serial_number_UD, 'uuid':UUID_UD}]

server_profiles_edit2 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 10',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                          'name': 'SP_Config1', 'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                 {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                  'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                 ]},
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':None, 'uuid':None}]

server_profiles_edit3 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 10',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': 'SP_Config1', 'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                 {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                  'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                 ]},
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':None, 'uuid':None}]

server_profiles_server7_bay1 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                 'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                                 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                         'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_server7_bay10 = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 9',
                                  'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                  'name': 'Profile_server10', 'description': '', 'affinity': 'Bay',
                                  'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                                         {'id': 2, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                          'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
                                  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

oa_details_1 = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_server7_bay1[0]['serverHardwareUri'].split(' ')[-1]}

oa_details_2 = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_server7_bay10[0]['serverHardwareUri'].split(' ')[-1]}

sdmp_body = {"errorCode": "CI", "encrypt": False}
le_sdmp_body = {"errorCode": "LE", "encrypt": False}

leupdate_body = [{"op": "replace", "path": "/firmware", "value": {"firmwareBaselineUri": Snap6_SPP_Uri, "forceInstallFirmware": True, "firmwareUpdateOn": "SharedInfrastructureOnly", "logicalInterconnectUpdateMode": "Parallel", "validateIfLIFirmwareUpdateIsNonDisruptive": False, "updateFirmwareOnUnmanagedInterconnect": False}}]

liupdate_body = {"sppUri": Snap5_SPP_Uri, "command": "UPDATE", "force": True, "ethernetActivationType": "Parallel", "ethernetActivationDelay": "0", "fcActivationType": "Parallel", "fcActivationDelay": "0", "validationType": "None"}

Port_enable_body = [{"associatedUplinkSetUri": None, "interconnectName": interconnectname_2, "portType": "Uplink", "portHealthStatus": "Disabled", "capability": ["FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":True, "portStatus":"Unlinked", "type":"port"}]

Port_disable_body = [{"associatedUplinkSetUri": None, "interconnectName": interconnectname_2, "portType": "Uplink", "portHealthStatus": "Normal", "capability": ["FibreChannel"], "configPortTypes":["FibreChannel"], "enabled":False, "portStatus":"Linked", "type":"port"}]

Vmac_body = {"type": "Range", "name": None, "prefix": None, "enabled": True, "rangeCategory": "CUSTOM", "startAddress": startAddress_mac, "endAddress": endAddress_mac, "totalCount": totalCount, "freeIdCount": freeIdCount, "allocatedIdCount": allocatedIdCount, "allocatorUri": None, "collectorUri": None, "reservedIdCount": 0, "uri": None, "category": "id-range-VMAC", "eTag": None, "created": None, "modified": None}

Vwwn_body = {"type": "Range", "name": None, "prefix": None, "enabled": True, "rangeCategory": "CUSTOM", "startAddress": startAddress_wwn, "endAddress": endAddress_wwn, "totalCount": totalCount, "freeIdCount": freeIdCount, "allocatedIdCount": allocatedIdCount, "allocatorUri": None, "collectorUri": None, "reservedIdCount": 0, "uri": None, "category": "id-range-VWWN", "eTag": None, "created": None, "modified": None}

Vsn_body = {"type": "Range", "name": None, "prefix": None, "enabled": True, "rangeCategory": "CUSTOM", "startAddress": startAddress_sn, "endAddress": endAddress_sn, "totalCount": totalCount, "freeIdCount": freeIdCount, "allocatedIdCount": allocatedIdCount, "allocatorUri": None, "collectorUri": None, "reservedIdCount": 0, "uri": None, "category": "id-range-VSNN", "eTag": None, "created": None, "modified": None}

dis_mac = {"type": "Range", "enabled": False}
dis_wwn = {"type": "Range", "enabled": False}
dis_sn = {"type": "Range", "enabled": False}

linux_details = {"hostip": "15.245.134.7", "username": "root", "password": "rootpwd", "dir_location": "/root/",
                 "python_cmd": "python2.7"}

oa_details = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_edit1[0]['serverHardwareUri'].split(' ')[-1]}

oa_details_3 = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_gen8[0]['serverHardwareUri'].split(' ')[-1]}

VC_details = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_edit1[0]['serverHardwareUri'].split(' ')[-1]}

diskspd_cmd = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b20K -h -L D:\\multi5.dat >C:\\Ov_restartbefore1.dat"

diskspd_cmd_16Gb = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d120 -r -w70 -t19 -o12 -b40k -h -L E:\\multi5.dat >C:\\Ov_restartbefore1.dat"

diskspd_cmd_1 = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b20K -h -L E:\\multi5.dat >C:\\Ov_restartafter2.dat"

diskspd_cmd_disable_ports = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c60M -d86600 -r -w70 -t19 -o19 -b30K -h -L E:\\port_disable_enable.dat >C:\\port_dis_enable_1.dat"

diskspd_cmd_effuse = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c80M -d740 -r -w70 -t9 -o9 -b20K -h -L E:\\oa_failover.dat >C:\\OA_Failover_traffic.dat"
# Change this path according to the Checkout copy directory
module_file_path = "C:\\4.10_Gen10_Snap2_PB61\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\OVF269_Hill_TAA\\GetServerIPs.py"

diskspd_cmd_48_hours = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d172800 -r -w70 -t9 -o9 -b20K -h -L E:\\multi6.dat >C:\\OA_Failover_traffic.dat"

windows_server_cred = ["Administrator", 'hpvse1']

bay_no = [3, 4]

interconnect_no = [3, 4]

manual_IP = ['15.186.24.121', '15.186.24.131']

"""data variables"""


def make_range_list(start, end, prefix='net_', suffix=''):
    """function definition"""
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


APPLIANCE_IP = "15.186.18.7"
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "W6YNC2XC"
FUSION_PROMPT = '# '  # Fusion Appliance Prompt
FUSION_TIMEOUT = 180
IC_SSH_USERNAME = "root"
IC_TIMEOUT = 100
IC_PROMPT = '>'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}


users = [{'type': 'UserAndPermissions', 'userName': 'nat', 'fullName': 'Networkadmin', 'password': 'wpsthpvse1', 'enabled': True,
          'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'type': 'UserAndPermissions', 'userName': 'sarah', 'fullName': 'Serveradmin', 'password': 'wpsthpvse1', 'enabled': True,
          'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]}]


users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'enabled': True, 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'enabled': True, 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'enabled': True, 'type': 'UserAndPermissions'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'readonly', 'permissions': [{'roleName': 'Read only', 'scopeUri': None}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'enabled': True, 'type': 'UserAndPermissions'}
         ]
ENC1 = 'enc1'
ENC2 = 'enc2'
LE = 'enc1'
LIG1 = 'LIG_Hill'
LIG2 = 'enc1-LIG logical interconnect group'

valDict = {'status_code': 200}
valDict1 = {'status_code': 400, 'errorCode': "CRM_INVALID_LINK_STABILITY_TIME"}
fc_hill_names = {'fc1_hill', 'fc2_hill', 'fc3_hill', 'fc4_hill'}

li_uplink_sets3 = {'us1': {'name': 'us_fc1',
                           'networkType': 'FibreChannel',
                           'ethernetNetworkType': None,
                           'networkUris': ['fc1_hill'],
                           'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                           'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                   'us2': {'name': 'ETH-FCOE2',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['net_104'],
                           'fcNetworkUris': [],
                           'fcoeNetworkUris': ['fcoe_1004'],
                           'lacpTimer': 'Short',
                           'logicalInterconnectUri': None,
                           'primaryPortLocation': None,
                           'manualLoginRedistributionState': 'NotSupported',
                           'connectionMode': 'Auto',
                           'nativeNetworkUri': None,
                           'portConfigInfos': [{'bay': '4', 'port': 'X1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X2', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X3', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X4', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X5', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X6', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X7', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X8', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X9', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X10', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                   'us3': {'name': 'Invalid-Uses-X11-X14',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['net_104'],
                           'fcNetworkUris': [],
                           'fcoeNetworkUris': ['fcoe_1004'],
                           'lacpTimer': 'Short',
                           'logicalInterconnectUri': None,
                           'primaryPortLocation': None,
                           'manualLoginRedistributionState': 'NotSupported',
                           'connectionMode': 'Auto',
                           'nativeNetworkUri': None,
                           'portConfigInfos': [{'bay': '4', 'port': 'X11', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X12', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X13', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                               {'bay': '4', 'port': 'X14', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},
                   }


encs = [{'hostname': '15.186.18.129', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_Hill', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

Expected_Consistency_Status = 'CONSISTENT'
Server_name = 'enc1, bay 1'
Module_name = 'HP VC 16Gb 24-Port FC Module'
interconnectname_1 = 'enc1, interconnect 5'
interconnectname_2 = 'enc1, interconnect 6'
fc_firmwareVersion_snap6 = '3.05'
fc_firmwareVersion_snap5 = '3.01'
BAY5_IP = '15.186.27.232'
BAY6_IP = '15.186.13.104'
OA_HOST = '15.186.27.232'
OA_USER = 'Administrator'
OA_PASS = 'compaq'
DEVICE = 'IOM'
BAY = '5'
Hill_Bay_Username = 'root'
Hill_Bay_Password = '6KWDJF7J'
IC_Command = 'snmpconfig --show snmpv1'
IC_Match = 'Trap recipient: \d+.\d+.\d+.\d+'
SNMP_Match = 'SNMPv1:\w+'
ACTION = 'OFF'
Mode = 'PRESERVE_NETWORK'
admin_default_paswd = "admin"
factory_reset_sleep_time = "800"
BACKUPFILE_DIR = "C:\\ONR\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\"
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
SSH_SNMP_IP = '15.186.21.149'
SNMP_UserName = 'root'
SNMP_Password = 'password'
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
loggerlevel = r'INFO'  # use INFO|DEBUG
value = False
LE1 = 'enc1-LIG_Hill'
enet_hill_old = {'name': 'enet_hill',
                 'type': 'ethernet-networkV300',
                 'vlanId': None,
                 'purpose': 'General',
                 'smartLink': True,
                 'privateNetwork': False,
                 'connectionTemplateUri': None,
                 'ethernetNetworkType': 'Untagged'}

enet_hill = {"purpose": "General",
             "name": "enet_hill",
                        "smartLink": False,
                        "privateNetwork": False,
                        "connectionTemplateUri": None,
                        "ethernetNetworkType": "Untagged",
                        "type": "ethernet-networkV300"
             }

enet_V2 = {"vlanId": "10",
           "ethernetNetworkType": "Tagged",
           "purpose": "General",
           "name": "enet1",
           "smartLink": True,
           "privateNetwork": False,
           "connectionTemplateUri": None,
           "type": "ethernet-networkV3"
           }

fc1_hill = [{'type': 'fc-networkV300',
             'linkStabilityTime': 30,
             'autoLoginRedistribution': False,
             'name': 'fc1_hill',
             'connectionTemplateUri': None,
             'managedSanUri': None,
             'fabricType': 'FabricAttach'}]

fc2_hill = [{'type': 'fc-networkV300',
             'linkStabilityTime': 30,
             'autoLoginRedistribution': False,
             'name': 'fc2_hill',
             'connectionTemplateUri': None,
             'managedSanUri': None,
             'fabricType': 'FabricAttach'}]

fc3_hill = [{'type': 'fc-networkV300',
             'linkStabilityTime': 30,
             'autoLoginRedistribution': True,
             'name': 'fc3_hill',
             'connectionTemplateUri': None,
             'managedSanUri': None,
             'fabricType': 'FabricAttach'}]

fc_hill = [{'type': 'fc-networkV4',
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

lig_uplink_sets = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                              ]},
                   'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                   'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                              ]}}

lig_uplink_sets1 = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}, {'bay': '3', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                                               ]},
                    'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                               {'bay': '4', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                               ]},
                    'UplinkSet_3': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc3_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                               {'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                                               ]},
                    'UplinkSet_4': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc4_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                               {'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                               ]}}


lig_uplink_sets2 = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                               {'bay': '3', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]},
                    'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                               {'bay': '4', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_3': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc3_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                               {'bay': '5', 'enclosure': '1', 'port': '3', 'speed': 'Auto'},
                                                               {'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'}
                                                               ]},
                    'UplinkSet_4': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc4_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                    'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'},
                                                               {'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'},
                                                               {'bay': '6', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}
                                                               ]}
                    }

#  Manual Login Redistribution Bay Port Format Conversion as below:
bay_port_detail = {}
for i in 'UplinkSet_1', 'UplinkSet_2':
    tlist = []
    for j in lig_uplink_sets[i]['logicalPortConfigInfos']:
        tlist.append(int(j['port']))
        bay_port_detail[int(j['bay'])] = tlist

bay_port_detail2 = {}
for i in 'UplinkSet_1', 'UplinkSet_2':
    tlist = []
    for j in lig_uplink_sets1[i]['logicalPortConfigInfos']:
        tlist.append(int(j['port']))
        bay_port_detail2[int(j['bay'])] = tlist

bay_port_detail3 = {}
for i in 'UplinkSet_1', 'UplinkSet_2':
    tlist = []
    for j in lig_uplink_sets2[i]['logicalPortConfigInfos']:
        tlist.append(int(j['port']))
        bay_port_detail3[int(j['bay'])] = tlist

Alr_initial = {'3.1': 2, '3.2': 2, '4.1': 2, '4.2': 2}
Alr_serverpoweron = {'3.2': 2, '4.1': 2}
Alr_output_disable = {'3.2': 0, '3.3': 2, '4.1': 0, '4.2': 2}
ALR = {'3.1': 0, '4.1': 0, '5.2': 0, '6.1': 0}
alr_after_addingport = {'3.2': 1, '3.3': 1, '4.1': 1, '4.2': 1}
alr_after_addingport_Li = {'3.1': 1, '3.2': 1, '4.1': 1, '4.2': 1}
alr_after_addingport1 = {'3.1': 1, '3.2': 1, '4.1': 1, '4.2': 1}
alr_after_addingports = {'3.2': 1, '3.3': 1, '4.1': 1, '4.2': 1}
Alr_after_enable = {'3.2': 1, '3.3': 1, '4.1': 1, '4.2': 1}
Mlr_after_enable = {'3.1': 1, '3.2': 1, '4.1': 1, '4.2': 1}
Mlr_after_addingports = {'3.1': 1, '3.2': 1, '4.1': 1, '4.2': 1}
interconnect_ports_to_disable = [3.2, 4.1]
api_version = 500
INTERCONNECTS = ['enc1, interconnect 3', 'enc1, interconnect 4']
Linked_Uplink_port = [['2', '3'], ['1', '2']]
Linked_Downlink_port = [['d3', 'd6'], ['d3', 'd6']]
Linked_Uplink_ports = [['2'], ['1']]
Linked_Downlink_ports = [['d3'], ['d3']]
edit_interconnect_port_payload_keys = ["associatedUplinkSetUri", "interconnectName", "portType", "portId", "portHealthStatus", "capability", "configPortTypes", "enabled", "portName", "portStatus", "type"]
IC_IP = "15.186.13.24"
Password = "W6YNC2XC"

portno = ['4', '5']

lig_uplink_config = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_3': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc3_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '4', 'speed': 'Auto'}]},
                     'UplinkSet_4': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc4_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '3', 'speed': 'Auto'}]}
                     }

lig_uplink_server = {'UplinkSet_1': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_2': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}]},
                     'UplinkSet_3': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_4': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_5': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}, {'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_6': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '1', 'speed': 'Auto'}, {'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_7': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_8': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Auto'}]},
                     'UplinkSet_9': {'name': 'us_fc1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                     'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Speed8G'}]},
                     'UplinkSet_10': {'name': 'us_fc2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Speed16G'}]},
                     'UplinkSet_11': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Speed8G'}]},
                     'UplinkSet_12': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': '2', 'speed': 'Speed16G'}]},
                     'UplinkSet_13': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Speed8G'}]},
                     'UplinkSet_14': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Speed16G'}]},
                     'UplinkSet_15': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Speed8G'}]},
                     'UplinkSet_16': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '5', 'enclosure': '1', 'port': '2', 'speed': 'Speed16G'}]},
                     'UplinkSet_17': {'name': 'us_fc3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc1_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': []},
                     'UplinkSet_18': {'name': 'us_fc4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['fc2_hill'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': []}
                     }

lig_hill = {'name': 'LIG_Hill',
            'type': 'logical-interconnect-groupV400',
            'enclosureType': 'C7000',
            'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
            'uplinkSets': [],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': False, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
            'qosConfiguration': None}

lig_hill_new = [{'name': 'LIG_Hill',
                 'type': 'logical-interconnect-groupV7',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                 'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_sets['UplinkSet_2'].copy()], 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess':[], 'enabled':True, 'description':None, 'name':None, 'state':None, 'status':None, 'eTag':None, 'category':'snmp-configuration', 'uri':None},
                 'qosConfiguration':None},
                {'name': 'LIG_Hill',
                 'type': 'logical-interconnect-groupV7',
                         'enclosureType': 'C7000',
                         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                 'uplinkSets': [lig_uplink_sets1['UplinkSet_1'].copy(), lig_uplink_sets1['UplinkSet_2'].copy()], 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess':[], 'enabled':True, 'description':None, 'name':None, 'state':None, 'status':None, 'eTag':None, 'category':'snmp-configuration', 'uri':None},
                 'qosConfiguration':None},
                {'name': 'LIG_Hill',
                 'type': 'logical-interconnect-groupV7',
                 'enclosureType': 'C7000',
                         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'}],
                 'uplinkSets': [lig_uplink_sets2['UplinkSet_1'].copy(), lig_uplink_sets2['UplinkSet_2'].copy(), ], 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess':[], 'enabled':True, 'description':None, 'name':None, 'state':None, 'status':None, 'eTag':None, 'category':'snmp-configuration', 'uri':None},
                 'qosConfiguration':None}
                ]

lig_hill_edit = {'name': 'LIG_Hill',
                 'type': 'logical-interconnect-groupV7',
                 'enclosureType': 'C7000',
                 'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                 'uplinkSets': [lig_uplink_sets2['UplinkSet_1'].copy(), lig_uplink_sets2['UplinkSet_2'].copy(), lig_uplink_sets2['UplinkSet_3'].copy(), lig_uplink_sets2['UplinkSet_4'].copy()], 'stackingMode': 'Enclosure',
                 'ethernetSettings': None,
                 'state': 'Active',
                 'telemetryConfiguration': None,
                 'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '15.186.21.149', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': ['Critical', 'Major', 'Minor', 'Warning', 'Normal', 'Info', 'Unknown'], 'vcmTrapCategories':['Legacy'], 'enetTrapCategories':['PortStatus', 'PortThresholds', 'Other'], 'fcTrapCategories':['PortStatus', 'Other']}], 'snmpAccess': [], 'enabled': True, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                 'qosConfiguration': None}

lig_hill_trap6 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [], 'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': {'type': 'snmp-configuration', 'readCommunity': 'public', 'systemContact': '', 'trapDestinations': [{'trapDestination': '1.1.1.1', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '2.2.2.2', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '3.3.3.3', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '4.4.4.4', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '5.5.5.5', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}, {'trapDestination': '6.6.6.6', 'communityString': 'public', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories':[], 'enetTrapCategories':[], 'fcTrapCategories':[]}], 'snmpAccess': [], 'enabled': True, 'description': None, 'name': None, 'state': None, 'status': None, 'eTag': None, 'category': 'snmp-configuration', 'uri': None},
                  'qosConfiguration': None}

lig_hill_config = {'name': 'LIG_Hill',
                   'type': 'logical-interconnect-groupV5',
                   'enclosureType': 'C7000',
                   'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                               {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                   'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_1'].copy(), lig_uplink_config['UplinkSet_2'].copy(),
                                  lig_uplink_config['UplinkSet_3'].copy(), lig_uplink_config['UplinkSet_4'].copy()],
                   'stackingMode': 'Enclosure',
                   'ethernetSettings': None,
                   'state': 'Active',
                   'telemetryConfiguration': None,
                   'snmpConfiguration': None,
                   'qosConfiguration': None}

lig_hill_edit1 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_2'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit2 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_3'].copy(), lig_uplink_server['UplinkSet_4'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit3 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_5'].copy(), lig_uplink_server['UplinkSet_6'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit4 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_7'].copy(), lig_uplink_server['UplinkSet_8'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit5 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_9'].copy(), lig_uplink_server['UplinkSet_10'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit6 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_11'].copy(), lig_uplink_server['UplinkSet_12'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit7 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_13'].copy(), lig_uplink_server['UplinkSet_14'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit8 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_15'].copy(), lig_uplink_server['UplinkSet_16'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

lig_hill_edit9 = {'name': 'LIG_Hill',
                  'type': 'logical-interconnect-groupV5',
                  'enclosureType': 'C7000',
                  'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 16Gb 24-Port FC Module'},
                                              {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 16Gb 24-Port FC Module'}],
                  'uplinkSets': [lig_uplink_sets['UplinkSet_1'].copy(), lig_uplink_server['UplinkSet_17'].copy(), lig_uplink_server['UplinkSet_18'].copy()],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None,
                  'qosConfiguration': None}

#  Bay number to get the port statistics of the FC module in interconnect page
#  The number is applicable to the interconnect number in interconnect page
#  fc_bay_num = lig_uplink_sets['UplinkSet_2']['logicalPortConfigInfos'][0]['bay']
#  portno_for_statistics = [lig_uplink_sets['UplinkSet_2']['logicalPortConfigInfos'][0]['port'],lig_uplink_sets['UplinkSet_2']['logicalPortConfigInfos'][1]['port']]


enc_group_V200 = {'name': 'EG_Hill',
                  'type': 'EnclosureGroupV200',
                  'enclosureTypeUri': '/rest/enclosure-types/c7000',
                  'stackingMode': 'Enclosure',
                  'interconnectBayMappingCount': 8,
                  'configurationScript': None,
                  'interconnectBayMappings':
                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}

enc_group_hill = {'name': 'EG_Hill', 'interconnectBayMappings':
                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:LIG_Hill'},
                   {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                   {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}],
                  "ipRangeUris": [],
                  "enclosureCount": 1,
                  "osDeploymentSettings": None,
                  "configurationScript": None,
                  "powerMode": None,
                  "ambientTemperatureMode": "Standard"}


encs_m = {'hostname': '15.186.27.232', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': None, 'licensingIntent': 'OneViewStandard', 'state': 'Monitored'}

encs_fwupdate = [{'hostname': '15.186.27.232', 'username': 'Administrator', 'password': 'compaq', 'enclosureGroupUri': 'EG:EG_Hill', 'force': False, 'licensingIntent': 'OneView', 'firmwareBaselineUri': Snap6_SPP_Uri, 'forceInstallFirmware': True, 'updateFirmwareOn': 'EnclosureOnly'}]

enclosure_preview = {"hostname": "15.186.27.232", "username": "Administrator", "password": "compaq", "ligPrefix": "LIG_Hill", "force": True, "logicalInterconnectGroupNeeded": True}

intervals = ['3', '20', '60', '100', '0', '1801', '-1', '120', '180']

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
                               'portConfigInfos': [{'bay': '5', 'port': '1', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1},
                                                   {'bay': '5', 'port': '2', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}]}
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
                                  'portConfigInfos': [{'bay': '5', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},

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
                                  'portConfigInfos': [{'bay': '6', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},

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
                                  'portConfigInfos': [{'bay': '5', 'enclosure': ENC1, 'port': '1', 'desiredSpeed': 'Auto'}, {'bay': '5', 'enclosure': ENC1, 'port': '2', 'desiredSpeed': 'Auto'}]},

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
                                  'portConfigInfos': [{'bay': '6', 'enclosure': ENC1, 'port': '1', 'desiredSpeed': 'Auto'}, {'bay': '6', 'enclosure': ENC1, 'port': '2', 'desiredSpeed': 'Auto'}]},

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
                                  'portConfigInfos': [{'bay': '5', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},

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
                                  'portConfigInfos': [{'bay': '6', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}]},

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
                                  'portConfigInfos': [{'bay': '5', 'port': '2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},

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
                                  'portConfigInfos': [{'bay': '6', 'port': '2', 'desiredSpeed': 'Speed16G', 'enclosure': ENC1}]},

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
                                  'portConfigInfos': [{'bay': '5', 'port': '2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},

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
                                   'portConfigInfos': [{'bay': '6', 'port': '2', 'desiredSpeed': 'Speed16G', 'enclosure': ENC1}]},

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
                                   'portConfigInfos': [{'bay': '5', 'port': '2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},

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
                                   'portConfigInfos': [{'bay': '5', 'port': '1', 'desiredSpeed': 'Speed16G', 'enclosure': ENC1}]},

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
                                   'portConfigInfos': [{'bay': '5', 'port': '1', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}]},

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
                                   'portConfigInfos': [{'bay': '5', 'port': '2', 'desiredSpeed': 'Speed16G', 'enclosure': ENC1}]},

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

server_profiles_gen8 = [
    [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 3',
      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
      'name': 'Profile_server2', 'description': '', 'affinity': 'Bay',
      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                              'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                              'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                             ]},
      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}],
    [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 6',
      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
      'name': 'Profile_server4', 'description': '', 'affinity': 'Bay',
      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                              'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                              'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                             ]},
      'boot': {'manageBoot': True, 'order': ["HardDisk"]}, "bootMode":{'manageMode': True, 'mode': 'UEFI', 'secureBoot': 'Disabled', 'pxeBootPolicy': 'Auto'}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':None, 'uuid':None}]]


p = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
      'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                              'requestedMbps': 'Auto', 'networkUri': 'FC:fc3_hill',
                                              'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}, {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                                                   'requestedMbps': 'Auto', 'networkUri': 'FC:fc4_hill',
                                                                                                   'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}

                                             ]},
      'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}],
p = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 5',
      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
      'name': 'Profile_server5', 'description': '', 'affinity': 'Bay',
      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                              'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                              'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}, {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                                                                   'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                                                                                   'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}

                                             ]},
      'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}],
p = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 10',
      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
      'name': 'Profile_server10', 'description': '', 'affinity': 'Bay',
      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc3_hill',
                                                 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                             {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                              'requestedMbps': 'Auto', 'networkUri': 'FC:fc4_hill',
                                              'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                             ]},
      'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

#  The below profile is used for MLR test case
#  server_profiles_gen8_enc1_bay1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 4',
#  'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:'+ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
#  'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
#  'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
#  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
#  {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
#  'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
#  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
#  ],
#  'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios':False,'overriddenSettings':[]}, 'sanStorage': None}]


server_profiles_gen8_bay1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 1',
                              'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                              'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                              'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'mac': None, 'wwpn': '', 'wwnn': ''}],
                              'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]


server_profiles_gen9 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 1',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'mac': None, 'wwpn': '', 'wwnn': ''}],
                         'boot': None, 'bootMode': {'manageMode': False}, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_edit1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 10',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'UserDefined', 'macType': 'Virtual', 'wwnType': 'Physical',
                          'name': 'SP_Config1', 'description': '', 'affinity': 'Bay',
                          'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'boot': {'priority': 'NotBootable'}, 'macType': 'UserDefined', 'mac': MAC_address_UD, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                           'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpnType': 'UserDefined', 'wwpn': WWPN_UD, 'wwnn': WWNN_UD}
                                          ],
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':Serial_number_UD, 'uuid':UUID_UD}]

server_profiles_edit2 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 10',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                          'name': 'SP_Config1', 'description': '', 'affinity': 'Bay',
                          'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                           'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None}
                                          ],
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':None, 'uuid':None}]

server_profiles_edit3 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 10',
                          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                          'name': 'SP_Config1', 'description': '', 'affinity': 'Bay',
                          'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                          {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                           'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                           'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': None, 'wwnn': None}
                                          ],
                          'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None, 'serialNumber':None, 'uuid':None}]

server_profiles_server7_bay1 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 1',
                                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                 'name': 'Profile_server1', 'description': '', 'affinity': 'Bay',
                                 'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                 {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                  'requestedMbps': 'Auto', 'networkUri': 'FC:fc1_hill',
                                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}],
                                 'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']}, 'bios':{'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]

server_profiles_server7_bay10 = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 10',
                                  'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG_Hill', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Physical',
                                  'name': 'Profile_server10', 'description': '', 'affinity': 'Bay',
                                  'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:enet_hill',
                                                   'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                  {'id': 2, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                                   'requestedMbps': 'Auto', 'networkUri': 'FC:fc2_hill',
                                                   'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}],
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

linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

oa_details = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_edit1[0]['serverHardwareUri'].split(' ')[-1]}

VC_details = {'oa_ip': encs[0]['hostname'], "username": encs[0]["username"], "password": encs[0]["password"], "server_bay": server_profiles_edit1[0]['serverHardwareUri'].split(' ')[-1]}

diskspd_cmd = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d120 -r -w70 -t9 -o9 -b20K -h -L E:\\multi5.dat >C:\\Ov_restartbefore1.dat"

diskspd_cmd_16Gb = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d120 -r -w70 -t19 -o12 -b40k -h -L E:\\multi5.dat >C:\\Ov_restartbefore1.dat"

diskspd_cmd_1 = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d1200 -r -w70 -t9 -o9 -b20K -h -L E:\\multi5.dat >C:\\Ov_restartafter2.dat"

diskspd_cmd_disable_ports = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c60M -d86600 -r -w70 -t19 -o19 -b30K -h -L E:\\port_disable_enable.dat >C:\\port_dis_enable_1.dat"

diskspd_cmd_effuse = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c80M -d740 -r -w70 -t9 -o9 -b20K -h -L E:\\oa_failover.dat >C:\\OA_Failover_traffic.dat"
#  Change this path according to the Checkout copy directory
module_file_path = "C:\\ONR\\fusion\\tests\\wpst_crm\\feature_tests\\C7000\\F137\\GetServerIPs.py"

diskspd_cmd_48_hours = "C:\\disk\\Diskspd-v2.0.17\\amd64fre\\diskspd.exe -c50M -d172800 -r -w70 -t9 -o9 -b20K -h -L E:\\multi6.dat >C:\\OA_Failover_traffic.dat"

windows_server_cred = ["Administrator", 'password@123']

bay_no = [5, 6]

interconnect_no = [5, 6]

manual_IP = ['15.186.24.121', '15.186.24.131']

hostname_manual = 'ABCDEFGH'

uplink_sets = [{'name': 'us_fc1',
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
                'portConfigInfos': [{'bay': '3', 'port': '2', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1},
                                    {'bay': '3', 'port': '3', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}
                                    ]},
               {'name': 'us_fc2',
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
                'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1},
                                    {'bay': '4', 'port': '2', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}
                                    ]}]

uplink_sets1 = [{'name': 'us_fc1',
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
                 'portConfigInfos': [{'bay': '3', 'port': '2', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}]},
                {'name': 'us_fc2',
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
                 'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Speed4G', 'enclosure': ENC1}]}
                ]

san_switch_details = {'ip': '15.186.29.162 ', 'username': 'admin', 'password': 'password'}
switch_cmd = ['switchshow']
port_list = {'npiv_port': ['5', '6']}
login_dist = ['1 N Port + 1 NPIV public', '1 N Port + 2 NPIV public']

# OVF3626
APPLIANCE_IP = '15.245.131.108'
ADMIN_CREDS = {'userName': 'Administrator', 'password': 'hpvse123'}

ICM_MODEL = 'Virtual Connect SE 100Gb F32 Module for Synergy'
IC_state = 'Configured'

ENC1 = 'CN754406WY'
ENC2 = 'XXXXXXXXXX'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'
test = 'Nitro'  # uri for syslog

'''
Interconnect Map Template for LIG
'''

InterconnectMapTemplate1 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
]

InterconnectMapTemplate2 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
]

InterconnectMapTemplate3 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 3}
]

InterconnectMapTemplate_Aside = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                                  'enclosureIndex': 1}]

InterconnectMapTemplate_Bside = [{'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy',
                                  'enclosureIndex': 1}]

################################################################################################
#                                Variables for Nitro Hardware
# ##############################################################################################

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################

# REDUNDANCY = 'HA'
# LIG = 'LIG'
LI = 'LE-LIG'

snmp_host = '15.245.133.30'
snmp_host2 = '15.245.134.7'
snmp_user = 'root'
snmp_pass = 'rootpwd'
snmp_path = 'root/SNMP'
syslog_path = 'var/log'
snmp_file = 'vcmtrap.log'
syslog_file = 'messages'

icm_bays = ['3', '6']

frame = 1
IBS = 3
LIG_ETH1_UPLINKS = ['Q1', 'Q1']
LIG_FC_UPLINKS = ['Q3.1']
# EG = 'EG' + '-' + REDUNDANCY
EG = 'EG'
EG1 = 'EG1'
# LE = 'LE'
# LE = 'LE' + '-' + REDUNDANCY
ENC1 = 'CN754406WY'
ENC2 = 'CN754404R2'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]
# LI = LE + '-' + LIG
# LI = 'LE-LIG'

uplink_sets_in_lig_A = [
    {
        'name': 'US-eth1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net_Vlan_401'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_ETH1_UPLINKS[0], 'speed': 'Auto'}
        ]
    }]

uplink_sets_in_lig_B = [
    {
        'name': 'US-eth2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['Net_Vlan_401'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '6', 'port': LIG_ETH1_UPLINKS[0], 'speed': 'Auto'}
        ]
    }]


uplink_sets_nitro1 = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Net_Vlan_401'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '3', 'enclosure': '1', 'port': 'Q1', 'speed': 'Auto'}]},
                      'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged', 'networkUris': ['Net_Vlan_402'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                      'logicalPortConfigInfos': [{'bay': '6', 'enclosure': '1', 'port': 'Q1', 'speed': 'Auto'}]}
                      }

trap_output = '\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::fallingAlarm) Uptime: 0:15:21.63\r\n\tRMON-MIB::alarmIndex = INTEGER: 139\tRMON-MIB::alarmVariable = OID: IF-MIB::ifOutOctets.247\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 0\tRMON-MIB::alarmFallingThreshold = INTEGER: 148\r\n2018-07-31 18:11:47 15.245.132.117(via UDP: [15.245.132.117]:44481) TRAP, SNMP v1, community public\r\n\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::risingAlarm) Uptime: 0:15:21.63\r\n\tRMON-MIB::alarmIndex = INTEGER: 159\tRMON-MIB::alarmVariable = OID: IF-MIB::ifOutOctets.272\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 562335\tRMON-MIB::alarmRisingThreshold = INTEGER: 178\r\n2018-07-31 18:11:59 15.245.132.117(via UDP: [15.245.132.117]:46725) TRAP, SNMP v1, community public\r\n\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::fallingAlarm) Uptime: 0:15:41.66\r\n\tRMON-MIB::alarmIndex = INTEGER: 153\tRMON-MIB::alarmVariable = OID: IF-MIB::ifInOctets.267\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 0\tRMON-MIB::alarmFallingThreshold = INTEGER: 162\r\n2018-07-31 18:11:59 15.245.132.117(via UDP: [15.245.132.117]:53880) TRAP, SNMP v1, community public\r\n\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::fallingAlarm) Uptime: 0:15:41.80\r\n\tRMON-MIB::alarmIndex = INTEGER: 155\tRMON-MIB::alarmVariable = OID: IF-MIB::ifOutOctets.267\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 0\tRMON-MIB::alarmFallingThreshold = INTEGER: 164\r\n2018-07-31 18:11:59 15.245.132.117(via UDP: [15.245.132.117]:58533) TRAP, SNMP v1, community public\r\n\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::fallingAlarm) Uptime: 0:15:41.80\r\n\tRMON-MIB::alarmIndex = INTEGER: 157\tRMON-MIB::alarmVariable = OID: IF-MIB::ifInOctets.272\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 0\tRMON-MIB::alarmFallingThreshold = INTEGER: 166\r\n2018-07-31 18:11:59 15.245.132.117(via UDP: [15.245.132.117]:38797) TRAP, SNMP v1, community public\r\n\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::fallingAlarm) Uptime: 0:15:41.80\r\n\tRMON-MIB::alarmIndex = INTEGER: 159\tRMON-MIB::alarmVariable = OID: IF-MIB::ifOutOctets.272\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 0\tRMON-MIB::alarmFallingThreshold = INTEGER: 168\r\n2018-07-31 18:12:19 15.245.132.117(via UDP: [15.245.132.117]:53681) TRAP, SNMP v1, community public\r\n\tRMON-MIB::rmon Enterprise Specific Trap (RMON-MIB::fallingAlarm) Uptime: 0:16:01.83\r\n\tRMON-MIB::alarmIndex = INTEGER: 131\tRMON-MIB::alarmVariable = OID: IF-MIB::ifOutOctets.237\tRMON-MIB::alarmSampleType = INTEGER: deltaValue(2)\tRMON-MIB::alarmValue = INTEGER: 125\tRMON-MIB::alarmFallingThreshold = INTEGER: 140\r\n'
lig_Nitro = {'name': 'LIG',
             'interconnectMapTemplate': InterconnectMapTemplate1,
                     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                     'interconnectBaySet': IBS,
                     'redundancyType': 'Redundant',
                     'downlinkSpeedMode': 'SPEED_10GB',
                     'telemetryConfiguration': {'type': 'telemetry-configuration', 'enableTelemetry': True, 'sampleCount': 12, 'sampleInterval': 300},
                     'uplinkSets': [uplink_sets_nitro1['UplinkSet_1'].copy(), uplink_sets_nitro1['UplinkSet_2'].copy()],
             }


enc_group_A_B = {'name': "EG",
                 'enclosureCount': frame,
                 'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_A'},
                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_B'}],
                 'ipAddressingMode': 'DHCP'
                 }
enc_group_C_D = {'name': "EG_1",
                 'enclosureCount': frame,
                 'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_C'},
                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_D'}],
                 'ipAddressingMode': 'DHCP'
                 }

enc_group = {'name': "EG",
             'enclosureCount': frame,
             'interconnectBayMappings':
                 [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                  {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG'},
                  {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                  {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                  {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG'}],
             'ipAddressingMode': 'DHCP'
             }


LE_Nitro = {'name': "LE",
            'enclosureUris': ['ENC:' + ENC1],
            'enclosureGroupUri': 'EG:' + 'EG',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

les = {
    'Enc1-LE':
        {
            'name': 'LE_IGMP_SNOOPING_SE',
            'enclosureUris': [ENC1],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        },
    'Enc2-LE':
        {
            'name': 'LE_IGMP_SNOOPING_2ME',
            'enclosureUris': [ENC1, ENC2],
            'enclosureGroupUri': None,
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
        }}

Network_body = {'connectionTemplateUri': None,
                'ethernetNetworkType': 'Tagged',
                'name': 'Net_Vlan_401',
                'privateNetwork': False,
                'purpose': 'General',
                'smartLink': False,
                'type': 'ethernet-networkV4',
                'vlanId': 401
                }

Enet_nitro = [{'connectionTemplateUri': None,
               'ethernetNetworkType': 'Tagged',
               'name': 'Net_Vlan_401',
               'privateNetwork': False,
               'purpose': 'General',
               'smartLink': False,
               'type': 'ethernet-networkV4',
               'vlanId': 401
               },
              {'connectionTemplateUri': None,
               'ethernetNetworkType': 'Tagged',
               'name': 'Net_Vlan_402',
               'privateNetwork': False,
               'purpose': 'General',
               'smartLink': False,
               'type': 'ethernet-networkV4',
               'vlanId': 402
               },
              {'connectionTemplateUri': None,
               'ethernetNetworkType': 'Tagged',
               'name': 'Net_Vlan_403',
               'privateNetwork': False,
               'purpose': 'General',
               'smartLink': False,
               'type': 'ethernet-networkV4',
               'vlanId': 403
               }]
Enet_nitro_new = [{'connectionTemplateUri': None,
                   'ethernetNetworkType': 'Tagged',
                   'name': 'Net_Vlan401',
                   'privateNetwork': False,
                   'purpose': 'General',
                   'smartLink': False,
                   'type': 'ethernet-networkV4',
                   'vlanId': 401
                   }]


Vlans = ['401', '402', '403']

# Used to edit LIG's
LIG_names = ['LIG']

# Used to edit LI's
LI_names = ['LE-LIG']

snmpv1_body = {'readCommunity': 'public',
               'enabled': 'true',
               'systemContact': '',
               'snmpAccess': [],
               'snmpUsers': [],
               'trapDestinations': [
                   {'enetTrapCategories': [],
                    'vcmTrapCategories': [],
                    'trapSeverities':[],
                    'communityString': 'public',
                    'port': '162',
                    'fcTrapCategories': [],
                    'trapDestination': '15.245.133.30',
                    'trapFormat': 'SNMPv1'
                    }],
               'type': 'snmp-configuration',
               'v3Enabled': 'true'
               }

snmpv1_invalid_body = {'readCommunity': '',
                       'enabled': 'true',
                       'systemContact': '',
                       'snmpAccess': [],
                       'snmpUsers': [],
                       'trapDestinations': [
                           {'enetTrapCategories': [],
                            'vcmTrapCategories': [],
                            'trapSeverities':[],
                            'communityString': '',
                            'port': '162',
                            'fcTrapCategories': [],
                            'trapDestination': '15.245.133.30',
                            'trapFormat': 'SNMPv1'
                            }],
                       'type': 'snmp-configuration',
                       'v3Enabled': 'true'
                       }

trapDestination_2 = {'readCommunity': 'public',
                     'enabled': 'true',
                     'systemContact': '',
                     'snmpAccess': [],
                     'snmpUsers': [],
                     'trapDestinations': [
                         {'enetTrapCategories': [],
                             'vcmTrapCategories': [],
                             'trapSeverities':[],
                             'communityString': 'public',
                             'port': '162',
                             'fcTrapCategories': [],
                             'trapDestination': '15.245.133.30',
                             'trapFormat': 'SNMPv1'
                          },
                         {'enetTrapCategories': [],
                             'vcmTrapCategories': [],
                             'trapSeverities':[],
                             'communityString': 'public',
                             'port': '162',
                             'fcTrapCategories': [],
                             'trapDestination': '15.245.134.7',
                             'trapFormat': 'SNMPv1'
                          }],
                     'type': 'snmp-configuration',
                     'v3Enabled': 'true'
                     }


power_value = ['Off', 'On']
edit_power_body = {'op': 'replace',
                   'path': '/powerState',
                   'value': ''}

power_state = ['Maintenance', 'Configured']

valDict = {'status_code': 200,
           'taskState': 'Completed'}

remote_syslog_body = {
    "type": "RemoteSyslog",
    "sendTestLog": 'false',
    "remoteSyslogPort": "514",
    "remoteSyslogDestination": "15.245.133.30",
    "enabled": 'true'
}

remote_syslog_body2 = {
    "type": "RemoteSyslog",
    "sendTestLog": 'true',
    "remoteSyslogPort": "514",
    "remoteSyslogDestination": "15.245.133.30",
    "enabled": 'true'
}

remote_syslog_clear = {
    "type": "RemoteSyslog",
    "sendTestLog": 'false',
    "remoteSyslogPort": "",
    "remoteSyslogDestination": "",
    "enabled": 'false'
}

Syslog_message = ['DOWN', 'UP']
pattern = ['Link Status', 'for ethernet']
# Syslog-downlink disable = Network Adapter Link Down
snmp_walk_command = 'snmpwalk -Os -c public -v 1 ICMIP sysDescr.0'
Nitro_walk_module = 'VC SE 100Gb F32 Module'

lldpIpAddressMode = ['IPV4', 'IPV6', 'BOTH_IPV4_IPV6']

INTERCONNECTS = ['CN754406WY, interconnect 3', 'CN754406WY, interconnect 6']
Uplinksets_nitro = ['UplinkSet_1', 'UplinSet_2']
Linked_uplink_ports = ['Q1', 'Q1']
Linked_downlink_ports = ['d2', 'd2']
Linked_ports_uplink = [['Q1'], ['Q1']]
Linked_ports_downlink = [['d2'], ['d2']]
Linked_downlink_ports_bay6 = ['d6']
port_action = ['disable', 'enable']
portStatus = ['Unlinked', 'Linked']
# Disable uplink port
Edit_port_body = {
    "associatedUplinkSetUri": "",
    "interconnectName": "",
    "portType": "Uplink",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": "False",
    "portName": "",
    "type": "portV5"
}
# check port status
interconnect_status = {
    "name": "",
    "linked_ports": Linked_uplink_ports[0]

}

INTERCONNECTS_dto = {'name': 'CN754406WY, interconnect 3'}, {'name': 'CN754406WY, interconnect 6'}
list = [INTERCONNECTS_dto[0], INTERCONNECTS_dto[1]]


efuse_action = ['EFuseOn', 'EFuseOff']
ICM_reboot_action = ['On', 'Off']

SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC
FUSION_IP = '15.245.131.108'
IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'


# Utilization sampling
diff_sample_count = ['30', '15']
diff_sample_interval = ['70', '300']
diff_sample_interval_lag = ['100', '400']
diff_sample_interval_60 = ['60']
sample_interval_100 = '100'
invalid_sample_count_min = '11'
invalid_sample_count_max = '51'

invalid_sample_interval_min = '1'
invalid_sample_interval_max = '3601'

diff_octets = ['10000', '40000', '70000']
diff_pkts = ['80']
diff_pkts_bc = ['35']
diff_octets_bc = ['4000', '8000', '15000']
diff_sample_count_li = ['30', '20', '10']
diff_sample_interval_li = ['200', '400', '800']
time_interval_2min = '120'
time_interval_5min = '300'
time_interval_1min = '60'
time_interval = ['200', '400', '700']
time_interval_lag = ['200', '500']
time_interval_1 = ['300', '500', '900']
min_octets = '5000'
min_pkts = '50'
max_time = ['1200', '4800']
min_time = ['100', '400']
sample_count_1 = '12'
sample_count_2 = '15'
sample_count_disable = '0'
SH_bay6_name = 'CN754406WY, bay 6'

Server_profile1 = {'name': 'SP_1', 'type': 'ServerProfileV10', 'serverHardwareUri': 'SH:CN754406WY, bay 6', 'serialNumberType': 'Physical', 'iscsiInitiatorNameType': None, 'macType': 'Physical', 'wwnType': 'Physical', 'description': 'Updated Profile', 'affinity': 'Bay',
                   'connectionSettings': {'connections': [{'id': 1, 'name': 'Ethernet1', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_Vlan_401', 'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                                          {'id': 2, 'name': 'Ethernet2', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_Vlan_402', 'boot': None},
                                                          ]},
                   # 'boot':{'manageBoot':True, 'order':['HardDisk']},
                   'boot': None,
                   # 'bootMode':{'manageMode':True, 'mode':'UEFI', 'pxeBootPolicy':'Auto'},
                   'bootMode': None,
                   'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
                   'bios': None,
                   'hideUnusedFlexNics': None, 'iscsiInitiatorName': '', 'osDeploymentSettings': None,
                   'localStorage': None,
                   'sanStorage': None,
                   }
linux_details = {'hostip': '15.245.134.7', 'username': 'root', 'password': 'rootpwd', 'dir_location': '/root/', 'python_cmd': 'python2.7'}

ilo_details_enc1_bay6 = {'ilo_ip': '15.245.134.47', 'username': 'Administrator', 'password': 'hpvse1'}

server_details = {'username': 'Administrator', 'password': 'Hpvse1'}
broadcast_ip = '10.11.255.255'
ping_cmd1 = "ping -t -l 1024 'gateway_ip'>sample.txt"
ping_cmds = ["ping -t -l 64 'gateway_ip'>sample.txt", "ping -t -l 512 'gateway_ip'>sample.txt", "ping -t -l 1024 'gateway_ip'>sample.txt"]
ping_cmd_512 = "ping -t -l 512 'gateway_ip'>sample.txt"
kill_cmd = "TASKKILL /F /IM PING.EXE"
kill_diskspd = "TASKKILL /F /IM diskspd.exe"
iperf_start_server = 'iperf3.exe -s'
sampling_interval = '300'

diskspd_cmd = ["C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b10K -h -L D:\\sample.dat >C:\\sample1.dat", "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b20K -h -L D:\\sample.dat >C:\\sample1.dat", "C:\\Users\\Administrator\\Desktop\\Diskspd\\diskspd.exe -c50M -d300 -r -w70 -t9 -o9 -b30K -h -L D:\\sample.dat >C:\\sample1.dat"]

Li_telemetry_body = {"type": "telemetry-configuration",
                     "enableTelemetry": True,
                     "sampleCount": 15,
                     "sampleInterval": 200,
                     "description": None,
                     "status": None,
                     "name": "",
                     "state": None,
                     "eTag": None,
                     "created": None,
                     "modified": None,
                     "category": "telemetry-configurations",
                     "uri": ""}

Li_telemetry_body2 = {"type": "telemetry-configuration",
                      "enableTelemetry": True,
                      "sampleCount": 15,
                      "sampleInterval": 60,
                      "description": None,
                      "status": None,
                      "name": "",
                      "state": None,
                      "eTag": None,
                      "created": None,
                      "modified": None,
                      "category": "telemetry-configurations",
                      "uri": ""}

uplink_counters = ['1000', '700', '500']
downlink_counters = ['1000', '700', '500']

SNMPV3_LI_body_all_users = {'category': 'snmp-configuration',
                            'enabled': 'false',
                            'readCommunity': 'public',
                            'snmpAccess': [],
                            'snmpUsers': [{'snmpV3UserName': 'e20sysadminnone',
                                           'userCredentials': [],
                                           'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                          {'snmpV3UserName': 'e20sysadminshaaes',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e20sysadminmd5aes',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e20sysadminmd5des',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'MD5', 'v3PrivacyProtocol': 'DES56'},
                                          {'snmpV3UserName': 'e20sysadminshades',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                          {'snmpV3UserName': 'e20sysadminsha',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                            'trapDestinations': [{'communityString': '',
                                                  'enetTrapCategories': [],
                                                  'fcTrapCategories': [],
                                                  'inform': 'false',
                                                  'port': '162',
                                                  'trapDestination': '15.245.133.30',
                                                  'trapFormat': 'SNMPv3',
                                                  'trapSeverities': [],
                                                  'userName': 'e20sysadminmd5des',
                                                  'vcmTrapCategories': []}],
                            'type': 'snmp-configuration',
                            'uri': '',
                            'v3Enabled': 'true'}

SNMPV3_LIG_body_users = {'category': 'snmp-configuration',
                         'enabled': 'false',
                         'readCommunity': 'public',
                         'snmpAccess': [],
                         'snmpUsers': [

                             {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

                             {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA'},

                             {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'NA'},

                             {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'NA'},

                             {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},

                             {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'TDEA'},

                             {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'},

                             {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},

                             {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'}],

                         'trapDestinations': [{'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.245.133.30',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'User1',
                                               'vcmTrapCategories': []}],
                         'type': 'snmp-configuration',
                         'uri': '',
                         'v3Enabled': 'true'}

SNMPV3_SHA = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'User8',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA384',
                                         'v3PrivacyProtocol': 'AES192'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.245.133.30',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'User8',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

SNMPV3_LIG_body_11_users = {'category': 'snmp-configuration',
                            'enabled': 'false',
                            'readCommunity': 'public',
                            'snmpAccess': [],
                            'snmpUsers': [

                                       {'snmpV3UserName': 'User1', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},

                                       {'snmpV3UserName': 'User2', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'NA'},

                                       {'snmpV3UserName': 'User3', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'NA'},

                                       {'snmpV3UserName': 'User4', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'NA'},

                                       {'snmpV3UserName': 'User5', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},

                                       {'snmpV3UserName': 'User6', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'TDEA'},

                                       {'snmpV3UserName': 'User7', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA512', 'v3PrivacyProtocol': 'AES128'},

                                       {'snmpV3UserName': 'User8', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'AES192'},

                                       {'snmpV3UserName': 'User9', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES256'},

                                       {'snmpV3UserName': 'User10', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA256', 'v3PrivacyProtocol': 'TDEA'},

                                       {'snmpV3UserName': 'User11', 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}, {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password123', 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}], 'v3AuthProtocol': 'SHA384', 'v3PrivacyProtocol': 'DES56'}],

                            'trapDestinations': [{'communityString': '',
                                                  'enetTrapCategories': [],
                                                  'fcTrapCategories': [],
                                                  'inform': 'false',
                                                  'port': '162',
                                                  'trapDestination': '15.245.133.30',
                                                  'trapFormat': 'SNMPv3',
                                                  'trapSeverities': [],
                                                  'userName': 'User1',
                                                  'vcmTrapCategories': []}],
                            'type': 'snmp-configuration',
                            'uri': '',
                            'v3Enabled': 'true'}


LI_update = {'name': LI}
v1_trap = {'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories': [], 'port': '162',
           'trapDestination': '15.245.134.7', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories': []}

v1_trap_list = [{'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories':[], 'port':'162',
                 'trapDestination':'15.245.134.7', 'trapFormat': 'SNMPv1', 'trapSeverities':[], 'vcmTrapCategories':[]}]

v3_7trapDestinations = [{'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User1',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User2',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User3',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User4',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User5',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User6',
                         'vcmTrapCategories': []},
                        {'communityString': '',
                         'enetTrapCategories': [],
                         'fcTrapCategories': [],
                         'inform': 'false',
                         'port': '162',
                         'trapDestination': '15.245.133.30',
                         'trapFormat': 'SNMPv3',
                         'trapSeverities': [],
                         'userName': 'User7',
                         'vcmTrapCategories': []}]

alternate_trap_ip = '15.245.134.7'
li_usernames_edit = ['sha5des_1', 'md5aes_1', 'sha_1_aes', 'sha_d_des', 'shA1', 'sha_none']
engine_id = '0x80001F888071F26C0ED6B8E15800000000'

Empty_list = ['', '']
null_list = []

invalid_userCredentials = [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'HPEoneview',
                            'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                           {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'HPEoneview',
                            'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]

inavlid_snmp_usernames = ['talent@123', '        ', 'Change$!#']
max_length_username = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '']
valid_snmp_username = ['snmpusernmae', '12345678', 'password123', 'change_1234', 'ABCDEFGH', 'AbCdEfGh']
invalid_auth_passwords = '       '
valid_auth_username = ['snmpusernmae', '12345678', 'change_1234', 'AbCdEfGh']
min_length_auth_password = 'hello'

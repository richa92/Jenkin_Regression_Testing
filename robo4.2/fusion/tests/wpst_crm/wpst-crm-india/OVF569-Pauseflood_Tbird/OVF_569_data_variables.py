import os
import sys
import paramiko
import time
import re


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


def file_exists(file_path):
    file = os.path.exists('file_path')


def removefile(file_path):
    file = os.remove('file_path')


def Remove_Whitespace(instring):
    return instring.strip()

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ENC1 = 'TCAY635A5E'
ENC2 = '6HISEUIFY1'
ENC_SNMP = 'EM1FFFF500'
LE_name = 'LE'
DL_PORT = '6'
LIGname = 'LIG1'
PFPTrue = True
PFPFalse = False
ICM_1 = ENC1 + ', interconnect 3'
li = 'LE-LIG1'
SERVER_BAY = ENC1 + ', bay 6'
DL_PORT_NUMBER = '9'
DL_PORT_NAME = ['d6', 'd10']
UL_PORT_NAME = ['Q1:1', 'Q2.1', 'Q7']
UL_PORT_NAME_X1 = 'Q7'
PFD_PORT_STATUS_REASON = 'PauseFloodDetected'
PFD_PORT_STATUS_REASON_NONE = 'None'
PORT_STATUS_REASON_ACTIVE = 'Active'
PORT_STATUS_REASON_STANDBY = 'Standby'
PORT_STATUS_REASON_OK = 'Ok'
PORT_STATUS_LINK = 'Linked'
PORT_STATUS_UNLINK = 'Unlinked'
PORT_STATUS_DISABLE = 'Disabled'
PORT_STATUS_UNKNOWN = 'Unknown'
PORT_STATUS_DISABLED = 'AdminDisabled'
PORT_STATUS_REASON_NONE = 'None'
DISABLE_PORT = 'false'
ENABLE_PORT = 'true'
UPLINK_MSG = 'A pause flood condition has been detected on the uplink port(s) ' + UL_PORT_NAME[0] + '.'
DOWNLINK_MSG = 'Connection on downlink port ' + DL_PORT + ', subport a  has failed. A pause frame flood condition caused the port to be unlinked.'
DOWNLINK_MSG1 = 'Connection on downlink port ' + DL_PORT + ', subport c  has failed. A pause frame flood condition caused the port to be unlinked.'
COMPLAINCE_ALERT = 'The logical interconnect is inconsistent with the logical interconnect group ' + LIGname + '.'
COMPLAINCE_ALERT_1 = 'The logical interconnect is inconsistent with the logical interconnect group ' + LIGname + '.\nInterconnect settings do not match the template.'
COMPLAINCE_ALERT_2 = 'The logical interconnect is inconsistent with the logical interconnect group ' + LIGname + '.\nInterconnect settings do not match the template.'
FW_ALERT = 'Interconnect firmware version is less than the required firmware version'
IC_Absernt_MSG = 'The interconnect module is absent. A Virtual Connect SE 40Gb F8 Module for Synergy is expected.'
POWER_OFF = 'Off'
POWER_ON = 'On'
RESET = 'Reset'
POWER_STATE = '/powerState'
RESET_STATE = '/deviceResetState'
IC_CONFIG_STATE = 'Configured'
IC_CONFIG_ERROR_STATE = 'Configuration error'
IC_ABSENT_STATE = 'Absent'
IC_MAINTENANCE_STATE = 'Maintenance'
SERVER_PROF_MSG1 = 'An error has occurred on connection 2.  A pause frame flood condition caused the port to be unlinked.'
SERVER_PROF_MSG = 'An error has occurred on connection 1.  A pause frame flood condition caused the port to be unlinked.'
varTrue = True
varFalse = False
Alert = ['Active', 'Locked']
Consistency_State = ['CONSISTENT', 'NOT_CONSISTENT']
localfile = 'HPEOneView-fullupdate-4.00.00-SNAPSHOT-0300225.bin'
version_Check = '4.00.00-0300225'
Upload_Sleep_Time = '4200'
ic_firmwareVersion_old = '1.2.0.62'
ic_firmwareVersion_new = '1.2.0.64'
ic_firmwareVersion_old_unsupported = '1.1.0.6'
old_SPP_bundle = 'Cust-K120-62-EM201-Dev.iso'
old_SPP_bundle_name = 'Cust-K120-62-EM201-Dev'
latest_SPP_bundle = 'Cust-K120-64-EM201-Dev.iso'
latest_SPP_bundle_name = 'Cust-K120-64-EM201-Dev'
unsupported_SPP_bundle = 'cust-k110-Dev-EM2-G10BB.iso'
unsupported_SPP_bundle_name = 'cust-k110-Dev-EM2-G10BB'
recommendedAction = 'Retry the downgrade operation for the constituent interconnects with an SPP containing the minimum supported firmware version or higher.'
li_update_error = 'Staging failed for the LI ' + li
Enet_switch_ip = ''
switch_port_num = ''
Portname = "portname"
team_status_cmd = "Get-NetLbfoTeam -Name 'Team1' | fl Name,Status"
detlete_team_cmd = "Remove-NetLbfoTeam 'Team1'"
MacAddress = 'A6-B2-42-D0-00-39'
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'switchindependent'"
Poweron_Server_Sleeptime = '600'
vlan_tagging_cmd = "Set-NetAdapter \-Name 'interface_name' -VlanId 'valn_id'"
EM_SN = ENC1
EM_SNMP = ENC_SNMP
EG_name = 'EG_check'
HOST = '192.168.144.171'
HOST_SNMP = '192.168.144.144'
Efuse_sleep_time = '500'
uplinkset_name = 'set1'
Efuse_Action = ['EFuseOn', 'EFuseOff']
Bay_No = '3'
Bay_SNMP = ['3', '6']
# Bay_No = '6'
# Server_No = '1'
Server_No = '6'
Server_SNMP = '3'
IC_IP = '192.168.146.23'
ic_set_pf = 'enable'
ic_off_pf = 'disable'
uplink_interface = "Ten-GigabitEthernet 0/0/1:1"
switchport_interface = "Ten-GigabitEthernet1/0/38"
disable_command = "shutdown"
enable_command = "undo shutdown"
stacking_interface = "FortyGigE 0/0/7"
downlink_interface = "TwentyGigE 0/1/6"
portType = 'Uplink'
firmware_warning = 'Unable to update firmware for the logical interconnect LE-LIG as an attempt was made to downgrade the firmware below the minimum supported version for the following constituent interconnects:CN77080KR1, interconnect 3'
LE_unsupported_alert = 'The interconnect firmware does not support the current configuration for: Pause Flood Protection. Please upgrade the firmware to 1.2.0 or later or remove the unsupported configuration.'
IC_ERROR = 'The interconnect is Unmanaged.'
IC_unmanaged_STATE = 'Unmanaged'
FW_ALERT = 'Interconnect firmware version is less than the required firmware version'
dump_file_path = ''
server_ip = '192.168.145.106'
li_disable = {"type": "EthernetInterconnectSettingsV4", "enablePauseFloodProtection": False}
li_enable = {"type": "EthernetInterconnectSettingsV4", "enablePauseFloodProtection": True}
Disable_Ports = [{"interconnectName": ICM_1, "portType": "Uplink", "portId": '', "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":False, "portName":"Q1:1", "portStatus":"Linked", "type":"port"},
                 ]
Enable_Ports = [{"interconnectName": ICM_1, "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":True, "portName":"Q3", "portStatus":"Unknown", "type":"port"}]
interconnects_disable = [ENC1 + ', interconnect 3']
INTERCONNECTS = [ENC1 + ', interconnect 3']
INTERCONNECTS1 = [ENC2 + ', interconnect 5']
downlink_port_disable = [{"interconnectName": ICM_1, "portType": "Downlink", "portId": '', "enabled": False, "portName": "d1", "portStatus": "Linked", "type": "port"},
                         ]
downlink_port_enable = [{"interconnectName": ICM_1, "portType": "Downlink", "portId": '', "enabled": True, "portName": "d1", "portStatus": "Linked", "type": "port"},
                        ]
uplink_ports = ['Q1:1', 'Q2:1']
switch_port_num = ['2']
downlink_ports = ['d1']
users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Storageadmin', 'password': 'Storageadmin', 'fullName': 'Storageadmin', "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         {'userName': 'InfrastructureAdmin', 'password': 'InfrastructureAdmin', 'fullName': 'InfrastructureAdmin', "enabled": True, "permissions": [{"roleName": "Infrastructure administrator", "scopeUri": None}], 'emailAddress': '', 'officePhone': '', 'mobilePhone': '', 'type': 'UserAndPermissions'},
         ]

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            {'userName': 'InfrastructureAdmin', 'password': 'InfrastructureAdmin'},
            ]
LE = 'LE'

ethnets = [{'name': 'Net_1',
            'type': 'ethernet-networkV4',
            'vlanId': '1601',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'ethernetNetworkType': 'Tagged'},
           {'name': 'Net2',
            'type': 'ethernet-networkV4',
            'vlanId': '1',
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'ethernetNetworkType': 'Tagged'},
           {'name': 'Net3',
            'type': 'ethernet-networkV4',
            'vlanId': '10',
            'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'ethernetNetworkType': 'Tagged'},
           ]

fcoenets = [
    {
        "name": "FCoENet_1602",
        "vlanId": "1602",
        "type": "fcoe-networkV4"
    }, ]

icmap_SE = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
            ]

uplink_sets = {'us1': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'set2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net3'],
                       'nativeNetworkUri': 'Net3',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                  ]},
               'us3': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['FCoENet_1602', 'Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                  ]},
               'us4': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': []},
               }
redundancyType = 'NonRedundantASide'
ligs = {'LIG1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': [{'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False}],
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig2':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                              'interconnectType': 'Ethernet',
                              'enablePauseFloodProtection': False,
                              'enableIgmpSnooping': False,
                              'igmpIdleTimeoutInterval': 260,
                              'enableFastMacCacheFailover': True,
                              'macRefreshInterval': 5,
                              'enableNetworkLoopProtection': True,
                              'enableTaggedLldp': False,
                              'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig3':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig4':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig5':
        {'name': 'LIG2',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': [{'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False}],
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig6':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig7':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us3'].copy()],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig8':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                              'interconnectType': 'Ethernet',
                              'enablePauseFloodProtection': True,
                              'enableIgmpSnooping': False,
                              'igmpIdleTimeoutInterval': 260,
                              'enableFastMacCacheFailover': True,
                              'macRefreshInterval': 5,
                              'enableNetworkLoopProtection': True,
                              'enableTaggedLldp': False,
                              'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig9':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_SE,
         'enclosureIndexes': [1],
         'interconnectBaySet': 3,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us4'].copy()],
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4',
                              'interconnectType': 'Ethernet',
                              'enablePauseFloodProtection': True,
                              'enableIgmpSnooping': False,
                              'igmpIdleTimeoutInterval': 260,
                              'enableFastMacCacheFailover': True,
                              'macRefreshInterval': 5,
                              'enableNetworkLoopProtection': True,
                              'enableTaggedLldp': False,
                              'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        }
enc_group_SE = {'name': 'EG1',
                'enclosureCount': 1,
                'interconnectBayMappings':
                [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIGname},
                 ],
                'ipAddressingMode': 'DHCP',
                'ipRangeUris': [],
                'powerMode': 'RedundantPowerFeed'
                }
LE = [{'name': LE,
       'enclosureUris': ['ENC:' + ENC1],  # REAL
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False},
      ]
iLo_1 = '192.168.149.27'
ilo1_details = {'ilo_ip': iLo_1, 'username': 'Administrator', 'password': 'hpvse123'}
ip_1 = '195.168.140.108'
server1_details = {'windows_ip': ip_1, 'username': 'root', 'password': '12iso*help12345'}
up_interface = "ifup interface-name"
server_profiles = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net2', 'mac': None, 'wwpn': None, 'wwnn': None}]}}]

server_profiles1 = [{'type': 'ServerProfileV8', 'name': 'Profile1', 'serverHardwareUri': ENC1 + ', bay 6',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': []}}
                    ]

server_profile_fcoe = [{'type': 'ServerProfileV8', 'name': 'Profile1', 'serverHardwareUri': ENC1 + ', bay 6',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                        'description': '', 'affinity': 'Bay',
                        'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                        'connectionSettings': {'connections': [
                            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                             'requestedMbps': '2500', 'networkUri': 'FCOE:FCoENet_1602', 'mac': None, 'wwpn': None, 'wwnn': None},
                            {'id': 5, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None}]}}
                       ]
iLo_1 = '192.168.149.27'
ip_1 = '192.168.145.38'
liupdate_body = {"sppUri": '',
                 "command": "UPDATE",
                 "force": True,
                 "ethernetActivationType": "Parallel",
                 "ethernetActivationDelay": "0",
                 "fcActivationType": "Parallel",
                 "fcActivationDelay": "0",
                 "validationType": "None"}

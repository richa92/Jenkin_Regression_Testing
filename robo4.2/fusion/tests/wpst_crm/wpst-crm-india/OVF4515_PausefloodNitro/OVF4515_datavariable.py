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
SFLOW_CONFIGURATION_ENABLED = "Pause flood protection will be enabled."
Multi_three_compliance_list = ['qualityOfService', 'snmp', 'uplinkSets', 'interconnectSettings', 'utilizationSampling', 'internalNetworks', 'sFlow']
ENC1 = 'TCAY635A5E'
ENC2 = '6HISEUIFY1'
LE_name = 'LE'
LIGname = 'LIG1'
PFPTrue = True
PFPFalse = False
ICM_1 = ENC2 + ', interconnect 5'
ICM_2 = ENC2 + ', interconnect 2'
li = 'LE-LIG1'
SERVER_BAY = ENC1 + ', bay 6'
DL_PORT = ['1', '13', '18', '6']
DL_PORT_NAME = ['d1', 'd3']
DL_PORT_NAME_ICM2 = ['d18', 'd1']
UL_PORT_NAME = ['Q1:1', 'Q2:1', 'Q7']
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
UPLINK_MSG1 = 'A pause flood condition has been detected on the uplink port(s) ' + UL_PORT_NAME[0] + ',' + UL_PORT_NAME[1] + '.'
UPLINK_MSG_STACKING = 'A pause flood condition has been detected on the uplink port(s) ' + UL_PORT_NAME[2] + '.'
DOWNLINK_MSG = 'Connection on downlink port ' + DL_PORT[0] + ', subport a  has failed. A pause frame flood condition caused the port to be unlinked.'
DOWNLINK_MSG1 = 'Connection on downlink port ' + DL_PORT[0] + ', subport c  has failed. A pause frame flood condition caused the port to be unlinked.'
DOWNLINK_MSG_2 = 'Connection on downlink port ' + DL_PORT[1] + ', subport a  has failed. A pause frame flood condition caused the port to be unlinked.'
DOWNLINK_MSG_1 = 'Connection on downlink port ' + DL_PORT[2] + ', subport a  has failed. A pause frame flood condition caused the port to be unlinked.'
DOWNLINK_MSG1_1 = 'Connection on downlink port ' + DL_PORT[3] + ', subport a  has failed. A pause frame flood condition caused the port to be unlinked.'


COMPLAINCE_ALERT = 'The logical interconnect is inconsistent with the logical interconnect group ' + LIGname + '.'
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
alert_type = ['swmon.pauseFloodDetected', 'crm.connectionStateChange', 'profilemgr.Connections.CONNECTION_SCMB_ERROR']
Alert = ['Active', 'Locked', 'Cleared']
Consistency_State = ['CONSISTENT', 'NOT_CONSISTENT']
localfile = 'HPEOneView-fullupdate-4.00.00-SNAPSHOT-0300225.bin'
version_Check = '4.00.00-0300225'
Upload_Sleep_Time = '4200'
ic_firmwareVersion_old = '2.0.0.65'
ic_firmwareVersion_new = '2.0.0.67'
ic_firmwareVersion_old_unsupported = '1.1.0.6'
old_SPP_bundle = 'Cust-K130-RC4-N200-65D-EM204-G10.iso'
old_SPP_bundle_name = 'Cust-K130-RC4-N200-65D-EM204-G10'
latest_SPP_bundle = 'Cust-K130-RC5-N200-67D-EM204-G10.iso'
latest_SPP_bundle_name = 'Cust-K130-RC5-N200-67D-EM204-G10'
unsupported_SPP_bundle = 'cust-k110-Dev-EM2-G10BB.iso'
unsupported_SPP_bundle_name = 'cust-k110-Dev-EM2-G10BB'
recommendedAction = 'Retry the downgrade operation for the constituent interconnects with an SPP containing the minimum supported firmware version or higher.'
li_update_error = 'Staging failed for the LI ' + li
Enet_switch_ip = ''
switch_port_num = ''
Portname = "portname"
Adapter_1 = "nmcli connection up adapter1"
Adapter_2 = "nmcli connection up adapter2"
Create_bond = "nmcli connection add type bond ifname bond-name mode 802.3ad"
Master_slave_1 = "nmcli con add type bond-slave ifname connection-name-1"
Master_slave_2 = "nmcli con add type bond-slave ifname connection-name-2"
Master = "master bond-name"
Bond_slave_1 = "nmcli connection up bond-slave-connection-name-1"
Bond_slave_2 = "nmcli connection up bond-slave-connection-name-2"
Network_bond = "nmcli connection up bond-bond-name"
Delete_Network_bond = "nmcli connection delete bond-bond-name"
Delete_bond_slave_1 = "nmcli connection delete bond-slave-connection-name-1"
Delete_bond_slave_2 = "nmcli connection delete bond-slave-connection-name-2"
set_ip_bond = "ifconfig bond-name"
up_interface = "ifup interface-name"
down_interface = "ifdown interface-name"
down_interface1 = "ifdown ens2f4"
get_interface = "ifconfig interface-name"
Ip_netmask = "ip netmask 255.255.255.0 up"
Set_ip = 'ip addr add ip-address'
Set_interface = 'dev interface-name'
interface_up = 'ip link set interface-name up'
Modify_bond = 'nmcli connection modify bond-bond-name'
Modify_ip = 'ip4 ip-address'
Modify_manual = 'netmask gw4 192.168.144.1 autoconnect yes ipv4.method manual'
Bond_1 = 'bond1'
Bond_2 = 'bond2'
Ip_bond_1 = '192.168.145.105'
Ip_bond_2 = '195.168.140.86'
Netmask = '21'
Space = ''
BACKUPFILE_DIR = ''
EM_SN = ENC2
EM_SN1 = ENC1
EG_name = 'EG_check'
HOST = '192.168.144.171'
Efuse_sleep_time = '500'
uplinkset_name = 'set1'
Efuse_Action = ['EFuseOn', 'EFuseOff']
Bay_No = ['5', '2', '3']
Server_No = '1'
Server_No_1 = '1'

IC_IP = '192.168.149.120'
ic_set_pf = 'enable'
ic_off_pf = 'disable'
uplink_interface = "Ethernet 1/0/1:1"
downlink_interface = "Ethernet 1/2/1"
switchport_interface = "Ten-GigabitEthernet1/0/39"
Potash_Credentials = {'username': 'root', 'password': 'UnoVista'}
Potash_Cred = ['root', 'UnoVista']
uplink_interface_1 = "Ethernet 1/0/2:1"
downlink_interface_1 = "Ethernet 1/1/6"
disable_command = "shutdown"
enable_command = "undo shutdown"
stacking_interface = "FortyGigE 0/0/7"
portType = 'Uplink'
firmware_warning = 'Unable to update firmware for the logical interconnect LE-LIG as an attempt was made to downgrade the firmware below the minimum supported version for the following constituent interconnects:CN77080KR1, interconnect 3'
LE_unsupported_alert = 'The interconnect firmware does not support the current configuration for: Pause Flood Protection. Please upgrade the firmware to 1.2.0 or later or remove the unsupported configuration.'
IC_ERROR = 'The interconnect is Unmanaged.'
IC_unmanaged_STATE = 'Unmanaged'
FW_ALERT = 'Interconnect firmware version is less than the required firmware version'
dump_file_path = ''
server_ip = '192.168.145.102'
li_disable = {"type": "EthernetInterconnectSettingsV5", "enablePauseFloodProtection": False}
li_enable = {"type": "EthernetInterconnectSettingsV5", "enablePauseFloodProtection": True}
Disable_Ports = [{"interconnectName": ICM_1, "portType": "Uplink", "portId": '', "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":False, "portName":"Q1:1", "portStatus":"Linked", "type":"portV5"},
                 ]
Enable_Ports = [{"interconnectName": ICM_1, "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled":True, "portName":"Q3", "portStatus":"Unknown", "type":"portV5"}]
interconnects_disable = [ENC1 + ', interconnect 2']
INTERCONNECTS = [ENC2 + ', interconnect 5']
INTERCONNECTS1 = [ENC1 + ', interconnect 2']
downlink_port_disable = [{"interconnectName": ICM_1, "portType": "Downlink", "portId": '', "portHealthStatus": "Normal", "capability": ["EnetFcoe", "Ethernet", "FibreChannel"], "configPortTypes":["EnetFcoe", "Ethernet"], "enabled": False, "portName": "d1", "portStatus": "Linked", "type": "portV5"}
                         ]
downlink_port_enable = [{"interconnectName": ICM_1, "portType": "Downlink", "portId": '', "enabled": True, "portName": "d1", "portStatus": "Linked", "type": "portV5"},
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

icmap_ME = [{'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
            {'bay': 5, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
            {'bay': 2, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
            {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
            ]

uplink_sets = {'us1': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'set2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net3'],
                       'nativeNetworkUri': 'Net3',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'},
                                                  ]},
               'us3': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['FCoENet_1602', 'Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'},
                                                  ]},
               'us4': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': []},
               'us5': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1', 'Net2'],
                       'nativeNetworkUri': 'Net_1',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'},
                                                  {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}
                                                  ]},
               }
redundancyType = 'HighlyAvailable'
ligs = {'LIG1':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'downlinkSpeedMode': 'SPEED_10GB',
                 'ethernetSettings': [{'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False}],
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig1':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'downlinkSpeedMode': 'SPEED_10GB',
                 'ethernetSettings': None,
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        'lig2':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'downlinkSpeedMode': 'SPEED_10GB',
                 'ethernetSettings': {
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
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
         'downlinkSpeedMode': 'SPEED_10GB',
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
         'snmpConfiguration': None},
        'lig4':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                 'downlinkSpeedMode': 'SPEED_10GB',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig5':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
                 'downlinkSpeedMode': 'SPEED_10GB',
         'ethernetSettings': [{'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False}],
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig6':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [],
                 'downlinkSpeedMode': 'SPEED_10GB',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig7':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us3'].copy()],
                 'downlinkSpeedMode': 'SPEED_10GB',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        'lig8':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us1'].copy()],
                 'downlinkSpeedMode': 'SPEED_10GB',
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
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us4'].copy()],
                 'downlinkSpeedMode': 'SPEED_10GB',
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
        'lig10':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap_ME,
         'enclosureIndexes': [1, 2],
         'interconnectBaySet': 2,
         'redundancyType': redundancyType,
         'uplinkSets': [uplink_sets['us5'].copy()],
                 'downlinkSpeedMode': 'SPEED_10GB',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV4', 'interconnectType': 'Ethernet', 'enablePauseFloodProtection': True, 'enableIgmpSnooping': False, 'igmpIdleTimeoutInterval': 260, 'enableFastMacCacheFailover': True, 'macRefreshInterval': 5, 'enableNetworkLoopProtection': True, 'enableTaggedLldp': False, 'enableRichTLV': False},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None, },
        }
enc_group_ME = {'name': 'EG1',
                'enclosureCount': 2,
                'interconnectBayMappings':
                [{'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIGname},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIGname},
                 ],
                'ipAddressingMode': 'DHCP',
                'ipRangeUris': [],
                'powerMode': 'RedundantPowerFeed'
                }
LE = [{'name': LE,
       'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],  # REAL
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False},
      ]

server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-c',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:Net2', 'mac': None, 'wwpn': None, 'wwnn': None}]}}]

server_profiles_old = [{'type': 'ServerProfileV8', 'serverHardwareUri': ENC2 + ', bay 6',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                        'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                        'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                        "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                        'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                                                                'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                               {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-c',
                                                                'requestedMbps': '2500', 'networkUri': 'ETH:Net2', 'mac': None, 'wwpn': None, 'wwnn': None}]}}]


server_profiles1 = [{'type': 'ServerProfileV10', 'name': 'Profile1', 'serverHardwareUri': ENC2 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': []}}
                    ]

server_profile_fcoe = [{'type': 'ServerProfileV10', 'name': 'Profile1', 'serverHardwareUri': ENC2 + ', bay 1',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                        'description': '', 'affinity': 'Bay',
                        'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                        'connectionSettings': {'connections': [
                            {'id': 4, 'name': '', 'functionType': 'FibreChannel', 'portId': 'Mezz 2:1-b',
                             'requestedMbps': '2500', 'networkUri': 'FCOE:FCoENet_1602', 'mac': None, 'wwpn': None, 'wwnn': None},
                            {'id': 5, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                                'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None}]}}
                       ]
server_profiles_2 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 6',
                      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                      'name': 'Profile2', 'description': '', 'affinity': 'Bay',
                      "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                                                              'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a',
                                                              'requestedMbps': '2500', 'networkUri': 'ETH:Net2', 'mac': None, 'wwpn': None, 'wwnn': None}]}}]
server_profiles_1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 1',
                      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                      'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                      "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                                                              'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                             {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a',
                                                              'requestedMbps': '2500', 'networkUri': 'ETH:Net2', 'mac': None, 'wwpn': None, 'wwnn': None}]}}]

server_profiles_LAG1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 1',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                         'connectionSettings': {'connections': [{'id': 1, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a',
                                                                 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                {'id': 2, 'name': '', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a',
                                                                 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}]}}]
iLo_1 = '192.168.149.212'
iLo_2 = '192.168.147.221'
ilo1_details = {'ilo_ip': iLo_1, 'username': 'Administrator', 'password': 'hpvse123'}
ilo2_details = {'ilo_ip': iLo_2, 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details = {'ilo_ip': iLo_1, 'username': 'Administrator', 'password': 'hpvse123'}

liupdate_body = {"sppUri": '',
                 "command": "UPDATE",
                 "force": True,
                 "ethernetActivationType": "Parallel",
                 "ethernetActivationDelay": "0",
                 "fcActivationType": "Parallel",
                 "fcActivationDelay": "0",
                 "validationType": "None"}
ip_1 = '195.168.140.108'
ip_2 = '195.168.140.118'
ip_3 = '195.168.140.161'
ip_4 = '195.168.140.103'

server1_details = {'windows_ip': ip_1, 'username': 'root', 'password': '12iso*help12345'}

server2_details = {'windows_ip': ip_2, 'username': 'root', 'password': '12iso*help12345'}

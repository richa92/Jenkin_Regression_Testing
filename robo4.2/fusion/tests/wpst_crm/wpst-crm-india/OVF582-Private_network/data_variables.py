import os
import sys
import paramiko
import os.path
import tarfile
import time
import re
from robot.libraries.BuiltIn import BuiltIn
from FusionLibrary.ui.business_logic.base import FusionUIBase
from FusionLibrary.ui.business_logic.base import SectionType
from RoboGalaxyLibrary.ui.common import ui_lib

cwd = os.getcwd()
download_to_path = cwd


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


def delete_file(file_path):
    file = os.remove('file_path')


def Remove_Whitespace(instring):
    return instring.strip()


def navigate():
    FusionUIBase.navigate_to_section(SectionType.INTERCONNECTS)
    selenium2lib = ui_lib.get_s2l()
    selenium2lib.reload_page()


APPLIANCE_IP = '192.168.144.171'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

different_user_admin = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
                        {'userName': 'Serveradmin', 'password': 'Serveradmin'},
                        {'userName': 'Storageadmin', 'password': 'Storageadmin'},
                        {'userName': 'Backupadmin', 'password': 'Backupadmin'}]


users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True}, {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True}, {'userName': 'Storageadmin', 'password': 'Storageadmin', 'fullName': 'Storageadmin', 'permissions': [{'roleName': 'Storage administrator', 'scopeUri': None}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True}, {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True}]

LIG_1 = 'LIG1'
LIG2 = 'LIG_2'
# ENC_1 = 'SGH714WYBW'
New_ENC_1 = '6HISEUIFY1'
ENC_2 = '6HISEUIFY1'
New_ENC_2 = 'TCAY635A5E'
# ENC_2 = 'SGH714WYBX'
ENC_1 = 'TCAY635A5E'
LE = 'LE'
iLo_1 = '192.168.149.27'
iLo_2 = '192.168.147.221'

# interconnectname_1 = 'SGH714WYBW, interconnect 2'
# interconnectname_2 = 'SGH714WYBX, interconnect 5'
# interconnectname_3 = 'SGH714WYBX, interconnect 2'
# interconnectname_4 = 'SGH714WYBW, interconnect 5'

# interconnectname_1 = '6HISEUIFY1, interconnect 2'
# interconnectname_2 = 'J4BFQUL7Y6, interconnect 5'
# interconnectname_3 = 'J4BFQUL7Y6, interconnect 2'
# interconnectname_4 = '6HISEUIFY1, interconnect 5'

interconnectname_1 = 'TCAY635A5E, interconnect 2'
interconnectname_2 = '6HISEUIFY1, interconnect 5'
interconnectname_3 = '6HISEUIFY1, interconnect 2'
interconnectname_4 = 'TCAY635A5E, interconnect 5'

IC_Configured = 'Configured'
IC_Maintenance = 'Maintenance'
IC_Unmanaged = 'Unmanaged'
host_ip1 = '195.168.140.127'
# host_ip = '192.168.148.96'
host_ip = '192.168.145.87'
pnet_true = True
pnet_false = False
admin_default_paswd = "admin"
factory_reset_sleep_time = "800"
BACKUPFILE_DIR = "C:\\OVF582_24_05\\fusion\\tests\\wpst_crm\\wpst-crm-india\\OVF582-API\\"
# Fw_old = 'cust-K120-32-Dev-Gen10.iso'
# Fw_new = 'cust-K120-36-EM2-DEV-G10.iso'
# Fw_latest = 'cust-K120-37-EM2-Dev-G10.iso'
Fw_old = 'Cust-K130-28-EM202-G10-prod.iso'
Fw_new = 'Cust-K130-29-EM202-G10-prod.iso'
Fw_latest = 'Cust-K130-30-EM202-G10-prod.iso'
Fw_unsupported = 'Cust-spp-EM2-k110-36-Gen10.iso'
Module_name = 'Virtual Connect SE 40Gb F8 Module for Synergy'
SPP_Uri = ''
localfile = ''
version_Check = ''
Switch_IP = '192.168.144.119'
EM_SN = ''
Network_edit_time = '140'
Port_edit_time = '80'
App_Upload_Sleep_Time = '4200'
LE_Update_Sleep_Time = '1500'
LI_Update_Sleep_Time = '900'
LE_Support_Dump_Time = '600'
Backup_Sleep_Time = '200'
Upload_Backup_Sleep_Time = '360'
Poweron_Server_Sleeptime = '600'
update_from_group_time = '300'
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Alert_Message_Network_page = 'Unrecognized JSON field.'
Alert_Message_uplinkset = 'Duplicate VLAN IDs are not allowed in this logical interconnect group.'
Alert_message_network = 'The VLAN ID must be between 1 and 4094, excluding internally reserved VLAN IDs 3967-4094.'
Alert_Message_LI = ''
Error_msg = 'Authorization error: User not authorized for this operation.'
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
get_interface = "ifconfig interface-name"
Ip_netmask = "ip netmask 255.255.255.0 up"
Set_ip = 'ip addr add ip-address'
Set_interface = 'dev interface-name'
interface_up = 'ip link set interface-name up'
Modify_bond = 'nmcli connection modify bond-bond-name'
Modify_ip = 'ip4 ip-address'
Modify_manual = 'netmask gw4 195.168.140.1 autoconnect yes ipv4.method manual'
Bond_1 = 'bond1'
Bond_2 = 'bond2'
Ip_bond_1 = '195.168.140.85'
Ip_bond_2 = '195.168.140.86'
Netmask = '24'
Space = ''
BACKUPFILE_DIR = ''
frame = 2
enc_list = ['ENC:' + ENC_1, 'ENC:' + ENC_2]
New_enc_list = ['ENC:' + New_ENC_1, 'ENC:' + New_ENC_2]
stacking_ports = ['Q7:1', 'Q8:1']
uplink_port_number = ['Q1:1', 'Q2:1']
downlink_port_number_1 = ['d6', 'd18']
downlink_port_number_2 = ['d13', 'd1']
Net_name = ['ENet_1', 'ENet_2']
stat = 'statistics'
Mode = 'FULL'
broad_range = '1-4'
Efuse_sleep_time = 400
power_on = 'On'
power_off = 'Off'
ip_1 = '195.168.140.108'
ip_2 = '195.168.140.118'
ip_3 = '195.168.140.161'
ip_4 = '195.168.140.103'
Untag_ip_1 = ''
Untag_ip_2 = ''
Tunnel_ip_1 = ''
Tunnel_ip_2 = ''
icm_ip = '192.168.146.237'
server_ip_address = ['195.168.140.22', '195.168.140.19']
Potash_Credentials = {'username': 'root', 'password': 'UnoVista'}
Potash_Cred = ['root', 'UnoVista']
uplink_interface = ['Ten-GigabitEthernet1/0/45', 'Ten-GigabitEthernet1/0/47', 'Ten-GigabitEthernet1/0/39', 'Ten-GigabitEthernet1/0/37']
downlink_interface = "TwentyGigE 0/1/3"

Enet = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Enet1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 101,
    'purpose': 'General',
    'name': 'Enet2',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 30,
    'purpose': 'General',
    'name': 'Enet2',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'}]

Enet_types = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Tag1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 20,
    'purpose': 'General',
    'name': 'Untag1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Untagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 30,
    'purpose': 'General',
    'name': 'Tunnel',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tunnel',
    'type': 'ethernet-networkV4'}]

Enet_vlan = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'lan_1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 10,
    'purpose': 'General',
    'name': 'lan_2',
    'smartLink': True,
    'privateNetwork': False,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'
}]

Untag_Tun = [{
    'vlanId': 0,
    'purpose': 'General',
    'name': 'Untagged',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Untagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 0,
    'purpose': 'General',
    'name': 'Tunnel',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tunnel',
    'type': 'ethernet-networkV4'}]

Enet_1 = [{
    'vlanId': 1601,
    'purpose': 'General',
    'name': 'Net_1',
    'smartLink': True,
    'privateNetwork': True,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 1,
    'purpose': 'General',
    'name': 'Net_2',
    'smartLink': True,
    'privateNetwork': True,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'}
]

Enet_default = [{
    'vlanId': 1601,
    'purpose': 'General',
    'name': 'Net_1',
    'smartLink': True,
    'privateNetwork': False,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 1,
    'purpose': 'General',
    'name': 'Net_2',
    'smartLink': True,
    'privateNetwork': False,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'
}]

Enet_private = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Net_1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 20,
    'purpose': 'General',
    'name': 'Net_2',
    'smartLink': True,
    'privateNetwork': True,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'
}]

Enet_oneonone = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Net_True',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 20,
    'purpose': 'General',
    'name': 'Net_False',
    'smartLink': True,
    'privateNetwork': False,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'
}]

Enet_4095 = {
    'vlanId': 4095,
    'purpose': 'General',
    'name': 'Net_1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'}

Enet_3000 = [{
    'vlanId': 3000,
    'purpose': 'General',
    'name': 'Vlan_3000',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 3400,
    'purpose': 'General',
    'name': 'Vlan_3400',
    'smartLink': True,
    'privateNetwork': True,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'
}]

Enet_1_2 = [{
    'vlanId': 1,
    'purpose': 'General',
    'name': 'Vlan_1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 2,
    'purpose': 'General',
    'name': 'Vlan_2',
    'smartLink': True,
    'privateNetwork': True,
    'ethernetNetworkType': 'Tagged',
    'connectionTemplateUri': None,
    'type': 'ethernet-networkV4'
}]

FC_net = [{'type': 'fc-networkV4',
           'linkStabilityTime': 30,
           'autoLoginRedistribution': False,
           'name': 'fc1_pnet',
           'connectionTemplateUri': None,
           'privateNetwork': True,
           'managedSanUri': None,
           'fabricType': 'FabricAttach'},
          {'type': 'fc-networkV4',
           'linkStabilityTime': 30,
           'autoLoginRedistribution': False,
           'name': 'fc1',
           'connectionTemplateUri': None,
           'managedSanUri': None,
           'fabricType': 'FabricAttach'}]


Fceo_net = [{'name': 'Fceo_pnet',
             'vlanId': 20,
             'connectionTemplateUri': None,
             'type': 'fcoe-networkV4',
             'privateNetwork': True},
            {'name': 'Fceo1',
             'vlanId': 20,
             'connectionTemplateUri': None,
             'type': 'fcoe-networkV4'}]

edit_conn_temp = [{
    'name': 'Net_1',
    'type': 'connection-template',
    'bandwidth': {'maximumBandwidth': '5000', 'typicalBandwidth': '3500'}},
    {
    'name': 'Net_2',
    'type': 'connection-template',
    'bandwidth': {'maximumBandwidth': '6000', 'typicalBandwidth': '4500'}}]

Enet_bulk = {'vlanIdRange': '1-8',
             'purpose': 'General',
             "namePrefix": 'NS_1',
             "smartLink": True,
             "privateNetwork": True,
             "bandwidth": {"maximumBandwidth": 8000, "typicalBandwidth": 2000},
             "type": "bulk-ethernet-networkV1",
             'initialScopeUris': []}

Enet_broad = [{
    'vlanId': 10,
    'purpose': 'General',
    'name': 'Enet_1',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 20,
    'purpose': 'General',
    'name': 'Enet_2',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 30,
    'purpose': 'General',
    'name': 'Enet_3',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'},
    {
    'vlanId': 40,
    'purpose': 'General',
    'name': 'Enet_4',
    'smartLink': True,
    'privateNetwork': True,
    'connectionTemplateUri': None,
    'ethernetNetworkType': 'Tagged',
    'type': 'ethernet-networkV4'}]


network_sets = {'name': 'netset1', 'type': 'network-setV4', 'networkUris': [''], 'nativeNetworkUri': None,
                'connectionTemplateUri': None}


Enc2MapBayset2 = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
]

Enc2MapBaysetA = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 2, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 5, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2}
]
Enc2MapBaysetB = [
    {'bay': 2, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 2, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
]

Enc1MapBayset1 = [
    {'bay': 2, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 5, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1}
]

Enc1MapBayset2 = [
    {'bay': 5, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 2, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}
]

uplink_sets = {'us': {'name': 'upset1',
                      'ethernetNetworkType': 'Tagged',
                      'networkType': 'Ethernet',
                      'networkUris': ['Net_1', 'Net_2'],
                      'nativeNetworkUri': 'Net_2',
                      'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]
                      },
               'us1': {'name': 'upset1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]
                       },
               'us1_1': {'name': 'upset1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['Net_1', 'Net_2'],
                         'nativeNetworkUri': None,
                         'logicalPortConfigInfos': []},
               'us1_2': {'name': 'upset1',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['Net_1', 'Net_2'],
                         'nativeNetworkUri': 'Net_1',
                         'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]
                         },
               'us2': {'name': 'upset1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_1'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': []},

               'us3': {'name': 'upset2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Net_2'],
                       'nativeNetworkUri': 'Net_2',
                       'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},

               'us4': {'name': 'upset4',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['lan_1', 'lan_2'],
                       'nativeNetworkUri': '',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us5': {'name': 'upset5',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': [''],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us6': {'name': 'upset6',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': [''],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '5', 'port': 'Q8', 'speed': 'Auto'}
                                                  ]},
               'us7': {'name': 'upset7',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Enet_1', 'Enet_3'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us8': {'name': 'upset8',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Enet_2', 'Enet_4'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us9': {'name': 'upset7',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['Vlan_3000', 'Vlan_3400'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us10': {'name': 'upset8',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': [],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us11': {'name': 'upset8',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['Enet_1', 'Enet_3'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'us12': {'name': 'upset8',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['Enet_2', 'Enet_4'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '1', 'bay': '2', 'port': 'Q2.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q1.1', 'speed': 'Auto'}, {'enclosure': '2', 'bay': '5', 'port': 'Q2.1', 'speed': 'Auto'}]},
               'up_tag': {'name': 'upset_untag',
                          'ethernetNetworkType': 'Untagged',
                          'networkType': 'Ethernet',
                          'networkUris': ['Untagged'],
                          'nativeNetworkUri': None,
                          'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Auto'},
                                                     {'enclosure': '2', 'bay': '5', 'port': 'Q1:1', 'speed': 'Auto'}
                                                     ]},
               'up_tun': {'name': 'upset_tunnel',
                          'ethernetNetworkType': 'Tunnel',
                          'networkType': 'Ethernet',
                          'networkUris': ['Tunnel'],
                          'nativeNetworkUri': None,
                          'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q2:1', 'speed': 'Auto'},
                                                     {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Auto'}
                                                     ]},
               'up_A': {'name': 'upset_Aside',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['Net_1'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '2', 'port': 'Q1:1', 'speed': 'Auto'},
                                                   {'enclosure': '1', 'bay': '2', 'port': 'Q2:1', 'speed': 'Auto'},
                                                   {'enclosure': '1', 'bay': '5', 'port': 'Q1:1', 'speed': 'Auto'},
                                                   {'enclosure': '1', 'bay': '5', 'port': 'Q2:1', 'speed': 'Auto'}
                                                   ]},
               'up_B': {'name': 'upset_Bside',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['Net_1'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '2', 'port': 'Q1:1', 'speed': 'Auto'},
                                                   {'enclosure': '2', 'bay': '2', 'port': 'Q2:1', 'speed': 'Auto'},
                                                   {'enclosure': '2', 'bay': '5', 'port': 'Q1:1', 'speed': 'Auto'},
                                                   {'enclosure': '2', 'bay': '5', 'port': 'Q2:1', 'speed': 'Auto'}
                                                   ]}}
Edit_uplink = {
    "type": "uplink-setV4",
    "primaryPortLocation": None,
    "nativeNetworkUri": None,
    "networkUris": [],
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "reachability": None,
    # "fcMode": null,
    "logicalInterconnectUri": " ",
    "manualLoginRedistributionState": "NotSupported",
    "connectionMode": "Auto",
    "portConfigInfos": [],
    "lacpTimer": "Short",
    "networkType": "Ethernet",
    "ethernetNetworkType": "Tagged",
    "description": None,
    "name": "upset1",
    "state": "Unknown",
    "status": "Unknown",
    "category": "logical-interconnects",
    "created": None,
    "modified": None,
    "eTag": None,
    "uri": " "
}

Edit_uplink_Net = {
    "type": "uplink-setV4",
    "primaryPortLocation": None,
    "nativeNetworkUri": None,
    "networkUris": [],
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "reachability": None,
    # "fcMode": null,
    "logicalInterconnectUri": " ",
    "manualLoginRedistributionState": "NotSupported",
    "connectionMode": "Auto",
    "portConfigInfos": [],
    "lacpTimer": "Short",
    "networkType": "Ethernet",
    "ethernetNetworkType": "Tagged",
    "description": None,
    "name": "us1",
    "state": "Unknown",
    "status": "Unknown",
    "category": "logical-interconnects",
    "uri": " "
}
Edit_uplink_NativeNet = {
    "type": "uplink-setV4",
    "primaryPortLocation": None,
    "nativeNetworkUri": None,
    "networkUris": [],
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "reachability": None,
    # "fcMode": null,
    "logicalInterconnectUri": " ",
    "manualLoginRedistributionState": "NotSupported",
    "connectionMode": "Auto",
    "portConfigInfos": [],
    "lacpTimer": "Short",
    "networkType": "Ethernet",
    "ethernetNetworkType": "Tagged",
    "description": None,
    "name": "us1",
    "state": "Unknown",
    "status": "Unknown",
    "category": "logical-interconnects",
    "uri": " "
}

LIGS_TB = {'ligsup': [{'name': 'LIG1',
                       'type': 'logical-interconnect-groupV5',
                       'enclosureType': 'SY12000',
                       'interconnectMapTemplate': Enc2MapBayset2,
                       'enclosureIndexes': [1, 2],
                       'interconnectBaySet': 2,
                       'redundancyType': 'HighlyAvailable',
                       'uplinkSets': [uplink_sets['us'].copy()],
                       'internalNetworkUris':[],
                       'ethernetSettings': None,
                       'state': 'Active',
                       'telemetryConfiguration': None,
                       'snmpConfiguration': None}],

           'ligsup_exthost': [{'name': 'LIG1',
                               'type': 'logical-interconnect-groupV5',
                               'enclosureType': 'SY12000',
                               'interconnectMapTemplate': Enc2MapBayset2,
                               'enclosureIndexes': [1, 2],
                               'interconnectBaySet': 2,
                               'redundancyType': 'HighlyAvailable',
                               'uplinkSets': [uplink_sets['us1_2'].copy()],
                               'internalNetworkUris':[],
                               'ethernetSettings': None,
                               'state': 'Active',
                               'telemetryConfiguration': None,
                               'snmpConfiguration': None}],

           'ligsup_re': [{'name': 'LIG1',
                          'type': 'logical-interconnect-groupV5',
                          'enclosureType': 'SY12000',
                          'interconnectMapTemplate': Enc2MapBayset2,
                          'enclosureIndexes': [1, 2],
                          'interconnectBaySet': 2,
                          'redundancyType': 'HighlyAvailable',
                          'uplinkSets': [uplink_sets['us1_1'].copy()],
                          'internalnetworksUris':[],
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None}],

           'ligsint': [{'name': 'LIG2',
                        'type': 'logical-interconnect-groupV5',
                        'enclosureType': 'SY12000',
                        'interconnectMapTemplate': Enc2MapBayset2,
                        'enclosureIndexes': [1, 2],
                        'interconnectBaySet': 2,
                        'redundancyType': 'HighlyAvailable',
                        'uplinkSets': [],
                        # 'uplinkSets': [uplink_sets['us2'].copy()],
                        'internalNetworkUris': [],
                        'ethernetSettings': None,
                        'state': None,
                        'telemetryConfiguration': None,
                        'snmpConfiguration': None}
                       ],
           'ligsup_1': [{'name': 'LIG1',
                         'type': 'logical-interconnect-groupV5',
                         'enclosureType': 'SY12000',
                         'interconnectMapTemplate': Enc2MapBayset2,
                         'enclosureIndexes': [1, 2],
                         'interconnectBaySet': 2,
                         'redundancyType': 'HighlyAvailable',
                         'uplinkSets': [uplink_sets['us3'].copy()],
                         'internalNetworkUris':[],
                         'ethernetSettings': None,
                         'state': None,
                         'telemetryConfiguration': None,
                         'snmpConfiguration': None}
                        ],
           'ligsup_2': [{'name': 'LIG1',
                         'type': 'logical-interconnect-groupV5',
                         'enclosureType': 'SY12000',
                         'interconnectMapTemplate': Enc2MapBayset2,
                         'enclosureIndexes': [1, 2],
                         'interconnectBaySet': 2,
                         'redundancyType': 'HighlyAvailable',
                         'uplinkSets': [uplink_sets['us2'].copy(), uplink_sets['us3'].copy()],
                         'internalNetworkUris':[],
                         'ethernetSettings': None,
                         'state': None,
                         'telemetryConfiguration': None,
                         'snmpConfiguration': None}
                        ],
           'ligsup_vlan': [{'name': 'LIG1',
                            'type': 'logical-interconnect-groupV5',
                            'enclosureType': 'SY12000',
                            'interconnectMapTemplate': Enc2MapBayset2,
                            'enclosureIndexes': [1, 2],
                            'interconnectBaySet': 2,
                            'redundancyType': 'HighlyAvailable',
                            'uplinkSets': [uplink_sets['us4'].copy()],
                            'ethernetSettings': None,
                            'state': 'Active',
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None}],
           'ligsup_Le': [{'name': 'LIG1',
                          'type': 'logical-interconnect-groupV4',
                          'enclosureType': 'SY12000',
                          'interconnectMapTemplate': Enc2MapBayset2,
                          'enclosureIndexes': [1, 2],
                          'interconnectBaySet': 2,
                          'redundancyType': 'HighlyAvailable',
                          'uplinkSets': [uplink_sets['us4'].copy()],
                          'internalNetworkUris':[],
                          'ethernetSettings': None,
                          'state': 'Active',
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None}
                         ],
           'ligsup_broad': [{'name': 'LIG1',
                             'type': 'logical-interconnect-groupV4',
                             'enclosureType': 'SY12000',
                             'interconnectMapTemplate': Enc2MapBayset2,
                             'enclosureIndexes': [1, 2],
                             'interconnectBaySet': 2,
                             'redundancyType': 'HighlyAvailable',
                             'uplinkSets': [uplink_sets['us7'].copy(), uplink_sets['us8'].copy()],
                             'internalNetworkUris':[],
                             'ethernetSettings': None,
                             'state': None,
                             'telemetryConfiguration': None,
                             'snmpConfiguration': None}
                            ],
           'ligsup_potash': [{'name': 'LIG1',
                              'type': 'logical-interconnect-groupV4',
                              'enclosureType': 'SY12000',
                              'interconnectMapTemplate': Enc2MapBayset2,
                              'enclosureIndexes': [1, 2],
                              'interconnectBaySet': 2,
                              'redundancyType': 'HighlyAvailable',
                              'uplinkSets': [uplink_sets['us9'].copy(), uplink_sets['us10'].copy()],
                              'internalNetworkUris':[],
                              'ethernetSettings': None,
                              'state': None,
                              'telemetryConfiguration': None,
                              'snmpConfiguration': None}
                             ],
           'ligsup_mlag': [{'name': 'LIG1',
                            'type': 'logical-interconnect-groupV4',
                            'enclosureType': 'SY12000',
                            'interconnectMapTemplate': Enc2MapBayset2,
                            'enclosureIndexes': [1, 2],
                            'interconnectBaySet': 2,
                            'redundancyType': 'HighlyAvailable',
                            'uplinkSets': [uplink_sets['us11'].copy(), uplink_sets['us12'].copy()],
                            'internalNetworkUris':[],
                            'ethernetSettings': None,
                            'state': None,
                            'telemetryConfiguration': None,
                            'snmpConfiguration': None}
                           ],
           'ligsup_Untag': [{'name': 'LIG1',
                             'type': 'logical-interconnect-groupV5',
                             'enclosureType': 'SY12000',
                             'interconnectMapTemplate': Enc2MapBayset2,
                             'enclosureIndexes': [1, 2],
                             'interconnectBaySet': 2,
                             'redundancyType': 'HighlyAvailable',
                             'uplinkSets': [uplink_sets['up_tag'].copy()],
                             'internalNetworkUris':[],
                             'ethernetSettings': None,
                             'state': None,
                             'telemetryConfiguration': None,
                             'snmpConfiguration': None}
                            ],

           'ligsup_Tun': [{'name': 'LIG1',
                           'type': 'logical-interconnect-groupV5',
                           'enclosureType': 'SY12000',
                           'interconnectMapTemplate': Enc2MapBayset2,
                           'enclosureIndexes': [1, 2],
                           'interconnectBaySet': 2,
                           'redundancyType': 'HighlyAvailable',
                           'uplinkSets': [uplink_sets['up_tun'].copy()],
                           'internalNetworkUris':[],
                           'ethernetSettings': None,
                           'state': None,
                           'telemetryConfiguration': None,
                           'snmpConfiguration': None}
                          ],
           'ligsup_AB': [{'name': 'LIG1',
                          'type': 'logical-interconnect-groupV4',
                          'enclosureType': 'SY12000',
                          'interconnectMapTemplate': Enc2MapBayset2,
                          'enclosureIndexes': [1, 2],
                          'interconnectBaySet': 2,
                          'redundancyType': 'NonRedundantASide',
                          'uplinkSets': [uplink_sets['us1'].copy()],
                          'internalNetworkUris':[],
                          'ethernetSettings': None,
                          'state': None,
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None},
                         {'name': 'LIG_2',
                          'type': 'logical-interconnect-groupV4',
                          'enclosureType': 'SY12000',
                          'interconnectMapTemplate': Enc2MapBayset2,
                          'enclosureIndexes': [1, 2],
                          'interconnectBaySet': 2,
                          'redundancyType': 'NonRedundantBSide',
                          'uplinkSets': [uplink_sets['us1'].copy()],
                          'internalNetworkUris':[],
                          'ethernetSettings': None,
                          'state': None,
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None}],
           'ligsup_HA': [{'name': 'LIG1',
                          'type': 'logical-interconnect-groupV5',
                          'enclosureType': 'SY12000',
                          'interconnectMapTemplate': Enc2MapBayset2,
                          'enclosureIndexes': [1, 2],
                          'interconnectBaySet': 2,
                          'redundancyType': 'HighlyAvailable',
                          'uplinkSets': [uplink_sets['us1'].copy()],
                          'internalNetworkUris':[],
                          'ethernetSettings': None,
                          'state': None,
                          'telemetryConfiguration': None,
                          'snmpConfiguration': None}],
           'ligsup_A': [{'name': 'LIG1',
                         'type': 'logical-interconnect-groupV4',
                         'enclosureType': 'SY12000',
                         'interconnectMapTemplate': Enc2MapBaysetA,
                         'enclosureIndexes': [1, 2],
                         'interconnectBaySet': 2,
                         'redundancyType': 'Redundant',
                         'uplinkSets': [uplink_sets['up_A'].copy()],
                         'internalNetworkUris':[],
                         'ethernetSettings': None,
                         'state': None,
                         'telemetryConfiguration': None,
                         'snmpConfiguration': None}],
           'ligsup_B': [{'name': 'LIG1',
                         'type': 'logical-interconnect-groupV4',
                         'enclosureType': 'SY12000',
                         'interconnectMapTemplate': Enc2MapBaysetB,
                         'enclosureIndexes': [1, 2],
                         'interconnectBaySet': 2,
                         'redundancyType': 'Redundant',
                         'uplinkSets': [uplink_sets['up_B'].copy()],
                         'internalNetworkUris':[],
                         'ethernetSettings': None,
                         'state': None,
                         'telemetryConfiguration': None,
                         'snmpConfiguration': None}]}


Enc_group = {'name': 'EG1',
             'configurationScript': None,
             'powerMode': 'RedundantPowerFeed',
             'ipAddressingMode': 'DHCP',
             'ipRangeUris': [],
             'enclosureCount': frame,
             'osDeploymentSettings': {'manageOSDeployment': False, 'deploymentModeSettings': {'deploymentMode': 'None', 'deploymentNetworkUri': None}},
             'interconnectBayMappings':
             [{'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'}
              ]}


Logical_Enclosure = [{'name': LE,
                      'enclosureUris': enc_list[0:frame],  # REAL
                      'enclosureGroupUri': 'EG:EG1',
                      'firmwareBaselineUri': None,
                      'forceInstallFirmware': False}]
New_Logical_Enclosure = [{'name': LE,
                          'enclosureUris': New_enc_list[0:frame],  # REAL
                          'enclosureGroupUri': 'EG:EG1',
                          'firmwareBaselineUri': None,
                          'forceInstallFirmware': False}]

server_profile_1 = [{'type': 'ServerProfileV9',
                     'serverHardwareUri': ENC_1 + ', bay 6',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_1,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'Profile1',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}, {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]


server_profile1_1 = [{'type': 'ServerProfileV9',
                      'serverHardwareUri': ENC_1 + ', bay 6',
                      'serverHardwareTypeUri': '',
                      'enclosureUri': 'ENC:' + ENC_1,
                      'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual',
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'macType': 'Virtual',
                      'wwnType': 'Virtual',
                      'name': 'Profile1',
                      'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}, {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                      'boot': {'manageBoot': False},
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]


server_profile_2 = [{'type': 'ServerProfileV9',
                     'serverHardwareUri': ENC_2 + ', bay 1',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_2,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'Profile2',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}, {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profiles_1 = [{'type': 'ServerProfileV8',
                      'serverHardwareUri': ENC_2 + ', bay 1',
                      'serverHardwareTypeUri': '',
                      'enclosureUri': 'ENC:' + ENC_2,
                      'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual',
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'macType': 'Virtual',
                      'wwnType': 'Virtual',
                      'name': 'pro3',
                      'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                      'boot': {'manageBoot': False},
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None},
                     {'type': 'ServerProfileV8',
                      'serverHardwareUri': ENC_2 + ', bay 1',
                      'serverHardwareTypeUri': '',
                      'enclosureUri': 'ENC:' + ENC_2,
                      'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual',
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'macType': 'Virtual',
                      'wwnType': 'Virtual',
                      'name': 'pro3',
                      'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                      'boot': {'manageBoot': False},
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}
                     ]

server_profiles_2 = [{'type': 'ServerProfileV8',
                      'serverHardwareUri': ENC_2 + ', bay 1',
                      'serverHardwareTypeUri': '',
                      'enclosureUri': 'ENC:' + ENC_2,
                      'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual',
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'macType': 'Virtual',
                      'wwnType': 'Virtual',
                      'name': 'pro3',
                      'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                      'boot': {'manageBoot': False},
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None},
                     {'type': 'ServerProfileV8',
                      'serverHardwareUri': ENC_2 + ', bay 1',
                      'serverHardwareTypeUri': '',
                      'enclosureUri': 'ENC:' + ENC_2,
                      'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual',
                      'iscsiInitiatorNameType': 'AutoGenerated',
                      'macType': 'Virtual',
                      'wwnType': 'Virtual',
                      'name': 'pro3',
                      'description': '', 'affinity': 'Bay',
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                      'boot': {'manageBoot': False},
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                      'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                      'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}
                     ]

Lag_server_profile = [{'type': 'ServerProfileV8',
                       'serverHardwareUri': ENC_2 + ', bay 1',
                       'serverHardwareTypeUri': '',
                       'enclosureUri': 'ENC:' + ENC_2,
                       'enclosureGroupUri': 'EG:EG1',
                       'serialNumberType': 'Virtual',
                       'iscsiInitiatorNameType': 'AutoGenerated',
                       'macType': 'Virtual',
                       'wwnType': 'Virtual',
                       'name': 'pro3',
                       'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                       'boot': {'manageBoot': False},
                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                       'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None},
                      {'type': 'ServerProfileV8',
                       'serverHardwareUri': ENC_2 + ', bay 1',
                       'serverHardwareTypeUri': '',
                       'enclosureUri': 'ENC:' + ENC_2,
                       'enclosureGroupUri': 'EG:EG1',
                       'serialNumberType': 'Virtual',
                       'iscsiInitiatorNameType': 'AutoGenerated',
                       'macType': 'Virtual',
                       'wwnType': 'Virtual',
                       'name': 'pro3',
                       'description': '', 'affinity': 'Bay',
                       'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                       'boot': {'manageBoot': False},
                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                       'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                       'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}
                      ]

server_profileA1 = [{'type': 'ServerProfileV8',
                     'serverHardwareUri': ENC_1 + ', bay 6',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_1,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'Profile1',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileA2 = [{'type': 'ServerProfileV8',
                     'serverHardwareUri': ENC_2 + ', bay 1',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_2,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'Profile2',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileA1_Lag = [{'type': 'ServerProfileV8',
                         'serverHardwareUri': ENC_1 + ', bay 6',
                         'serverHardwareTypeUri': '',
                         'enclosureUri': 'ENC:' + ENC_1,
                         'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual',
                         'iscsiInitiatorNameType': 'AutoGenerated',
                         'macType': 'Virtual',
                         'wwnType': 'Virtual',
                         'name': 'Profile1',
                         'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}},
                                                                {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                         'boot': {'manageBoot': False},
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                         'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileA2_lag = [{'type': 'ServerProfileV8',
                         'serverHardwareUri': ENC_2 + ', bay 1',
                         'serverHardwareTypeUri': '',
                         'enclosureUri': 'ENC:' + ENC_2,
                         'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual',
                         'iscsiInitiatorNameType': 'AutoGenerated',
                         'macType': 'Virtual',
                         'wwnType': 'Virtual',
                         'name': 'Profile2',
                         'description': '', 'affinity': 'Bay',
                         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}},
                                                                {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                         'boot': {'manageBoot': False},
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                         'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileA2_Edit = [{'type': 'ServerProfileV8',
                          'serverHardwareUri': ENC_2 + ', bay 1',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC_2,
                          'enclosureGroupUri': 'EG:EG1',
                          'serialNumberType': 'Virtual',
                          'iscsiInitiatorNameType': 'AutoGenerated',
                          'macType': 'Virtual',
                          'wwnType': 'Virtual',
                          'name': 'Profile2',
                          'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                          'boot': {'manageBoot': False},
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                          'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileB1 = [{'type': 'ServerProfileV8',
                     'serverHardwareUri': ENC_1 + ', bay 6',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_1,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'Profile1',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileB2 = [{'type': 'ServerProfileV8',
                     'serverHardwareUri': ENC_2 + ', bay 1',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_2,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'Profile2',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profileB3 = [{'type': 'ServerProfileV8',
                     'serverHardwareUri': ENC_2 + ', bay 1',
                     'serverHardwareTypeUri': '',
                     'enclosureUri': 'ENC:' + ENC_2,
                     'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual',
                     'iscsiInitiatorNameType': 'AutoGenerated',
                     'macType': 'Virtual',
                     'wwnType': 'Virtual',
                     'name': 'pro3',
                     'description': '', 'affinity': 'Bay',
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                     'boot': {'manageBoot': False},
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                     'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_Untag_1 = [{'type': 'ServerProfileV9',
                           'serverHardwareUri': ENC_1 + ', bay 6',
                           'serverHardwareTypeUri': '',
                           'enclosureUri': 'ENC:' + ENC_1,
                           'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual',
                           'iscsiInitiatorNameType': 'AutoGenerated',
                           'macType': 'Virtual',
                           'wwnType': 'Virtual',
                           'name': 'Profile1',
                           'description': '', 'affinity': 'Bay',
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                           'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]
server_profile_Untag_2 = [{'type': 'ServerProfileV9',
                           'serverHardwareUri': ENC_2 + ', bay 1',
                           'serverHardwareTypeUri': '',
                           'enclosureUri': 'ENC:' + ENC_2,
                           'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual',
                           'iscsiInitiatorNameType': 'AutoGenerated',
                           'macType': 'Virtual',
                           'wwnType': 'Virtual',
                           'name': 'Profile2',
                           'description': '', 'affinity': 'Bay',
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Untagged', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                           'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_Tunnel_1 = [{'type': 'ServerProfileV9',
                            'serverHardwareUri': ENC_1 + ', bay 6',
                            'serverHardwareTypeUri': '',
                            'enclosureUri': 'ENC:' + ENC_1,
                            'enclosureGroupUri': 'EG:EG1',
                            'serialNumberType': 'Virtual',
                            'iscsiInitiatorNameType': 'AutoGenerated',
                            'macType': 'Virtual',
                            'wwnType': 'Virtual',
                            'name': 'Profile1',
                            'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                            'boot': {'manageBoot': False},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                            'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]
server_profile_Tunnel_2 = [{'type': 'ServerProfileV9',
                            'serverHardwareUri': ENC_2 + ', bay 1',
                            'serverHardwareTypeUri': '',
                            'enclosureUri': 'ENC:' + ENC_2,
                            'enclosureGroupUri': 'EG:EG1',
                            'serialNumberType': 'Virtual',
                            'iscsiInitiatorNameType': 'AutoGenerated',
                            'macType': 'Virtual',
                            'wwnType': 'Virtual',
                            'name': 'Profile2',
                            'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                            'boot': {'manageBoot': False},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                            'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA1_Dphy = [{'type': 'ServerProfileV9',
                            'serverHardwareUri': ENC_1 + ', bay 6',
                            'serverHardwareTypeUri': '',
                            'enclosureUri': 'ENC:' + ENC_1,
                            'enclosureGroupUri': 'EG:EG1',
                            'serialNumberType': 'Virtual',
                            'iscsiInitiatorNameType': 'AutoGenerated',
                            'macType': 'Virtual',
                            'wwnType': 'Virtual',
                            'name': 'Profile1',
                            'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}
                                                                   ]},
                            'boot': {'manageBoot': False},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                            'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA2_Dphy = [{'type': 'ServerProfileV9',
                            'serverHardwareUri': ENC_2 + ', bay 1',
                            'serverHardwareTypeUri': '',
                            'enclosureUri': 'ENC:' + ENC_2,
                            'enclosureGroupUri': 'EG:EG1',
                            'serialNumberType': 'Virtual',
                            'iscsiInitiatorNameType': 'AutoGenerated',
                            'macType': 'Virtual',
                            'wwnType': 'Virtual',
                            'name': 'Profile2',
                            'description': '', 'affinity': 'Bay',
                            'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                            'boot': {'manageBoot': False},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                            'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                            'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA1_OP = [{'type': 'ServerProfileV9',
                          'serverHardwareUri': ENC_1 + ', bay 6',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC_1,
                          'enclosureGroupUri': 'EG:EG1',
                          'serialNumberType': 'Virtual',
                          'iscsiInitiatorNameType': 'AutoGenerated',
                          'macType': 'Virtual',
                          'wwnType': 'Virtual',
                          'name': 'Profile1',
                          'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-c', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}
                                                                 ]},
                          'boot': {'manageBoot': False},
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                          'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA2_OP = [{'type': 'ServerProfileV9',
                          'serverHardwareUri': ENC_2 + ', bay 1',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC_2,
                          'enclosureGroupUri': 'EG:EG1',
                          'serialNumberType': 'Virtual',
                          'iscsiInitiatorNameType': 'AutoGenerated',
                          'macType': 'Virtual',
                          'wwnType': 'Virtual',
                          'name': 'Profile2',
                          'description': '', 'affinity': 'Bay',
                          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                          'boot': {'manageBoot': False},
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                          'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]


server_profile_HA1_lag = [{'type': 'ServerProfileV9',
                           'serverHardwareUri': ENC_1 + ', bay 6',
                           'serverHardwareTypeUri': '',
                           'enclosureUri': 'ENC:' + ENC_1,
                           'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual',
                           'iscsiInitiatorNameType': 'AutoGenerated',
                           'macType': 'Virtual',
                           'wwnType': 'Virtual',
                           'name': 'Profile1',
                           'description': '', 'affinity': 'Bay',
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-a', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                           'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA2_lag = [{'type': 'ServerProfileV9',
                           'serverHardwareUri': ENC_2 + ', bay 1',
                           'serverHardwareTypeUri': '',
                           'enclosureUri': 'ENC:' + ENC_2,
                           'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual',
                           'iscsiInitiatorNameType': 'AutoGenerated',
                           'macType': 'Virtual',
                           'wwnType': 'Virtual',
                           'name': 'Profile2',
                           'description': '', 'affinity': 'Bay',
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                           'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA3_lag = [{'type': 'ServerProfileV9',
                           'serverHardwareUri': ENC_1 + ', bay 6',
                           'serverHardwareTypeUri': '',
                           'enclosureUri': 'ENC:' + ENC_1,
                           'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual',
                           'iscsiInitiatorNameType': 'AutoGenerated',
                           'macType': 'Virtual',
                           'wwnType': 'Virtual',
                           'name': 'Profile1',
                           'description': '', 'affinity': 'Bay',
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                           'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

server_profile_HA4_lag = [{'type': 'ServerProfileV9',
                           'serverHardwareUri': ENC_2 + ', bay 1',
                           'serverHardwareTypeUri': '',
                           'enclosureUri': 'ENC:' + ENC_2,
                           'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual',
                           'iscsiInitiatorNameType': 'AutoGenerated',
                           'macType': 'Virtual',
                           'wwnType': 'Virtual',
                           'name': 'Profile2',
                           'description': '', 'affinity': 'Bay',
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 2:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 2:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Net_1', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None, 'requestedVFs': '0', 'ipv4': {}}]},
                           'boot': {'manageBoot': False},
                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                           'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': '', 'firmwareActivationType': 'Immediate'},
                           'bios': {'manageBios': False, 'overriddenSettings': []}, 'hideUnusedFlexNics':True, 'iscsiInitiatorName':'', 'osDeploymentSettings':None, 'localStorage':{'sasLogicalJBODs': [], 'controllers':[]}, 'sanStorage':None}]

LE_SupportDump_Payload = {"encrypt": True, "errorCode": "MyDump16", "excludeApplianceDump": False}

warmboot_firmware = {"sppUri": '',
                     "command": "UPDATE",
                     "force": True,
                     "ethernetActivationType": "PairProtect",
                     "ethernetActivationDelay": "0",
                     "fcActivationType": "PairProtect",
                     "fcActivationDelay": "0",
                     "validationType": "ValidateBestEffort"}

firmware_li_upgrade = {"sppUri": '',
                       "command": "UPDATE",
                       "force": True,
                       "ethernetActivationType": "Parallel",
                       "ethernetActivationDelay": "0",
                       "fcActivationType": "Parallel",
                       "fcActivationDelay": "0",
                       "validationType": "None"}

firmware_li_downgrade = {"sppUri": '',
                         "command": "UPDATE",
                         "force": True,
                         "ethernetActivationType": "Parallel",
                         "ethernetActivationDelay": "0",
                         "fcActivationType": "Parallel",
                         "fcActivationDelay": "0",
                         "validationType": "None"}

le_spp_downgrade = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/downgrade",
                    "firmwareUpdateOn": "SharedInfrastructureOnly",
                    "logicalInterconnectUpdateMode": "Parallel",
                    "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                    "updateFirmwareOnUnmanagedInterconnect": True}

ilo1_details = {'ilo_ip': iLo_1, 'username': 'Administrator', 'password': 'hpvse123'}
ilo2_details = {'ilo_ip': iLo_2, 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details = {'ilo_ip': iLo_1, 'username': 'Administrator', 'password': 'hpvse123'}


server1_details = {'windows_ip': ip_1, 'username': 'root', 'password': '12iso*help12345'}

server2_details = {'windows_ip': ip_2, 'username': 'root', 'password': '12iso*help12345'}

server_details = {'windows_ip': '', 'username': 'root', 'password': '12iso*help12345'}

Untag_server_1 = {'windows_ip': '', 'username': 'Administrator', 'password': '12iso*help'}

Untag_server_2 = {'windows_ip': '', 'username': 'Administrator', 'password': '12iso*help'}

Tunnel_server_1 = {'windows_ip': '', 'username': 'Administrator', 'password': '12iso*help'}

Tunnel_server_2 = {'windows_ip': '', 'username': 'Administrator', 'password': '12iso*help'}

switch_details = {'switch_ip': Switch_IP, 'username': 'admin', 'password': 'welcome123'}

server_1 = {'windows_ip': '', 'username': 'Administrator', 'password': '12iso*help'}

server_2 = {'windows_ip': '', 'username': 'Administrator', 'password': '12iso*help'}

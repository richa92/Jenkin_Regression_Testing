def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist

SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password


FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

SWITCH_USERNAME = 'admin'
SWITCH_PASSWORD = 'wpsthpvse1'
SWITCH_PROMPT = '>'
SWITCH_TIMEOUT = 300

IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN 106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'portmon.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}
out_file = "11-05-2016-0941_output.txt"
volume_size = '50'
linux_details = {"hostip": "15.199.235.170", "username": "root", "password": "hpvse123", "dir_location": "/root/",
                 "python_cmd": "python2.7"}
ilo_details = [{'ilo_ip': '15.245.132.91', 'username': 'Administrator', 'password': 'compaq'}, {'ilo_ip': '15.245.132.50', 'username': 'Administrator', 'password': 'compaq'}, {'ilo_ip': '15.245.132.86', 'username': 'Administrator', 'password': 'compaq'}, {'ilo_ip': '15.245.132.72', 'username': 'Administrator', 'password': 'compaq'}]
san_switch_details = {'ip': '15.245.128.124', 'username': 'admin', 'password': 'wpsthpvse1'}
server_ip_static = ['10.11.1.2', '10.11.1.3', '10.11.1.4', '10.11.1.5']
os_type = ['linux', 'windows', 'linux', 'wondows']
switch_cmd = ['switchshow', 'portshow']
port_list = {'npiv_port': ['2', '3', '12', '13'], 'npiv_final': ['2', '12'], 'port_number': ['26', '12', '13', '14'],
             'expected_speed': ['N8Gbps', 'N8Gbps', 'N8Gbps', 'N8Gbps']}
port_speed = ['N8Gbps']
switch_port_speed = {'26': 'N2Gbps', '12': 'N2Gbps', '13': 'N4Gbps', '14': 'N8Gbps'}
login_dist = ['1 N Port + 1 NPIV public', '1 N Port + 2 NPIV public']
dd_cmd = 'dd if=\/dev\/zero of=lun_disk bs=1024 count=1048'
bay_port_detail = {'CN7545061V, interconnect 3': ['Q2:2', 'Q2:3'], 'CN7545085D, interconnect 6': ['Q2:2', 'Q2:3']}
login_initial_output = {'3.Q2:2': 1, '3.Q2:3': 1, '6.Q2:2': 1, '6.Q2:3': 1}
login_final_output = {'3.Q2:2': 2, '3.Q2:3': 0, '6.Q2:2': 2, '6.Q2:3': 0}
interconnect_ports_to_disable = [5.2, 6.1]
server_details1 = [{'linux_ip': '', 'username': 'root', 'password': 'hpvse1'}, {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse1'}]
BFS_server_details = {'username': 'Administrator', 'password': 'Compaq123'}
diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\Write_to_lun.ps1"
list_disk_cmd = "PowerShell.exe -ExecutionPolicy Bypass -File .\\list_disk.ps1"
GetVolume_cmd = "PowerShell.exe -ExecutionPolicy Bypass -File .\\GetVolume.ps1"
lsscsi_cmd = "lsscsi | grep VV"
diskspd_cmd_60s_failover1 = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s_failover1.ps1"
diskspd_cmd_5m = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-5m.ps1"
diskspd_cmd_10m = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-10m.ps1"
diskspd_cmd_20m = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-20m.ps1"
diskspd_cmd_1hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-1hr.ps1"
diskspd_cmd_2hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-2hr.ps1"
diskspd_cmd_4hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-4hr.ps1"
diskspd_cmd_6hr = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-6hr.ps1"

########################################

true = True
false = False

########################################
"""
default_variables = {'admin_credentials': admin_credentials,
                     'appliance': appliance,
                     'encs': encs,
                     'enc_groups': enc_groups,
                     'ethernet_networks': ethernet_networks,
                     'ethernet_ranges': ethernet_ranges,
                     'fc_networks': fc_networks,
                     'fcoe_networks': fcoe_networks,
                     'fcoe_ranges': fcoe_ranges,
                     'les': les,
                     'licenses': licenses,
                     'ligs': ligs,
                     'network_sets': network_sets,
                     'network_set_ranges': network_set_ranges,
                     'ranges': ranges,
                     'rc': rc,
                     'server_profiles': server_profiles,
                     'uplink_sets': uplink_sets,
                     'users': users,
                     'timeandlocale': timeandlocale,
                     'true': true, 'false': false,
                     'vcenter': vcenter}


def get_variables():

    variables = default_variables
    return variables
"""

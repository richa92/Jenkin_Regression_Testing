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

APPLIANCE_IP = '15.199.233.234'
ENCLOSURE_IP = '15.245.129.1'

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

oa_details = {"oa_ip": ENCLOSURE_IP, "username": "Administrator", "password": "hpvse123"}

win_server_details = {"username": "Administrator", "password": "Hpvse123"}

Server_bays = ['1', '2', '3']

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


linux_details = {"hostip": "15.199.235.170", "username": "root", "password": "hpvse123", "dir_location": "/root/",
                 "python_cmd": "python2.7"}

ilo_details = [{'ilo_ip': '15.245.132.127', 'username': 'Administrator', 'password': 'compaq'}, {'ilo_ip': '15.245.132.30', 'username': 'Administrator', 'password': 'hpvse123'}]

server_details1 = [{'username': 'Administrator', 'password': 'Compaq123'}, {'username': 'Administrator', 'password': 'hpvse1'}]


diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\Write_to_lun.ps1"
list_disk_cmd = "PowerShell.exe -ExecutionPolicy Bypass -File .\\list_disk.ps1"

bay = ['3', '1']
bay_quartz = '2'


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

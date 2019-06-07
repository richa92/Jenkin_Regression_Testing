""" OVF442 """

ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

cim1_name = "CN75120D7B, appliance bay 1"

MAINTENANCE_CREDENTIALS = {"host": {"active": "16.114.210.229",
                                    "standby": "16.114.210.230"},
                           "username": "root",
                           "password": "hpvse1"}

MAINTENANCE_CREDENTIALS_BAK = {"host": {"active": "16.114.210.230",
                                        "standby": "16.114.210.229"},
                               "username": "maintenance",
                               "password": "hpvse1"}

CIM_HOSTS = {"active": "16.114.209.229",
             "standby": "16.114.211.59"}

CIM_HOSTS_BAK = {"active": "16.114.211.59",
                 "standby": "16.114.209.229"}

ilo_credentials = {'username': 'Admin', 'password': 'hpvse123'}

disable_ssh_body = {"allowSshAccess": False,
                    "type": "SshAccess"}

enable_ssh_body = {"allowSshAccess": True,
                   "type": "SshAccess"}

iLo_config_path = '/mnt/usb/'
Config_CIM_iLo_commands = {
    'part1': 'python /mnt/usb/em_cli.py',
    'part2': 'post CIManager/2 {"Action":"IloCmd","cmd":"set /map1/enetport1/lanendpt1/ipendpt1 IPv4Address=16.114.211.59 SubnetMask=255.255.240.0"}',
    'part3': 'post CIManager/2 {"Action": "IloCmd", "cmd":"set /map1/gateway1 AccessInfo=16.114.208.1"}',
    'part4': 'post CIManager/2 {"Action":"IloCmd","cmd":"create /map1/accounts1 username=Admin password=hpvse123 group=admin,config,oemhp_vm,oemhp_rc,oemhp_power"}',
    'part5': 'post CIManager/2 {"Action":"IloCmd","cmd":"set /map1/vlan1 EnabledState=disabled"}'
}

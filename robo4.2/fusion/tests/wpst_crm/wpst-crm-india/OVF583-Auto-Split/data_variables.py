
login_details = {'userName': 'Administrator', 'password': 'hpvse123'}
network_login_details = {'userName': 'network', 'password': 'hpvse123'}
server_login_details = {'userName': 'server', 'password': 'hpvse123'}
storage_login_details = {'userName': 'storage', 'password': 'hpvse123'}
software_login_details = {'userName': 'software', 'password': 'hpvse123'}
users = [{'userName': 'server', 'password': 'hpvse123', 'fullName': 'server', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'hpvse123', 'fullName': 'network', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'hpvse123', 'fullName': 'storage', 'roles': ['Storage administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'software', 'password': 'hpvse123', 'fullName': 'software', 'roles': ['Software administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]
# The Hafnium module IP can be either ipv4 or ipv6 (without % interface)
# Example
# PotashIP           = fe80::9edc:71ff:feac:34ad
# PotashIP            = 'fe80::5eb9:1ff:fe47:c48b'
PotashIP = '192.168.147.226'
PotashPassword = 'netoppwd'
PotashUname = 'netop'
Pcmd = 'ls'
PreLEPrompt = 'HPE#'
PostLEPrompt = 'OneView#'
SplitterInterface = 'Ten-GigabitEthernet 0/0/2:1'
FortyGigEInterface = 'FortyGigE 0/0/1'
pcmd = 'show'
HafniumModule = 'FVTCRMENC2, interconnect 3'
SSH_PASS = 'hpvse1'
PostLEInterfaceList = ['Ten-GigabitEthernet 0/0/2:1', 'Ten-GigabitEthernet 0/0/2:2', 'Ten-GigabitEthernet 0/0/2:3', 'FortyGigE 0/0/1']
PreLEInterfaceList = ['Ten-GigabitEthernet 0/0/1:1', 'Ten-GigabitEthernet 0/0/1:2', 'Ten-GigabitEthernet 0/0/1:3', 'FortyGigE 0/0/3']

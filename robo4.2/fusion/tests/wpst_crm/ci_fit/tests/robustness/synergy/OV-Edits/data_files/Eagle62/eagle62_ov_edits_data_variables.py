"""
USER DEFINED VARIABLES
"""

# INTERCONNECT NAMES FOR TOGGLE_UPLINK,TOGGLE_DOWNLINK
ICM_NAMES = ['ENC62_CN744502FG, interconnect 3', 'ENC63_CN754404R3, interconnect 6']

# DOWNLINK_PORT_NAME FOR TOGGLE_DOWNLINK
DOWNLINK_PORT_NAME = ['d2', 'd2']

# UPLINK_PORT_NAME  FOR TOGGLE_UPLINK
UPLINK_PORT_NAME = ['Q2', 'Q2']

# LE NAME  FOR REAPPLY_LE & TO GET LI NAME
LE = ['LE']

# LI NAME FOR LI-REAPPLY
LI = ['LE-LIG2_Potash']

# UPLINK SET TO BE DELETED IN LI FOR UFG SCENARIO
DELETE_UPLINKSET_NAME = ['BigPipe']

# SERVER_PROFILE FOR SERVER ONLINE,OFFLINE EDIT
# First column: Server Profiles. Second column: Enclosure, bay #
SERVER_PROFILE_ONLINE_OFFLINE_EDIT = {'rhel7_nolag_E63_Bay1': 'ENC63_CN754404R3, bay 1',
                                      'rhel7_lag_E63_Bay2': 'ENC63_CN754404R3, bay 2'
                                      }

# REQUESTED MBPS TO BE EDITED - FOR SERVER OFFLINE EDIT
REQUESTEDMBPS = '1500'

# CONNECTION DELETE FOR SERVER OFFLINE EDIT
# EXCEPTION - PXE CONNECTION DELETE ###PXE SECONDARY ID SHOULD BE DELETED BEFORE PXE PRIMARY ID###
# EXCEPTION - FC CONNECTION DELETE ###FC SECONDARY ID SHOULD BE DELETED BEFORE FC PRIMARY ID###
CONNECTION_ID = '2'

# server_profile_to_bay_map - FOR POWEROFF SERVER,POWERON SERVER,ASSIGN,UNASSIGN SERVERS
# First column: Server Profiles. Second column: Enclosure, bay #
SERVER_PROFILE_TO_BAY_MAP = SERVER_PROFILE_ONLINE_OFFLINE_EDIT

# support-dump-interval
LE_SUPPORT_DUMP_SLEEP = '50m'
OV_SUPPORT_DUMP_SLEEP = '15m'

# Appliance-Backup-Restore
POST_RESTORE_SLEEP = '50m'
BACKUP_DOWNLOAD_SLEEP = '5m'
UPLOAD_BACKUP_WAIT_TIME = '5m'
UPLOAD_BACKUP_WAIT_INTERVAL = '5s'

# server power on sleep
SERVER_POWERON_SLEEP = '15m'

# server hardware assign timeout
SERVER_HW_ASSIGN_WAIT_TIME = '240m'
SERVER_HW_ASSIGN_INTERVAL = '3s'

UPDATE_FROM_GROUP_WAIT_TIME = '90m'
UPDATE_FROM_GROUP_WAIT_INTERVAL = '5s'

# Wait for task sleep
WAIT_FOR_TASK_WAIT_TIME = '30m'
WAIT_FOR_TASK_INTERVAL = '5s'

# TOGGLE-IC-PORT
TOGGLE_INTERCONNECT_PORT_SLEEP = '3m'

# Server unaasign reassign sleep post restoration
SERVER_UNASSIGN_REASSIGN_SLEEP = '25m'

# -----------------
# Below variables are a copy of robustness data variable file. If we need to use  only one data variable file for test cases, its advisable to copy the above variables to configs robustnees data variable file
# -----------------

"""
DEFAULT VARIABLES
"""

# REQUEST BODY FOR LE SUPPORT DUMP
# errorCode - This string is a mandatory one to generate LE support dump and it is a part of support-dump file name,
# excludeApplianceDump - Boolean value that determines whether the appliance support dump content is excluded from the logical enclosure support dump. This attribute defaults to false if not included
# encrypt - Boolean value indicating if support dump needs to be encrypted or not
LE_SUPPORTDUMP_PAYLOAD = {"encrypt": False, "errorCode": "MyDump16", "excludeApplianceDump": False}

# REQUEST BODY FOR OV SUPPORT DUMP
# errorCode - This error code is a mandatory one and it is a part of support-dump file name, such as CI1234 or CI892a2
# encrypt - Boolean value indicating if support dump needs to be encrypted or not
SUPPORT_DUMP = {
    "errorCode": "CI",
    "encrypt": False
}

# ICM scripts directory and get ICM password script
ICM_SCRIPTS_DIR = '/root/ci-fit/virtualenv5/fusion500/tests/wpst_crm/ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'

# USE_HAFNIUM_RESOURCE_IPV4 = <True|False>
#   True: IPv4 address of Master Potash from resource data and use it.
#   False: Get the IPv6 link local address from canmic block
#          through OneView and use it.
#        : This recommended if your TCS has SSH access to Master Potash
#          using IPv6 link local.
USE_HAFNIUM_RESOURCE_IPV4 = True

# DISABLE_BONDING_MULTI_TEST: Perform multiple bonding interface checks which varies depending on the bonding mode.
# NOTE: This is by default set to False. Thus, to disable this test set this variable to True (Not recommented)
# DISABLE_BONDING_MULTI_TEST = False
# REMOTE_RUN_CHECKS: List of dictionary data of other hosts/ips that you want to trigger server checks (bonding, network, etc).
# REMOTE_RUN_CHECKS = [
#         { 'host': '15.186.13.8', 'username': 'root', 'password': 'rootpwd', 'command': {'logDir': 'remote_check_server', 'script': 'Check-Server.robot', 'scriptLocation': '/tmp/jasonp/fusion_420/tests/wpst_crm/ci_fit/tests/robustness/tools', 'haFile': '/tmp/jasonp/CISCO_HA_FILE-multi_tcs_compliant.conf', 'dataFile': '/tmp/jasonp/fusion_420/tests/wpst_crm/ci_fit/tests/robustness/resources/synergy_robustness_data_variables_template.py'}},
# ]

# NO_CHECK_BONDS: List of profiles you don't want to perform check bonds.
# Default (empty list): []
# Example workflow: 2 profiles will be excluded from check bonds
# NO_CHECK_BONDS = [
#     'CI-FIT-I8-Eagle35-Bay1',
#     'CI-FIT-I8-Eagle35-Bay2',
#     'CI-FIT-I8-Eagle35-Bay3',
#     'CI-FIT-I8-Eagle35-Bay4',
#     'CI-FIT-I8-Eagle35-Bay5',
#     'CI-FIT-I8-Eagle35-Bay6',
#     'CI-FIT-I8-Eagle49-Bay1',
#     'CI-FIT-I8-Eagle49-Bay2',
#     'CI-FIT-I8-Eagle49-Bay3',
#     'CI-FIT-I8-Eagle49-Bay4',
#     'CI-FIT-I8-Eagle49-Bay5',
#     'CI-FIT-I8-Eagle49-Bay6',
#     'CI-FIT-I8-Eagle49-Bay7',
#     'CI-FIT-I8-Eagle49-Bay8',
#     'CI-FIT-I8-Eagle49-Bay9',
#     'CI-FIT-I8-Eagle49-Bay10',
#     'CI-FIT-I8-Eagle49-Bay11',
#     'CI-FIT-I8-Eagle49-Bay12'
# ]
NO_CHECK_BONDS = [
    'ESX_eag62_bay3',
    'WIN_eag62_bay4',
]

# IGNORE_BOND_ATTRIBUTES: Dictionary of data containing profiles, bonds, and attributes you don't wnat check_bonds.py to test. We should only be using this for case like known issue and want to continue with the rest of the check bonds tests.
# Example:
# IGNORE_BOND_ATTRIBUTES = {
#         'rhel7_lag_E63_Bay2' : {
#             'All': ['Link Failure Count']
#         },
#         'rhel7_nolag_E63_Bay1' : {
#             'bond0': ['Link Failure Count']
#         }
# }
IGNORE_BOND_ATTRIBUTES = {
    'All': {
        'All': ['Link Failure Count']
    }
}

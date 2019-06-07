"""
    Example robustness data file for Synergy
"""

# For IPv6, use this '[your:ipv6:addr]'
APPLIANCE_IP = '15.186.9.xx'
# For multiple recipients, use comma-separated.
EMAIL_TO = 'your.email@hpe.com'

# Your local repo toplevel
TOPLEVEL_DIR = '/root/ci-fit/virtualenv1/fusion'

# SSHLibrary related variables
SSH_READ_WAIT = '2.0s'

# ICM scripts directory and get ICM password script
ICM_SCRIPTS_DIR = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'

# tcpdump script
REPO_SERVER_SCRIPTS_DIR = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/server'
TCPDUMP_SCRIPT = 'tcpdump_capture_blade.sh'

# HA_FILE
HA_FILE = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr.conf'

# USE_HAFNIUM_RESOURCE_IPV4 = <True|False>
#   True: IPv4 address of Master Potash from resource data and use it.
#   False: Get the IPv6 link local address from canmic block
#          through OneView and use it.
#        : This recommended if your TCS has SSH access to Master Potash
#          using IPv6 link local.
# USE_HAFNIUM_RESOURCE_IPV4 = True

# Assign server profile to server hardware even if server status is not OK
# FORCE_PROFILE_APPLY = 'all'

# Expected Common Resource Attributes
# NOTE: We are limited to simple key:value pair. We may consider adding complex structure like list, list of dictionary, etc in the future.
#       The goal for now is to be more granular with how we test resource states.
# ENCLOSURE: Dictionary of enclosures with corresponding attributes to check and the expected values
ENCLOSURES = {
    'Eagle62_CN744502FG': {
        'state': 'Configured',
        'status': 'OK',
        'refreshState': 'NotRefreshing',
        'enclosureType': 'SY12000',
        'reconfigurationState': 'NotReapplyingConfiguration'
    }
}

# TODO: ENCLOSURE_MANAGERS: Dictionary of EMs with expected attributes

# LOGICAL_ENCLOSURES: Dictionary of Logical Enclosures with corresponding attributes to check and the expected values
LOGICAL_ENCLOSURES = {
    'Eagle62_CN744502FG': {
        'state': 'Consistent',
        'status': 'OK',
        'scalingState': 'NotScaling',
        'powerMode': 'RedundantPowerFeed',
        'deleteFailed': False,
        'ambientTemperatureMode': 'Standard'
    }
}

# INTERCONNECTS: Dictionary of interconnects attributes and its corresponding expected values
INTERCONNECTS = {
    'Eagle62_CN744502FG, interconnect 3': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 40Gb F8 Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_40G',
        'networkLoopProtectionInterval': 5,
        'portCount': 104,
        'subPortCount': 8
    },
    'Eagle62_CN744502FG, interconnect 6': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 40Gb F8 Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_40G',
        'networkLoopProtectionInterval': 5,
        'portCount': 104,
        'subPortCount': 8
    }
}

# LOGICAL_INTERCONNECTS: Dictionary of logical interconnects attributes and its corresponding expected values
LOGICAL_INTERCONNECTS = {
    'LE-LIG 1': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'BiConnected',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    }
}

# Robustness wait timeouts, intervals and sleep settings will be here.
# Different environment may require different wait time, interval, and or sleep
# so please feel free to create your own settings that applies to your environment.
# This is similar concept as your setup and teardown data variable file.

# Common
ICM_POWER_REQUEST_WAIT_TIMEOUT = '60m'
ICM_POWER_REQUEST_WAIT_INTERVAL = '2s'
SERVER_POWERON_WAIT_TIMEOUT = '60m'
SERVER_POWERON_WAIT_INTERVAL = '2s'
ASSIGN_SERVER_WAIT_TIMEOUT = '60m'
ASSIGN_SERVER_WAIT_INTERVAL = '2s'
UNASSIGN_SERVER_WAIT_TIMEOUT = '60m'
UNASSIGN_SERVER_WAIT_INTERVAL = '2s'
SPP_UPLOAD_WAIT_TIMEOUT = '60m'
SPP_UPLOAD_WAIT_INTERVAL = '30s'

# Appliance-Backup-Restore
POST_RESTORE_SLEEP = '10m'
CREATE_BACKUP_WAIT_TIMEOUT = '15m'
CREATE_BACKUP_WAIT_INTERVAL = '2s'
UPLOAD_BACKUP_WAIT_TIMEOUT = '1m'
UPLOAD_BACKUP_WAIT_INTERVAL = '2s'
RESTORE_BACKUP_WAIT_TIMEOUT = '60m'
RESTORE_BACKUP_WAIT_INTERVAL = '2s'

# Appliance-Reboot
POST_APPLIANCE_REBOOT_SLEEP = '45m'
APPLIANCE_REBOOT_WAIT_TIMEOUT = '45m'
APPLIANCE_REBOOT_WAIT_INTERVAL = '2s'

# Blade-Hot-Plug
BLADE_REMOVE_WAIT_TIMEOUT = '30m'
BLADE_REMOVE_WAIT_INTERVAL = '2s'
BLADE_INSERT_WAIT_TIMEOUT = '30m'
BLADE_INSERT_WAIT_INTERVAL = '2s'
BLADE_HOTPLUG_STATE_WAIT_TIMEOUT = '30m'
BLADE_HOTPLUG_STATE_WAIT_INTERVAL = '2s'
BLADE_HOTPLUG_CYCLE_SLEEP = '1m'

# CIM-Hot-Plug
POST_CIM_HOTPLUG_SLEEP = '40m'

# CIM-Failover
CIM_FAILOVER_CYCLE_SLEEP = '60m'
CIM_FAILOVER_WAIT_TIMEOUT = '60m'
CIM_FAILOVER_WAIT_INTERVAL = '2s'

# EM-Failover
POST_EM_FAILOVER_SLEEP = '5m'

# ICM-Hot-Plug
# Based on Aileen Cantarelli, Carbon recommended sleep is 20m
ICM_HOTPLUG_CYCLE_SLEEP = '60m'
ICM_HOTPLUG_WAIT_TIMEOUT = '35m'
ICM_HOTPLUG_WAIT_INTERVAL = '15s'

# ICM-EFuseReset
# Based on Aileen Cantarelli, Carbon recommended sleep is 20m
ICM_EFUSE_RESET_CYCLE_SLEEP = '150m'
ICM_EFUSE_RESET_WAIT_TIMEOUT = '150m'
ICM_EFUSE_RESET_WAIT_INTERVAL = '15s'


# ICM-Reboot
POTASH_SERVER_RECOVERY_SLEEP = '30m'
ICM_REBOOT_ALERT_WAIT_TIMEOUT = '240m'
ICM_REBOOT_ALERT_WAIT_INTERVAL = '1m'
ICM_REBOOT_MAINTENANCE_WAIT_TIMEOUT = '60m'
ICM_REBOOT_MAINTENANCE_WAIT_INTERVAL = '30s'
ICM_REBOOT_CONFIGURED_WAIT_TIMEOUT = '60m'
ICM_REBOOT_CONFIGURED_WAIT_INTERVAL = '30s'

# ICM-Reset
POST_ICM_RESET_SLEEP = '10m'
ICM_RESET_WAIT_TIMEOUT = '2m'
ICM_RESET_WAIT_INTERVAL = '2s'

# LE-add-remove
POST_SERVER_ON_SLEEP = '30m'
POST_ADD_LE_SLEEP = '5m'

# Potash-Warm-Reboot
# Due to it's complexity, it has its own dedicated data variable file under the Potash-Warm-Reboot dir.

# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
# CHECK_READONLY = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
# CHECK_MEATGRINDER = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# SEQUENTIAL_PING_SCRIPT: This is path to your ping_ips_sequential script
SEQUENTIAL_PING_SCRIPT = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/tcs/ping_ips_sequential'

# PING_HAFILE: Sequential ping will be run as part of the test using the HA file provided in this variable
# PING_HAFILE = HA_FILE

# CHECK_MULTIPATH: IPs to check for multipath
# Example from Eagle11 setup:
# CHECK_MULTIPATH = {'192.168.1.140':2, '192.168.1.200':3, '172.18.25.2':4, '192.168.1.190':4, '192.168.11.103':4, '192.168.1.125':2, '192.168.1.105':2, '192.168.1.150':4, '192.168.1.158':4, '192.168.1.128':4}

# FPING_HOST_IP, FPING_HOST_USERNAME, and FPING_HOST_PASSWORD: Are shared by remote fping execution and CHECK_FPING_LOSS feature
# FPING_HOST_IP = '15.186.6.161'
# FPING_HOST_USERNAME = 'root'
# FPING_HOST_PASSWORD = 'rootpwd'
# CHECK_FPING_LOSS: When set to True, it will ssh to FPING_HOST_IP and issue the get-all-continuous-fping-loss.py command below
# CHECK_FPING_LOSS = True
# NOTE: -m value is the maximum acceptable ping loss in milliseconds
# GET_FPING_LOSS_CMD = '/root/jasonp/get-all-continuous-fping-loss.py -s 10000 -m 0 -c /root/ci-fit/config_files/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf -l /root/tools/logs/old/JasonRunOnOV40RC3Hf120P1005Chloride1.08_2017-12-06_02_17_16/ -n sub_en*'
# GET_FPING_LOSS_CMD = '/root/jasonp/get-all-continuous-fping-loss.py -s 10000 -m 0 -c ~/ci-fit/config_files/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf -l /root/tools/logs/old/NDFUA-1.2.0.1005to1.2.1.3/ -n sub_en*'
# NO_PING_SOURCE: List of server profile names that will not have a ping source (they are still ping targets)
#                 This is to workaround a current limitation with our fping source. Windows fping behaves differently.
# NO_PING_SOURCE = [
#    'ESX_eag62_bay3',
#    'WIN_eag62_bay4',
# ]

# CHECK_ISS_CRASH: When set to True, it will ssh to Hafnium and check for ISS crash.
# NOTE: This is by default set to True. Thus, to disable this test set this variable to False (Not recommended).
# CHECK_ISS_CRASH = True

# SERVER_BONDING_CHECKS: Check server bonding interfaces based on the defined arguments/checks below.
# Supported arguments/check depends the bonding mode.
# Default: None
# To disable: SERVER_BONDING_CHECKS = None
# For example, mode=4: --churn-state --permanent-hw-addr --actor-system-mac --speed 10000 --status both --aggregator-id --system-mac-addr
# mode=5: --permanent-hw-addr --speed 10000 --status both
# SERVER_BONDING_CHECKS = '--churn-state --permanent-hw-addr --actor-system-mac --speed 10000 --status both --aggregator-id --system-mac-addr'

# CHECK_ETH_SUMMARY: Check that all ports are linked
# CHECK_ETH_SUMMARY = True

# DISABLE_BONDING_MULTI_TEST: Perform multiple bonding interface checks which varies depending on the bonding mode.
# NOTE: This is by default set to False. Thus, to disable this test set this variable to True (Not recommented)
# DISABLE_BONDING_MULTI_TEST = False
# REMOTE_RUN_CHECKS: List of dictionary data of other hosts/ips that you want to trigger server checks (bonding, network, etc).
# REMOTE_RUN_CHECKS = [
#         { 'host': '15.186.13.8', 'username': 'root', 'password': 'rootpwd', 'command': {'logDir': 'remote_check_server', 'script': 'Check-Server.robot', 'scriptLocation': '/tmp/jasonp/fusion_420/tests/wpst_crm/ci_fit/tests/robustness/tools', 'haFile': '/tmp/jasonp/CISCO_HA_FILE-multi_tcs_compliant.conf', 'dataFile': '/tmp/jasonp/fusion_420/tests/wpst_crm/ci_fit/tests/robustness/resources/synergy_robustness_data_variables_template.py'}},
# ]
# REMOTE_RUN_CHECKS = [
#         { 'host': '15.186.7.224', 'username': 'root', 'password': 'rootpwd', 'command': {'logDir': 'remote_check_server', 'script': 'Check-Server.robot', 'scriptLocation': '/root/ci-fit/virtualenv5/fusion500/tests/wpst_crm/ci_fit/tests/robustness/tools', 'haFile': '/root/ci-fit/config_files/Eagle62-63_HA_ipaddr_sortedByVlan.conf', 'dataFile': '/root/ci-fit/config_files/robustness/Eagle62-63_robustness_data_variable.py'}},
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

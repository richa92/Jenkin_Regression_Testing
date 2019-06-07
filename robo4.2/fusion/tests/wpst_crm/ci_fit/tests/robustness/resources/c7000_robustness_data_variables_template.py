APPLIANCE_IP = '15.186.9.x'
# For multiple recipients, use comma-separated.
EMAIL_TO = 'your.email@hpe.com'

# Your local repo toplevel
TOPLEVEL_DIR = '/root/ci-fit/virtualenv/fusion-410/fusion'

# SSHLibrary related variables
SSH_READ_WAIT = '2.0s'

# Assign server profile to server hardware even if server status is not OK
# FORCE_PROFILE_APPLY = 'all'

# Expected Common Resource Attributes
# NOTE: We are limited to simple key:value pair. We may consider adding complex structure like list, list of dictionary, etc in the future.
#       The goal for now is to be more granular with how we test resource states.
# ENCLOSURE: Dictionary of enclosures with corresponding attributes to check and the expected values
ENCLOSURES = {
    'C15M_Bmark': {
        'enclosureType': 'C7000',
        'licensingIntent': 'OneViewNoiLO',
        'reconfigurationState': 'NotReapplyingConfiguration',
        'refreshState': 'NotRefreshing',
        'state': 'Configured',
        'status': 'OK'
    }
}

# TODO: ENCLOSURE_MANAGERS: Dictionary of EMs with expected attributes

# LOGICAL_ENCLOSURES: Dictionary of Logical Enclosures with corresponding attributes to check and the expected values
LOGICAL_ENCLOSURES = {
    'C15M_Bmark': {
        'state': 'Consistent',
        'status': 'OK',
        'scalingState': 'NotScaling',
        'powerMode': None,
        'deleteFailed': False,
        'ambientTemperatureMode': 'Standard'
    }
}

# INTERCONNECTS: Dictionary of interconnects attributes and its corresponding expected values
INTERCONNECTS = {
    'C15M_Bmark, interconnect 1': {
        'deviceResetState': None,
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'C7000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_20G',
        'model': 'HP VC FlexFabric-20/40 F8 Module',
        'networkLoopProtectionInterval': 5,
        'portCount': 42,
        'powerState': 'On',
        'state': 'Configured',
        'status': 'OK',
        'subPortCount': 4
    },
    'C15M_Bmark, interconnect 2': {
        'deviceResetState': None,
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'C7000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_20G',
        'model': 'HP VC FlexFabric-20/40 F8 Module',
        'networkLoopProtectionInterval': 5,
        'portCount': 42,
        'powerState': 'On',
        'state': 'Configured',
        'status': 'OK',
        'subPortCount': 4
    },
    'C15M_Bmark, interconnect 3': {
        'deviceResetState': None,
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'C7000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_10G',
        'model': 'HP VC Flex-10/10D Module',
        'networkLoopProtectionInterval': 5,
        'portCount': 30,
        'powerState': 'On',
        'state': 'Configured',
        'status': 'OK',
        'subPortCount': 4
    },
    'C15M_Bmark, interconnect 4': {
        'deviceResetState': None,
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'C7000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_10G',
        'model': 'HP VC Flex-10/10D Module',
        'networkLoopProtectionInterval': 5,
        'portCount': 30,
        'powerState': 'On',
        'state': 'Configured',
        'status': 'OK',
        'subPortCount': 4
    },
    'C15M_Bmark, interconnect 5': {
        'deviceResetState': None,
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'C7000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_10G',
        'model': 'HP VC 8Gb 24-Port FC Module',
        'networkLoopProtectionInterval': 5,
        'portCount': 24,
        'powerState': 'On',
        'state': 'Configured',
        'status': 'OK',
        'subPortCount': -1
    },
    'C15M_Bmark, interconnect 6': {
        'deviceResetState': None,
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'C7000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_10G',
        'model': 'HP VC 8Gb 24-Port FC Module',
        'networkLoopProtectionInterval': 5,
        'portCount': 24,
        'powerState': 'On',
        'state': 'Configured',
        'status': 'OK',
        'subPortCount': -1
    }
}

# LOGICAL_INTERCONNECTS: Dictionary of logical interconnects attributes and its corresponding expected values
LOGICAL_INTERCONNECTS = {
    'C15M_Bmark-LIG 1': {
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'C7000',
        'stackingHealth': 'NotApplicable',
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
    }
}

# Robustness wait timeouts, intervals and sleep settings will be here.
# Different environment may require different wait time, interval, and or sleep
# so please feel free to create your own settings that applies to your environment.
# This is similar concept as your setup and teardown data variable file.

# Common
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

# Appliance-Enc-Add-Remove
REMOVE_ENC_WAIT_TIMEOUT = '10m'
REMOVE_ENC_WAIT_INTERVAL = '5s'
POST_ADD_ENC_SLEEP = '10m'
POST_ASSIGN_PROFILE_SLEEP = '2m'
POST_SERVER_ON_SLEEP = '20m'

# Appliance-Reboot
POST_APPLIANCE_REBOOT_SLEEP = '45m'
APPLIANCE_REBOOT_WAIT_TIMEOUT = '45m'
APPLIANCE_REBOOT_WAIT_INTERVAL = '2s'

# Blade-Hot-Plug
BLADE_REMOVE_WAIT_TIMEOUT = '30m'
BLADE_REMOVE_WAIT_INTERVAL = '2s'
BLADE_HOTPLUG_STATE_WAIT_TIMEOUT = '35m'
BLADE_HOTPLUG_STATE_WAIT_INTERVAL = '15s'
POST_BLADE_REMOVE_SLEEP = '2m'
BLADE_HOTPLUG_CYCLE_SLEEP = '5m'

# ICM-Hot-Plug
ICM_HOTPLUG_STATE_WAIT_TIMEOUT = '35m'
ICM_HOTPLUG_STATE_WAIT_INTERVAL = '15s'
POST_ICM_REMOVE_SLEEP = '2m'
ICM_HOTPLUG_CYCLE_SLEEP = '15m'

# ICM-Reboot
# See NOTE in the script on why this should no longer be needed
# ICM_REBOOT_ABSENT_WAIT_TIMEOUT = '35m'
# ICM_REBOOT_ABSENT_WAIT_INTERVAL = '15s'
ICM_REBOOT_CONFIGURED_WAIT_TIMEOUT = '35m'
ICM_REBOOT_CONFIGURED_WAIT_INTERVAL = '15s'
POST_ICM_REBOOT_SLEEP = '2m'
ICM_REBOOT_CYCLE_SLEEP = '5m'

# OA-Force-Takeover
POST_OA_TAKEOVER_SLEEP = '6m'

# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
# CHECK_READONLY = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
# CHECK_MEATGRINDER = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# SEQUENTIAL_PING_SCRIPT: Path to your ping_ips_sequential script.
# SEQUENTIAL_PING_SCRIPT = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/tcs/ping_ips_sequential'

# PING_HAFILE: Sequential ping will be run as part of the test using the HA file provided in this variable
# Example from Eagle11 setup:
# PING_HAFILE = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr.conf'

# CHECK_MULTIPATH: IPs to check for multipath
# Example from Eagle11 setup:
# CHECK_MULTIPATH = {'192.168.1.140':2, '192.168.1.200':3, '172.18.25.2':4, '192.168.1.190':4, '192.168.11.103':4, '192.168.1.125':2, '192.168.1.105':2, '192.168.1.150':4, '192.168.1.158':4, '192.168.1.128':4}
# Example from C7000 EST Verizon setup:
# CHECK_MULTIPATH = {
# fit-12
# '172.16.229.154':2, '172.16.228.39':4, '172.16.229.219':2, '172.16.229.3':2, '172.16.228.40':2, #'172.16.228.241':4,
# '172.16.228.235':2, fit-12 bay 7
#        '172.16.229.5':4,
# fit-13
#        '172.16.228.248':2, '172.16.228.194':4, '172.16.228.193':2, '172.16.229.7':4, '172.16.229.9':2, '172.16.228.43':4, '172.16.228.42':2, '172.16.230.43':4, '172.16.230.16':4,
# fit-14
# '172.16.228.250':4, '172.16.228.195':4, '172.16.229.206':4, '172.16.229.13':3, #'172.16.229.16':4,
#        '172.16.228.201':4, '172.16.228.198':2, '172.16.229.14':1, '172.16.228.199':2, '172.16.229.15':2,
# fit-15
#        '172.16.229.20':4, '172.16.229.22':4, '172.16.229.24':4, '172.16.228.202':4, '172.16.229.26':4, '172.16.228.243':4,
# fit-16
# nothing
# fit-17
# '172.16.229.160':4, '172.16.229.234':3, #'172.16.228.254':4,
# '172.16.229.198':2, fit-17 bay 5 very slow
# '172.16.229.193':4, '172.16.229.236':3, '172.16.229.2':4, #'172.16.229.199':2,
# '172.16.229.191':4, '172.16.229.238':3, #'172.16.229.11':4,
# '172.16.131.1':4, #'172.16.229.240':3, #fit-17 bay 15 not going back after hotplug ICM4 (verizon is not using it so will worrry later)
# '172.16.229.0':4
#        }

# CHECK_FPING_LOSS: When set to True, it will ssh to FPING_HOST_IP and issue the get-all-continuous-fping-loss.py command below
# CHECK_FPING_LOSS = True
# FPING_HOST_IP = '15.186.6.161'
# FPING_HOST_USERNAME = 'root'
# FPING_HOST_PASSWORD = 'rootpwd'
# NOTE: -m value is the maximum acceptable ping loss in milliseconds
# GET_FPING_LOSS_CMD = '/root/jasonp/get-all-continuous-fping-loss.py -s 10000 -m 0 -c /root/ci-fit/config_files/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf -l /root/tools/logs/old/JasonRunOnOV40RC3Hf120P1005Chloride1.08_2017-12-06_02_17_16/ -n sub_en*'
# GET_FPING_LOSS_CMD = '/root/jasonp/get-all-continuous-fping-loss.py -s 10000 -m 0 -c ~/ci-fit/config_files/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf -l /root/tools/logs/old/NDFUA-1.2.0.1005to1.2.1.3/ -n sub_en*'

# DISABLE_BONDING_MULTI_TEST: Perform multiple bonding interface checks which varies depending on the bonding mode.
# NOTE: This is by default set to True for C7000 while it is a work in progress. Don't enable this for now!
# DISABLE_BONDING_MULTI_TEST = True
# REMOTE_RUN_CHECKS: List of dictionary data of other hosts/ips that you want to trigger server checks (bonding, network, etc).
# REMOTE_RUN_CHECKS = [
#         { 'host': '15.186.13.8', 'username': 'root', 'password': 'rootpwd', 'command': {'logDir': 'remote_check_server', 'script': 'Check-Server.robot', 'scriptLocation': '/tmp/jasonp/fusion_420/tests/wpst_crm/ci_fit/tests/robustness/tools', 'haFile': '/tmp/jasonp/CISCO_HA_FILE-multi_tcs_compliant.conf', 'dataFile': '/tmp/jasonp/fusion_420/tests/wpst_crm/ci_fit/tests/robustness/resources/synergy_robustness_data_variables_template.py'}},
# ]

# NO_CHECK_BONDS: List of profiles you don't want to perform check bonds.
# Default (empty list): []
# Example workflow: 2 profiles will be excluded from check bonds
# NO_CHECK_BONDS = ['CN754404R3_bay1', 'CN754404R3_bay2']

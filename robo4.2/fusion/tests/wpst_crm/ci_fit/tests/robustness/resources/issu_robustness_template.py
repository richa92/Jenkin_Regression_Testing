APPLIANCE_IP = '15.186.9.xx'
# For multiple recipients, use comma-separated.
EMAIL_TO = 'your.email@hpe.com'

# Your local repo toplevel
TOPLEVEL_DIR = '/root/ci-fit/virtualenv/fusion-410/fusion'

# Fusion defaults
# FUSION_IP = '15.199.230.101'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
# FUSION_SSH_PASSWORD = 'hponeview'        # Fusion SSH Password

FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

# Fusion Interconnect Decoder Ring
CARBON = 'Virtual Connect SE 16Gb FC Module for Synergy'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
HAFNIUM_ICM_MODELS = [POTASH, NITRO]

# Server default credentials
SERVER_USERNAME = 'root'
SERVER_PASSWORD = 'rootpwd'

# Assign server profile to server hardware even if server status is not OK
# FORCE_PROFILE_APPLY = 'all'

# MeatGrinder location
MEATGRINDER_DIR = '/root/tools/LinuxMG_2.610_x86-64'

# Sequential ping script
SEQUENTIAL_PING_SCRIPT = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/tcs/ping_ips_sequential'

# Multipath script
MULTIPATH_SCRIPT = '/root/tools/scripts/check-multipath.sh'

# CHECK_FPING_LOSS: When set to True, it will ssh to FPING_HOST_IP and issue the get-all-continuous-fping-loss.py command below
# CHECK_FPING_LOSS = True
# FPING_HOST_IP = '15.186.6.161'
# FPING_HOST_USERNAME = 'root'
# FPING_HOST_PASSWORD = 'rootpwd'
# NOTE: -m value is the maximum acceptable ping loss in milliseconds
# GET_FPING_LOSS_CMD = '/root/jasonp/get-all-continuous-fping-loss.py -s 10000 -m 0 -c /root/ci-fit/config_files/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf -l /root/tools/logs/old/JasonRunOnOV40RC3Hf120P1005Chloride1.08_2017-12-06_02_17_16/ -n sub_en*'
# GET_FPING_LOSS_CMD = '/root/jasonp/get-all-continuous-fping-loss.py -s 10000 -m 0 -c ~/ci-fit/config_files/HA_ipaddr_I1_VPLagV5Woutnet_1_manual_correct_subnets_conflicts.conf -l /root/tools/logs/old/NDFUA-1.2.0.1005to1.2.1.3/ -n sub_en*'

# CHECK_ISS_CRASH: When set to True, it will ssh to Hafnium and check for ISS crash.
# NOTE: This is by default set to True. Thus, to disable this test set this variable to False.
# CHECK_ISS_CRASH = False

# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
# CHECK_READONLY = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
# CHECK_MEATGRINDER = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

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

ICM_SCRIPTS_DIR = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'
ENC_NAME = 'CN754404R3'
ICM_NAMES = [ENC_NAME + ', interconnect 3', ENC_NAME + ', interconnect 6']
TARGET_LI = 'LE-LIG 1'
LI_UPDATE_BODY = {"sppUri": ' ',
                  "command": "UPDATE",
                  "force": True,
                  "ethernetActivationType": "PairProtect",
                  "ethernetActivationDelay": "0",
                  "fcActivationType": "PairProtect",
                  "fcActivationDelay": "0",
                  "validationType": "ValidateBestEffort"
                  }
# Some of the wait timeouts/intervals
SPP_UPLOAD_WAIT_TIMEOUT = '30m'
SPP_UPLOAD_WAIT_INTERVAL = '2s'
FW_UPDATE_WAIT_TIMEOUT = '60m'
FW_UPDATE_WAIT_INTERVAL = '1m'
END_OF_CYCLE_WAIT = '15m'

# Expected Common Resource Attributes
# NOTE: We are limited to simple key:value pair. We may consider adding complex structure like list, list of dictionary, etc in the future.
#       The goal for now is to be more granular with how we test resource states.
# ENCLOSURE: Dictionary of enclosures with corresponding attributes to check and the expected values
ENCLOSURES = {
    ENC_NAME: {
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
    'LE': {
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
    ICM_NAMES[0]: {
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
    ICM_NAMES[1]: {
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
    TARGET_LI: {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'BiConnected',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    }
}

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
# NO_CHECK_BONDS = ['CN754404R3_bay1', 'CN754404R3_bay2']

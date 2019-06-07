"""
    Template of data file for MultiActive Detection and Recovery robustness test
"""


# For IPv6, use this '[your:ipv6:addr]'
APPLIANCE_IP = '15.186.9.xx'
# For multiple recipients, use comma-separated.
EMAIL_TO = 'your.email@hpe.com'

# Your local repo toplevel
TOPLEVEL_DIR = '/root/ci-fit/virtualenv/fusion-410/fusion'

# Fusion defaults
# FUSION_IP = '15.199.230.101'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# SSHLibrary related variables
SSH_READ_WAIT = '2.0s'

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
FORCE_PROFILE_APPLY = 'all'

# MeatGrinder location
MEATGRINDER_DIR = '/root/tools/LinuxMG_2.610_x86-64'

# Sequential ping script
SEQUENTIAL_PING_SCRIPT = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/tcs/ping_ips_sequential'

# Multipath script
MULTIPATH_SCRIPT = '/root/tools/scripts/check-multipath.sh'


ICM_SCRIPTS_DIR = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'
ENC_NAMES = ['CN744502F3']
ICM3 = ENC_NAMES[0] + ', interconnect 3'
ICM6 = ENC_NAMES[0] + ', interconnect 6'
ICM_NAMES = [ICM3, ICM6]
# TARGET_ENC: Enclosure where you want to break DUS or programatically remove stacking link.
TARGET_ENC = ENC_NAMES[0]
# TARGET_ICM: Interconnect name where the stacking links be removed.
TARGET_ICM = ICM_NAMES[0]
STACKING_LINK_WAIT_TIMEOUT = '60m'
STACKING_LINK_WAIT_INTERVAL = '30s'
STACKING_SLEEP = '30s'

TARGET_LI = 'LE-LIG 2'
# Disable FC uplink port (side a)
FC_UPLINK_PORT_SIDEA = "Q3:1"
FC_NETWORK_NAME_SIDEA = "SAN-A-FA"
FC_UPLINK_SET_SIDEA = FC_NETWORK_NAME_SIDEA
DISABLE_FC_UPLINK_SIDEA = {
    "associatedUplinkSetUri": FC_UPLINK_SET_SIDEA,
    "interconnectName": ICM_NAMES[0],
    "portType": "Uplink",
    # NOTE: change this to your ICM's {id}
    "portId": "64081102-6f44-400c-a8ad-457b156adcd7:%s" % FC_UPLINK_PORT_SIDEA,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["FibreChannel"],
    "enabled": False,
    "portName": FC_UPLINK_PORT_SIDEA,
    "portStatus": "Linked",
    "type": "port"
}
TOGGLE_UPLINK_WAIT_TIMEOUT = '30m'
TOGGLE_UPLINK_WAIT_INTERVAL = '15s'
# Enable FC uplink port
ENABLE_FC_UPLINK_SIDEA = {
    "associatedUplinkSetUri": FC_UPLINK_SET_SIDEA,
    "interconnectName": ICM_NAMES[0],
    "portType": "Uplink",
    # NOTE: change this to your ICM's {id}
    "portId": "64081102-6f44-400c-a8ad-457b156adcd7:%s" % FC_UPLINK_PORT_SIDEA,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["FibreChannel"],
    "enabled": True,
    "portName": FC_UPLINK_PORT_SIDEA,
    "portStatus": "Linked",
    "type": "port"
}

# Expected Common Resource Attributes
# NOTE: We are limited to simple key:value pair. We may consider adding complex structure like list, list of dictionary, etc in the future.
#       The goal for now is to be more granular with how we test resource states.
# ENCLOSURE: Dictionary of enclosures with corresponding attributes to check and the expected values
ENCLOSURES = {
    ENC_NAMES[0]: {
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
        #        'state': 'Consistent',
        #        'status': 'OK',
        'scalingState': 'NotScaling',
        'powerMode': 'RedundantPowerFeed',
        'deleteFailed': False,
        'ambientTemperatureMode': 'Standard'
    }
}

# INTERCONNECTS: Dictionary of interconnects attributes and its corresponding expected values
INTERCONNECTS = {
    ENC_NAMES[0] + ', interconnect 3': {
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
    ENC_NAMES[0] + ', interconnect 6': {
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
    ENC_NAMES[0] + ', interconnect 1': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 16Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_16G',
        'networkLoopProtectionInterval': 5,
        'portCount': 36,
        'subPortCount': 0
    },
    ENC_NAMES[0] + ', interconnect 4': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 16Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_16G',
        'networkLoopProtectionInterval': 5,
        'portCount': 36,
        'subPortCount': 0
    }
}

# LOGICAL_INTERCONNECTS: Dictionary of logical interconnects attributes and its corresponding expected values
LOGICAL_INTERCONNECTS = {
    'LE-LIG 1-1': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'NotApplicable',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    },
    TARGET_LI: {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        #        'status': 'OK',
        'stackingHealth': 'BiConnected',
        #        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    }
}

# Negative testing: toggling stacking ports using REST API
# Disable stacking port 1
STACKING_PORT_1 = "Q7"
DISABLE_STACKING_PORT_1 = {
    "associatedUplinkSetUri": None,
    "interconnectName": ICM_NAMES[0],
    "portType": "Stacking",
    "portId": "319ef9a0-eb56-41c6-98be-27ea869537b7:%s" % STACKING_PORT_1,
    "portHealthStatus": "Normal",
    "capability": ["Stacking", "Ethernet"],
    "configPortTypes": ["Stacking", "Ethernet"],
    "enabled": False,
    "portName": STACKING_PORT_1,
    "portStatus": "Linked",
    "type": "port"
}

# Enable stacking port 1
ENABLE_STACKING_PORT_1 = {
    "associatedUplinkSetUri": None,
    "interconnectName": ICM_NAMES[0],
    "portType": "Stacking",
    "portId": "319ef9a0-eb56-41c6-98be-27ea869537b7:%s" % STACKING_PORT_1,
    "portHealthStatus": "Normal",
    "capability": ["Stacking", "Ethernet"],
    "configPortTypes": ["Stacking", "Ethernet"],
    "enabled": True,
    "portName": STACKING_PORT_1,
    "portStatus": "Linked",
    "type": "port"
}

# Disable stacking port 2
STACKING_PORT_2 = "Q8"
DISABLE_STACKING_PORT_2 = {
    "associatedUplinkSetUri": None,
    "interconnectName": ICM_NAMES[1],
    "portType": "Stacking",
    "portId": "37818749-e7db-4e22-ab19-6c691155fd2c:%s" % STACKING_PORT_2,
    "portHealthStatus": "Normal",
    "capability": ["Stacking", "Ethernet"],
    "configPortTypes": ["Stacking", "Ethernet"],
    "enabled": False,
    "portName": STACKING_PORT_2,
    "portStatus": "Linked",
    "type": "port"
}

# Enable stacking port 2
ENABLE_STACKING_PORT_2 = {
    "associatedUplinkSetUri": None,
    "interconnectName": ICM_NAMES[1],
    "portType": "Stacking",
    "portId": "37818749-e7db-4e22-ab19-6c691155fd2c:%s" % STACKING_PORT_2,
    "portHealthStatus": "Normal",
    "capability": ["Stacking", "Ethernet"],
    "configPortTypes": ["Stacking", "Ethernet"],
    "enabled": True,
    "portName": STACKING_PORT_2,
    "portStatus": "Linked",
    "type": "port"
}

# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
# CHECK_READONLY = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
CHECK_MEATGRINDER = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.19.189 192.168.1.125 192.168.1.105 192.168.1.150 192.168.19.155 172.19.13.2'

# PING_HAFILE: Sequential ping will be run as part of the test using the HA file provided in this variable
# Example from Eagle11 setup:
PING_HAFILE = TOPLEVEL_DIR + '/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr.conf'

# CHECK_MULTIPATH: IPs to check for multipath while in steady state or all expected paths are up, active and running
# Example from Eagle11 setup:
CHECK_MULTIPATH = {
    # bay1
    '192.168.1.140': 2,
    # bay2
    '192.168.1.200': 3,
    # bay3
    '192.168.18.32': 4,
    # bay3
    # '172.18.25.2':4,
    # bay4
    '192.168.1.190': 4,
    # bay5
    '192.168.19.189': 4,
    # bay7
    '192.168.1.125': 2,
    # bay8
    '192.168.1.105': 2,
    # bay10
    '192.168.1.150': 4,
    # bay11
    '192.168.19.155': 4,
    # bay12
    '172.19.13.2': 4
}

# CHECK_MULTIPATH_LESS1FC: your multipath when your 1 side of your FC connection set in data file is disabled.
CHECK_MULTIPATH_LESS1FC = {
    # bay1
    '192.168.1.140': 2,
    # bay2
    '192.168.1.200': 2,
    # bay3
    '192.168.18.32': 4,
    # bay3
    # '172.18.25.2':4,
    # bay4
    '192.168.1.190': 4,
    # bay5
    '192.168.19.189': 3,
    # bay7
    '192.168.1.125': 1,
    # bay8
    '192.168.1.105': 2,
    # bay10
    '192.168.1.150': 3,
    # bay11
    '192.168.19.155': 4,
    # bay12
    '172.19.13.2': 4
}

# CHECK_MULTIPATH_BREAKDUS: your expected multipath when in MAD condition (stacking link is disabled).
CHECK_MULTIPATH_BREAKDUS = {
    # bay1
    '192.168.1.140': 1,
    # bay2
    '192.168.1.200': 2,
    # bay3
    '192.168.18.32': 2,
    # bay3
    # '172.18.25.2':2,
    # bay4
    '192.168.1.190': 2,
    # bay5
    '192.168.19.189': 2,
    # bay7
    '192.168.1.125': 1,
    # bay8
    '192.168.1.105': 1,
    # bay10
    '192.168.1.150': 2,
    # bay11
    '192.168.19.155': 2,
    # bay12
    '172.19.13.2': 2
}

# CHECK_INTERFACE: IPs to check for server network interfaces
# CHECK_INTERFACE = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158 192.168.1.128'

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

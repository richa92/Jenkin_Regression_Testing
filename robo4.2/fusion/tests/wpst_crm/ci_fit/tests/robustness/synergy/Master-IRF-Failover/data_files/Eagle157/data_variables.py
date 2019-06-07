APPLIANCE_IP = '15.186.9.157'
# For multiple recipients, use comma-separated.
EMAIL_TO = 'satyalok.dash@hpe.com'

# USE_HAFNIUM_RESOURCE_IPV4 = <True|False>
#   True: IPv4 address of Master Potash from resource data and use it.
#   False: Get the IPv6 link local address from canmic block
#          through OneView and use it.
#        : This recommended if your TCS has SSH access to Master Potash
#          using IPv6 link local.
USE_HAFNIUM_RESOURCE_IPV4 = True
# Below are Hafnium credential
HAFNIUM_USERNAME = 'root'
HAFNIUM_PASSWORD = 'UnoVista'
# Your 59XX switch IP and credential
SW_59XX_IPADDR = '15.186.6.35'
SW_59XX_USERNAME = 'admin'
SW_59XX_PASSWORD = 'password'
# Below are iPDU IP Address and Socket port.
iPDU_IP = '15.186.18.118'
iPDU_IP2 = '15.186.18.77'
iPDU_IP3 = '15.186.18.152'
iPDU_PORT = 50443
# Mapping of your 59XX switch cpu-mac to that of your power control XMLs
SW_iPDU_XML = {
    '00e0-fc0f-8c02': {
        'on': {
            iPDU_IP2: './iPDU/Eagle157/set_top_59xx_on2.xml',
            iPDU_IP3: './iPDU/Eagle157/set_top_59xx_on3.xml'
        },
        'off': {
            iPDU_IP2: './iPDU/Eagle157/set_top_59xx_off2.xml',
            iPDU_IP3: './iPDU/Eagle157/set_top_59xx_off3.xml'
        }
    },
    '00e0-fc0f-8c03': {
        'on': {
            iPDU_IP2: './iPDU/Eagle157/set_bottom_59xx_on2.xml',
            iPDU_IP3: './iPDU/Eagle157/set_bottom_59xx_on3.xml'
        },
        'off': {
            iPDU_IP2: './iPDU/Eagle157/set_bottom_59xx_off2.xml',
            iPDU_IP3: './iPDU/Eagle157/set_bottom_59xx_off3.xml'
        }
    }
}
# IRF_DISPLAY_NUMBER is the line number between the top of your 'display irf'
#                    output to the 1st switch data. This should not be change
#                    unless the display irf output change which seem to vary
#                    between 5950 and 5900.
IRF_DISPLAY_NUMBER = 9
# MASTER_IRF_FAILOVER_WAIT is the number of minutes you will keep your Master
#                          IRF down/off.
MASTER_IRF_FAILOVER_WAIT = '12m'
# END_OF_CYCLE_SLEEP is the enc of cycle wait time after the previous master
#                    was brought back up/powered on.
END_OF_CYCLE_SLEEP = '10m'
# ICM_CONFIGURE_WAIT_TIMEOUT should not be required but added in cases where
#                            Potash gets reconfigured. This is the time script
#                            will wait for Potash to transion to Configured
#                            state before failing/timing out.
ICM_CONFIGURE_WAIT_TIMEOUT = '60m'
# Below is the path to your tools/interconnect/scripts and the script we use
# to retrieve OneView credential of Potash
ICM_SCRIPTS_DIR = '/root/ci-fit/5.00/fusion/tests/wpst_crm/\
ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'

# Your enclosure name(s)
ENC_NAME = ['Eag_157_MXQ8200680', 'Eag_158_MXQ8200681']
# Your Potash interconnect names
ICM_NAMES = [ENC_NAME[0] + ', interconnect 3',
             ENC_NAME[1] + ', interconnect 6']

# OV Uplinks to Potash operationalSpeed mapping
OPERATIONAL_SPEED = {
    'Speed100G': 'ethernet',
    'Speed25G': 'ethernet',
    'Speed10G': 'ethernet',
}

# OV Upinks to Potash protocol mapping
LAG_STATES = {
    'LACP': 'LacpActivity'
}

# OV Uplinks to Potash ports mapping
INTERCONNECT_NAME = {
    ICM_NAMES[0]: '0/0',
    ICM_NAMES[1]: '1/0'
}

# OV Uplinks to Potash
TARGET_LI = 'Eag_157_158_159_LE-LIG-ICM-3_6-HA'
TARGET_US = ['BIG-PIPE-ENET', 'Tunnel1', 'PXE']
TARGET_ATTRIBUTES = ['lagId', 'interconnectName', 'portName', 'portStatus',
                     'portStatusReason', 'operationalSpeed', 'lagStates',
                     'uri']

# Expected ports for both OV and Hafnium
EXPECTED_PORTS = [
    'ethernet0/0/1:1(P)', 'ethernet0/0/1:2(P)',
    'ethernet0/0/1:3(P)', 'ethernet0/0/1:4(P)',
    'ethernet1/0/1:1(P)', 'ethernet1/0/1:2(P)',
    'ethernet1/0/1:3(P)', 'ethernet1/0/1:4(P)',
    'ethernet0/0/2(P)', 'ethernet1/0/2(P)',
    'ethernet0/0/3:1(P)', 'ethernet0/0/3:2(P)',
    'ethernet0/0/3:3(P)', 'ethernet0/0/3:4(P)',
    'ethernet1/0/3:1(P)', 'ethernet1/0/3:2(P)',
    'ethernet1/0/3:3(P)', 'ethernet1/0/3:4(P)'
]

# portUri attributes that we care to check for the test
EXPECTED_PORTS_ATTRIBUTES = {
    'portStatus': 'Linked',
    'portStatusReason': 'Active'
}

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
CARBON = 'Virtual Connect SE 32Gb FC Module for Synergy'
POTASH = 'Virtual Connect SE 40Gb F8 Module for Synergy'
NITRO = 'Virtual Connect SE 100Gb F32 Module for Synergy'
HAFNIUM_ICM_MODELS = [POTASH, NITRO]

# Server default credentials
SERVER_USERNAME = 'root'
SERVER_PASSWORD = 'rootpwd'

# MeatGrinder location
MEATGRINDER_DIR = '/root/tools/LinuxMG_2.610_x86-64'

# Sequential ping script
SEQUENTIAL_PING_SCRIPT = '/root/ci-fit/5.00/fusion/tests/wpst_crm/ci_fit/\
tools/tcs/ping_ips_sequential'

# Multipath script
MULTIPATH_SCRIPT = '/root/tools/scripts/check-multipath.sh'

# Expected Common Resource Attributes
# NOTE: We are limited to simple key:value pair. We may consider adding complex
#       structure like list, list of dictionary, etc in the future.
#       The goal for now is to be more granular with how we test resource
#       states.
# ENCLOSURE: Dictionary of enclosures with corresponding attributes to check
#            and the expected values
ENCLOSURES = {
    'Eag_157_MXQ8200680': {
        'state': 'Configured',
        'status': 'OK',
        'refreshState': 'NotRefreshing',
        'enclosureType': 'SY12000',
        'reconfigurationState': 'NotReapplyingConfiguration'
    },
    'Eag_158_MXQ8200681': {
        'state': 'Configured',
        'status': 'OK',
        'refreshState': 'NotRefreshing',
        'enclosureType': 'SY12000',
        'reconfigurationState': 'NotReapplyingConfiguration'
    },
    'Eag_159_MXQ8200682': {
        'state': 'Configured',
        'status': 'OK',
        'refreshState': 'NotRefreshing',
        'enclosureType': 'SY12000',
        'reconfigurationState': 'NotReapplyingConfiguration'
    }
}
#
# TODO: ENCLOSURE_MANAGERS: Dictionary of EMs with expected attributes
#
# LOGICAL_ENCLOSURES: Dictionary of Logical Enclosures with corresponding
#                     attributes to check and the expected values
LOGICAL_ENCLOSURES = {
    'Eag_157_158_159_LE': {
        'state': 'Consistent',
        'status': 'OK',
        'scalingState': 'NotScaling',
        'powerMode': 'RedundantPowerSupply',
        'deleteFailed': False,
        'ambientTemperatureMode': 'Standard'
    }
}
#
# INTERCONNECTS: Dictionary of interconnects attributes and its corresponding
#                expected values
INTERCONNECTS = {
    'Eag_157_MXQ8200680, interconnect 1': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 32Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_32G',
        'networkLoopProtectionInterval': 5,
        'portCount': 28,
        'subPortCount': 0
    },
    'Eag_157_MXQ8200680, interconnect 3': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 100Gb F32 Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'SPEED_50G',
        'networkLoopProtectionInterval': 5,
        'portCount': 44,
        'subPortCount': 8
    },
    'Eag_157_MXQ8200680, interconnect 4': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 32Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_32G',
        'networkLoopProtectionInterval': 5,
        'portCount': 28,
        'subPortCount': 0
    },
    'Eag_157_MXQ8200680, interconnect 6': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'HPE Synergy 50Gb Satellite Link Module',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'SPEED_50G',
        'networkLoopProtectionInterval': 5,
        'portCount': 14,
        'subPortCount': 0
    },
    'Eag_158_MXQ8200681, interconnect 1': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 32Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_32G',
        'networkLoopProtectionInterval': 5,
        'portCount': 28,
        'subPortCount': 0
    },
    'Eag_158_MXQ8200681, interconnect 3': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'HPE Synergy 50Gb Satellite Link Module',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'SPEED_50G',
        'networkLoopProtectionInterval': 5,
        'portCount': 14,
        'subPortCount': 0
    },
    'Eag_158_MXQ8200681, interconnect 4': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 32Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_32G',
        'networkLoopProtectionInterval': 5,
        'portCount': 28,
        'subPortCount': 0
    },
    'Eag_158_MXQ8200681, interconnect 6': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 100Gb F32 Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'SPEED_50G',
        'networkLoopProtectionInterval': 5,
        'portCount': 44,
        'subPortCount': 8
    },
    'Eag_159_MXQ8200682, interconnect 1': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 32Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_32G',
        'networkLoopProtectionInterval': 5,
        'portCount': 28,
        'subPortCount': 0
    },
    'Eag_159_MXQ8200682, interconnect 3': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'HPE Synergy 50Gb Satellite Link Module',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'SPEED_50G',
        'networkLoopProtectionInterval': 5,
        'portCount': 14,
        'subPortCount': 0
    },
    'Eag_159_MXQ8200682, interconnect 4': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'Virtual Connect SE 32Gb FC Module for Synergy',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'Speed_32G',
        'networkLoopProtectionInterval': 5,
        'portCount': 28,
        'subPortCount': 0
    },
    'Eag_159_MXQ8200682, interconnect 6': {
        'state': 'Configured',
        'status': 'OK',
        'powerState': 'On',
        'model': 'HPE Synergy 50Gb Satellite Link Module',
        'deviceResetState': 'Normal',
        'enableFastMacCacheFailover': True,
        'enableIgmpSnooping': False,
        'enableNetworkLoopProtection': True,
        'enablePauseFloodProtection': True,
        'enableRichTLV': False,
        'enableTaggedLldp': False,
        'enclosureType': 'SY12000',
        'igmpIdleTimeoutInterval': 260,
        'maxBandwidth': 'SPEED_50G',
        'networkLoopProtectionInterval': 5,
        'portCount': 14,
        'subPortCount': 0
    },
}
#
# LOGICAL_INTERCONNECTS: Dictionary of logical interconnects attributes
#                        and its corresponding expected values
LOGICAL_INTERCONNECTS = {
    'Eag_157_158_159_LE-LIG-ICM-1_4-HA_TRUNK_32G-1': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'NotApplicable',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    },

    'Eag_157_158_159_LE-LIG-ICM-1_4-HA_TRUNK_16G-2': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'NotApplicable',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    },

    'Eag_157_158_159_LE-LIG-ICM-1_4-HA_TRUNK_16/32G-3': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'NotApplicable',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    },
    'Eag_157_158_159_LE-LIG-ICM-3_6-HA': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        'status': 'OK',
        'stackingHealth': 'BiConnected',
        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    }
}

# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
# CHECK_READONLY = '192.168.1.140 192.168.1.200 172.18.25.2 192.168.1.190
# 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150 192.168.1.158
# 192.168.1.128'

# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
# CHECK_MEATGRINDER = '192.168.1.140 192.168.1.200 172.18.25.2
# 192.168.1.190 192.168.1.252 192.168.1.125 192.168.1.105 192.168.1.150
# 192.168.1.158 192.168.1.128'

# PING_HAFILE: Sequential ping will be run as part of the test using
#              the HA file provided in this variable
# Example from Eagle11 setup:
# PING_HAFILE = '/root/ci-fit/fusion/tests/wpst_crm/ci_fit/
# tools/appliance/d-nct/HA_ipaddr.conf'

# CHECK_MULTIPATH: IPs to check for multipath
# Example from Eagle11 setup:
# CHECK_MULTIPATH = {'192.168.1.140':2, '192.168.1.200':3, '172.18.25.2':4,
#                    '192.168.1.190':4, '192.168.11.103':4,
#                    '192.168.1.125':2, '192.168.1.105':2,
#                    '192.168.1.150':4, '192.168.1.158':4,
#                    '192.168.1.128':4}
# Example from C7000 EST Verizon setup:
# CHECK_MULTIPATH = {
# fit-12
# '172.16.229.154':2, '172.16.228.39':4, '172.16.229.219':2,
# '172.16.229.3':2, '172.16.228.40':2, '172.16.228.241':4,
# '172.16.228.235':2,
# fit-12 bay 7
#        '172.16.229.5':4,
# fit-13
#        '172.16.228.248':2, '172.16.228.194':4, '172.16.228.193':2,
#        '172.16.229.7':4, '172.16.229.9':2, '172.16.228.43':4,
#        '172.16.228.42':2, '172.16.230.43':4, '172.16.230.16':4,
# fit-14
# '172.16.228.250':4, '172.16.228.195':4, '172.16.229.206':4,
# '172.16.229.13':3, '172.16.229.16':4,
#        '172.16.228.201':4, '172.16.228.198':2, '172.16.229.14':1,
#        '172.16.228.199':2, '172.16.229.15':2,
# fit-15
#        '172.16.229.20':4, '172.16.229.22':4, '172.16.229.24':4,
#        '172.16.228.202':4, '172.16.229.26':4, '172.16.228.243':4,
# fit-16
# nothing
# fit-17
# '172.16.229.160':4, '172.16.229.234':3, #'172.16.228.254':4,
# '172.16.229.198':2, fit-17 bay 5 very slow
# '172.16.229.193':4, '172.16.229.236':3, '172.16.229.2':4,
# '172.16.229.199':2,
# '172.16.229.191':4, '172.16.229.238':3, #'172.16.229.11':4,
# '172.16.131.1':4, #'172.16.229.240':3,
# fit-17 bay 15 not going back after hotplug ICM4
# (verizon is not using it so will worrry later)
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

# CHECK_ISS_CRASH: When set to True, it will ssh to Hafnium and check for ISS crash.
# NOTE: This is by default set to True. Thus, to disable this test set this variable to False.
CHECK_ISS_CRASH = True

# !!!! NOTE: This data variable file was written for Eagle11 only !!!!
APPLIANCE_IP = '15.186.9.xx'
# For multiple recipients, use comma-separated.
EMAIL_TO = 'your.email@hpe.com'

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
FORCE_PROFILE_APPLY = 'all'

# MeatGrinder location
MEATGRINDER_DIR = '/root/tools/LinuxMG_2.610_x86-64'

# Sequential ping script
SEQUENTIAL_PING_SCRIPT = '/root/ci-fit/4.10/fusion/tests/wpst_crm/ci_fit/tools/tcs/ping_ips_sequential'

# Multipath script
MULTIPATH_SCRIPT = '/root/tools/scripts/check-multipath.sh'

# Expected Common Resource Attributes
# NOTE: We are limited to simple key:value pair. We may consider adding complex structure like list, list of dictionary, etc in the future.
#       The goal for now is to be more granular with how we test resource states.
# ENCLOSURE: Dictionary of enclosures with corresponding attributes to check and the expected values
ENCLOSURES = {
    'CN744502F3': {
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
    'CN744502F3, interconnect 3': {
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
        'maxBandwidth': 'Speed_20G',
        'networkLoopProtectionInterval': 5,
        'portCount': 42,
        'subPortCount': 8
    },
    'CN744502F3, interconnect 6': {
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
        'maxBandwidth': 'Speed_20G',
        'networkLoopProtectionInterval': 5,
        'portCount': 42,
        'subPortCount': 8
    },
    'CN744502F3, interconnect 1': {
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
    'CN744502F3, interconnect 4': {
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
    'LE-LIG 2': {
        # Known issue OVD2000 LI state is always Unknown
        'state': 'Unknown',
        #        'status': 'OK',
        'stackingHealth': 'BiConnected',
        #        'consistencyStatus': 'CONSISTENT',
        'enclosureType': 'SY12000',
    }
}


# HINT: For ease of collecting these IPs, use tools/tcs/get-pxe-ip.sh
# CHECK_READONLY: IPs to check for readonly FS
# Example from Eagle11 setup:
CHECK_READONLY = '172.16.3.3 172.17.37.2 172.18.25.2 172.19.13.3 172.20.1.3 172.17.37.3 172.16.3.2 172.20.1.2 172.18.25.3 172.19.13.2'
CHECK_READONLY_NO13811_4 = '172.17.37.2 172.20.1.3 172.17.37.3 172.20.1.2 172.19.13.2'
CHECK_READONLY_NO4 = '172.16.3.3 172.17.37.2 172.18.25.2 172.20.1.3 172.17.37.3 172.16.3.2 172.20.1.2 172.18.25.3 172.19.13.2'

# CHECK_MEATGRINDER: IPs to check for error in the latest MeatGrinder log
# Example from Eagle11 setup:
CHECK_MEATGRINDER = '172.16.3.3 172.17.37.2 172.18.25.2 172.19.13.3 172.20.1.3 172.17.37.3 172.16.3.2 172.20.1.2 172.18.25.3 172.19.13.2'
CHECK_MEATGRINDER_NO13811_4 = '172.17.37.2 172.20.1.3 172.17.37.3 172.20.1.2 172.19.13.2'
CHECK_MEATGRINDER_NO4 = '172.16.3.3 172.17.37.2 172.18.25.2 172.20.1.3 172.17.37.3 172.16.3.2 172.20.1.2 172.18.25.3 172.19.13.2'

# PING_HAFILE: Sequential ping will be run as part of the test using the HA file provided in this variable
# Example from Eagle11 setup:
PING_HAFILE = '/root/ci-fit/4.10/fusion/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr.conf'
PING_HAFILE_NO13811_4 = '/root/ci-fit/4.10/fusion/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr_no13811_4.conf'
PING_HAFILE_NO4 = '/root/ci-fit/4.10/fusion/tests/wpst_crm/ci_fit/tools/appliance/d-nct/HA_ipaddr_nobay4.conf'

# CHECK_MULTIPATH: IPs to check for multipath
# Example from Eagle11 setup:
CHECK_MULTIPATH = {
    # bay1
    '172.16.3.3': 2,
    # bay2
    '172.17.37.2': 2,
    # bay3
    '172.18.25.2': 4,
    # bay4
    '172.19.13.3': 4,
    # bay5
    '172.20.1.3': 4,
    # bay7
    '172.17.37.3': 2,
    # bay8
    '172.16.3.2': 2,
    # bay10
    '172.20.1.2': 4,
    # bay11
    '172.18.25.3': 4,
    # bay12
    '172.19.13.2': 4
}

CHECK_MULTIPATH_NO13811_4 = {
    # bay1
    # '172.16.3.3': 2,
    # bay2
    '172.17.37.2': 2,
    # bay3
    # '172.18.25.2': 4,
    # bay4
    # '172.19.13.3': 4,
    # bay5
    '172.20.1.3': 4,
    # bay7
    '172.17.37.3': 2,
    # bay8
    # '172.16.3.2': 2,
    # bay10
    '172.20.1.2': 4,
    # bay11
    # '172.18.25.3': 4,
    # bay12
    '172.19.13.2': 4
}
CHECK_MULTIPATH_NO13811_4_LESS1FC = {
    # bay1
    # '172.16.3.3': 2,
    # bay2
    '172.17.37.2': 1,
    # bay3
    # '172.18.25.2': 4,
    # bay4
    # '172.19.13.3': 4,
    # bay5
    '172.20.1.3': 3,
    # bay7
    '172.17.37.3': 1,
    # bay8
    # '172.16.3.2': 2,
    # bay10
    '172.20.1.2': 3,
    # bay11
    # '172.18.25.3': 4,
    # bay12
    '172.19.13.2': 4
}
CHECK_MULTIPATH_NO4 = {
    # bay1
    '172.16.3.3': 2,
    # bay2
    '172.17.37.2': 2,
    # bay3
    '172.18.25.2': 4,
    # bay4
    # '172.19.13.3': 4,
    # bay5
    '172.20.1.3': 4,
    # bay7
    '172.17.37.3': 2,
    # bay8
    '172.16.3.2': 2,
    # bay10
    '172.20.1.2': 4,
    # bay11
    '172.18.25.3': 4,
    # bay12
    '172.19.13.2': 4
}
CHECK_MULTIPATH_NO4_LESS1FCOE = {
    # bay1
    '172.16.3.3': 1,
    # bay2
    '172.17.37.2': 2,
    # bay3
    '172.18.25.2': 3,
    # bay4
    # '172.19.13.3': 4,
    # bay5
    '172.20.1.3': 4,
    # bay7
    '172.17.37.3': 2,
    # bay8
    '172.16.3.2': 1,
    # bay10
    '172.20.1.2': 4,
    # bay11
    '172.18.25.3': 3,
    # bay12
    '172.19.13.2': 4
}
CHECK_MULTIPATH_NO13811_4_LESS1BAY2 = {
    # bay1
    # '172.16.3.3': 2,
    # bay2
    '172.17.37.2': 1,
    # bay3
    # '172.18.25.2': 4,
    # bay4
    # '172.19.13.3': 4,
    # bay5
    '172.20.1.3': 4,
    # bay7
    '172.17.37.3': 2,
    # bay8
    # '172.16.3.2': 2,
    # bay10
    '172.20.1.2': 4,
    # bay11
    # '172.18.25.3': 4,
    # bay12
    '172.19.13.2': 4
}

# deletedConnectionBody = {
#    'allocatedMbps': 2500,
#    'allocatedVFs': None,
#    'boot': {'priority': 'NotBootable'},
#    'functionType': 'FibreChannel',
#    'id': 2,
#    'interconnectUri': '/rest/interconnects/3bfa24d3-522f-44e1-a1f7-711ead01db85',
#    'ipv4': None,
#    'lagName': None,
#    'mac': 'B2:99:99:00:00:08',
#    'macType': 'Virtual',
#    'managed': True,
#    'maximumMbps': 10000,
#    'name': '2',
#    'networkName': None,
#    'networkUri': '/rest/fc-networks/6fc3a636-7e7e-4385-aa38-568588cb7c2a',
#    'portId': 'Mezz 3:1-b',
#    'requestedMbps': '2500',
#    'requestedVFs': None,
#    'state': 'Deployed',
#    'status': 'OK',
#    'wwnn': '10:00:16:11:00:00:00:05',
#    'wwpn': '10:00:16:11:00:00:00:04',
#    'wwpnType': 'Virtual'
# }

ICM_SCRIPTS_DIR = '/root/ci-fit/fusion-4.00/tests/wpst_crm/ci_fit/tools/interconnect/scripts'
ICM_PASSWD_SCRIPT = 'get-icm-passwd.sh'
ENC_NAME = 'CN744502F3'
ICM3 = ENC_NAME + ', interconnect 3'
ICM6 = ENC_NAME + ', interconnect 6'
ICM_NAMES = [ICM3, ICM6]
TARGET_LI = 'LE-LIG 2'
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
SPP_UPLOAD_WAIT_TIMEOUT = '60m'
SPP_UPLOAD_WAIT_INTERVAL = '2s'
END_OF_CYCLE_WAIT = '15m'
SPP_UPLOAD_WAIT_TIMEOUT = '30m'
SPP_UPLOAD_WAIT_INTERVAL = '2s'
SERVER_POWEROFF_WAIT_TIMEOUT = '30m'
SERVER_POWEROFF_WAIT_INTERVAL = '15s'
SERVER_POWERON_WAIT_TIMEOUT = '45m'
SERVER_POWERON_WAIT_INTERVAL = '30s'
TOGGLE_UPLINK_WAIT_TIMEOUT = '30m'
TOGGLE_UPLINK_WAIT_INTERVAL = '15s'
FW_UPDATE_WAIT_TIMEOUT = '30m'
FW_UPDATE_WAIT_INTERVAL = '1m'
STACKING_LINK_WAIT_TIMEOUT = '60m'
STACKING_LINK_WAIT_INTERVAL = '30s'
STACKING_SLEEP = '2m'
EDIT_UPLINK_SETS_SLEEP = '2m'
TOGGLE_UPLINK_PORT_SLEEP = '2m'
CREATE_US_WAIT_TIMEOUT = '90m'
CREATE_US_WAIT_INTERVAL = '15s'
DELETE_NETWORK_WAIT_TIMEOUT = '4m'
DELETE_NETWORK_WAIT_INTERVAL = '2s'
DELETE_PROFILES_WAIT_TIMEOUT = '300m'
DELETE_PROFILES_WAIT_INTERVAL = '10s'
CREATE_FC_NETWORK_NAME_SIDEA = 'SAN-A-FA-WB'
CREATE_FC_NETWORK_NAME_SIDEB = 'SAN-B-FA-WB'
CREATE_FC_NETWORKS = [
    {'name': CREATE_FC_NETWORK_NAME_SIDEA, 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'},
    {'name': CREATE_FC_NETWORK_NAME_SIDEB, 'type': 'fc-networkV4', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'connectionTemplateUri': None, 'managedSanUri': None, 'fabricType': 'FabricAttach'}
]
CREATE_UPLINK_SETS_FC = [{"type": "uplink-setV4", "name": CREATE_FC_NETWORK_NAME_SIDEA,
                          "networkUris": [],
                          "portConfigInfos":[{"desiredSpeed": "Auto",
                                              "location": {"locationEntries": [{"value": "Q1:1",
                                                                                "type": "Port"},
                                                                               {"value": "3",
                                                                                "type": "Bay"},
                                                                               # NOTE: Change this to the URI or your enclosure
                                                                               {"value": "/rest/enclosures/000000" + ENC_NAME,
                                                                                "type": "Enclosure"}
                                                                               ]
                                                           }
                                              }],
                          "networkType": "FibreChannel",
                          "primaryPortLocation": None,
                          "reachability": "Reachable",
                          "manualLoginRedistributionState": "Supported",
                          "logicalInterconnectUri": TARGET_LI,
                          "connectionMode": "Auto",
                          "lacpTimer": None,
                          "nativeNetworkUri": None,
                          "fcNetworkUris": [CREATE_FC_NETWORK_NAME_SIDEA],
                          "fcoeNetworkUris":[],
                          "state": None,
                          "description": None,
                          "uri": None,
                          "category": "logical-interconnects",
                          "ethernetNetworkType": "NotApplicable"},
                         {"type": "uplink-setV4", "name": CREATE_FC_NETWORK_NAME_SIDEB,
                          "networkUris": [],
                          "portConfigInfos":[{"desiredSpeed": "Auto",
                                              "location": {"locationEntries": [{"value": "Q5:1",
                                                                                "type": "Port"},
                                                                               {"value": "6",
                                                                                "type": "Bay"},
                                                                               # NOTE: Change this to the URI or your enclosure
                                                                               {"value": "/rest/enclosures/000000" + ENC_NAME,
                                                                                "type": "Enclosure"}
                                                                               ]
                                                           }
                                              }],
                          "networkType": "FibreChannel",
                          "primaryPortLocation": None,
                          "reachability": "Reachable",
                          "manualLoginRedistributionState": "Supported",
                          "logicalInterconnectUri": TARGET_LI,
                          "connectionMode": "Auto",
                          "lacpTimer": None,
                          "nativeNetworkUri": None,
                          "fcNetworkUris": [CREATE_FC_NETWORK_NAME_SIDEB],
                          "fcoeNetworkUris":[],
                          "state": None,
                          "description": None,
                          "uri": None,
                          "category": "logical-interconnects",
                          "ethernetNetworkType": "NotApplicable"}
                         ]

FCOE_NETWORK_NAME_SIDEA = 'FCOE-3093-A'
UPLINK_SETS_FCOE_SIDEA = 'FCoE-A'
FCOE_NETWORK_NAME_SIDEB = 'FCOE-3094-B'
UPLINK_SETS_FCOE_SIDEB = 'FCoE-B'
UPLINK_SETS_FCOE_RESTOREPORT_SIDEA = [{"type": "uplink-setV4", "name": UPLINK_SETS_FCOE_SIDEA,
                                       "networkUris": [],
                                       "portConfigInfos":[{"desiredSpeed": "Auto",
                                                           "location": {"locationEntries": [{"value": "Q4:1",
                                                                                             "type": "Port"},
                                                                                            {"value": "3",
                                                                                             "type": "Bay"},
                                                                                            # NOTE: Change this to the URI or your enclosure
                                                                                            {"value": "/rest/enclosures/000000" + ENC_NAME,
                                                                                             "type": "Enclosure"}
                                                                                            ]
                                                                        }
                                                           }],
                                       "networkType": "Ethernet",
                                       "primaryPortLocation": None,
                                       "reachability": "Reachable",
                                       "manualLoginRedistributionState": "NotSupported",
                                       "logicalInterconnectUri": TARGET_LI,
                                       "connectionMode": "Auto",
                                       "lacpTimer": "Short",
                                       "nativeNetworkUri": None,
                                       "fcNetworkUris": [],
                                       "fcoeNetworkUris":[FCOE_NETWORK_NAME_SIDEA],
                                       "state": None,
                                       "description": None,
                                       "uri": None,
                                       "category": "logical-interconnects",
                                       "ethernetNetworkType": "Tagged"}
                                      ]

UPLINK_SETS_FCOE_RESTOREPORT_SIDEB = [{"type": "uplink-setV4", "name": UPLINK_SETS_FCOE_SIDEB,
                                       "networkUris": [],
                                       "portConfigInfos":[{"desiredSpeed": "Auto",
                                                           "location": {"locationEntries": [{"value": "Q4:1",
                                                                                             "type": "Port"},
                                                                                            {"value": "6",
                                                                                             "type": "Bay"},
                                                                                            # NOTE: Change this to the URI or your enclosure
                                                                                            {"value": "/rest/enclosures/000000" + ENC_NAME,
                                                                                             "type": "Enclosure"}
                                                                                            ]
                                                                        }
                                                           }],
                                       "networkType": "Ethernet",
                                       "primaryPortLocation": None,
                                       "reachability": "Reachable",
                                       "manualLoginRedistributionState": "NotSupported",
                                       "logicalInterconnectUri": TARGET_LI,
                                       "connectionMode": "Auto",
                                       "lacpTimer": "Short",
                                       "nativeNetworkUri": None,
                                       "fcNetworkUris": [],
                                       "fcoeNetworkUris":[FCOE_NETWORK_NAME_SIDEB],
                                       "state": None,
                                       "description": None,
                                       "uri": None,
                                       "category": "logical-interconnects",
                                       "ethernetNetworkType": "Tagged"}
                                      ]

UPLINK_SETS_FCOE_NOPORT_SIDEA = [{"type": "uplink-setV4", "name": UPLINK_SETS_FCOE_SIDEA,
                                  "networkUris": [],
                                  "portConfigInfos": [],
                                  "networkType": "Ethernet",
                                  "primaryPortLocation": None,
                                  "reachability": "Reachable",
                                  "manualLoginRedistributionState": "NotSupported",
                                  "logicalInterconnectUri": TARGET_LI,
                                  "connectionMode": "Auto",
                                  "lacpTimer": "Short",
                                  "nativeNetworkUri": None,
                                  "fcNetworkUris": [],
                                  "fcoeNetworkUris":[FCOE_NETWORK_NAME_SIDEA],
                                  "state": None,
                                  "description": None,
                                  "uri": None,
                                  "category": "logical-interconnects",
                                  "ethernetNetworkType": "Tagged"},
                                 ]

UPLINK_SETS_FCOE_NOPORT_SIDEB = [
    {"type": "uplink-setV4", "name": UPLINK_SETS_FCOE_SIDEB,
     "networkUris": [],
     "portConfigInfos": [],
     "networkType": "Ethernet",
     "primaryPortLocation": None,
     "reachability": "Reachable",
     "manualLoginRedistributionState": "NotSupported",
     "logicalInterconnectUri": TARGET_LI,
     "connectionMode": "Auto",
     "lacpTimer": "Short",
     "nativeNetworkUri": None,
     "fcNetworkUris": [],
     "fcoeNetworkUris": [FCOE_NETWORK_NAME_SIDEB],
     "state": None,
     "description": None,
     "uri": None,
     "category": "logical-interconnects",
                 "ethernetNetworkType": "Tagged"}
]

FC_UPLINK_PORT_SIDEA = "Q3:1"
FC_NETWORK_NAME_SIDEA = "SAN-A-FA"
FC_UPLINK_PORT_SIDEB = "Q3:1"
FC_NETWORK_NAME_SIDEB = "SAN-B-FA"
UPLINK_SETS_FC_NOPORT_SIDEA = [{"type": "uplink-setV4", "name": FC_NETWORK_NAME_SIDEA,
                                "networkUris": [],
                                "portConfigInfos": [],
                                "networkType": "FibreChannel",
                                "primaryPortLocation": None,
                                "reachability": "Reachable",
                                "manualLoginRedistributionState": "Supported",
                                "logicalInterconnectUri": TARGET_LI,
                                "connectionMode": "Auto",
                                "lacpTimer": None,
                                "nativeNetworkUri": None,
                                "fcNetworkUris": [FC_NETWORK_NAME_SIDEA],
                                "fcoeNetworkUris":[],
                                "state": None,
                                "description": None,
                                "uri": None,
                                "category": "logical-interconnects",
                                "ethernetNetworkType": "NotApplicable"},
                               ]

UPLINK_SETS_FC_RESTOREPORT_SIDEA = [
    {"type": "uplink-setV4", "name": FC_NETWORK_NAME_SIDEA,
     "networkUris": [],
     "portConfigInfos":[{"desiredSpeed": "Auto",
                         "location": {"locationEntries": [{"value": FC_UPLINK_PORT_SIDEA,
                                                           "type": "Port"},
                                                          {"value": "3",
                                                           "type": "Bay"},
                                                          # NOTE: Change this to the URI or your enclosure
                                                          {"value": "/rest/enclosures/000000" + ENC_NAME,
                                                           "type": "Enclosure"}
                                                          ]
                                      }
                         }],
     "networkType": "FibreChannel",
     "primaryPortLocation": None,
     "reachability": "Reachable",
     "manualLoginRedistributionState": "Supported",
     "logicalInterconnectUri": TARGET_LI,
     "connectionMode": "Auto",
     "lacpTimer": None,
     "nativeNetworkUri": None,
     "fcNetworkUris": [FC_NETWORK_NAME_SIDEA],
     "fcoeNetworkUris":[],
     "state": None,
     "description": None,
     "uri": None,
     "category": "logical-interconnects",
     "ethernetNetworkType": "NotApplicable"},
]

UPLINK_SETS_FC_NOPORT_SIDEB = [
    {"type": "uplink-setV4", "name": FC_NETWORK_NAME_SIDEB,
     "networkUris": [],
     "portConfigInfos": [],
     "networkType": "FibreChannel",
     "primaryPortLocation": None,
     "reachability": "Reachable",
     "manualLoginRedistributionState": "Supported",
     "logicalInterconnectUri": TARGET_LI,
     "connectionMode": "Auto",
     "lacpTimer": None,
     "nativeNetworkUri": None,
     "fcNetworkUris": [FC_NETWORK_NAME_SIDEB],
     "fcoeNetworkUris":[],
     "state": None,
     "description": None,
     "uri": None,
     "category": "logical-interconnects",
                 "ethernetNetworkType": "NotApplicable"}
]

UPLINK_SETS_FC_RESTOREPORT_SIDEB = [
    {"type": "uplink-setV4", "name": FC_NETWORK_NAME_SIDEB,
     "networkUris": [],
     "portConfigInfos":[{"desiredSpeed": "Auto",
                         "location": {"locationEntries": [{"value": FC_UPLINK_PORT_SIDEB,
                                                           "type": "Port"},
                                                          {"value": "6",
                                                           "type": "Bay"},
                                                          # NOTE: Change this to the URI or your enclosure
                                                          {"value": "/rest/enclosures/000000" + ENC_NAME,
                                                           "type": "Enclosure"}
                                                          ]
                                      }
                         }],
     "networkType": "FibreChannel",
     "primaryPortLocation": None,
     "reachability": "Reachable",
     "manualLoginRedistributionState": "Supported",
     "logicalInterconnectUri": TARGET_LI,
     "connectionMode": "Auto",
     "lacpTimer": None,
     "nativeNetworkUri": None,
     "fcNetworkUris": [FC_NETWORK_NAME_SIDEB],
     "fcoeNetworkUris":[],
     "state": None,
     "description": None,
     "uri": None,
     "category": "logical-interconnects",
                 "ethernetNetworkType": "NotApplicable"}
]

# Delete FC profile connection and recreate the connection variables
PROFILE_TO_EDIT = ENC_NAME + '_bay2'
CONNECTION_ID_EDIT_NEGATIVE = 2
CONNECTION_ID_EDIT = 3
POST_DELETE_PROFILE_CONNECTION_SLEEP = '15m'

# Update FC profile connection
PROFILE_TO_UPDATE = ENC_NAME + '_bay7'
CONNECTION_ID_UPDATE = 3

# Disable FC uplink port (side a)
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

# Disable FC uplink port (side b)
FC_UPLINK_SET_SIDEB = FC_NETWORK_NAME_SIDEB
DISABLE_FC_UPLINK_SIDEB = {
    "associatedUplinkSetUri": FC_UPLINK_SET_SIDEB,
    "interconnectName": ICM_NAMES[1],
    "portType": "Uplink",
    # NOTE: change this to your ICM's {id}
    "portId": "7e868d0e-18a7-486e-8224-ba2318348a7d:%s" % FC_UPLINK_PORT_SIDEB,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["FibreChannel"],
    "enabled": False,
    "portName": FC_UPLINK_PORT_SIDEB,
    "portStatus": "Linked",
    "type": "port"
}

# Enable FC uplink port
ENABLE_FC_UPLINK_SIDEB = {
    "associatedUplinkSetUri": FC_UPLINK_SET_SIDEB,
    "interconnectName": ICM_NAMES[1],
    "portType": "Uplink",
    # NOTE: change this to your ICM's {id}
    "portId": "7e868d0e-18a7-486e-8224-ba2318348a7d:%s" % FC_UPLINK_PORT_SIDEB,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["FibreChannel"],
    "enabled": True,
    "portName": FC_UPLINK_PORT_SIDEB,
    "portStatus": "Linked",
    "type": "port"
}

DELETE_CREATE_PROFILE_BAY = 11
SERVER_PROFILE_TO_BAY_MAP = {
    ENC_NAME + '_bay1': ENC_NAME + ', bay 1',
    ENC_NAME + '_bay2': None,
    ENC_NAME + '_bay3': ENC_NAME + ', bay 3',
    ENC_NAME + '_bay4': None,
    ENC_NAME + '_bay5': None,
    ENC_NAME + '_bay6': None,
    ENC_NAME + '_bay7': None,
    ENC_NAME + '_bay8': ENC_NAME + ', bay 8',
    ENC_NAME + '_bay9': None,
    ENC_NAME + '_bay10': None,
    ENC_NAME + '_bay11': ENC_NAME + ', bay 11',
    ENC_NAME + '_bay12': None,
}
SERVER_PROFILES_NOHW = [
    # NOTE: serialNumberType has to be UserDefined, mac, wwpn, and wwnn static.
    # NOTE: Make sure they are not in the Virtual range on your setup data variable because we are statically assigning it here.
    {'type': 'ServerProfileV9', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG 1', 'serialNumberType': 'UserDefined', 'serialNumber': 'VCUTTT0000', 'uuid': 'c60af6bf-c5ca-4f4e-9585-8eff8fa8eacc', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': ENC_NAME + '_bay1', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings': {
         'connections': [
             {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:00', 'wwpn': '', 'wwnn': ''},
             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3093-A', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '22110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:01', 'wwpn': '10:00:16:11:00:00:00:00', 'wwnn': '10:00:16:11:00:00:00:01'},
             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3094-B', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '23110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:02', 'wwpn': '10:00:16:11:00:00:00:02', 'wwnn': '10:00:16:11:00:00:00:03'},
             {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:03', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:04', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:05', 'wwpn': '', 'wwnn': ''},
             {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:06', 'wwpn': '', 'wwnn': ''},
         ]
     }},
    {'type': 'ServerProfileV9', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG 1', 'serialNumberType': 'UserDefined', 'serialNumber': 'VCUTTT0002', 'uuid': '0630c604-31fc-41a8-a181-3ed2743a735c', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CN744502F3_bay3', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings': {
         'connections': [
             {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:0E', 'wwpn': '', 'wwnn': ''},
             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3093-A', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:0F', 'wwpn': '10:00:16:11:00:00:00:08', 'wwnn': '10:00:16:11:00:00:00:09'},
             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3094-B', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:10', 'wwpn': '10:00:16:11:00:00:00:0a', 'wwnn': '10:00:16:11:00:00:00:0b'},
             {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:11', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:12', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:13', 'wwpn': '', 'wwnn': ''},
             {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:14', 'wwpn': '', 'wwnn': ''},
             {'id': 8, 'name': '8', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:SAN-A-3-1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '22110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:15', 'wwpn': '10:00:16:11:00:00:00:0c', 'wwnn': '10:00:16:11:00:00:00:0d'},
             {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:SAN-B-4-1', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '23110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:16', 'wwpn': '10:00:16:11:00:00:00:0e', 'wwnn': '10:00:16:11:00:00:00:0f'},
         ]
     }},
    {'type': 'ServerProfileV9', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG 1', 'serialNumberType': 'UserDefined', 'serialNumber': 'VCUTTT0007', 'uuid': '820e8fe0-4138-497d-b1e2-ed5566039ae4', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CN744502F3_bay8', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings': {
         'connections': [
             {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:37', 'wwpn': '', 'wwnn': ''},
             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3093-A', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '22110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:38', 'wwpn': '10:00:16:11:00:00:00:20', 'wwnn': '10:00:16:11:00:00:00:21'},
             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3094-B', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '23110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:39', 'wwpn': '10:00:16:11:00:00:00:22', 'wwnn': '10:00:16:11:00:00:00:23'},
             {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:3A', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:3B', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:3C', 'wwpn': '', 'wwnn': ''},
             {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'ETH:Tunnel1', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:3D', 'wwpn': '', 'wwnn': ''},
         ]
     }},
    {'type': 'ServerProfileV9', 'serverHardwareUri': None,
     'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG 1', 'serialNumberType': 'UserDefined', 'serialNumber': 'VCUTTT000A', 'uuid': '66d7d4e2-a1bd-4d82-bc13-a42d2360b14a', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': 'CN744502F3_bay11', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings': {
         'connections': [
             {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:4E', 'wwpn': '', 'wwnn': ''},
             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3093-A', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:4F', 'wwpn': '10:00:16:11:00:00:00:2c', 'wwnn': '10:00:16:11:00:00:00:2d'},
             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3094-B', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:50', 'wwpn': '10:00:16:11:00:00:00:2e', 'wwnn': '10:00:16:11:00:00:00:2f'},
             {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:51', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:52', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:53', 'wwpn': '', 'wwnn': ''},
             {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:54', 'wwpn': '', 'wwnn': ''},
             {'id': 8, 'name': '8', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:SAN-A-3-1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '22110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:55', 'wwpn': '10:00:16:11:00:00:00:30', 'wwnn': '10:00:16:11:00:00:00:31'},
             {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:SAN-B-4-1', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '23110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:56', 'wwpn': '10:00:16:11:00:00:00:32', 'wwnn': '10:00:16:11:00:00:00:33'},
         ]
     }},
]

DELETE_CREATE_PROFILE = [
    {'type': 'ServerProfileV9', 'serverHardwareUri': ENC_NAME + ', bay 11',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_NAME, 'enclosureGroupUri': 'EG:EG 1', 'serialNumberType': 'UserDefined', 'serialNumber': 'VCUTTT000A', 'uuid': '66d7d4e2-a1bd-4d82-bc13-a42d2360b14a', 'macType': 'Virtual', 'wwnType': 'Virtual', 'name': ENC_NAME + '_bay11', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
     'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '', 'forceInstallFirmware': False, 'firmwareInstallType': None},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics':True,
     'iscsiInitiatorName':'',
     'osDeploymentSettings':None,
     'connectionSettings': {
         'connections': [
             {'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:IC', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:4E', 'wwpn': '', 'wwnn': ''},
             {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3093-A', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:4F', 'wwpn': '10:00:16:11:00:00:00:2c', 'wwnn': '10:00:16:11:00:00:00:2d'},
             {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b', 'requestedMbps': '2500', 'networkUri': 'FCOE:FCOE-3094-B', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:50', 'wwpn': '10:00:16:11:00:00:00:2e', 'wwnn': '10:00:16:11:00:00:00:2f'},
             {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:51', 'wwpn': '', 'wwnn': ''},
             {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk4', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:52', 'wwpn': '', 'wwnn': ''},
             {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:53', 'wwpn': '', 'wwnn': ''},
             {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'requestedMbps': '2500', 'networkUri': 'NS:VlanTrunk5', 'boot': {'priority': 'NotBootable'}, 'mac': 'B2:99:99:00:00:54', 'wwpn': '', 'wwnn': ''},
             {'id': 8, 'name': '8', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:1', 'requestedMbps': 'Auto', 'networkUri': 'FC:SAN-A-3-1', 'boot': {'priority': 'Primary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '22110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:55', 'wwpn': '10:00:16:11:00:00:00:30', 'wwnn': '10:00:16:11:00:00:00:31'},
             {'id': 9, 'name': '9', 'functionType': 'FibreChannel', 'portId': 'Mezz 1:2', 'requestedMbps': 'Auto', 'networkUri': 'FC:SAN-B-4-1', 'boot': {'priority': 'Secondary', 'bootVolumeSource': 'UserDefined', 'targets': [{'arrayWwpn': '23110002AC00326A', 'lun': '0'}]}, 'mac': 'B2:99:99:00:00:56', 'wwpn': '10:00:16:11:00:00:00:32', 'wwnn': '10:00:16:11:00:00:00:33'},
         ]
     }},
]

# Disable FCoE uplink port (side a)
FCOE_UPLINK_PORT_SIDEA = "Q4:1"
FCOE_UPLINK_SET_SIDEA = "FCoE-A"
DISABLE_FCOE_UPLINK_SIDEA = {
    "associatedUplinkSetUri": FCOE_UPLINK_SET_SIDEA,
    "interconnectName": ICM_NAMES[0],
    "portType": "Uplink",
    "portId": "319ef9a0-eb56-41c6-98be-27ea869537b7:%s" % FCOE_UPLINK_PORT_SIDEA,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["Ethernet", "EnetFcoe"],
    "enabled": False,
    "portName": FCOE_UPLINK_PORT_SIDEA,
    "portStatus": "Linked",
    "type": "port"
}

# Enable FCoE uplink port
ENABLE_FCOE_UPLINK_SIDEA = {
    "associatedUplinkSetUri": FCOE_UPLINK_SET_SIDEA,
    "interconnectName": ICM_NAMES[0],
    "portType": "Uplink",
    "portId": "319ef9a0-eb56-41c6-98be-27ea869537b7:%s" % FCOE_UPLINK_PORT_SIDEA,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["Ethernet", "EnetFcoe"],
    "enabled": True,
    "portName": FCOE_UPLINK_PORT_SIDEA,
    "portStatus": "Linked",
    "type": "port"
}

# Disable FCoE uplink port (side b)
FCOE_UPLINK_PORT_SIDEB = "Q4:1"
FCOE_UPLINK_SET_SIDEB = "FCoE-B"
DISABLE_FCOE_UPLINK_SIDEB = {
    "associatedUplinkSetUri": FCOE_UPLINK_SET_SIDEB,
    "interconnectName": ICM_NAMES[1],
    "portType": "Uplink",
    "portId": "37818749-e7db-4e22-ab19-6c691155fd2c:%s" % FCOE_UPLINK_PORT_SIDEB,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["Ethernet", "EnetFcoe"],
    "enabled": False,
    "portName": FCOE_UPLINK_PORT_SIDEB,
    "portStatus": "Linked",
    "type": "port"
}

# Enable FCoE uplink port
ENABLE_FCOE_UPLINK_SIDEB = {
    "associatedUplinkSetUri": FCOE_UPLINK_SET_SIDEB,
    "interconnectName": ICM_NAMES[1],
    "portType": "Uplink",
    "portId": "37818749-e7db-4e22-ab19-6c691155fd2c:%s" % FCOE_UPLINK_PORT_SIDEB,
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["Ethernet", "EnetFcoe"],
    "enabled": True,
    "portName": FCOE_UPLINK_PORT_SIDEB,
    "portStatus": "Linked",
    "type": "port"
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

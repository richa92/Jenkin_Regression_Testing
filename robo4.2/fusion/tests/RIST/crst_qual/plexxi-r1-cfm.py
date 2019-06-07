from Common import *  # local import from .\Common.py
from copy import deepcopy
import os.path
import json


def rlist(start, end, prefix='Net_', suffix='', exclude=[]):
    rlist = []
    for x in xrange(start, end + 1):
        if x in exclude:
            continue
        rlist.append(prefix + str(x) + suffix)
    return rlist


# Need to decide on a naming convention.  I have CAPS and non_caps
# which FABRIC_NAME
FABRIC_NAME = "Plexxi-r1"
DOMAIN = "vse.rdlabs.hpecorp.net"
OV_HOSTNAME = "OV-%s.%s" % (FABRIC_NAME, DOMAIN)
CFM = "%s-cfm.%s" % (FABRIC_NAME, DOMAIN)
DL_HOSTNAME_PREFIX = "plexr1"

# Feature Toggles expected enabled/disabled.  These will be confirmed to
# be enable (true) or disabled (false)
FEATURE_TOGGLES = [
    "false:OVF6484_Composable_Rack_Plexxi_Switch_3eq",
    "true:OVF6385_Composable_Rack_Plexxi_Switch_3ex"]
# If FEATURE_TOGGLES are not correct and IF FEATURE_TOGGLES_COMMAND is
# defined then the command will be executed
# FEATURE_TOGGLES_COMMAND = "/ci/bin/set-feature-toggles -d OVF6484_Composable_Rack_Plexxi_Switch_3eq -e OVF6385_Composable_Rack_Plexxi_Switch_3ex"

# Plexxi Switches
PLEXXI_SWITCH_PROMPT_REGEX = "%s-[12]" % FABRIC_NAME.lower()
PLEXXI_SWITCH_CHASSISIDS = {
    "%s-1" % FABRIC_NAME.lower(): 'E0:39:D7:84:21:80',
    "%s-2" % FABRIC_NAME.lower(): 'E0:39:D7:84:27:00'
}
PLEXXI_SWITCH_NAMES = [
    "%s-1" % FABRIC_NAME.lower(),
    "%s-2" % FABRIC_NAME.lower()
]
PLEXXI_SWITCH_FQDN = [
    "%s-1.%s" % (FABRIC_NAME.lower(), DOMAIN),
    "%s-2.%s" % (FABRIC_NAME.lower(), DOMAIN)
]
PLEXXI_SWITCH_TYPE = "Composable Fabric FM 3180"
# Used when confirming Plexxi ports.  We only check Access Ports for
# profile connections
PLEXXI_LAST_ACCESS_PORT = 40

# This defines the file where switch data is obtained.  This is used to create CONFIRM_SWITCHES below.
# The file is obtained using a simple GET on /rest/switches and saved to (for example): Plexxi-r1-switches_master.txt
# This is an idea in action.  This is only good for testing static environments.  Which is what I think the Qual
# Rings are going to be.  This confirms the switch environment as not changed.
# Once the file is obtained via a GET, then it should be manually evaluated (1 time) for correct expectation.
OV_SWITCHES_FILE = "%s-switches_master.txt" % FABRIC_NAME

PLEXXI_SWITCHES_CREDENTIALS = {
    '1': {
        'hostname': PLEXXI_SWITCH_FQDN[0],
        'username': 'admin',
        'password': 'plexxi'
    },
    '2': {
        'hostname': PLEXXI_SWITCH_FQDN[1],
        'username': 'admin',
        'password': 'plexxi'
    }
}

# Plexxi Fabric request bodies
#    :List of dictionary of request bodies
PLEXXI_FABRICS = [
    {
        "host": PLEXXI_SWITCHES_CREDENTIALS['1']['hostname'],
        "name": FABRIC_NAME,
        "description": "Plexxi Qual on FABRIC_NAME: %s" % FABRIC_NAME
    }
]

# LOGICAL SWITCH GROUP, LOGICAL SWITCH
LSG_NAME = 'LSG_%s' % FABRIC_NAME
LS_NAME = "LS_Qual_%s" % FABRIC_NAME

# Base Resources and DL
BULK_VLANIdRange_1 = "3-1000"
BULK_VLANIdRange_2 = "1001-1500"

WIN_NS_NAME = 'win-netset'
WIN_NS_START = 1
WIN_NS_STOP = 32
WIN_NS_VLANS = WIN_NS_STOP - WIN_NS_START  # native_vlan removed from range
WIN_NS_RANGE = "1, 3-%s" % WIN_NS_STOP
WIN_NS_PORT = 3     # which ports should used on CFM
WIN_NS_PORT_EDIT = 2

LINUX_NS_NAME = 'linux-netset-1k'
LINUX_NS_START = 1
LINUX_NS_STOP = 1000
LINUX_NS_VLANS = LINUX_NS_STOP - LINUX_NS_START
LINUX_NS_PORT = 2
LINUX_NS_PORT_EDIT = 1
LINUX_NS_RANGE = "1, 3-%s" % LINUX_NS_STOP

DL_ADD_STATUS = "REGEX:OK|Warning"
DL_SERVER_IP_RANGE = "16.114.213.170-16.114.213.173"
DL_SERVER_IPs = ["16.114.213.170",
                 "16.114.213.171",
                 "16.114.213.172",
                 "16.114.213.173"]

DL_SP_NAMES = [
    "DL1-windows-net2",
    "DL2-linux-netset",
    "DL3-windows-netset",
    "DL4-linux-net5"
]

DL_SP_EDIT_NAMES = [
    "DL1-now-linux-netset",
    "DL2-now-windows-netset",
    "DL3-now-linux-net5",
    "DL4-now-windows-net2",
]

DL_SP_DESC = [
    "Qual Profile for DL 1",
    "Qual Profile for DL 2",
    "Qual Profile for DL 3",
    "Qual Profile for DL 4"
]

# Prefix for Support Dump name
SD_PREFIX = "qual-r1"

# Used to generate DL Hostnames.  Expects them to be sequentially named.
first_dl = 1
last_dl = 4
DL_SERVER_NAMES = [
    "%s-dl10-%d" %
    (DL_HOSTNAME_PREFIX,
     n) for n in xrange(
        first_dl,
        last_dl +
        1)]


DL_SHORT_MODEL = "DL360 Gen10"
DL_SERVER_FQDN = ["%s.%s" % (name, DOMAIN) for name in DL_SERVER_NAMES]

# Networks
ETHERNET_NETWORKS = [
    {'name': 'Net_1',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'Net_2',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 2,
     'purpose': 'Management',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

BULK_ETHERNET_NETWORKS = [
    {"vlanIdRange": BULK_VLANIdRange_1,
     "namePrefix": "Net",
     "privateNetwork": False,
     "smartLink": True,
     "purpose": "General",
     "type": BULK_ETHERNET_NETWORK_TYPE,
     "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500}
     },
    {"vlanIdRange": BULK_VLANIdRange_2,
     "namePrefix": "Net",
     "privateNetwork": False,
     "smartLink": True,
     "purpose": "General",
     "type": BULK_ETHERNET_NETWORK_TYPE,
     "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500}
     }
]

NETWORK_SETS = [
    {'name': WIN_NS_NAME,
     'type': NETWORK_SET_TYPE,
     'networkUris': rlist(WIN_NS_START, WIN_NS_STOP),
     'nativeNetworkUri': "Net_2"
     },
    {'name': LINUX_NS_NAME,
     'type': NETWORK_SET_TYPE,
     'networkUris': rlist(LINUX_NS_START, LINUX_NS_STOP),
     'nativeNetworkUri': "Net_2",
     'networkSetType': 'Large'
     }
]

# DL Rack Servers
RACKSERVERS = [
    {
        "name": DL_SERVER_NAMES[0],
        "hostname": DL_SERVER_FQDN[0],
        "username": ILO_CREDENTIALS['username'],
        "password": ILO_CREDENTIALS['password'],
        "force": True,
        "licensingIntent": "OneViewNoiLO",
        "configurationState": "Managed",
        # "initialScopeUris": ["Scope:Test"]
    },
    {
        "name": DL_SERVER_NAMES[1],
        "hostname": DL_SERVER_FQDN[1],
        "username": ILO_CREDENTIALS['username'],
        "password": ILO_CREDENTIALS['password'],
        "force": True,
        "licensingIntent": "OneViewNoiLO",
        "configurationState": "Managed",
        # "initialScopeUris": ["Scope:Test"]
    },
    {
        "name": DL_SERVER_NAMES[2],
        "hostname": DL_SERVER_FQDN[2],
        "username": ILO_CREDENTIALS['username'],
        "password": ILO_CREDENTIALS['password'],
        "force": True,
        "licensingIntent": "OneViewNoiLO",
        "configurationState": "Managed",
        # "initialScopeUris": ["Scope:Test"]
    },
    {
        "name": DL_SERVER_NAMES[3],
        "hostname": DL_SERVER_FQDN[3],
        "username": ILO_CREDENTIALS['username'],
        "password": ILO_CREDENTIALS['password'],
        "force": True,
        "licensingIntent": "OneViewNoiLO",
        "configurationState": "Managed",
        # "initialScopeUris": ["Scope:Test"]
    }
]

RACK_SERVER_RANGES = {
    "mpHostsAndRanges": [DL_SERVER_IP_RANGE],
    "username": ILO_CREDENTIALS['username'],
    "password": ILO_CREDENTIALS['password'],
    "licensingIntent": "OneViewNoiLO",
    "configurationState": "Managed",
    "initialScopeUris": []
}

RACK_SERVER_LIST = {
    "mpHostsAndRanges": DL_SERVER_FQDN,
    "username": ILO_CREDENTIALS['username'],
    "password": ILO_CREDENTIALS['password'],
    "licensingIntent": "OneViewNoiLO",
    "configurationState": "Managed",
    "initialScopeUris": []
}

EXPECTED_RACK_SERVERS = [
    {
        "name": DL_SERVER_FQDN[0],
        "licensingIntent": "OneViewNoiLO",
        "shortModel": DL_SHORT_MODEL,
        "status": DL_ADD_STATUS,
        "type": SERVER_HARDWARE_TYPE,
    },
    {
        "name": DL_SERVER_FQDN[1],
        "licensingIntent": "OneViewNoiLO",
        "shortModel": DL_SHORT_MODEL,
        "status": DL_ADD_STATUS,
        "type": SERVER_HARDWARE_TYPE
    },
    {
        "name": DL_SERVER_FQDN[2],
        "licensingIntent": "OneViewNoiLO",
        "shortModel": DL_SHORT_MODEL,
        "status": DL_ADD_STATUS,
        "type": SERVER_HARDWARE_TYPE,
    },
    {
        "name": DL_SERVER_FQDN[3],
        "licensingIntent": "OneViewNoiLO",
        "shortModel": DL_SHORT_MODEL,
        "status": DL_ADD_STATUS,
        "type": SERVER_HARDWARE_TYPE,
    }
]

# Build CONFIRM_SWITCHES{}
# Execute a GET on /rest/switches (using PostMan or similar) and save to FABRIC_NAME-switches_master.txt
# For example: Plexxi-r1-switches.txt
if os.path.exists(OV_SWITCHES_FILE):
    with open(OV_SWITCHES_FILE, "r") as switches_file:
        switch_string = switches_file.read()
    switch_json = json.loads(switch_string)

    CONFIRM_SWITCHES = []
    CONFIRM_SWITCH = {}
    for switch in switch_json["members"]:
        CONFIRM_SWITCH["name"] = switch["name"]
        CONFIRM_SWITCH["state"] = "Configured"
        CONFIRM_SWITCH["status"] = "OK"
        CONFIRM_SWITCH["foreignStatus"] = "SYNCED"
        CONFIRM_SWITCH["modelName"] = PLEXXI_SWITCH_TYPE
        CONFIRM_SWITCH["chassisId"] = PLEXXI_SWITCH_CHASSISIDS[switch["name"]]
        CONFIRM_SWITCH["switchMAC"] = PLEXXI_SWITCH_CHASSISIDS[switch["name"]]
        CONFIRM_SWITCH["ports"] = switch["ports"]
        # remove these items as they are dynamic
        for port in CONFIRM_SWITCH["ports"]:
            del port["uri"]
            del port["portId"]
            if port["neighbor"] is not None:
                del port["neighbor"]["linkUri"]
                if int(port["name"]) <= len(DL_SERVER_FQDN):
                    port["neighbor"]["linkLabel"] = "REGEX:(%s|%s)" % (DL_SERVER_FQDN[int(port["name"]) - 1], DL_SERVER_IPs[int(port["name"]) - 1])
                    port["neighbor"]["remoteSystemName"] = "REGEX:HPE Eth 10\/25Gb 2p 631FLR-SFP28 Adptr fw_version:.*$"

        CONFIRM_SWITCHES.append(CONFIRM_SWITCH)
        CONFIRM_SWITCH = {}

LSG = {
    'name': LSG_NAME,
    'type': 'logical-switch-groupV4',
    'switchMapTemplate': {
            'switchMapEntryTemplates': [
                {
                    'logicalLocation': {
                        'locationEntries': [
                            {
                                'relativeValue': 1,
                                'type': 'StackingMemberId'
                            }
                        ]
                    },
                    'permittedSwitchTypeUri': 'SWT:' + PLEXXI_SWITCH_TYPE
                },
                {
                    'logicalLocation': {
                        'locationEntries': [
                            {
                                'relativeValue': 2,
                                'type': 'StackingMemberId'
                            }
                        ]
                    },
                    'permittedSwitchTypeUri': 'SWT:' + PLEXXI_SWITCH_TYPE
                }
            ]
    }
}

LS = {
    "logicalSwitch": {
        "name": LS_NAME,
        "state": "Active",
        "status": None,
        "type": "logical-switchV5",
        "managementLevel": "BASIC_MANAGED",
        "logicalSwitchGroupUri": "LSG:" + LSG_NAME,
        "switchCredentialConfiguration": [
                {
                    "snmpV1Configuration": {
                        "communityString": "public"
                    },
                    "snmpV3Configuration": {
                        "authorizationProtocol": None,
                        "privacyProtocol": None,
                        "securityLevel": None
                    },
                    "logicalSwitchManagementHost": PLEXXI_SWITCHES_CREDENTIALS['1']['hostname'],
                    "snmpVersion": "SNMPv1",
                    "snmpPort": 161
                }
        ],
        # name of switches, script will find their appropriate uris by name
        "switchUris": ["SW:" + PLEXXI_SWITCH_NAMES[0], "SW:" + PLEXXI_SWITCH_NAMES[1]]
    },
    "logicalSwitchCredentials": [
        {
            "connectionProperties": [
                {
                    "propertyName": "SshBasicAuthCredentialUser",
                    "value": PLEXXI_SWITCHES_CREDENTIALS['1']['username'],
                    "valueFormat": "Unknown",
                    "valueType": "String"
                },
                {
                    "propertyName": "SshBasicAuthCredentialPassword",
                    "value": PLEXXI_SWITCHES_CREDENTIALS['1']['password'],
                    "valueFormat": "SecuritySensitive",
                    "valueType": "String"
                }
            ]
        }
    ]
}

SERVER_PROFILES_ONE = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": DL_SP_NAMES[0],
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[0],
        "serverHardwareTypeUri": SHTypes[0],
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "description": DL_SP_DESC[0],
        "affinity": None,
        "connectionSettings": {
            "connections": [{
                "id": 2,
                "name": "Conn_1",
                "functionType": "Ethernet",
                "portId": "Flr 1:1",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_2",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 3,
                "name": "Conn_2",
                "functionType": "Ethernet",
                "portId": "Flr 1:2",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_2",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }]
        },
        "boot": {
            "manageBoot": False
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "secureBoot": "Unmanaged",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{
                "logicalDrives": [{
                    "name": "Raid_0_LS",
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": 1,
                    "driveTechnology": None,
                    "sasLogicalJBODId": None,
                    "driveNumber": None,
                    "accelerator": "Unmanaged"
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged"
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": DL_SP_NAMES[1],
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[1],
        "serverHardwareTypeUri": SHTypes[0],
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "description": DL_SP_DESC[1],
        "affinity": None,
        "connectionSettings": {
            "connections": [{
                "id": 2,
                "name": "Conn_1",
                "functionType": "Ethernet",
                "portId": "Flr 1:1",
                "requestedMbps": 0,
                "networkUri": "NS:%s" % LINUX_NS_NAME,
                "lagName": "LAG1",
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 3,
                "name": "Conn_2",
                "functionType": "Ethernet",
                "portId": "Flr 1:2",
                "requestedMbps": 0,
                "networkUri": "NS:%s" % LINUX_NS_NAME,
                "lagName": "LAG1",
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }]
        },
        "boot": {
            "manageBoot": False
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "secureBoot": "Unmanaged",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{
                "logicalDrives": [{
                    "name": "Raid_1_LS",
                    "raidLevel": "RAID1",
                    "bootable": False,
                    "numPhysicalDrives": 2,
                    "driveTechnology": None,
                    "sasLogicalJBODId": None,
                    "driveNumber": None,
                    "accelerator": "Unmanaged"
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged"
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    }
]

CONFIRM_SERVER_PROFILES_ONE = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": DL_SP_NAMES[0],
        "description": DL_SP_DESC[0],
        "serialNumber": "MXQ8240585",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverProfileTemplateUri": None,
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[0],
        "serverHardwareTypeUri": SHTypes[0],
        "macType": "Physical",
        "wwnType": "Physical",
        "serialNumberType": "Physical",
        "status": "OK",
        "state": "Normal",
        "serverHardwareReapplyState": "NotApplying",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": [
                {
                    "id": 2,
                    "name": "Conn_1",
                    "functionType": "Ethernet",
                    "networkUri": "ETH:Net_2",
                    "portId": "Flr 1:1",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:25:50",
                },
                {
                    "id": 3,
                    "name": "Conn_2",
                    "functionType": "Ethernet",
                    "networkUri": "ETH:Net_2",
                    "portId": "Flr 1:2",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:25:58",
                }
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Unmanaged"
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
            "reapplyState": "NotApplying"
        },
        "managementProcessor": {
            "reapplyState": "NotApplying",
            "manageMp": False,
            "mpSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "deviceSlot": "Embedded",
                    "mode": "Mixed",
                    "initialize": False,
                    "importConfiguration": False,
                    "driveWriteCache": "Unmanaged",
                    "predictiveSpareRebuild": "Unmanaged",
                    "logicalDrives": [
                            {
                                "name": "Raid_0_LS",
                                "raidLevel": "RAID0",
                                "bootable": False,
                                "numPhysicalDrives": 1,
                                "driveTechnology": None,
                                "sasLogicalJBODId": None,
                                "accelerator": "Unmanaged",
                                "numSpareDrives": None,
                                "driveNumber": 1
                            }
                    ]
                }
            ],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying"
        },
        "osDeploymentSettings": {
            "osDeploymentPlanUri": None,
            "osVolumeUri": None,
            "forceOsDeployment": False,
            "osCustomAttributes": [],
            "reapplyState": "NotApplying"
        },
        "refreshState": "NotRefreshing"
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": DL_SP_NAMES[1],
        "description": DL_SP_DESC[1],
        "serialNumber": "MXQ82405J3",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[1],
        "serverHardwareTypeUri": SHTypes[0],
        "hideUnusedFlexNics": None,
        "macType": "Physical",
        "wwnType": "Physical",
        "serialNumberType": "Physical",
        "status": "OK",
        "state": "Normal",
        "serverHardwareReapplyState": "NotApplying",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": [
                {
                    "id": 2,
                    "name": "Conn_1",
                    "functionType": "Ethernet",
                    "networkUri": "NS:%s" % LINUX_NS_NAME,
                    "portId": "Flr 1:1",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:3F:30",
                },
                {
                    "id": 3,
                    "name": "Conn_2",
                    "functionType": "Ethernet",
                    "networkUri": "NS:%s" % LINUX_NS_NAME,
                    "portId": "Flr 1:2",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:3F:38",
                }
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Unmanaged"
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
            "reapplyState": "NotApplying"
        },
        "managementProcessor": {
            "reapplyState": "NotApplying",
            "manageMp": False,
            "mpSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "deviceSlot": "Embedded",
                    "mode": "Mixed",
                    "initialize": False,
                    "importConfiguration": False,
                    "driveWriteCache": "Unmanaged",
                    "predictiveSpareRebuild": "Unmanaged",
                    "logicalDrives": [
                            {
                                "name": "Raid_1_LS",
                                "raidLevel": "RAID1",
                                "bootable": False,
                                "numPhysicalDrives": 2,
                                "driveTechnology": None,
                                "sasLogicalJBODId": None,
                                "accelerator": "Unmanaged",
                                "numSpareDrives": None,
                                "driveNumber": 1
                            }
                    ]
                }
            ],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying"
        },
        "osDeploymentSettings": {
            "osDeploymentPlanUri": None,
            "osVolumeUri": None,
            "forceOsDeployment": False,
            "osCustomAttributes": [],
            "reapplyState": "NotApplying"
        },
        "refreshState": "NotRefreshing"
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": DL_SP_NAMES[2],
        "description": DL_SP_DESC[2],
        "serialNumber": "MXQ824058S",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverProfileTemplateUri": None,
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[2],
        "serverHardwareTypeUri": SHTypes[0],
        "macType": "Physical",
        "wwnType": "Physical",
        "serialNumberType": "Physical",
        "status": "OK",
        "state": "Normal",
        "serverHardwareReapplyState": "NotApplying",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": [
                {
                    "id": 2,
                    "name": "Conn_1",
                    "functionType": "Ethernet",
                    "networkUri": "NS:%s" % WIN_NS_NAME,
                    "portId": "Flr 1:1",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:41:20",
                },
                {
                    "id": 3,
                    "name": "Conn_2",
                    "functionType": "Ethernet",
                    "networkUri": "NS:%s" % WIN_NS_NAME,
                    "portId": "Flr 1:2",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:41:28",
                }
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Unmanaged"
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
            "reapplyState": "NotApplying"
        },
        "managementProcessor": {
            "reapplyState": "NotApplying",
            "manageMp": False,
            "mpSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "deviceSlot": "Embedded",
                    "mode": "Mixed",
                    "initialize": False,
                    "importConfiguration": False,
                    "driveWriteCache": "Unmanaged",
                    "predictiveSpareRebuild": "Unmanaged",
                    "logicalDrives": [
                        {
                            "name": "Raid_0_LS",
                            "raidLevel": "RAID0",
                            "bootable": False,
                            "numPhysicalDrives": 1,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "accelerator": "Unmanaged",
                            "numSpareDrives": None,
                            "driveNumber": 1
                        }
                    ]
                }
            ],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying"
        },
        "osDeploymentSettings": {
            "osDeploymentPlanUri": None,
            "osVolumeUri": None,
            "forceOsDeployment": False,
            "osCustomAttributes": [],
            "reapplyState": "NotApplying"
        },
        "refreshState": "NotRefreshing"
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": DL_SP_NAMES[3],
        "description": DL_SP_DESC[3],
        "serialNumber": "MXQ8240589",
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[3],
        "serverHardwareTypeUri": SHTypes[0],
        "hideUnusedFlexNics": None,
        "macType": "Physical",
        "wwnType": "Physical",
        "serialNumberType": "Physical",
        "status": "OK",
        "state": "Normal",
        "serverHardwareReapplyState": "NotApplying",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": [
                {
                    "id": 2,
                    "name": "Conn_1",
                    "functionType": "Ethernet",
                    "networkUri": "ETH:Net_5",
                    "portId": "Flr 1:1",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:8B:D0",
                },
                {
                    "id": 3,
                    "name": "Conn_2",
                    "functionType": "Ethernet",
                    "networkUri": "ETH:Net_5",
                    "portId": "Flr 1:2",
                    "macType": "Physical",
                    "mac": "9C:DC:71:B8:8B:D8",
                }
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto",
            "secureBoot": "Unmanaged"
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
            "reapplyState": "NotApplying"
        },
        "managementProcessor": {
            "reapplyState": "NotApplying",
            "manageMp": False,
            "mpSettings": []
        },
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [
                {
                    "deviceSlot": "Embedded",
                    "mode": "Mixed",
                    "initialize": False,
                    "importConfiguration": False,
                    "driveWriteCache": "Unmanaged",
                    "predictiveSpareRebuild": "Unmanaged",
                    "logicalDrives": [
                        {
                            "name": "Raid_1_LS",
                            "raidLevel": "RAID1",
                            "bootable": False,
                            "numPhysicalDrives": 2,
                            "driveTechnology": None,
                            "sasLogicalJBODId": None,
                            "accelerator": "Unmanaged",
                            "numSpareDrives": None,
                            "driveNumber": 1
                        }
                    ]
                }
            ],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying"
        },
        "osDeploymentSettings": {
            "osDeploymentPlanUri": None,
            "osVolumeUri": None,
            "forceOsDeployment": False,
            "osCustomAttributes": [],
            "reapplyState": "NotApplying"
        },
        "refreshState": "NotRefreshing"
    }
]

# we first build a dict of access ports where they are all not used.  Then replace those that are filled.
# this way we can use Fusion Api Validate Response Follow to confirm both
# used and notused ports.
CONFIRM_PLEXXI_PORTS_ONE = {
    "result": []
}
CONFIRM_PLEXXI_PORTS_EMPTY = {
    "result": []
}

used_plexxi_ports = {
    1: {
        "native_vlan": 2,
        "vlans": ""
    },
    2: {
        "native_vlan": 2,
        "vlans": "1, 3-%d" % LINUX_NS_STOP
    },
    3: {
        "native_vlan": 2,
        "vlans": "1, 3-%d" % WIN_NS_STOP
    },
    4: {
        "native_vlan": 5,
        "vlans": ""
    }
}

for port in xrange(1, PLEXXI_LAST_ACCESS_PORT + 1):

    for switch in PLEXXI_SWITCH_NAMES:
        template = {
            "native_vlan": 0,
            "vlans": "",
            "port_label": "%s" % port,
            "switch_name": "%s" % switch
        }
        CONFIRM_PLEXXI_PORTS_EMPTY["result"].append(deepcopy(template))
        if port in used_plexxi_ports:
            template["native_vlan"] = used_plexxi_ports[port]["native_vlan"]
            template["vlans"] = used_plexxi_ports[port]["vlans"]

        CONFIRM_PLEXXI_PORTS_ONE["result"].append(deepcopy(template))

# Negative Profiles start
neg_server_profiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "windows-360",
        "serverHardwareUri": "SH:%s" % DL_SERVER_FQDN[0],
        "serverHardwareTypeUri": SHTypes[0],
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "description": "Neg Profile for DL 1",
        "affinity": None,
        "connectionSettings": {
            "connections": [{
                "id": 2,
                "name": "Conn_1",
                "functionType": "Ethernet",
                "portId": "Flr 1:1",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_2",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 3,
                "name": "Conn_2",
                "functionType": "Ethernet",
                "portId": "Flr 1:2",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_2",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 4,
                "name": "Conn_3",
                "functionType": "Ethernet",
                "portId": "Flr 1:1",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_5",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 5,
                "name": "Conn_4",
                "functionType": "Ethernet",
                "portId": "Flr 1:2",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_5",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }]
        },
        "boot": {
            "manageBoot": False
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "secureBoot": "Unmanaged",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{
                "logicalDrives": [{
                    "name": "Raid_0_LS",
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": 1,
                    "driveTechnology": None,
                    "sasLogicalJBODId": None,
                    "driveNumber": None,
                    "accelerator": "Unmanaged"
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged"
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    }
]

SERVER_PROFILES_NEG_ONE = [
    {
        'keyword': 'Add Server Profile',
        'argument': neg_server_profiles[0].copy(),
        'taskState': 'Error',
        'errorMessage': 'DUPLICATE_PORT_CONNECTION'
    }
]

UNASSIGNED_SERVER_PROFILES_ONE = [
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "Unassigned_1",
        "description": "",
        "serialNumber": None,
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareUri": None,
        "serverHardwareTypeUri": SHTypes[0],
        "affinity": None,
        "associatedServer": None,
        "hideUnusedFlexNics": None,
        "firmware": {
                "firmwareBaselineUri": None,
                "manageFirmware": False,
                "forceInstallFirmware": False,
                "firmwareInstallType": None,
                "firmwareScheduleDateTime": None,
                "firmwareActivationType": None,
                "reapplyState": "NotApplying"
        },
        "macType": "Physical",
        "wwnType": "Physical",
        "serialNumberType": "Physical",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": []
        },
        "bootMode": {
            "manageMode": False,
            "mode": None,
            "pxeBootPolicy": None,
            "secureBoot": "Unmanaged"
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
            "reapplyState": "NotApplying"
        }, "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying"
        },
        "osDeploymentSettings": {
            "osDeploymentPlanUri": None,
            "osVolumeUri": None,
            "forceOsDeployment": False,
            "osCustomAttributes": [],
            "reapplyState": "NotApplying"
        },
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "Unassigned_2",
        "description": "",
        "serialNumber": None,
        "iscsiInitiatorNameType": "AutoGenerated",
        "serverHardwareUri": None,
        "serverHardwareTypeUri": SHTypes[0],
        "affinity": None,
        "associatedServer": None,
        "hideUnusedFlexNics": None,
        "firmware": {
                "firmwareBaselineUri": None,
                "manageFirmware": False,
                "forceInstallFirmware": False,
                "firmwareInstallType": None,
                "firmwareScheduleDateTime": None,
                "firmwareActivationType": None,
                "reapplyState": "NotApplying"
        },
        "macType": "Physical",
        "wwnType": "Physical",
        "serialNumberType": "Physical",
        "connectionSettings": {
            "reapplyState": "NotApplying",
            "connections": []
        },
        "bootMode": {
            "manageMode": False,
            "mode": None,
            "pxeBootPolicy": None,
            "secureBoot": "Unmanaged"
        },
        "boot": {
            "manageBoot": False,
            "order": []
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [],
            "reapplyState": "NotApplying"
        }, "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [],
            "reapplyState": "NotApplying"
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": [],
            "sanSystemCredentials": [],
            "reapplyState": "NotApplying"
        },
        "osDeploymentSettings": {
            "osDeploymentPlanUri": None,
            "osVolumeUri": None,
            "forceOsDeployment": False,
            "osCustomAttributes": [],
            "reapplyState": "NotApplying"
        },
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "Unassigned_3",
        "serverHardwareUri": None,
        "serverHardwareTypeUri": SHTypes[0],
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "description": DL_SP_DESC[2],
        "affinity": None,
        "connectionSettings": {
            "connections": [{
                "id": 2,
                "name": "Conn_1",
                "functionType": "Ethernet",
                "portId": "Flr 1:1",
                "requestedMbps": 0,
                "networkUri": "NS:%s" % WIN_NS_NAME,
                "lagName": "LAG1",
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 3,
                "name": "Conn_2",
                "functionType": "Ethernet",
                "portId": "Flr 1:2",
                "requestedMbps": 0,
                "networkUri": "NS:%s" % WIN_NS_NAME,
                "lagName": "LAG1",
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }]
        },
        "boot": {
            "manageBoot": False
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "secureBoot": "Unmanaged",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{
                "logicalDrives": [{
                    "name": "Raid_0_LS",
                    "raidLevel": "RAID0",
                    "bootable": False,
                    "numPhysicalDrives": 1,
                    "driveTechnology": None,
                    "sasLogicalJBODId": None,
                    "driveNumber": None,
                    "accelerator": "Unmanaged"
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged"
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "name": "Unassigned_4",
        "serverHardwareUri": None,
        "serverHardwareTypeUri": SHTypes[0],
        "serialNumberType": "Physical",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Physical",
        "wwnType": "Physical",
        "description": DL_SP_DESC[3],
        "affinity": None,
        "connectionSettings": {
            "connections": [{
                "id": 2,
                "name": "Conn_1",
                "functionType": "Ethernet",
                "portId": "Flr 1:1",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_5",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }, {
                "id": 3,
                "name": "Conn_2",
                "functionType": "Ethernet",
                "portId": "Flr 1:2",
                "requestedMbps": 0,
                "networkUri": "ETH:Net_5",
                "lagName": None,
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "ipv4": {}
            }]
        },
        "boot": {
            "manageBoot": False
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "secureBoot": "Unmanaged",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": []
        },
        "managementProcessor": {
            "manageMp": False,
            "mpSettings": []
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": [{
                "logicalDrives": [{
                    "name": "Raid_1_LS",
                    "raidLevel": "RAID1",
                    "bootable": False,
                    "numPhysicalDrives": 2,
                    "driveTechnology": None,
                    "sasLogicalJBODId": None,
                    "driveNumber": None,
                    "accelerator": "Unmanaged"
                }],
                "deviceSlot": "Embedded",
                "mode": "Mixed",
                "initialize": True,
                "importConfiguration": False,
                "driveWriteCache": "Unmanaged"
            }]
        },
        "sanStorage": None,
        "initialScopeUris": []
    }
]

ASSIGN_SERVER_PROFILES_ONE = [
    {
        "name": UNASSIGNED_SERVER_PROFILES_ONE[2]["name"],
        "newName": DL_SP_NAMES[2],
        "serverHardware": "SH:%s" % DL_SERVER_FQDN[2],
    },
    {
        "name": UNASSIGNED_SERVER_PROFILES_ONE[3]["name"],
        "newName": DL_SP_NAMES[3],
        "serverHardware": "SH:%s" % DL_SERVER_FQDN[3],
    }
]

EXPECTED_LAGS = {
    DL_SP_NAMES[1]: {
        "description": "Created and Managed by OneView",
        "mlag": True,
        "name": "OV-_PROFILE_UUID_-LAG1",
        "native_vlan": 2,
        "type": "provisioned",
        "vlans": LINUX_NS_RANGE
    },
    DL_SP_NAMES[2]: {
        "description": "Created and Managed by OneView",
        "mlag": True,
        "name": "OV-_PROFILE_UUID_-LAG1",
        "native_vlan": 2,
        "type": "provisioned",
        "vlans": WIN_NS_RANGE
    }
}

EXPECTED_LAGS_EDIT = {
    DL_SP_EDIT_NAMES[0]: {
        "description": "Created and Managed by OneView",
        "mlag": True,
        "name": "OV-_PROFILE_UUID_-LAG1",
        "native_vlan": 2,
        "type": "provisioned",
        "vlans": LINUX_NS_RANGE
    },
    DL_SP_EDIT_NAMES[1]: {
        "description": "Created and Managed by OneView",
        "mlag": True,
        "name": "OV-_PROFILE_UUID_-LAG1",
        "native_vlan": 2,
        "type": "provisioned",
        "vlans": WIN_NS_RANGE
    }
}

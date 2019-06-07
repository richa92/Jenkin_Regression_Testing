"""
F248_US38249 feature
"""

# pylint: disable=E0401,E0602

from robot.libraries.BuiltIn import BuiltIn
from dto import *
from env_variables import *
from copy import deepcopy

try:
    TEST_RING = BuiltIn().get_variable_value("${X_TEST_RING}")
except:  # noqa
    TEST_RING = 'DCS'

FUSION_IP = APPLIANCE_VIP
CREDENTIALS = deepcopy(admin_credentials)
FUSION_USERNAME = CREDENTIALS['userName']    # Fusion Appliance Username
FUSION_PASSWORD = CREDENTIALS['password']         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

# ports
DownLinkPort = 'd5'
UpLinkPort = 'Q4:1'

# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3

# Sas Interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

enclosures = [
    {"type": "EnclosureV400", "name": ENC1},
    {"type": "EnclosureV400", "name": ENC2},
    {"type": "EnclosureV400", "name": ENC3}
]

ics = [
    {"name": ENC1ICBAY3},
    {"name": ENC1ICBAY6},
    {"name": ENC2ICBAY3},
    {"name": ENC2ICBAY6},
    {"name": ENC3ICBAY3},
    {"name": ENC3ICBAY6}
]
ethernet_networks = [
    {
        'name': 'net100',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 100,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'
    },
    {
        'name': 'net300',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 300,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'
    }
]
icmap = [
    {
        'bay': 3,
        'enclosure': 1,
        'type': POTASH,
        'enclosureIndex': 1
    },
    {
        'bay': 6,
        'enclosure': 2,
        'type': POTASH,
        'enclosureIndex': 2
    },
    {
        'bay': 6,
        'enclosure': 1,
        'type': CHLORIDE20,
        'enclosureIndex': 1
    },
    {
        'bay': 3,
        'enclosure': 2,
        'type': CHLORIDE20,
        'enclosureIndex': 2
    },
    {
        'bay': 3,
        'enclosure': 3,
        'type': CHLORIDE20,
        'enclosureIndex': 3
    },
    {
        'bay': 6,
        'enclosure': 3,
        'type': CHLORIDE20,
        'enclosureIndex': 3
    },
]

uplink_sets = {
    'us_untagged': {
        'name': 'us-untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-untagged'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
            {
                'enclosure': '2',
                'bay': '6',
                'port': 'Q1.1',
                'speed': 'Auto'
            },
        ]
    },
    'us_tagged': {
        'name': 'us-tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net100', 'net300'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
            {
                'enclosure': '2',
                'bay': '6',
                'port': 'Q2.1',
                'speed': 'Auto'
            },
        ]
    },
    'us_tunnel': {
        'name': 'us-tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['network-tunnel'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
            {
                'enclosure': '2',
                'bay': '6',
                'port': 'Q3.1',
                'speed': 'Auto'
            },
        ]
    },
}

ligs = [
    {
        'name': LIG_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(),
                       uplink_sets['us_tunnel'].copy(), ],
    }
]

sasligs = [
    {
        "name": 'SASLIG1',  # Dual SAS switch
        "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
        "enclosureType": "SY12000",
        "enclosureIndexes": [1],
        "interconnectBaySet": "1",
        'interconnectMapTemplate': [
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 1,
                'type': NATASHA
            },
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': NATASHA}]
    }
]

egs = [
    {
        'name': 'EG1',
        'type': 'EnclosureGroupV300',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 3,
        'configurationScript': None,
        'interconnectBayMappings': [
            {"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:LIG1"
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:LIG1"
            }
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
    }
]

les = [
    {
        'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
    }
]

potash_on = [
    {"name": ENC1ICBAY3, "uri": "IC:" + ENC1ICBAY3, "powerState": "On"}]
potash_on_configured = [
    {"name": ENC1ICBAY3, "uri": "IC:" + ENC1ICBAY3, "state": "Configured"}]
potash_off = [
    {"name": ENC1ICBAY3, "uri": "IC:" + ENC1ICBAY3, "powerState": "Off"}]

disable_uplink = {
    "associatedUplinkSetUri": "FA-path1",
    "interconnectName": ENC1ICBAY3,
    "portType": "Uplink",
    "portId": "Q4:1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": INTERCONNECT_PORT_TYPE
}

disable_downlink = {
    "associatedUplinkSetUri": "us-untagged",
    "interconnectName": ENC1ICBAY3,
    "portType": "Downlink",
    "portId": "d5",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": DownLinkPort,
    "portStatus": "Linked",
    "type": INTERCONNECT_PORT_TYPE
}

enable_uplink = {
    "associatedUplinkSetUri": "FA-path1",
    "interconnectName": ENC1ICBAY3,
    "portType": "Uplink",
    "portId": "Q4:1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": INTERCONNECT_PORT_TYPE
}

enable_downlink = {
    "associatedUplinkSetUri": "us-untagged",
    "interconnectName": ENC1ICBAY3,
    "portType": "Downlink",
    "portId": "d5",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": True,
    "portName": DownLinkPort,
    "portStatus": "Linked",
    "type": INTERCONNECT_PORT_TYPE
}

server_profiles = [
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
        'serverHardwareTypeUri': 'SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 3',
        'description': '',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': [
                {
                    'id': 1,
                    'name': 'network-untagged',
                    'functionType': 'Ethernet',
                    'portId': 'Auto',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:network-untagged',
                    'mac': None,
                    'wwpn': None,
                    'wwnn': None,
                    'requestedVFs': '0',
                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'FA1',
                    'functionType': 'FibreChannel',
                    'portId': 'Auto',
                    'requestedMbps': '2500',
                    'networkUri': 'FC:FA1',
                    'mac': None,
                    'wwpn': None,
                    'wwnn': None,
                    'ipv4': {}
                }
            ]
        },
        'boot': None,
        'bootMode': {'manageMode': False},
        'firmware': {
            'manageFirmware': False, 'firmwareBaselineUri': '',
            'forceInstallFirmware': False, 'firmwareInstallType': None,
            'firmwareScheduleDateTime': ''
        },
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorName': '',
        'osDeploymentSettings': None,
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': None
    },
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
        'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 5',
        'description': '',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': [
                {
                    'id': 1,
                    'name': 'untagged',
                    'functionType': 'Ethernet',
                    'portId': 'Auto',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:network-untagged',
                    'mac': None,
                    'wwpn': None,
                    'wwnn': None,
                    'requestedVFs': '0',
                    'ipv4': {}
                },
                {
                    'id': 2,
                    'name': 'tunnel',
                    'functionType': 'Ethernet',
                    'portId': 'Auto',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:network-tunnel',
                    'mac': None,
                    'wwpn': None,
                    'wwnn': None,
                    'requestedVFs': '0',
                    'ipv4': {}
                }
            ]
        },
        'boot': None,
        'bootMode': {'manageMode': False},
        'firmware': {
            'manageFirmware': False, 'firmwareBaselineUri': '',
            'forceInstallFirmware': False, 'firmwareInstallType': None,
            'firmwareScheduleDateTime': ''
        },
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorName': '',
        'osDeploymentSettings': None,
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        'sanStorage': None
    },
]

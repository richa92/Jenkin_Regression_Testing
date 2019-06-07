from dto import *
from env_variables import *

ENC_NAME = "CN744502CL"
FLM_IPv6 = ["fe80::1658:d0ff:fe41:4308", "fe80::1658:d0ff:fe41:53b0"]
FRAME = ENC_NAME

LIG_NAME = ENC_NAME + "_LIG"
EG_NAME = ENC_NAME + "_EG"
LE_NAME = ENC_NAME + "_LE"

SERVER_NAME = "CN744502CL, bay 1"
ILO_IP = "16.114.222.42"
PROFILE_NAME = ENC_NAME + "_bay_1_profile"

# Tbird10  CN744502CL
ENC_IPv6 = "fe80::1658:d0ff:fe41:53b0"

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
    {'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
    {
        'bay': 6,
        'enclosure': 1,
        'type': POTASH,
        'enclosureIndex': 1
    }
]

lig = [
    {
        "enclosureIndexes": [
            1
        ],
        "description": None,
        "telemetryConfiguration": {
            "description": None,
            "sampleCount": 12,
            "enableTelemetry": True,
            "sampleInterval": 300,
            "type": "telemetry-configuration",
            "name": None
        },
        "internalNetworkUris": [],
        "name": LIG_NAME,
        "uplinkSets": [
            {
                "networkUris": [
                    "net100"
                ],
                "ethernetNetworkType": "Tagged",
                "name": "ULS1",
                "lacpTimer": "Short",
                "primaryPort": None,
                "nativeNetworkUri": None,
                "mode": "Auto",
                "networkType": "Ethernet",
                "logicalPortConfigInfos": [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
            },
            {
                "networkUris": [
                    "net300"
                ],
                "ethernetNetworkType": "Tagged",
                "name": "ULS2",
                "lacpTimer": "Short",
                "primaryPort": None,
                "nativeNetworkUri": None,
                "mode": "Auto",
                "networkType": "Ethernet",
                "logicalPortConfigInfos": [{'enclosure': '1', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}]
            }
        ],
        "redundancyType": "Redundant",
        "enclosureType": "SY12000",
        "fabricUri": "Fabric:DefaultFabric",
        "qosConfiguration": {
            "name": None,
            "type": "qos-aggregated-configuration",
            "inactiveFCoEQosConfig": None,
            "inactiveNonFCoEQosConfig": None,
            "activeQosConfig": {
                "description": None,
                "configType": "Passthrough",
                "downlinkClassificationType": None,
                "uplinkClassificationType": None,
                "qosTrafficClassifiers": [],
                "type": "QosConfiguration",
                "name": None
            },
            "description": None
        },
        "scopeUris": [],
        "type": LOGICAL_INTERCONNECT_GROUP_TYPE,
        "interconnectMapTemplate": icmap,
        "ethernetSettings": {
            "interconnectType": "Ethernet",
            "igmpIdleTimeoutInterval": 260,
            "macRefreshInterval": 5,
            "description": None,
            "enableTaggedLldp": False,
            "enableRichTLV": False,
            "enableNetworkLoopProtection": True,
            "enableFastMacCacheFailover": True,
            "lldpIpv4Address": "",
            "enableIgmpSnooping": False,
            "enablePauseFloodProtection": True,
            "dependentResourceUri": "LIG:LIG_NAME",
            "type": "EthernetInterconnectSettingsV201",
            "lldpIpv6Address": "",
            "name": "name2003202772-1470153927401"
        },
        "stackingHealth": None,
        "stackingMode": None,
        "interconnectBaySet": 3,
        "snmpConfiguration": {
            "description": None,
            "readCommunity": "public",
            "enabled": True,
            "systemContact": "",
            "snmpAccess": [],
            "trapDestinations": [],
            "type": "snmp-configuration",
            "name": None
        }
    }
]

eg = [
    {
        "osDeploymentSettings": {
            "deploymentModeSettings": {
                "deploymentNetworkUri": None,
                "deploymentMode": "None"
            },
            "manageOSDeployment": False
        },
        "powerMode": "RedundantPowerFeed",
        "interconnectBayMappings": [
            {
                "logicalInterconnectGroupUri": "LIG:" + LIG_NAME,
                "interconnectBay": 3
            },
            {
                "logicalInterconnectGroupUri": "LIG:" + LIG_NAME,
                "interconnectBay": 6
            }
        ],
        "enclosureCount": 1,
        "ipAddressingMode": "DHCP",
        "ipRangeUris": [],
        "name": EG_NAME
    }
]

le = [
    {
        'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC_NAME],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
    }
]

profile = {
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "connections": [
        {
            "requestedVFs": "0",
            "wwnn": None,
            "portId": "Mezz 3:1-a",
            "name": "conn1",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:net100",
            "interconnectUri": "IC:CN744502CL, interconnect 3",
            "maximumMbps": 10000,
            "functionType": "Ethernet",
            "macType": "Virtual"
        },
        {
            "requestedVFs": "0",
            "wwnn": None,
            "portId": "Mezz 3:2-a",
            "name": "conn2",
            "wwpnType": "Virtual",
            "requestedMbps": "2500",
            "networkUri": "ETH:net300",
            "interconnectUri": "IC:CN744502CL, interconnect 6",
            "maximumMbps": 10000,
            "functionType": "Ethernet",
            "macType": "Virtual"
        }
    ],
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "firmware": {
        "firmwareBaselineUri": None,
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "boot": {
        "manageBoot": False,
        "order": []
    },
    "hideUnusedFlexNics": True,
    "bootMode": {
        "manageMode": False,
        "pxeBootPolicy": None,
        "mode": None
    },
    "affinity": "Bay",
    "localStorage": {
        "controllers": [],
        "sasLogicalJBODs": []
    },
    "type": SERVER_PROFILE_TYPE,
    "enclosureUri": "ENC:CN744502CL",
    "associatedServer": None,
    "osDeploymentSettings": None,
    "description": "",
    "iscsiInitiatorName": "iqn.2015-02.com.hpe:oneview-vcgnka005r",
    "templateCompliance": "Unknown",
    "serverHardwareUri": "SH:CN744502CL, bay 1",
    "enclosureBay": 1,
    "name": ENC_NAME + "_bay_1_profile",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }
}

ris_original = {
    "server": SERVER_NAME,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/NetworkAdapters/1",
    "validate": {
        "PhysicalPorts": [{"MacAddress": "34:64:A9:93:68:30"}, {"MacAddress": "34:64:A9:93:68:38"}]
    }
}

PostStateDiscoveryComplete = {
    "server": SERVER_NAME,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1",
    "validate": {
        "Oem": {
            "Hp": {
                "PostState": "InPostDiscoveryComplete",
                "DeviceDiscoveryComplete": {
                    "DeviceDiscovery": "vMainDeviceDiscoveryComplete"
                }
            }
        }
    }
}

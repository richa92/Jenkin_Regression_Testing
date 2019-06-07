"""
This file is used to Add_Base_Resources(ABR) to Oneview which will be used in FVT C7000 API Tests
"""
# pylint: disable=E0401,E0602
from copy import deepcopy
from dto import *
from env_variables_C7000 import *

admin_credentials = deepcopy(ADMIN_CREDENTIALS_COMMON)
oa_credentials = deepcopy(OA_CREDENTIALS_COMMON)
cliq_credentials = deepcopy(STOREVIRTUAL_SLPT_STATIC_CLIQ_CREDENTIALS)
ilo_credentials = deepcopy(ILO_CREDENTIALS_COMMON)
hpmctp_credentials = deepcopy(HPMCTP_CREDENTIALS_COMMON)

# FTS, users, and licenses
APP1_IPV4_ADDRESS = APPLIANCE_VIP
HOSTNAME = APPLIANCE_HOSTNAME

appliance = {
    'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    'applianceNetworks': [{
        'device': 'eth0',
        'macAddress': None,
        'interfaceName': 'Appliance',
        'activeNode': '1',
        'unconfigure': False,
        'ipv4Type': IPV4_TYPE,
        'app1Ipv4Addr': APP1_IPV4_ADDRESS,
        'ipv6Type': IPV6_TYPE,
        'ipv4Subnet': IPV4_SUBNET,
        'ipv4Gateway': IPV4_GATEWAY,
        'hostname': HOSTNAME,
        'confOneNode': True,
        'domainName': DOMAIN_NAME,
        'ipv4NameServers': [IPV4_DNS1, IPV4_DNS2, IPV4_DNS3],
        'aliasDisabled': False
    }]
}

timeandlocale = {
    'type': TIME_AND_LOCALE_TYPE,
    'dateTime': None,
    'timezone': TIME_ZONE,
    'ntpServers': [NTP_SERVER_HOSTNAME],
    'locale': LOCALE_EN
}

users = [
    {
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "Serveradmin",
        "fullName": "Serveradmin",
        "password": "Serveradmin",
        "emailAddress": "sarah@hp.com",
        "officePhone": "970-555-0003",
        "mobilePhone": "970-500-0003",
        "enabled": True,
        "permissions": [{
            "roleName": "Server administrator",
            "scopeUri": None
        }]
    },
    {
        'userName': 'Networkadmin',
        'password': 'Networkadmin',
        'fullName': 'Networkadmin',
        "permissions": [
            {
                "roleName": "Network administrator",
                "scopeUri": None
            }
        ],
        'emailAddress': 'nat@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Backupadmin',
        'password': 'Backupadmin',
        'fullName': 'Backupadmin',
        "permissions": [
            {
                "roleName": "Backup administrator",
                "scopeUri": None
            }
        ],
        'emailAddress': 'backup@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Noprivledge',
        'password': 'Noprivledge',
        'fullName': 'Noprivledge',
        "permissions": [
            {
                "roleName": "Read only",
                "scopeUri": None
            }
        ],
        'emailAddress': 'rheid@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    }
]

# SAN Manager and Managed SANs
SAN_Managers = [
    {
        "connectionInfo": [
            {'name': 'Type', 'value': SAN_MANAGER_BNA},
            {
                "name": "Host",
                "displayName": "Host",
                "required": True,
                "value": SAN_MANAGER_BNA_IP,
                "valueFormat": "IPAddressOrHostname",
                "valueType": "String"
            },
            {
                "name": "Port",
                "displayName": "Port",
                "required": True,
                "value": 5989,
                "valueFormat": "None",
                "valueType": "Integer"
            },
            {
                "name": "Username",
                "displayName": "Username",
                "required": True,
                "value": "Administrator",
                "valueFormat": "None",
                "valueType": "String"
            },
            {
                "name": "Password",
                "displayName": "Password",
                "required": True,
                "value": "password",
                "valueFormat": "SecuritySensitive",
                "valueType": "String"
            },
            {
                "name": "UseSsl", "displayName": "UseSsl", "required": True, "value": True, "valueFormat": "None",
                "valueType": "Boolean"
            }, ],
    },
    {
        "connectionInfo": [
            {'name': 'Type', 'value': SAN_MANAGER_HPE},
            {"name": "Host", "value": SAN_MANAGER_HPE_IP},
            {"name": "SnmpPort", "value": 161},
            {"name": "SnmpUserName", "value": "UNoAuthNoPriv"},
            {"name": "SnmpAuthLevel", "value": "NOAUTHNOPRIV"}]
    }
]

# Enclosures, Interconnects, Server Hardware, Networks, ULS, LIG, and EG

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1  # BL465c Gen8
ENC1SHBAY2 = '%s, bay 2' % ENC1  # BL465c Gen8
ENC1SHBAY3 = '%s, bay 3' % ENC1  # BL465c Gen8
ENC1SHBAY4 = '%s, bay 4' % ENC1  # BL420c Gen8
ENC1SHBAY5 = '%s, bay 5' % ENC1  # BL460c Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1  # BL460c G6
ENC1SHBAY8 = '%s, bay 7' % ENC1  # BL495c G5
ENC1SHBAY14 = '%s, bay 14' % ENC1  # BL460c Gen10
ENC1SHBAY16 = '%s, bay 16' % ENC1  # BL460c Gen10
ENC2SHBAY1 = '%s, bay 1' % ENC2  # BL465c Gen8
ENC2SHBAY2 = '%s, bay 2' % ENC2  # BL465c Gen8
ENC2SHBAY3 = '%s, bay 3' % ENC2  # BL465c Gen8
ENC2SHBAY4 = '%s, bay 4' % ENC2  # BL420c Gen8
ENC2SHBAY5 = '%s, bay 5' % ENC2  # BL460c Gen9
ENC2SHBAY6 = '%s, bay 6' % ENC2  # BL460c G6
ENC2SHBAY7 = '%s, bay 7' % ENC2  # BL2x220c G5
ENC2SHBAY10 = '%s, bay 10' % ENC2  # BL460c Gen10
ENC2SHBAY16 = '%s, bay 16' % ENC2  # BL460c Gen10
ENC3SHBAY1 = '%s, bay 1' % ENC3  # BL465c Gen8
ENC3SHBAY2 = '%s, bay 2' % ENC3  # BL465c Gen8
ENC3SHBAY3 = '%s, bay 3' % ENC3  # BL465c Gen8
ENC3SHBAY4 = '%s, bay 4' % ENC3  # BL420c Gen8
ENC3SHBAY5 = '%s, bay 5' % ENC3  # BL460c Gen9
ENC3SHBAY7 = '%s, bay 7' % ENC3  # BL660c Gen9
ENC3SHBAY8 = '%s, bay 8' % ENC3  # BL660c Gen8
ENC3SHBAY9 = '%s, bay 9' % ENC3  # BL460c G7
ENC3SHBAY10 = '%s, bay 10' % ENC3  # BL465c G7

ethernet_networks = [
    {
        'name': 'network-tunnel',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 1,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tunnel'
    },
    {
        'name': 'network-untagged',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 1,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Untagged'
    },
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
    },
]

fc_networks = [
    {
        'name': 'fa-a', 'autoLoginRedistribution': True, 'type': FC_NETWORK_TYPE, 'linkStabilityTime': '30',
        'fabricType': 'FabricAttach', 'connectionTemplateUri': None, 'managedSanUri': 'FCSan:' + FA_SAN_A
    },
    {
        'name': 'fa-b',
        'autoLoginRedistribution': True,
        'type': FC_NETWORK_TYPE,
        'linkStabilityTime': '30',
        'fabricType': 'FabricAttach',
        'connectionTemplateUri': None,
        'managedSanUri': 'FCSan:' + FA_SAN_B
    },
    {
        'name': 'FA3',
        'type': FC_NETWORK_TYPE,
        'fabricType': 'FabricAttach',
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True,
        'managedSanUri': None
    },
    {
        'name': 'FA4',
        'type': FC_NETWORK_TYPE,
        'fabricType': 'FabricAttach',
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True
    },
    {
        'name': 'DA1',
        'type': FC_NETWORK_TYPE,
        'fabricType': 'DirectAttach',
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True,
        'managedSanUri': None
    },
    {
        'name': 'DA2',
        'type': FC_NETWORK_TYPE,
        'fabricType': 'DirectAttach',
        'linkStabilityTime': 30,
        'autoLoginRedistribution': True
    }
]

fcoe_networks = [
    {'name': 'fcoe_103', 'type': FCOE_NETWORK_TYPE, 'vlanId': 103},
    {
        'name': 'FCoE1',
        'type': FCOE_NETWORK_TYPE,
        'vlanId': 750,
        'managedSanUri': 'FCSan:VSAN750'
    },
    {
        'name': 'FCoE2',
        'type': FCOE_NETWORK_TYPE,
        'vlanId': 850,
        'managedSanUri': 'FCSan:VSAN850'
    },
]

network_sets = [
    {
        'name': 'NS1',
        'type': NETWORK_SET_TYPE,
        'networkUris': ['net100', 'net300'],
        'nativeNetworkUri': 'net100'
    },
    {
        'name': 'Net-Set1',
        'type': NETWORK_SET_TYPE,
        'networkUris': ['dev100',
                        'dev300-pxeboot'],
        'nativeNetworkUri': None
    },
    {
        'name': 'Net-Set2',
        'type': NETWORK_SET_TYPE,
        'networkUris': ['dev101-management',
                        'dev103-ft-a'],
        'nativeNetworkUri': None
    },
]

ligs = [
    {
        'name': LIG1_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': FRAME_TYPE2,
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': SHEPPARD},
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 2,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 3,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 4,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 5,
                'type': OCHO
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 6,
                'type': OCHO
            },
        ],
        'uplinkSets': [
            {
                'name': 'us-untagged',
                'ethernetNetworkType': 'Untagged',
                'networkType': 'Ethernet',
                'networkUris': ['network-untagged'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-tunnel',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['network-tunnel'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-tagged',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['net100', 'net300'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                           {'bay': '4', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-fa-a',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': ['fa-a'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}]
            },
            {
                'name': 'us-fa-b',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': ['fa-b'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}]
            },
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    {
        'name': LIG2_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': FRAME_TYPE2,
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': SUPERSHAW},
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 2,
                'type': SUPERSHAW
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 3,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 4,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 5,
                'type': OCHO
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 6,
                'type': OCHO
            },
        ],
        'uplinkSets': [
            {
                'name': 'us-untagged',
                'ethernetNetworkType': 'Untagged',
                'networkType': 'Ethernet',
                'networkUris': ['network-untagged'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]
            },
            {
                'name': 'us-tunnel',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['network-tunnel'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]
            },
            {
                'name': 'us-tagged',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['net100', 'net300'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                           {'bay': '4', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-fa-a',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': ['fa-a'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}]
            },
            {
                'name': 'us-fa-b',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': ['fa-b'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}]
            },
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    {
        'name': LIG3_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': FRAME_TYPE2,
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': SHEPPARD},
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 2,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 3,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 4,
                'type': SHEPPARD
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 5,
                'type': UTAH
            },
            {
                'enclosure': 1,
                'enclosureIndex': 1,
                'bay': 6,
                'type': UTAH
            },
        ],
        'uplinkSets': [
            {
                'name': 'us-untagged',
                'ethernetNetworkType': 'Untagged',
                'networkType': 'Ethernet',
                'networkUris': ['network-untagged'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-tunnel',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['network-tunnel'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-tagged',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['net100', 'net300'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                                           {'bay': '4', 'port': 'X3', 'speed': 'Auto'}]
            },
            {
                'name': 'us-fa-a',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': ['fa-a'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '5', 'port': '1', 'speed': 'Auto'}]
            },
            {
                'name': 'us-fa-b',
                'ethernetNetworkType': 'NotApplicable',
                'networkType': 'FibreChannel',
                'networkUris': ['fa-b'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [{'bay': '6', 'port': '1', 'speed': 'Auto'}]
            },
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
]

enc_groups = [
    {
        'name': EG1_NAME,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
                {
                    'interconnectBay': 2,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME
                },
                {
                    'interconnectBay': 3,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME
                },
                {
                    'interconnectBay': 4,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME
                },
                {
                    'interconnectBay': 5,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME
                },
                {
                    'interconnectBay': 6,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME
                },
                {
                    'interconnectBay': 7,
                    'logicalInterconnectGroupUri': None
                },
                {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
            ]
    },
    {
        'name': EG2_NAME,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
                {
                    'interconnectBay': 2,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME
                },
                {
                    'interconnectBay': 3,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME
                },
                {
                    'interconnectBay': 4,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME
                },
                {
                    'interconnectBay': 5,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME
                },
                {
                    'interconnectBay': 6,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME
                },
                {
                    'interconnectBay': 7,
                    'logicalInterconnectGroupUri': None
                },
                {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
            ]
    },
    {
        'name': EG3_NAME,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
                {
                    'interconnectBay': 2,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME
                },
                {
                    'interconnectBay': 3,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME
                },
                {
                    'interconnectBay': 4,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME
                },
                {
                    'interconnectBay': 5,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME
                },
                {
                    'interconnectBay': 6,
                    'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME
                },
                {
                    'interconnectBay': 7,
                    'logicalInterconnectGroupUri': None
                },
                {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
            ]
    }
]

enclosures = [
    {
        'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
        'enclosureGroupUri': 'EG:' + EG1_NAME,
        'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None,
    },
    {
        'hostname': ENC2_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
        'enclosureGroupUri': 'EG:' + EG2_NAME,
        'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None,
    },
    {
        'hostname': ENC3_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
        'enclosureGroupUri': 'EG:' + EG3_NAME,
        'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None,
    },
]

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst26", "state": "Configured", },
]

interconnects_expected = [
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY1,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY2,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY3,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY4,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY5,
        "productName": OCHO,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC1ICBAY6,
        "productName": OCHO,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY1,
        "productName": SUPERSHAW,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY2,
        "productName": SUPERSHAW,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY3,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY4,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY5,
        "productName": OCHO,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC2ICBAY6,
        "productName": OCHO,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY1,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY2,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY3,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY4,
        "productName": SHEPPARD,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY5,
        "productName": UTAH,
    },
    {
        "type": INTERCONNECT_TYPE,
        "name": ENC3ICBAY6,
        "productName": UTAH,
    },
]

# StoreVirtual
STOREVIRTUAL1_NAME = STOREVIRTUAL_SLPT_STATIC_NAME
STOREVIRTUAL1_HOSTNAME = STOREVIRTUAL_SLPT_STATIC_HOSTNAME
STOREVIRTUAL1_VIP = STOREVIRTUAL_SLPT_STATIC_VIP
STOREVIRTUAL1_POOL = STOREVIRTUAL_SLPT_STATIC_POOL
STOREVIRTUAL2_NAME = STOREVIRTUAL_MLPT_NAME
STOREVIRTUAL2_HOSTNAME = STOREVIRTUAL_MLPT_HOSTNAME
STOREVIRTUAL2_VIP = STOREVIRTUAL_MLPT_VIP
STOREVIRTUAL2_POOL = STOREVIRTUAL_MLPT_POOL
STOREVIRTUAL3_NAME = STOREVIRTUAL_SLPT_DHCP_NAME
STOREVIRTUAL3_HOSTNAME = STOREVIRTUAL_SLPT_DHCP_HOSTNAME
STOREVIRTUAL3_VIP = STOREVIRTUAL_SLPT_DHCP_VIP
STOREVIRTUAL3_POOL = STOREVIRTUAL_SLPT_DHCP_POOL

storage_systems = [
    {
        "type": STORAGE_SYSTEM_TYPE,
        "name": STORESERV1_NAME,
        "family": "StoreServ",
        "hostname": STORESERV1_HOSTNAME,
        "credentials": STORESERV1_CREDENTIALS,
        "deviceSpecificAttributes": {
            "discoveredDomains": DISCOVERED_DOMAINS,
            "managedDomain": STORESERV1_MANAGED_DOMAIN,
        },
    },
    {
        "type": STORAGE_SYSTEM_TYPE,
        "name": STOREVIRTUAL1_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL1_HOSTNAME,
        "credentials": STOREVIRTUAL_SLPT_STATIC_CREDENTIALS,
        "ports": [
            {
                "name": STOREVIRTUAL1_VIP,
                "expectedNetworkUri": "ETH:network-untagged",
                "expectedNetworkName": "network-untagged",
                "mode": "Managed",
            }
        ],
    },
    {
        'type': 'StorageSystemV4',
        'name': STOREVIRTUAL2_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL2_HOSTNAME,
        "credentials": STOREVIRTUAL_MLPT_CREDENTIALS,
        "ports": [{
            "name": STOREVIRTUAL2_VIP,
            "expectedNetworkUri": "ETH:network-tunnel",
            "expectedNetworkName": "network-tunnel",
            "mode": "Managed"
        }, ],
    },
    {
        'type': 'StorageSystemV4',
        'name': STOREVIRTUAL3_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL3_HOSTNAME,
        "credentials": STOREVIRTUAL_SLPT_DHCP_CREDENTIALS,
        "ports": [{
            "name": STOREVIRTUAL3_VIP,
            "expectedNetworkUri": "ETH:network-untagged",
            "expectedNetworkName": "network-untagged",
            "mode": "Managed"
        }, ],
    },
]

storage_pools = [
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL1,
        "isManaged": True,
    },
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL2,
        "isManaged": True,
    },
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL3,
        "isManaged": True,
    },
]

# OVF1061
OVF1061_SERVER1 = ENC1SHBAY14
OVF1061_SERVER1_ILO = ''
OVF1061_SERVER1_SERVER_NAME_1 = "wpst22bay14-1"
OVF1061_SERVER1_SERVER_NAME_2 = "wpst22bay14-2"
OVF1061_SERVER1_SERVER_NAME_3 = "WPST22BAY14-OS"
OVF1061_SERVER2 = ENC2SHBAY2
OVF1061_SERVER2_ILO = ''
OVF1061_SERVER2_SERVER_NAME_1 = "wpst23bay2-1"
OVF1061_SERVER2_SERVER_NAME_2 = "wpst23bay2-2"
OVF1061_SERVER2_SERVER_NAME_3 = "wpst23bay2-os"

server_settings_1 = [
    {
        'name': OVF1061_SERVER1,
        'ilo': OVF1061_SERVER1_ILO,
        'server_name': OVF1061_SERVER1_SERVER_NAME_1
    },
    {
        'name': OVF1061_SERVER2,
        'ilo': OVF1061_SERVER2_ILO,
        'server_name': OVF1061_SERVER2_SERVER_NAME_1
    },
]

server_settings_2 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_2},
    {'name': OVF1061_SERVER2, 'server_name': OVF1061_SERVER2_SERVER_NAME_2},
]

server_settings_3 = [
    {'name': OVF1061_SERVER1, 'server_name': OVF1061_SERVER1_SERVER_NAME_3},
    {'name': OVF1061_SERVER2, 'server_name': OVF1061_SERVER2_SERVER_NAME_3},
]

# OVF487
snmpv3_user1 = 'fvttest1'
snmpv3_user2 = 'fvttest2'
snmpv3_user3 = 'fvttest3'
snmpv3_passphrase = 'wpsthpvse1'
rocommunity1 = 'public'
rocommunity2 = 'abcabc'
rocommunity3 = 'xyzxyz'
ovf487_testhead = 'wpst-jenkins-2.vse.rdlabs.hpecorp.net'
ovf487_oa = ENC1_OA1
ovf487_oa_username = oa_credentials['username']
ovf487_oa_password = oa_credentials['password']
ovf487_oa_user1 = [snmpv3_user1, 'SHA1', snmpv3_passphrase, 'AES128', snmpv3_passphrase]
ovf487_oa_trapreceiver1 = [ovf487_testhead, rocommunity2]
ovf487_oa_trapreceiver2 = [ovf487_testhead, snmpv3_user1]
ovf487_server1 = ENC1SHBAY3
ovf487_ilo1 = ''
ovf487_server2 = ENC3SHBAY5
ovf487_ilo2 = ''
ovf487_server3 = ENC1SHBAY14
ovf487_ilo3 = ''

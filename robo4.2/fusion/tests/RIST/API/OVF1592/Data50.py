# pylint: disable=E0401,E0602
from dto import *

# Precondition for OVF1592
credentials = {
    "admin_credentials": {
        'userName': 'Administrator',
        'password': 'wpsthpvse1'
    },
    "na_credentials": {
        'userName': 'NA',
        'password': 'wpsthpvse1'
    },
    "ia_credentials": {
        'userName': 'IA',
        'password': 'wpsthpvse1'
    },
    "sa_credentials": {
        'userName': 'SA',
        'password': 'wpsthpvse1'
    },
    "spa_credentials": {
        'userName': 'SPA',
        'password': 'wpsthpvse1'
    },
    "spo_credentials": {
        'userName': 'SPO',
        'password': 'wpsthpvse1'
    },
}

enclosure = ['CN75120D7B', 'CN75120D77', 'CN750163KD']
enc_list = ["ENC:%s" % enc for enc in enclosure]
fc_domain = "Tbird_Regression_Domain"
fcoe_domain = "NO DOMAIN"

Scope_List = ["Production", "Test", "Stage", "Scope1", "Scope2", "Scope3"]

Scopes = [
    {
        "name": Scope_List[1],
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": Scope_List[0],
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": [],
        "initialScopeUris": []
    },
    {
        "name": Scope_List[2],
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": []
    },
    {
        "name": Scope_List[3],
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": [],
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        "name": Scope_List[4],
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": [],
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        "name": Scope_List[5],
        "description": "",
        "type": SCOPE_TYPE,
        "addedResourceUris": [],
        "removedResourceUris": [],
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]

licenses = [
    {
        'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'
    },
    {
        'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'YB2C D9MA H9PA 8HU3 V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE 9QSP XFR8 CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    },
    {
        'key': 'YBCG D9MA H9PA GHUY V2B4 HWWV Y9JL KMPL B89H MZVU GR4S JHWE JVSH XV5S CMRG HPMR UFVU A5K9 MWHC 9K4K HKDU LWWP JQLG UPJ4 AQYC Q7NV M658 AGVQ QZWD HY9B N4ZF BGWB EWV7 2EUZ NK64 R4WA 5886 FCYX YKC5 G3AD QVKT NLY8 EZUN HENY"24R2-02192-002 T1111A FC_License J4E8IAMANEON"'
    }
]

users = [
    {
        'userName': 'IA',
        'password': 'wpsthpvse1',
        'fullName': 'IA',
        "permissions": [
            {
                "roleName": "Infrastructure administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Infrastructure administrator",
                "scopeUri": "Scope:Production"
            },
        ],
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'SA',
        'password': 'wpsthpvse1',
        'fullName': 'SA',
        "permissions": [
            {
                "roleName": "Server administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Server administrator",
                "scopeUri": "Scope:Production"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Production"
            },
        ],
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'NA',
        'password': 'wpsthpvse1',
        'fullName': 'NA',
        "permissions": [
            {
                "roleName": "Network administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Network administrator",
                "scopeUri": "Scope:Production"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Production"
            },
        ],
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'SPA',
        'password': 'wpsthpvse1',
        'fullName': 'BA',
        "permissions": [
            {
                "roleName": "Server profile administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Server profile administrator",
                "scopeUri": "Scope:Production"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Production"
            },
        ],
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'SPO',
        'password': 'wpsthpvse1',
        'fullName': 'BA',
        "permissions": [
            {
                "roleName": "Server profile operator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Server profile operator",
                "scopeUri": "Scope:Production"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Test"
            },
            {
                "roleName": "Scope administrator",
                "scopeUri": "Scope:Production"
            },
        ],
        'type': USER_AND_PERMISSION_TYPE
    },
]

SAN_Managers = [
    {
        "connectionInfo": [
            {
                'name': 'Type',
                'value': 'Brocade Network Advisor'
            },
            {
                "name": "Host",
                "displayName": "Host",
                "required": True,
                "value": "16.125.65.9",
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
                "name": "UseSsl",
                "displayName": "UseSsl",
                "required": True,
                "value": True,
                "valueFormat": "None",
                "valueType": "Boolean"
            },
        ],
    },
    {
        "connectionInfo": [
            {'name': 'Type', 'value': 'HPE'},
            {"name": "Host", "value": "16.125.25.45"},
            {"name": "SnmpPort", "value": 161},
            {"name": "SnmpUserName", "value": "UNoAuthNoPriv"},
            {"name": "SnmpAuthLevel", "value": "NOAUTHNOPRIV"},
            {"name": "SnmpAuthProtocol", "value": ""},
            {"name": "SnmpAuthString", "value": ""},
            {"name": "SnmpPrivProtocol", "value": ""},
            {"name": "SnmpPrivString", "value": ""}
        ],
    },
]

Ethernet_Networks = [
    {
        "vlanId": "101",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "eth1",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[0],
            "Scope:%s" % Scope_List[1]
        ]
    },
    {
        "vlanId": "102",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "eth2",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[1]
        ]
    },
    {
        "vlanId": "103",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "eth3",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[0]
        ]
    },
    {
        "vlanId": "104",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "eth4",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[2]
        ]
    },
]

fc_networks = [
    {
        "name": "fc1",
        "connectionTemplateUri": None,
        "linkStabilityTime": 30,
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55',
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[1],
            "Scope:%s" % Scope_List[0]
        ]
    },
    {
        "name": "fc2",
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56',
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        "name": "fc3",
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55',
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
    {
        "name": "fc4",
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56',
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]

fcoe_networks = [
    {
        "name": "fcoe1",
        "vlanId": 350,
        "connectionTemplateUri": None,
        'managedSanUri': 'FCSan:VSAN350',
        'type': FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[1],
                             "Scope:%s" % Scope_List[0]]
    },
    {
        "name": "fcoe2",
        "vlanId": 450,
        "connectionTemplateUri": None,
        'managedSanUri': 'FCSan:VSAN450',
        'type': FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        "name": "fcoe3",
        "vlanId": 351,
        "connectionTemplateUri": None,
        'type': FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
    {
        "name": "fcoe4",
        "vlanId": 451,
        "connectionTemplateUri": None,
        "managedSanUri": None,
        'type': FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]

network_sets = [
    {
        "name": "net-set1",
        "networkUris": ["eth4"],
        "type": NETWORK_SET_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[0],
            "Scope:%s" % Scope_List[1]
        ],
        "nativeNetworkUri": None
    },
    {
        "name": "net-set2",
        "networkUris": [],
        "type": NETWORK_SET_TYPE,
        "nativeNetworkUri": None,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        "name": "net-set3",
        "networkUris": [],
        "type": NETWORK_SET_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[0]],
        "nativeNetworkUri": None
    },
    {
        "name": "net-set4",
        "networkUris": [],
        "type": NETWORK_SET_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]],
        "nativeNetworkUri": None
    }
]

uplink_sets1 = [
    {
        'name': 'net1',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth1'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'}, ]
    },
    {
        'name': 'net2',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth2'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2', 'speed': 'Auto'}, ]
    },
    {
        'name': 'net3',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth3'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}, ]
    },
    {
        'name': 'net4',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth4'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4', 'speed': 'Auto'}, ]
    },
]

icmap = {
    'LIG_POTASH': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
    ],
    'LIG_SAS': [
        {'bay': 1, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
        {'bay': 4, 'enclosure': 1, 'type': 'Synergy 12Gb SAS Connection Module', 'enclosureIndex': 1},
    ],
    'LIG_CARBONS': [
        {'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
    ],
}

LIG_BASE = [
    {
        'name': 'LIG1',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [],
        "initialScopeUris": [
            "Scope:%s" % Scope_List[0],
            "Scope:%s" % Scope_List[1]
        ]
    },
    {
        'name': 'LIG2',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': uplink_sets1,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        'name': 'LIG3',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': uplink_sets1,
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
    {
        'name': 'LIG4',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [],
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    },
    {
        'name': 'LIG-Synergy',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [],
    }
]

SAS_LIG = [
    {
        "name": "SAS1",
        "state": "Active",
        "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
        "enclosureType": "SY12000",
        "interconnectMapTemplate": icmap["LIG_SAS"],
        "enclosureIndexes": [1],
        "interconnectBaySet": 1,
    }
]

EG_BASE = [
    {
        'name': 'EG1',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[0]["name"]},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[0]["name"]},
            ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed",
        "initialScopeUris": [
            "Scope:%s" % Scope_List[1],
            "Scope:%s" % Scope_List[0]]
    },
    {
        'name': 'EG2',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[1]["name"]},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[1]["name"]},
            ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed",
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        'name': 'EG3',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[2]["name"]},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[2]["name"]},
            ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed",
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
    {
        'name': 'EG4',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[3]["name"]},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[3]["name"]},
            ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed",
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    },
    {
        'name': 'EG-Synergy',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[4]["name"]},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_BASE[4]["name"]},
                {
                    "interconnectBay": 1, "enclosureIndex": 1,
                    "logicalInterconnectGroupUri": "SASLIG:" + SAS_LIG[0]["name"]
                },
                {
                    "interconnectBay": 4, "enclosureIndex": 1,
                    "logicalInterconnectGroupUri": "SASLIG:" + SAS_LIG[0]["name"]
                },
            ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed",
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
]

LE_BASE = {
    "name": "LE_SYNERGY",
    "enclosureUris": enc_list,
    "enclosureGroupUri": "EG:" + EG_BASE[4]["name"],
    "firmwareBaselineUri": None,
    "forceInstallFirmware": False
}

StorageSystems_Put = [
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': 'wpst3par-7200-7-srv',
        'family': 'StoreServ',
        'hostname': 'wpst3par-7200-7-srv.vse.rdlabs.hpecorp.net',
        'credentials': {'username': 'fusionadm', 'password': 'hpvse1'},
        'deviceSpecificAttributes': {
            'discoveredDomains': [
                'NO DOMAIN',
                'wpst20',
                'wpst22',
                'wpst23',
                'wpst26',
                'wpst30',
                'wpst31',
                'wpst32',
                'wpst33',
                'wpst34',
                'wpst8',
                'wpst9',
                'FVT_C7000_reg1',
                'Tbird_Regression_Domain',
            ],
            'managedDomain': fc_domain,
        },
    },
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': 'fvt3par-8400-1-srv',
        'family': 'StoreServ',
        'hostname': 'fvt3par-8400-1-srv.vse.rdlabs.hpecorp.net',
        'credentials': {'username': '3paradm', 'password': '3pardata'},
        'deviceSpecificAttributes': {
            'discoveredDomains': [
                'NO DOMAIN',
            ],
            'managedDomain': fcoe_domain,
        }
    }]
StoragePools = [
    {'storageSystemUri': 'wpst3par-7200-7-srv', "name": "FVT_Tbird_reg1_r1", "isManaged": True, },
    {'storageSystemUri': 'wpst3par-7200-7-srv', "name": "FVT_Tbird_reg1_r5", "isManaged": True, },
    {'storageSystemUri': 'wpst3par-7200-7-srv', "name": "FVT_Tbird_reg1_r6", "isManaged": True, },
    {'storageSystemUri': 'fvt3par-8400-1-srv', "name": "FC_r1", "isManaged": True, },
    {'storageSystemUri': 'fvt3par-8400-1-srv', "name": "FC_r5", "isManaged": True, },
]

scope_resources = {
    "Test": [
        "SPOOL:FVT_Tbird_reg1_r1",
        "SPOOL:FVT_Tbird_reg1_r5",
        "IC:CN75120D77, interconnect 1",
        "IC:CN75120D7B, interconnect 3",
        "SH:CN75120D7B, bay 5",
        "SH:CN75120D7B, bay 7",
        "DE:CN75120D7B, bay 1",
    ],
    "Production": [
        "SPOOL:FVT_Tbird_reg1_r1",
        "SPOOL:FVT_Tbird_reg1_r6",
        "IC:CN75120D77, interconnect 1",
        "IC:CN75120D77, interconnect 4",
        "SH:CN75120D7B, bay 7",
        "SH:CN75120D77, bay 5",
    ],
    "Stage": [
        "SPOOL:FC_r1",
        "IC:CN75120D77, interconnect 6",
        "SH:CN75120D77, bay 1",
    ]
}

VolumeTemplates = [
    {
        'name': 'VOL-TMP1',
        'description': '',
        'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
        "initialScopeUris": [
            "Scope:%s" % Scope_List[1],
            "Scope:%s" % Scope_List[0]],
        'properties': {
            'storageSystem': 'wpst3par-7200-7-srv',
            'name': {
                'title': 'Volume name',
                'description': 'A volume name between 1 and 100 characters',
                'type': 'string',
                'minLength': 1,
                'maxLength': 100,
                'required': True,
                'meta': {'locked': False}
            },
            'description': {
                'title': 'Description',
                'description': 'A description for the volume',
                'type': 'string',
                'minLength': 0,
                'maxLength': 2000,
                'default': '3Par1 pool1 private',
                'meta': {'locked': False}
            },
            'storagePool': {
                'title': 'Storage Pool',
                'description': 'A common provisioning group URI reference',
                'type': 'string',
                'required': True,
                'format': 'x-uri-reference',
                'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                'default': 'FVT_Tbird_reg1_r1'
            },
            'size': {
                'title': 'Capacity',
                'description': 'The capacity of the volume in bytes',
                'type': 'integer',
                'required': True,
                'minimum': 1073741824,
                'maximum': 17592186044416,
                'meta': {'locked': False, 'semanticType': 'capacity'},
                'default': 1073741824,
            },
            'isShareable': {
                'title': 'Is Shareable',
                'description': 'The shareability of the volume',
                'type': 'boolean',
                'meta': {'locked': False},
                'default': False,
            },
            'provisioningType': {
                'title': 'Provisioning Type',
                'description': 'The provisioning type for the volume',
                'type': 'string',
                'enum': ['Thin', 'Full'],
                'meta': {'locked': True, 'createOnly': True},
                'default': 'Thin'
            },
            'snapshotPool': {
                'title': 'Snapshot Pool',
                'description': 'A URI reference to the common provisioning group used to create snapshots',
                'type': 'string',
                'format': 'x-uri-reference',
                'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                'default': 'FVT_Tbird_reg1_r1'
            }
        },
    },
    {
        'name': 'VOL-TMP2',
        'description': '',
        'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
        "initialScopeUris": ["Scope:%s" % Scope_List[1]],
        'properties': {
            'storageSystem': 'wpst3par-7200-7-srv',
            'name': {
                'title': 'Volume name', 'description': 'A volume name between 1 and 100 characters',
                'type': 'string',
                'minLength': 1,
                'maxLength': 100,
                'required': True,
                'meta': {'locked': False}
            },
            'description': {
                'title': 'Description',
                'description': 'A description for the volume',
                'type': 'string',
                'minLength': 0,
                'maxLength': 2000,
                'default': '3Par1 pool1 private',
                'meta': {'locked': False}
            },
            'storagePool': {
                'title': 'Storage Pool',
                'description': 'A common provisioning group URI reference',
                'type': 'string',
                'required': True,
                'format': 'x-uri-reference',
                'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                'default': 'FVT_Tbird_reg1_r5'
            },
            'size': {
                'title': 'Capacity',
                'description': 'The capacity of the volume in bytes',
                'type': 'integer',
                'required': True,
                'minimum': 1073741824,
                'maximum': 17592186044416,
                'meta': {'locked': False, 'semanticType': 'capacity'},
                'default': 1073741824,
            },
            'isShareable': {
                'title': 'Is Shareable',
                'description': 'The shareability of the volume',
                'type': 'boolean',
                'meta': {'locked': False},
                'default': False,
            },
            'provisioningType': {
                'title': 'Provisioning Type',
                'description': 'The provisioning type for the volume',
                'type': 'string',
                'enum': ['Thin', 'Full'],
                'meta': {'locked': True, 'createOnly': True},
                'default': 'Full'
            },
            'snapshotPool': {
                'title': 'Snapshot Pool',
                'description': 'A URI reference to the common provisioning group used to create snapshots',
                'type': 'string',
                'format': 'x-uri-reference',
                'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                'default': 'FVT_Tbird_reg1_r5'
            }
        },
    },
    {
        'name': 'VOL-TMP3',
        'description': '',
        'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
        "initialScopeUris": ["Scope:%s" % Scope_List[0]],
        'properties': {
            'storageSystem': 'wpst3par-7200-7-srv',
            'name': {
                'title': 'Volume name',
                'description': 'A volume name between 1 and 100 characters',
                'type': 'string',
                'minLength': 1,
                'maxLength': 100,
                'required': True,
                'meta': {'locked': False}
            },
            'description': {
                'title': 'Description',
                'description': 'A description for the volume',
                'type': 'string',
                'minLength': 0,
                'maxLength': 2000,
                'default': '3Par1 pool1 private',
                'meta': {'locked': False}
            },
            'storagePool': {
                'title': 'Storage Pool',
                'description': 'A common provisioning group URI reference',
                'type': 'string',
                'required': True,
                'format': 'x-uri-reference',
                'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                'default': 'FVT_Tbird_reg1_r6'
            },
            'size': {
                'title': 'Capacity',
                'description': 'The capacity of the volume in bytes',
                'type': 'integer',
                'required': True,
                'minimum': 1073741824,
                'maximum': 17592186044416,
                'meta': {'locked': False, 'semanticType': 'capacity'},
                'default': 1073741824,
            },
            'isShareable': {
                'title': 'Is Shareable',
                'description': 'The shareability of the volume',
                'type': 'boolean',
                'meta': {'locked': False},
                'default': True,
            },
            'provisioningType': {
                'title': 'Provisioning Type',
                'description': 'The provisioning type for the volume',
                'type': 'string',
                'enum': ['Thin', 'Full'],
                'meta': {'locked': True, 'createOnly': True},
                'default': 'Thin'
            },
            'snapshotPool': {
                'title': 'Snapshot Pool',
                'description': 'A URI reference to the common provisioning group used to create snapshots',
                'type': 'string',
                'format': 'x-uri-reference',
                'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                'default': 'FVT_Tbird_reg1_r6'
            }
        },
    },
    {
        'name': 'VOL-TMP4',
        'description': '',
        'rootTemplateUri': 'Volume root template for StoreServ 3.1.3',
        "initialScopeUris": ["Scope:%s" % Scope_List[2]],
        'properties': {
            'storageSystem': 'fvt3par-8400-1-srv',
            'name': {
                'title': 'Volume name',
                'description': 'A volume name between 1 and 100 characters',
                'type': 'string',
                'minLength': 1,
                'maxLength': 100,
                'required': True,
                'meta': {'locked': False}
            },
            'description': {
                'title': 'Description',
                'description': 'A description for the volume',
                'type': 'string',
                'minLength': 0,
                'maxLength': 2000,
                'default': '3Par1 pool1 private',
                'meta': {'locked': False}
            },
            'storagePool': {
                'title': 'Storage Pool',
                'description': 'A common provisioning group URI reference',
                'type': 'string',
                'required': True,
                'format': 'x-uri-reference',
                'meta': {'locked': False, 'createOnly': True, 'semanticType': 'device-storage-pool'},
                'default': 'FC_r1'
            },
            'size': {
                'title': 'Capacity',
                'description': 'The capacity of the volume in bytes',
                'type': 'integer',
                'required': True,
                'minimum': 1073741824,
                'maximum': 17592186044416,
                'meta': {'locked': False, 'semanticType': 'capacity'},
                'default': 1073741824,
            },
            'isShareable': {
                'title': 'Is Shareable',
                'description': 'The shareability of the volume',
                'type': 'boolean',
                'meta': {'locked': False},
                'default': False,
            },
            'provisioningType': {
                'title': 'Provisioning Type',
                'description': 'The provisioning type for the volume',
                'type': 'string',
                'enum': ['Thin', 'Full'],
                'meta': {'locked': True, 'createOnly': True},
                'default': 'Thin'
            },
            'snapshotPool': {
                'title': 'Snapshot Pool',
                'description': 'A URI reference to the common provisioning group used to create snapshots',
                'type': 'string',
                'format': 'x-uri-reference',
                'meta': {'locked': True, 'semanticType': 'device-snapshot-storage-pool'},
                'default': 'FC_r1',
            }
        },
    },
]

Volumes = [
    {
        'properties': {
            'name': 'VOL1',
            'storagePool': 'FVT_Tbird_reg1_r1',
            'storageSystem': 'wpst3par-7200-7-srv',
            'size': 1073741824,
            'provisioningType': 'Thin',
            'isShareable': False,
            'snapshotPool': 'FVT_Tbird_reg1_r1'
        },
        'templateUri': 'VOL-TMP1',
        'isPermanent': True,
        "initialScopeUris": ["Scope:%s" % Scope_List[1],
                             "Scope:%s" % Scope_List[0]]
    },
    {
        'properties': {
            'name': 'VOL2',
            'storagePool': 'FVT_Tbird_reg1_r5',
            'storageSystem': 'wpst3par-7200-7-srv',
            'size': 1073741824,
            'provisioningType': 'Full',
            'isShareable': False,
            'snapshotPool': 'FVT_Tbird_reg1_r5'
        },
        'templateUri': 'VOL-TMP2',
        'isPermanent': True,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        'properties': {
            'name': 'VOL3',
            'storagePool': 'FVT_Tbird_reg1_r6',
            'storageSystem': 'wpst3par-7200-7-srv',
            'size': 1073741824,
            'provisioningType': 'Thin',
            'isShareable': True,
            'snapshotPool': 'FVT_Tbird_reg1_r6',
        },
        'templateUri': 'VOL-TMP3',
        'isPermanent': True,
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
    {
        'properties': {
            'name': 'VOL4',
            'storagePool': 'FC_r1',
            'storageSystem': 'fvt3par-8400-1-srv',
            'size': 1073741824,
            'provisioningType': 'Thin',
            'isShareable': True,
            'snapshotPool': 'FC_r1'
        },
        'templateUri': 'VOL-TMP4',
        'isPermanent': True,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    },
]

SP = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": None,
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "sp1",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "boot": None,
        "bootMode": {"manageMode": False},
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
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": None,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[0],
            "Scope:%s" % Scope_List[1]
        ]
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": None,
        "serverHardwareTypeUri": "SHT:SY 660 Gen9 1",
        "enclosureGroupUri": "EG:EG2",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "sp2",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "boot": None,
        "bootMode": {"manageMode": False},
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
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": None,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": None,
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1",
        "enclosureGroupUri": "EG:EG3",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "sp3",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "boot": None,
        "bootMode": {"manageMode": False},
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
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": None,
        "initialScopeUris": ["Scope:%s" % Scope_List[0]]
    },
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": None,
        "serverHardwareTypeUri": "SHT:SY 480 Gen9 1",
        "enclosureGroupUri": "EG:EG4",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "sp4",
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {"connections": []},
        "boot": None,
        "bootMode": {"manageMode": False},
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
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": None,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]

LIG = ["LIG1", "LIG2", "LIG3", "LIG4", "LIG-Synergy"]

# Error message
invalid_resource_error = "INVALID_RESOURCE"
invalid_scope_error = "INVALID_SCOPE"
not_authorized_error = "NOT_AUTHORIZED_ERROR"
creation_not_authorized_error = "CREATION_NOT_AUTHORIZED_ERROR"
ASSOCIATION_FORBIDDEN_BY_SCOPE = "ASSOCIATION_FORBIDDEN_BY_SCOPE"
AUTHORIZATION = "AUTHORIZATION"
INVALID_NETWORK_ON_STORAGE_PATH = "INVALID_NETWORK_ON_STORAGE_PATH"
STORAGE_POOL_INVALID = "STORAGE_POOL_INVALID"
invalid_protocol = "Invalid_Protocol"
NOT_AUTHORIZED_SCOPE = "NOT_AUTHORIZED_SCOPE"
RESOURCE_NOT_SCOPABLE_ERROR = "RESOURCE_NOT_SCOPABLE_ERROR"

# Patch the scope for resources
Patch_add_Scope0 = [
    {
        "op": "add",
        "path": "/scopeUris/-",
        "value": "Scope:%s" % Scope_List[0]
    }
]
Patch_add_Scope1 = [
    {
        "op": "add",
        "path": "/scopeUris/-",
        "value": "Scope:%s" % Scope_List[1]
    }
]
Patch_add_Scope2 = [
    {
        "op": "add",
        "path": "/scopeUris/-",
        "value": "Scope:%s" % Scope_List[2]
    }
]
Patch_add_Scope3 = [
    {
        "op": "add",
        "path": "/scopeUris/-",
        "value": "Scope:%s" % Scope_List[3]
    }
]
Patch_add_Scope5 = [
    {
        "op": "add",
        "path": "/scopeUris/-",
        "value": "Scope:%s" % Scope_List[5]
    }
]

Patch_remove_Scope0 = [
    {
        "op": "remove",
        "path": "/scopeUris/0"
    }
]
Patch_remove_Scope1 = [
    {
        "op": "remove",
        "path": "/scopeUris/1"
    }
]

Patch_replace_Scope1 = [
    {
        "op": "replace",
        "path": "/refreshState",
        "value": "RefreshPending"
    }
]

# Network SBAC DTO
vlanId = ["101", "102", "103", "104", "105"]
new_ethernet_name = "eth5"
new_fc_name = "fc5"
eth_list = ["eth1", "eth2", "eth3", "eth4"]
fc_list = ["fc1", "fc2", "fc3", "fc4"]
fcoe_list = ["fcoe1", "fcoe2", "fcoe3", "fcoe4"]
new_fcoe_name = "fcoe5"
Update_Ethernet_Name = "eth11"

Create_Ethernet = [
    {
        "vlanId": "101",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": new_ethernet_name,
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[1]
        ]
    }
]
Create_Ethernet2 = [
    {
        "vlanId": "101",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "eth6",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[2]
        ]
    }
]
Create_Ethernet3 = [
    {
        "vlanId": "101",
        "ethernetNetworkType": "Tagged",
        "subnetUri": None,
        "purpose": "General",
        "name": "eth7",
        "smartLink": True,
        "privateNetwork": False,
        "connectionTemplateUri": None,
        "type": ETHERNET_NETWORK_TYPE,
        "initialScopeUris": [
            "Scope:%s" % Scope_List[2],
            "Scope:%s" % Scope_List[1]
        ]
    }
]
Bulk_Create_Ethernet = [
    {
        "vlanIdRange": "101-105",
        "namePrefix": "bulk",
        "privateNetwork": False,
        "smartLink": True,
        "purpose": "General",
        "type": BULK_ETHERNET_NETWORK_TYPE,
        "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500},
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    }
]
Bulk_Create_Ethernet2 = [
    {
        "vlanIdRange": "101-105",
        "namePrefix": "bulk",
        "privateNetwork": False,
        "smartLink": True,
        "purpose": "General",
        "type": BULK_ETHERNET_NETWORK_TYPE,
        "bandwidth": {"maximumBandwidth": 20000, "typicalBandwidth": 2500},
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]
Update_Ethernet = {
    "name": eth_list[0],
    "new_name": "eth6",
    "type": ETHERNET_NETWORK_TYPE
}
Update_Ethernet2 = {
    "name": "eth6",
    "new_name": eth_list[0],
    "type": ETHERNET_NETWORK_TYPE
}
Update_Ethernet3 = {
    "uri": "",
    "name": eth_list[3],
    "new_name": new_ethernet_name,
    "vlanId": 101,
    "ethernetNetworkType": "Tagged",
    "subnetUri": None,
    "purpose": "General",
    "smartLink": True,
    "privateNetwork": True,
    "type": ETHERNET_NETWORK_TYPE,
    "connectionTemplateUri": "123"
}

create_fc_network = [
    {
        "name": new_fc_name,
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    }
]
create_fc_network2 = [
    {
        "name": "fc6",
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]
create_fc_network3 = [
    {
        "name": "fc7",
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": None,
        "type": FC_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[2], "Scope:%s" % Scope_List[1]]
    }
]
update_fc_network = [
    {
        "uri": "",
        "name": "fc6",
        # "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55',
        "type": FC_NETWORK_TYPE
    }
]
update_fc_network2 = [
    {
        "uri": "",
        "name": fc_list[0],
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55',
        "type": FC_NETWORK_TYPE
    }
]
update_fc_network3 = [
    {
        "uri": "",
        "name": "fc7",
        "connectionTemplateUri": None,
        "linkStabilityTime": "30",
        "autoLoginRedistribution": True,
        "fabricType": "FabricAttach",
        "managedSanUri": "FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56",
        "type": FC_NETWORK_TYPE
    }
]

create_fcoe_network = [
    {
        "name": new_fcoe_name,
        "vlanId": "105",
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[1]]
    }
]
create_fcoe_network2 = [
    {
        "name": "fcoe6",
        "vlanId": "105",
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[2]]
    }
]
create_fcoe_network3 = [
    {
        "name": "fcoe7",
        "vlanId": "105",
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": FCOE_NETWORK_TYPE,
        "initialScopeUris": ["Scope:%s" % Scope_List[1], "Scope:%s" % Scope_List[2]]
    }
]
update_fcoe_network = [
    {
        "uri": "123",
        "name": "fcoe6",
        "vlanId": 350,
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": FCOE_NETWORK_TYPE
    }
]
update_fcoe_network2 = [
    {
        "uri": "",
        "name": fcoe_list[0],
        "vlanId": 350,
        "connectionTemplateUri": None,
        "managedSanUri": "FCSan:VSAN350",
        "type": FCOE_NETWORK_TYPE
    }
]
update_fcoe_network3 = [
    {
        "uri": "123",
        "name": "fcoe7",
        "vlanId": 451,
        "connectionTemplateUri": None,
        "managedSanUri": None,
        "type": FCOE_NETWORK_TYPE
    }
]

# Network Sets
new_NS_name = "net-set5"
new_NS_name2 = "net-set6"
network_set_list = ['net-set1', 'net-set2', 'net-set3', 'net-set4']
create_network_set = [{
    "name": new_NS_name,
    "networkUris": [],
    "type": NETWORK_SET_TYPE,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]],
    "nativeNetworkUri": None
}]  # create ns5 test
create_network_set2 = [{
    "name": new_NS_name2,
    "networkUris": [],
    "type": NETWORK_SET_TYPE,
    "initialScopeUris": ["Scope:%s" % Scope_List[2]],
    "nativeNetworkUri": None
}]  # create ns6 stage
create_network_set3 = [{
    "name": new_NS_name2,
    "networkUris": [],
    "type": NETWORK_SET_TYPE,
    "initialScopeUris": ["Scope:%s" % Scope_List[1], "Scope:%s" % Scope_List[2]],
    "nativeNetworkUri": None
}]  # create ns6 stage test
create_network_set4 = [{
    "name": new_NS_name,
    "networkUris": [eth_list[1]],
    "type": NETWORK_SET_TYPE,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]],
    "nativeNetworkUri": None
}]  # create ns5 test eth2
create_network_set5 = [{
    "name": new_NS_name2,
    "networkUris": [eth_list[1], eth_list[2]],
    "type": NETWORK_SET_TYPE,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]],
    "nativeNetworkUri": None
}]  # create ns6 test eth2 eth3
create_network_set6 = [{
    "name": new_NS_name2,
    "networkUris": [eth_list[3]],
    "type": NETWORK_SET_TYPE,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]],
    "nativeNetworkUri": None
}]  # create ns6 test eth4
update_network_set = [{
    "name": network_set_list[0],
    "networkUris": [],
    "add_networkUris": [eth_list[0]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns1 add eth1
update_network_set2 = [{
    "name": network_set_list[1],
    "networkUris": [],
    "add_networkUris": [eth_list[1]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns2 add eth2
update_network_set3 = [{
    "name": network_set_list[1],
    "networkUris": [],
    "add_networkUris": [eth_list[1]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": eth_list[1],
    "uri": ''
}]  # update ns2 add native eth2
update_network_set4 = [{
    "name": network_set_list[1],
    "networkUris": [],
    "delete_networkUris": [eth_list[1]],
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns2 delete eth2
update_network_set5 = [{
    "name": network_set_list[0],
    "networkUris": [],
    "add_networkUris": [eth_list[3]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns1 add eth4
update_network_set6 = [{
    "name": network_set_list[0],
    "networkUris": [],
    "add_networkUris": [eth_list[3]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": eth_list[3],
    "uri": ''
}]  # update ns1 add eth4 native
update_network_set7 = [{
    "name": network_set_list[0],
    "networkUris": [],
    "delete_networkUris": [eth_list[3]],
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns1 delete eth4
update_network_set8 = [{
    "name": network_set_list[3],
    "networkUris": [],
    "add_networkUris": [eth_list[1]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns4 add eth2
update_network_set9 = [{
    "name": network_set_list[1],
    "networkUris": [],
    "add_networkUris": [eth_list[2]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns2 add eth3
update_network_set10 = [{
    "name": network_set_list[1],
    "networkUris": [],
    "add_networkUris": [eth_list[3]],
    "connectionTemplateUri": "",
    "type": NETWORK_SET_TYPE,
    "nativeNetworkUri": None,
    "uri": ''
}]  # update ns2 add eth4

# Enclosure SBAC DTO
new_enc_name = 'CN75120D7B'
enc_name_list = [new_enc_name, 'CN75120D77', 'CN750163KD']
mod_enc_name = 'OVF1592Test'

EG = 'EG1'

edit_users_permission = {
    "sessionID": None,
    "permissionsToActivate": [
        {
            "roleName": "Scope administrator",
            "scopeUri": "Test"
        },
        {
            "roleName": "Server administrator",
            "scopeUri": "Test"
        }
    ]
}

# ServerHardware SBAC DTO
sh_name = 'CN75120D7B, bay 3'
sh_name_list = [
    sh_name,
    'CN75120D7B, bay 5',
    'CN75120D7B, bay 6',
    'CN75120D7B, bay 7',
    'CN75120D7B, bay 8',
    'CN75120D77, bay 1',
    'CN75120D77, bay 5',
    'CN75120D77, bay 6',
    'CN75120D77, bay 7',
    'CN75120D77, bay 8',
    'CN750163KD, bay 1',
    'CN750163KD, bay 5'
]

edit_spa_users_permission = {
    "sessionID": None,
    "permissionsToActivate": [
        {
            "roleName": "Server profile administrator",
            "scopeUri": "Test"
        }
    ]
}

edit_spo_users_permission = {
    "sessionID": None,
    "permissionsToActivate": [
        {
            "roleName": "Server profile operator",
            "scopeUri": "Test"
        }
    ]
}

edit_ia_users_permission = {
    "sessionID": None,
    "permissionsToActivate": [
        {
            "roleName": "Infrastructure administrator",
            "scopeUri": "Test"
        }
    ]
}

edit_na_users_permission = {
    "sessionID": None,
    "permissionsToActivate": [
        {
            "roleName": "Network administrator",
            "scopeUri": "Test"
        }
    ]
}

edit_sa_users_permission = {
    "sessionID": None,
    "permissionsToActivate": [
        {
            "roleName": "Server administrator",
            "scopeUri": "Test"
        }
    ]
}

# Logical Interconnect SBAC DTO
LI1 = 'LE_SYNERGY-LIG-Synergy'

li_name_list = [LI1, ]

li_profile = {
    "type": "telemetry-configuration",
    "sampleInterval": 300,
    "sampleCount": 12,
    "enableTelemetry": False,
    "description": None,
    "name": LI1,
    "category": "telemetry-configurations"
}

li_profile_back = {
    "type": "telemetry-configuration",
    "sampleInterval": 300,
    "sampleCount": 12,
    "enableTelemetry": True,
    "description": None,
    "name": LI1,
    "category": "telemetry-configurations"
}

li_internal_network_add_active1 = ["ETH:%s" % eth_list[1]]
li_internal_network_add_active2 = ["ETH:%s" % eth_list[2]]
li_internal_network_add_inactive = ["ETH:%s" % eth_list[3]]
li_internal_network_remove = []

li_update_dto = {'name': LI1}

# Enclosure Group
new_EG_name = "EG5"
new_EG_name2 = "EG6"
EG_list = ["EG1", "EG2", "EG3", "EG4", "EG-Synergy"]  # exist EG name

create_EG1 = {
    "name": new_EG_name,
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[0],
                         "Scope:%s" % Scope_List[1]]
}  # Test Production EG5

create_EG2 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}  # Stage EG6

create_EG3 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}  # Stage EG6

create_EG4 = {
    "name": new_EG_name,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # create EG5 with LIG2 Test

create_EG5 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[3]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[3]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # create EG6 with LIG4 Test

create_EG6 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[2]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[2]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # create EG6 with LIG3 Test

create_EG7 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}  # Test Production EG1

create_EG8 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}  # Test EG2

Edit_scope_EG = {
    "type": SCOPE_TYPE,
    "name": Scope_List[0],
    "category": "scopes",
    "uri": "",
    "addedResourceUris": [],
    "removedResourceUris": []
}  # add EG5 to scope of production

Edit_EG = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappings": [],
    "ipAddressingMode": "External",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # Edit EG5

Edit_EG1 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": EG_list[0],
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[3]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[3]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # add lig4 to EG1

Edit_EG2 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": EG_list[3],
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappings": [],
    "ipAddressingMode": "External",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # Edit EG4

Edit_EG3 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": EG_list[0],
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # remove lig4 from EG1

Edit_EG5 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # ADD lig2 to EG2

Edit_EG6 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[0]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[0]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # change EG2 to lig1

Edit_EG7 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappings": [],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # remove all lig from EG2

Edit_EG8 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[2]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[2]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # add lig3 to EG2

Edit_EG9 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[3]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[3]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": False,
        "deploymentModeSettings": {
            "deploymentMode": "None",
            "deploymentNetworkUri": None
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # add lig4 to EG5

create_EG_Network1 = {
    "name": new_EG_name,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1],
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1],
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": True,
        "deploymentModeSettings": {
            "deploymentMode": "External",
            "deploymentNetworkUri": eth_list[1]
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # add EG5 eth2

create_EG_Network2 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1],
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1],
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": True,
        "deploymentModeSettings": {
            "deploymentMode": "External",
            "deploymentNetworkUri": eth_list[2]
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # add EG6 eth3

create_EG_Network3 = {
    "name": new_EG_name2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1],
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1],
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "enclosureCount": 3,
    "osDeploymentSettings": {
        "manageOSDeployment": True,
        "deploymentModeSettings": {
            "deploymentMode": "External",
            "deploymentNetworkUri": eth_list[3]
        }
    },
    "powerMode": "RedundantPowerFeed",
    "ambientTemperatureMode": "Standard",
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # add EG6 eth4

Edit_network_EG1 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": True,
        "deploymentModeSettings": {
            "deploymentMode": "External",
            "deploymentNetworkUri": eth_list[1]
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # add eth2 to EG2

Edit_network_EG2 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": True,
        "deploymentModeSettings": {
            "deploymentMode": "External",
            "deploymentNetworkUri": eth_list[2]
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # add eth3 to EG2

Edit_network_EG3 = {
    "type": ENCLOSURE_GROUP_TYPE,
    "uri": "",
    "category": "enclosure-groups",
    "name": new_EG_name,
    "stackingMode": "Enclosure",
    "portMappingCount": 8,
    "portMappings": [],
    "interconnectBayMappingCount": 2,
    "interconnectBayMappings": [
        {
            "interconnectBay": 3,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        },
        {
            "interconnectBay": 6,
            "logicalInterconnectGroupUri": "LIG:" + LIG[1]
        }
    ],
    "ipAddressingMode": "DHCP",
    "ipRangeUris": [],
    "powerMode": "RedundantPowerFeed",
    "description": None,
    "osDeploymentSettings": {
        "manageOSDeployment": True,
        "deploymentModeSettings": {
            "deploymentMode": "External",
            "deploymentNetworkUri": eth_list[3]
        }
    },
    "ambientTemperatureMode": "Standard",
    "enclosureCount": 3,
    "associatedLogicalInterconnectGroups": [],
    "enclosureType": "TClass"
}  # add eth4 to EG2

# Logic Interconnect Group
new_LIG_name = "LIG5"
new_LIG_name2 = "LIG6"
LIG_network_name1 = "uplink"

create_LIG1 = {
    'name': new_LIG_name,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'interconnectMapTemplate': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [],
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # ADD LIG5 Test
create_LIG2 = {
    'name': new_LIG_name2,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'interconnectMapTemplate': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [],
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}  # ADD LIG6  Stage

create_LIG3 = {
    'name': new_LIG_name2,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'interconnectMapTemplate': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [],
    "initialScopeUris": ["Scope:%s" % Scope_List[2], "Scope:%s" % Scope_List[1]]
}

create_LIG_network1 = {
    'name': new_LIG_name,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'internalNetworkUris': [],
    'interconnectMapTemplate': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [
        {
            "networkUris": [eth_list[1]],
            "mode": "Auto",
            "lacpTimer": "Short",
            "primaryPort": None,
            "logicalPortConfigInfos": [],
            "networkType": "Ethernet",
            "ethernetNetworkType": "Tagged",
            "nativeNetworkUri": None,
            "name": LIG_network_name1
        }
    ],
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # ADD LIG6 ETH3

create_LIG_network2 = {
    'name': new_LIG_name2,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'internalNetworkUris': [],
    'interconnectMapTemplate': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [
        {
            "networkUris": [eth_list[2]],
            "mode": "Auto",
            "lacpTimer": "Short",
            "primaryPort": None,
            "logicalPortConfigInfos": [],
            "networkType": "Ethernet",
            "ethernetNetworkType": "Tagged",
            "nativeNetworkUri": None,
            "name": LIG_network_name1
        }
    ],
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # ADD LIG6 ETH3

create_LIG_network3 = {
    'name': new_LIG_name2,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'internalNetworkUris': [],
    'interconnectMapTemplate': [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}],
    'interconnectBaySet': 3,
    'redundancyType': 'Redundant',
    'uplinkSets': [
        {
            "networkUris": [eth_list[3]],
            "mode": "Auto",
            "lacpTimer": "Short",
            "primaryPort": None,
            "logicalPortConfigInfos": [],
            "networkType": "Ethernet",
            "ethernetNetworkType": "Tagged",
            "nativeNetworkUri": None,
            "name": LIG_network_name1
        }
    ],
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # ADD LIG6 ETH4

uplinks_data = [
    {
        'name': 'net_path1', 'networkType': 'Ethernet', 'ethernetNetworkType': 'Tagged',
        'networkUris': [eth_list[1]], 'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
    },
    {
        'name': 'net_path1', 'networkType': 'Ethernet', 'nativeNetworkUri': eth_list[1],
        'ethernetNetworkType': 'Tagged', 'networkUris': [eth_list[1]], 'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
    },
    {
        'name': 'net_path2', 'networkType': 'Ethernet', 'networkUris': [eth_list[2]],
        'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
    },
    {
        'name': 'net_path3', 'networkType': 'Ethernet', 'networkUris': [eth_list[3]],
        'ethernetNetworkType': 'Tagged', 'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
    },
    {
        'name': 'net_path4', 'networkType': 'Ethernet', 'nativeNetworkUri': eth_list[3],
        'ethernetNetworkType': 'Tagged', 'networkUris': [eth_list[3]], 'mode': 'Auto',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'}]
    }
]

update_lig1 = [
    {
        'name': new_LIG_name,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [], 'interconnectBaySet': 3, 'redundancyType': 'Redundant',
        'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration',
            'uri': None
        }
    }
]  # Edit LIG5
update_lig2 = [
    {
        'name': LIG[3], 'type': LOGICAL_INTERCONNECT_GROUP_TYPE, 'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [], 'interconnectBaySet': 3, 'redundancyType': 'Redundant',
        'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None, 'category': 'qos-aggregated-configuration',
            'uri': None
        }
    }
]  # Edit LIG4
Edit_lig_network1 = [
    {
        'name': new_LIG_name,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [uplinks_data[0]],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [],
        'interconnectBaySet': 3, 'redundancyType': 'Redundant', 'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None,
            'category': 'qos-aggregated-configuration', 'uri': None
        }
    }
]
# add eth2 to LIG5
Edit_lig_network2 = [
    {
        'name': new_LIG_name,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [uplinks_data[1]],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [],
        'interconnectBaySet': 3, 'redundancyType': 'Redundant', 'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None,
            'category': 'qos-aggregated-configuration', 'uri': None
        }
    }
]  # add eth2 native to LIG5
Edit_lig_network3 = [
    {
        'name': new_LIG_name,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [],
        'interconnectBaySet': 3, 'redundancyType': 'Redundant', 'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None,
            'category': 'qos-aggregated-configuration', 'uri': None
        }
    }
]
# delete eth2 from LIG5
Edit_lig_network4 = [
    {
        'name': new_LIG_name,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [uplinks_data[2]],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [],
        'interconnectBaySet': 3, 'redundancyType': 'Redundant', 'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None,
            'category': 'qos-aggregated-configuration', 'uri': None
        }
    }
]
# add eth3 to LIG5
Edit_lig_network5 = [
    {
        'name': new_LIG_name,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'ethernetSettings': None, 'description': None,
        'uplinkSets': [uplinks_data[3]],
        'interconnectMapTemplate': [
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 3, 'enclosure': 1, 'enclosureIndex': 1
            },
            {
                'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
                'bay': 6, 'enclosure': 1, 'enclosureIndex': 1
            }
        ],
        'internalNetworkUris': [],
        'interconnectBaySet': 3, 'redundancyType': 'Redundant', 'enclosureIndexes': [1],
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration', 'configType': 'Passthrough',
                'downlinkClassificationType': None, 'uplinkClassificationType': None,
                'qosTrafficClassifiers': None, 'description': None, 'status': None,
                'name': None, 'state': None, 'category': 'qos-aggregated-configuration',
                'created': None, 'modified': None, 'eTag': None, 'uri': None
            },
            'inactiveFCoEQosConfig': None, 'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration', 'name': None, 'state': None, 'status': None,
            'eTag': None, 'modified': None, 'created': None,
            'category': 'qos-aggregated-configuration', 'uri': None
        }
    }
]
# add eth4 to LIG5
Edit_lig_network6 = [
    {
        'name': LIG[0],
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'enclosureIndexes': [1, 2, 3],
        'ethernetSettings': None,
        'uplinkSets': [uplinks_data[3]],
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'internalNetworkUris': [],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration',
                'configType': 'Passthrough',
                'downlinkClassificationType': None,
                'uplinkClassificationType': None,
                'qosTrafficClassifiers': None,
                'description': None,
                'status': None,
                'name': None,
                'state': None,
                'category': 'qos-aggregated-configuration',
                'created': None,
                'modified': None,
                'eTag': None,
                'uri': None
            },
            'inactiveFCoEQosConfig': None,
            'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration',
            'name': None,
            'state': None,
            'status': None,
            'eTag': None,
            'modified': None,
            'created': None,
            'category': 'qos-aggregated-configuration',
            'uri': None
        }
    }
]
Edit_lig_network7 = [
    {
        'name': LIG[0],
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'enclosureIndexes': [1, 2, 3],
        'ethernetSettings': None,
        'uplinkSets': [],
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'internalNetworkUris': [],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration',
                'configType': 'Passthrough',
                'downlinkClassificationType': None,
                'uplinkClassificationType': None,
                'qosTrafficClassifiers': None,
                'description': None,
                'status': None,
                'name': None,
                'state': None,
                'category': 'qos-aggregated-configuration',
                'created': None,
                'modified': None,
                'eTag': None,
                'uri': None
            },
            'inactiveFCoEQosConfig': None,
            'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration',
            'name': None,
            'state': None,
            'status': None,
            'eTag': None,
            'modified': None,
            'created': None,
            'category': 'qos-aggregated-configuration',
            'uri': None
        }
    }
]
Edit_lig_network8 = [
    {
        'name': LIG[0],
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'enclosureIndexes': [1, 2, 3],
        'ethernetSettings': None,
        'uplinkSets': [uplinks_data[4]],
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'internalNetworkUris': [],
        'interconnectBaySet': 3, 'redundancyType': 'HighlyAvailable',
        'qosConfiguration': {
            'activeQosConfig': {
                'type': 'QosConfiguration',
                'configType': 'Passthrough',
                'downlinkClassificationType': None,
                'uplinkClassificationType': None,
                'qosTrafficClassifiers': None,
                'description': None,
                'status': None,
                'name': None,
                'state': None,
                'category': 'qos-aggregated-configuration',
                'created': None,
                'modified': None,
                'eTag': None,
                'uri': None
            },
            'inactiveFCoEQosConfig': None,
            'inactiveNonFCoEQosConfig': None,
            'type': 'qos-aggregated-configuration',
            'name': None,
            'state': None,
            'status': None,
            'eTag': None,
            'modified': None,
            'created': None,
            'category': 'qos-aggregated-configuration',
            'uri': None
        }
    }
]
Edit_lig_network9 = [
    {
        'name': LIG[1],
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': None,
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [uplinks_data[0]]
    }
]

# Interconnects DTO
Patch_inter_power = [{"op": "replace", "path": "/powerState", "value": "Off"}]  # power off
Patch_inter_reset = [{"op": "replace", "path": "/deviceResetState", "value": "Reset"}]  # reset
interconects_list = ["%s, interconnect 1" % enclosure[1],
                     "%s, interconnect 3" % enclosure[0],
                     "%s, interconnect 4" % enclosure[1],
                     "%s, interconnect 6" % enclosure[1]]
interconect_name = [{"name": interconects_list[1]},
                    {"name": interconects_list[3]}]

update_IC = {
    "associatedUplinkSetUri": None,
    "interconnectName": interconects_list[1],
    "portType": "Downlink",
    "portHealthStatus": "Normal",
    "capability": ["Ethernet"],
    "configPortTypes": ["Ethernet"],
    "enabled": True,
    "portName": "d1",
    "portStatus": "Unlinked",
    "type": INTERCONNECT_PORT_TYPE
}  # Edit IC3

update_IC2 = {
    "associatedUplinkSetUri": None,
    "interconnectName": interconects_list[3],
    "portType": "Downlink",
    "portHealthStatus": "Normal",
    "capability": ["Ethernet"],
    "configPortTypes": ["Ethernet"],
    "enabled": True,
    "portName": "d1",
    "portStatus": "Linked",
    "type": INTERCONNECT_PORT_TYPE
}
# Edit IC4
DownLinkPort = 'd1'
UpLinkPort = 'None'

# Scope
new_scope_name = "Scope5"
new_scope_name_update = "Scope55"
new_scope_name2 = "Scope6"
new_scope_name3 = "Scope7"
create_scope1 = {
    "name": new_scope_name,
    "type": SCOPE_TYPE,
    "addedResourceUris": [],
    "removedResourceUris": [],
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}
create_scope2 = {
    "name": new_scope_name2,
    "type": SCOPE_TYPE,
    "addedResourceUris": [],
    "removedResourceUris": [],
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}
create_scope3 = {
    "name": new_scope_name3,
    "type": SCOPE_TYPE,
    "addedResourceUris": [],
    "removedResourceUris": [],
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}
create_scope4 = {
    "name": new_scope_name3,
    "type": SCOPE_TYPE,
    "addedResourceUris": [],
    "removedResourceUris": [],
    "initialScopeUris": ["Scope:%s" % Scope_List[2], "Scope:%s" % Scope_List[1]]
}

#  Uplink sets
LI = [LI1, ]
uplink_name = "US1"
uplink_name2 = "US2"
uplink_name3 = "US3"

add_Uplinksets = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [],
    "portConfigInfos": [],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}

# add an empty uplink to LI

add_Uplinksets1 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": ["ETH:%s" % eth_list[1]],
    "portConfigInfos": [
        {
            "desiredSpeed": "Auto",
            "location": {
                "locationEntries": [
                    {"value": "Q1", "type": "Port"},
                    {"value": 3, "type": "Bay"},
                    {
                        "value": "Enclosure:%s" % enclosure[0],
                        "type": "Enclosure"
                    }
                ]
            }
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}  # add eth2 uplink to LI

add_Uplinksets2 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": ["ETH:%s" % eth_list[2]],
    "portConfigInfos": [
        {
            "desiredSpeed": "Auto",
            "location": {
                "locationEntries": [
                    {"value": "Q2", "type": "Port"},
                    {"value": 3, "type": "Bay"},
                    {
                        "value": "Enclosure:%s" % enclosure[0],
                        "type": "Enclosure"
                    }
                ]
            }
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}  # add eth3 uplink2 to LI

add_Uplinksets3 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": ["ETH:%s" % eth_list[3]],
    "portConfigInfos": [
        {
            "desiredSpeed": "Auto",
            "location": {
                "locationEntries": [
                    {"value": "Q3", "type": "Port"},
                    {"value": 3, "type": "Bay"},
                    {
                        "value": "Enclosure:%s" % enclosure[0],
                        "type": "Enclosure"
                    }
                ]
            }
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}

update_Uplinksets = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [],
    "portConfigInfos": [],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}

update_Uplinksets1 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [eth_list[1]],
    "portConfigInfos": [
        {
            'enclosure': enclosure[0],
            'bay': '3',
            'port': 'Q1',
            'desiredSpeed': 'Auto'
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}

update_Uplinksets2 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [eth_list[2]],
    "portConfigInfos": [{
        'enclosure': enclosure[0],
        'bay': '3',
        'port': 'Q1',
        'desiredSpeed': 'Auto'
    }],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}  # add eth3 uplink2 to LI

update_Uplinksets3 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [eth_list[3]],
    "portConfigInfos": [
        {
            'enclosure': enclosure[0],
            'bay': '3',
            'port': 'Q1',
            'desiredSpeed': 'Auto'
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": None,
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}  # add eth4 uplink2 to LI

update_Uplinksets4 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [eth_list[1]],
    "portConfigInfos": [
        {
            'enclosure': enclosure[0],
            'bay': '3',
            'port': 'Q1',
            'desiredSpeed': 'Auto'
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": "ETH:%s" % eth_list[1],
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}  # edit eth2's "native" on LI

update_Uplinksets5 = {
    "type": UPLINK_SET_TYPE,
    "name": uplink_name,
    "networkUris": [eth_list[3]],
    "portConfigInfos": [
        {
            'enclosure': enclosure[0],
            'bay': '3',
            'port': 'Q1',
            'desiredSpeed': 'Auto'
        }
    ],
    "networkType": "Ethernet",
    "manualLoginRedistributionState": "NotSupported",
    "logicalInterconnectUri": "LI:" + LI[0],
    "connectionMode": "Auto",
    "lacpTimer": "Short",
    "nativeNetworkUri": "ETH:%s" % eth_list[3],
    "fcNetworkUris": [],
    "fcoeNetworkUris": [],
    "ethernetNetworkType": "Tagged"
}  # edit eth4's "native" on LI

# server profile SBAC
sp_list = ["sp1", "sp2", "sp3", "sp4"]
new_sp_name = "sp5"  # OVF1592 use the name when create a new server profiles
new_sp_name2 = "sp6"  # OVF1592 use the name when create a new server profiles
new_sp_name3 = "sp7"  # OVF1592 use the name when create a new server profiles

serverHardware1 = "%s, bay 7" % enclosure[0]  # Create sp1
serverHardware2 = "%s, bay 5" % enclosure[0]  # Create sp2
serverHardware3 = "%s, bay 5" % enclosure[1]  # Create sp3
serverHardware4 = "%s, bay 1" % enclosure[1]  # Create sp4
serverHardware5 = "%s, bay 3" % enclosure[0]  # Create sp5

serverHardwaretype = "SY 660 Gen9 1"  # enclosure2 Test Production

create_server_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": "EG:%s" % EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # create sp5 Test

create_sp_neg_1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": "EG:%s" % EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name2,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[2]]
}  # create sp6 stage

create_sp_neg_2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": "EG:%s" % EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name2,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1],
                         "Scope:%s" % Scope_List[2]],
}  # create sp6 stage

Edit_server_profile_base = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": None,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": "EG:EG2",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_server_profile = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": "EG:%s" % EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}  # Edit sp1 to sp7

Edit_server_profile2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": None,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": "EG:EG1",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name3,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_server_profile3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": None,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": "EG%s" % EG_list[0],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[3],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}  # Edit sp4

# Associated with EG/SH/Enc
create_server_profile_EG1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": None,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": EG_list[1],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # create sp5 Test server hardware EG2

create_server_profile_EG2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": None,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": EG_list[3],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # create sp5 Test server hardware EG4

create_server_profile_EG3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # add sp5 Test server hardware EG4 SH2

create_server_profile_EG4 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "enclosureUri": "ENC:%s" % enc_name_list[1],
    "enclosureBay": 3,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # add sp5 Test server hardware EG4 SH2

Edit_server_profile_EG1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}  # Edit sp2 to EG-Synergy

Edit_server_profile_EG2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}

Edit_server_profile_EG3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareTypeUri": serverHardwaretype,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "enclosureUri": "ENC:%s" % enc_name_list[1],
    "enclosureBay": 3,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}

create_server_profile_SH1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware3,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}  # add sp5 Test server hardware EG4 SH2

create_server_profile_SH2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware4,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_server_profile_SH1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware3,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}

Edit_server_profile_SH2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware4,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None
}

# Associated with networks
# 1. Ethernet
lig_original = [
    {
        'name': 'LIG-Synergy',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [],
    }
]
eth_uplink_sets = [
    {
        "name": "eth-path1",
        "networkUris": [eth_list[0]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q1.1"
            },
        ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
    {
        "name": "eth-path2",
        "networkUris": [eth_list[1]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q2.1"
            },
        ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
    {
        "name": "eth-path3",
        "networkUris": [eth_list[2]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q3.1"
            }, ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
    {
        "name": "eth-path4",
        "networkUris": [eth_list[3]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q4.1"
            },
        ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
]

lig_eth_path = [
    {
        'name': 'LIG-Synergy',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': eth_uplink_sets,
    },
]

create_sp_network1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[1],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_network2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[2],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_network3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[3],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_sp_network_base = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_network1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[1],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_network2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[2],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_network3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware3,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[3],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_network4 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:%s" % eth_list[0],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_network_port1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "ETH:%s" % eth_list[0],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_network_port2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "ETH:%s" % eth_list[3],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

# 2. FC
fc_uplink_sets = [
    {
        "name": "FA-path1",
        "networkUris": [fc_list[0]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q1.1"
            }, ],
        "networkType": "FibreChannel",
        "ethernetNetworkType": None,
        "nativeNetworkUri": None,
    },
    {
        "name": "FA-path2",
        "networkUris": [fc_list[1]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q2.1"
            }, ],
        "networkType": "FibreChannel",
        "ethernetNetworkType": None,
        "nativeNetworkUri": None,
    },
    {
        "name": "FA-path3",
        "networkUris": [fc_list[2]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q3.1"
            }, ],
        "networkType": "FibreChannel",
        "ethernetNetworkType": None,
        "nativeNetworkUri": None,
    },
    {
        "name": "FA-path4",
        "networkUris": [fc_list[3]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q4.1"
            }, ],
        "networkType": "FibreChannel",
        "ethernetNetworkType": None,
        "nativeNetworkUri": None,
    },
]

lig_fc_path = [
    {
        'name': 'LIG-Synergy',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': fc_uplink_sets,
    },
]

create_sp_fc1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[1],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_fc2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[2],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_fc3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[3],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_sp_fc_base = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fc1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[1],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fc2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[2],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fc3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware3,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[3],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fc4 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FC:%s" % fc_list[0],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fc_port1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "FC:%s" % fc_list[0],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fc_port2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "FC:%s" % fc_list[3],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

# 2. FCoE
fcoe_uplink_sets = [
    {
        "name": "fcoe-path1",
        "networkUris": [fcoe_list[0]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q1.1"
            },
        ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
    {
        "name": "fcoe-path2",
        "networkUris": [fcoe_list[1]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q2.1"
            },
        ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
    {
        "name": "fcoe-path3",
        "networkUris": [fcoe_list[2]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q3.1"
            }, ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
    {
        "name": "fcoe-path4",
        "networkUris": [fcoe_list[3]],
        "mode": "Auto",
        "lacpTimer": "Short",
        "primaryPort": None,
        "logicalPortConfigInfos": [
            {
                "bay": 3,
                "enclosure": 1,
                "port": "Q4.1"
            },
        ],
        "networkType": "Ethernet",
        "ethernetNetworkType": "Tagged",
        "nativeNetworkUri": None,
    },
]

lig_fcoe_path = [
    {
        'name': 'LIG-Synergy',
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap['LIG_POTASH'],
        'enclosureIndexes': [1, 2, 3],
        'interconnectBaySet': 3,
        'redundancyType': 'HighlyAvailable',
        'fcoeSettings': {'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': fcoe_uplink_sets,
    },
]

create_sp_fcoe1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[1],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_fcoe2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[2],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_fcoe3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[3],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_sp_fcoe_base = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fcoe1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[1],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fcoe2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[2],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fcoe3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware3,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[3],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fcoe4 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "FCOE:%s" % fcoe_list[0],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fcoe_port1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "FCOE:%s" % fcoe_list[0],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_fcoe_port2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "FibreChannel",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "FCOE:%s" % fcoe_list[3],
                "ipv4": {
                    "ipAddressSource": None,
                    "subnetMask": None,
                    "gateway": None,
                    "ipAddress": None
                },
            }
        ]
    },
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

# 3.network-sets.
network_sets_for_sp = [
    {
        "name": network_set_list[0],
        "networkUris": [],
        "add_networkUris": [eth_list[0]],
        "delete_networkUris": [eth_list[3]],
        "connectionTemplateUri": "",
        "type": NETWORK_SET_TYPE,
        "nativeNetworkUri": None,
        "uri": ''
    },
    {
        "name": network_set_list[1],
        "networkUris": [],
        "add_networkUris": [eth_list[1]],
        "connectionTemplateUri": "",
        "type": NETWORK_SET_TYPE,
        "nativeNetworkUri": None,
        "uri": ''
    },
    {
        "name": network_set_list[2],
        "networkUris": [],
        "add_networkUris": [eth_list[2]],
        "connectionTemplateUri": "",
        "type": NETWORK_SET_TYPE,
        "nativeNetworkUri": None,
        "uri": ''
    },
    {
        "name": network_set_list[3],
        "networkUris": [],
        "add_networkUris": [eth_list[3]],
        "connectionTemplateUri": "",
        "type": NETWORK_SET_TYPE,
        "nativeNetworkUri": None,
        "uri": ''
    },
]

create_sp_netsets1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[1],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_netsets2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[2],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_sp_netsets3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "eth1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[3],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_sp_netsets_base = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_netsets1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[1],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_netsets2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[2],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_netsets3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware3,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[3],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_netsets4 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "NS:%s" % network_set_list[0],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_netsets_port1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "NS:%s" % network_set_list[0],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

Edit_sp_netsets_port2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "con1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2600",
                "networkUri": "NS:%s" % network_set_list[3],
                "requestedVFs": "0",
                "ipv4": {},
                "boot": {
                    "priority": "NotBootable",
                    "iscsi": {}
                }
            }]
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "HardDisk", "PXE"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "secureBoot": "Unmanaged"
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
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": None,
}

# Associated with Volume
vol_list = ["VOL1", "VOL2", "VOL3", "VOL4"]

create_server_profile_volume1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + vol_list[1],
            "isBootVolume": False,
            "lunType": "Auto",
            "lun": None,
            "volume": {},
            "storagePaths": [],
        }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_volume2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + vol_list[2],
            "isBootVolume": False,
            "lunType": "Auto",
            "lun": None,
            "volume": {},
            "storagePaths": [],
        }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_volume3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + vol_list[3],
            "isBootVolume": False,
            "lunType": "Auto",
            "lun": None,
            "volume": {},
            "storagePaths": [],
        }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_server_profile_volume1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + vol_list[1],
            "isBootVolume": False,
            "lunType": "Auto",
            "lun": None,
            "volume": {},
            "storagePaths": []
        }]
    },
}

Edit_server_profile_volume2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + vol_list[2],
            "isBootVolume": False,
            "lunType": "Auto",
            "lun": None,
            "volume": {},
            "storagePaths": []
        }]
    },
}

Edit_server_profile_volume3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "volumeUri": "SVOL:" + vol_list[3],
            "isBootVolume": False,
            "lunType": "Auto",
            "lun": None,
            "volume": {},
            "storagePaths": []
        }]
    },
}

# Associated with storage pool
vol_tmp_list = ["VOL-TMP1", "VOL-TMP2", "VOL-TMP3", "VOL-TMP4"]
pool_list = ["FVT_Tbird_reg1_r1", "FVT_Tbird_reg1_r5", "FVT_Tbird_reg1_r6", "FC_r1"]
new_vol_name = "VOL5"
# new_vol_name2 = "VOL6"
new_volumes_list = [{"properties": {"name": new_vol_name}}]
Storage_Systems1 = "wpst3par-7200-7-srv"
Storage_Systems2 = "fvt3par-8400-1-srv"

create_server_profile_pool1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems1,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[1],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "ROOT:" + pool_list[1],
                    "isPermanent": True
                }
            }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_pool2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems1,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[2],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "ROOT:" + pool_list[2],
                    "isPermanent": True
                }
            }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_pool3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems2,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[3],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "ROOT:" + pool_list[3],
                    "isPermanent": True
                }
            }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_pool4 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems1,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[1],
                        "size": 1073741824,
                        "provisioningType": "Full",
                        "isShareable": False
                    },
                    "templateUri": "SVT:" + vol_tmp_list[1],
                    "isPermanent": True
                }
            }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_pool5 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems1,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[2],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": True
                    },
                    "templateUri": "SVT:" + vol_tmp_list[2],
                    "isPermanent": True
                }
            }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

create_server_profile_pool6 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems2,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[3],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "SVT:" + vol_tmp_list[1],
                    "isPermanent": True
                }
            }]
    },
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_server_profile_pool1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems1,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[1],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "ROOT:" + pool_list[1],
                    "isPermanent": True
                }
            }]
    },
}

Edit_server_profile_pool2 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems1,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[2],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "ROOT:" + pool_list[2],
                    "isPermanent": True
                }
            }]
    },
}

Edit_server_profile_pool3 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "volumeUri": None,
                "isBootVolume": False,
                "lunType": "Auto",
                "lun": None,
                "storagePaths": [],
                "volumeStorageSystemUri": "SSYS:" + Storage_Systems2,
                "volume": {
                    "properties": {
                        "name": new_vol_name,
                        "storagePool": "SPOOL:" + pool_list[3],
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False
                    },
                    "templateUri": "ROOT:" + pool_list[3],
                    "isPermanent": True
                }
            }]
    },
}

# Association with Drive Enclosure
drive_enc = "CN75120D7B, bay 1"
create_server_profile_de1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware5,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": new_sp_name,
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [
            {
                "id": 1,
                "deviceSlot": "Mezz 1",
                "name": "test",
                "numPhysicalDrives": 2,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
            }
        ],
        "controllers": [
            {
                "logicalDrives": [
                    {
                        "name": None,
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": None,
                        "driveTechnology": None,
                        "sasLogicalJBODId": 1,
                        "driveNumber": None
                    }
                ],
                "deviceSlot": "Mezz 1",
                "mode": "RAID",
                "initialize": False,
                "importConfiguration": False
            }
        ]
    },
    "sanStorage": None,
    "initialScopeUris": ["Scope:%s" % Scope_List[1]]
}

Edit_server_profile_de1 = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": serverHardware2,
    "enclosureGroupUri": EG_list[4],
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": sp_list[1],
    "affinity": "Bay",
    "connectionSettings": {"connections": []},
    "boot": None,
    "bootMode": {"manageMode": False},
    "firmware": {
        "manageFirmware": False,
        "forceInstallFirmware": False,
        "firmwareInstallType": None,
        "firmwareActivationType": "Immediate"
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [
            {
                "id": 1,
                "deviceSlot": "Mezz 1",
                "name": "test",
                "numPhysicalDrives": 2,
                "driveMinSizeGB": 146,
                "driveMaxSizeGB": 146,
                "driveTechnology": "SasHdd",
                "eraseData": False,
            }
        ],
        "controllers": [
            {
                "logicalDrives": [
                    {
                        "name": None,
                        "raidLevel": "RAID1",
                        "bootable": False,
                        "numPhysicalDrives": None,
                        "driveTechnology": None,
                        "sasLogicalJBODId": 1,
                        "driveNumber": None
                    }
                ],
                "deviceSlot": "Mezz 1",
                "mode": "RAID",
                "initialize": False,
                "importConfiguration": False
            }
        ]
    },
    "sanStorage": None,
}

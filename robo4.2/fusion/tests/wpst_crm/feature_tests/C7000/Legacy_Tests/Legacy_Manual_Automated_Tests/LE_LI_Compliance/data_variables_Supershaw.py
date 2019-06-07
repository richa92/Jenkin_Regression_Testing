def make_range_list(vrange):
    rlist = []
    for x in xrange(vrange['start'], (vrange['end'] + 1)):
        rlist.append(vrange['prefix'] + str(x) + vrange['suffix'])
    return rlist


SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password


FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

SWITCH_USERNAME = 'admin'
SWITCH_PASSWORD = 'wpsthpvse1'
SWITCH_PROMPT = '>'
SWITCH_TIMEOUT = 300

IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

ethernet_networks = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork1",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "wpstnetwork2",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    }
]

Fc_body = {"type": "fc-networkV4",
           "name": "DATAAUTOMATED2",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }

Li_body = {"type": "telemetry-configuration",
           "enableTelemetry": True,
           "sampleCount": 20,
           "sampleInterval": 200,
           "description": None,
           "status": None,
           "name": "",
           "state": None,
           "eTag": None,
           "created": None,
           "modified": None,
           "category": "telemetry-configurations",
           "uri": ""}

users = [{'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Network administrator', 'scopeUri': None}]},
         {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Server administrator', 'scopeUri': None}]},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Backup administrator', 'scopeUri': None}]},
         {'userName': 'Readonly', 'password': 'Readonly', 'fullName': 'Readonly', 'emailAddress': 'Readonly@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions', 'enabled': True, 'permissions': [{'roleName': 'Read only', 'scopeUri': None}]}
         ]

LIG_body = [{'name': 'LIG-COMP-SS1',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric-20/40 F8 Module'}
                                         ],
             'uplinkSets': [{'name': 'ss-comp-ug1',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['wpstnetwork1'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                        {'bay': '2', 'port': 'X3', 'speed': 'Auto'}
                                                        ]

                             }
                            ],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None},

            {'name': 'LIG-COMP-SS2',
             'type': 'logical-interconnect-groupV6',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC Flex-10/10D Module'},
                                         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC Flex-10/10D Module'}
                                         ],
             'uplinkSets': [{'name': 'ss-comp-ug2',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['wpstnetwork2'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'logicalPortConfigInfos': [{'bay': '3', 'port': 'X1', 'speed': 'Auto'},
                                                        {'bay': '4', 'port': 'X9', 'speed': 'Auto'}]

                             }
                            ],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None}]


Authorization_Login = [{'userName': 'Backupadmin', 'password': 'Backupadmin'},
                       {'userName': 'Readonly', 'password': 'Readonly'}
                       ]

EditTelemetryNoPriv_users = [{'userName': 'Serveradmin', 'password': 'Serveradmin'},
                             {'userName': 'Readonly', 'password': 'Readonly'},
                             {'userName': 'Backupadmin', 'password': 'Backupadmin'}
                             ]


Enclosure_Name1 = 'aus-c7000-188'

li2_uplink_set_Edit = {'name': 'ss-comp-ug2',
                       'ethernetNetworkType': None,
                       'networkType': 'Ethernet',
                       'networkUris': ['wpstnetwork2'],
                       'fcNetworkUris': [],
                       'fcoeNetworkUris': [],
                       'lacpTimer': 'Short',
                       'logicalInterconnectUri': None,
                       'primaryPortLocation': None,
                       'manualLoginRedistributionState': 'NotSupported',
                       'connectionMode': 'Auto',
                       'nativeNetworkUri': None,
                       'portConfigInfos': [{'bay': '3', 'port': 'X9', 'desiredSpeed': 'Auto', 'enclosure': Enclosure_Name1}]}


eg_body1 = {'name': 'config4-group',
            'ipRangeUris': [],
            'enclosureCount': 1,
            'osDeploymentSettings': None,
            'configurationScript': '',
            'powerMode': None,
            'ambientTemperatureMode': 'Standard',
            'interconnectBayMappings':
            [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS1'},
             {'interconnectBay': 2, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS1'},
             {'interconnectBay': 3, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS2'},
             {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:LIG-COMP-SS2'}
             ]}

encs = [{'hostname': '15.186.2.227', 'username': 'Administrator', 'password': 'Compaq123', 'enclosureGroupUri': 'EG:config4-group', 'force': False, 'licensingIntent': 'OneViewNoiLO'}]

LI1 = 'aus-c7000-188-LIG-COMP-SS1'
LI2 = 'aus-c7000-188-LIG-COMP-SS2'

bay_no = 5

Li_body_Disable = {"type": "telemetry-configuration",
                   "enableTelemetry": False,
                   "sampleCount": 12,
                   "sampleInterval": 200,
                   "description": None,
                   "status": None,
                   "name": "",
                   "state": None,
                   "eTag": None,
                   "created": None,
                   "modified": None,
                   "category": "telemetry-configurations",
                   "uri": ""}

snmp_body = {'enabled': False,
             'type': 'snmp-configuration'}

IGMP_body = {'enableIgmpSnooping': True,
             'type': 'EthernetInterconnectSettingsV5',
             'id': ''}

IGMP_body_False = {'enableIgmpSnooping': False,
                   'type': 'EthernetInterconnectSettingsV5',
                   'id': ''}

IGMP_enableFastMacCacheFailover = {'enableFastMacCacheFailover': False,
                                   'type': 'EthernetInterconnectSettingsV5',
                                   'id': ''}

IGMP_macRefreshInterval = {'macRefreshInterval': 10,
                           'type': 'EthernetInterconnectSettingsV5',
                                   'id': ''}


IGMP_igmpIdleTimeoutInterval = {'igmpIdleTimeoutInterval': 100,
                                'type': 'EthernetInterconnectSettingsV5',
                                'id': ''}


SP_body1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': Enclosure_Name1 + ', bay 5',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + Enclosure_Name1, 'enclosureGroupUri': 'EG:config4-group', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
             'name': 'Profile1', 'description': '', 'affinity': 'Bay',
             'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:wpstnetwork1',
                                                     'boot': None, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                                    ]},
             'boot': None, 'bios': {'manageBios': False, 'overriddenSettings': []}, 'sanStorage': None}]


alert1 = 'The logical interconnect is inconsistent with the logical interconnect group LIG-COMP-SS1.'

alert2 = 'The logical interconnect is inconsistent with the logical interconnect group LIG-COMP-SS2.'

li_US = {"type": "uplink-setV5", "name": "ss-comp-add", "networkUris": [],
         "portConfigInfos": [{"desiredSpeed": "Auto", "location": {"locationEntries": [{"value": "X9", "type": "Port"},
                                                                                       {"value": 3, "type": "Bay"},
                                                                                       {"value": "", "type": "Enclosure"}
                                                                                       ]}}],
         "ethernetNetworkType": "Tagged",
         "networkType": "Ethernet",
         "primaryPortLocation": None,
         "reachability": None,
         "manualLoginRedistributionState": "NotSupported",
         "logicalInterconnectUri": [],
         "connectionMode": "Auto",
         "lacpTimer": "Short",
         "nativeNetworkUri": None,
         "fcNetworkUris": [],
         "fcoeNetworkUris": [],
         "state": None,
         "description": None,
         "status": None,
         "uri": None,
         "category": None,
         "modified": None,
         "created": None,
         "eTag": None}

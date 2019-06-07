'''
Plexxi Data File For OVF6392
'''
appliance_ip = '15.186.25.224'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

plexxi_connect_host = '15.186.25.208'
plexxi_credentials = {'userName': 'admin', 'password': 'plexxi'}
Fabric_name = 'plexxi_fabric'
plexxi_switches = [
    {'name': 'plexxiR1S1', 'ip': '15.186.12.49'},
    {'name': 'plexxiR1S2', 'ip': '15.186.12.50'},
    {'name': 'plexxiR2S1', 'ip': '15.186.12.59'},
    {'name': 'plexxiR2S2', 'ip': '15.186.12.60'},
    {'name': 'plexxiR3S1', 'ip': '15.186.12.69'},
    {'name': 'plexxiR3S2', 'ip': '15.186.12.70'}
]

DL_Servers = [
    {'name': 'ILOMXQ82505G2.us.rdlabs.hpecorp.net', 'IP': '15.186.24.77'},
    {'name': 'ILOMXQ7340093.us.rdlabs.hpecorp.net', 'IP': '15.186.18.64'},
]
DL_Body = {
    "username": "Administrator",
    "password": "hpvse123",
    "force": True,
    "licensingIntent": "OneView",
    # "licensingIntent":"OneViewNoiLO",
    "configurationState": "Managed",
}

oneview_config = {
    "host": appliance_ip,
    "username": admin_credentials['userName'],
    "password": admin_credentials['password'],
    "enabled": True,
    "verify_ssl": True,
    "name": "HPE OneView Configuration"
}

networks = {
    'namePrefix': 'net',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    "bandwidth": {
        "maximumBandwidth": 20000,
        "typicalBandwidth": 2500
    },
    'type': 'bulk-ethernet-networkV2'
}

Fabric_claim = [{"op": "replace", "path": "/state", "value": "Adding"}]

plexxi_lsg = {
    "name": "Plexxi-LSG",
    "type": "logical-switch-groupV4",
    "switchMapTemplate": {
            "switchMapEntryTemplates": [
                {
                    "logicalLocation": {
                        "locationEntries": [
                            {"relativeValue": 1, "type": "StackingMemberId"}
                        ]
                    },
                    "permittedSwitchTypeUri": "Composable Fabric FM 3180"
                },
                {
                    "logicalLocation": {
                        "locationEntries": [
                            {"relativeValue": 2, "type": "StackingMemberId"}
                        ]
                    },
                    "permittedSwitchTypeUri": "Composable Fabric FM 3180"
                }
            ]
    }
}

logical_switches = [
    {
        'name': 'Plexxi-LS1',
                'switchUris': [plexxi_switches[0]['name'], plexxi_switches[1]['name']]
    }
]

profile_connections_lag = {
    'name': 'profile_connections_lag',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ7340093.us.rdlabs.hpecorp.net',
    'connectionSettings': {
            'connections': [
                {
                    'name': 'conn1',
                    'functionType': 'Ethernet',
                    'portId': 'flr 1:1',
                    'lagName': 'LAG1'
                },
                {
                    'name': 'conn2',
                    'functionType': 'Ethernet',
                    'portId': 'flr 1:2',
                    'lagName': 'LAG1'
                }
            ]
    }
}

profile_connections__no_lag = {
    'name': 'profile_connections_no_lag',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ7340093.us.rdlabs.hpecorp.net',
    'connectionSettings': {
            'connections': [
                {
                    'name': 'conn1',
                    'functionType': 'Ethernet',
                    'portId': 'flr 1:1',
                },
                {
                    'name': 'conn2',
                    'functionType': 'Ethernet',
                    'portId': 'flr 1:2',
                }
            ]
    }
}

SPT_unassigned_connections = {
    'name': 'SPT_unassigned_connections',
    'type': 'ServerProfileTemplateV7',
    'serverHardwareTypeUri': 'DL360 Gen10 1',
    'connectionSettings': {
            'manageConnections': True,
        'complianceControl': 'Checked',
        'connections': [
            {
                'name': 'conn1',
                        'functionType': 'Ethernet',
                'portId': 'flr 1:1',
            },
            {
                'name': 'conn2',
                        'functionType': 'Ethernet',
                'portId': 'flr 1:2',
            }
        ]
    }
}

ProfileTemp_unassigned_connections = {
    'name': 'ProfileTemp_unassigned_connections',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ7340093.us.rdlabs.hpecorp.net',
    'serverProfileTemplateUri': 'SPT_unassigned_connections'
}

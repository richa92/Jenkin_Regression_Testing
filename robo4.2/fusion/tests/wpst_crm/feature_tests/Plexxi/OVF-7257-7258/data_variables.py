'''
Plexxi Data File For OVF7257 And OVF7258
'''
appliance_ip = '15.186.24.198'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

plexxi_connect_host = '15.186.25.6'
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
    {'name': 'ILOMXQ82505G5.us.rdlabs.hpecorp.net', 'IP': '15.186.24.216'},
    {'name': 'ILOMXQ82503CP.us.rdlabs.hpecorp.net', 'IP': '15.186.24.222'},
]
DL_Body = {
    "username": "Administrator",
    "password": "hpvse123",
    "force": True,
    "licensingIntent": "OneView",
    # "licensingIntent":"OneViewNoiLO",
    "configurationState": "Managed",
}

sudo_password = 'plexxi'
switch_login_prompt = '$'
sudo_command = 'sudo px-shell'
sudo_login_prompt = 'admin:'
sudo_password_prompt = '[sudo] password for admin:'
plexxi_switch_prompt = '>'

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
                    "logicalLocation":
                        {
                            "locationEntries": [
                                {
                                    "relativeValue": 1, "type": "StackingMemberId"
                                }
                            ]
                        },
                    "permittedSwitchTypeUri": "Composable Fabric FM 3180"
                },
                {
                    "logicalLocation":
                        {
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
    },
    {
        'name': 'Plexxi-LS2',
        'switchUris': [plexxi_switches[2]['name'], plexxi_switches[3]['name']]
    },
    {
        'name': 'Plexxi-LS3',
        'switchUris': [plexxi_switches[4]['name'], plexxi_switches[5]['name']]
    }
]

conn1 = {
    'name': 'conn1',
    'functionType': 'Ethernet',
    'portId': 'flr 1:1',
}

conn2 = {
    'name': 'conn2',
    'functionType': 'Ethernet',
    'portId': 'flr 1:2',
}

add_connection = {
    'name': 'conn2',
    'functionType': 'Ethernet',
    'portId': 'flr 1:2',
    'networkUri': 'RNS_2'
}

Profile_unassigned_connections = {
    'name': 'Profile_unassigned_connections',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ82505G2.us.rdlabs.hpecorp.net',
    'connectionSettings': {
            'connections': [conn1, conn2]
    }
}

Profile_assigned_connections = {
    'name': 'Profile_assigned_connections',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ7340093.us.rdlabs.hpecorp.net',
    'connectionSettings': {
            'connections': [
                {
                    'name': 'conn1',
                    'functionType': 'Ethernet',
                    'portId': 'flr 1:1',
                    'networkUri': 'RNS_1'
                }
            ]
    }
}

unassigned_mlag_connections = [
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

mlag_connections = [
    {
        'name': 'conn1',
        'functionType': 'Ethernet',
                'portId': 'flr 1:1',
                'networkUri': 'RNS_3',
                'lagName': 'LAG1'
    },
    {
        'name': 'conn2',
        'functionType': 'Ethernet',
                'portId': 'flr 1:2',
                'networkUri': 'RNS_3',
                'lagName': 'LAG1'
    }
]

Profile_mlags_unassigned = {
    'name': 'Profile_mlags_unassigned',
    'type': 'ServerProfileV11',
    'serverHardwareTypeUri': 'DL360 Gen10 1',
    'connectionSettings': {
            'connections': unassigned_mlag_connections
    }
}

Profile_mlags_assigned = {
    'name': 'Profile_mlags_assigned',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ82505G2.us.rdlabs.hpecorp.net',
    'connectionSettings': {
            'connections': mlag_connections
    }
}

SPT_unassigned_connections = {
    'name': 'SPT_unassigned_connections',
    'type': 'ServerProfileTemplateV7',
    'serverHardwareTypeUri': 'DL360 Gen10 1',
    'connectionSettings': {
            'manageConnections': True,
        'complianceControl': 'Checked',
        'connections': [conn1, conn2]
    }
}

SPT_assigned_connections = {
    'name': 'SPT_assigned_connections',
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
                'networkUri': 'net_401'
            }
        ]
    }
}

SPT_mlags = {
    'name': 'SPT_mlags',
    'type': 'ServerProfileTemplateV7',
    'serverHardwareTypeUri': 'DL360 Gen10 1',
    'connectionSettings': {
            'manageConnections': True,
        'complianceControl': 'Checked',
        'connections': mlag_connections
    }
}

ProfileTemp_unassigned_connections = {
    'name': 'ProfileTemp_unassigned_connections',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ7340093.us.rdlabs.hpecorp.net',
    'serverProfileTemplateUri': 'SPT_unassigned_connections'
}

ProfileTemp_assigned_connections = {
    'name': 'ProfileTemp_assigned_connections',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ82505G2.us.rdlabs.hpecorp.net',
    'serverProfileTemplateUri': 'SPT_assigned_connections'
}

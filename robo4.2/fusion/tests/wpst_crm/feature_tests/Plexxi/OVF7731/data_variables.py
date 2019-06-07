'''
Plexxi Data File For OVF7731
'''
appliance_ip = '15.186.25.224'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

plexxi_connect_host = '15.186.25.226'
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

Profile = {
    'name': 'Plexxi Profile',
    'type': 'ServerProfileV11',
    'serverHardwareUri': 'ILOMXQ7340093.us.rdlabs.hpecorp.net',
    'connectionSettings': {
            'connections': [
                {
                    'name': 'conn',
                    'functionType': 'Ethernet',
                    'portId': 'flr 1:1',
                    'networkUri': 'RNS_1'
                }
            ]
    }
}

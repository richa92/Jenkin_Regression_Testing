# def getFusionDirPath():
#    import os
#    import FusionLibrary

#    return os.path.dirname(os.path.dirname(FusionLibrary.__file__))

# FUSION_DIRPATH = getFusionDirPath()
admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
oneview = {
    'ip': '16.114.211.88',
    'cred': {
        'userName': 'Administrator',
        'password': 'wpsthpvse1',
    },
    'cliCredentials': {
        'userName': 'root',
        'password': 'hpvse1',
    }
}

serversAndCredentials = {
    'le:LE/encl:1/bay:9': {
        'platform': 'windows',
        'iLOUserLoginCredentials': {
            'userName': 'Administrator',
            'password': 'hpvse123'
        },
        'osUserLoginCredentials': {
            'userName': 'root',
            'password': 'Wpsthpvse1'
        },
    },
}

pingTemplate1 = {
    'size': 100,
    'fragment': False,
}

pingTemplate2 = {
    'size': 100,
    'fragment': False,
    'numberOfEchoRequest': 1000000,
    'timeToLive': 50,  # In milli seconds
}

# Traffic from server bay to testhead
trafficTestData1 = {
    'fusion': oneview,
    'serversAndCredentials': serversAndCredentials,
    'entities': [
        {
            'trafficgen': 'ping',
            'stream': pingTemplate1,
            'vlan': ['tagged', 283],
            'source': 'le:LE/encl:1/bay:9/port:3:1-a',
            'destination': [
                '16.114.218.168',
                '16.114.218.140'
            ],
        },
    ]
}

# Traffic from test head to server bay
trafficTestData2 = {
    'fusion': oneview,
    'serversAndCredentials': serversAndCredentials,
    'platform': 'windows',
    'entities': [
        {
            'trafficgen': 'ping',
            'stream': pingTemplate1,
            'vlan': ['tagged', 283],
            'source': '16.114.220.185',
            'destination': [
                '16.114.213.37',
            ],
        },
    ]
}

# Enclosures
ENC1 = 'CN744502CG'
# LIG, AND LE
LIG_NAME = 'LIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE'

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1

ethernet_networks = [
    {'name': 'net100',
     'type': 'ethernet-networkV300',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net283',
     'type': 'ethernet-networkV300',
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

uplink_sets = {'us_tagged': {'name': 'us-tagged',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['net100', 'net283'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        ]
                             },
               }

edit_profile_add_connection = {
    'type': 'ServerProfileV7',
    'name': 'CN744502CG, bay 9',
    'description': '',
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 9',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG1',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureBay': 9,
    'affinity': 'Bay',
    'associatedServer': 'SH:' + ENC1 + ', bay 9',
    'hideUnusedFlexNics': True,
    'firmware': {
        'manageFirmware': False,
        'firmwareBaselineUri': '',
        'forceInstallFirmware': False,
        'firmwareInstallType': None,
    },
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'serialNumberType': 'Virtual',
    'category': 'server-profiles',
    'status': 'OK',
    'state': 'Normal',
    'connections': [{
        'id': 1,
        'name': '',
        'functionType': 'Ethernet',
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': "ETH:net283",
        'requestedVFs': 'Auto',
        'ipv4': {}
    }, {
        'id': 2,
        'name': '',
        'functionType': 'Ethernet',
        'portId': 'Auto',
        'requestedMbps': '2500',
        'networkUri': "ETH:net100",
        'requestedVFs': 'Auto',
        'ipv4': {}
    }],
    'bootMode': {
        'manageMode': False
    },
    'boot': None,
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': None,
    'osDeploymentSettings': None,
    'refreshState': 'NotRefreshing',
}

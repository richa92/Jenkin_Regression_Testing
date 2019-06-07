from dto import *
from env_variables import *

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY3 = '%s, bay 3' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3

enclosures = [
    {"type": ENCLOSURE_TYPE_400, "name": ENC1, },
    {"type": ENCLOSURE_TYPE_400, "name": ENC2, },
    {"type": ENCLOSURE_TYPE_400, "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, },
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1, },
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4, },
]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC2ICBAY6, },
]

ethernet_networks = [
    {
        'name': 'network-tunnel',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 0,
        'subnetUri': None,
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

network_sets = [{'name': 'NS1', 'type': NETWORK_SET_TYPE, 'networkUris': ['net100'], 'nativeNetworkUri': 'net100'}, ]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': CHLORIDE20, 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': CHLORIDE20, 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': CHLORIDE20, 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': CHLORIDE20, 'enclosureIndex': 3},
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
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
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
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
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
            {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
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
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': NATASHA},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': NATASHA}]
    }
]

egs = [
    {
        'name': 'EG1',
        'type': ENCLOSURE_GROUP_TYPE_300,
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [
                {"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
                {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
                {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
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

firebird_server_profile_templates = [
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE,
        'serverProfileDescription': ENC1 + ', bay 3 - Firebird-LS',
        'serverHardwareTypeUri': 'SHT:SY 680 Gen9:1:Smart Array P542D '
                                 'Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 3 - Firebird-LS',
        'description': ENC1 + ', bay 3 - Firebird-LS',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': [
                {
                    'id': 1,
                    'name': '1',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'boot': {'priority': 'NotBootable'},
                    'requestedVFs': 'Auto'
                },
                {
                    'id': 2,
                    'name': '2',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-b',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net300',
                    'boot': {'priority': 'NotBootable'},
                    'requestedVFs': 'Auto'
                }
            ], 'manageConnections': True
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'localStorage': {
            'sasLogicalJBODs': [
                {
                    'id': 1,
                    'name': ENC1 + ', bay 3 - LS1',
                    'deviceSlot': 'Mezz 1',
                    'numPhysicalDrives': 3,
                    'driveMinSizeGB': 50,
                    'driveMaxSizeGB': 500,
                    'driveTechnology': 'SasHdd'
                }
            ],
            'controllers': [
                {
                    'logicalDrives': [
                        {
                            'name': ENC1 + ', bay 3-rd1',
                            'raidLevel': 'RAID1',
                            'bootable': False,
                            'numPhysicalDrives': 2,
                            'driveTechnology': 'SasHdd',
                            'sasLogicalJBODId': None
                        }
                    ],
                    'deviceSlot': 'Embedded',
                    'mode': 'RAID',
                    'initialize': True
                },
                {
                    'logicalDrives': [
                        {
                            'name': None,
                            'raidLevel': 'RAID0',
                            'bootable': False,
                            'numPhysicalDrives': None,
                            'driveTechnology': None,
                            'sasLogicalJBODId': 1
                        }
                    ],
                    'deviceSlot': 'Mezz 1',
                    'mode': 'RAID',
                    'initialize': False
                }
            ]
        },
        'sanStorage': None
    },

    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE,
        'serverProfileDescription': ENC3 + ', bay 5',
        'serverHardwareTypeUri': 'SHT:SY 680 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC3 + ', bay 5',
        'description': ENC3 + ', bay 5',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': [
                {
                    'id': 1,
                    'name': '1',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'boot': {'priority': 'NotBootable'},
                    'requestedVFs': 'Auto'
                },
                {
                    'id': 2,
                    'name': '2',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-b',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net300',
                    'boot': {'priority': 'NotBootable'},
                    'requestedVFs': 'Auto'
                }
            ], 'manageConnections': True
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': [
                {
                    'logicalDrives': [
                        {
                            'name': 'test',
                            'raidLevel': 'RAID0',
                            'bootable': False,
                            'numPhysicalDrives': 1,
                            'driveTechnology': 'SasHdd',
                            'sasLogicalJBODId': None
                        }
                    ],
                    'deviceSlot': 'Embedded',
                    'mode': 'RAID',
                    'initialize': True,
                }
            ]
        },
        'sanStorage': None
    },
]

firebird_server_profiles = [
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC3 + ', bay 5',
        'serverHardwareTypeUri': 'SHT:SY 680 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC3 + ', bay 5',
        'description': '',
        'affinity': 'Bay',
        'connectionSettings': {
            'connections': [
                {
                    'id': 1,
                    'name': '1',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'requestedVFs': 'Auto'
                },
                {
                    'id': 2,
                    'name': '2',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-b',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net300',
                    'requestedVFs': 'Auto'
                }
            ]
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'firmware': {
            'manageFirmware': False, 'firmwareBaselineUri': '',
            'forceInstallFirmware': False, 'firmwareInstallType': None
        },
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorName': 'AutoGenerated',
        'osDeploymentSettings': None,
        'localStorage': {
            'sasLogicalJBODs': [],
            'controllers': [{
                'logicalDrives': [{
                    'name': 'test',
                    'raidLevel': 'RAID0',
                    'bootable': False,
                    'numPhysicalDrives': 1,
                    'driveTechnology': 'SasHdd',
                    'sasLogicalJBODId': None
                }],
                'deviceSlot': 'Embedded',
                'mode': 'RAID',
                'initialize': True,
            }]
        },
        'sanStorage': None
    },

    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
        'serverHardwareTypeUri': 'SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy'
                                 ' 3820C 10/20Gb CNA',
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
                    'name': '',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'requestedVFs': 'Auto'
                },
                {
                    'id': 2,
                    'name': '',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-b',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net300',
                    'requestedVFs': 'Auto'
                }
            ]
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'firmware': {
            'manageFirmware': False, 'firmwareBaselineUri': '',
            'forceInstallFirmware': False, 'firmwareInstallType': None
        },
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorName': 'AutoGenerated',
        'osDeploymentSettings': None,
        'localStorage': {
            'sasLogicalJBODs': [
                {
                    'id': 1,
                    'name': ENC1 + ', bay 3 - LS1',
                    'deviceSlot': 'Mezz 1',
                    'numPhysicalDrives': 3,
                    'driveMinSizeGB': 50,
                    'driveMaxSizeGB': 500,
                    'driveTechnology': 'SasHdd'
                }
            ],
            'controllers': [
                {
                    'logicalDrives': [
                        {
                            'name': ENC1 + ', bay 3-rd1',
                            'raidLevel': 'RAID1',
                            'bootable': False,
                            'numPhysicalDrives': 2,
                            'driveTechnology': 'SasHdd',
                            'sasLogicalJBODId': None
                        }],
                    'deviceSlot': 'Embedded',
                    'mode': 'RAID',
                    'initialize': True
                },
                {
                    'logicalDrives': [
                        {
                            'name': None,
                            'raidLevel': 'RAID0',
                            'bootable': False,
                            'numPhysicalDrives': None,
                            'driveTechnology': None,
                            'sasLogicalJBODId': 1
                        }
                    ],
                    'deviceSlot': 'Mezz 1',
                    'mode': 'RAID',
                    'initialize': False
                }
            ]
        },
        'sanStorage': None
    }
]

edit_profile_add_jbod = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
    'serverHardwareTypeUri': 'SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 3',
    'description': '',
    'affinity': 'Bay',
    'connectionSettings': {
        'connections': [
            {
                ''
                'id': 1,
                'name': '1',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:net100',
                'requestedVFs': 'Auto'
            }
        ]
    },
    'boot': None,
    'bootMode': {'manageMode': False},
    'firmware': {
        'manageFirmware': False,
        'firmwareBaselineUri': '',
        'forceInstallFirmware': False,
        'firmwareInstallType': None
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'hideUnusedFlexNics': True,
    'iscsiInitiatorNameType': 'AutoGenerated',
    'localStorage': {
        'sasLogicalJBODs': [
            {
                'id': 1,
                'deviceSlot': 'Mezz 1',
                'name': ENC1 + ', bay 3 - LS1',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasHdd',
                'sasLogicalJBODUri': 'SASLJBOD:' + ENC1 + ', bay 3 - LS1',
            },
            {
                'id': 2,
                'deviceSlot': 'Mezz 1',
                'name': 'LS2',
                'numPhysicalDrives': 2,
                'driveMinSizeGB': 20,
                'driveMaxSizeGB': 200,
                'driveTechnology': 'SasHdd',
            }
        ],
        'controllers': [
            {
                'logicalDrives': [
                    {
                        'name': ENC1 + ', bay 3-rd1',
                        'raidLevel': 'RAID1',
                        'bootable': False,
                        'numPhysicalDrives': 2,
                        'driveTechnology': 'SasHdd',
                        'sasLogicalJBODId': None,
                    }
                ],
                'deviceSlot': 'Embedded',
                'mode': 'RAID',
                'initialize': True,
                'importConfiguration': False
            },
            {
                'logicalDrives': [
                    {
                        'name': None,
                        'raidLevel': 'RAID0',
                        'bootable': False,
                        'numPhysicalDrives': None,
                        'driveTechnology': None,
                        'sasLogicalJBODId': 1,
                    },
                    {
                        'name': None,
                        'raidLevel': 'RAID1',
                        'bootable': False,
                        'numPhysicalDrives': None,
                        'driveTechnology': None,
                        'sasLogicalJBODId': 2,
                    }
                ],
                'deviceSlot': 'Mezz 1',
                'mode': 'RAID',
                'initialize': False,
                'importConfiguration': False
            }
        ]
    },
    'sanStorage': None
}

sas_logical_jbods = [
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 3 - LS1',
        'clearMetaData': False,
        'minSizeGB': 50,
        'maxSizeGB': 500,
        'numPhysicalDrives': 3,
        'driveTechnology': {'deviceInterface': 'SAS', 'driveMedia': 'HDD'},
        'sasLogicalInterconnectUri': 'SASLI:LE1-SASLIG1-1',
        'stateReason': None,
        'refreshState': 'NotRefreshing',
        'state': 'Configured',
        'description': None,
        'status': 'OK',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 3 - LS1',
    },
]

sas_logical_jbod_attachments = [
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 3',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
        'sasLogicalJBODUri': 'SASLJBOD:' + ENC1 + ', bay 3 - LS1',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-1',
        'state': 'Deployed',
        'description': None,
        'status': 'OK',
        'category': 'sas-logical-jbod-attachments',
    },
]

sas_logical_jbods_after_edit = [
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 3 - LS1',
        'clearMetaData': False,
        'minSizeGB': 50,
        'maxSizeGB': 500,
        'numPhysicalDrives': 3,
        'driveTechnology': {'deviceInterface': 'SAS', 'driveMedia': 'HDD'},
        'sasLogicalInterconnectUri': 'SASLI:LE1-SASLIG1-1',
        'stateReason': None,
        'refreshState': 'NotRefreshing',
        'state': 'Configured',
        'description': None,
        'status': 'OK',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 3 - LS1',
    },
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': 'LS2',
        'clearMetaData': False,
        'minSizeGB': 20,
        'maxSizeGB': 200,
        'numPhysicalDrives': 2,
        'driveTechnology': {'deviceInterface': 'SAS', 'driveMedia': 'HDD'},
        'sasLogicalInterconnectUri': 'SASLI:LE1-SASLIG1-1',
        'stateReason': None,
        'refreshState': 'NotRefreshing',
        'state': 'Configured',
        'description': None,
        'status': 'OK',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:LS2',
    }
]

sas_logical_jbod_attachments_after_edit = [
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 3',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
        'sasLogicalJBODUri': 'SLJBOD:' + ENC1 + ', bay 3 - LS1',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-1',
        'state': 'Deployed',
        'description': None,
        'status': 'OK',
        'category': 'sas-logical-jbod-attachments',
    },
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 3',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
        'sasLogicalJBODUri': 'SLJBOD:LS2',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-2',
        'state': 'Deployed',
        'description': None,
        'status': 'OK',
        'category': 'sas-logical-jbod-attachments',
    },
]

server_profile = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC3 + ', bay 5',
    'serverHardwareTypeUri': 'SHT:SY 680 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'iscsiInitiatorNameType': 'AutoGenerated',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'Firebird Move profile from Enc3 bay5 to Enc1 bay3',
    'description': '',
    'affinity': 'Bay',
    'connectionSettings': {
        'connections': [
            {
                'id': 1,
                'name': '1',
                'functionType': 'Ethernet',
                'portId': 'Mezz 3:1-a',
                'requestedMbps': '2500',
                'networkUri': 'ETH:net100',
                'requestedVFs': 'Auto'
            },
            {
                'id': 2,
                'name': '2',
                'functionType': 'Ethernet',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': '2500',
                'networkUri': 'ETH:net300',
                'requestedVFs': 'Auto'
            }
        ]
    },
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'firmware': {
        'manageFirmware': False, 'firmwareBaselineUri': '',
        'forceInstallFirmware': False, 'firmwareInstallType': None
    },
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True,
    'iscsiInitiatorName': 'AutoGenerated',
    'osDeploymentSettings': None,
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': [
            {
                'logicalDrives': [
                    {
                        'name': 'test',
                        'raidLevel': 'RAID0',
                        'bootable': False,
                        'numPhysicalDrives': 1,
                        'driveTechnology': 'SasHdd',
                        'sasLogicalJBODId': None
                    }
                ],
                'deviceSlot': 'Embedded',
                'mode': 'RAID',
                'initialize': True,
            }
        ]
    },
    'sanStorage': None
}

move_server_profile_to_enc2 = {
    'type': SERVER_PROFILE_TYPE,
    'name': 'Firebird Move profile from Enc3 bay5 to Enc1 bay3',
    'description': 'moved to Enc1 bay3',
    'iscsiInitiatorName': None,
    'iscsiInitiatorNameType': 'AutoGenerated',
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
    'serverHardwareTypeUri': 'SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG1',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureBay': 3,
    'affinity': 'Bay',
    'associatedServer': None,
    'hideUnusedFlexNics': True,
    'firmware': {
        'manageFirmware': False,
        'firmwareBaselineUri': '',
        'forceInstallFirmware': False,
        'firmwareInstallType': None
    },
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'serialNumberType': 'Virtual',
    'category': 'server-profiles',
    'created': '20160523T172227.667Z',
    'modified': '20160523T174455.703Z',
    'status': 'OK',
    'state': 'Normal',
    'inProgress': False,
    'connectionSettings': {
        'connections': [
            {
                'id': 1,
                'name': '1',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:net100',
                'boot': {
                    'priority': 'NotBootable',
                },
            },
            {
                'id': 2,
                'name': '2',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:net300',
                'boot': {
                    'priority': 'NotBootable',
                },
            }
        ]
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': [
            {
                'logicalDrives': [
                    {
                        'name': 'test',
                        'raidLevel': 'RAID0',
                        'bootable': False,
                        'numPhysicalDrives': 1,
                        'driveTechnology': 'SasHdd',
                        'sasLogicalJBODId': None,
                        'driveNumber': 1
                    }
                ],
                'deviceSlot': 'Embedded',
                'mode': 'RAID',
                'initialize': True,
                'importConfiguration': False
            }
        ]
    },
    'sanStorage': None,
}

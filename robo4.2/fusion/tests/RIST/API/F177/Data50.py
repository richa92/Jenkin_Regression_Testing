from robot.libraries.BuiltIn import BuiltIn
from dto import *
from env_variables import *

try:
    TEST_RING = BuiltIn().get_variable_value("${X_TEST_RING}")
except:  # noqa
    TEST_RING = 'DCS'

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
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

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

network_sets = [
    {
        'name': 'NS1',
        'type': NETWORK_SET_TYPE,
        'networkUris': ['net100'],
        'nativeNetworkUri': 'net100'
    },
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
            {
                'enclosure': '1', 'bay': '3',
                'port': 'Q1.1', 'speed': 'Auto'
            },
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
        'uplinkSets': [uplink_sets['us_untagged'].copy(),
                       uplink_sets['us_tagged'].copy(), uplink_sets['us_tunnel'].copy(), ],
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
        'interconnectBayMappings':
            [
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

profile_templates = [
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE,
        'serverProfileDescription': ENC1 + ', bay 5-withBothRaid',
        'serverHardwareTypeUri':
            'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 5-SPT-withBothRaid',
        'description': ENC1 + ', bay 5-SPT-withBothRaid',
        'affinity': 'Bay',
        'connectionSettings': {
            'manageConnections': True,
            'connections': [
                {
                    'id': 1,
                    'name': '',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'boot': {'priority': 'NotBootable'},
                    'requestedVFs': 'Auto'
                }
            ]
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'localStorage': {
            'sasLogicalJBODs': [
                {
                    'id': 1,
                    'name': ENC1 + ', bay 5-rd0',
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
                            'name': ENC1 + ', bay 5-rd1',
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
        'serverProfileDescription': ENC1 + ', bay 7-withbothHBA',
        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 7-SPT-withbothHBA',
        'description': ENC1 + ', bay 7-SPT-withbothHBA',
        'affinity': 'Bay',
        'connectionSettings': {
            'manageConnections': True,
            'connections': [
                {
                    'id': 1,
                    'name': '',
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
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'localStorage': {
            'sasLogicalJBODs': [
                {
                    'id': 1,
                    'deviceSlot': 'Mezz 1',
                    'name': ENC1 + ', bay 7-jbod1',
                    'numPhysicalDrives': 3,
                    'driveMinSizeGB': 50,
                    'driveMaxSizeGB': 500,
                    'driveTechnology': 'SasHdd'
                }
            ],
            'controllers': [
                {
                    'logicalDrives': None,
                    'deviceSlot': 'Embedded',
                    'mode': 'HBA',
                    'initialize': True
                },
                {
                    'logicalDrives': None,
                    'deviceSlot': 'Mezz 1',
                    'mode': 'HBA',
                    'initialize': False
                }
            ]
        },
        'sanStorage': None
    }
]

verify_profile_templates = [
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE,
        'serverProfileDescription': ENC1 + ', bay 5-withBothRaid',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 5-SPT-withBothRaid',
        'description': ENC1 + ', bay 5-SPT-withBothRaid',
        'affinity': 'Bay',
        'connectionSettings': {
            'manageConnections': True,
            'connections': [
                {
                    'id': 1,
                    'name': '',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'boot': {'priority': 'NotBootable'},
                    'requestedVFs': 'Auto'
                }
            ]
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'localStorage': {
            'sasLogicalJBODs': [
                {
                    'id': 1,
                    'name': ENC1 + ', bay 5-rd0',
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
                },
                {
                    'logicalDrives': [
                        {
                            'name': ENC1 + ', bay 5-rd1',
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
                }
            ]
        },
        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []}
    },
    {
        'type': SERVER_PROFILE_TEMPLATE_TYPE,
        'serverProfileDescription': ENC1 + ', bay 7-withbothHBA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 7-SPT-withbothHBA',
        'description': ENC1 + ', bay 7-SPT-withbothHBA',
        'affinity': 'Bay',
        'connectionSettings': {
            'manageConnections': True,
            'connections': [
                {
                    'id': 1,
                    'name': '',
                    'functionType': 'Ethernet',
                    'portId': 'Mezz 3:1-a',
                    'requestedMbps': '2500',
                    'networkUri': 'ETH:net100',
                    'requestedVFs': 'Auto'
                }
            ]
        },
        'boot': {'manageBoot': False, 'order': []},
        'bootMode': {'manageMode': False},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'localStorage': {
            'sasLogicalJBODs': [
                {
                    'id': 1,
                    'deviceSlot': 'Mezz 1',
                    'name': ENC1 + ', bay 7-jbod1',
                    'numPhysicalDrives': 3,
                    'driveMinSizeGB': 50,
                    'driveMaxSizeGB': 500,
                    'driveTechnology': 'SasHdd'
                }
            ],
            'controllers': [
                {
                    'logicalDrives': None,
                    'deviceSlot': 'Embedded',
                    'mode': 'HBA',
                    'initialize': True
                },
                {
                    'logicalDrives': None,
                    'deviceSlot': 'Mezz 1',
                    'mode': 'HBA',
                    'initialize': False
                }
            ]
        },
        'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []}
    }
]

server_profiles = [
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
        'enclosureUri': 'ENC:' + ENC1,
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 7',
        'serverProfileTemplateUri': 'SPT:' + ENC1 + ', bay 7-SPT-withbothHBA',
        'description': ENC1 + ', bay 7-withbothHBA',
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
                }
            ]
        },
        'boot': {'manageBoot': False, 'order': []},
        'bootMode': {'manageMode': False},
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': None,
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
                    'name': ENC1 + ', bay 7-jbod1',
                    'numPhysicalDrives': 3,
                    'driveMinSizeGB': 50,
                    'driveMaxSizeGB': 500,
                    'driveTechnology': 'SasHdd'
                }
            ],
            'controllers': [
                {
                    'logicalDrives': None,
                    'deviceSlot': 'Mezz 1',
                    'mode': 'HBA',
                    'initialize': False
                },
                {
                    'logicalDrives': None,
                    'deviceSlot': 'Embedded',
                    'mode': 'HBA',
                    'initialize': False
                }
            ]
        },
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}
    },
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
        'enclosureUri': 'ENC:' + ENC1,
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 5',
        'serverProfileTemplateUri': 'SPT:' + ENC1 + ', bay 5-SPT-withBothRaid',
        'description': ENC1 + ', bay 5-SPT-withBothRaid',
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
                }
            ]
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto'
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': None,
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
                    'name': ENC1 + ', bay 5-rd0',
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
                            'name': ENC1 + ', bay 5-rd1',
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
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}
    }

]

verify_server_profiles = [
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
        'enclosureUri': 'ENC:' + ENC1,
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 7',
        'serverProfileTemplateUri': 'SPT:' + ENC1 + ', bay 7-SPT-withbothHBA',
        'description': ENC1 + ', bay 7-withbothHBA',
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
                }
            ]
        },
        'boot': {'manageBoot': False, 'order': []},
        'bootMode': {'manageMode': False},
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': None,
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
                    'name': 'REGEX:{}, bay 7-jbod1'.format(ENC1),
                    'numPhysicalDrives': 3,
                    'driveMinSizeGB': 50,
                    'driveMaxSizeGB': 500,
                    'driveTechnology': 'SasHdd'
                }
            ],
            'controllers': [
                {
                    'logicalDrives': [],
                    'deviceSlot': 'Mezz 1',
                    'mode': 'HBA',
                    'initialize': False
                },
                {
                    'logicalDrives': [],
                    'deviceSlot': 'Embedded',
                    'mode': 'HBA',
                    'initialize': False
                }
            ]
        },
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}
    },
    {
        'type': SERVER_PROFILE_TYPE,
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
        'enclosureUri': 'ENC:' + ENC1,
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 5',
        'serverProfileTemplateUri': 'SPT:' + ENC1 + ', bay 5-SPT-withBothRaid',
        'description': ENC1 + ', bay 5-withBothRaid',
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
                }
            ]
        },
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {
            'manageMode': True,
            'mode': 'UEFI',
            'pxeBootPolicy': 'Auto'
        },
        'firmware': {
            'manageFirmware': False,
            'firmwareBaselineUri': None,
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
                    'name': 'REGEX:{}, bay 5-rd0'.format(ENC1),
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
                            'name': ENC1 + ', bay 5-rd1',
                            'raidLevel': 'RAID1',
                            'bootable': False,
                            'numPhysicalDrives': 2,
                            'driveTechnology': 'SasHdd',
                            'sasLogicalJBODId': None
                        }
                    ],
                    'deviceSlot': 'Embedded',
                    'mode': 'RAID',
                    'initialize': False
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
        'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}
    }

]

unassigned_server_profile = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'unassigned',
    'description': 'unassigned',
    'affinity': 'Bay',
    'connectionSettings': {
        'connections': [
            {
                'id': 1,
                'name': '',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:net100',
                'requestedVFs': 'Auto'
            }
        ]
    },
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True,
    'iscsiInitiatorNameType': 'AutoGenerated',
    'localStorage': {
        'sasLogicalJBODs': [
            {
                'id': 1,
                'deviceSlot': 'Mezz 1',
                'name': 'unassigned1',
                'numPhysicalDrives': 1,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasHdd'
            },
            {
                'id': 2,
                'deviceSlot': 'Mezz 1',
                'name': 'unassigned2',
                'numPhysicalDrives': 1,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasHdd'
            }
        ]
    },
    'sanStorage': None
}

edit_profile_add_jbod = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
    'serverHardwareTypeUri':
        'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 7',
    'serverProfileTemplateUri':
        'SPT:' + ENC1 + ', bay 7-SPT-withbothHBA',
    'description': '',
    'affinity': 'Bay',
    'connectionSettings': {
        'connections': [
            {
                'id': 1,
                'name': '',
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
                'name': ENC1 + ', bay 7-jbod1',
                'sasLogicalJBODUri':
                    'SASLJBOD:' + ENC1 + ', bay 7-jbod1',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasHdd'
            },
            {
                'id': 2,
                'deviceSlot': 'Mezz 1',
                'name': ENC1 + ', bay 7-jbod2',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 30,
                'driveMaxSizeGB': 300,
                'driveTechnology': 'SasHdd'
            }
        ],
        'controllers': [
            {
                'logicalDrives': None,
                'deviceSlot': 'Embedded',
                'mode': 'HBA',
                'initialize': True
            },
            {
                'logicalDrives': None,
                'deviceSlot': 'Mezz 1',
                'mode': 'HBA',
                'initialize': False
            }
        ]
    },
    'sanStorage': None
}
unassign_existing_profile = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareTypeUri':
        'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG1',
    'serverHardwareUri': None,
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 7',
    'serverProfileTemplateUri':
        'SPT:' + ENC1 + ', bay 7-SPT-withbothHBA',
    'description': 'unassign existing Server profile',
    'affinity': 'Bay',
    'associatedServer': None,
    'enclosureBay': None,
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
            }
        ]
    },
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'firmware': {
        'manageFirmware': False,
        'firmwareBaselineUri': None,
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
                'name': ENC1 + ', bay 7-jbod1',
                'sasLogicalJBODUri':
                    'SASLJBOD:' + ENC1 + ', bay 7-jbod1',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasHdd'
            },
            {
                'id': 2,
                'deviceSlot': 'Mezz 1',
                'name': ENC1 + ', bay 7-jbod2',
                'sasLogicalJBODUri':
                    'SASLJBOD:' + ENC1 + ', bay 7-jbod2',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 30,
                'driveMaxSizeGB': 300,
                'driveTechnology': 'SasHdd'
            }
        ],
        'controllers': [
            {
                'logicalDrives': None,
                'deviceSlot': 'Embedded',
                'mode': 'HBA',
                'initialize': True
            },
            {
                'logicalDrives': None,
                'deviceSlot': 'Mezz 1',
                'mode': 'HBA',
                'initialize': False
            }
        ]
    },
    'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}
}

# Server profile with drives = 256 test case 10
server_profile_invalid_drives = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
    'serverHardwareTypeUri':
        'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 7 invalid_drives',
    'description': '',
    'affinity': 'Bay',
    'connectionSettings': {'connections': []},
    'localStorage': {
        'sasLogicalJBODs': [
            {
                'id': 1,
                'deviceSlot': 'Mezz 1',
                'name': ENC1 + ', bay 7',
                'numPhysicalDrives': 257,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasHdd'
            },
        ]
    },

}
# Logical JBOD min size > max size test case 11
server_profile_min_max_mismatch = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
    'serverHardwareTypeUri':
        'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 5 min_max_mismatch',
    'description': '',
    'affinity': 'Bay',
    'connectionSettings': {
        'connections': []
    },
    'localStorage': {
        'sasLogicalJBODs': [
            {
                'id': 1,
                'deviceSlot': 'Mezz 1',
                'name': ENC1 + ', bay 5',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 500,
                'driveMaxSizeGB': 40,
                'driveTechnology': 'SasHdd'
            },
        ]
    },

}
# Logical JBOD wrong Drive Techonology test case 12
server_profile_wrong_drive_type = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
    'serverHardwareTypeUri':
        'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 7 wrong_drive_type',
    'description': '',
    'affinity': 'Bay',
    'connectionSettings': {
        'connections': []
    },
    'localStorage': {
        'sasLogicalJBODs': [
            {
                'id': 1,
                'deviceSlot': 'Mezz 1',
                'name': ENC1 + ', bay 7',
                'numPhysicalDrives': 3,
                'driveMinSizeGB': 50,
                'driveMaxSizeGB': 500,
                'driveTechnology': 'SasSsd'
            },
        ]
    },

}
# Create server profile - set more than one Boot local drive test case 13
server_profile_more_boot_drives = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
    'serverHardwareTypeUri':
        'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 7 more_boot_drives',
    'description': '',
    'affinity': 'Bay',
    'bootMode': {'manageMode': True, 'mode': 'BIOS'},
    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'PXE', 'HardDisk']},
    'connectionSettings': {
        'connections': []
    },
    'localStorage': {
        'sasLogicalJBODs': [
            {
                'id': 1,
                'name': ENC1 + ', bay 7-rd0',
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
                        'name': ENC1 + ', bay 7-rd1',
                        'raidLevel': 'RAID1',
                        'bootable': True,
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
                        'bootable': True,
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

}

# Create server profile - LD with both reinitialize and import config -
# test case 15
server_profile_ld_with_both = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
    'serverHardwareTypeUri':
        'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 7 ld_with_both',
    'description': '',
    'affinity': 'Bay',
    'bootMode': {'manageMode': True, 'mode': 'BIOS'},
    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'PXE', 'HardDisk']},
    'connectionSettings': {
        'connections': []
    },
    'localStorage': {
        'controllers': [
            {
                'logicalDrives': [
                    {
                        'name': ENC1 + ', bay 7-rd1',
                        'raidLevel': 'RAID1',
                        'bootable': True,
                        'numPhysicalDrives': 2,
                        'driveTechnology': 'SasHdd',
                        'sasLogicalJBODId': None
                    }
                ],
                'deviceSlot': 'Embedded',
                'mode': 'RAID',
                'initialize': True,
                'importConfiguration': True
            },
        ]
    },

}
# Create server profile with wrong RAID type -test case 16
server_profile_wrong_raid = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
    'serverHardwareTypeUri':
        'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 5 wrong_raid',
    'description': '',
    'affinity': 'Bay',
    'bootMode': {'manageMode': True, 'mode': 'BIOS'},
    'boot': {'manageBoot': True, 'order': ['CD', 'USB', 'PXE', 'HardDisk']},
    'connectionSettings': {
        'connections': []
    },
    'localStorage': {
        'controllers': [
            {
                'logicalDrives': [
                    {
                        'name': ENC1 + ', bay 5-rd1',
                        'raidLevel': 'RAID22',
                        'bootable': True,
                        'numPhysicalDrives': 2,
                        'driveTechnology': 'SasHdd',
                        'sasLogicalJBODId': None
                    }
                ],
                'deviceSlot': 'Embedded',
                'mode': 'RAID',
                'initialize': True
            },
        ]
    },
}

negative_server_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': server_profile_invalid_drives.copy(),
        'taskState': 'Error',
        'timeout': '120',
        'errorMessage': 'DFRM_INSUFFICIENT_DRIVE_COUNT'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': server_profile_min_max_mismatch.copy(),
        'taskState': 'Error',
        'timeout': '120',
        'errorMessage': 'DirectFabricJbodInvalidNumMinSizeGb'
    },
    #    {'keyword': 'Add Server Profile',
    #     'argument': server_profile_wrong_drive_type.copy(),
    #     'taskState': 'Error',
    #     'timeout': '120',
    #     'errorMessage': 'DFRM_INSUFFICIENT_DRIVE_COUNT'},
    #    {'keyword': 'Add Server Profile',
    #     'argument': server_profile_ld_with_both.copy(),
    #     'taskState': 'Error',
    #     'timeout': '120',
    #    'errorMessage': 'DFRM_INSUFFICIENT_DRIVE_COUNT'},
    {
        'keyword': 'Add Server Profile',
        'argument': server_profile_wrong_raid.copy(),
        'taskState': 'Error',
        'timeout': '6000',
        'errorMessage': 'UNSUPPORTED_RAID_LEVEL_660'
    },
    {
        'keyword': 'Add Server Profile',
        'argument': server_profile_more_boot_drives.copy(),
        'taskState': 'Error',
        'timeout': '6000',
        'errorMessage': 'MORE_THAN_ONE_BOOTABLE_LOGICAL_DRIVE'
    },
]

sas_logical_jbods = [
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 5-rd0',
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
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 5-rd0',
    },
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 7-jbod1',
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
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 7-jbod1',
    }
]

sas_logical_jbod_attachments = [
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 7',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
        'sasLogicalJBODUri': 'REGEX:/rest/sas-logical-jbods/*',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-1',
        'state': 'Deployed',
        'description': None,
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbod-attachments',
    },
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 5',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
        'sasLogicalJBODUri': 'REGEX:/rest/sas-logical-jbods/*',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-2',
        'state': 'Deployed',
        'description': None,
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbod-attachments',
    }
]

sas_logical_jbods_after_edit = [
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 5-rd0',
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
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 5-rd0',
    },
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 7-jbod1',
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
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 7-jbod1',
    },
    {
        'type': SAS_LOGICAL_JBOD_TYPE,
        'name': ENC1 + ', bay 7-jbod2',
        'clearMetaData': False,
        'minSizeGB': 30,
        'maxSizeGB': 300,
        'numPhysicalDrives': 3,
        'driveTechnology': {'deviceInterface': 'SAS', 'driveMedia': 'HDD'},
        'sasLogicalInterconnectUri': 'SASLI:LE1-SASLIG1-1',
        'stateReason': None,
        'refreshState': 'NotRefreshing',
        'state': 'Configured',
        'description': None,
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbods',
        'uri': 'SASLJBOD:' + ENC1 + ', bay 7-jbod2',
    }
]

sas_logical_jbod_attachments_after_edit = [
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 7',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
        'sasLogicalJBODUri': 'REGEX:/rest/sas-logical-jbods/*',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-1',
        'state': 'Deployed',
        'description': None,
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbod-attachments',
    },
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 5',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
        'sasLogicalJBODUri': 'REGEX:/rest/sas-logical-jbods/*',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-2',
        'state': 'Deployed',
        'description': None,
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbod-attachments',
    },
    {
        'type': SAS_LOGICAL_JBOD_ATTACHMENT_TYPE,
        'serverProfileUri': 'SP:' + ENC1 + ', bay 7',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
        'sasLogicalJBODUri': 'REGEX:/rest/sas-logical-jbods/*',
        'mezzSlotNumber': 1,
        'name': 'LE1-SASLIG1-1-SLJA-3',
        'state': 'Deployed',
        'description': None,
        'status': 'REGEX:(OK|WARNING)',
        'category': 'sas-logical-jbod-attachments',
    },
]

move1_newName = ENC1 + ', bay 3'
move2_newName = ENC2 + ', bay 3'

move_server_profile_within_same_tbird = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1 + ', bay 3',
    'serverHardwareTypeUri':
        'SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC1,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 5',
    'description': 'moved from Enc XL Bay 5 to Enc XL bay 3',
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
            }
        ]
    },
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'firmware': {
        'manageFirmware': False,
        'firmwareBaselineUri': None,
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
                'name': ENC1 + ', bay 5-rd0',
                'sasLogicalJBODUri':
                    'SASLJBOD:' + ENC1 + ', bay 5-rd0',
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
                        'name':
                            ENC1 + ', bay 5-rd1',
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
    'sanStorage': {'volumeAttachments': [], 'manageSanStorage': False}
}

move_server_profile_between_two_tbirds_within_same_ring = {
    'type': SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC2 + ', bay 5',
    'serverHardwareTypeUri':
        'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureUri': 'ENC:' + ENC2,
    'enclosureGroupUri': 'EG:EG1',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': ENC1 + ', bay 3',
    'description': 'moved from XL Bay 3 to R6 bay 3',
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
            }
        ]
    },
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'firmware': {
        'manageFirmware': False,
        'firmwareBaselineUri': None,
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
                'name': ENC2 + ', bay 5-rd0',
                'sasLogicalJBODUri':
                    'SASLJBOD:' + ENC2 + ', bay 5-rd0',
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
                        'name': ENC2 + ', bay 5-rd1',
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
    'sanStorage': {
        'volumeAttachments': [],
        'manageSanStorage': False
    }
}

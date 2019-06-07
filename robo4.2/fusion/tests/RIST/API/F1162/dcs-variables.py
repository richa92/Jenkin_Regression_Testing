admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}


LIG_NAME = 'LIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE_1'

# Enclosures
ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'
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
ENC2SASICBAY1 = '%s, interconnect 1' % ENC2
ENC2SASICBAY4 = '%s, interconnect 4' % ENC2
ENC3SASICBAY1 = '%s, interconnect 1' % ENC3
ENC3SASICBAY4 = '%s, interconnect 4' % ENC3
# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1
ENC1DEBAY7 = '%s, bay 7' % ENC1
ENC2DEBAY1 = '%s, bay 1' % ENC2
ENC2DEBAY7 = '%s, bay 7' % ENC2
ENC3DEBAY1 = '%s, bay 1' % ENC3
ENC3DEBAY7 = '%s, bay 7' % ENC3
# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1
ENC1SHBAY10 = '%s, bay 10' % ENC1
ENC1SHBAY11 = '%s, bay 11' % ENC1
ENC1SHBAY12 = '%s, bay 12' % ENC1
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY4 = '%s, bay 4' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY9 = '%s, bay 9' % ENC2
ENC2SHBAY10 = '%s, bay 10' % ENC2
ENC2SHBAY11 = '%s, bay 11' % ENC2
ENC2SHBAY12 = '%s, bay 12' % ENC2
ENC3SHBAY3 = '%s, bay 3' % ENC3
ENC3SHBAY4 = '%s, bay 4' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3
ENC3SHBAY6 = '%s, bay 6' % ENC3
ENC3SHBAY9 = '%s, bay 9' % ENC3
ENC3SHBAY10 = '%s, bay 10' % ENC3
ENC3SHBAY11 = '%s, bay 11' % ENC3
ENC3SHBAY12 = '%s, bay 12' % ENC3
# Ethernet Networks
net100 = 'ETH:%s' % 'net100'

ethernet_networks = [{'name': 'network-iSCSI',
                      'type': 'ethernet-networkV300',
                      'vlanId': 1,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Untagged'},
                     {'name': 'net100',
                      'type': 'ethernet-networkV300',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net300',
                      'type': 'ethernet-networkV300',
                      'vlanId': 300,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     ]

egs = [ {'name': 'EG1',
               'type': 'EnclosureGroupV300',
               'enclosureCount': 3,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 2,
               'configurationScript': None,
               'interconnectBayMappings':
               [
                {"interconnectBay":3,"logicalInterconnectGroupUri":"LIG:LIG1"},
                {"interconnectBay":6,"logicalInterconnectGroupUri":"LIG:LIG1"}
                ],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
            ]

enclosures = [
    { "type": "EnclosureV300", "name": ENC1, },
    { "type": "EnclosureV300", "name": ENC2, },
    { "type": "EnclosureV300", "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, }
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1}
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4}
]

ics = [
    {"name": ENC1ICBAY3},
    {"name": ENC2ICBAY6}
]

les = [{'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}
       ]

icmap = [
         {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        ]

uplink_sets = {'us_untagged': {'name': 'us_untagged',
                           'ethernetNetworkType': 'Untagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['network-iSCSI'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                      ]
                            },
               'us_tagged': {'name': 'us_tagged',
                           'ethernetNetworkType': 'Tagged',
                           'networkType': 'Ethernet',
                           'networkUris': ['net100','net300'],
                           'nativeNetworkUri': None,
                           'mode': 'Auto',
                           'lacpTimer': 'Long',
                           'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                      ]
                            },
               }

ligs = [ {'name': 'LIG1',
         'type': 'logical-interconnect-groupV300',
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
         'uplinkSets': [uplink_sets['us_untagged'].copy(),uplink_sets['us_tagged'].copy(),],
        }
    ]

sasligs = [{'name': 'SASLIG1',  # Single SAS switch
            "type": "sas-logical-interconnect-group",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'}]}
           ]

network_sets = [{'name': 'NS1', 'type': 'network-setV300', 'networkUris': ['net100'], 'nativeNetworkUri': 'net100'},]
# Verify Create Server Profile Template
# iSCSI primary only
spt_1 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt1_primary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    #'serverHardwareUri': 'SH: '+ENC1SHBAY3,
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'firstBootTargetIp': '192.168.21.72',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '192.168.22.73',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

spt_1_edit = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt1_primary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'firstBootTargetIp': '192.168.21.72',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '192.168.22.73',
                'secondBootTargetPort': '3260',
                'chapLevel': 'None'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary and secondary
spt_2 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt2_primary_secondary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'firstBootTargetIp': '192.168.21.72',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '192.168.22.73',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
    },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'Chap'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary only UEFI optimized
spt_3 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt3_primary_uefioptimized',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'Chap'
            }
    },
    ],
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary and secondary UEFI optimized
spt_4 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt4_primary_secondary_uefioptimized',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'Chap'
            }
    },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'Chap'
            }
    },
    ],
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary and secondary UEFI optimized
spt_5 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt5_primary_secondary_no_chap',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'None'
            }
    },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'None'
            }
    },
    ],
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary and secondary UEFI optimized
spt_5 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt5_primary_secondary_no_chap',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'None'
            }
    },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'chapLevel': 'None'
            }
    },
    ],
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

sp_from_spt = [{
    'type': 'ServerProfileV6',
    'name': 'sp_from_spt1',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'serverHardwareUri': ENC1SHBAY3,
    'serverProfileTemplateUri': 'SPT:spt1_primary',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorName': 'iqn.2015-02.com.hpe:oneview-0c005d02-dca6-43a7-96f2-f3491a4acee',
                'initiatorIp': '192.168.22.88',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'firstBootTargetIp': '192.168.21.72',
                'bootTargetName': 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:84:tbird8-bay6-vol1',
                'bootTargetLun': '0',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '192.168.22.73',
                'secondBootTargetPort': '3260',
                'chapLevel': 'None'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}]


# Verify Network Sets are NOT Supported during Create Server Profile
# Template with iSCSI SW Boot
negative_spt1 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'negative_spt_1',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'NS:NS1',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Network Sets are NOT Supported during Create Server Profile
# Template with iSCSI SW Boot
negative_spt2 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'negative_spt_2',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'NS:NS1',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Cannot Create Server Profile Template with only iSCSI Secondary
# Boot Mode
negative_spt3 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'negative_spt_3',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Cannot Create Server Profile Template with multiple primary or
# secondary
negative_spt4 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'negative_spt_4',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [
        {
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
        },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
        },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Cannot Create Server Profile Template with multiple primary or
# secondary
negative_spt5 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'negative_spt_5',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [
        {
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
        },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
        },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Required Fields
negative_spt6 = {
    'type': 'ServerProfileTemplateV2',
    'name': 'negative_spt_6',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [
        {
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
        },
        {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Secondary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'initiatorVlanId': 1,
                'firstBootTargetIp': '',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
        },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_ethernet'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_ethernet'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Boot_initiator_subnet_required'},
    {
        'keyword': 'Fusion Api Delete Server Profile Template',
        'argument': 'spt1_primary',
        'taskState': 'Error',
        'errorMessage': 'Referenced_by_server_profile'},
]

create_profile_templates = [
    spt_1.copy(),
    spt_2.copy(),
    spt_3.copy(),
    spt_4.copy(),
    spt_5.copy(),
]

delete_profile_templates = [
    'spt1_primary',
    'spt2_primary_secondary',
    'spt3_primary_uefioptimized',
    'spt4_primary_secondary_uefioptimized',
    'spt5_primary_secondary_no_chap',
]

delete_profile = {
    'type': 'ServerProfileTemplateV2',
    'name': 'spt1_primary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'serverHardwareUri': ENC1SHBAY3,
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connections': [{
        'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'boot': {
                'priority': 'Primary',
                'initiatorNameSource': 'UserDefined',
                'initiatorSubnetMask': '255.255.192.0',
                'initiatorGateway': '192.168.1.1',
                'firstBootTargetIp': '192.168.21.72',
                'firstBootTargetPort': '3260',
                'secondBootTargetIp': '192.168.22.73',
                'secondBootTargetPort': '3260',
                'chapLevel': 'Chap'
            }
    },
    ],
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
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}
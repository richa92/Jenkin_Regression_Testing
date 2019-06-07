admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
server_credentials = {'userName': 'Serveradmin_f1222', 'password': 'wpsthpvse1'}
network_credentials = {'userName': 'Networkadmin_f1222', 'password': 'wpsthpvse1'}
storage_credentials = {'userName': 'storage', 'password': 'wpsthpvse1'}


users = [
    {'userName': 'Serveradmin_f1222', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin_f1222', 'permissions': [{'roleName': 'Server administrator'}],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin_f1222', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin_f1222', 'permissions': [{'roleName': 'Network administrator'}],
     'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Backupadmin_f1222', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin_f1222', 'permissions': [{'roleName': 'Backup administrator'}],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'storage_f1222', 'password': 'wpsthpvse1', 'fullName': 'storage_f1222', 'permissions': [{'roleName': 'Storage administrator'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Noprivledge_f1222', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge_f1222', 'permissions': [{'roleName': 'Read only'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]

# Enclosures
ENC1 = 'CN75120D7B'
ENC2 = 'CN75120D77'
ENC3 = 'CN750163KD'

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

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1

ENC2SHBAY1 = '%s, bay 1' % ENC2

ENC3SHBAY1 = '%s, bay 1' % ENC3

enclosures = [
    {"type": "EnclosureV300", "name": ENC1},
    {"type": "EnclosureV300", "name": ENC2},
    {"type": "EnclosureV300", "name": ENC3}
]

sasics = [
    {"name": ENC1SASICBAY1},
    {"name": ENC1SASICBAY4}
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1}
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4}
]

ics = [
    {"name": ENC1ICBAY3},
    {"name": ENC1ICBAY6},
    {"name": ENC2ICBAY3},
    {"name": ENC2ICBAY6},
    {"name": ENC3ICBAY3},
    {"name": ENC3ICBAY6}
]

ethernet_networks = [{'name': 'net100',
                      'type': 'ethernet-networkV4',
                      'vlanId': 100,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'},
                     {'name': 'net300',
                      'type': 'ethernet-networkV4',
                      'vlanId': 300,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}
                     ]

icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
         ]

uplink_sets = {'us_ethernet': {'name': 'us_ethernet',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['net100', 'net300'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                          ]
                               }
               }

ligs = [{'name': 'LIG2',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'ethernetSettings': None,
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'stackingMode': 'Enclosure',
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [uplink_sets['us_ethernet'].copy()],
         },
        {'name': 'LIG3',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'ethernetSettings': None,
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'stackingMode': 'Enclosure',
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [uplink_sets['us_ethernet'].copy()],
         }
        ]

sasligs = [{'name': 'SASLIG2',  # Single SAS switch
            "type": "sas-logical-interconnect-groupV2",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
            ]
            },
           {'name': 'SASLIG3',  # Single SAS switch
            "type": "sas-logical-interconnect-groupV2",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
            ]
            }
           ]

egs = [{'name': 'EG2',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG2"},
             {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG2"},
             {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG2"}
             ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        },
       {'name': 'EG3',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
            [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG3"},
             {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG3"},
             {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG3"}
             ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]

les = [{'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

profile_templates = [
    {'type': 'ServerProfileTemplateV6',
     'serverProfileDescription': 'change_sht-Virtual-network',
     'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:HP Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
     'enclosureGroupUri': 'EG:EG2',
     'serialNumberType': 'Virtual',
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'name': 'change_sht-Virtual-network',
     'description': 'change_sht-Virtual-network',
     'affinity': 'Bay',
     'connectionSettings': {'connections': [{'id': 1,
                                             'name': '',
                                             'functionType': 'Ethernet',
                                             'portId': 'Mezz 3:1-a',
                                             'requestedMbps': '2500',
                                             'networkUri': 'ETH:net100',
                                             'boot': {'priority': 'NotBootable'},
                                             'requestedVFs': 'Auto'}], 'manageConnections': True},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True,
             "localStorage": {
         "sasLogicalJBODs": [],
         "controllers": []
     },
     "sanStorage": {
         "manageSanStorage": False,
         "volumeAttachments": []
     }},
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-Physical-network',
        'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG2',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-Physical-network',
        'description': 'change_sht-Physical-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    },
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-and-eg-network',
        'serverHardwareTypeUri': 'SHT:SY 680 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG2',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-and-eg-network',
        'description': 'change_sht-and-eg-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }
        ], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    }
]

edit_eg_templates = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-and-eg-network',
        'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG3',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-and-eg-network',
        'description': 'change_sht-and-eg-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }
        ], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    }
]

edit_sht_templates = [
    {'type': 'ServerProfileTemplateV6',
     'serverProfileDescription': 'change_sht-Virtual-network',
     'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
     'enclosureGroupUri': 'EG:EG2',
     'serialNumberType': 'Virtual',
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'name': 'change_sht-Virtual-network',
     'description': 'change_sht-Virtual-network',
     'affinity': 'Bay',
     'connectionSettings': {'connections': [{'id': 1,
                                             'name': '',
                                             'functionType': 'Ethernet',
                                             'portId': 'Mezz 3:1-a',
                                             'requestedMbps': '2500',
                                             'networkUri': 'ETH:net100',
                                             'boot': {'priority': 'NotBootable'},
                                             'requestedVFs': 'Auto'}], 'manageConnections': True},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'bios': {'manageBios': False, 'overriddenSettings': []},
     'hideUnusedFlexNics': True,
     "localStorage": {
         "sasLogicalJBODs": [],
         "controllers": []
     },
     "sanStorage": {
         "manageSanStorage": False,
         "volumeAttachments": []
     }},
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-Physical-network',
        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG2',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-Physical-network',
        'description': 'change_sht-Physical-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }
        ], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    },
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-and-eg-network',
        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG3',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-and-eg-network',
        'description': 'change_sht-and-eg-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }
        ], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    }
]

transformation_eg_templates = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-and-eg-network',
        'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:HP Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG2',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-and-eg-network',
        'description': 'change_sht-and-eg-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }
        ], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    }
]


verify_transformation_eg_templates = [
    {
        'type': 'ServerProfileTemplateV6',
        'serverProfileDescription': 'change_sht-and-eg-network',
        'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:HP Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG2',
        'serialNumberType': 'Physical',
        'macType': 'Physical',
        'wwnType': 'Physical',
        'name': 'change_sht-and-eg-network',
        'description': 'change_sht-and-eg-network',
        'affinity': 'Bay',
        'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
        }
        ], 'manageConnections': True},
        'boot': {'manageBoot': True, 'order': ['HardDisk']},
        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        "localStorage": {
            "sasLogicalJBODs": [],
            "controllers": []
        },
        "sanStorage": {
            "manageSanStorage": False,
            "volumeAttachments": []
        }
    }
]

transformation_edit_eg_templates = [{
    'type': 'ServerProfileTemplateV6',
    'serverProfileDescription': 'change_sht-and-eg-network',
    'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG2',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change_sht-and-eg-network',
    'description': 'change_sht-and-eg-network',
    'affinity': 'Bay',
    'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
    }
    ], 'manageConnections': True},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }
}]

invalid_eg_edit_template = {
    'type': 'ServerProfileTemplateV6',
    'serverProfileDescription': 'change_sht-and-eg-network',
    'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:badEG',
    'name': 'change_sht-and-eg-network',
    'description': 'change_sht-and-eg-network',
    'affinity': 'Bay',
    'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
    }
    ], 'manageConnections': True},
    'boot': None,
    'bootMode': {'manageMode': False},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}


invalid_sht_edit_template = {
    'type': 'ServerProfileTemplateV6',
    'serverProfileDescription': 'change_sht-and-eg-network',
    'serverHardwareTypeUri': 'SHT:badSHT',
    'enclosureGroupUri': 'EG:EG2',
    'name': 'change_sht-and-eg-network',
    'description': 'change_sht-and-eg-network',
    'affinity': 'Bay',
    'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
    }
    ], 'manageConnections': True},
    'boot': None,
    'bootMode': {'manageMode': False},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

invalid_addresses_change_edit_template = {
    'type': 'ServerProfileTemplateV6',
    'serverProfileDescription': 'change_sht-and-eg-network',
    'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG2',
    'serialNumberType': 'Virtual',
    'macType': 'Virtual',
    'wwnType': 'Virtual',
    'name': 'change_sht-and-eg-network',
    'description': 'change_sht-and-eg-network',
    'affinity': 'Bay',
    'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
    }
    ], 'manageConnections': True},
    'boot': None,
    'bootMode': {'manageMode': False},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}


auth_test_edit_eg_templates = {
    'type': 'ServerProfileTemplateV6',
    'serverProfileDescription': 'change_sht-and-eg-network',
    'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:EG2',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'name': 'change_sht-and-eg-network',
    'description': 'change_sht-and-eg-network',
    'affinity': 'Bay',
    'connectionSettings': {'connections': [{
            'id': 1,
            'name': '',
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': '2500',
            'networkUri': 'ETH:net100',
            'requestedVFs': 'Auto'
    }
    ], 'manageConnections': True},
    'boot': None,
    'bootMode': {'manageMode': False},
    'bios': {'manageBios': False, 'overriddenSettings': []},
    'hideUnusedFlexNics': True,
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    }}

sp_from_spt = {
    "name": "F1222_from_template",
    "serverProfileTemplateUri": "SPT:change_sht-and-eg-network"
}

negative_unauth_edit_template = [
    {'keyword': 'Edit Server Profile Template',
     'argument': auth_test_edit_eg_templates.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'NOT_AUTHORIZED_ERROR'}]

negative_tests_eg_sht_addresses = [
    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_eg_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'INVALID_ENCLOSURE_GROUP'},
    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_sht_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'UNKNOWN_SERVER_TYPE'},
    {'keyword': 'Edit Server Profile Template',
     'argument': invalid_addresses_change_edit_template.copy(),
     'taskState': 'Error',
     'timeout': '120',
     'errorMessage': 'FINAL_ATTRIBUTE_CHANGED'}
]

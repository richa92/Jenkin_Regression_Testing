admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

FUSION_IP = '16.114.209.223'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'wpsthpvse1'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

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
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 5' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

# needed to re-apply confi
SAS_LI_NAME = "LE1-SASLIG1-1"

enclosures = [
    {"type": "EnclosureV400", "name": ENC1},
    {"type": "EnclosureV400", "name": ENC2},
    {"type": "EnclosureV400", "name": ENC3}
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
icmap = [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
         {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
         {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
         {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
         {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
         {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
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
uplink_sets = {'us_ethernet': {'name': 'us_ethernet',
                               'ethernetNetworkType': 'Tagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['net100', 'net300'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q1:1', 'speed': 'Auto'},
                                                          ]
                               }
               }
ligs = [{'name': 'LIG1',
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

sasligs = [{'name': 'SASLIG1',  # Single SAS switch
            "type": "sas-logical-interconnect-group",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
            ]
            }
           ]

egs = [{'name': 'EG1',
        'type': 'EnclosureGroupV7',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'interconnectBayMappingCount': 2,
        'configurationScript': None,
        'interconnectBayMappings':
            [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
             {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
             {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
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

server_profiles = [
    {'type': 'ServerProfileV10',
     'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
     'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
     'enclosureUri': 'ENC:' + ENC1,
     'enclosureGroupUri': 'EG:EG1',
     'serialNumberType': 'Virtual',
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'name': ENC1 + ', bay 5',
     'description': '',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': []
     },
     'boot': None,
     'bootMode': {'manageMode': False},
     'firmware': {'manageFirmware': False,
                  'firmwareBaselineUri': '',
                  'forceInstallFirmware': False,
                  'firmwareInstallType': None
                  },
     'bios': {'manageBios': False,
              'overriddenSettings': []
              },
     'hideUnusedFlexNics': True,
     'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [{'id': 1,
                                           'name': ENC1 + ', bay 5-rd0',
                                           'deviceSlot': 'Mezz 1',
                                           'numPhysicalDrives': 3,
                                           'driveMinSizeGB': 50,
                                           'driveMaxSizeGB': 500,
                                           'driveTechnology': 'SasHdd'}],
                      'controllers': [{'logicalDrives': [{'name': ENC1 + ', bay 5-rd1',
                                                          'raidLevel': 'RAID1',
                                                          'bootable': False,
                                                          'numPhysicalDrives': 2,
                                                          'driveTechnology': 'SasHdd',
                                                          'sasLogicalJBODId': None}],
                                       'deviceSlot': 'Embedded',
                                       'mode': 'RAID',
                                       'initialize': True},
                                      {'logicalDrives': [{'name': None,
                                                          'raidLevel': 'RAID0',
                                                          'bootable': False,
                                                          'numPhysicalDrives': None,
                                                          'driveTechnology': None,
                                                          'sasLogicalJBODId': 1}],
                                       'deviceSlot': 'Mezz 1',
                                       'mode': 'RAID',
                                       'initialize': False}]},
     'sanStorage': None
     },
    {'type': 'ServerProfileV10',
     'serverHardwareUri': 'SH:' + ENC1 + ', bay 7',
     'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
     'enclosureUri': 'ENC:' + ENC1,
     'enclosureGroupUri': 'EG:EG1',
     'serialNumberType': 'Virtual',
     'macType': 'Virtual',
     'wwnType': 'Virtual',
     'name': ENC1 + ', bay 7',
     'description': '',
     'affinity': 'Bay',
     'connectionSettings': {
         'connections': []
     },
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'bootMode': {'manageMode': True,
                  'mode': 'UEFI',
                  'pxeBootPolicy': 'Auto'},
     'firmware': {'manageFirmware': False,
                  'firmwareBaselineUri': '',
                  'forceInstallFirmware': False,
                  'firmwareInstallType': None},
     'bios': {'manageBios': False,
              'overriddenSettings': []},
     'hideUnusedFlexNics': True,
     'iscsiInitiatorNameType': 'AutoGenerated',
     'localStorage': {'sasLogicalJBODs': [{'id': 1,
                                           'deviceSlot': 'Mezz 1',
                                           'name': ENC1 + ', bay 7-jbod1',
                                           'numPhysicalDrives': 3,
                                           'driveMinSizeGB': 50,
                                           'driveMaxSizeGB': 500,
                                           'driveTechnology': 'SasHdd'}],
                      'controllers': [{'logicalDrives': [],
                                       'deviceSlot': 'Embedded',
                                       'mode': 'HBA',
                                       'initialize': True},
                                      {'logicalDrives': [],
                                       'deviceSlot': 'Mezz 1',
                                       'mode': 'HBA',
                                       'initialize': False}]
                      },
     'sanStorage': None}

]

edit_profile_add_jbod = {'type': 'ServerProfileV10',
                         'serverHardwareUri': 'SH:' + ENC1 + ', bay 5',
                         'serverHardwareTypeUri': 'SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
                         'enclosureUri': 'ENC:' + ENC1,
                         'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual',
                         'macType': 'Virtual',
                         'wwnType': 'Virtual',
                         'name': ENC1 + ', bay 5',
                         'description': '',
                         'affinity': 'Bay',
                         'connectionSettings': {
                             'connections': []
                         },
                         'boot': None,
                         'bootMode': {'manageMode': False},
                         'firmware': {'manageFirmware': False,
                                      'firmwareBaselineUri': '',
                                      'forceInstallFirmware': False,
                                      'firmwareInstallType': None
                                      },
                         'bios': {'manageBios': False,
                                  'overriddenSettings': []
                                  },
                         'hideUnusedFlexNics': True,
                         'iscsiInitiatorNameType': 'AutoGenerated',
                         'localStorage': {'sasLogicalJBODs': [{'id': 1,
                                                               'deviceSlot': 'Mezz 1',
                                                               'name': ENC1 + ', bay 5-rd0',
                                                               'sasLogicalJBODUri': 'SASLJBOD:' + ENC1 + ', bay 5-rd0',
                                                               'numPhysicalDrives': 3,
                                                               'driveMinSizeGB': 50,
                                                               'driveMaxSizeGB': 500,
                                                               'driveTechnology': 'SasHdd'},
                                                              {'id': 2,
                                                               'deviceSlot': 'Mezz 1',
                                                               'name': ENC1 + ', bay 5-jbod2',
                                                               'numPhysicalDrives': 3,
                                                               'driveMinSizeGB': 30,
                                                               'driveMaxSizeGB': 300,
                                                               'driveTechnology': 'SasHdd'}],
                                          'controllers': [{'logicalDrives': [{'name': ENC1 + ', bay 5-rd1',
                                                                              'raidLevel': 'RAID1',
                                                                              'bootable': False,
                                                                              'numPhysicalDrives': 2,
                                                                              'driveTechnology': 'SasHdd',
                                                                              'sasLogicalJBODId': None}],
                                                           'deviceSlot': 'Embedded',
                                                           'mode': 'RAID',
                                                           'initialize': True},
                                                          {'logicalDrives': [{'name': None,
                                                                              'raidLevel': 'RAID0',
                                                                              'bootable': False,
                                                                              'numPhysicalDrives': None,
                                                                              'driveTechnology': None,
                                                                              'sasLogicalJBODId': 1},
                                                                             {'name': None,
                                                                              'raidLevel': 'RAID0',
                                                                              'bootable': False,
                                                                              'numPhysicalDrives': None,
                                                                              'driveTechnology': None,
                                                                              'sasLogicalJBODId': 2}],
                                                           'deviceSlot': 'Mezz 1',
                                                           'mode': 'RAID',
                                                           'initialize': False}],

                                          },
                         'sanStorage': None
                         }

# RIS nodes
create_ris_node_bay7_drive1 = {
    "server": ENC1SHBAY7,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/16",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPD5'
            }
        },
        'Id': '16',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:34',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FBQDC',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
create_ris_node_bay7_drive2 = {
    "server": ENC1SHBAY7,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/17",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPDD'
            }
        },
        'Id': '17',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:35',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FARWD',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
create_ris_node_bay7_drive3 = {
    "server": ENC1SHBAY7,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/18",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPDD'
            }
        },
        'Id': '18',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:36',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FARWD',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
edit_ris_node_bay5_drive1 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/16",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPD5'
            }
        },
        'Id': '16',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:31',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FBQDC',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
edit_ris_node_bay5_drive2 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/17",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPD5'
            }
        },
        'Id': '17',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:32',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FBQDC',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
edit_ris_node_bay5_drive3 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/18",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPD5'
            }
        },
        'Id': '18',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:33',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FBQDC',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}

edit_ris_node_bay5_logical_drive1 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/LogicalDrives/1",
    "validate": {
        "Description": "HP Smart Storage Logical Drive View",
        'CapacityMiB': 419946,
        'Id': '1',
        'LogicalDriveEncryption': False,
        'LogicalDriveNumber': 1,
        'LogicalDriveType': 'Data',
        'Name': 'HpSmartStorageLogicalDrive',
        'Raid': '0',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled'
        },
        'StripeSizeBytes': 262144,
        'Type': 'HpSmartStorageLogicalDrive.1.1.0',
    },
}

edit_ris_node_bay5_logical_drive2 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/LogicalDrives/2",
    "validate": {
        "Description": "HP Smart Storage Logical Drive View",
        'CapacityMiB': 419946,
        'Id': '2',
        'LogicalDriveEncryption': False,
        'LogicalDriveNumber': 2,
        'LogicalDriveType': 'Data',
        'Name': 'HpSmartStorageLogicalDrive',
        'Raid': '0',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled'
        },
        'StripeSizeBytes': 262144,
        'Type': 'HpSmartStorageLogicalDrive.1.1.0',
    },
}

edit_ris_node_bay5_drive4 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/19",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPDD'
            }
        },
        'Id': '19',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:37',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FARWD',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
edit_ris_node_bay5_drive5 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/20",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPDD'
            }
        },
        'Id': '20',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:38',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FARWD',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}
edit_ris_node_bay5_drive6 = {
    "server": ENC1SHBAY5,
    "username": "Administrator",
    "password": "hpvse123",
    "path": "/rest/v1/Systems/1/SmartStorage/ArrayControllers/1/DiskDrives/21",
    "validate": {
        "Description": "HP Smart Storage Disk Drives View",
        'BlockSizeBytes': 512,
        'CapacityGB': 146,
        'CapacityLogicalBlocks': 286749488,
        'CapacityMiB': 140014,
        'CarrierApplicationVersion': '11',
        'CarrierAuthenticationStatus': 'OK',
        'Description': 'HP Smart Storage Disk Drive View',
        'EncryptedDrive': False,
        'FirmwareVersion': {
            'Current': {
                'VersionString': 'HPDD'
            }
        },
        'Id': '21',
        'InterfaceSpeedMbps': 6000,
        'InterfaceType': 'SAS',
        'Location': '01:1:39',
        'LocationFormat': 'ControllerPort:Box:Bay',
        'MediaType': 'HDD',
        'Model': 'EH0146FARWD',
        'Name': 'HpSmartStorageDiskDrive',
        'PowerOnHours': None,
        'RotationalSpeedRpm': 15000,
        'SSDEnduranceUtilizationPercentage': None,
        'SerialNumber': 'REGEX:\w*',
        'Status': {
            'Health': 'OK',
            'State': 'Enabled',
        },
        'Type': 'HpSmartStorageDiskDrive.1.2.0',
    }
}


ris_nodes_create_ilo = [create_ris_node_bay7_drive1, create_ris_node_bay7_drive2, create_ris_node_bay7_drive3]
ris_nodes_after_edit_ilo = [create_ris_node_bay7_drive1, create_ris_node_bay7_drive2, create_ris_node_bay7_drive3, edit_ris_node_bay5_drive1, edit_ris_node_bay5_drive2, edit_ris_node_bay5_drive3, edit_ris_node_bay5_logical_drive1, edit_ris_node_bay5_logical_drive2, edit_ris_node_bay5_drive4, edit_ris_node_bay5_drive5, edit_ris_node_bay5_drive6]

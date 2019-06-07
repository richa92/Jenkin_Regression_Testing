def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist



le_spp_upgrade = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/upgrade",
                  "firmwareUpdateOn": "SharedInfrastructureOnly",
                  "logicalInterconnectUpdateMode": "Parallel",
                  "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                  "updateFirmwareOnUnmanagedInterconnect": True}


le_spp_downgrade = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/downgrade",
                    "firmwareUpdateOn": "SharedInfrastructureOnly",
                    "logicalInterconnectUpdateMode": "Parallel",
                    "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                    "updateFirmwareOnUnmanagedInterconnect": True}

le_spp_upgrade_profiles = {"forceInstallFirmware": False, "firmwareBaselineUri": "/rest/firmware-drivers/upgrade",
                           "firmwareUpdateOn": "SharedInfrastructureAndServerProfiles",
                           "logicalInterconnectUpdateMode": "Parallel",
                           "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                           "updateFirmwareOnUnmanagedInterconnect": True}

le_upgrade_linkmodule = {"forceInstallFirmware": True, "firmwareBaselineUri": "/rest/firmware-drivers/downgrade",
                           "firmwareUpdateOn": "EnclosureOnly",
                           "logicalInterconnectUpdateMode": "Parallel",
                           "validateIfLIFirmwareUpdateIsNonDisruptive": False,
                           "updateFirmwareOnUnmanagedInterconnect": True}

EG = 'EG'
enc_groups = [{'name': EG,
               'type': 'EnclosureGroupV400',
               'enclosureCount': 1,
               'enclosureTypeUri': '/rest/enclosure-types/SY12000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 6,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None}],
               'ipAddressingMode': "External",
               'ipRangeUris': [],
               'powerMode': "RedundantPowerFeed"
               }
              ]

ENC1 = 'EM1FFFF500'
LE = 'LE'

les = [{'name': LE,
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:EG',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       ]

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': ENC1 + ', bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'SP', 'description': '', 'affinity': 'Bay',
                    'connections': []}
                   ]

downlink_d11_enable = {'interconnectName': 'CN754404RC, interconnect 1', 'enabled': True,
                       'portName': 'd11',
                       'type': 'port',
                       }

downlink_d11_disable = {'interconnectName': 'CN754404RC, interconnect 1', 'enabled': False,
                        'portName': 'd11',
                        'type': 'port',
                        }

downlink_enable = {'interconnectName': 'EM1FFFF500, interconnect 1', 'enabled': True,
                       'portName': 'd3',
                       'type': 'port',
                       }

downlink_disable = {'interconnectName': 'EM1FFFF500, interconnect 1', 'enabled': False,
                        'portName': 'd3',
                        'type': 'port',
                        }

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
network_admin = {'userName': 'network', 'password': 'networkadmin'}
storage_admin = {'userName': 'storage', 'password': 'storageadmin'}
backup_admin = {'userName': 'backup', 'password': 'backupadmin'}
server_admin = {'userName': 'server', 'password': 'serveradmin'}
read_only = {'userName': 'readonly', 'password': 'readonly'}

users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]

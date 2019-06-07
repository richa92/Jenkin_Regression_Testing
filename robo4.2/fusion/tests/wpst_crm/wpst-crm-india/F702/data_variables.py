def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

lig1_ethernetsettings = {'type': 'EthernetInterconnectSettingsV3', 'enableRichTLV': True, 'interconnectType': 'Ethernet'}

li_set1 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": True, "enableTaggedLldp": True}
li_set2 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": False, "enableTaggedLldp": True}
li_set3 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": True, "enableTaggedLldp": False}
li_set4 = {"type": "EthernetInterconnectSettingsV201", "enableRichTLV": False, "enableTaggedLldp": False}

apic_admin_credentials = {"aaaUser": {
    "attributes": {
        "name": "admin", "pwd": "password"}}}


apic_ip = ['10.10.0.203', '10.10.5.16']

li_spp_downgrade = {'command': 'UPDATE', 'sppUri': '/rest/firmware-drivers/SPP2014090_2014_0710_89', 'force': True}

li_spp_upgrade = {'command': 'UPDATE', 'sppUri': '/rest/firmware-drivers/SPP2016100_2016_0917_171', 'force': False}

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

ethernet_networks1_201 = [{'name': 'eth-100',
                           'type': 'ethernet-networkV3',
                           'vlanId': 100,
                           'purpose': 'General',
                           'smartLink': True,
                           'privateNetwork': False,
                           'connectionTemplateUri': None,
                           'ethernetNetworkType': 'Tunnel'},
                          {'name': 'eth-101',
                           'type': 'ethernet-networkV3',
                           'vlanId': 101,
                           'purpose': 'General',
                           'smartLink': True,
                           'privateNetwork': False,
                           'connectionTemplateUri': None,
                           'ethernetNetworkType': 'Tunnel'},
                          ]

ethernet_networks1 = [{'name': 'eth-100',
                       'type': 'ethernet-networkV300',
                       'vlanId': 100,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},
                      {'name': 'eth-101',
                       'type': 'ethernet-networkV300',
                       'vlanId': 101,
                       'purpose': 'General',
                       'smartLink': True,
                       'privateNetwork': False,
                       'connectionTemplateUri': None,
                       'ethernetNetworkType': 'Tunnel'},
                      ]

network_sets = [{'name': 'netset1', 'type': 'network-set', 'networkUris': ['network-a'], 'nativeNetworkUri': None}]


enc_group_201 = {'name': 'EGLldp',
                 'type': 'EnclosureGroupV200',
                 'enclosureTypeUri': '/rest/enclosure-types/c7000',
                 'stackingMode': 'Enclosure',
                 'interconnectBayMappingCount': 8,
                 'configurationScript': None,
                 'interconnectBayMappings':
                 [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                     {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                     {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}

enc_group = {'name': 'EGLldp',
             'type': 'EnclosureGroupV400',
             'enclosureTypeUri': '/rest/enclosure-types/c7000',
             'stackingMode': 'Enclosure',
             'interconnectBayMappingCount': 8,
             'configurationScript': None,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}

enc_group_02 = {'name': 'EGLldp',
                'type': 'EnclosureGroupV200',
                'enclosureTypeUri': '/rest/enclosure-types/c7000',
                'stackingMode': 'Enclosure',
                'interconnectBayMappingCount': 8,
                'configurationScript': None,
                'interconnectBayMappings':
                [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                 {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                 {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}


encREAL = [{'hostname': '10.10.2.11', 'username': 'Administrator', 'password': 'Admin', 'enclosureGroupUri': 'EG:EGLldp', 'force': True, 'licensingIntent': 'OneViewNoiLO'}]

encs = encREAL
LIG1 = 'LIG1'
LE = 'WPST-PABA58-EN1'

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-100'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '1', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth-101'],
                       'primaryPort': None,
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'},
                                                  {'bay': '2', 'port': 'X2', 'speed': 'Auto'},
                                                  ]},
               }


icmap_02 = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric-20/40 F8 Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric-20/40 F8 Module'},

            ]
icmap = [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC Flex-10/10D Module'},
         {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC Flex-10/10D Module'},

         ]

ligs_201 = {'lig1':
            {'name': 'LIG1',
             'type': 'logical-interconnect-groupV3',
             'enclosureType': 'C7000',
             'interconnectMapTemplate': icmap,
             'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None},

            'ligTT':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
             'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None},

            'ligFT':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
             'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None},

            'ligTF':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None},

            'ligFF':
            {'name': 'LIG1',
                'type': 'logical-interconnect-groupV3',
                'enclosureType': 'C7000',
                'interconnectMapTemplate': icmap,
                'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
                'stackingMode': 'Enclosure',
                'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
                'state': 'Active',
                'telemetryConfiguration': None,
                'snmpConfiguration': None}
            }


ligs = {'lig1':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligTT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligFT':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': True, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligTF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': True, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},

        'ligFF':
        {'name': 'LIG1',
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': icmap,
         'uplinkSets': [uplink_sets['us1'].copy(), uplink_sets['us2'].copy()],
         'stackingMode': 'Enclosure',
         'ethernetSettings': {'type': 'EthernetInterconnectSettingsV201', 'enableRichTLV': False, 'enableTaggedLldp': False, 'interconnectType': 'Ethernet'},
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}


        }

server_profiles_201 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                        'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                        'boot': {'manageBoot': False},
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]},
                       ]

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SGH411DFYA, bay 6',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False},
                    'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-100', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:eth-101', 'mac': None, 'wwpn': '', 'wwnn': ''},
                                    ]},
                   ]

server_profiles1 = [{'type': 'ServerProfileV5', 'serverHardwareUri': 'SGH411DFYA, bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:SGH411DFYA', 'enclosureGroupUri': 'EG:EGLldp', 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'Sp_APIC', 'description': '', 'affinity': 'Bay',
                     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC1', 'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Flb 1:2-b', 'requestedMbps': '2500', 'networkUri': 'ETH:APIC2', 'boot': {'priority': 'Primary', 'targets': [{'arrayWwpn': '21110002AC003655', 'lun': '0'}]}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     ]},

                    ]

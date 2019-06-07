def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def Remove_Whitespace(instring):
    return instring.strip()


def convert_unicode_to_string(String):
    res = String.encode("utf-8")
    return res


SSH_PASS = 'hpvse1'
${APPLIANCE_IP}     15.245.131.72


LE = 'LE'
ENC1 = 'CN7544044G'
ENC2 = 'CN7545084V'
LIG1 = 'LIG1'
${Host}    15.245.131.72

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethnets = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_401",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 401
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_402",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 402
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_403",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 403
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_404",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 404
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_801",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 801
    }
]

uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth_401', 'eth_402', 'eth_403', 'eth_404'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth_401', 'eth_402', 'eth_801'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                                  ]},
               'us3': {'name': 'us3',
                       'ethernetNetworkType': 'Untagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['untaggednet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q2', 'speed': 'Auto'},
                                                  ]},
               'us4': {'name': 'us4',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['tunnelnet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                                  ]},
               'us_a': {'name': 'us_a',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['eth_401', 'eth_402'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'}
                                                   ]},
               'us_b': {'name': 'us_b',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['eth_401'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'}
                                                   ]

                        }
               }
LIGS_TB = [{'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                        ],

            'uplinkSets': [uplink_sets['us1'].copy()],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': None},

           {'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                        ],

            'uplinkSets': [uplink_sets['us2'].copy()],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': None
            },

           {'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
                                        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
                                        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
                                        ],

            'uplinkSets': [uplink_sets['us3'].copy(), uplink_sets['us4'].copy()],
            'enclosureIndexes': [1, 2],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': None}
           ]

enc_group = {'name': 'EG1',
             'enclosureCount': 2,
             'interconnectBayMappings':
             [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
                 {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
              ],
             'ipAddressingMode': 'DHCP',
             'ipRangeUris': [],
             'powerMode': 'RedundantPowerFeed'
             }

les = {'name': 'LE1',
       'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False

       }

Logical_Enclosure = {'name': 'LE1',
                     'enclosureUris': ['ENC:' + ENC2, 'ENC:' + ENC1],
                     'enclosureGroupUri': 'EG:EG1',
                     'firmwareBaselineUri': None,
                     'forceInstallFirmware': False
                     }

Enet = [{'name': 'untaggednet',
         'type': 'ethernet-networkV4',
         'vlanId': None,
         'purpose': 'General',
         'smartLink': True,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Untagged'},

        {'name': 'tunnelnet',
         'type': 'ethernet-networkV4',
         'vlanId': None,
         'purpose': 'General',
         'smartLink': True,
         'privateNetwork': False,
         'connectionTemplateUri': None,
         'ethernetNetworkType': 'Tunnel'}
        ]

network_sets = [{"name": "set1", "networkUris": ["eth_401", "eth_402"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None},
                {"name": "set2", "networkUris": ["eth_403", "eth_404"], "connectionTemplateUri":None, "type":"network-setV5", "nativeNetworkUri":None}]


Server_profile1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 10',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                           ]}}]

sp_vlan801 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 10',
               'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
               'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
               'name': 'profile_1', 'description': '', 'affinity': 'Bay',
               "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
               'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_801', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                      {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                       'requestedMbps': '2500', 'networkUri': 'ETH:eth_801', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                      ]}}]

sp_1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'profile_1', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                ]}}]

Server_profile1_temp = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 10',
                         'serverHardwareTypeUri': '', 'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'profile1', 'description': '', 'affinity': 'Bay',
                         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                 'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                 'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                                 'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnet', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                                 'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnet', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                ]}, 'serverProfileTemplateUri': 'profile_1'}]

SP_template = [{'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:EG1',
                'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                'boot': None, 'boot': {'manageBoot': False}, 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1'},
                                                       {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1'},
                                                       {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnet', 'lagName': 'LAG2'},
                                                       {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnet', 'lagName': 'LAG2'}

                                                       ], "manageConnections": True}}]

SP_netset = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 2',
              'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
              'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
              'name': 'profile_1', 'description': '', 'affinity': 'Bay',
              "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
              'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                               'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                              {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                               'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                              ]}]

sp_enc1_bay1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 10',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                 'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                 "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                 'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 5, 'name': '5', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_403', 'lagName': 'LAG3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 6, 'name': '6', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_403', 'lagName': 'LAG3', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 7, 'name': '7', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_404', 'lagName': 'LAG4', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 8, 'name': '8', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_404', 'lagName': 'LAG4', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                        ]}}]

sp_enc2_bay6 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 2',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                 'name': 'profile_2', 'description': '', 'affinity': 'Bay',
                 "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                 "connectionSettings": {"connections": [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_403', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_404', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                        ]}}]

Gen10Server_profiles = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 3',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'profile_bay2', 'description': '', 'affinity': 'Bay',
                         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'mac': None, 'wwpn': None, 'wwnn': None},
                                         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Auto',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_403', 'mac': None, 'wwpn': None, 'wwnn': None},
                                         {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Auto',
                                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_404', 'mac': None, 'wwpn': None, 'wwnn': None},

                                         ]}]

ilo_details_1 = {'ilo_ip': '15.245.132.37', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_2 = {'ilo_ip': '15.245.132.153', 'username': 'Administrator', 'password': 'hpvse1'}

server_details_enc1_bay1 = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse1'}
server_details_enc2_bay6 = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse1'}

ethernet_networks = [{'name': 'net_401',
                      'type': 'ethernet-networkV300',
                      'vlanId': 401,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}

                     ]

server = "CN754404R2, bay 1"
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Powershell_get_mac2 = "New-netlbfoteam -name 'Team2' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Powershell_get_mac3 = "New-netlbfoteam -name 'Team3' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Powershell_get_mac4 = "New-netlbfoteam -name 'Team4' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
team_cmd = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
team_status_cmd0 = "Get-NetLbfoTeam -Name 'Team1' | fl Name,Status"
team_status_cmd1 = "Get-NetLbfoTeam -Name 'Team2' | fl Name,Status"
team_status_cmd2 = "Get-NetLbfoTeam -Name 'Team3' | fl Name,Status"
team_status_cmd3 = "Get-NetLbfoTeam -Name 'Team4' | fl Name,Status"
detlete_team_cmd0 = "Remove-NetLbfoTeam 'Team1'"
detlete_team_cmd1 = "Remove-NetLbfoTeam 'Team2'"
detlete_team_cmd2 = "Remove-NetLbfoTeam 'Team3'"
detlete_team_cmd3 = "Remove-NetLbfoTeam 'Team4'"
# Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'switchindependent'"
linux_ilo_details = {'ilo_ip': '15.245.132.127', 'username': 'Administrator', 'password': 'hpvse123'}
linux_server_details = {'linux_ip': '', 'username': 'root', 'password': 'hpvse1'}
LACP_Alert = "Connection on downlink port 13, subport a  has failed. The subport is not an active member of the link aggregation group LAG1."
sp_lag = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 10',
           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'profile_1', 'description': '', 'affinity': 'Bay',
           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                  ]}}]

SP_no_con = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 6',
              'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
              'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
              'name': 'profile_1', 'description': '', 'affinity': 'Bay',
              "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
              'connectionSettings': {'connections': []}}]

SP_non_lag = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 10',
               'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
               'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
               'name': 'profile_1', 'description': '', 'affinity': 'Bay',
               "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
               'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                      {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                       'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                      ]}}]


sp_networks_sets = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'Profile-Enc2-Bay3-Gen10-Win', 'description': '', 'affinity': 'Bay',
                     "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                             'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                            {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                             'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                            ]}}]

sp_tagged_net = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                  'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                  'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                  'name': 'Profile1', 'description': '', 'affinity': 'Bay',
                  "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                  'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                          'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                          'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                         {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                          'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnet', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                         {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                          'requestedMbps': '2500', 'networkUri': 'ETH:tunnelnet', 'lagName': 'LAG2', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                         ]}}]

server_profile2 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC2 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'profile_2', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}


                                                           ]}}]

icbays = ['3', '6']
Chloride_icbays = ['6', '3']
Enc = ['CN7544044G', 'CN7545084V']
Action = ['EFuseOn', 'EFuseOff']
state = ['Absent', 'Configured']
Bladeserver = ['10', '']
Bladebay = ['CN7544044G, bay 10', '']
INTERCONNECTS = ['CN7544044G, interconnect 3', 'CN7545084V, interconnect 6']
INTERCONNECT = ['CN7544044G, interconnect 6', 'CN7545084V, interconnect 3']
windows_ilo_details = {'ilo_ip': '15.245.133.62', 'username': 'Administrator', 'password': 'hpvse123'}
windows_ilo_details1 = {'ilo_ip': '15.245.132.58', 'username': 'Administrator', 'password': 'hpvse123'}
Interconnects_chloride = ['CN7545084V, interconnect 3', 'CN7544044G, interconnect 6']

Interconnects_potash = ['CN7545084V, interconnect 6', 'CN7544044G, interconnect 3']
windows_server_details = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse1'}
windows_server_details1 = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse1'}

interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]
interconnect_potash = ['CN7545084V, interconnect 6', 'CN7544044G, interconnect 3']
uplink_ports = ['Q6', 'Q6']
downlink_ports = ['d22', 'd10']
ic_disable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":"", "portStatus":"Linked", "type":"portV5"}]
ic_enable_body = [{"associatedUplinkSetUri": "", "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":True, "portName":"", "portStatus":"Linked", "type":"portV5"}]
disable_status = 'Unlinked'
enable_status = 'Linked'
lag_list = ['LAG1', 'LAG1']


sp_diff_bandwidth = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                      'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                      "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                              'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                             {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                              'requestedMbps': '3500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                             ]}}]

sp_diff_adapters = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                     "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                            {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                            ]}}]

sp_diff_networks = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                     "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                            {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                            ]}}]

sp_diff_networks_sets = [[{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                           'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set2', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                  ]}}],

                         [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                           'name': 'profile_1', 'description': '', 'affinity': 'Bay',
                           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                  ]}}]]

sp_one_lag = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 1',
               'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
               'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
               'name': 'profile_1', 'description': '', 'affinity': 'Bay',
               "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
               'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                      ]}}]

LIGS_Aside_Bside = [{'name': 'LIG_A',
                     'type': 'logical-interconnect-groupV5',

                     'enclosureType': 'SY12000',
                     'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
                                                 {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}
                                                 ],

                     'uplinkSets': [uplink_sets['us_a'].copy()],
                     'enclosureIndexes': [1, 2],
                     'interconnectBaySet': 3,
                     'redundancyType': 'NonRedundantASide',
                     'internalNetworkUris': [],
                     'snmpConfiguration': {'type': 'snmp-configuration',
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'category': 'snmp-configuration'
                                           }},
                    {'name': 'LIG_B',
                     'type': 'logical-interconnect-groupV5',
                     'enclosureType': 'SY12000',
                     'interconnectMapTemplate': [{'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
                                                 {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1}
                                                 ],

                     'uplinkSets': [uplink_sets['us_b'].copy()],
                     'enclosureIndexes': [1, 2],
                     'interconnectBaySet': 3,
                     'redundancyType': 'NonRedundantBSide',
                     'internalNetworkUris': [],
                     'snmpConfiguration': {'type': 'snmp-configuration',
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'v3Enabled': True,
                                           'enabled': False,
                                           'category': 'snmp-configuration'
                                           }}
                    ]

enc_group1 = {'name': 'EG1',
              'enclosureCount': 2,
              'interconnectBayMappings':
              [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_A'},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_B'}],
              'ipAddressingMode': 'DHCP',
              'ipRangeUris': [],
              'powerMode': 'RedundantPowerFeed'
              }

LE = {'name': 'LE_AB',
      'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],  # REAL
      'enclosureGroupUri': 'EG:EG1',
      'firmwareBaselineUri': None,
      'forceInstallFirmware': False}

th = ["Copyright (C) 2013 Microsoft Corporation. All rights reserved.\r\nPS C:\\Users\\Administrator>\x1b[25;28f\x1b[25;28f\x1b[24;28fGet-NetAdapter | where MacAddress -eq '00-BA-51-00-00\r\n-1D' | Select Name\n\x1b[26;1f\n\x1b[25;1f\x1b[1;1f \x1b[2;1f \x1b[3;1fPS C:\\Users\\Administrator> Powershell\x1b[4;1fWindows PowerShell\x1b[5;1fCopyright (C) 2013 Microsoft Corporation. All rights reserved.\x1b[6;1f \x1b[7;1fPS C:\\Users\\Administrator> Get-NetAdapter | where MacAddress -e\x1b[8;1f-1C' | Select Name\x1b[9;1f \x1b[10;1fName \x1b[11;1f----\x1b[12;1fEthernet 12\x1b[13;1f \x1b[14;1f \x1b[15;1fPS C:\\Users\\Administrator> Powershell\x1b[16;1fWindows PowerShell\x1b[17;1fCopyright (C) 2013 Microsoft Corporation. All rights reserved.\x1b[18;1f \x1b[19;1fPS C:\\Users\\Administrator> Get-NetAdapter | where MacAddress -eq '00-BA-51-00-00\x1b[20;1f-1D' | Select Name\x1b[21;1f \x1b[22;1fName \x1b[23;1f----\x1b[24;1fEthernet 9\r\n\r\n\r\nPS C:\\Users\\Administrator>\x1b[27;28f\x1b[27;28f"]

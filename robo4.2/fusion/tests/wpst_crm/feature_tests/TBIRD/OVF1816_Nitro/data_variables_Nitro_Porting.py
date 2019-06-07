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

LE = 'LE'
enc_count = 3
frame = 3
ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZH'
ENC3 = 'MXQ81804ZG'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]
LIG1 = 'LIG1'
Enc = ['MXQ81804ZF', 'MXQ81804ZH', 'MXQ81804ZG']
SSH_PASS = 'hpvse1'

FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'hpvse123'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC
FUSION_IP = '15.245.131.251'
IC_SSH_USERNAME = 'root'
IC_TIMEOUT = 100
IC_PROMPT = '>'
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
    }
]

uplink_sets = {'us1': {'name': 'us1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth_401', 'eth_402', 'eth_403', 'eth_404'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth_401', 'eth_402', 'eth_403', 'eth_404', 'net_405'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
                                                  ]},
               'us3': {'name': 'us3',
                       'ethernetNetworkType': 'Untagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['untaggednet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q6', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q6', 'speed': 'Auto'},
                                                  ]},

               'us4': {'name': 'us4',
                       'ethernetNetworkType': 'Tunnel',
                       'networkType': 'Ethernet',
                       'networkUris': ['tunnelnet'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                  {'enclosure': '2', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
                                                  ]},
               'us_a': {'name': 'us_a',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['eth_401', 'eth_402'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'}
                                                   ]},
               'us_b': {'name': 'us_b',
                        'ethernetNetworkType': 'Tagged',
                        'networkType': 'Ethernet',
                        'networkUris': ['eth_401'],
                        'nativeNetworkUri': None,
                        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'}
                                                   ]

                        }
               }


LIGS_TB = [{'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
                {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
                {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
            ],
            'uplinkSets': [uplink_sets['us1'].copy()],
            'downlinkSpeedMode': 'SPEED_25GB',
            'enclosureIndexes': [x for x in xrange(1, frame + 1)],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'readCommunity': 'public',
                                  'systemContact': '',
                                  'enabled': 'true',
                                  'category': 'snmp-configuration',
                                  'trapDestinations': [],
                                  'snmpAccess': [],
                                  'snmpUsers': [],
                                  'uri': '',
                                  'v3Enabled': 'true'
                                  }},
           {'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
                {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
                {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
            ],
            'uplinkSets': [uplink_sets['us2'].copy()],
            'downlinkSpeedMode': 'SPEED_25GB',
            'enclosureIndexes': [x for x in xrange(1, frame + 1)],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'readCommunity': 'public',
                                  'systemContact': '',
                                  'enabled': 'true',
                                  'category': 'snmp-configuration',
                                  'trapDestinations': [],
                                  'snmpAccess': [],
                                  'snmpUsers': [],
                                  'uri': '',
                                  'v3Enabled': 'true'
                                  }},

           {'name': 'LIG1',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [
                {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
                {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
                {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
                {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
                {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
            ],

            'uplinkSets': [uplink_sets['us3'].copy(), uplink_sets['us4'].copy()],
            'downlinkSpeedMode': 'SPEED_25GB',
            'enclosureIndexes': [x for x in xrange(1, frame + 1)],
            'interconnectBaySet': 3,
            'redundancyType': 'HighlyAvailable',
            'internalNetworkUris': [],
            'snmpConfiguration': {'type': 'snmp-configuration',
                                  'readCommunity': 'public',
                                  'systemContact': '',
                                  'enabled': 'true',
                                  'category': 'snmp-configuration',
                                  'trapDestinations': [],
                                  'snmpAccess': [],
                                  'snmpUsers': [],
                                  'uri': '',
                                  'v3Enabled': 'true'
                                  }}
           ]

enc_group = {'name': 'EG1',
             'enclosureCount': 3,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'}],
             'ipAddressingMode': 'DHCP',
             'ipRangeUris': [],
             'powerMode': 'RedundantPowerFeed'
             }

les = {'name': 'LE',
       'enclosureUris': ENC_List[0:frame],
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False

       }

Logical_Enclosure = {'name': 'LE1',
                     'enclosureUris': ['ENC:' + ENC2, 'ENC:' + ENC1],
                     'enclosureGroupUri': 'EG:EG1',
                     'firmwareBaselineUri': None,
                     'forceInstallFirmware': False}


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


network_sets = [{"name": "set1", "networkUris": ["eth_401"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None},
                {"name": "set2", "networkUris": ["eth_403", "eth_404"], "connectionTemplateUri":None, "type":"network-setV4", "nativeNetworkUri":None}]

update_network_set1 = {"name": "set1", "networkUris": ["eth_401", "eth_402", "net_405"], "connectionTemplateUri": None, "type": "network-setV4", "nativeNetworkUri": None}
Server_profile1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                           ]}}]

sp_1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
         'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
         "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
         'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                 'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                ]}}]

Server_profile1_temp = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
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
                                                                ]}, 'serverProfileTemplateUri': ''}]

SP_template = [{'type': 'ServerProfileTemplateV6', 'serverProfileDescription': '',
                'serverHardwareTypeUri': 'SHT:SY 480 Gen10 5', 'enclosureGroupUri': 'EG:EG1',
                'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                "boot": None, 'boot': {'manageBoot': False}, 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1'},
                                                       {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                        'requestedMbps': '2500', 'networkUri': 'ETH:untaggednet', 'lagName': 'LAG1'}

                                                       ], "manageConnections": True}}]

SP_netset = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 4',
              'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
              'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
              'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
              "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
              'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                               'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                              {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                               'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                              ]}]

sp_enc1_bay1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:EG1',
                 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                 'name': 'profile_bay6', 'description': '', 'affinity': 'Bay',
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

sp_enc2_bay6 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                 'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                 "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                 "connectionSettings": {"connections": [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_403', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                        {'id': 4, 'name': '4', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_404', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                        ]}}]

Gen10Server_profiles = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 4',
                         'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                         'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                         'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
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

ilo_details_enc1_bay1 = {'ilo_ip': '15.245.133.8', 'username': 'Administrator', 'password': 'hpvse123'}
ilo_details_enc2_bay6 = {'ilo_ip': '15.245.133.7', 'username': 'Administrator', 'password': 'hpvse123'}


server_details_enc1_bay1 = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse@1'}
server_details_enc2_bay6 = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse@1'}

ethernet_networks = [{'name': 'net_405',
                      'type': 'ethernet-networkV300',
                      'vlanId': 405,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}

                     ]

server = "MXQ81804ZF, bay 1"
server6 = "MXQ81804ZG, bay 2"
Powershell_get_mac = "Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name"
Powershell_get_mac1 = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Powershell_get_mac2 = "New-netlbfoteam -name 'Team2' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Powershell_get_mac3 = "New-netlbfoteam -name 'Team3' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
Powershell_get_mac4 = "New-netlbfoteam -name 'Team4' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
tagging_cmd = "Add-NetLbfoTeamNIC -Team 'Team1' -VlanID 'vlan_id'"
remove_tagging_cmd = "Remove-NetLbfoTeamNIC -Team 'Team1' -VlanID 'vlan_id'"
team_cmd = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
team_status_cmd0 = "Get-NetLbfoTeam -Name 'Team1' | fl Name,Status"
team_status_cmd1 = "Get-NetLbfoTeam -Name 'Team2' | fl Name,Status"
team_status_cmd2 = "Get-NetLbfoTeam -Name 'Team3' | fl Name,Status"
team_status_cmd3 = "Get-NetLbfoTeam -Name 'Team4' | fl Name,Status"
detlete_team_cmd0 = "Remove-NetLbfoTeam 'Team1'"
detlete_team_cmd1 = "Remove-NetLbfoTeam 'Team2'"
detlete_team_cmd2 = "Remove-NetLbfoTeam 'Team3'"
detlete_team_cmd3 = "Remove-NetLbfoTeam 'Team4'"

linux_ilo_details = {'ilo_ip': '15.245.132.127', 'username': 'Administrator', 'password': 'hpvse123'}
linux_server_details = {'linux_ip': '', 'username': 'root', 'password': 'hpvse1'}
LACP_Alert = "Connection on downlink port 13, subport a  has failed. The subport is not an active member of the link aggregation group LAG1."
sp_lag = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                  ]}}]

sp_ns = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
          'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
          'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
          "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
          'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                  'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                  'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                 {'id': 3, 'name': '3', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                 ]}}]

SP_no_con = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 6',
              'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
              'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
              'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
              "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
              'connectionSettings': {'connections': []}}]

SP_non_lag = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
               'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
               'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
               'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
               "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
               'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                      {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                       'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                      ]}}]


sp_networks_sets = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC2 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'Profile-Enc2-Bay3-Gen10-Win', 'description': '', 'affinity': 'Bay',
                     "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                             'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                            {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                             'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                            ]}}]

sp_tagged_net = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 4',
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

server_profile2 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'profile_bay6', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Auto',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'mac': None, 'wwpn': None, 'wwnn': None}


                                                           ]}}]

Nitro_icbays = ['3', '6']
methane_icbays = ['6', '3']
upload_timeout = '4200'
Action = ['EFuseOn', 'EFuseOff']
state = ['Absent', 'Configured']
Bladeserver = ['1', '']
Bladebay = ['MXQ81804ZF, bay 1', '']
Interconnect_dto = [{'name': 'MXQ81804ZF, interconnect 3'}, {'name': 'MXQ81804ZH, interconnect 6'}]
Interconnect_dto_Methane = [{'name': 'MXQ81804ZF, interconnect 6'}, {'name': 'MXQ81804ZH, interconnect 3'}]
INTERCONNECTS = ['MXQ81804ZF, interconnect 3', 'MXQ81804ZH, interconnect 6']
INTERCONNECT = ['CN754404R2, interconnect 3', 'CN754406W5, interconnect 6']
windows_ilo_details = {'ilo_ip': '15.245.133.62', 'username': 'Administrator', 'password': 'hpvse123'}
windows_ilo_details1 = {'ilo_ip': '15.245.132.58', 'username': 'Administrator', 'password': 'hpvse123'}
interconnect_nitro = ['MXQ81804ZF, interconnect 3', 'MXQ81804ZH, interconnect 6']
interconnect_support = ['MXQ81804ZF, interconnect 6', 'MXQ81804ZH, interconnect 3']
windows_server_details = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse@1'}
windows_server_details1 = {'windows_ip': '', 'username': 'Administrator', 'password': 'hpvse@1'}
interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]
uplink_ports = ['Q3', 'Q3']
downlink_ports = ['d13', 'd13']
ic_disable_body = [{"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":uplink_ports[0], "portStatus":"Linked", "type":"port"},
                   {"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":uplink_ports[1], "portStatus":"Linked", "type":"port"}]
ic_enable_body = [{"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":True, "portName":uplink_ports[0], "portStatus":"Linked", "type":"port"},
                  {"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":True, "portName":uplink_ports[1], "portStatus":"Linked", "type":"port"}]
disable_status = 'Unlinked'
enable_status = 'Linked'
lag_list = ['LAG1', 'LAG1']

ic_disable_body_downlink = [{"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":downlink_ports[0], "portStatus":"Linked", "type":"port"},
                            {"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":downlink_ports[1], "portStatus":"Linked", "type":"port"}]
ic_enable_body_downlink = [{"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":True, "portName":downlink_ports[0], "portStatus":"Linked", "type":"port"},
                           {"associatedUplinkSetUri": uplink_sets['us1']['name'], "interconnectName": "", "portType": "Downlink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":True, "portName":downlink_ports[1], "portStatus":"Linked", "type":"port"}]


sp_diff_bandwidth = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                      'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                      'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                      'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                      "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                      'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                              'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                             {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                              'requestedMbps': '3500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                             ]}}]

sp_diff_adapters = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                     "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                            {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                            ]}}]

sp_diff_networks = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                     'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                     "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                     'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                            {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                             'requestedMbps': '2500', 'networkUri': 'ETH:eth_402', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                            ]}}]

sp_diff_networks_sets = [[{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                           'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set2', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                  ]}}],

                         [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                           'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                           'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                                  {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                                   'requestedMbps': '2500', 'networkUri': 'NS:set1', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                                  ]}}]]

sp_one_lag = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
               'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
               'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
               'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
               "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
               'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                      ]}}]

LIGS_Aside_Bside = [{'name': 'LIG_A',
                     'type': 'logical-interconnect-groupV4',

                     'enclosureType': 'SY12000',
                     'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
                                                 {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                                                 {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}],

                     'uplinkSets': [uplink_sets['us_a'].copy()],
                     'downlinkSpeedMode':'SPEED_25GB',
                     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                     'interconnectBaySet': 3,
                     'redundancyType': 'NonRedundantASide',
                     'internalNetworkUris': [],
                     'snmpConfiguration': {'type': 'snmp-configuration',
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'enabled': 'true',
                                           'category': 'snmp-configuration',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'snmpUsers': [],
                                           'uri': '',
                                           'v3Enabled': 'true'
                                           }},
                    {'name': 'LIG_B',
                     'type': 'logical-interconnect-groupV4',
                     'enclosureType': 'SY12000',
                     'interconnectMapTemplate': [{'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
                                                 {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
                                                 {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}],

                     'uplinkSets': [uplink_sets['us_b'].copy()],
                     'downlinkSpeedMode':'SPEED_25GB',
                     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
                     'interconnectBaySet': 3,
                     'redundancyType': 'NonRedundantBSide',
                     'internalNetworkUris': [],
                     'snmpConfiguration': {'type': 'snmp-configuration',
                                           'readCommunity': 'public',
                                           'systemContact': '',
                                           'enabled': 'true',
                                           'category': 'snmp-configuration',
                                           'trapDestinations': [],
                                           'snmpAccess': [],
                                           'snmpUsers': [],
                                           'uri': '',
                                           'v3Enabled': 'true'
                                           }}
                    ]

enc_group1 = {'name': 'EG1',
              'enclosureCount': 3,
              'interconnectBayMappings':
              [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_A'},
               {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
               {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG_B'}],
              'ipAddressingMode': 'DHCP',
              'ipRangeUris': [],
              'powerMode': 'RedundantPowerFeed'
              }

LE = {'name': 'LE_AB',
      'enclosureUris': ENC_List[0:frame],  # REAL
      'enclosureGroupUri': 'EG:EG1',
      'firmwareBaselineUri': None,
      'forceInstallFirmware': False}

ping_file = ['ping_serverip0.txt', 'ping_serverip1.txt', 'ping_serverip2.txt', 'ping_serverip3.txt', 'ping_serverip4.txt', 'ping_serverip5.txt', 'ping_serverip6.txt', 'ping_serverip7.txt']
team = ['ping_teamip0.txt', 'ping_teamip1.txt', 'ping_teamip2.txt', 'ping_teamip3.txt']
name = ['serverip0.txt', 'serverip1.txt', 'serverip2.txt', 'serverip3.txt']
team0 = ['teamip.txt']
server2file = ['server2file0.txt', 'server2file1.txt', 'server2file2.txt', 'server2file3.txt']
ICMabsent = ['ICMabsent0.txt', 'ICMabsent1.txt']
ICMconfigured_ips = ['ICMconfigured_ips0.txt', 'ICMconfigured_ips1.txt']
ping_enable_downlink = ['pingfile_enable_downlink1.txt', 'pingfile_enable_downlink2.txt']
Team_Ip = ['10.11.4.118']

Edit_LIG = [{'name': 'LIG1',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': [
                 {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
                 {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
                 {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
                 {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
                 {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
                 {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
             ],

             'uplinkSets': [uplink_sets['us1'].copy()],
             'downlinkSpeedMode': 'SPEED_25GB',
             'enclosureIndexes': [x for x in xrange(1, frame + 1)],
             'interconnectBaySet': 3,
             'redundancyType': 'HighlyAvailable',
             'internalNetworkUris': [],
             'snmpConfiguration': {'type': 'snmp-configuration',
                                   'readCommunity': 'public',
                                   'systemContact': '',
                                   'enabled': 'true',
                                   'category': 'snmp-configuration',
                                   'trapDestinations': [],
                                   'snmpAccess': [],
                                   'snmpUsers': [],
                                   'uri': '',
                                   'v3Enabled': 'true'
                                   }}]

sp_edit_network = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                    'name': 'profile_bay1', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},

                                                           ]}}]

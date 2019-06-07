import os


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


APPLIANCE_IP = '15.245.131.251'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZG'
ENC3 = 'MXQ81804ZH'
LIG1 = 'LIG1'
LI = 'LE1' + '-' + 'LIG1'
ENCLOSURE_URIS = ['ENC:' + ENC1, 'ENC:' + ENC3, 'ENC:' + ENC2]

Enc_Count = 3
IBS = 3

if Enc_Count == 1:
    logicalPortConfigInfo = [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                             {'enclosure': '1', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
                             ]
elif Enc_Count == 2:
    logicalPortConfigInfo = [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                             {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
                             ]
elif Enc_Count == 3:
    logicalPortConfigInfo = [{'enclosure': '1', 'bay': '3', 'port': 'Q3', 'speed': 'Auto'},
                             {'enclosure': '2', 'bay': '6', 'port': 'Q3', 'speed': 'Auto'},
                             ]

ethnets = [
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_401",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "connectionTemplateUri": None,
        "vlanId": "401"
    },
    {
        "type": "ethernet-networkV4",
        "ethernetNetworkType": "Tagged",
        "name": "eth_402",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "connectionTemplateUri": None,
        "vlanId": "402"
    }
]

uplink_sets = {'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth_401', 'eth_402'],
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'logicalPortConfigInfos': logicalPortConfigInfo
                       }
               }

icmap_1 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

icmap_2 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

icmap_3 = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

if Enc_Count == 1:
    REDUNDANCY = 'Redundant'
    InterconnectMapTemplate = icmap_1
elif Enc_Count == 2:
    REDUNDANCY = 'HighlyAvailable'
    InterconnectMapTemplate = icmap_2
elif Enc_Count == 3:
    REDUNDANCY = 'HighlyAvailable'
    InterconnectMapTemplate = icmap_3

LIGS_TB = [{'name': 'LIG1',
            'type': 'logical-interconnect-groupV6',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': InterconnectMapTemplate,
            'uplinkSets': [uplink_sets['us2'].copy()],
            'enclosureIndexes': [x for x in xrange(1, Enc_Count + 1)],
            'interconnectBaySet': IBS,
            'downlinkSpeedMode': 'SPEED_25GB',
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'redundancyType': REDUNDANCY,
            'internalNetworkUris': [],
            'snmpConfiguration': None},
           ]
diff_sample_count = ['50']
diff_sample_interval = ['60']

Li_body_telemetry = {"type": "telemetry-configuration",
                     "enableTelemetry": True,
                     "sampleCount": 300,
                     "sampleInterval": 60,
                     "description": None,
                     "status": None,
                     "name": "",
                     "state": None,
                     "eTag": None,
                     "created": None,
                     "modified": None,
                     "category": "telemetry-configurations",
                     "uri": ""}

enc_group = {'name': 'EG1',
             'enclosureCount': Enc_Count,
             'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
              ],
             'ipAddressingMode': 'DHCP',
             'ipRangeUris': [],
             'powerMode': 'RedundantPowerFeed'
             }

les = {'name': 'LE1',
       'enclosureUris': ENCLOSURE_URIS,
       'enclosureGroupUri': 'EG:EG1',
       'firmwareBaselineUri': None,
       'forceInstallFirmware': False}

sp_lag = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'profile1', 'description': '', 'affinity': 'Bay',
           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
           'connectionSettings': {'connections': []}}]

Server_profile1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'profile1', 'description': '', 'affinity': 'Bay',
                    'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto", 'secureBoot': 'Disabled'},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                           ]}}]

ilo_details_enc1_bay11 = {'ilo_ip': '15.245.133.8', 'username': 'Administrator', 'password': 'hpvse123', 'OS': 'windows', 'type': 'Gen10'}
server_details_enc1_bay11 = {'ip': '', 'username': 'Administrator', 'password': 'hpvse@1', 'OS': 'windows', 'type': 'Gen10'}
file1 = 'Adapter_List.txt'

NITRO3 = ENC1 + ', ' + 'interconnect 3'
NITRO6 = ENC3 + ', ' + 'interconnect 6'

INTERCONNECTS = [NITRO3, NITRO6]

Linked_ports = [['Q3', 'Q3'], ['d1', 'd13']]
stats_flag = ['uplink', 's_channel']
stats_lag_flag = ['uplink_lag', 's_channel_lag']
subport_no = [None, 1]

kill_cmd = "TASKKILL /F /IM PING.EXE"

Powershell_get_mac = "cmd /c powershell \"Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name\" > %s" % file1

team_cmd = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
delete_team_cmd = "Remove-NetLbfoTeam 'Team1'"

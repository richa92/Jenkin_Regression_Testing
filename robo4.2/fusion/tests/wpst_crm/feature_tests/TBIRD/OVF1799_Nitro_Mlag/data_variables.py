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


APPLIANCE_IP = '15.245.131.108'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

LE = 'LE'
ENC1 = 'CN754406WY'
ENC2 = 'xxxxxxxxxx'
LIG1 = 'LIG1'
LI = 'LE1' + '-' + 'LIG1'

ENCLOSURE_URIS = ['ENC:' + ENC1]


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
    }
]

uplink_sets = {'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['eth_401', 'eth_402'],
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1', 'speed': 'Auto'},
                                                  {'enclosure': '1', 'bay': '6', 'port': 'Q1', 'speed': 'Auto'},
                                                  ]
                       }
               }

LIGS_TB = [{'name': 'LIG1',
            'type': 'logical-interconnect-groupV6',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
                                        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
                                        ],
            'uplinkSets': [uplink_sets['us2'].copy()],
            'enclosureIndexes': [1],
            'interconnectBaySet': 3,
            'redundancyType': 'Redundant',
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
             'enclosureCount': 1,
             'interconnectBayMappings':
             [{'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + 'LIG1'},
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
       'forceInstallFirmware': False

       }

sp_lag = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 11',
           'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
           'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
           'name': 'profile1', 'description': '', 'affinity': 'Bay',
           "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
           'connectionSettings': {'connections': []}}]

Server_profile1 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC1 + ', bay 11',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG1',
                    'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                    'name': 'profile1', 'description': '', 'affinity': 'Bay',
                    "boot": None, 'boot': {'manageBoot': False}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                    'connectionSettings': {'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None},
                                                           {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401', 'lagName': 'LAG1', 'mac': None, 'wwpn': None, 'wwnn': None}
                                                           ]}}]

ilo_details_enc1_bay11 = {'ilo_ip': '15.245.132.173', 'username': 'Administrator', 'password': 'password@123', 'OS': 'windows', 'type': 'Gen10'}
server_details_enc1_bay11 = {'windows_ip': '', 'username': 'Administrator', 'password': 'password@123', 'OS': 'windows', 'type': 'Gen10'}
file1 = 'Adapter_List.txt'

NITRO3 = ENC1 + ', ' + 'interconnect 3'
NITRO6 = ENC1 + ', ' + 'interconnect 6'

INTERCONNECTS = [NITRO3, NITRO6]

Linked_ports = [['Q1', 'Q1'], ['d11', 'd11']]
stats_flag = ['uplink', 's_channel']
stats_lag_flag = ['uplink_lag', 's_channel_lag']
subport_no = [None, 1]

kill_cmd = "TASKKILL /F /IM PING.EXE"

Powershell_get_mac = "cmd /c powershell \"Get-NetAdapter | where MacAddress -eq 'pppppppp' | Select Name\" > %s" % file1

team_cmd = "New-netlbfoteam -name 'Team1' -TeamMembers 'pppp','qqq' -TeamingMode 'LACP'"
delete_team_cmd = "Remove-NetLbfoTeam 'Team1'"

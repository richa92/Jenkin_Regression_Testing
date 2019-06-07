"""Data Variable"""


def make_range_list(start, end, prefix='net_', suffix=''):
    """Function Definition"""
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def Remove_Whitespace(instring):
    """Function Definition"""
    return instring.strip()


def convert_unicode_to_string(String):
    """Function Definition"""
    res = String.encode('utf-8')
    return res


SSH_PASS = 'hpvse1'

APPLIANCE_IP = "15.186.9.20"
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180
IC_SSH_USERNAME = "root"
IC_TIMEOUT = 100
IC_PROMPT = '>'

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator'}], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator'}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
          'type': 'UserAndPermissions'}]

ENC1 = 'CN750160YS'
loggerlevel = r'INFO'   # use INFO|DEBUG

fcnets = [{"type": "fc-networkV4",
           "name": "FC_1",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           },
          {"type": "fc-networkV4",
           "name": "FC_2",
           "fabricType": "FabricAttach",
           "linkStabilityTime": 30,
           "autoLoginRedistribution": True
           }]

uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed16G'}]}
               }
neg_uplink_sets = {'name': 'UplinkSet_2_1',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_1'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': 'Q1:4', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}
                                       ]}

neg_uplink_sets1 = {'name': 'UplinkSet_2_1',
                    'ethernetNetworkType': 'NotApplicable',
                    'networkType': 'FibreChannel',
                    'networkUris': [],
                    'fcNetworkUris': ['FC_2'],
                    'fcoeNetworkUris': [],
                    'lacpTimer': 'Short',
                    'logicalInterconnectUri': None,
                    'primaryPortLocation': None,
                    'manualLoginRedistributionState': 'Supported',
                    'connectionMode': 'Auto',
                    'nativeNetworkUri': None,
                    'portConfigInfos': [{'bay': '4', 'port': '2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}
                                        ]}

neg_uplink_sets122 = {'Uplinkset_neg': {'name': 'US-FC3',
                                        'networkType': 'FibreChannel',
                                        'networkUris': [],
                                        'fcNetworkUris': ['FC_2'],
                                        'fcoeNetworkUris': [],
                                        'lacpTimer': 'Short',
                                        'logicalInterconnectUri': None,
                                        'primaryPortLocation': None,
                                        'manualLoginRedistributionState': 'NotSupported',
                                        'connectionMode': 'Auto',
                                        'nativeNetworkUri': None,
                                        'portConfigInfos': [{'enclosure': ENC1, 'bay': '4', 'port': '2', 'desiredSpeed': 'Auto'}]}}


Lig_name = 'LIG1'
Lig_name_A = "LIG_A_Side"
Lig_name_B = "LIG_B_Side"

interconnects = [ENC1 + ', interconnect 1', ENC1 + ', interconnect 4']
ic_bay1 = interconnects[0].split()[-1]
ic_bay2 = interconnects[1].split()[-1]
analyzer_port_qport = "Q1:4"
analyzer_port_2_bay4 = "2"
analyzer_qport3_bay1 = "Q1:3"
used_uplink_port = "Q1:1"
used_uplink_port_bay4 = 1

port_map = {
    '1': '25', '2': '26', '3': '27', '4': '28', '5': '29', '6': '30', '7': '31', '8': '0',
    'Q1:1': '32', 'Q1:2': '33', 'Q1:3': '34', 'Q1:4': '35',
    'Q2:1': '36', 'Q2:2': '37', 'Q2:3': '38', 'Q2:4': '39',
    'Q3:1': '40', 'Q3:2': '41', 'Q3:3': '42', 'Q3:4': '43',
    'Q4:1': '44', 'Q4:2': '45', 'Q4:3': '46', 'Q4:4': '47'}
analyzer_dport = "d1"

li_portmonitor = {"type": "port-monitorV1",
                  "enablePortMonitor": 'true',
                  "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                   "portUri": "UplinkportUri"},
                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"}]
                  }


li_portmonitor_to_server = {"type": "port-monitorV1",
                            "enablePortMonitor": 'true',
                            "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                             "portUri": "UplinkportUri"},
                            "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                "portUri": "DownlinkportUri"}]
                            }

li_portmonitor_from_server = {"type": "port-monitorV1",
                              "enablePortMonitor": 'true',
                              "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                               "portUri": "UplinkportUri"},
                              "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredFromServer",
                                                  "portUri": "DownlinkportUri"}]
                              }

pm_timer = 500
cli_login = 60

ligs = {'lig1':
        {'name': Lig_name,
         'type': 'logical-interconnect-groupV7',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
                 'eTag': None,
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         },
        'lig2':
        {'name': Lig_name_A,
         'type': 'logical-interconnect-groupV7',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'NonRedundantASide',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         },
        'lig3':
        {'name': Lig_name_B,
         'type': 'logical-interconnect-groupV7',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 16Gb FC Module for Synergy', 'enclosureIndex': -1}],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'NonRedundantBSide',
         'uplinkSets': [uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': {'type': 'snmp-configuration',
                               'readCommunity': 'public',
                               'systemContact': '',
                               'enabled': 'true',
                               'category': 'snmp-configuration'
                               }
         }
        }
EG = 'EG1'
EG_Aside = "EG_Aside"
EG_Bside = "EG_Bside"
enc_groups = {'enc_group_1':
              {'name': EG,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:' + Lig_name},
                {'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:' + Lig_name}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group_Aside':
              {'name': EG_Aside,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 1, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:' + Lig_name_A}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               },
              'enc_group_Bside':
              {'name': EG_Bside,
               'enclosureCount': 1,
               'configurationScript': None,
               'interconnectBayMappings':
               [{'interconnectBay': 4, 'enclosureIndex': 1, 'logicalInterconnectGroupUri': 'LIG:' + Lig_name_B}
                ],
               'ipAddressingMode': 'External',
               'ipRangeUris': [],
               'powerMode': 'RedundantPowerFeed'
               }
              }


les = {'le1':
       {'name': 'LE_HA',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:' + EG,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       'le2':
       {'name': 'LE_A_side',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:' + EG_Aside,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        },
       'le3':
       {'name': 'LE_B_side',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:' + EG_Bside,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       }
LI = "LE_HA" + '-' + "LIG1" + '-1'
LI_A = les['le2']['name'] + '-' + Lig_name_A + '-1'
LI_B = les['le3']['name'] + '-' + Lig_name_B + '-1'

sfp_connector_16 = {"portName": "1",
                                "vendorName": "HP-A     BROCADE",
                                "vendorPartNumber": "QK724A",
                                "vendorRevision": "A",
                                "speed": "null",
                                "vendorOui": "00:05:1e",
                                "extIdentifier": "null",
                                "digitalDiagnostics":
                    {"temperature": "27",
                        "voltage": "3340.600",
                        "rxPower": "-23.372",
                        "txPower": "-40.000",
                        "current": "0.002"
                     },
                    "serialNumber": "HAA115466085Z32",
                    "identifier": "SFP",
                    "connector": "LC"}

sfp_connector_8 = {"portName": "2",
                   "vendorName": "HP-A     BROCADE",
                   "vendorPartNumber": "AJ716A",
                   "vendorRevision": "A",
                   "speed": "null",
                   "vendorOui": "00:05:1e",
                                "extIdentifier": "null",
                                "digitalDiagnostics":
                   {"temperature": "27",
                    "voltage": "3340.600",
                    "rxPower": "-23.372",
                    "txPower": "-40.000",
                    "current": "0.002"
                    },
                   "serialNumber": "UAA109151207762",
                   "identifier": "SFP",
                   "connector": "LC"}

unsupported_sfp = {"portName": "3",
                   "vendorName": "HP-A     BROCADE",
                   "vendorPartNumber": "AJ716A",
                   "vendorRevision": "A",
                   "speed": "null",
                   "vendorOui": "00:05:1e",
                                "extIdentifier": "null",
                                "digitalDiagnostics":
                   {"temperature": "27",
                    "voltage": "3340.600",
                    "rxPower": "-23.372",
                    "txPower": "-40.000",
                    "current": "0.002"
                    },
                   "serialNumber": "UAA109151207762",
                   "identifier": "SFP",
                   "connector": "LC"}

qsfp_connector = {
    "speed": "null",
    "vendorName": "BROCADE",
    "vendorPartNumber": "57-1000294-01",
    "vendorRevision": "A",
    "vendorOui": "00:05:1e",
    "extIdentifier": "null",
    "digitalDiagnostics": {
        "temperature": "26",
        "voltage": "3306.100",
        "rxPower": "-2.884",
        "txPower": "0",
        "current": "0.000"
    },
    "portName": "Q1:2",
    "identifier": "QSFP_PLUS",
    "serialNumber": "HUA21436000008P",
    "connector": "MPO_PARALLEL_OPTIC"
}


interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]

server_bay_3 = 3

# Server Profiles for HA redundancy
server_profiles = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 2',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'BFS_QLGC_LEGACY2', 'description': '', 'affinity': 'Bay',
     'bootMode': {"manageMode": True, "mode": "BIOS"},
     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
     'connectionSettings':{'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}},
                                           {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}},
                                           ]}}
]

server_profiles2 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'BFS_QLGC_LEGACY', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connectionSettings':{'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}},
                                                           {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Secondary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}},
                                                           ]}}]

server_profiles3 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'LUNS_ELX_LGCY', 'description': '', 'affinity': 'Bay',
                     'bootMode': {"manageMode": True, "mode": "BIOS"},
                     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                     'connectionSettings':{'connections': [{'id': 1, 'name': 'BAY1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:56", "wwnn": "20:00:00:90:fa:5d:34:56", "boot": {"priority": "NotBootable", "iscsi": {}}},
                                                           {'id': 2, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:57", "wwnn": "20:00:00:90:fa:5d:34:57", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}},
                                                           ]}}]

# Server Profiles for A Side redundancy

server_profiles_A_side = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 2',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG_Aside, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'BFS_QLGC_LEGACY2', 'description': '', 'affinity': 'Bay',
     'bootMode': {"manageMode": True, "mode": "BIOS"},
     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
     'connectionSettings':{'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:08", "wwnn": "20:00:9a:69:37:00:00:08", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:9a:69:37:00:00:08", "lun": "1"}], "iscsi": {}}}
                                           ]}}
]

server_profiles2_A_side = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG_Aside, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': 'BFS_QLGC_LEGACY', 'description': '', 'affinity': 'Bay',
                            'bootMode': {"manageMode": True, "mode": "BIOS"},
                            'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                            'connectionSettings':{'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:52", "wwnn": "20:00:00:90:fa:5d:34:52", "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:52", "lun": "0"}], "iscsi": {}}}
                                                                  ]}}]

server_profiles3_A_side = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 3',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG_Aside, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': 'LUNS_ELX_LGCY', 'description': '', 'affinity': 'Bay',
                            'bootMode': {"manageMode": True, "mode": "BIOS"},
                            'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                            'connectionSettings':{'connections': [{'id': 1, 'name': 'BAY1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:56", "wwnn": "20:00:00:90:fa:5d:34:56", "boot": {"priority": "NotBootable", "iscsi": {}}}
                                                                  ]}}]


# Server Profiles for B Side redundancy
server_profiles_B_side = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 2',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG_Bside, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'BFS_QLGC_LEGACY2', 'description': '', 'affinity': 'Bay',
     'bootMode': {"manageMode": True, "mode": "BIOS"},
     'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
     'connectionSettings':{'connections': [{'id': 1, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:9a:69:37:00:00:10", "wwnn": "20:00:9a:69:37:00:00:10", "ipv4": {}, "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "20:00:9a:69:37:00:00:10", "lun": "0"}], "iscsi": {}}}
                                           ]}}
]

server_profiles2_B_side = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 1',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG_Bside, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': 'BFS_QLGC_LEGACY', 'description': '', 'affinity': 'Bay',
                            'bootMode': {"manageMode": True, "mode": "BIOS"},
                            'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                            'connectionSettings':{'connections': [{'id': 1, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:53", "wwnn": "20:00:00:90:fa:5d:34:53", "ipv4": {}, "boot": {"priority": "Primary", "bootVolumeSource": "UserDefined", "targets": [{"arrayWwpn": "10:00:00:90:fa:5d:34:53", "lun": "0"}], "iscsi": {}}}
                                                                  ]}}]

server_profiles3_B_side = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 3',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG_Bside, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                            'name': 'LUNS_ELX_LGCY', 'description': '', 'affinity': 'Bay',
                            'bootMode': {"manageMode": True, "mode": "BIOS"},
                            'boot': {"manageBoot": True, "order": ["CD", "USB", "HardDisk"]},
                            'connectionSettings':{'connections': [{'id': 1, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2', "wwpnType": "UserDefined", "wwpn": "10:00:00:90:fa:5d:34:57", "wwnn": "20:00:00:90:fa:5d:34:57", "ipv4": {}, "boot": {"priority": "NotBootable", "iscsi": {}}}
                                                                  ]}}]


diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"

server_details = {'username': 'Administrator', 'password': 'password@123'}

linux_details = {"hostip": "15.186.25.25", "username": "root", "password": "password@123", "dir_location": "/root/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}
server_bay_3 = "3"

import os
import sys


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


def execute_windows_commands(ip, username, passwd, wcmd):
    '''
    Execute the diskSPD tool Command
    '''
    try:
        single_cmd = "C:\\PSTools\\PsExec \\\\" + ip + " -u " + username + " -p " + passwd + " " + \
                     wcmd
        print single_cmd
        output = os.system(single_cmd)
        return (output)
    except Exception as e:
        return (e)


def Change_Directory(dir):
    os.chdir(dir)


def get_matching_lines_with_number(string, pattern, case_insensitive=False):
    if case_insensitive:
        pattern = pattern.lower()
        contains = lambda line: pattern in line.lower()
    else:
        contains = lambda line: pattern in line
    print '*INFO* %s' % (string)
    print '*INFO* %s' % (pattern)
    print '*INFO* %s' % (contains)
    lines = string.splitlines()
    matching = [line for line in lines if contains(line)]
    print '*INFO* %d out of %d lines matched' % (len(matching), len(lines))
    return '\n'.join(matching), len(matching)


APPLIANCE_IP = '15.186.9.136'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
appliance_cred = ['root', 'hpvse1']
IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
Enclosure_Name = ['MXQ80503HJ', 'MXQ734024N']
enclosureCount = 2
ENC1 = 'MXQ80503HJ'
ENC2 = 'MXQ734024N'

IC_model_name = "Virtual Connect SE 32Gb FC Module for Synergy"
# values should be either 'Redundant' or 'NonRedundantASide' or 'NonRedundantBSide'
Enc_bay_type = {'enc1': 'Redundant', 'enc2': 'Redundant'}
FUSION_IP = APPLIANCE_IP
FUSION_SSH_USERNAME = "root"
FUSION_SSH_PASSWORD = "hpvse1"
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180
IC_SSH_USERNAME = "root"
IC_TIMEOUT = 100
IC_PROMPT = '>'
time = 300
V3_host = '15.186.21.149'
V3_user = 'root'
V3_pass = 'password'
trap = '\nTRAP..'

server_details = {'username': 'admin', 'password': 'hpvse@123'}
linux_details = {"hostip": "15.186.21.149", "username": "root", "password": "password", "dir_location": "/root/pexpect/pexpect-u-2.5.1/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '15.186.28.58', 'username': 'Administrator', 'password': 'hpvse123'}

diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"

status = ['Linked', 'Unlinked']
Action = ['EFuseOff', 'EFuseOn']
LI_dto = [{'name': 'LE-LIG1-1'}, {'name': 'LE-LIG2-2'}]
LIG = ['LIG1', 'LIG2']
uplinkset_names = ['UplinkSet_1', 'UplinkSet_2', 'UplinkSet_3', 'UplinkSet_4']
icmap_Redundant = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1},
                                                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                              {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantASide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

icmap_NonRedundantBSide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                                      {"type": "Enclosure", "relativeValue": -1}]}, "logicalDownlinkUri": None, "permittedInterconnectTypeUri": "", "enclosureIndex": -1}]}

LIG_body = {"type": "logical-interconnect-groupV5",
            "ethernetSettings": None,
            "name": "",
            "telemetryConfiguration": None,
            "interconnectMapTemplate": "",
            "uplinkSets": [],
            "enclosureType": "SY12000",
            "enclosureIndexes": [-1],
            "enclosureIndexes": [-1],
            "interconnectBaySet": IC_bay_set,
            "redundancyType": "",
            "internalNetworkUris": [],
            "snmpConfiguration": None,
            "qosConfiguration": None}
uplink_sets = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': '4', 'speed': 'Auto'}


                                                          ]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                          {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'}
                                                          ]},

               'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'}
                                                          ]},
               'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                          {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'}
                                                          ]},
               'UplinkSet_5': {'name': 'UplinkSet_5', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_5'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1:2', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1:3', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1:4', 'speed': 'Auto'}
                                                          ]},
               }

uplink_sets_pm = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                  'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}
                                                             ]},
                  'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                  'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}
                                                             ]},
                  'UplinkSet_3': {'name': 'UplinkSet_3', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_3'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                  'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'}

                                                             ]},
                  'UplinkSet_4': {'name': 'UplinkSet_4', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_4'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                  'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},

                                                             ]},

                  }
ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None
         },
        {'name': 'LIG2',
         'type': 'logical-interconnect-groupV400',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                     {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                     ],
         'enclosureIndexes': [-1],
         'interconnectBaySet': 1,
         'redundancyType': 'Redundant',
         'uplinkSets': [uplink_sets['UplinkSet_3'].copy(), uplink_sets['UplinkSet_4'].copy(), uplink_sets['UplinkSet_5'].copy()],
         'internalNetworkUris': [],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
                  'telemetryConfiguration': None,
                  'snmpConfiguration': None
         }]
ligs_pm = [{'name': 'LIG1',
            'type': 'logical-interconnect-groupV400',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                        ],
            'enclosureIndexes': [-1],
            'interconnectBaySet': 1,
            'redundancyType': 'Redundant',
            'uplinkSets': [uplink_sets_pm['UplinkSet_1'].copy(), uplink_sets_pm['UplinkSet_2'].copy()],
            'internalNetworkUris': [],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None
            },
           {'name': 'LIG2',
            'type': 'logical-interconnect-groupV400',
            'enclosureType': 'SY12000',
            'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                        {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                        ],
            'enclosureIndexes': [-1],
            'interconnectBaySet': 1,
            'redundancyType': 'Redundant',
            'uplinkSets': [uplink_sets_pm['UplinkSet_3'].copy(), uplink_sets_pm['UplinkSet_4'].copy()],
            'internalNetworkUris': [],
            'stackingMode': 'Enclosure',
            'ethernetSettings': None,
            'state': 'Active',
            'telemetryConfiguration': None,
            'snmpConfiguration': None
            }]

lig_telemetry = [{'name': 'LIG1',
                  'enclosureType': 'SY12000',
                  'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                              {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                              ],
                  'enclosureIndexes': [-1],
                  'interconnectBaySet': 1,
                  'redundancyType': 'Redundant',
                  'uplinkSets': [uplink_sets['UplinkSet_1'].copy(), uplink_sets['UplinkSet_2'].copy()],
                  'internalNetworkUris': [],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': {"type": "telemetry-configuration", "enableTelemetry": True, "sampleCount": 10, "sampleInterval": 6},
                  'snmpConfiguration': None
                  },
                 {'name': 'LIG2',
                  'enclosureType': 'SY12000',
                  'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                              {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                              ],
                  'enclosureIndexes': [-1],
                  'interconnectBaySet': 1,
                  'redundancyType': 'Redundant',
                  'uplinkSets': [uplink_sets['UplinkSet_3'].copy(), uplink_sets['UplinkSet_4'].copy()],
                  'internalNetworkUris': [],
                  'stackingMode': 'Enclosure',
                  'ethernetSettings': None,
                  'state': 'Active',
                  'telemetryConfiguration': {"type": "telemetry-configuration", "enableTelemetry": True, "sampleCount": 10, "sampleInterval": 6},
                  'snmpConfiguration': None
                  }]
interconnectBayMappings = [{"interconnectBay": IC_bay_set, "enclosureIndex": 1, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 1, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 2, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 2, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 3, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 3, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 4, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 4, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set, "enclosureIndex": 5, "logicalInterconnectGroupUri": ""},
                           {"interconnectBay": IC_bay_set_pair, "enclosureIndex": 5, "logicalInterconnectGroupUri": ""}]
EG_body = {"name": "",
           "interconnectBayMappings": interconnectBayMappings,
           "ipAddressingMode": "DHCP",
           "ipRangeUris": [],
                   "enclosureCount": enclosureCount}

les = [{'name': 'LE',
        'enclosureUris': [],
        'enclosureGroupUri': '',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]
EG = 'EG'
Fc_body = {"name": "",
           "connectionTemplateUri": None,
           "linkStabilityTime": "30",
           "autoLoginRedistribution": True,
           "fabricType": "",
           "type": "fc-networkV4"}


server_profiles = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:80', 'wwnn': '20:00:00:00:c9:71:7b:80'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:81', 'wwnn': '20:00:00:00:c9:71:7b:81'},
                                        ]}},
                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 12',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay12', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:36', 'wwnn': '20:00:00:00:c9:71:7b:36'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:37', 'wwnn': '20:00:00:00:c9:71:7b:37'},
                                        ]}},
                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 3',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC2 + '_Bay3', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:32', 'wwnn': '20:00:00:00:c9:71:7b:32'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:33', 'wwnn': '20:00:00:00:c9:71:7b:33'},
                                        ]}},
                   {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 5',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
                                                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                                 'name': ENC2 + '_Bay5', 'description': '', 'affinity': 'Bay',
                                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:34', 'wwnn': '20:00:00:00:c9:71:7b:34'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:35', 'wwnn': '20:00:00:00:c9:71:7b:35'},
                                        ]}},
                   ]

sp_pm = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG,
          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
          'name': ENC1 + '_Bay1', 'description': '', 'affinity': 'Bay',
          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
          'boot': {'manageBoot': True, 'order': ['HardDisk']},
          'connectionSettings': {
              'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                               'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                               'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:80', 'wwnn': '20:00:00:00:c9:71:7b:80'},
                              {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                               'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                               'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:81', 'wwnn': '20:00:00:00:c9:71:7b:81'},
                              ]}},
         {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 1',
          'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
          'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
          'name': ENC2 + '_Bay1', 'description': '', 'affinity': 'Bay',
          'bootMode': None, 'boot': None,
          'connectionSettings': {
              'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                               'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                               'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                              {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                               'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                               'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                              ]}}]
sp_snmp = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 1',
                    'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC1 + '_Bay1', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:80', 'wwnn': '20:00:00:00:c9:71:7b:80'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:81', 'wwnn': '20:00:00:00:c9:71:7b:81'},
                                        ]}},
           {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 3',
            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
            'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
            'name': ENC2 + '_Bay3', 'description': '', 'affinity': 'Bay',
            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
            'boot': {'manageBoot': True, 'order': ['HardDisk']},
            'connectionSettings': {
                'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                          'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                ]}}]

sp_telemetry = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC1 + ', bay 12',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:%s' % EG,
                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                 'name': ENC1 + '_Bay12', 'description': '', 'affinity': 'Bay',
                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                 'connectionSettings': {
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                      'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:36', 'wwnn': '20:00:00:00:c9:71:7b:36'},
                                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:37', 'wwnn': '20:00:00:00:c9:71:7b:37'},
                                     ]}},
                {'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 5',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                 'name': ENC2 + '_Bay5', 'description': '', 'affinity': 'Bay',
                                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_3',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:34', 'wwnn': '20:00:00:00:c9:71:7b:34'},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                         'requestedMbps': 'Auto', 'networkUri': 'FC:FC_4',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:35', 'wwnn': '20:00:00:00:c9:71:7b:35'},
                                        ]}}]
LI = ['LE-LIG1-1', 'LE-LIG2-2']
uplink_ports = ['1']
Interconnects_ENC1 = [ENC1 + ', interconnect 1', ENC1 + ', interconnect 4']
Interconnects_ENC2 = [ENC2 + ', interconnect 1', ENC2 + ', interconnect 4']
Interconnects_ENCS = [ENC1 + ', interconnect 1', ENC1 + ', interconnect 4', ENC2 + ', interconnect 1', ENC2 + ', interconnect 4']
Interconnects = [ENC1 + ', interconnect 1', ENC2 + ', interconnect 1']
Interconnects1 = [ENC1 + ', interconnect 4', ENC2 + ', interconnect 4']
Interconnect_ENCS = [ENC1 + ', interconnect 1', ENC1 + ', interconnect 4', ENC2 + ', interconnect 1', ENC2 + ', interconnect 4']
Interconnect_dto = [{'name': 'MXQ80503HJ, interconnect 1'}, {'name': 'MXQ734024N, interconnect 1'}]
Interconnect_dto1 = [{'name': 'MXQ80503HJ, interconnect 4'}, {'name': 'MXQ734024N, interconnect 4'}]
Interconnectdto_ENC1 = [{'name': 'MXQ80503HJ, interconnect 1'}, {'name': 'MXQ80503HJ, interconnect 4'}]
Interconnectdto_ENC2 = [{'name': 'MXQ734024N, interconnect 1'}, {'name': 'MXQ734024N, interconnect 4'}]
portno_for_statistics = ['1']
total_samples_10 = 9
total_samples_60 = 60
total_samples_24 = 23
exp_samples = 5
telemetry_LI = {"name": '', "type": "telemetry-configuration", "enableTelemetry": "true", "sampleCount": '60', "sampleInterval": 60}
telemetry_LIG = {"type": "telemetry-configuration", "enableTelemetry": "true", "sampleCount": '', "sampleInterval": 60}
Interconnect_bays = ['1', '4']
analyzer_port_bay1 = ['2', 'Q1:2']
analyzer_port_bay4 = "2"
analyzer_port_3_bay1 = ['3', 'Q1:3']
used_uplink_port = ['1', 'Q1:1']
used_uplink_port_bay4 = 1
analyzer_dport = "d1"
Alr_serverpoweron = [{'4.1': 1, '1.1': 1, '1.2': 1, '1.3': 0, '1.4': 0, '4.2': 1}, {'4.1': 1, '1.1': 1, '1.2': 1, '4.2': 1}]
Alr_serverpoweron1 = {'4.1': 1, '1.1': 1, '1.2': 1, '1.3': 0, '1.4': 0, '4.2': 1}
disable_ports = [{'4.1': 0, '1.1': 0, '1.2': 1, '1.3': 1, '1.4': 0, '4.2': 2}, {'4.1': 0, '1.1': 0, '1.2': 2, '4.2': 2}]
enable_ports = [{'4.1': 1, '1.1': 0, '1.2': 1, '1.3': 1, '1.4': 0, '4.2': 1}, {'4.1': 1, '1.1': 1, '1.2': 1, '4.2': 1}]
remove_ports = [{'4.1': 2, '1.1': 1, '1.2': 0, '1.3': 1, '1.4': 0, '4.2': 0}, {'4.1': 2, '1.1': 2, '1.2': 0, '4.2': 0}]
add_ports = [{'4.1': 1, '1.1': 1, '1.2': 0, '1.3': 1, '1.4': 0, '4.2': 1}, {'4.1': 1, '1.1': 1, '1.2': 1, '4.2': 1}]
valDict = {'status_code': 200}
valDict1 = {'status_code': 400, 'errorCode': "CRM_INVALID_LINK_STABILITY_TIME"}
fc_names = {'FC_1', 'FC_2', 'FC_3', 'FC_4'}
intervals = ['120']
snmp_config = 'snmp-configuration'
v1_trap_list = [{'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories':[], 'port':'162',
                 'trapDestination':'15.186.21.149', 'trapFormat': 'SNMPv1', 'trapSeverities':[], 'vcmTrapCategories':[]}]
inavlid_snmp_usernames = ['talent@123', '        ', 'Change$!#']
valid_snmp_username = ['snmpusernmae', '12345678', 'password123', 'change_1234', 'ABCDEFGH', 'AbCdEfGh']
valid_auth_username = ['snmpusernmae', '12345678', 'change_1234', 'AbCdEfGh']
invalid_auth_passwords = '       '
min_length_auth_password = 'hello'
max_length_username = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '']
invalid_trap_ip = '15.20.30'
li_usernames_edit = ['e136sysadminmd5', 'md5des_1', 'md5aes_1', 'sha_1_aes', 'sha_d_des', 'shA1', 'Md5_none']
engine_id = '0x80001F888071F26C0ED6B8E15800000000'
port_map = {
    '1': '25', '2': '26', '3': '27', '4': '28', '5': '29', '6': '30', '7': '31', '8': '0',
    'Q1:1': '32', 'Q1:2': '33', 'Q1:3': '34', 'Q1:4': '35',
    'Q2:1': '36', 'Q2:2': '37', 'Q2:3': '38', 'Q2:4': '39',
    'Q3:1': '40', 'Q3:2': '41', 'Q3:3': '42', 'Q3:4': '43',
    'Q4:1': '44', 'Q4:2': '45', 'Q4:3': '46', 'Q4:4': '47'}


users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator'}], 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator'}], 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator'}], 'fullName': 'Backupadmin', 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'readonly', 'permissions': [{'roleName': 'Read only'}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]
usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'},
            {'userName': 'readonly', 'password': 'readonly'}]


li_portmonitor = {"type": "port-monitor",
                  "enablePortMonitor": 'true',
                  "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                   "portUri": "UplinkportUri"},
                  "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredBoth",
                                      "portUri": "DownlinkportUri"}]
                  }

li_portmonitor_to_server = {"type": "port-monitor",
                            "enablePortMonitor": 'true',
                            "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                             "portUri": "UplinkportUri"},
                            "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredToServer",
                                                "portUri": "DownlinkportUri"}]
                            }

li_portmonitor_from_server = {"type": "port-monitor",
                              "enablePortMonitor": 'true',
                              "analyzerPort": {"portMonitorConfigInfo": "AnalyzerPort",
                                               "portUri": "UplinkportUri"},
                              "monitoredPorts": [{"portMonitorConfigInfo": "MonitoredFromServer",
                                                  "portUri": "DownlinkportUri"}]}

neg_uplink_sets = [{'name': 'UplinkSet_1',
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
                    'portConfigInfos': [{'bay': '1', 'port': '2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC1}
                                        ]},

                   {'name': 'UplinkSet_3',
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
                    'portConfigInfos': [{'bay': '1', 'port': '1:2', 'desiredSpeed': 'Speed8G', 'enclosure': ENC2}
                                        ]}
                   ]

delete_uplinkport = [{'name': 'UplinkSet_1',
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
                      'portConfigInfos': [{'bay': '1', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                          {'bay': '1', 'port': '3', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                          {'bay': '1', 'port': '4', 'desiredSpeed': 'Auto', 'enclosure': ENC1}
                                          ]},
                     {'name': 'UplinkSet_2',
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
                      'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1}
                                          ]},
                     {'name': 'UplinkSet_3',
                      'ethernetNetworkType': 'NotApplicable',
                      'networkType': 'FibreChannel',
                      'networkUris': [],
                      'fcNetworkUris': ['FC_3'],
                      'fcoeNetworkUris': [],
                      'lacpTimer': 'Short',
                      'logicalInterconnectUri': None,
                      'primaryPortLocation': None,
                      'manualLoginRedistributionState': 'Supported',
                      'connectionMode': 'Auto',
                      'nativeNetworkUri': None,
                      'portConfigInfos': [{'bay': '1', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC2}
                                          ]},
                     {'name': 'UplinkSet_4',
                      'ethernetNetworkType': 'NotApplicable',
                      'networkType': 'FibreChannel',
                      'networkUris': [],
                      'fcNetworkUris': ['FC_4'],
                      'fcoeNetworkUris': [],
                      'lacpTimer': 'Short',
                      'logicalInterconnectUri': None,
                      'primaryPortLocation': None,
                      'manualLoginRedistributionState': 'Supported',
                      'connectionMode': 'Auto',
                      'nativeNetworkUri': None,
                      'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC2}
                                          ]}]
add_uplinkport = [{'name': 'UplinkSet_1',
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
                   'portConfigInfos': [{'bay': '1', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                       {'bay': '1', 'port': '3', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                       {'bay': '1', 'port': '4', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                       {'bay': '1', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}
                                       ]},
                  {'name': 'UplinkSet_2',
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
                   'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC1},
                                       {'bay': '4', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC1}
                                       ]},
                  {'name': 'UplinkSet_3',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_3'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '1', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC2},
                                       {'bay': '1', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC2}
                                       ]},
                  {'name': 'UplinkSet_4',
                   'ethernetNetworkType': 'NotApplicable',
                   'networkType': 'FibreChannel',
                   'networkUris': [],
                   'fcNetworkUris': ['FC_4'],
                   'fcoeNetworkUris': [],
                   'lacpTimer': 'Short',
                   'logicalInterconnectUri': None,
                   'primaryPortLocation': None,
                   'manualLoginRedistributionState': 'Supported',
                   'connectionMode': 'Auto',
                   'nativeNetworkUri': None,
                   'portConfigInfos': [{'bay': '4', 'port': '1', 'desiredSpeed': 'Auto', 'enclosure': ENC2},
                                       {'bay': '4', 'port': '2', 'desiredSpeed': 'Auto', 'enclosure': ENC2}
                                       ]}]

bay_port_detail_0 = {}
for i in 'UplinkSet_1', 'UplinkSet_2':
    tlist = []
    for j in uplink_sets[i]['logicalPortConfigInfos']:
        tlist.append(int(j['port']))
        bay_port_detail_0[int(j['bay'])] = tlist

bay_port_detail_1 = {}
for i in 'UplinkSet_3', 'UplinkSet_4':
    tlist = []
    for j in uplink_sets[i]['logicalPortConfigInfos']:
        tlist.append(int(j['port']))
        bay_port_detail_1[int(j['bay'])] = tlist

ic_disable_body = [{"associatedUplinkSetUri": uplink_sets['UplinkSet_1']['name'], "interconnectName": "", "portType": "Uplink", "portId": "", "portHealthStatus": "Normal", "capability": ["Ethernet", "EnetFcoe", "FibreChannel"], "configPortTypes":["Ethernet"], "enabled":False, "portName":uplink_ports[0], "portStatus":"Linked", "type":"port"},
                   ]

FC_switch_ports = {'segment1': [8, 9, 10, 11], 'segment2': [16, 17], 'segment3': [27, 28], 'segment4': [32, 33], 'segment5': [1, 2, 3, 4], }
neg_ports = ['1', '2', 'Q2:3', 'Q2:4']
US_details = [{'bay': IC_bay_set, 'Act_ports': ['1', '2', '3', '4'], 'rel_ports':['13', '14', '15', '16'], 'name':'UplinkSet_1', 'ENC':'MXQ80503HJ'},
              {'bay': IC_bay_set_pair, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_2', 'ENC':'MXQ80503HJ'},
              {'bay': IC_bay_set, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_3', 'ENC':'MXQ734024N'},
              {'bay': IC_bay_set_pair, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_4', 'ENC':'MXQ734024N'},
              {'bay': IC_bay_set, 'Act_ports': ['Q1:1', 'Q1:2', 'Q1:3', 'Q1:4'], 'rel_ports':['21', '22', '23', '24'], 'name':'UplinkSet_5', 'ENC':'MXQ734024N'}]

US_details_li1 = [{'bay': IC_bay_set, 'Act_ports': ['1', '2', '3', '4'], 'rel_ports':['13', '14', '15', '16'], 'name':'UplinkSet_1', 'ENC':'MXQ80503HJ'},
                  {'bay': IC_bay_set, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_4', 'ENC':'MXQ734024N'},
                  ]
US_details2 = [{'bay': IC_bay_set, 'Act_ports': ['1', '2', '3', '4'], 'rel_ports':['13', '14', '15', '16'], 'name':'UplinkSet_1', 'ENC':'MXQ80503HJ'},
               {'bay': IC_bay_set_pair, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_2', 'ENC':'MXQ80503HJ'},
               {'bay': IC_bay_set, 'Act_ports': ['Q1:2', 'Q1:3', 'Q1:1', 'Q1:4'], 'rel_ports':['22', '23', '21', '24'], 'name':'UplinkSet_5', 'ENC':'MXQ734024N'},
               {'bay': IC_bay_set_pair, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_4', 'ENC':'MXQ734024N'}]

US_details2_1 = [{'bay': IC_bay_set, 'Act_ports': ['1', '2', '3', '4'], 'rel_ports':['13', '14', '15', '16'], 'name':'UplinkSet_1', 'ENC':'MXQ80503HJ'},
                 {'bay': IC_bay_set, 'Act_ports': ['Q1:2', 'Q1:3', 'Q1:1', 'Q1:4'], 'rel_ports':['22', '23', '21', '24'], 'name':'UplinkSet_5', 'ENC':'MXQ734024N'}
                 ]
US_details2_2 = [{'bay': IC_bay_set_pair, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_2', 'ENC': 'MXQ80503HJ'},
                 {'bay': IC_bay_set_pair, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'UplinkSet_4', 'ENC':'MXQ734024N'}
                 ]

no_trunk_message = 'No ports have Trunk Area enabled'
FC_switch_details = {'ip': '15.186.14.219', 'userName': 'admin', 'password': 'password'}
Trunk_Commands = ['porttrunkarea --show enabled', 'portdisable', 'porttrunkarea --disable', 'portcfgtrunkport', 'portenable', 'porttrunkarea --enable', 'portCfgPersistentEnable']

fcmodes = ['TRUNK', 'NONE']
enabled_status = ['True', 'False']
desiredSpeeds = ['Auto', 'Speed8G', 'Speed32G', 'Speed16G']
empty_list = []
logicalPortConfigInfos = [{"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}}]


portConfigInfos = [{"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}},
                   {"desiredSpeed": "", "location": {"locationEntries": [{"value": "", "type": "Port"}, {"value": "", "type": "Bay"}, {"value": "", "type": "Enclosure"}]}}]

li_upsbody = [{"type": "uplink-setV4",
               "name": "",
               "fcMode": "",
               "networkUris": [],
               "portConfigInfos":"",
               "networkType":"FibreChannel",
               "primaryPortLocation":None,
               "reachability":None,
               "manualLoginRedistributionState":"Supported",
               "logicalInterconnectUri":"",
               "connectionMode":"Auto",
               "fcoeNetworkUris":[],
               "fcNetworkUris":[]}]

lig_uls_body1 = {"networkUris": [],
                 "mode": "Auto",
                 "name": "",
                 "lacpTimer": "Short",
                 "primaryPort": None,
                 "logicalPortConfigInfos": "",
                 "networkType": "FibreChannel",
                 "ethernetNetworkType": None,
                 "nativeNetworkUri": None,
                 }
disable_uplink = {"associatedUplinkSetUri": '',
                  "interconnectName": '',
                  "portType": "Uplink",
                  "portId": "",
                  "portHealthStatus": "Normal",
                  "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
                  "configPortTypes": ["EnetFcoe", "Ethernet"],
                  "enabled": False,
                  "portName": '',
                  "portStatus": "Linked",
                  "type": "port"}

alternate_trap_ip = '15.186.232.29'

v1_trap = {'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories': [], 'port': '162',
           'trapDestination': '15.186.21.149', 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories': []}
SNMPV3_LI_body_all_users = {'category': 'snmp-configuration',
                            'enabled': 'false',
                            'readCommunity': 'public',
                            'snmpAccess': [],
                            'snmpUsers': [{'snmpV3UserName': 'e136sysadminnone',
                                           'userCredentials': [],
                                           'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                          {'snmpV3UserName': 'e136sysadminshaaes',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e136sysadminmd5aes',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e136sysadminmd5des',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                          {'snmpV3UserName': 'e136sysadminshades',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                          {'snmpV3UserName': 'e136sysadminsha',
                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                            'trapDestinations': [{'communityString': '',
                                                  'enetTrapCategories': [],
                                                  'fcTrapCategories': [],
                                                  'inform': 'false',
                                                  'port': '162',
                                                  'trapDestination': '15.186.21.149',
                                                  'trapFormat': 'SNMPv3',
                                                  'trapSeverities': [],
                                                  'userName': 'e136sysadminnone',
                                                  'vcmTrapCategories': []}],
                            'type': 'snmp-configuration',
                            'uri': '',
                            'v3Enabled': 'true'}
SNMPV3_LI_body_sha_aes = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA',
                                         'v3PrivacyProtocol': 'AES128'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.21.149',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminshaaes',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

SNMPV3_LI_body_7_users = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e20sysadminnone',
                                         'userCredentials': [],
                                         'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                        {'snmpV3UserName': 'e20sysadminshaaes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e20sysadminmd5aes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                        'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e20sysadminmd5des',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                        'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e20sysadminshades',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                        {'snmpV3UserName': 'e20sysadminsha',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                        {'snmpV3UserName': 'e20sysadminmd5',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.21.149',
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5des',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

SNMPV3_LI_body_invalid_trap_user = {'category': 'snmp-configuration',
                                    'enabled': 'false',
                                    'readCommunity': 'public',
                                    'snmpAccess': [],
                                    'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                                   'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                       {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                   'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [{'communityString': '',
                                                          'enetTrapCategories': [],
                                                          'fcTrapCategories': [],
                                                          'inform': 'false',
                                                          'port': '162',
                                                          'trapDestination': '15.186.29.238',
                                                          'trapFormat': 'SNMPv3',
                                                          'trapSeverities': [],
                                                          'userName': 'e20sysadminmd5',
                                                          'vcmTrapCategories': []}],
                                    'type': 'snmp-configuration',
                                    'uri': '',
                                    'v3Enabled': 'true'}

SNMPV3_LI_body_6_trap = {'category': 'snmp-configuration',
                         'enabled': 'false',
                         'readCommunity': 'public',
                         'snmpAccess': [],
                         'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                        'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                             'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                            {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                             'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                        'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                         'trapDestinations': [{'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.1',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e136sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.2',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e136sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.3',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e136sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.4',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e136sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.5',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e136sysadminshaaes',
                                               'vcmTrapCategories': []},
                                              {'communityString': '',
                                               'enetTrapCategories': [],
                                               'fcTrapCategories': [],
                                               'inform': 'false',
                                               'port': '162',
                                               'trapDestination': '15.186.13.6',
                                               'trapFormat': 'SNMPv3',
                                               'trapSeverities': [],
                                               'userName': 'e136sysadminshaaes',
                                               'vcmTrapCategories': []}],
                         'type': 'snmp-configuration',
                         'uri': '',
                         'v3Enabled': 'true'}

snmpv3_li_body_6_users_7_traps = {'category': 'snmp-configuration',
                                  'enabled': 'false',
                                  'readCommunity': 'public',
                                  'snmpAccess': [],
                                  'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e136sysadminmd5aes',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e136sysadminmd5des',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e136sysadminshades',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e136sysadminsha',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                {'snmpV3UserName': 'e136sysadminmd5',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                  'trapDestinations': [{'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.1',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminshaaes',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.2',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminshades',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.3',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminmd5aes',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.4',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminmd5des',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.5',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminsha',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.6',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminmd5',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.6',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminshaaes',
                                                        'vcmTrapCategories': []}],
                                  'type': 'snmp-configuration',
                                  'uri': '',
                                  'v3Enabled': 'true'}

snmpv1_li_body_6_traps = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.1',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminshaaes',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.2',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminshades',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.3',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5aes',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.4',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5des',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.5',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminsha',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.6',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}


snmpv3_li_body_duplicate_user = {'category': 'snmp-configuration',
                                 'enabled': 'false',
                                 'readCommunity': 'public',
                                 'snmpAccess': [],
                                 'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                                'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                    {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                               {'snmpV3UserName': 'e136sysadminshaaes',
                                                'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                 'trapDestinations': [],
                                 'type': 'snmp-configuration',
                                 'uri': '',
                                 'v3Enabled': 'true'}

SNMPV3_LI_body_sha_inform = {'category': 'snmp-configuration',
                             'enabled': 'false',
                             'readCommunity': 'public',
                             'snmpAccess': [],
                             'snmpUsers': [{'snmpV3UserName': 'e136sysadminsha',
                                            'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                            'v3AuthProtocol': 'SHA',
                                            'v3PrivacyProtocol': 'NA'}],
                             'trapDestinations': [{'communityString': '',
                                                   'enetTrapCategories': [],
                                                   'fcTrapCategories': [],
                                                   'inform': 'true',
                                                   'engineId': '0x80001F888071F26C0ED6B8E15800000000',
                                                   'port': '162',
                                                   'trapDestination': '15.186.21.149',
                                                   'trapFormat': 'SNMPv3',
                                                   'trapSeverities': [],
                                                   'userName': 'e136sysadminsha',
                                                   'vcmTrapCategories': []}],
                             'type': 'snmp-configuration',
                             'uri': '',
                             'v3Enabled': 'true'}

SNMPV3_LI_body_sha_inform_duplicate = {'category': 'snmp-configuration',
                                       'enabled': 'false',
                                       'readCommunity': 'public',
                                       'snmpAccess': [],
                                       'snmpUsers': [{'snmpV3UserName': 'e136sysadmintratorsha',
                                                      'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                           'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                      'v3AuthProtocol': 'SHA',
                                                      'v3PrivacyProtocol': 'NA'}],
                                       'trapDestinations': [{'communityString': '',
                                                             'enetTrapCategories': [],
                                                             'fcTrapCategories': [],
                                                             'inform': 'true',
                                                             'engineId': '0x80001F888071F26C0ED6B8E15800000000',
                                                             'port': '162',
                                                             'trapDestination': '15.186.21.149',
                                                             'trapFormat': 'SNMPv3',
                                                             'trapSeverities': [],
                                                             'userName': 'e136sysadmintratorsha',
                                                             'vcmTrapCategories': []}],
                                       'type': 'snmp-configuration',
                                       'uri': '',
                                       'v3Enabled': 'true'}

SNMPV3_LI_body_sha_aes_duplicate = {'category': 'snmp-configuration',
                                    'enabled': 'false',
                                    'readCommunity': 'public',
                                    'snmpAccess': [],
                                    'snmpUsers': [{'snmpV3UserName': 'e20sysadminshaaes',
                                                   'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                        'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive',
                                                                        'valueType': 'String'},
                                                                       {'propertyName': 'SnmpV3PrivacyPassword',
                                                                        'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive',
                                                                        'valueType': 'String'}],
                                                   'v3AuthProtocol': 'SHA',
                                                   'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [],
                                    'type': 'snmp-configuration',
                                    'uri': '',
                                    'v3Enabled': 'true'}
LIG1 = 'LIG1'
LI2 = 'LE-LIG2-2'
LE1 = 'LE'
ICM_MODEL = 'Virtual Connect SE 32Gb FC Module for Synergy'
TRAPDESTINATION = "15.186.21.149"
Interconnect_dto_1IC = {"name": Interconnects_ENC2[0]}
LIG_ME = ['LIG1', 'LIG2']
le_body = {'name': 'LE',
           'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2],
           'enclosureGroupUri': 'EG:' + EG,
           'firmwareBaselineUri': None,
           'forceInstallFirmware': False
           }
fcmode = 'NONE'
uplinkset = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                             'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'},
                                                        {'bay': '1', 'enclosure': '-1', 'port': 'Q1:1', 'speed': 'Auto'},
                                                        {'bay': '1', 'enclosure': '-1', 'port': 'Q1:2', 'speed': 'Auto'},
                                                        {'bay': '1', 'enclosure': '-1', 'port': 'Q1:3', 'speed': 'Auto'},
                                                        {'bay': '1', 'enclosure': '-1', 'port': 'Q1:4', 'speed': 'Auto'}]},
             'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                             'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '6', 'speed': 'Auto'},
                                                        {'bay': '4', 'enclosure': '-1', 'port': '7', 'speed': 'Auto'},
                                                        {'bay': '4', 'enclosure': '-1', 'port': '8', 'speed': 'Auto'},
                                                        {'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}]}
             }
uplinkset1port = {'UplinkSet_1': {'name': 'UplinkSet_1', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_1'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                                  'logicalPortConfigInfos': [{'bay': '1', 'enclosure': '-1', 'port': '1', 'speed': 'Auto'}, ]}}
lig_1port = {'name': 'LIG2',
             'type': 'logical-interconnect-groupV400',
             'enclosureType': 'SY12000',
             'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                         {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                         ],
             'enclosureIndexes': [-1],
             'interconnectBaySet': 1,
             'redundancyType': 'Redundant',
             'uplinkSets': [uplinkset1port['UplinkSet_1'].copy()],
             'internalNetworkUris': [],
             'stackingMode': 'Enclosure',
             'ethernetSettings': None,
             'state': 'Active',
             'telemetryConfiguration': None,
             'snmpConfiguration': None
             }
lig_set = {'name': 'LIG2',
           'type': 'logical-interconnect-groupV400',
           'enclosureType': 'SY12000',
           'interconnectMapTemplate': [{'bay': 1, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1},
                                       {'bay': 4, 'enclosure': -1, 'type': 'Virtual Connect SE 32Gb FC Module for Synergy', 'enclosureIndex': -1}
                                       ],
           'enclosureIndexes': [-1],
           'interconnectBaySet': 1,
           'redundancyType': 'Redundant',
           'uplinkSets': [uplinkset['UplinkSet_1'].copy(), uplinkset['UplinkSet_2'].copy()],
           'internalNetworkUris': [],
           'stackingMode': 'Enclosure',
           'ethernetSettings': None,
           'state': 'Active',
           'telemetryConfiguration': None,
           'snmpConfiguration': None
           }
# Digital Diagnostics
sfp_connector_32 = {"portName": "1",
                                "vendorName": "HPE-F    BROCADE",
                                "vendorPartNumber": "P9H32A",
                                "vendorRevision": "A",
                                "speed": "null",
                                "vendorOui": "00:05:1e",
                                "extIdentifier": "null",
                                "digitalDiagnostics":
                    {"temperature": "40",
                        "voltage": " 3350.600",
                        "laneInformation": [{"laneId": "1", "txPowermW": "0.6377", "txPowerdBm": "-1.9540", "rxPowermW": "1.0000", "rxPowerdBm": "0.0000", "current": "6.496"}]
                     },
                    "serialNumber": "JAF3171600000M9",
                    "identifier": "SFP",
                    "connector": "LC"}

sfp_connector_16 = {"portName": "1",
                                "vendorName": "HP-A     BROCADE",
                                "vendorPartNumber": "QK724A",
                                "vendorRevision": "A",
                                "speed": "null",
                                "vendorOui": "00:05:1e",
                                "extIdentifier": "null",
                                "digitalDiagnostics":
                    {"temperature": "36",
                        "voltage": "  3293.500",
                        "laneInformation": [{"laneId": "1", "txPowermW": "0.5882", "txPowerdBm": "-2.3050", "rxPowermW": "0.4845", "rxPowerdBm": "-3.1470", "current": "7.426"}]
                     },
                    "serialNumber": "HAA114146001W35",
                    "identifier": "SFP",
                    "connector": "LC"}

sfp_connector_8 = {"portName": "6",
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

unsupported_sfp = {"portName": "6",
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
unsupported_sfp_ports = [{"portName": "6"}, {"portName": "7"}, {"portName": "8"}]

qsfp_connector1 = {
    "identifier": "QSFP_28",
    "extIdentifier": "null",
    "connector": "MPO_PARALLEL_OPTIC",
    "vendorName": "BROCADE",
    "vendorOui": "00:05:1e",
    "vendorPartNumber": "57-1000351-01",
    "vendorRevision": "A",
    "portName": "Q1:1",
    "speed": "null",
    "serialNumber": "ZUA11717000002T",
    "digitalDiagnostics": {
        "temperature": "28",
        "voltage": "3312.900",
        "laneInformation": [
            {
                "laneId": "1",
                "txPowermW": "unsupported",
                "txPowerdBm": "unsupported",
                "rxPowermW": "0.7558",
                "rxPowerdBm": "-1.2160",
                "current": "6.370"
            }], }}

qsfp_connector2 = {
    "identifier": "QSFP_28",
    "extIdentifier": "null",
    "connector": "MPO_PARALLEL_OPTIC",
    "vendorName": "BROCADE",
    "vendorOui": "00:05:1e",
    "vendorPartNumber": "57-1000351-01",
    "vendorRevision": "A",
    "portName": "Q1:2",
    "speed": "null",
    "serialNumber": "ZUA11717000002T",
    "digitalDiagnostics": {
        "temperature": "28",
        "voltage": "3312.900",
        "laneInformation": [
            {
                "laneId": "1",
                "txPowermW": "unsupported",
                "txPowerdBm": "unsupported",
                "rxPowermW": "0.8730",
                "rxPowerdBm": "-0.5900",
                "current": "6.486"
            }], }}

qsfp_connector3 = {
    "identifier": "QSFP_28",
    "extIdentifier": "null",
    "connector": "MPO_PARALLEL_OPTIC",
    "vendorName": "BROCADE",
    "vendorOui": "00:05:1e",
    "vendorPartNumber": "57-1000351-01",
    "vendorRevision": "A",
    "portName": "Q1:3",
    "speed": "null",
    "serialNumber": "ZUA11717000002T",
    "digitalDiagnostics": {
        "temperature": "28",
        "voltage": "3314.900",
        "laneInformation": [
            {
                "laneId": "1",
                "txPowermW": "unsupported",
                "txPowerdBm": "unsupported",
                "rxPowermW": "0.8266",
                "rxPowerdBm": "-0.8270",
                "current": "6.286"
            }], }}

qsfp_connector4 = {
    "identifier": "QSFP_28",
    "extIdentifier": "null",
    "connector": "MPO_PARALLEL_OPTIC",
    "vendorName": "BROCADE",
    "vendorOui": "00:05:1e",
    "vendorPartNumber": "57-1000351-01",
    "vendorRevision": "A",
    "portName": "Q1:4",
    "speed": "null",
    "serialNumber": "ZUA11717000002T",
    "digitalDiagnostics": {
        "temperature": "28",
        "voltage": "3311.000",
        "laneInformation": [
            {
                "laneId": "1",
                "txPowermW": "unsupported",
                "txPowerdBm": "unsupported",
                "rxPowermW": "0.8904",
                "rxPowerdBm": "-0.5040",
                "current": "6.654"}]}}
# SNMPV3 #
SNMP_IP = '15.186.21.149'
V3_user = 'root'
V3_pass = 'password'
Supported_port = "d1"
SNMPV3_LI_body_md5_des = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e136sysadminmd5des',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA',
                                         'v3PrivacyProtocol': 'DES56'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': TRAPDESTINATION,
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5des',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'True'}
v1_trap = {'communityString': 'public', 'enetTrapCategories': [], 'fcTrapCategories': [], 'port': '162',
           'trapDestination': TRAPDESTINATION, 'trapFormat': 'SNMPv1', 'trapSeverities': [], 'vcmTrapCategories': []}
alternate_trap_ip = '15.186.29.238'
File_Names = ['writeMECanmic.sh', 'readMECanmic.sh']
snmpv1_trap_split = 'Community'
Users_details = 'Trap/Inform'
user_left = '\\n'
split_trap = 'Trap Entry'
trap_ip1 = '15.186.21.149'
temp_engine_id = '00:00:00:00:00:00:00:00:00'
match = '\\n\\nSNMPv3 \']'
name = [' ', '1 (rw): ', '2 (rw): ', '3 (rw): ', '4 (ro): ', '5 (ro): ', '6 (ro): ']
var = ''
trap_users_list = ['e136sysadminshaaes', 'e136sysadminsha', 'e136sysadminmd5aes', 'e136sysadminnone']

SNMPV3_LI_body_sha_aes = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword',
                                                              'value': 'password',
                                                              'valueFormat': 'SecuritySensitive',
                                                              'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA',
                                         'v3PrivacyProtocol': 'AES128'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': TRAPDESTINATION,
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminshaaes',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}

SNMPV3_LI_body_sha_inform = {'category': 'snmp-configuration',
                             'enabled': 'false',
                             'readCommunity': 'public',
                             'snmpAccess': [],
                             'snmpUsers': [{'snmpV3UserName': 'e136sysadminsha',
                                            'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                 'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                            'v3AuthProtocol': 'SHA',
                                            'v3PrivacyProtocol': 'NA'}],
                             'trapDestinations': [{'communityString': '',
                                                   'enetTrapCategories': [],
                                                   'fcTrapCategories': [],
                                                   'inform': 'true',
                                                   'engineId': '0x80001F888071F26C0ED6B8E15800000000',
                                                   'port': '162',
                                                   'trapDestination': TRAPDESTINATION,
                                                   'trapFormat': 'SNMPv3',
                                                   'trapSeverities': [],
                                                   'userName': 'e136sysadminsha',
                                                   'vcmTrapCategories': []}],
                             'type': 'snmp-configuration',
                             'uri': '',
                             'v3Enabled': 'true'}
valid_trap_ip = ['15.186.13.8', '']
invalid_trap_ip = '15.20.30'
SNMPV3_LI_body_7_users = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [{'snmpV3UserName': 'e136sysadminnone',
                                         'userCredentials': [],
                                         'v3AuthProtocol': 'NA', 'v3PrivacyProtocol': 'NA'},
                                        {'snmpV3UserName': 'e136sysadminshaaes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e136sysadminmd5aes',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                        'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                        {'snmpV3UserName': 'e136sysadminmd5des',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                        {'snmpV3UserName': 'e136sysadminshades',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                             {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                        {'snmpV3UserName': 'e136sysadminsha',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                        {'snmpV3UserName': 'e136sysadminmd5',
                                         'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                              'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                         'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': TRAPDESTINATION,
                                                'trapFormat': 'SNMPv3',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5des',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}
SNMPV3_LI_body_invalid_trap_user = {'category': 'snmp-configuration',
                                    'enabled': 'false',
                                    'readCommunity': 'public',
                                    'snmpAccess': [],
                                    'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                                   'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                       {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                   'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'}],
                                    'trapDestinations': [{'communityString': '',
                                                          'enetTrapCategories': [],
                                                          'fcTrapCategories': [],
                                                          'inform': 'false',
                                                          'port': '162',
                                                          'trapDestination': '15.186.13.1',
                                                          'trapFormat': 'SNMPv3',
                                                          'trapSeverities': [],
                                                          'userName': 'e136sysadminmd5',
                                                          'vcmTrapCategories': []}],
                                    'type': 'snmp-configuration',
                                    'uri': '',
                                    'v3Enabled': 'true'}
snmpv3_li_body_6_users_7_traps = {'category': 'snmp-configuration',
                                  'enabled': 'false',
                                  'readCommunity': 'public',
                                  'snmpAccess': [],
                                  'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e136sysadminmd5aes',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                {'snmpV3UserName': 'e136sysadminmd5des',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                {'snmpV3UserName': 'e136sysadminshades',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                     {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                {'snmpV3UserName': 'e136sysadminsha',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                {'snmpV3UserName': 'e136sysadminmd5',
                                                 'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                      'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                 'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                  'trapDestinations': [{'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.1',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminshaaes',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.2',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminshades',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.3',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminmd5aes',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.4',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminmd5des',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.5',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminsha',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.6',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminmd5',
                                                        'vcmTrapCategories': []},
                                                       {'communityString': '',
                                                        'enetTrapCategories': [],
                                                        'fcTrapCategories': [],
                                                        'inform': 'false',
                                                        'port': '162',
                                                        'trapDestination': '15.186.13.6',
                                                        'trapFormat': 'SNMPv3',
                                                        'trapSeverities': [],
                                                        'userName': 'e136sysadminshaaes',
                                                        'vcmTrapCategories': []}],
                                  'type': 'snmp-configuration',
                                  'uri': '',
                                  'v3Enabled': 'true'}
snmpv1_li_body_6_traps = {'category': 'snmp-configuration',
                          'enabled': 'false',
                          'readCommunity': 'public',
                          'snmpAccess': [],
                          'snmpUsers': [],
                          'trapDestinations': [{'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.1',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminshaaes',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.2',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminshades',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.3',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5aes',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.4',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5des',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.5',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminsha',
                                                'vcmTrapCategories': []},
                                               {'communityString': '',
                                                'enetTrapCategories': [],
                                                'fcTrapCategories': [],
                                                'inform': 'false',
                                                'port': '162',
                                                'trapDestination': '15.186.13.6',
                                                'trapFormat': 'SNMPv1',
                                                'trapSeverities': [],
                                                'userName': 'e136sysadminmd5',
                                                'vcmTrapCategories': []}],
                          'type': 'snmp-configuration',
                          'uri': '',
                          'v3Enabled': 'true'}
snmpv1_li_body_6snmpv3traps_5snmpv1traps = {'category': 'snmp-configuration',
                                            'enabled': 'false',
                                            'readCommunity': 'public',
                                            'snmpAccess': [],
                                            'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                          {'snmpV3UserName': 'e136sysadminmd5aes',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                          'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                                          {'snmpV3UserName': 'e136sysadminmd5des',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                          {'snmpV3UserName': 'e136sysadminshades',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                               {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'DES56'},
                                                          {'snmpV3UserName': 'e136sysadminsha',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                           'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'},
                                                          {'snmpV3UserName': 'e136sysadminmd5',
                                                           'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                                'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                          'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                            'trapDestinations': [{'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.2',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminshades',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.3',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminmd5aes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.4',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminmd5des',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.5',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminsha',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.6',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminmd5',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.7',
                                                                  'trapFormat': 'SNMPv3',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminshaaes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.1',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminshaaes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.2',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminshades',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.3',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminmd5aes',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.4',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminmd5des',
                                                                  'vcmTrapCategories': []},
                                                                 {'communityString': '',
                                                                  'enetTrapCategories': [],
                                                                  'fcTrapCategories': [],
                                                                  'inform': 'false',
                                                                  'port': '162',
                                                                  'trapDestination': '15.186.13.5',
                                                                  'trapFormat': 'SNMPv1',
                                                                  'trapSeverities': [],
                                                                  'userName': 'e136sysadminsha',
                                                                  'vcmTrapCategories': []},
                                                                 ],
                                            'type': 'snmp-configuration',
                                            'uri': '',
                                            'v3Enabled': 'true'}
snmpv3_li_body_duplicate_user = {'category': 'snmp-configuration',
                                 'enabled': 'false',
                                 'readCommunity': 'public',
                                 'snmpAccess': [],
                                 'snmpUsers': [{'snmpV3UserName': 'e136sysadminshaaes',
                                                'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                                                                    {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'AES128'},
                                               {'snmpV3UserName': 'e136sysadminshaaes',
                                                'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'password',
                                                                     'valueFormat': 'SecuritySensitive', 'valueType': 'String'}],
                                                'v3AuthProtocol': 'SHA', 'v3PrivacyProtocol': 'NA'}],
                                 'trapDestinations': [],
                                 'type': 'snmp-configuration',
                                 'uri': '',
                                 'v3Enabled': 'true'}
SNMPV3_LI_body_md5_des_duplicate = {'category': 'snmp-configuration',
                                    'enabled': 'false',
                                    'readCommunity': 'public',
                                    'snmpAccess': [],
                                    'snmpUsers': [{'snmpV3UserName': 'e136sysadminmd5des',
                                                   'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                                        'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive',
                                                                        'valueType': 'String'},
                                                                       {'propertyName': 'SnmpV3PrivacyPassword',
                                                                        'value': 'password',
                                                                        'valueFormat': 'SecuritySensitive',
                                                                        'valueType': 'String'}],
                                                   'v3AuthProtocol': 'SHA',
                                                   'v3PrivacyProtocol': 'DES56'}],
                                    'trapDestinations': [],
                                    'type': 'snmp-configuration',
                                    'uri': '',
                                    'v3Enabled': 'true'}
SNMPV3_LI_body_md5 = {'category': 'snmp-configuration',
                      'enabled': 'false',
                      'readCommunity': 'public',
                      'snmpAccess': [],
                      'snmpUsers': [{'snmpV3UserName': 'e20sysadminmd5',
                                     'userCredentials': [{'propertyName': 'SnmpV3AuthorizationPassword',
                                                          'value': 'password',
                                                          'valueFormat': 'SecuritySensitive',
                                                          'valueType': 'String'}],
                                     'v3AuthProtocol': 'SHA',
                                     'v3PrivacyProtocol': 'NA'}],
                      'trapDestinations': [{'communityString': '',
                                            'enetTrapCategories': [],
                                            'fcTrapCategories': [],
                                            'inform': 'false',
                                            'port': '162',
                                            'trapDestination': TRAPDESTINATION,
                                            'trapFormat': 'SNMPv3',
                                            'trapSeverities': [],
                                            'userName': 'e20sysadminmd5',
                                            'vcmTrapCategories': []}],
                      'type': 'snmp-configuration',
                      'uri': '',
                      'v3Enabled': 'true'}
invalid_userCredentials = [{'propertyName': 'SnmpV3AuthorizationPassword', 'value': 'HPEoneview',
                            'valueFormat': 'SecuritySensitive', 'valueType': 'String'},
                           {'propertyName': 'SnmpV3PrivacyPassword', 'value': 'HPEoneview',
                            'valueFormat': 'SecuritySensitive', 'valueType': 'String'}]
LI_consistent = 'CONSISTENT'
LI_Inconsistent = 'NOT_CONSISTENT'
IC_state = 'Configured'
port = '162'
invalid_snmp_usernames = ['talent@123', '        ', 'Change$!#', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '']
valid_snmp_username = ['snmpusernmae', '12345678', 'password123', 'change_1234', 'ABCDEFGH', 'AbCdEfG']
invalid_auth_passwords = ['       ', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'hello']
valid_auth_username = ['snmpusernmae', '12345678', 'change_1234', 'AbCdEfGh']
invalid_engine_id = '888071F26C0ED6B'
users_list = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'permissions': [{'roleName': 'Server administrator'}], 'fullName': 'Serveradmin', 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
              {'userName': 'Networkadmin', 'password': 'Networkadmin', 'permissions': [{'roleName': 'Network administrator'}], 'fullName': 'Networkadmin', 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
              {'userName': 'Backupadmin', 'password': 'Backupadmin', 'permissions': [{'roleName': 'Backup administrator'}], 'fullName': 'Backupadmin', 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
              {'userName': 'readonly', 'password': 'readonly', 'fullName': 'readonly', 'permissions': [{'roleName': 'Read only'}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
              ]
lig_duplicate_trap_ip = [{'communityString': '',
                          'enetTrapCategories': [],
                          'fcTrapCategories': [],
                          'inform': 'false',
                          'port': '162',
                          'trapDestination': '15.186.13.8',
                          'trapFormat': 'SNMPv3',
                          'trapSeverities': [],
                          'userName': 'e136sysadminmd5aes',
                          'vcmTrapCategories': []},
                         {'communityString': '',
                          'enetTrapCategories': [],
                          'fcTrapCategories': [],
                          'inform': 'false',
                          'port': '162',
                          'trapDestination': '15.186.13.8',
                          'trapFormat': 'SNMPv3',
                          'trapSeverities': [],
                          'userName': 'e136sysadminsha',
                          'vcmTrapCategories': []
                          }]
engine_id1 = '0x80000634B21000C4F57CE794E5'
user_exceeds_max_error = "CRM_SNMP_CONFIGURATION_USERS_EXCEEDS_MAX"
trap_dest_duplicate_error = "CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_DUPLICATE"
username_not_found = "CRM_SNMP_CONFIGURATION_USER_NAME_NOT_FOUND"
trap_destination_max_error = "CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_EXCEEDS_MAX"
duplicate_username_error = "CRM_SNMP_CONFIGURATION_DUPLICATE_USER_NAME"
username_invalid = "CRM_SNMP_CONFIGURATION_USER_NAME_INVALID"
Auth_pwd_invalid = "CRM_SNMP_CONFIGURATION_AUTH_PWD_INVALID"
Privacy_pwd_invalid = "CRM_SNMP_CONFIGURATION_PRIV_PWD_INVALID"
invalid_engine_id_msg = "CRM_SNMP_CONFIGURATION_INVALID_ENGINEID"
trap_dest_ip_invalid = "CRM_SNMP_CONFIGURATION_TRAP_DESTINATION_IP_INVALID"
Invalid_users_error = "ACTION_FORBIDDEN_BY_ROLE"
# Support dump
sdmp_body = [{"errorCode": "CI", "encrypt": True, "dump": "both"}]
enclsdump_body = [{"encrypt": True, "errorCode": "MyDump16", "excludeApplianceDump": False, "name": LE1}]
# syslog
snmp_host = '15.186.21.149'
snmp_user = 'root'
snmp_pass = 'password'
snmp_path = 'root/SNMP'
syslog_path = '/var/log'
snmp_file = 'vcmtrap.log'
syslog_file = 'messages'
remote_syslog_body = {
    "type": "RemoteSyslog",
    "sendTestLog": 'true',
    "remoteSyslogPort": "514",
    "remoteSyslogDestination": "15.186.21.149",
    "enabled": 'true'
}

remote_syslog_clear = {
    "type": "RemoteSyslog",
    "sendTestLog": 'false',
    "remoteSyslogPort": "",
    "remoteSyslogDestination": "",
    "enabled": 'false'
}
reste = 'configuration was reset'
# The port added in uplinkset iplinkset1port to be given for uplink port and server to which profile is applied to be given for downlink port
Linked_ports = [{"portName": "1", "portType": "Uplink"}, {"portName": "d1", "portType": "Downlink"}]
Linkup_Message = 'persistently enabled.'
Linkdown_Message = 'persistently disabled'
Reload_message = 'VirtualConnect, System is about to reload.'
ON_Message = 'IPv4 DHCP ICIP/19 DHCP On'
Power_message = 'VirtualConnect, Added account OneView with admin authorization'
server_profile = [{'type': 'ServerProfileV9', 'serverHardwareUri': ENC2 + ', bay 1',
                   'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC2, 'enclosureGroupUri': 'EG:%s' % EG,
                   'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                   'name': ENC2 + '_Bay1', 'description': '', 'affinity': 'Bay',
                   'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                   'boot': {'manageBoot': True, 'order': ['HardDisk']},
                   'connectionSettings': {
                       'connections': [{'id': 1, 'name': '1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                        'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1',
                                        'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '10:00:00:00:c9:71:7b:30', 'wwnn': '20:00:00:00:c9:71:7b:30'},
                                       ]}}]
# DownLinkdown_Message = 'Network Adapter Link Down'
# DownLinkup_Message = 'Network Adapter Link Up'
# Match_message = 'ICM [ALERT] CFA'
# Test_messsage = '_HPOneViewAdmin'
Test_messsage = 'OneView: Remote syslog test message'
# Management_IP = 'fe80::be2f:8a18:2e06:8b9e'
Management_IP = '15.186.10.136'
rsyserror = 'Validation failed. Please check the remoteSyslogDestination and remoteSyslogPort.'

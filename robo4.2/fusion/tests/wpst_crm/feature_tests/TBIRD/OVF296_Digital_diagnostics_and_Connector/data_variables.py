"""Data Variable"""


def make_range_list(start, end, prefix='net_', suffix=''):
    """Function Definition"""
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'

APPLIANCE_IP = "15.186.9.20"

appliance_cred = ['root', 'hpvse1']

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator', 'Backup administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}]


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
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1.2', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1.3', 'speed': 'Auto'},
                                                          {'bay': '1', 'enclosure': '-1', 'port': 'Q1.4', 'speed': 'Auto'}]},
               'UplinkSet_2': {'name': 'UplinkSet_2', 'networkType': 'FibreChannel', 'ethernetNetworkType': None, 'networkUris': ['FC_2'], 'mode': 'Auto', 'lacpTimer': 'Short', 'primaryPort': None,
                               'logicalPortConfigInfos': [{'bay': '4', 'enclosure': '-1', 'port': '1', 'speed': 'Speed16G'},
                                                          {'bay': '4', 'enclosure': '-1', 'port': '2', 'speed': 'Auto'},
                                                          {'bay': '4', 'enclosure': '-1', 'port': '3', 'speed': 'Auto'}]}
               }

Lig_name = 'LIG1'
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
         }
        }
EG = 'EG1'
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
               }
              }

ENC1 = 'CN750160YS'
les = {'le1':
       {'name': 'LE_1',
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': 'EG:' + EG,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }
       }

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
                    "serialNumber": "HAA115456082YM2",
                    "identifier": "SFP",
                    "connector": "LC"}

sfp_connector_8 = {"portName": "2",
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
                   "serialNumber": "HAA115456082YM2",
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

qsfp_connector1 = {
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
    "portName": "Q1:1",
    "identifier": "QSFP_PLUS",
    "serialNumber": "HUA21436000008P",
                    "connector": "MPO_PARALLEL_OPTIC"
}

qsfp_connector2 = {
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
qsfp_connector3 = {
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
    "portName": "Q1:3",
    "identifier": "QSFP_PLUS",
    "serialNumber": "HUA21436000008P",
                    "connector": "MPO_PARALLEL_OPTIC"
}

qsfp_connector4 = {
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
    "portName": "Q1:4",
    "identifier": "QSFP_PLUS",
    "serialNumber": "HUA21436000008P",
                    "connector": "MPO_PARALLEL_OPTIC"
}

INTERCONNECTS = ['CN750160YS, interconnect 1', 'CN750160YS, interconnect 4']

interconnect_poweroff = [{"op": "replace", "path": "/powerState", "value": "Off"}]
interconnect_poweron = [{"op": "replace", "path": "/powerState", "value": "On"}]

server_bay_3 = 3
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

server_profiles1 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 2',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': 'BFS_QLGC_LEGACY', 'description': '', 'affinity': 'Bay',
                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                     'boot': {'manageBoot': True, 'order': ['HardDisk']},
                     'connectionSettings':{'connections': [{'id': 1, 'name': 'Downlink_1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:BAY1'},
                                                           {'id': 2, 'name': 'Downlink_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:BAY4'},
                                                           ]}},
                    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC1 + ', bay 3',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:' + EG, 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                     'name': "LUNS_ELX_LGCY", 'description': 'Server using Carbon', 'affinity': 'Bay',
                     'boot': {'manageBoot': False},
                     'bootMode': None,
                     'connectionSettings': {'connections': [{'id': 1, 'name': 'BAY1', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1'},
                                                            {'id': 2, 'name': 'BAY4', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': '16000', 'networkUri': 'FC:FC_2'}
                                                            ]}}]

diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\test-60s.ps1"

server_details = {'username': 'Administrator', 'password': 'password@123'}

linux_details = {"hostip": "15.186.25.25", "username": "root", "password": "password@123", "dir_location": "/root/",
                 "python_cmd": "python2.7"}

ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}

# server with Luns configured to run the IO traffic
server_bay_3 = "3"

power_value = ['Off', 'On']
edit_power_body = [{'op': 'replace',
                    'path': '/powerState',
                    'value': ''}]

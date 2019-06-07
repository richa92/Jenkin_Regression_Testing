from copy import deepcopy


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

serveradmin_credentials = {'userName': 'Serveradmin', 'password': 'Serveradmin'}

network_admin = {'userName': 'Networkadmin', 'password': 'Networkadmin'}

backup_admin = {'userName': 'Backupadmin', 'password': 'Backupadmin'}

readonly_user = {'userName': 'readonly', 'password': 'readonly'}

vcenter = {'server': '15.199.230.130', 'user': 'GopalK', 'password': 'hpvse1'}

frame = 3
IBS = 3
ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZH'
ENC3 = 'MXQ81804ZG'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4, 'ENC:' + ENC5]
LIG1 = 'LIG1'
EG = 'EG'
LE = 'LE'
LI = {'name': 'LE-LIG1'}

usercred = [{'userName': 'Networkadmin', 'password': 'Networkadmin'},
            {'userName': 'Serveradmin', 'password': 'Serveradmin'},
            {'userName': 'Storageadmin', 'password': 'Storageadmin'},
            {'userName': 'Backupadmin', 'password': 'Backupadmin'}]

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN 106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'portmon.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

users = [{"type": "UserAndPermissions", "userName": "Networkadmin", "fullName": "", "password": "Networkadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Network administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Storageadmin", "fullName": "", "password": "Storageadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Storage administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Backupadmin", "fullName": "", "password": "Backupadmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Backup administrator", "scopeUri": None}]},
         {"type": "UserAndPermissions", "userName": "Serveradmin", "fullName": "", "password": "Serveradmin",
          "emailAddress": "", "officePhone": "", "mobilePhone": "", "enabled": True, "permissions": [{"roleName": "Server administrator", "scopeUri": None}]},
         ]

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'], 'locale': 'en_US.UTF-8'}

fcoenets = [
    {
        "name": "fcoe-1002",
        "vlanId": "1002",
        "type": "fcoe-networkV4"
    }
]
uplink_sets = {'us1': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['fcoe-1002'],
                       'consistencyChecking': 'ExactMatch',
                       'mode': 'Auto',
                       'lacpTimer': 'Short',
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
                                                  ]},
               'us2': {'name': 'us2',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['fcoe-1002'],
                       'consistencyChecking': 'ExactMatch',
                       'mode': 'Auto',
                       'lacpTimer': 'Short',
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'}
                                                  ]},
               'us3': {'name': 'us3',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': [],
                       'consistencyChecking': 'ExactMatch',
                       'nativeNetworkUri': None,
                       'mode': 'Auto',
                       'lacpTimer': 'Short',
                       'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
                                                  ]},
               'us4': {'name': 'set1',
                       'ethernetNetworkType': 'Tagged',
                       'networkType': 'Ethernet',
                       'networkUris': ['fcoe-1002'],
                       'consistencyChecking': 'ExactMatch',
                       'mode': 'Auto',
                       'lacpTimer': 'Short',
                       'nativeNetworkUri': None,
                       'logicalPortConfigInfos': []}
               }

InterconnectMapTemplate1 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
]

InterconnectMapTemplate2 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
]

InterconnectMapTemplate3 = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
]

ligs = {'lig1':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': InterconnectMapTemplate3,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [deepcopy(uplink_sets['us2'])],
         'downlinkSpeedMode': 'SPEED_25GB'},
        'lig2':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': InterconnectMapTemplate3,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [deepcopy(uplink_sets['us3'])],
         'downlinkSpeedMode': 'SPEED_25GB'},
        'lig3':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': InterconnectMapTemplate3,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [deepcopy(uplink_sets['us1'])],
         'downlinkSpeedMode': 'SPEED_25GB'},
        'lig4':
        {'name': 'LIG1',
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': InterconnectMapTemplate3,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'HighlyAvailable',
         'uplinkSets': [deepcopy(uplink_sets['us4'])],
         'downlinkSpeedMode': 'SPEED_25GB'}
        }

enc_group = {
    'EG':
        {'name': 'EG',
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG1}],
         'ipAddressingMode': 'DHCP',
         'ipRangeUris': [],
         'powerMode': 'RedundantPowerFeed'
         }
}

Logical_Enclosure = {
    'LE':
    {'name': LE,
     'enclosureUris': ENC_List[0:frame],
     'enclosureGroupUri': 'EG:' + EG,
     'firmwareBaselineUri': None,
     'forceInstallFirmware': False}}

server_profiles = [{'type': 'ServerProfileV11',
                    'serverHardwareUri': ENC3 + ', bay 2',
                    'serverHardwareTypeUri': '',
                    'enclosureUri': 'ENC:' + ENC3,
                    'enclosureGroupUri': 'EG:EG',
                    'serialNumberType': 'Virtual',
                    'macType': 'Virtual',
                    'wwnType': 'Virtual',
                    'name': 'Profile1',
                    'description': '',
                    'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': False},
                    'connectionSettings': {'connections': [{'id': 1,
                                                            'name': '1',
                                                            'functionType': 'FibreChannel',
                                                            'portId': 'Mezz 3:1-b',
                                                            'requestedMbps': '2500',
                                                            'networkUri': 'FCOE:fcoe-1002',
                                                            'mac': '14:02:EC:D2:2F:FC',
                                                            'wwpn': '20:00:14:02:ec:d2:2f:fc',
                                                            'wwnn': '10:00:14:02:ec:d2:2f:fc'}]}}
                   ]

server_profiles_edit = [{'type': 'ServerProfileV11',
                         'serverHardwareUri': ENC3 + ', bay 2',
                         'serverHardwareTypeUri': '',
                         'enclosureUri': 'ENC:' + ENC3,
                         'enclosureGroupUri': 'EG:EG',
                         'serialNumberType': 'Virtual',
                         'macType': 'Virtual',
                         'wwnType': 'Virtual',
                         'name': 'Profile1',
                         'description': '',
                         'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                         'boot': {'manageBoot': False},
                         'connectionSettings': {'connections': []}}
                        ]

server_profiles_edit1 = [{'type': 'ServerProfileV11',
                          'serverHardwareUri': ENC3 + ', bay 2',
                          'serverHardwareTypeUri': '',
                          'enclosureUri': 'ENC:' + ENC3,
                          'enclosureGroupUri': 'EG:EG',
                          'serialNumberType': 'Virtual',
                          'macType': 'Virtual',
                          'wwnType': 'Virtual',
                          'name': 'Profile1',
                          'description': '',
                          'affinity': 'Bay',
                          'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                          'boot': {'manageBoot': False},
                          'connectionSettings': {'connections': [{'id': 1,
                                                                  'name': '1',
                                                                  'functionType': 'FibreChannel',
                                                                  'portId': 'Mezz 3:1-b',
                                                                  'requestedMbps': '2500',
                                                                  'networkUri': 'FCOE:fcoe-1002',
                                                                  'mac': 'e6:4c:e0:b0:00:01',
                                                                  'wwpn': '10:00:12:5c:24:60:00:00',
                                                                  'wwnn': '10:00:12:5c:24:60:00:01'}]}}]

interconnects = ['MXQ81804ZF, interconnect 3', 'MXQ81804ZH, interconnect 6']

dto = [{'name': 'MXQ81804ZF, interconnect 3'}, {'name': 'MXQ81804ZH, interconnect 6'}]

Interconnect_name = [ENC1 + ', ' + 'interconnect 3', ENC2 + ', ' + 'interconnect 6']

Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]

port_name = ['Q5', 'Q5']

IC_stacking_domain_role = ['Subordinate', 'Master']

ports = [{'uplink_port': 'Q5', 'downlink_port': 'd26'}]

uplink_ports = 'Q5'

downlink_ports = 'd26'

FIPsnooping_Parameters = {"fcfMacAddress": "ec:9b:8b:1e:a3:55", "fcID": "01:0b:01", "lagId": "2", "fcfName": "20:01:ec:9b:8b:1e:a3:4f", "fcoeMacAddress": "0e:fc:00:7d:08:01", "fcMap": "0e:fc:00"}

FIPsnooping_Parameters_uplink = {"fcfMacAddress": ["ec:9b:8b:1e:a3:55"], "fcID": [], "lagId": "2", "fcfName": "20:01:ec:9b:8b:1e:a3:4f", "fcoeMacAddress": [], "fcMap": "0e:fc:00"}

FIPsnooping_Parameters_downlink = {"fcfMacAddress": ["ec:9b:8b:1e:a3:55"], "lagId": "2", "fcfName": "20:01:ec:9b:8b:1e:a3:4f", "fcMap": None, "network": "fcoe-1002", "externalVlan": "1002", "fcoeLoginCount": "1", "port": "d26"}

Disable_Port = {"associatedUplinkSetUri": "us-Tagged", "interconnectName": ENC1 + ', ' + 'interconnect 3', "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["EnetFcoe", "Ethernet"], "enabled": False, "portName": "Q5", "portStatus": "Unknown", "type": "portV5"}

Enable_Port = {"associatedUplinkSetUri": "us-Tagged", "interconnectName": ENC1 + ', ' + 'interconnect 3', "portType": "Uplink", "portId": "", "capability": ["Ethernet", "EnetFcoe"], "configPortTypes": ["EnetFcoe", "Ethernet"], "enabled": True, "portName": "Q5", "portStatus": "Unknown", "type": "portV5"}

downlink_port_disable = {"associatedUplinkSetUri": "us-Tagged",
                         "interconnectName": "MXQ81804ZF, interconnect 3",
                         "portType": "Downlink",
                         "portId": "",
                         "portHealthStatus": "Normal",
                         "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
                         "configPortTypes": ["EnetFcoe", "Ethernet"],
                         "enabled": False,
                         "portName": "downlink_ports",
                         "portStatus": "Unknown",
                         "type": "portV5"}

downlink_port_enable = {"associatedUplinkSetUri": "us-Tagged",
                        "interconnectName": "MXQ81804ZF, interconnect 3",
                        "portType": "Downlink",
                        "portId": "",
                        "portHealthStatus": "Normal",
                        "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
                        "configPortTypes": ["EnetFcoe", "Ethernet"],
                        "enabled": True,
                        "portName": "downlink_ports",
                        "portStatus": "Unknown",
                        "type": "portV5"}

def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist


SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

vcenter = {'server': '15.199.230.130', 'user': 'rbriggs', 'password': 'hpvse1'}

appliance = {'type': 'ApplianceNetworkConfigurationV2',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'VLAN 106',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'DHCP',
                   'ipv6Type': 'UNCONFIGURE',
                   'hostname': 'minmax.usa.hp.com',
                   'confOneNode': True,
                   'domainName': 'usa.hp.com',
                   'aliasDisabled': True}]}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['192.173.0.23'],
                 'locale': 'en_US.UTF-8'}

users = [
    {'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin',
     'permissions': [{'roleName': 'Server administrator'}],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin',
     'permissions': [{'roleName': 'Network administrator'}], 'emailAddress': 'nat@hp.com',
     'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin',
     'permissions': [{'roleName': 'Backup administrator'}],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge',
     'permissions': [{'roleName': 'Read only'}],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': 'UserAndPermissions'}
]

licenses = [{
    'key': 'YCDE D9MA H9P9 8HUZ U7B5 HWW5 Y9JL KMPL MHND 7AJ9 DXAU 2CSM GHTG L762 LFH6 F4R4 KJVT D5KM EFVW DT5J 83HJ 8VC6 AK2P 3EW2 L9YE HUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207356 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR H3TCJHCGAYAY"'},
    {
        'key': 'QC3C A9MA H9PQ GHVZ U7B5 HWW5 Y9JL KMPL 2HVF 4FZ9 DXAU 2CSM GHTG L762 7JX5 V5FU KJVT D5KM EFVW DV5J 43LL PSS6 AK2P 3EW2 T9YE XUNJ TZZ7 MB5X 82Z5 WHEF GE4C LUE3 BKT8 WXDG NK6Y C4GA HZL4 XBE7 3VJ6 2MSU 4ZU9 9WGG CZU7 WE4X YN44 CH55 KZLG 2F4N A8RJ UKEG 3F9V JQY5 "423207566 HPOV-NFR2 HP_OneView_w/o_iLO_48_Seat_NFR 6H72JHCGY5AU"'}
]

ethernet_networks = [{'name': 'net_101',
                      'type': 'ethernet-networkV4',
                      'vlanId': 101,
                      'purpose': 'General',
                      'smartLink': True,
                      'privateNetwork': False,
                      'connectionTemplateUri': None,
                      'ethernetNetworkType': 'Tagged'}
                     ]

fcoe_networks = [{'name': 'fcoe_1002', 'type': 'fcoe-networkV4', 'vlanId': 1002}]

fc_networks = [{'type': 'fc-networkV4',
                'linkStabilityTime': 30,
                'autoLoginRedistribution': True,
                'name': 'SAN-A',
                'connectionTemplateUri': None,
                'managedSanUri': None,
                'fabricType': 'FabricAttach'}]

enc_groups = [{'name': 'EG',
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:LIG1'},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]}]

encs = [
    {'hostname': '192.173.0.20', 'username': 'Administrator', 'password': 'wpsthpvse1', 'enclosureGroupUri': 'EG:EG',
     'force': False, 'licensingIntent': 'OneViewNoiLO'}]

ligs = [{'name': 'LIG1',
         'type': 'logical-interconnect-groupV4',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
             {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
         ],
         'uplinkSets': [{'name': 'ETH-FCOE',
                         'ethernetNetworkType': 'Tagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['net_101', 'fcoe_1002'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
                        {'name': 'SAN-A',
                         'ethernetNetworkType': 'NotApplicable',
                         'networkType': 'FibreChannel',
                         'networkUris': ['SAN-A'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'},
                                                    {'bay': '1', 'port': 'X2', 'speed': 'Auto'}]}],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None}
        ]

ENC1 = 'WPST-PAAW63-EN1'

server_profiles = [
    {'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 1',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile1', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                      'requestedMbps': '2500', 'networkUri': 'ETH:net_101',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                      'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe_1002',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                     {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                      'requestedMbps': '2500', 'networkUri': 'FC:SAN-A',
                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}]},
]

"""
{"type":"ServerProfileTemplateV1","serverProfileDescription":"",
 "serverHardwareTypeUri":"/rest/server-hardware-types/7EDF550F-28E7-4600-A435-2CF877D55E68",
 "enclosureGroupUri":"/rest/enclosure-groups/7968834e-04d9-4873-b1c3-55bbdc432665",
 "serialNumberType":"Virtual","macType":"Virtual","wwnType":"Virtual","name":"template1","description":"","affinity":"Bay",
 "connections":[],"boot":{"manageBoot":true,"order":["CD","Floppy","USB","HardDisk","PXE"]},"bootMode":null,
 "firmware":{"manageFirmware":false,"firmwareBaselineUri":"","forceInstallFirmware":false,"firmwareInstallType":null},
 "bios":{"manageBios":false,"overriddenSettings":[]},"hideUnusedFlexNics":true,"localStorage":{},"sanStorage":null}
"""

server_profile_templates = [
    {'type': 'ServerProfileTemplateV1',
     'serverHardwareTypeUri': 'SHT:BL465c Gen8 1', 'enclosureGroupUri': 'EG:EG',
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': 'Profile1', 'description': '', 'affinity': 'Bay',
     'boot': {'manageBoot': True, 'order': ['CD', 'Floppy', 'USB', 'PXE', 'HardDisk']},
     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Flb 1:1-a',
                      'requestedMbps': '2000', 'networkUri': 'ETH:net_101',
                      'boot': {'priority': 'NotBootable'}},
                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Flb 1:2-b',
                      'requestedMbps': '2000', 'networkUri': 'FCOE:fcoe_102',
                      'boot': {'priority': 'NotBootable'}},
                     {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Flb 1:1-b',
                      'requestedMbps': '2000', 'networkUri': 'FC:SAN-A',
                      'boot': {'priority': 'NotBootable'}}]},
]

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Data for Profile tests for Enclosures 1

server_profile_raid0 = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connections': [],
                         'boot': {'manageBoot': True, 'order': ['PXE']},
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                          'sasLogicalJBODs': []}, }]


expected_server_profile_raid0 = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connections': [],
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                  'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                                   'sasLogicalJBODs': []},
                                  'status': 'OK'}]

server_profile_hba = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                       'connections': [],
                       'boot': {'manageBoot': True, 'order': ['PXE']},
                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                        'sasLogicalJBODs': []}, }]

expected_server_profile_hba = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                'connections': [],
                                'boot': {'manageBoot': True, 'order': ['PXE']},
                                'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                                 'sasLogicalJBODs': []},
                                'status': 'OK'}]


server_profile_raid1 = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                         'connections': [],
                         'boot': {'manageBoot': True, 'order': ['PXE']},
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                          'sasLogicalJBODs': []}, }]

expected_server_profile_raid1 = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                  'connections': [],
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                  'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                                   'sasLogicalJBODs': []},
                                  'status': 'OK'}]

server_profile_raid_no_initialize = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                      'connections': [],
                                      'boot': {'manageBoot': True, 'order': ['PXE']},
                                      'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                      'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                       'sasLogicalJBODs': []},
                                      }]

expected_server_profile_raid_no_initialize = [{'name': 'enc1_bay1', 'serverHardwareUri': 'SH:CN744502CQ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                               'connections': [],
                                               'boot': {'manageBoot': True, 'order': ['PXE']},
                                               'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                               'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                                'sasLogicalJBODs': []},
                                               'status': 'OK'}]

server_profile_templates = [{'name': 'Enclosure1Template', 'type': 'ServerProfileTemplateV3', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]}, },
                            {'name': 'Enc1 Bios and local storage with connections', 'type': 'ServerProfileTemplateV3', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                             'connectionSettings': {'manageConnections': True,
                                                    'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                             'bios': {'manageBios': True,
                                      'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                             'localStorage': {'sasLogicalJBODs': [],
                                              'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 2}]}]}}]


expected_server_profile_templates = [{'name': 'Enclosure1Template', 'uri': 'SPT:Enclosure1Template', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                      'connectionSettings': {'manageConnections': True,
                                                             'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                      'status': 'OK'},
                                     {'name': 'Enc1 Bios and local storage with connections', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                      'connectionSettings': {'manageConnections': True,
                                                             'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                      'bios': {'manageBios': True,
                                               'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                      'localStorage': {'sasLogicalJBODs': [],
                                                       'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 2}]}]},
                                      'status': 'OK'}]

server_profiles_from_spt = [{'name': 'wpst-tbird1-Bay1', 'serverHardwareUri': 'CN744502CQ, bay 1', 'serialNumberType': 'Virtual',
                             'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3:3:Synergy 3820C 10/20Gb CNA', 'serverProfileTemplateUri': 'SPT:Enclosure1Template'}]

expected_server_profiles_from_spt = [{'status': 'OK', 'name': 'wpst-tbird1-Bay1', 'serverHardwareUri': 'CN744502CQ, bay 1', 'serialNumberType': 'Virtual',
                                      'serverHardwareTypeUri': 'SHT:SY 480 Gen9 3:3:Synergy 3820C 10/20Gb CNA', 'serverProfileTemplateUri': 'SPT:Enclosure1Template'}]

server_profile_many_conn = [{'name': 'enc1_bay2_fail', 'serverHardwareUri': 'CN744502CQ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': 'Should fail, too many connections.', 'affinity': 'Bay',
                             'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                             {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:02', 'requestedVFs': '3'},
                                             {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:03'},
                                             {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:04'},
                                             {'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:05', 'requestedVFs': '3'},
                                             {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:06'},
                                             {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:07'},
                                             {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:08', 'requestedVFs': '3'},
                                             {'id': 9, 'name': 'net18', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net300', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:09'},
                                             {'id': 10, 'name': 'net19', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:10'},
                                             {'id': 11, 'name': 'net20', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:11'},
                                             {'id': 12, 'name': 'net21', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:12'},
                                             {'id': 13, 'name': 'net22', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:13'},
                                             {'id': 14, 'name': 'net23', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:14'},
                                             {'id': 15, 'name': 'net24', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:15'},
                                             {'id': 16, 'name': 'net25', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:10'},
                                             {'id': 17, 'name': 'net26', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:11'},
                                             {'id': 18, 'name': 'net27', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:12'},
                                             {'id': 19, 'name': 'net28', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:13'},
                                             {'id': 20, 'name': 'net29', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:14'},
                                             {'id': 21, 'name': 'net30', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:09'},
                                             {'id': 22, 'name': 'net31', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:10'},
                                             {'id': 23, 'name': 'net32', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:11'},
                                             {'id': 24, 'name': 'net33', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:12'},
                                             {'id': 25, 'name': 'net34', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:13'},
                                             {'id': 26, 'name': 'net35', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:14'}],
                             'boot': {'manageBoot': True, 'order': ['PXE']},
                             'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}}]
errormessage = 'No additional port available to support network'

server_profile_diff_conn = [{'name': 'enc1_bay2', 'serverHardwareUri': 'CN744502CQ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                             'boot': {'manageBoot': True, 'order': ['PXE']},
                             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                             'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                             {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15'},
                                             {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16'},
                                             {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17'}]}]


expected_server_profile_diff_conn = [{'name': 'enc1_bay2', 'serverHardwareUri': 'CN744502CQ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                      'boot': {'manageBoot': True, 'order': ['PXE']},
                                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                      'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                      {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15'},
                                                      {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16'},
                                                      {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17'}],
                                      'status': 'OK'}]

server_profile_three_conn = [{'name': 'enc1_bay2', 'serverHardwareUri': 'CN744502CQ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net10', 'boot': {'priority': 'Primary'}},
                                              {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net11'},
                                              {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net12'},
                                              {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net13'}]}]

expected_server_profile_three_conn = [{'name': 'enc1_bay2', 'serverHardwareUri': 'CN744502CQ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net10', 'boot': {'priority': 'Primary'}},
                                                       {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net11'},
                                                       {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net12'},
                                                       {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net13'}],
                                       'status': 'OK'}]

# Data for Profile tests for Enclosures 2
server_profile_templates_enc2 = [{'name': 'Enclosure2Template', 'type': 'ServerProfileTemplateV3', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]}, },
                                 {'name': 'Enc2 Bios and local storage with connections', 'type': 'ServerProfileTemplateV3', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                  'bios': {'manageBios': True,
                                           'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                  'localStorage': {'sasLogicalJBODs': [],
                                                   'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 2}]}]}}]


expected_server_profile_templates_enc2 = [{'name': 'Enclosure2Template', 'uri': 'SPT:Enclosure2Template', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                           'status': 'OK'},
                                          {'name': 'Enc2 Bios and local storage with connections', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]},
                                           'bios': {'manageBios': True,
                                                    'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                           'localStorage': {'sasLogicalJBODs': [],
                                                            'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 2}]}]},
                                           'status': 'OK'}]

server_profiles_from_spt_enc2 = [{'name': 'wpst-tbird2-Bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:HP Synergy 3820C 10/20Gb CNA',
                                  'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure2Template'}]

expected_server_profiles_from_spt_enc2 = [{'name': 'wpst-tbird2-Bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1:3:HP Synergy 3820C 10/20Gb CNA',
                                           'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure2Template', 'status': 'OK'}]

server_profile_raid0_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connections': [],
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid0_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connections': [],
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []},
                                       'status': 'OK'}]

server_profile_hba_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connections': [],
                            'boot': {'manageBoot': True, 'order': ['PXE']},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                            'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                             'sasLogicalJBODs': []}, }]

expected_server_profile_hba_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'connections': [],
                                     'boot': {'manageBoot': True, 'order': ['PXE']},
                                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                     'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                                      'sasLogicalJBODs': []},
                                     'status': 'OK'}]


server_profile_raid1_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connections': [],
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid1_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connections': [],
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []}, 'status': 'OK'}]

server_profile_raid_no_initialize_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connections': [],
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                           'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                            'sasLogicalJBODs': []}, }]

expected_server_profile_raid_no_initialize_enc2 = [{'name': 'enc2_bay1', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                                    'connections': [],
                                                    'boot': {'manageBoot': True, 'order': ['PXE']},
                                                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                                    'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                                     'sasLogicalJBODs': []},
                                                    'status': 'OK'}]

server_profile_many_conn_enc2 = [{'name': 'enc2_bay2_fail', 'serverHardwareUri': 'SH:CN744502CZ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': 'Should fail, too many connections.', 'affinity': 'Bay',
                                  'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:10', 'boot': {'priority': 'Primary'}},
                                                  {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:11', 'requestedVFs': '3'},
                                                  {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:12'},
                                                  {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:13'},
                                                  {'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:14', 'requestedVFs': '3'},
                                                  {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:15'},
                                                  {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:16'},
                                                  {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:17', 'requestedVFs': '3'},
                                                  {'id': 9, 'name': 'net18', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net18', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:18'}],
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}}]

server_profile_diff_conn_enc2 = [{'name': 'enc2_bay2', 'serverHardwareUri': 'SH:CN744502CZ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                  'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                  {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15'},
                                                  {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16'},
                                                  {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17'}], }]

expected_server_profile_diff_conn_enc2 = [{'name': 'enc2_bay2', 'serverHardwareUri': 'SH:CN744502CZ, bay 1', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                           'connections': [{'id': 1, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net14', 'boot': {'priority': 'Primary'}},
                                                           {'id': 2, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net15'},
                                                           {'id': 3, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net16'},
                                                           {'id': 4, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net17'}],
                                           'status': 'OK'}]

server_profile_three_conn_enc2 = [{'name': 'enc2_bay2', 'serverHardwareUri': 'SH:CN744502CZ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                   'boot': {'manageBoot': True, 'order': ['PXE']},
                                   'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                   'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:10', 'boot': {'priority': 'Primary'}},
                                                   {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:11', 'requestedVFs': '3'},
                                                   {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:12'},
                                                   {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:13'}], }]

expected_server_profile_three_conn_enc2 = [{'name': 'enc2_bay2', 'serverHardwareUri': 'SH:CN744502CQ, bay 2', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                            'boot': {'manageBoot': True, 'order': ['PXE']},
                                            'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                            'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:10', 'boot': {'priority': 'Primary'}},
                                                            {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:11', 'requestedVFs': '3'},
                                                            {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:12'},
                                                            {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:13'}],
                                            'status': 'OK'}]
# Data for Profile tests for Enclosures 3
server_profile_templates_enc3 = [{'name': 'Enclosure3Template', 'type': 'ServerProfileTemplateV3', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]
                                                         }, },
                                 {'name': 'Enc3 Bios and local storage with connections', 'type': 'ServerProfileTemplateV3', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'connectionSettings': {'manageConnections': True,
                                                         'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]
                                                         },
                                  'bios': {'manageBios': True,
                                           'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                  'localStorage': {'sasLogicalJBODs': [],
                                                   'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 2}]}]}
                                  }]

expected_server_profile_templates_enc3 = [{'name': 'Enclosure3Template', 'uri': 'SPT:Enclosure3Template', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]
                                                                  }, 'status': 'OK'},
                                          {'name': 'Enc3 Bios and local storage with connections', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2', 'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'connectionSettings': {'manageConnections': True,
                                                                  'connections': [{'id': 1, 'name': 'ETH', 'functionType': 'Ethernet', 'portId': 'Auto', 'requestedMbps': '2000', 'networkUri': 'ETH:net10'}]
                                                                  },
                                           'bios': {'manageBios': True,
                                                    'overriddenSettings': [{u'id': u'AdminName', u'value': u'Sylvester McSweggins'}]},
                                           'localStorage': {'sasLogicalJBODs': [],
                                                            'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'logicalDrives': [{u'name': u'raid', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': None, u'numPhysicalDrives': 2}]}]},
                                           'status': 'OK'}]

server_profiles_from_spt_enc3 = [{'name': 'wpst-tbird3-Bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
                                  'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure3Template'}]

expected_server_profiles_from_spt_enc3 = [{'status': 'OK', 'name': 'wpst-tbird3-Bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 1', 'serverHardwareTypeUri': 'SHT:SY 480 Gen9 2:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA',
                                           'serialNumberType': 'Virtual', 'serverProfileTemplateUri': 'SPT:Enclosure3Template'}]

server_profile_raid0_enc3 = [{'name': '"enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connections': [],
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid0_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connections': [],
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD0', u'bootable': False, u'raidLevel': u'RAID0', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []},
                                       'status': 'OK'}]

server_profile_hba_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                            'connections': [],
                            'boot': {'manageBoot': True, 'order': ['PXE']},
                            'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                            'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                             'sasLogicalJBODs': []}, }]

expected_server_profile_hba_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                     'connections': [],
                                     'boot': {'manageBoot': True, 'order': ['PXE']},
                                     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                     'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'HBA', u'importConfiguration': False}],
                                                      'sasLogicalJBODs': []},
                                     'status': 'OK'}]

server_profile_raid1_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                              'connections': [],
                              'boot': {'manageBoot': True, 'order': ['PXE']},
                              'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                              'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                               'sasLogicalJBODs': []}, }]

expected_server_profile_raid1_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                       'connections': [],
                                       'boot': {'manageBoot': True, 'order': ['PXE']},
                                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                       'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': True, u'mode': u'RAID', u'importConfiguration': False, u'logicalDrives': [{u'name': u'LD1', u'bootable': False, u'raidLevel': u'RAID1', u'sasLogicalJBODId': None, u'driveTechnology': u'SasHdd', u'numPhysicalDrives': 2, u'driveNumber': None}]}],
                                                        'sasLogicalJBODs': []},
                                       'status': 'OK'}]

server_profile_raid_no_initialize_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                           'connections': [],
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                           'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                            'sasLogicalJBODs': []}, }]

expected_server_profile_raid_no_initialize_enc3 = [{'name': 'enc3_bay1', 'serverHardwareUri': 'SH:CN750163KF, bay 7', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': '', 'affinity': 'Bay',
                                                    'connections': [],
                                                    'boot': {'manageBoot': True, 'order': ['PXE']},
                                                    'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                                    'localStorage': {'controllers': [{u'deviceSlot': u'Embedded', u'initialize': False, u'mode': u'RAID', u'importConfiguration': False}],
                                                                     'sasLogicalJBODs': []},
                                                    'status': 'OK'}]

server_profile_many_conn_enc3 = [{'name': 'enc3_bay5_fail', 'serverHardwareUri': 'SH:CN750163KF, bay 5', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'description': 'Should fail, too many connections.', 'affinity': 'Bay',
                                  'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                  {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:02', 'requestedVFs': '3'},
                                                  {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:03'},
                                                  {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:04'},
                                                  {'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:05', 'requestedVFs': '3'},
                                                  {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:06'},
                                                  {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:07'},
                                                  {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:08', 'requestedVFs': '3'},
                                                  {'id': 9, 'name': 'net18', 'functionType': 'Ethernet', 'portId': 'Auto', 'networkUri': 'ETH:net18', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:09'}],
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'}}]

server_profile_diff_conn_enc3 = [{'name': 'enc3_bay5', 'serverHardwareUri': 'SH:CN750163KF, bay 5', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                  'boot': {'manageBoot': True, 'order': ['PXE']},
                                  'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                  'connections': [{'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:14', 'boot': {'priority': 'Primary'}},
                                                  {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:15', 'requestedVFs': '3'},
                                                  {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:16'},
                                                  {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:17'}], }]

expected_server_profile_diff_conn_enc3 = [{'name': 'enc3_bay5', 'serverHardwareUri': 'SH:CN750163KF, bay 5', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                           'boot': {'manageBoot': True, 'order': ['PXE']},
                                           'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                                           'connections': [{'id': 5, 'name': 'net14', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a', 'networkUri': 'ETH:net14', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:14', 'boot': {'priority': 'Primary'}},
                                                           {'id': 6, 'name': 'net15', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-b', 'networkUri': 'ETH:net15', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:15', 'requestedVFs': '3'},
                                                           {'id': 7, 'name': 'net16', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-c', 'networkUri': 'ETH:net16', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:16'},
                                                           {'id': 8, 'name': 'net17', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-d', 'networkUri': 'ETH:net17', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:17'}],
                                           'status': 'OK'}]

server_profile_three_conn_enc3 = [{'name': 'enc3_bay5', 'serverHardwareUri': 'SH:CN750163KF, bay 5', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                   'boot': {'manageBoot': True, 'order': ['PXE']},
                                   'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                   'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                   {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:02', 'requestedVFs': '3'},
                                                   {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:03'},
                                                   {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:04'}], }]

expected_server_profile_three_conn_enc3 = [{'name': 'enc3_bay5', 'serverHardwareUri': 'SH:CN750163KF, bay 5', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual', 'affinity': 'Bay',
                                            'boot': {'manageBoot': True, 'order': ['PXE']},
                                            'bootMode':{'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                            'connections': [{'id': 1, 'name': 'net10', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a', 'networkUri': 'ETH:net10', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:01', 'boot': {'priority': 'Primary'}},
                                                            {'id': 2, 'name': 'net11', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-b', 'networkUri': 'ETH:net11', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:02', 'requestedVFs': '3'},
                                                            {'id': 3, 'name': 'net12', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-c', 'networkUri': 'ETH:net12', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:03'},
                                                            {'id': 4, 'name': 'net13', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-d', 'networkUri': 'ETH:net13', 'macType': 'UserDefined', 'mac': 'aa:bb:65:80:00:04'}],
                                            'status': 'OK'}]


server_profile_local_storage = [{
    'name': 'CN744502CZbay5',
    'serverHardwareUri': 'SH:CN744502CQ, bay 5',
    'enclosureGroupUri': 'ISO-EG-Ring',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'bootMode': {'manageMode': True, 'mode': 'UEFI',
                 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'firmware': {
        'firmwareScheduleDateTime': None,
        'firmwareActivationType': None,
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
    },
    'connections': [{
        'id': 1,
        'name': None,
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:net10',
        'functionType': 'Ethernet',
        'boot': {'priority': 'NotBootable'},
    }],
    'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
    'bios': {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName',
                                     'value': 'WPST Tester1'}, {'id': 'AdminPhone',
                                                                'value': '111-111-1111'}]},
    'localStorage': {'controllers': [{
        'deviceSlot': 'Embedded',
        'mode': 'RAID',
        'initialize': True,
        'importConfiguration': False,
        'logicalDrives': [{
            'name': 'LD1',
            'raidLevel': 'RAID0',
            'bootable': True,
            'numPhysicalDrives': 2,
            'driveTechnology': 'SasHdd',
            'sasLogicalJBODId': None,
        }],
    }]},
}]

expected_server_profile_local_storage = [{
    'status': 'OK',
    'type': 'ServerProfileV7',
    'name': 'CN744502CZbay5',
    'serverHardwareUri': 'SH:CN744502CQ, bay 5',
    'enclosureGroupUri': 'EG:ISO-EG-Ring',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'bootMode': {'manageMode': True, 'mode': 'UEFI',
                 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'firmware': {
        'firmwareScheduleDateTime': None,
        'firmwareActivationType': None,
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
    },
    'connections': [{
        'id': 1,
        'name': None,
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:net10',
        'functionType': 'Ethernet',
        'boot': {'priority': 'NotBootable'},
    }],
    'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
    'bios': {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName',
                                     'value': 'WPST Tester1'}, {'id': 'AdminPhone',
                                                                'value': '111-111-1111'}]},
    'localStorage': {'controllers': [{
        'deviceSlot': 'Embedded',
        'mode': 'RAID',
        'importConfiguration': False,
        'logicalDrives': [{
            'name': 'LD1',
            'raidLevel': 'RAID0',
            'bootable': True,
            'numPhysicalDrives': 2,
            'driveTechnology': 'SasHdd',
            'sasLogicalJBODId': None,
        }],
    }]},
}]

edit_serverprofile_hba = [{
    'name': 'CN744502CZbay5',
    'status': 'OK',
    'type': 'ServerProfileV7',
    'serverHardwareUri': 'SH:CN744502CQ, bay 5',
    'enclosureGroupUri': 'ISO-EG-Ring',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'bootMode': {'manageMode': True, 'mode': 'UEFI',
                 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'firmware': {
        'firmwareScheduleDateTime': None,
        'firmwareActivationType': None,
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
    },
    'connections': [{
        'id': 1,
        'name': None,
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:net10',
        'functionType': 'Ethernet',
        'boot': {'priority': 'NotBootable'},
    }],
    'bios': {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName',
                                     'value': 'WPST Tester1'}, {'id': 'AdminPhone',
                                                                'value': '111-111-1111'}]},
    'localStorage': {'sasLogicalJBODs': [], 'controllers': [{
        'deviceSlot': 'Embedded',
        'mode': 'HBA',
        'initialize': True,
        'importConfiguration': False,
    }]},
}]

expected_serverprofile_hba = edit_serverprofile_hba = [{
    'name': 'CN744502CZbay5',
    'type': 'ServerProfileV7',
    'serverHardwareUri': 'SH:CN744502CQ, bay 5',
    'enclosureGroupUri': 'ISO-EG-Ring',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'bootMode': {'manageMode': True, 'mode': 'UEFI',
                 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'firmware': {
        'firmwareScheduleDateTime': None,
        'firmwareActivationType': None,
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
    },
    'connections': [{
        'id': 1,
        'name': None,
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:net10',
        'functionType': 'Ethernet',
        'boot': {'priority': 'NotBootable'},
    }],
    'bios': {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName',
                                     'value': 'WPST Tester1'}, {'id': 'AdminPhone',
                                                                'value': '111-111-1111'}]},
    'localStorage': {'sasLogicalJBODs': [], 'controllers': [{
        'deviceSlot': 'Embedded',
        'mode': 'HBA',
        'initialize': True,
        'importConfiguration': False,
    }]},
}]

edit_serverprofile_raid = [{
    'name': 'CN744502CZbay5',
    'type': 'ServerProfileV7',
    'serverHardwareUri': 'SH:CN744502CQ, bay 5',
    'enclosureGroupUri': 'ISO-EG-Ring',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'bootMode': {'manageMode': True, 'mode': 'UEFI',
                 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'firmware': {
        'firmwareScheduleDateTime': None,
        'firmwareActivationType': None,
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
    },
    'connections': [{
        'id': 1,
        'name': None,
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:net10',
        'functionType': 'Ethernet',
        'boot': {'priority': 'NotBootable'},
    }],
    'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
    'bios': {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName',
                                     'value': 'WPST Tester1'}, {'id': 'AdminPhone',
                                                                'value': '111-111-1111'}]},
    'localStorage': {'controllers': [{
        'deviceSlot': 'Embedded',
        'mode': 'RAID',
        'initialize': True,
        'importConfiguration': False,
        'logicalDrives': [{
            'name': 'LD3',
            'raidLevel': 'RAID0',
            'bootable': True,
            'numPhysicalDrives': 2,
            'driveTechnology': 'SasHdd',
            'sasLogicalJBODId': None,
        }],
    }]},
}]

expected_serverprofile_raid = [{
    'name': 'CN744502CZbay5',
    'type': 'ServerProfileV7',
    'serverHardwareUri': 'SH:CN744502CQ, bay 5',
    'enclosureGroupUri': 'ISO-EG-Ring',
    'serialNumberType': 'Physical',
    'macType': 'Physical',
    'wwnType': 'Physical',
    'bootMode': {'manageMode': True, 'mode': 'UEFI',
                 'pxeBootPolicy': 'Auto'},
    'boot': {'manageBoot': True, 'order': ['HardDisk']},
    'firmware': {
        'firmwareScheduleDateTime': None,
        'firmwareActivationType': None,
        'firmwareInstallType': None,
        'forceInstallFirmware': False,
        'manageFirmware': False,
        'firmwareBaselineUri': None,
    },
    'connections': [{
        'id': 1,
        'name': None,
        'portId': 'Mezz 3:1-a',
        'requestedMbps': '2500',
        'networkUri': 'ETH:net10',
        'functionType': 'Ethernet',
        'boot': {'priority': 'NotBootable'},
    }],
    'sanStorage': {'manageSanStorage': False, 'volumeAttachments': []},
    'bios': {'manageBios': True,
             'overriddenSettings': [{'id': 'AdminName',
                                     'value': 'WPST Tester1'}, {'id': 'AdminPhone',
                                                                'value': '111-111-1111'}]},
    'localStorage': {'controllers': [{
        'deviceSlot': 'Embedded',
        'mode': 'RAID',
        'importConfiguration': False,
        'logicalDrives': [{
            'name': 'LD3',
            'raidLevel': 'RAID0',
            'bootable': True,
            'numPhysicalDrives': 2,
            'driveTechnology': 'SasHdd',
            'sasLogicalJBODId': None,
        }],
    }]},
}]

server_profiles = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CZ, bay 1',
                    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:ISO-EG-Ring',
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': 'CN744502CZbay1-to-CN744502CZbay5', 'description': '', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                    'boot': {'manageBoot': True, 'order': ['PXE']},
                    'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                    'localStorage': {"sasLogicalJBODs": [], "controllers": []},
                    'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}]

transformation_sp = [{"type": "ServerProfileV7", "name": "CN744502CZbay1-to-CN744502CZbay5", "description": "",
                      'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
                      "serverProfileTemplateUri": "", "templateCompliance": "Unknown", "serverHardwareUri": "SH:CN744502CZ, bay 5", "enclosureGroupUri": "EG:ISO-EG-Ring",
                      "enclosureUri": "ENC:CN744502CZ", "enclosureBay": 5, "affinity": "Bay", "associatedServer": None, "hideUnusedFlexNics": True,
                      "firmware": {"firmwareScheduleDateTime": None, "firmwareActivationType": None, "firmwareInstallType": None, "forceInstallFirmware": False,
                                   "manageFirmware": False, "firmwareBaselineUri": None},
                      "category": "server-profiles", "inProgress": False,
                      "connections": [{"id": 1, "name": "Mezz 3:1-a", "functionType": "Ethernet", "networkUri": "ETH:net10", "portId": "Mezz 3:1-a",
                                       "requestedVFs": "Auto", "allocatedVFs": 64, "macType": "Physical", "wwpnType": "Physical",
                                       "requestedMbps": "4000", "allocatedMbps": 4000,
                                       "maximumMbps": 10000, "ipv4": None, "boot": {"priority": "NotBootable"}}],
                      'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                      'boot': {'manageBoot': True, 'order': ['PXE']},
                      "bios": {"manageBios": False, "overriddenSettings": []},
                      "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                      "sanStorage": {"volumeAttachments": [], "sanSystemCredentials": [], "manageSanStorage": False}}]

expected_transformation_sp = [{'type': 'ServerProfileV7',
                               'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
                               'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Physical',
                               'macType': 'Physical', 'wwnType': 'Physical',
                               'name': 'CN744502CZbay1-to-CN744502CZbay5', 'description': '', 'affinity': 'Bay',
                               'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Auto', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}],
                               'bios': {'manageBios': False, 'overriddenSettings': []},
                               'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                               'boot': {'manageBoot': True, 'order': ['PXE']},
                               'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [], 'sanSystemCredentials': []},
                               'localStorage': {"sasLogicalJBODs": [], "controllers": []}}]

expected_sp_from_transform_dto = [{'type': 'ServerProfileV7',
                                   'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
                                   'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Physical',
                                   'macType': 'Physical', 'wwnType': 'Physical',
                                   'name': 'CN744502CZbay1-to-CN744502CZbay5', 'description': '', 'affinity': 'Bay',
                                   'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '4000', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}],
                                   'bios': {'manageBios': False, 'overriddenSettings': []},
                                   'status': 'OK', 'state': 'Normal',
                                   'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                   'boot': {'manageBoot': True, 'order': ['PXE']},
                                   'sanStorage': {'manageSanStorage': False, 'volumeAttachments': [], 'sanSystemCredentials': []},
                                   'localStorage': {"sasLogicalJBODs": [], "controllers": []}}]

edit_sp_transform = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CZ, bay 5',
                      'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:ISO-EG-Ring',
                      'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                      'name': 'CN744502CZbay1-to-CN744502CZbay5', 'description': '', 'affinity': 'Bay',
                      'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                      'boot': {'manageBoot': True, 'order': ['PXE', 'HardDisk', 'CD', 'USB']},
                      'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester2'}, {'id': 'AdminPhone', 'value': '222-222-2222'}]},
                      'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '4000', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}],
                      'localStorage': {"sasLogicalJBODs": [], "controllers": []}}]

expected_edit_sp_transform = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CZ, bay 5',
                               'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
                               'enclosureGroupUri': 'EG:ISO-EG-Ring', 'serialNumberType': 'Physical',
                               'macType': 'Physical', 'wwnType': 'Physical',
                               'bootMode': {'manageMode': True, 'mode': 'BIOS'},
                               'boot': {'manageBoot': True, 'order': ['PXE', 'HardDisk', 'CD', 'USB']},
                               'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester2'}, {'id': 'AdminPhone', 'value': '222-222-2222'}]},
                               'name': 'CN744502CZbay1-to-CN744502CZbay5', 'description': '', 'affinity': 'Bay',
                               'status': 'OK', 'state': 'Normal',
                               'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '4000', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}],
                               'localStorage': {"sasLogicalJBODs": [], "controllers": []}}]

health_status = {'enc_serial': 'CN744502CQ', 'efuse_bay_number': 2, 'efuse_action': 'EFuseReset'}

efuse_server_profile = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CQ, bay 5',
                         'serverHardwareTypeUri': 'SHT:SY 680 Gen9:3:HP FlexFabric Bronco Gen3 2p 20GbE CNA BCM57840', 'enclosureGroupUri': 'EG:ISO-EG-Ring',
                         'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                         'name': 'CN744502CQbay5', 'description': '', 'affinity': 'Bay',
                         'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                         'boot': {'manageBoot': True, 'order': ['PXE']},
                         'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                         'localStorage': {"sasLogicalJBODs": [], "controllers": []},
                         'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}]

expected_efuse_server_profile = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CQ, bay 5',
                                  'serverHardwareTypeUri': 'SHT:SY 680 Gen9:3:HP FlexFabric Bronco Gen3 2p 20GbE CNA BCM57840', 'enclosureGroupUri': 'EG:ISO-EG-Ring',
                                  'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                  'name': 'CN744502CQbay5', 'description': '', 'affinity': 'Bay',
                                  'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                  'boot': {'manageBoot': True, 'order': ['PXE']}, 'status': 'OK',
                                  'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                  'localStorage': {"sasLogicalJBODs": [], "controllers": []},
                                  'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}]


fan_failures = [{'enc_serial': 'CN744502CQ', 'fan_action': 'FanFaultInjection', 'fan_bay_number': 1, 'fan_fault_type': 'Fan1', 'inject_failure': 'true', 'filter': '/rest/v1/Fan/1'},
                {'enc_serial': 'CN744502CQ', 'fan_action': 'FanFaultInjection', 'fan_bay_number': 1, 'fan_fault_type': 'Fan1', 'inject_failure': 'false', 'filter': '/rest/v1/Fan/1'}]

power_failures = [{'enc_serial': 'CN744502CQ', 'power_action': 'PSFaultInjection', 'power_bay_number': 2, 'power_fault_type': 'PS_OK', 'inject_failure': 'true', 'filter': '/rest/v1/PowerSupply/2'},
                  {'enc_serial': 'CN744502CQ', 'power_action': 'PSFaultInjection', 'power_bay_number': 2, 'power_fault_type': 'PS_OK', 'inject_failure': 'false', 'filter': '/rest/v1/PowerSupply/2'}]

snmp_trap = [{'trap_tool_path': 'C:\\Users\\Administrator\\Desktop\\sendSnmpTrap.exe', 'source_server_hardware_name': 'CN744502CQ, bay 4', 'source_server_hardware': '16.114.221.66', 'trap_name': 'cpqHeResilientMemLockStepMemoryEngaged', 'trap_value': "cpqHoTrapFlags 1"},
             {'trap_tool_path': 'C:\\Users\\Administrator\\Desktop\\sendSnmpTrap.exe', 'source_server_hardware_name': 'CN744502CQ, bay 4', 'source_server_hardware': '16.114.221.66', 'trap_name': 'cpqHe4FltTolPowerSupplyFailed',
              'trap_value': "cpqHeFltTolPowerSupplyChassis 2" + " -v " + "cpqHeFltTolPowerSupplyBay 3" + " -v " + "cpqHeFltTolPowerSupplyStatus 13" + " -v " + "cpqHeFltTolPowerSupplyModel 5" + " -v " + "cpqHeFltTolPowerSupplySerialNumber 6" + " -v " + "cpqHeFltTolPowerSupplyAutoRev 7" +
              " -v " + "cpqHeFltTolPowerSupplyFirmwareRev 8" + " -v " + "cpqHeFltTolPowerSupplySparePartNum 9" + " -v " + "cpqSiServerSystemId 10"}]

snmp_server_profile = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CQ, bay 4',
                        'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:ISO-EG-Ring',
                        'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                        'name': 'CN744502CQbay4', 'description': '', 'affinity': 'Bay',
                        'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                        'boot': {'manageBoot': True, 'order': ['PXE']},
                        'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                        'localStorage': {"sasLogicalJBODs": [], "controllers": []},
                        'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}]

expected_snmp_server_profile = [{'type': 'ServerProfileV7', 'serverHardwareUri': 'SH:CN744502CQ, bay 4',
                                 'serverHardwareTypeUri': 'SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA', 'enclosureGroupUri': 'EG:ISO-EG-Ring',
                                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                                 'name': 'CN744502CQbay4', 'description': '', 'affinity': 'Bay',
                                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'IPv4'},
                                 'boot': {'manageBoot': True, 'order': ['PXE']}, 'status': 'OK',
                                 'bios': {'manageBios': True, 'overriddenSettings': [{'id': 'AdminName', 'value': 'WPST Tester1'}, {'id': 'AdminPhone', 'value': '111-111-1111'}]},
                                 'localStorage': {"sasLogicalJBODs": [], "controllers": []},
                                 'connections': [{'id': 1, 'name': 'Mezz 3:1-a', 'portId': 'Mezz 3:1-a', 'requestedMbps': '2500', 'networkUri': 'ETH:net10', 'functionType': 'Ethernet'}]}]

admin_credentials = {'userName': 'Administrator',
                     'password': 'wpsthpvse1'}

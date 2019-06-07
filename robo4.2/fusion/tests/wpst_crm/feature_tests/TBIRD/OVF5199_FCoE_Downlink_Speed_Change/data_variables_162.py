from copy import deepcopy

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks = [{'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_401', 'privateNetwork': False, 'purpose': 'General', 'smartLink': False, 'vlanId': 401}]

fcoe_networks = [{'name': 'fcoe-30', 'type': 'fcoe-networkV4', 'vlanId': 30},
                 {'name': 'fcoe-40', 'type': 'fcoe-networkV4', 'vlanId': 40}]


###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapASide =\
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

###
# Interconnect bays configurations
# 2 Enclosures, Fabric 3
###

Enc2Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc2MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]


###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}

    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

###
# Interconnect bays configurations
# 4 Enclosures, Fabric 3
###

Enc4Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4}
    ]

###
# Interconnect bays configurations
# 5 Enclosures, Fabric 3
###

Enc5Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 3, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 6, 'enclosure': 4, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 4},
        {'bay': 3, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5},
        {'bay': 6, 'enclosure': 5, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 5}
    ]

frame = 2

if frame == 1:
    REDUNDANCY = 'Redundant'
elif frame == 2:
    REDUNDANCY = 'HighlyAvailable'


IBS = 3
# LIG = 'LIG' + '_' + REDUNDANCY
LIG = 'LIG1'
EG = 'EG'
LE = 'LE'
LI = {'name': LE + '-' + LIG}
ENC_1 = 'MXQ734024M'
ENC_2 = 'CN7545084B'
ENC_3 = ''
ENC_4 = ''
ENC_5 = ''
ENC_List = ['ENC:' + ENC_1, 'ENC:' + ENC_2, 'ENC:' + ENC_3, 'ENC:' + ENC_4, 'ENC:' + ENC_5]
ENCs = [ENC_2, ENC_1]


uplink_sets = {
    'US-Eth': {
        'name': 'US-Eth',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_401'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q5', 'speed': 'Auto'},
                                   {'enclosure': '2', 'bay': '6', 'port': 'Q5', 'speed': 'Auto'}
                                   ]
    },
    'US-FCoE30': {
        'name': 'US-FCoE30',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-30'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q4.1', 'speed': 'Auto'}
                                   ]
    },
    'US-FCoE40': {
        'name': 'US-FCoE40',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-40'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q4.1', 'speed': 'Auto'}
                                   ]
    }
}

ligs = {
    'LIG':
    {'name': LIG,
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': Enc2Map,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': REDUNDANCY,
     'uplinkSets': [deepcopy(uplink_sets['US-Eth']), deepcopy(uplink_sets['US-FCoE30']), deepcopy(uplink_sets['US-FCoE40'])],
     'downlinkSpeedMode': 'SPEED_25GB'
     }
}

enc_group = {
    'EG':
        {'name': EG,
         'enclosureCount': frame,
         'interconnectBayMappings':
             [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG},
              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
              {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG}],
         'ipAddressingMode': 'DHCP'
         }
}

les = {
    'LE':
        {'name': LE,
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

Interconnect_name = [ENC_2 + ', ' + 'interconnect 6', ENC_1 + ', ' + 'interconnect 3']
Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]

Uplink_ports = [['Q5', 'Q4:2'], ['Q5', 'Q4:2']]
downlink_port_Quack = [['d15', 'd2'], ['d3', 'd14']]
downlink_port_Quagmire2 = [['d3', 'd16'], ['d15', 'd4']]

SP_Quack = [
    {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_1 + ', bay 3',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
             'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
             'name': ENC_1 + '_Bay3_Gen10_Quack', 'description': 'Gen10_Win', 'affinity': 'Bay',
             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
             'boot': {'manageBoot': True, 'order': ['HardDisk']},
             'connectionSettings': {
                 'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                  'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-30',
                                  'boot': {'priority': 'NotBootable'}, 'mac': 'DE:59:B8:A0:00:18', 'wwpn': '10:00:aa:33:7f:f0:00:0a', 'wwnn': '10:00:aa:33:7f:f0:00:0b'},
                                 {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                  'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-40',
                                  'boot': {'priority': 'NotBootable'}, 'mac': 'DE:59:B8:A0:00:0C', 'wwpn': '10:00:aa:33:7f:f0:00:0c', 'wwnn': '10:00:aa:33:7f:f0:00:0d'},
                                 ]}},
    {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_2 + ', bay 2',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_2, 'enclosureGroupUri': 'EG:%s' % EG,
             'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
             'name': ENC_2 + '_Bay2_Gen10_Quack', 'description': 'Gen10_Win', 'affinity': 'Bay',
             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
             'boot': {'manageBoot': True, 'order': ['HardDisk']},
             'connectionSettings': {
                 'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                  'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-30',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                  'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-40',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                 ]}}

]

ilo_details_Quack = [{'ilo_ip': '15.245.132.17', 'userName': 'Administrator', 'password': 'hpvse123'}, {'ilo_ip': '15.245.132.204', 'userName': 'Administrator', 'password': 'hpvse123'}]
server_credentials_Quack = [{'userName': 'Administrator', 'password': '"-hpvse123."'}, {'userName': 'Administrator', 'password': 'hpvse@123'}]

SP_Quagmire2 = [{'type': 'ServerProfileV10', 'serverHardwareUri': ENC_2 + ', bay 3',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_2, 'enclosureGroupUri': 'EG:%s' % EG,
                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                 'name': ENC_2 + '_Bay3_Gen10_Quagmire2', 'description': 'Gen10_Win', 'affinity': 'Bay',
                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                 'connectionSettings': {
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                      'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                      'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                      'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-30',
                                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                      'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-40',
                                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     ]}},
                {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_1 + ', bay 4',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
                    'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                    'name': ENC_1 + '_Bay4_Gen10_Quagmire2', 'description': 'Gen10_Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-30',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-40',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''}
                                        ]}}
                ]

ilo_details_Quagmire2 = [{'ilo_ip': '15.245.134.32', 'userName': 'Administrator', 'password': 'hpvse123'}, {'ilo_ip': '15.245.132.182', 'userName': 'Administrator', 'password': 'hpvse123'}]
server_credentials_Quagmire2 = [{'userName': 'Administrator', 'password': 'hpvse@1'}, {'userName': 'Administrator', 'password': 'hpvse@1'}]
ilo_details_all = [{'ilo_ip': '15.245.132.17', 'userName': 'Administrator', 'password': 'hpvse123'},
                   {'ilo_ip': '15.245.132.204', 'userName': 'Administrator', 'password': 'hpvse123'},
                   {'ilo_ip': '15.245.134.32', 'userName': 'Administrator', 'password': 'hpvse123'},
                   {'ilo_ip': '15.245.132.182', 'userName': 'Administrator', 'password': 'hpvse123'}]

server_details_all = [{'ip': '', 'userName': 'Administrator', 'password': '"-hpvse123."', 'wcmd': ''},
                      {'ip': '', 'userName': 'Administrator', 'password': 'hpvse@123', 'wcmd': ''},
                      {'ip': '', 'userName': 'Administrator', 'password': 'hpvse@1', 'wcmd': ''},
                      {'ip': '', 'userName': 'Administrator', 'password': 'hpvse@1', 'wcmd': ''}]

kill_diskspd = "TASKKILL /F /IM diskspd.exe"

diskspd_cmd = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"', 'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample2.dat"']
diskspd_cmd_30min = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"', 'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample2.dat"']
diskspd_cmds_Quagmire2 = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"', 'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample2.dat"']
diskspd_cmds_Quagmire2_30min = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"', 'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample2.dat"']
diskspd_cmds_30min = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"',
                      'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample2.dat"',
                      'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"',
                      'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample2.dat"']
diskspd_cmds_1min = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"',
                     'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample2.dat"',
                     'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L D:\sample.dat >C:\sample1.dat"',
                     'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample2.dat"']
SP_Quack_rbw16 = [
    {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_1 + ', bay 3',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
             'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
             'name': ENC_1 + '_Bay3_Gen10_Quack', 'description': 'Gen10_Win', 'affinity': 'Bay',
             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
             'boot': {'manageBoot': True, 'order': ['HardDisk']},
             'connectionSettings': {
                 'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                  'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-30',
                                  'boot': {'priority': 'NotBootable'}, 'mac': 'DE:59:B8:A0:00:18', 'wwpn': '10:00:aa:33:7f:f0:00:0a', 'wwnn': '10:00:aa:33:7f:f0:00:0b'},
                                 {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                  'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-40',
                                  'boot': {'priority': 'NotBootable'}, 'mac': 'DE:59:B8:A0:00:0C', 'wwpn': '10:00:aa:33:7f:f0:00:0c', 'wwnn': '10:00:aa:33:7f:f0:00:0d'},
                                 ]}}
]

SP_Quack_rbw8 = [
    {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_1 + ', bay 3',
             'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_1, 'enclosureGroupUri': 'EG:%s' % EG,
             'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
             'name': ENC_1 + '_Bay3_Gen10_Quack', 'description': 'Gen10_Win', 'affinity': 'Bay',
             'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
             'boot': {'manageBoot': True, 'order': ['HardDisk']},
             'connectionSettings': {
                 'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                                  'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                  'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                 {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                  'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-30',
                                  'boot': {'priority': 'NotBootable'}, 'mac': 'DE:59:B8:A0:00:18', 'wwpn': '10:00:aa:33:7f:f0:00:0a', 'wwnn': '10:00:aa:33:7f:f0:00:0b'},
                                 {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                  'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-40',
                                  'boot': {'priority': 'NotBootable'}, 'mac': 'DE:59:B8:A0:00:0C', 'wwpn': '10:00:aa:33:7f:f0:00:0c', 'wwnn': '10:00:aa:33:7f:f0:00:0d'},
                                 ]}}
]
Li_body_50GB = [{"op": "replace", "path": "/downlinkSpeedMode", "value": "SPEED_50GB"}]
Li_body_25GB = [{"op": "replace", "path": "/downlinkSpeedMode", "value": "SPEED_25GB"}]
# win_lun_count_Quack = [4, 2]
# win_lun_count_Quagmire2 = [2, 1]
# lun_count_total = [[4, 2],[2, 1]]
SP_Quagmire2_rbw32 = [
    {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_2 + ', bay 3',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_2, 'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': ENC_2 + '_Bay3_Gen10_Quagmire2', 'description': 'Gen10_Win', 'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                          'requestedMbps': '32000', 'networkUri': 'FCOE:fcoe-30',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                          'requestedMbps': '32000', 'networkUri': 'FCOE:fcoe-40',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         ]}}
]

SP_Quagmire2_rbw8 = [
    {'type': 'ServerProfileV10', 'serverHardwareUri': ENC_2 + ', bay 3',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC_2, 'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': ENC_2 + '_Bay3_Gen10_Quagmire2', 'description': 'Gen10_Win', 'affinity': 'Bay',
     'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
     'boot': {'manageBoot': True, 'order': ['HardDisk']},
     'connectionSettings': {
         'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         {'id': 2, 'name': '2', 'functionType': 'Ethernet', 'portId': 'Mezz 3:2-a',
                          'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                          'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-30',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         {'id': 4, 'name': '4', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                          'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-40',
                          'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                         ]}}
]

error_msg_patch_LI = 'The requested logical interconnect downlink speed of 25 Gb/s is less than the sum of all requested bandwidth settings for connections on the downlink ports associated with this logical interconnect.'

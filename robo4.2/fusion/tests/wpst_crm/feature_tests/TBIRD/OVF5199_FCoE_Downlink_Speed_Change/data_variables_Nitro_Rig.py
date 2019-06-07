from copy import deepcopy

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

ethernet_networks = [{'type': 'ethernet-networkV4', 'ethernetNetworkType': 'Tagged', 'name': 'eth_401', 'privateNetwork': False, 'purpose': 'General', 'smartLink': False, 'vlanId': 401}]

fcoe_networks = [{'name': 'fcoe-1002', 'type': 'fcoe-networkV4', 'vlanId': 1002},
                 {'name': 'fcoe-1004', 'type': 'fcoe-networkV4', 'vlanId': 1004}]


InterconnectMapTemplate_A = ''
InterconnectMapTemplate_B = ''
REDUNDANCY_A = ''
REDUNDANCY_B = ''
REDUNDANCY = ''
InterconnectMapTemplate = ''

ENC1 = 'MXQ81804ZF'
ENC2 = 'MXQ81804ZH'
ENC3 = 'MXQ81804ZG'
ENC4 = 'XXXXXXXXXX'
ENC5 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4, 'ENC:' + ENC5]

APPLIANCE_IP = '15.245.131.251'

frame = 3
IBS = 3
Config = 'HA'

ENC1ICBAY3 = 'MXQ81804ZF, interconnect 3'
ENCs = [ENC1, ENC2, ENC3]


###
# Interconnect bays configurations
# 1 Enclosures, Fabric 3
###

Enc1Map = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1}
    ]

Enc1MapASide = \
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
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50GB Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50GB Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]

Enc2MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50GB Interconnect Link Module', 'enclosureIndex': 2},
    ]

Enc2MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50GB Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2}
    ]


###
# Interconnect bays configurations
# 3 Enclosures, Fabric 3
###

Enc3bay3ICMMap = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]


Enc3MapASide = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 2},
        {'bay': 3, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
    ]

Enc3MapBSide = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 100Gb F32 Module for Synergy', 'enclosureIndex': 2},
        {'bay': 6, 'enclosure': 3, 'type': 'Synergy 50Gb Interconnect Link Module', 'enclosureIndex': 3}
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

if frame == 1:
    if Config == 'A':
        InterconnectMapTemplate_A = Enc1MapASide
        REDUNDANCY_A = 'NonRedundantASide'
    elif Config == 'B':
        InterconnectMapTemplate_A = Enc1MapBSide
        REDUNDANCY_B = 'NonRedundantBSide'
    elif Config == 'HA':
        REDUNDANCY = 'Redundant'
        InterconnectMapTemplate = Enc1Map
    elif Config == 'AB':
        InterconnectMapTemplate_A = Enc1MapASide
        InterconnectMapTemplate_B = Enc1MapBSide
        REDUNDANCY_A = 'RedundantASide'
        REDUNDANCY_B = 'RedundantBSide'
elif frame == 2:
    if Config == 'A':
        InterconnectMapTemplate_A = Enc2MapASide
        REDUNDANCY_A = 'NonRedundantASide'
    elif Config == 'B':
        InterconnectMapTemplate_A = Enc2MapBSide
        REDUNDANCY_B = 'NonRedundantBSide'
    elif Config == 'HA':
        REDUNDANCY = 'HighlyAvailable'
        InterconnectMapTemplate = Enc2Map
    elif Config == 'AB':
        InterconnectMapTemplate_A = Enc1MapASide
        InterconnectMapTemplate_B = Enc1MapBSide
        REDUNDANCY_A = 'RedundantASide'
        REDUNDANCY_B = 'RedundantBSide'
elif frame == 3:
    if Config == 'A':
        InterconnectMapTemplate_A = Enc3MapASide
        REDUNDANCY_A = 'NonRedundantASide'
    elif Config == 'B':
        InterconnectMapTemplate_A = Enc3MapBSide
        REDUNDANCY_B = 'NonRedundantBSide'
    elif Config == 'HA':
        REDUNDANCY = 'HighlyAvailable'
        InterconnectMapTemplate = Enc3bay3ICMMap
    elif Config == 'AB':
        InterconnectMapTemplate_A = Enc3MapASide
        InterconnectMapTemplate_B = Enc3MapBSide
        REDUNDANCY_A = 'NonRedundantASide'
        REDUNDANCY_B = 'NonRedundantBSide'

LIG = 'LIG' + '_' + REDUNDANCY
# LIG = 'LIG1'
EG = 'EG'
LE = 'LE'
LI = {'name': LE + '-' + LIG}


IC3_Enet_FcoE_uplink = 'Q5'
IC6_Enet_FcoE_uplink = 'Q5'
uplink_sets = {

    'US-FCoE1002': {
        'name': 'US-FCoE1002',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['eth_401', 'fcoe-1002'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'consistencyChecking': 'ExactMatch',  # Only applicable for OV version 5.00 and above
        'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': IC3_Enet_FcoE_uplink, 'speed': 'Auto'}
                                   ]
    },
    'US-FCoE1004': {
        'name': 'US-FCoE1004',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['fcoe-1004'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Short',
        'consistencyChecking': 'ExactMatch',  # Only applicable for OV version 5.00 and above
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': IC6_Enet_FcoE_uplink, 'speed': 'Auto'}
                                   ]
    }
}

ligs = {
    'LIG':
    {'name': LIG,
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': InterconnectMapTemplate,
     'enclosureIndexes': [x for x in xrange(1, frame + 1)],
     'interconnectBaySet': IBS,
     'redundancyType': REDUNDANCY,
     'uplinkSets': [deepcopy(uplink_sets['US-FCoE1002']), deepcopy(uplink_sets['US-FCoE1004'])],
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

Interconnect_name = [ENC2 + ', ' + 'interconnect 6', ENC1 + ', ' + 'interconnect 3']

Interconnect_dto = [{"name": Interconnect_name[0]}, {"name": Interconnect_name[1]}]

Uplink_ports = [[IC3_Enet_FcoE_uplink], [IC6_Enet_FcoE_uplink]]
downlink_port_Quack = [['d26'], ['d26']]
downlink_port_Quagmire2 = [['d27'], ['d27']]

SP_Quack = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': ENC3 + '_Bay2_Gen10_Quack', 'description': 'Gen10 Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1004',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}}
]

ilo_details_Quack = [{'ilo_ip': '15.245.133.7', 'username': 'Administrator', 'password': 'hpvse123'}]
server_credentials_Quack = [{'userName': 'Administrator', 'password': 'hpvse@1'}]

SP_Quagmire2 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 3',
                 'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:%s' % EG,
                 'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                 'name': ENC3 + '_Bay3_Gen10_Quagmire2', 'description': 'Gen10 Win', 'affinity': 'Bay',
                 'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                 'boot': {'manageBoot': True, 'order': ['HardDisk']},
                 'connectionSettings': {
                     'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                      'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                      'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '2500', 'networkUri': 'FCOE:fcoe-1004',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                     ]}}
                ]

ilo_details_Quagmire2 = [{'ilo_ip': '15.245.132.36', 'username': 'Administrator', 'password': 'hpvse123'}]
server_credentials_Quagmire2 = [{'userName': 'Administrator', 'password': 'hpvse@1'}]
ilo_details_all = [{'ilo_ip': '15.245.133.7', 'username': 'Administrator', 'password': 'hpvse123'},
                   {'ilo_ip': '15.245.132.36', 'username': 'Administrator', 'password': 'hpvse123'}]

server_details_all = [{'ip': '', 'userName': 'Administrator', 'password': 'hpvse@1', 'wcmd': ''},
                      {'ip': '', 'userName': 'Administrator', 'password': 'hpvse@1', 'wcmd': ''}]

kill_diskspd = "TASKKILL /F /IM diskspd.exe"

diskspd_cmd = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample1.dat"']

diskspd_cmds_30min = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample1.dat"',
                      'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d1800 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample2.dat"']
diskspd_cmds_1min = ['cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample1.dat"',
                     'cmd /c "C:\Users\Administrator\Desktop\Diskspd\diskspd.exe -c50M -d60 -r -w70 -t9 -o9 -b10K -h -L E:\sample.dat >C:\sample2.dat"']
SP_Quack_rbw16 = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': ENC3 + '_Bay2_Gen10_Quack', 'description': 'Gen10 Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '16000', 'networkUri': 'FCOE:fcoe-1004',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}}
]

SP_Quack_rbw8 = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 2',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': ENC3 + '_Bay2_Gen10_Quack', 'description': 'Gen10 Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-1004',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}}
]
Li_body_50GB = [{"op": "replace", "path": "/downlinkSpeedMode", "value": "SPEED_50GB"}]
Li_body_25GB = [{"op": "replace", "path": "/downlinkSpeedMode", "value": "SPEED_25GB"}]

SP_Quagmire2_rbw32 = [{'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 3',
                       'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:%s' % EG,
                       'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
                       'name': ENC3 + '_Bay3_Gen10_Quagmire2', 'description': 'Gen10 Win', 'affinity': 'Bay',
                       'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                       'boot': {'manageBoot': True, 'order': ['HardDisk']},
                       'connectionSettings': {
                           'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                            'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                           {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                            'requestedMbps': '32000', 'networkUri': 'FCOE:fcoe-1002',
                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                           {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                            'requestedMbps': '32000', 'networkUri': 'FCOE:fcoe-1004',
                                            'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                           ]}}
                      ]

SP_Quagmire2_rbw8 = [
    {'type': 'ServerProfileV11', 'serverHardwareUri': ENC3 + ', bay 3',
     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC3, 'enclosureGroupUri': 'EG:%s' % EG,
     'serialNumberType': 'Physical', 'macType': 'Physical', 'wwnType': 'Physical',
     'name': ENC3 + '_Bay3_Gen10_Quagmire2', 'description': 'Gen10 Win', 'affinity': 'Bay',
                    'bootMode': {'manageMode': True, 'mode': 'UEFI', 'pxeBootPolicy': 'Auto'},
                    'boot': {'manageBoot': True, 'order': ['HardDisk']},
                    'connectionSettings': {
                        'connections': [{'id': 1, 'name': '1', 'functionType': 'Ethernet', 'portId': 'Mezz 3:1-a',
                                         'requestedMbps': '2500', 'networkUri': 'ETH:eth_401',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 2, 'name': '2', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:1-b',
                                         'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-1002',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        {'id': 3, 'name': '3', 'functionType': 'FibreChannel', 'portId': 'Mezz 3:2-b',
                                         'requestedMbps': '8000', 'networkUri': 'FCOE:fcoe-1004',
                                         'boot': {'priority': 'NotBootable'}, 'mac': None, 'wwpn': '', 'wwnn': ''},
                                        ]}}
]

error_msg_patch_LI = 'The requested logical interconnect downlink speed of 25 Gb/s is less than the sum of all requested bandwidth settings for connections on the downlink ports associated with this logical interconnect.'

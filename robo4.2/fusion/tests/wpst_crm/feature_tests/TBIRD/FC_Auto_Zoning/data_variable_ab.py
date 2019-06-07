# Appliance Credentials
appliance_ip = '15.245.131.72'
admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

# Common SAN details

# SanManagerDetails

san_manager_details = {'connectionInfo': [{'name': 'Type', 'value': 'Brocade Network Advisor'},
                                          {'name': 'Host', 'value': '15.199.204.155'},
                                          {'name': 'Port', 'value': 5989},
                                          {'name': 'Username', 'value': 'Administrator'},
                                          {'name': 'Password', 'value': 'password'},
                                          {'name': 'UseSsl', 'value': True}]}

Storage_System_Cred = {"hostname": "15.245.128.151", "username": "3paruser", "password": "user@123", "family": "StoreServ"}

Storage_volume_data = {"properties": {"name": " ", "description": "",
                                      "storagePool": " ",
                                      "size": "", "provisioningType": "Thin", "isShareable": False,
                                      "snapshotPool": " "},
                       "templateUri": " ",
                       "isPermanent": True}

Volume_size = [21474836480, 26843545600]

Service_command = ['showcim', 'showwsapi']

#####################################################################
#                       Carbon Module variables
####################################################################
# values should be either 'Redundant' or 'NonRedundantASide' or 'NonRedundantBSide'
Enc_bay_type = {'enc1': 'Redundant'}

IC_bay_set = 1
IC_bay_set_pair = IC_bay_set + 3
enclosureCount = 1

Enclosure_Name = ['CN7545049F']
IC_model_name = "Virtual Connect SE 16Gb FC Module for Synergy"


Fc_body = {"name": "",
           "connectionTemplateUri": None,
           "linkStabilityTime": "30",
           "autoLoginRedistribution": True,
           "fabricType": "",
           "type": "fc-networkV4"}

icmap_Redundant = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries":
                                                                          [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                           {"type": "Enclosure", "relativeValue": -1}]},
                                                      "logicalDownlinkUri": None,
                                                      "permittedInterconnectTypeUri": "",
                                                      "enclosureIndex": -1},
                                                     {"logicalLocation": {"locationEntries":
                                                                          [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                           {"type": "Enclosure", "relativeValue": -1}]},
                                                      "logicalDownlinkUri": None,
                                                      "permittedInterconnectTypeUri": "",
                                                      "enclosureIndex": -1}]}

icmap_NonRedundantASide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries":
                                                                                  [{"type": "Bay", "relativeValue": IC_bay_set},
                                                                                   {"type": "Enclosure", "relativeValue": -1}]},
                                                              "logicalDownlinkUri": None,
                                                              "permittedInterconnectTypeUri": "",
                                                              "enclosureIndex": -1}]}

icmap_NonRedundantBSide = {"interconnectMapEntryTemplates": [{"logicalLocation": {"locationEntries":
                                                                                  [{"type": "Bay", "relativeValue": IC_bay_set_pair},
                                                                                   {"type": "Enclosure", "relativeValue": -1}]},
                                                              "logicalDownlinkUri": None,
                                                              "permittedInterconnectTypeUri": "",
                                                              "enclosureIndex": -1}]}

LIG_body = {"type": "logical-interconnect-groupV4",
            "ethernetSettings": None,
            "name": "",
            "telemetryConfiguration": None,
            "interconnectMapTemplate": "",
            "uplinkSets": [],
            "enclosureType": "SY12000",
            "enclosureIndexes": [-1],
            "interconnectBaySet": IC_bay_set,
            "redundancyType": "",
            "internalNetworkUris": [],
            "snmpConfiguration": None,
            "qosConfiguration": None}

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

les = [{'name': 'LE_1',
        'enclosureUris': [],
        'enclosureGroupUri': '',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

fcmodes = ['TRUNK', 'NONE']

US_details = [{'bay': IC_bay_set, 'Act_ports': ['1', '2'], 'rel_ports':['13', '14'], 'name':'us1'},
              {'bay': IC_bay_set_pair, 'Act_ports': ['1'], 'rel_ports':['13'], 'name':'us2'}]

desiredSpeeds = ['Auto', 'Speed4G', 'Speed8G', 'Speed16G']

logicalPortConfigInfos = [{"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}},
                          {"desiredSpeed": "", "logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": ""},
                                                                                       {"type": "Port", "relativeValue": ""},
                                                                                       {"type": "Enclosure", "relativeValue": -1}]}}]


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


server_profiles = [[{'type': 'ServerProfileV8', 'serverHardwareUri': Enclosure_Name[0] + ', bay 2',
                     'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + Enclosure_Name[0], 'enclosureGroupUri': ' ', 'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                     'name': 'PROFILE1', 'description': 'Server using SAN Storage', 'affinity': 'Bay',
                     'boot': {'manageBoot': False},
                     'bootMode': None,
                     'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                     'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2',
                                   'manageSanStorage': True,
                                   'volumeAttachments': [{'id': 1, 'volumeUri': '', 'lunType': 'Auto', 'lun': None,
                                                          'storagePaths': [{'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                                                                           {'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}],
                                                          'volumeStoragePoolUri':''}]},
                     'connections': [{'id': 1, 'name': 'Con_1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                      'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1'},
                                     {'id': 2, 'name': 'Con_2', 'functionType': 'FibreChannel', 'portId': 'Auto', 'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2'},
                                     ]}]
                   ]


################################################################################################
#                                Variables for Potash Hardware
# ##############################################################################################

##################################
# Interconnect bays configurations
# 2 or 3 Frames, IBS3, CL-20
##################################
REDUNDANCY = 'AB'
LIG_A = 'LIG-A'
LIG_B = 'LIG-B'
frame = 2
IBS = 3
IC3_LIG_ENET_UPLINK = 'Q4.1'
LIG_FA1_UPLINKS = ['Q3.1', 'Q4.2']
LIG_FA2_UPLINKS = ['Q3.1', 'Q5.1']
EG = 'EG' + '-' + REDUNDANCY
LE = 'LE' + '-' + REDUNDANCY
LI_A = LE + '-' + LIG_A
LI_B = LE + '-' + LIG_B
ENC1 = 'CN7544044G'
ENC2 = 'CN7545084V'
ENC3 = 'XXXXXXXXXX'
ENC4 = 'XXXXXXXXXX'
ENC_List = ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3, 'ENC:' + ENC4]

uplink_sets_in_lig = [
    {
        'name': 'US-FA1',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC_1'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': LIG_FA1_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '1', 'bay': '3', 'port': LIG_FA1_UPLINKS[1], 'speed': 'Auto'}
        ]
    },
    {
        'name': 'US-FA2',
        'ethernetNetworkType': 'NotApplicable',
        'networkType': 'FibreChannel',
        'networkUris': ['FC_2'],
        'lacpTimer': 'Short',
        'mode': 'Auto',
        'nativeNetworkUri': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': LIG_FA2_UPLINKS[0], 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': LIG_FA2_UPLINKS[1], 'speed': 'Auto'}
        ]
    }
]
# Map template for single frame
ICMP1_Aside = [
    {'bay': 3, 'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
]

ICMP1_Bside = [
    {'bay': 6, 'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1}
]
##############################
# Map template for two frame
################################
ICMP2_Aside = \
    [
        {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
        {'bay': 3, 'enclosure': 2, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 2}
    ]

ICMP2_Bside = \
    [
        {'bay': 6, 'enclosure': 1, 'type': 'Synergy 10Gb Interconnect Link Module', 'enclosureIndex': 1},
        {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2}
    ]
##############################
# Map template for three frame
#############################
ICMP3_Aside = [
    {'bay': 3, 'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2,
     'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3,
     'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}

]

ICMP3_Bside = [
    {'bay': 6, 'enclosure': 1,
     'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 3,
     'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3}
]

ligs = [{'name': LIG_A,
         'interconnectMapTemplate': ICMP2_Aside,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'NonRedundantASide',
         'uplinkSets': list(uplink_sets_in_lig_A)
         },
        {'name': LIG_B,
         'interconnectMapTemplate': ICMP2_Bside,
         'enclosureIndexes': [x for x in xrange(1, frame + 1)],
         'interconnectBaySet': IBS,
         'redundancyType': 'NonRedundantBSide',
         'uplinkSets': list(uplink_sets_in_lig_B),
         }]

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
         'ipAddressingMode': "External"
         }
}

LE_Potash = {
    'LE':
        {'name': LE,
         'enclosureUris': ENC_List[0:frame],
         'enclosureGroupUri': 'EG:' + EG,
         'firmwareBaselineUri': None,
         'forceInstallFirmware': False
         }
}

server_profiles_potash = [[{'type': 'ServerProfileV8', 'serverHardwareUri': ENC1 + ', bay 10',
                            'serverHardwareTypeUri': '', 'enclosureUri': 'ENC:' + ENC1, 'enclosureGroupUri': ' ',
                            'serialNumberType': 'Virtual', 'macType': 'Virtual', 'wwnType': 'Virtual',
                            'name': 'PROFILE1', 'description': 'Server using SAN Storage', 'affinity': 'Bay',
                            'boot': {'manageBoot': False},
                            'bootMode': None,
                            'localStorage': {'sasLogicalJBODs': [], 'controllers':[]},
                            'sanStorage':{'hostOSType': 'Windows 2012 / WS2012 R2',
                                          'manageSanStorage': True,
                                          'volumeAttachments': [{'id': 1, 'volumeUri': '', 'lunType': 'Auto', 'lun': None,
                                                                 'storagePaths': [{'isEnabled': True, 'connectionId': 1, 'targetSelector': 'Auto', 'targets': []},
                                                                                  {'isEnabled': True, 'connectionId': 2, 'targetSelector': 'Auto', 'targets': []}],
                                                                 'volumeStoragePoolUri':''}]},
                            'connections': [{'id': 1, 'name': 'Con_1', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                             'requestedMbps': 'Auto', 'networkUri': 'FC:FC_1'},
                                            {'id': 2, 'name': 'Con_2', 'functionType': 'FibreChannel', 'portId': 'Auto',
                                             'requestedMbps': 'Auto', 'networkUri': 'FC:FC_2'},
                                            ]}]
                          ]


#############################################################
#           IO Traffic
#############################################################
ilo_details = {'ilo_ip': '', 'username': 'Administrator', 'password': 'hpvse123'}

linux_details = {"hostip": "15.245.134.7", "username": "root", "password": "rootpwd", "dir_location": "/root/",
                 "python_cmd": "python2.7"}

server_details = {'username': 'Administrator', 'password': 'Hpvse@1'}

diskspd_cmd_60s = "PowerShell.exe -ExecutionPolicy Bypass -File .\\io_traffic.ps1"

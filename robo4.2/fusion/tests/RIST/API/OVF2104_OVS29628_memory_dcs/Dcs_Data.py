admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
cliq_credentials = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}

# Resource types for X-API-Version=1000
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FCOE_NETWORK_TYPE = 'fcoe-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
NETWORK_SET_TYPE = 'network-setV5'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV5'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV11'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'

# Enclosures
ENC1 = '0000A66101'
ENC2 = '0000A66102'
ENC3 = '0000A66103'

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1
ENC2DEBAY1 = '%s, bay 1' % ENC2
ENC3DEBAY1 = '%s, bay 1' % ENC3

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1  # sy660 Gen9
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1  # sy480 Gen9
ENC1SHBAY6 = '%s, bay 6' % ENC1  # sy660 Gen10
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY11 = '%s, bay 11' % ENC1  # sy480 Gen10
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY4 = '%s, bay 4' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY8 = '%s, bay 8' % ENC2
ENC2SHBAY11 = '%s, bay 11' % ENC2
ENC3SHBAY3 = '%s, bay 3' % ENC3
ENC3SHBAY4 = '%s, bay 4' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3
ENC3SHBAY6 = '%s, bay 6' % ENC3
ENC3SHBAY7 = '%s, bay 7' % ENC3
ENC3SHBAY8 = '%s, bay 8' % ENC3
ENC3SHBAY11 = '%s, bay 11' % ENC3

enclosures = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, },
    {"type": ENCLOSURE_TYPE, "name": ENC2, },
    {"type": ENCLOSURE_TYPE, "name": ENC3, },
]
enc1_sy480 = {"server": ENC1SHBAY11,
              "username": "Administrator",
              "password": "hpvse123",
              "path": "/dcs/rest/passThrough/", }
enc1_sy660 = {"server": ENC1SHBAY6,
              "username": "Administrator",
              "password": "hpvse123",
              "path": "/dcs/rest/passThrough/", }
ris_node3 = {"server": ENC2SHBAY11,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node4 = {"server": ENC2SHBAY6,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node5 = {"server": ENC3SHBAY11,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }
ris_node6 = {"server": ENC3SHBAY6,
             "username": "Administrator",
             "password": "hpvse123",
             "path": "/redfish/v1/Systems/1/Memory/", }

ris_nodes = [enc1_sy480, enc1_sy660, ris_node3, ris_node4, ris_node5, ris_node6]

ris_nodes_in_profiles = [enc1_sy660]

licenses = {'licenseType': 'HPE OneView Advanced',
            'license': [{'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'}]}
sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, },
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1, },
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4, },
]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC2ICBAY6, },
]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': 'ethernet-networkV4',
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]
fc_networks = [
    {'name': 'FA1',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': ''},
    {'name': 'FA2',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': ''},
]
network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100'],
                 'nativeNetworkUri': 'net100'},
                ]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': 'Synergy 20Gb Interconnect Link Module', 'enclosureIndex': 3},
]

uplink_sets = {'us_untagged': {'name': 'us-untagged',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['network-untagged'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          ]
                               },
               'us_tagged': {'name': 'us-tagged',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['net100', 'net300'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        ]
                             },
               'us_tunnel': {'name': 'us-tunnel',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['network-tunnel'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        ]
                             },
               }

ligs = [{'name': LIG_NAME,
         'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
         'enclosureType': 'SY12000',
         'interconnectMapTemplate': icmap,
         'enclosureIndexes': [1, 2, 3],
         'interconnectBaySet': 3,
         'redundancyType': 'HighlyAvailable',
         'fcoeSettings': {'fcoeMode': 'FcfNpv'},
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None,
         'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(), uplink_sets['us_tunnel'].copy(), ],
         }
        ]
sasligs = [{"name": 'SASLIG1',  # Dual SAS switch
            "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'}]}
           ]

egs = [{'name': 'EG1',
        'enclosureCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
        [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
         {"interconnectBay": 4, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
         {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
         {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}
         ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]

les = [{'name': 'LE1',
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': 'EG:EG1',
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}
       ]

# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3

# Sas Interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

gen10_server_profiles = [
    {
        "type": SERVER_PROFILE_TYPE,
        "serverHardwareUri": "SH:" + ENC1SHBAY6,
        "serverHardwareTypeUri": "SHT:SY 660 Gen10:1:HPE Smart Array P416ie-m SR Gen10 Controller:2:HPE Synergy 3830C 16G Fibre Channel Host Bus Adapter:3:HPE Synergy 3820C 10/20Gb Converged Network Adapter:4:HPE Smart Array P416ie-m SR Gen10 Controller",
        "enclosureGroupUri": "EG:" + EG_NAME,
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": ENC1SHBAY6,
        "description": "",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [{
                "id": 1,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:net100",
                "requestedVFs": "0",
                "ipv4": {},
            }, {
                "id": 2,
                "name": "",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:net300",
                "requestedVFs": "0",
                "ipv4": {},
            }]
        },
        "boot": {
            "manageBoot": True,
            "order": ["CD", "USB", "HardDisk", "PXE"]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "BIOS"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None,
            "firmwareScheduleDateTime": "",
            "firmwareActivationType": "Immediate"
        },
        "bios": {
            "manageBios": True,
            "overriddenSettings": [{
                "id": "CustomPostMessage",
                "value": "Harrier"
            }]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {"sasLogicalJBODs": [], "controllers": []},
        "sanStorage": None
    }, ]

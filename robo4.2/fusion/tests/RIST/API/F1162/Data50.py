"""
F1162 - SW iSCSI with User Specified Initiator for Server Profile Templates
"""
# pylint: disable=E0401,E0602
from dto import *
from env_variables import *

appliance = {
    "type": APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    "applianceNetworks": [
        {
            "activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.210.227", "app1Ipv6Addr": "",
            "app2Ipv4Addr": "16.114.210.228", "app2Ipv6Addr": "",
            "virtIpv4Addr": "16.114.209.223", "virtIpv6Addr": None, "app1Ipv4Alias": None, "app1Ipv6Alias": None,
            "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": "wpst-tbird-15-oneview.vse.rdlabs.hpecorp.net",
            "confOneNode": True, "interfaceName": "", "macAddress": None,
            "ipv4Type": "STATIC", "ipv6Type": "UNCONFIGURE", "overrideIpv4DhcpDnsServers": False,
            "ipv4Subnet": "255.255.240.0", "ipv4Gateway": "16.114.208.1", "ipv6Subnet": None, "ipv6Gateway": None,
            "domainName": "vse.rdlabs.hpecorp.net", "searchDomains": [],
            "ipv4NameServers": ["16.125.25.81", "16.125.25.82"],
            "ipv6NameServers": ["16.125.25.81", "16.125.25.82"], "bondedTo": None, "aliasDisabled": True,
            "configureRabbitMqSslListener": False, "configurePostgresSslListener": False, "webServerCertificate": None,
            "webServerCertificateChain": None, "webServerCertificateKey": None
        }
    ],
    "serverCertificate": {
        "rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
        "rabbitMQCertificateKey": None, "postgresCertificate": None,
        "postgresRootCACertificate": None, "postgresCertificateKey": None
    }
}

timeandlocale = {
    'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
    'locale': 'en_US.UTF-8'
}

users = [
    {
        'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin',
        'roles': ['Server administrator'],
        'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin',
        'roles': ['Network administrator'],
        'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin',
        'roles': ['Backup administrator'],
        'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'],
        'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    }
]

licenses = [
    {
        'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J '
               'EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP '
               'XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 '
               'HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'
    },
    {
        'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J '
               '4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP '
               'XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 '
               'HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'
    },
    {
        'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J '
               'TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP '
               'XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 '
               'HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
    {
        'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J '
               'TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP '
               'XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 '
               'HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'
    },
    {
        'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J '
               'VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP '
               'XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 '
               'HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'
    },
    {
        'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J '
               'FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP '
               'XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 '
               'HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
]

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY3 = '%s, bay 3' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

enclosures = [
    {"type": ENCLOSURE_TYPE_400, "name": ENC1, },
    {"type": ENCLOSURE_TYPE_400, "name": ENC2, },
    {"type": ENCLOSURE_TYPE_400, "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, },
    {"name": ENC1SASICBAY4, }
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1}
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4}
]

ics = [
    {"name": ENC1ICBAY3},
    {"name": ENC2ICBAY6}
]

ethernet_networks = [
    {
        'name': 'network-iSCSI',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 1,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Untagged'
    },
    {
        'name': 'net100',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 100,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'
    },
    {
        'name': 'net300',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 300,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'
    }, ]

network_sets = [{'name': 'NS1', 'type': NETWORK_SET_TYPE, 'networkUris': ['net100'], 'nativeNetworkUri': 'net100'}, ]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': POTASH, 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 2, 'type': POTASH, 'enclosureIndex': 2},
    {'bay': 6, 'enclosure': 1, 'type': CHLORIDE20, 'enclosureIndex': 1},
    {'bay': 3, 'enclosure': 2, 'type': CHLORIDE20, 'enclosureIndex': 2},
    {'bay': 3, 'enclosure': 3, 'type': CHLORIDE20, 'enclosureIndex': 3},
    {'bay': 6, 'enclosure': 3, 'type': CHLORIDE20, 'enclosureIndex': 3},
]

uplink_sets = {
    'us_untagged': {
        'name': 'us_untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-iSCSI'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{
            'enclosure': '1', 'bay': '3',
            'port': 'Q1.1', 'speed': 'Auto'
        }, ]
    },
    'us_tagged': {
        'name': 'us_tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net100', 'net300'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [{'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'}, ]
    },
}

ligs = [{
    'name': 'LIG1',
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
    'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(), ],
}]

sasligs = [{
    'name': 'SASLIG1',  # Single SAS switch
    "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
    "enclosureType": "SY12000",
    "enclosureIndexes": [1],
    "interconnectBaySet": "1",
    'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': NATASHA}]
}]

egs = [{
    'name': 'EG1',
    'type': ENCLOSURE_GROUP_TYPE_300,
    'enclosureCount': 3,
    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
    'stackingMode': 'Enclosure',
    'interconnectBayMappingCount': 2,
    'configurationScript': None,
    'interconnectBayMappings':
        [{"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
         {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}],
    'ipAddressingMode': "External",
    'ipRangeUris': [],
    'powerMode': "RedundantPowerFeed"
}]

edit_egs = [{
    'name': 'EG1',
    'type': ENCLOSURE_GROUP_TYPE_300,
    'enclosureCount': 3,
    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
    'stackingMode': 'Enclosure',
    'interconnectBayMappingCount': 3,
    'configurationScript': None,
    'interconnectBayMappings':
        [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
         {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:LIG1"},
         {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:LIG1"}],
    'ipAddressingMode': "External",
    'ipRangeUris': [],
    'powerMode': "RedundantPowerFeed"
}]

les = [{
    'name': 'LE1',
    'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
    'enclosureGroupUri': 'EG:EG1',
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}]

# Verify Create Server Profile Template
# iSCSI primary only
spt_1 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'spt1_primary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': '192.168.21.72',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '192.168.22.73',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

spt_1_edit = [{
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'spt1_primary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': '192.168.21.72',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '192.168.22.73',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'None'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}]
# iSCSI primary and secondary
spt_2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'spt2_primary_secondary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': '192.168.21.72',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '192.168.22.73',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary only UEFI optimized
spt_3 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'spt3_primary_uefioptimized',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary and secondary UEFI optimized
spt_4 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'spt4_primary_secondary_uefioptimized',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'chapLevel': 'Chap'
                }
            }
        }, {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI primary and secondary UEFI optimized
spt_5 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'spt5_primary_secondary_no_chap',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'chapLevel': 'None'
                }
            }
        }, {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:2-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'chapLevel': 'None'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFIOptimized',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {

        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

sp = [{
    'type': SERVER_PROFILE_TYPE,
    'name': 'sp1',
    'serverProfileTemplateUri': 'SPT:spt1_primary',
    'serverHardwareUri': ENC2SHBAY1,
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Mezz 3:1-a',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1',
                'ipAddress': '192.168.22.88',
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorName': 'iqn.2015-02.com.hpe:oneview-0c005d02-dca6-43a7-96f2-f3491a4acee',
                    'firstBootTargetIp': '192.168.21.72',
                    'bootTargetName': 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:84:tbird8-bay6-vol1',
                    'bootTargetLun': '0',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '192.168.22.73',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'None'
                }
            }
        }, ]
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}]

sp_pre_compliance = {
    "name": "sp1",
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        # need REGEX due to 3:1 which will cause fusion_api_validate_response_follow to think it is a GET lookup
        # also need to change 3:1 3.1 as fusion_api_validate_response_follow splits on ':'
        # also need to escap ( and ) or taken as "match" value
        "manualUpdates": [
            "REGEX:Change iSCSI authentication of connection \d on port Mezzanine \\(Mezz\\) \d:\d-a to CHAP\\."
        ]
    }
}

sp_post_compliance = {
    "name": "sp1",
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_Enable_Chap = {
    "type": SERVER_PROFILE_TYPE,
    "serverHardwareUri": "SH:" + ENC2SHBAY1,
    "enclosureUri": "ENC:" + ENC2,
    "serverProfileTemplateUri": "SPT:spt1_primary",
    "enclosureGroupUri": "EG:EG1",
    "serialNumberType": "Virtual",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "sp1",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [{
            "id": 1, "name": "",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1-a",
            "requestedMbps": "2500",
            "networkUri": 'ETH:net100',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "ipAddress": "192.168.22.88",
                "subnetMask": "255.255.192.0",
                "gateway": "192.168.1.1"
            },
            "boot": {
                "ethernetBootType": "iSCSI",
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    "initiatorNameSource": "UserDefined",
                    "initiatorName": "f1162-initiator",
                    "bootTargetName": "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:84:tbird8-bay6-vol1",
                    "bootTargetLun": "0",
                    "firstBootTargetIp": "192.168.21.72",
                    "firstBootTargetPort": "3260",
                    "secondBootTargetIp": "192.168.22.73",
                    "secondBootTargetPort": "3260",
                    "chapLevel": "Chap",
                    "chapName": "F1162",
                    "chapSecret": "F1162_Secret",
                    "mutualChapName": "",
                    "mutualChapSecret": None
                }
            }
        }]
    },
    "boot": {"manageBoot": True, "order": ["HardDisk"]},
    "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False, "firmwareBaselineUri": None,
        "forceInstallFirmware": False, "firmwareInstallType": None
    },
    "bios": {"manageBios": False, "overriddenSettings": []},
    "hideUnusedFlexNics": True,
    "localStorage": {"sasLogicalJBODs": [], "controllers": []},
    "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
}

# Verify Network Sets are NOT Supported during Create Server Profile
# Template with iSCSI SW Boot
negative_spt1 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'negative_spt_1',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'NS:NS1',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Network Sets are NOT Supported during Create Server Profile
# Template with iSCSI SW Boot
negative_spt2 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'negative_spt_2',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'NS:NS1',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Cannot Create Server Profile Template with only iSCSI Secondary
# Boot Mode
negative_spt3 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'negative_spt_3',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Cannot Create Server Profile Template with multiple primary or
# secondary
negative_spt4 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'negative_spt_4',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Cannot Create Server Profile Template with multiple primary or
# secondary
negative_spt5 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'negative_spt_5',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# Verify Required Fields
negative_spt6 = {
    'type': SERVER_PROFILE_TEMPLATE_TYPE,
    'name': 'negative_spt_6',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9:1:Synergy 3830C 16G FC HBA:3:HP Synergy 3820C 10/20Gb CNA',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    'connectionSettings': {
        'connections': [{
            'id': 1,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Primary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, {
            'id': 2,
            'functionType': 'Ethernet',
            'portId': 'Auto',
            'requestedMbps': 2500,
            'networkUri': 'ETH:net100',
            'ipv4': {
                'ipAddressSource': 'UserDefined',
                'subnetMask': '255.255.192.0',
                'gateway': '192.168.1.1'
            },
            'boot': {
                'priority': 'Secondary',
                'bootVolumeSource': 'UserDefined',
                'ethernetBootType': 'iSCSI',
                'iscsi': {
                    'initiatorNameSource': 'UserDefined',
                    'initiatorVlanId': 1,
                    'firstBootTargetIp': '',
                    'firstBootTargetPort': '3260',
                    'secondBootTargetIp': '',
                    'secondBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }
        }, ], 'manageConnections': True
    },
    'bootMode': {
        'manageMode': True,
        'mode': 'UEFI',
        'pxeBootPolicy': 'Auto'
    },
    'boot': {
        'manageBoot': True,
        'order': [
            'HardDisk'
        ]
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_ethernet'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_ethernet'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Boot_initiator_subnet_required'
    },
    {
        'keyword': 'Fusion Api Delete Server Profile Template',
        'argument': 'spt1_primary',
        'taskState': 'Error',
        'errorMessage': 'Referenced_by_server_profile'
    },
]

create_profile_templates = [
    spt_1.copy(),
    spt_2.copy(),
    spt_3.copy(),
    spt_4.copy(),
    spt_5.copy(),
]

delete_profile_templates = [
    'spt1_primary',
    'spt2_primary_secondary',
    'spt3_primary_uefioptimized',
    'spt4_primary_secondary_uefioptimized',
    'spt5_primary_secondary_no_chap',
]

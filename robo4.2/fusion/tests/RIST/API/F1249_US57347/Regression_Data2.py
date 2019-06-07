admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
server_credentials = {'userName': 'Serveradmin', 'password': 'wpsthpvse1'}
network_credentials = {'userName': 'Networkadmin', 'password': 'wpsthpvse1'}
ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}
hpmctp_credentials = {'ip': '16.114.218.103', 'username': 'root', 'password': 'hpvse1'}

cliq_credentials_173 = {'mgmt_ip': '16.71.149.173', 'username': 'admin', 'password': 'admin'}
cliq_credentials_116 = {'mgmt_ip': '16.71.148.116', 'username': 'admin', 'password': 'admin'}

# LIG, SASLIG, AND LE
LIG_NAME = 'LIG1'
SASLIG_NAME = 'SASLIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Enclosures
ENC1 = 'CN75120D7B'
ENC2 = 'CN75120D77'
ENC3 = 'CN75120D77'

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
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
VSA_116_BOOT_TARGET_IP = "192.168.21.59"
VSA_116_BOOT_TARGET_PORT = "3260"
VSA_173_BOOT_TARGET_IP = "192.168.21.71"
VSA_173_BOOT_TARGET_PORT = "3260"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

# Storage
STOREVIRTUAL1_NAME = "VSA_Cluster_116"
STOREVIRTUAL2_NAME = "VSA_Cluster_173-2"

STOREVIRTUAL1_POOL = "VSA_Cluster_116"
STOREVIRTUAL2_POOL = "VSA_Cluster_173-2"

VSA_Cluster_116 = "VSA_Cluster_116"
VSA_Cluster_173_2 = "VSA_Cluster_173-2"

# PROFILE1: profile on Enc1 bay7, Blackbird
PROFILE1_NAME = "tbird14-bay7-profile"
PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:258:tbird14-bay7-dhcp'
PROFILE1_DEFAULT_INITIATOR_NAME = 'iqn.1986-03.com.hp:uefi-i37-cn7446069m'
PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird14-bay7"
PROFILE1_INITIATOR_IP_1 = "192.168.22.49"
PROFILE1_INITIATOR_IP_2 = "192.168.22.58"
PROFILE1_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:258:tbird8-bay1-dhcp_attempt_1"
PROFILE1_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol_attempt_2"
PROFILE1_CHAP_NAME = 'tbird14-bay7'
PROFILE1_MCHAP_NAME = 'tbird14-bay7'

# PROFILE2: profile on Enc2 bay1, blackbird
PROFILE2_VOLUME_NAME = "tbird17-bay1-dhcp"
PROFILE2_NAME = "tbird17-bay1-profile"
PROFILE2_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:552:tbird17-bay1-dhcp"
PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-vcguhbt003"
PROFILE2_INITIATOR_IP_1 = "192.168.22.52"
PROFILE2_INITIATOR_IP_2 = "192.168.22.57"
PROFILE2_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:552:tbird17-bay1-dhcp_attempt_1"
PROFILE2_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird17-bay1-bootvol_attempt_2"
PROFILE2_CHAP_NAME = 'tbird17-bay1'
PROFILE2_MCHAP_NAME = 'tbird17-bay1'

# PROFILE3: Enc 3 bay1 profile,  blackbird
PROFILE3_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:613:tbird18-bay1-sles"
PROFILE3_INITIATOR_NAME = "iqn.1986-03.hp:uefi-tbird18-bay1-iscsiboot"
PROFILE3_INITIATOR_IP_1 = "192.168.22.58"
PROFILE3_INITIATOR_IP_2 = "192.168.22.59"
PROFILE3_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird18-bay1-bootvol_attempt_1"
PROFILE3_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird18-bay1-bootvol_attempt_2"
PROFILE3_CHAP_NAME = 'tbird18-bay1'
PROFILE3_MCHAP_NAME = 'tbird18-bay1'
profile3 = 'tbird18_bay1-SP-hw-iscsi-SpecifyBootTarget-UserSpecified'

# PROFILE4: Enc1 bay5 profile Red bird
PROFILE4_VOL1_TARGET = "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:301:tbird14-bay5-hw-iscsi-managedvol-dhcp-vol"
PROFILE4_VOL2_TARGET = "iqn.2003-10.com.lefthandnetworks:vsa-mg-116:521:tbird14-bay5-hw-iscsi-managedvol-dhcp-newvol"
PROFILE4_INITIATOR_IP = "192.168.22.50"
PROFILE4_Existing_vol = "tbird14-bay5-hw-iscsi-ManagedVol-DHCP-Vol"


existing_volumes = [
    {
        "storageSystemUri": STOREVIRTUAL1_NAME,
        "name": PROFILE4_Existing_vol,
        "deviceVolumeName": PROFILE4_Existing_vol,
        "isShareable": True,
    }]

enclosures = [
    {"type": "EnclosureV400", "name": ENC1, },
    {"type": "EnclosureV400", "name": ENC2, },
    {"type": "EnclosureV400", "name": ENC3, },
]

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
     'type': 'ethernet-networkV4',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': 'ethernet-networkV4',
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': 'ethernet-networkV4',
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

network_sets = [{'name': 'NS1', 'type': 'network-setV4 ', 'networkUris': ['net100'], 'nativeNetworkUri': 'net100'}, ]

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
         'type': 'logical-interconnect-groupV4',
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
            "type": "sas-logical-interconnect-group",
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'},
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'}]}
           ]

egs = [{'name': 'EG1',
        'type': 'EnclosureGroupV300',
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 3,
        'configurationScript': None,
        'interconnectBayMappings':
        [{"interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:SASLIG1"},
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

# Enclosures
ENC1 = 'CN754406XL'
ENC2 = 'CN754404R6'
ENC3 = 'CN754406WB'

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

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

profile_templates = [
    {"type": "ServerProfileTemplateV6",
     "serverProfileDescription": "SPT-sw-iscsi-SpecifyBootTarget-DHCP",
     "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
     "enclosureGroupUri": "EG:EG1",
     "serialNumberType": "Virtual",
     "macType": "Virtual",
     "wwnType": "Virtual",
     "name": "SPT-sw-iscsi-SpecifyBootTarget-DHCP",
     "description": "SPT-sw-iscsi-SpecifyBootTarget-DHCP",
     "affinity": "Bay",
     "connectionSettings": {
         "manageConnections": True,
         "connections": [{
             "id": 1,
             "name": "1",
             "functionType": "Ethernet",
             "portId": "Auto",
             "requestedMbps": "2500",
             "networkUri": "ETH:network-untagged",
             "requestedVFs": "0",
             "ipv4": {
                 "ipAddressSource": "DHCP",
                 "subnetMask": "",
                 "gateway": ""
             },
             "boot": {
                 "priority": "Primary",
                 "ethernetBootType": "iSCSI",
                 "bootVolumeSource": "UserDefined",
                 "iscsi": {
                     "initiatorNameSource": "UserDefined",
                     "initiatorVlanId": "",
                     "firstBootTargetIp": VSA_116_BOOT_TARGET_IP,
                     "firstBootTargetPort": VSA_116_BOOT_TARGET_PORT,
                     "secondBootTargetIp": "",
                     "secondBootTargetPort": "",
                     "chapLevel": "Chap"
                 }
             }
         }
         ]},
     "boot": {"manageBoot": True, "order": ["HardDisk"]},
     "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
     "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                  "forceInstallFirmware": False, "firmwareInstallType": None},
     "bios": {"manageBios": False, "overriddenSettings": []},
     "hideUnusedFlexNics": True,
     "iscsiInitiatorNameType": "AutoGenerated",
     "localStorage": {"sasLogicalJBODs": [], "controllers": []},
     "sanStorage": None
     },
    {
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "SPT-sw-iscsi-ManagedVol-DHCP",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "SPT-sw-iscsi-ManagedVol-DHCP",
        "description": "SPT-sw-iscsi-ManagedVol-DHCP",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [{
                "id": 1,
                "name": "1",
                "functionType": "Ethernet",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "requestedVFs": "0",
                "ipv4": {
                    "ipAddressSource": "DHCP",
                    "subnetMask": "",
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": None
                    #        "iscsi": {
                    #            "initiatorNameSource": "ProfileInitiatorName",
                    #            "initiatorVlanId": "",
                    #            "firstBootTargetIp": "",
                    #            "firstBootTargetPort": "",
                    #            "secondBootTargetIp": "",
                    #            "secondBootTargetPort": "",
                    #            "chapLevel": None
                    #        }
                }
            }
            ]},
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "tbird17-bay1-dhcp",
                        "description": "",
                        "storagePool": "StoragePoolV2:VSA_Cluster_116",
                        "size": 2147483648,
                                "provisioningType": "Thin",
                                "isShareable": False,
                                "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "StorageSystemV3:VSA_Cluster_116",
                "volumeUri": None,
            }]
        }
    },
    {
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
        "description": "SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [{
                "id": 1,
                "name": "1",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": VSA_173_BOOT_TARGET_IP,
                        "firstBootTargetPort": VSA_173_BOOT_TARGET_PORT,
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap"
                    }
                }
            },
                {
                "id": 2,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": VSA_173_BOOT_TARGET_IP,
                        "firstBootTargetPort": VSA_173_BOOT_TARGET_PORT,
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap"
                    }
                }
            }
            ]},
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "UserDefined",
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": None
    },
    {
        "type": "ServerProfileTemplateV6",
        "serverProfileDescription": "SPT-hw-iscsi-ManagedVol-DHCP",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "SPT-hw-iscsi-ManagedVol-DHCP",
        "description": "SPT-hw-iscsi-ManagedVol-DHCP",
        "affinity": "Bay",
        "connectionSettings": {
            "manageConnections": True,
            "connections": [{
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "DHCP",
                    "subnetMask": "",
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": None,
                    #        "iscsi": {
                    #           "initiatorNameSource": "ProfileInitiatorName",
                    #            "initiatorVlanId": "",
                    #            "firstBootTargetIp": "",
                    #            "firstBootTargetPort": "",
                    #            "secondBootTargetIp": "",
                    #            "secondBootTargetPort": "",
                    #            "chapLevel": None
                    #        }
                }
            }
            ]},
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorNameType": "AutoGenerated",
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "StorageVolumeV3:tbird14-bay5-hw-iscsi-ManagedVol-DHCP-Vol",
            }, {
                "id": 2,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "tbird14-bay5-hw-iscsi-ManagedVol-DHCP-NewVol",
                        "description": "",
                        "storagePool": "StoragePoolV2:VSA_Cluster_116",
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "StorageSystemV3:VSA_Cluster_116",
                "volumeUri": None,
            }]

        }
    }
]

server_profiles = [
    {
        "type": "ServerProfileV10",
        "serverHardwareUri": 'SH:' + ENC1 + ', bay 7',
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "Tbird14-bay7-SP-sw-iscsi-SpecifyBootTarget-DHCP",
        "description": "Tbird14-bay7-sw-iscsi-SpecifyBootTarget-DHCP",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "1",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:network-untagged",
                    "mac": None,
                    "wwpn": None,
                    "wwnn": None,
                    "requestedVFs": "0",
                    "ipv4": {
                        "ipAddressSource": "DHCP",
                        "subnetMask": "",
                        "gateway": "",
                        "ipAddress": ""
                    },
                    "boot": {
                        "priority": "Primary",
                        "ethernetBootType": "iSCSI",
                        "bootVolumeSource": "UserDefined",
                        "iscsi": {
                            "initiatorNameSource": "UserDefined",
                            "firstBootTargetIp": VSA_116_BOOT_TARGET_IP,
                            "firstBootTargetPort": VSA_116_BOOT_TARGET_PORT,
                            "secondBootTargetIp": "",
                            "secondBootTargetPort": "",
                            "chapLevel": "Chap",
                            "initiatorName": PROFILE1_INITIATOR_NAME,
                            "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                            "bootTargetLun": "0",
                            "chapName": PROFILE1_CHAP_NAME,
                            "chapSecret": CHAP_SECRET,
                            "mutualChapName": "",
                            "mutualChapSecret": None
                        }
                    }
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {"sasLogicalJBODs": [], "controllers": []},
        "sanStorage": None
    },
    {
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:" + ENC2 + ", bay 1",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "Tbird17-bay1-SP-sw-iscsi-ManagedVol-DHCP",
        "description": "Tbird17-bay1-SP-sw-iscsi-ManagedVol-DHCP",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "1",
                    "functionType": "Ethernet",
                    "portId": "Mezz 3:1-a",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:network-untagged",
                    "requestedVFs": "0",
                    "ipv4": {
                        "ipAddressSource": "DHCP",
                        "subnetMask": "",
                        "gateway": ""
                    },
                    "boot": {
                        "priority": "Primary",
                        "ethernetBootType": "iSCSI",
                        "bootVolumeSource": "ManagedVolume",
                        "iscsi": None,
                    }
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFIOptimized",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": PROFILE2_VOLUME_NAME,
                        "storagePool": "SPOOL:VSA_Cluster_116",
                        "size": 2147483648,
                        "provisioningType": "THIN",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
                "volumeUri": None,
            }]
        }
    },
    {
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:" + ENC3 + ", bay 1",
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "UserDefined",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "tbird18-bay1-SP-hw-iscsi-SpecifyBootTarget-UserSpecified",
        "description": "tbird18-bay1-SP-hw-iscsi-SpecifyBootTarget-UserSpecified",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "1",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:network-untagged",
                    "mac": None,
                    "wwpn": None,
                    "wwnn": None,
                    "ipv4": {
                        "ipAddressSource": "UserDefined",
                        "subnetMask": INITIATOR_SUBNET_MASK,
                        "gateway": INITIATOR_GATEWAY,
                        "ipAddress": PROFILE3_INITIATOR_IP_1
                    },
                    "boot": {
                        "priority": "Primary",
                        "bootVolumeSource": "UserDefined",
                        "iscsi": {
                            "initiatorNameSource": "UserDefined",
                            "firstBootTargetIp": VSA_173_BOOT_TARGET_IP,
                            "firstBootTargetPort": VSA_173_BOOT_TARGET_PORT,
                            "secondBootTargetIp": "",
                            "secondBootTargetPort": "",
                            "chapLevel": "MutualChap",
                            "initiatorName": PROFILE3_INITIATOR_NAME,
                            "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                            "bootTargetLun": "0",
                            "chapName": PROFILE3_CHAP_NAME,
                            "chapSecret": CHAP_SECRET,
                            "mutualChapName": PROFILE3_MCHAP_NAME,
                            "mutualChapSecret": MCHAP_SECRET
                        }
                    }
                },
                {
                    "id": 2,
                    "name": "",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:2-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:network-untagged",
                    "mac": None,
                    "wwpn": None,
                    "wwnn": None,
                    "ipv4": {
                        "ipAddressSource": "UserDefined",
                        "subnetMask": INITIATOR_SUBNET_MASK,
                        "gateway": INITIATOR_GATEWAY,
                        "ipAddress": PROFILE3_INITIATOR_IP_2
                    },
                    "boot": {
                        "priority": "Secondary",
                        "bootVolumeSource": "UserDefined",
                        "iscsi": {
                            "initiatorNameSource": "UserDefined",
                            "firstBootTargetIp": VSA_173_BOOT_TARGET_IP,
                            "firstBootTargetPort": VSA_173_BOOT_TARGET_PORT,
                            "secondBootTargetIp": "",
                            "secondBootTargetPort": "",
                            "chapLevel": "MutualChap",
                            "initiatorName": PROFILE3_INITIATOR_NAME,
                            "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                            "bootTargetLun": "0",
                            "chapName": PROFILE3_CHAP_NAME,
                            "chapSecret": CHAP_SECRET,
                            "mutualChapName": PROFILE3_MCHAP_NAME,
                            "mutualChapSecret": MCHAP_SECRET
                        }
                    }
                }
            ]
        },
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": None
    },
    {
        "type": "ServerProfileV10",
        "serverHardwareUri": "SH:" + ENC1 + ", bay 5",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
        "description": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
        "affinity": "Bay",
        "connectionSettings": {
            "connections": [
                {
                    "id": 1,
                    "name": "",
                    "functionType": "iSCSI",
                    "portId": "Mezz 3:1-b",
                    "requestedMbps": "2500",
                    "networkUri": "ETH:network-untagged",
                    "ipv4": {
                        "ipAddressSource": "DHCP",
                        "subnetMask": "",
                        "gateway": ""
                    },
                    "boot": {
                        "priority": "Primary",
                        "bootVolumeSource": "ManagedVolume",
                        "iscsi": None,
                        #        "iscsi": {
                        #            "initiatorNameSource": "ProfileInitiatorName",
                        #            "firstBootTargetIp": "",
                        #            "firstBootTargetPort": "",
                        #            "secondBootTargetIp": "",
                        #            "secondBootTargetPort": "",
                        #            "chapLevel": None,
                        #            "initiatorName": "",
                        #            "bootTargetName": "",
                        #            "bootTargetLun": "",
                        #            "chapName": "",
                        #            "chapSecret": None,
                        #            "mutualChapName": "",
                        #            "mutualChapSecret": None
                        #        }
                    }
                }
            ]
        },
        "boot": {"manageBoot": True, "order": ["HardDisk"]},
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-Vol",
            }, {
                "id": 2,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-NewVol",
                        "storagePool": "StoragePoolV2:VSA_Cluster_116",
                        "size": 1073741824,
                        "provisioningType": "THIN",
                                "isShareable": False,
                                "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "StorageSystemV3:VSA_Cluster_116",
                "volumeUri": None,
            }]
        }
    }
]

# ris check for DHCP setting
sw_iscsi_ris = [{
    "server": ENC1SHBAY7,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/iSCSI",
    "validate":{
        "Description": "This is the Server iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE1_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": "",
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": "",
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": "",
                "iSCSIReverseChapUsername": "",
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": VSA_116_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE1_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE1_INITIATOR_NAME,
    }
},
    {
    "server": ENC2SHBAY1,
    "username": ilo_credentials['username'],
    "password":ilo_credentials['password'],
    "path":"/rest/v1/Systems/1/bios/iSCSI",
    "validate":{
        "Description": "This is the Server iSCSI Software Initiator Current Settings",
        "iSCSIBootSources":
        [
            {
                "StructuredBootString": "NIC.Slot.3.1.iSCSI",
                "iSCSIAuthenticationMethod": "Chap",
                "iSCSIBootAttemptInstance": 1,
                "iSCSIBootAttemptName": PROFILE2_ISCSI_BOOT_ATTEMPT_1,
                "iSCSIBootEnable": "Enabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": "",
                "iSCSIChapType": "Mutual",
                "iSCSIChapUsername": "",
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": "Slot3NicBoot1",
                "iSCSIReverseChapSecret": "",
                "iSCSIReverseChapUsername": "",
                "iSCSITargetInfoViaDHCP": False,
                "iSCSITargetIpAddress": VSA_116_BOOT_TARGET_IP,
                "iSCSITargetName": PROFILE2_BOOT_TARGET_NAME,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            },
            {
                "StructuredBootString": None,
                "UEFIDevicePath": None,
                "iSCSIAuthenticationMethod": "None",
                "iSCSIBootAttemptInstance": 0,
                "iSCSIBootAttemptName": "",
                "iSCSIBootEnable": "Disabled",
                "iSCSIBootLUN": "0",
                "iSCSIChapSecret": None,
                "iSCSIChapType": "OneWay",
                "iSCSIChapUsername": None,
                "iSCSIConnectRetry": 3,
                "iSCSIConnectTimeoutMS": 20000,
                "iSCSIInitiatorGateway": "0.0.0.0",
                "iSCSIInitiatorInfoViaDHCP": True,
                "iSCSIInitiatorIpAddress": "0.0.0.0",
                "iSCSIInitiatorNetmask": "0.0.0.0",
                "iSCSIIpAddressType": "IPv4",
                "iSCSINicSource": None,
                "iSCSIReverseChapSecret": None,
                "iSCSIReverseChapUsername": None,
                "iSCSITargetInfoViaDHCP": True,
                "iSCSITargetIpAddress": "0.0.0.0",
                "iSCSITargetName": None,
                "iSCSITargetTcpPort": 3260
            }
        ],
        "iSCSIInitiatorName": PROFILE2_INITIATOR_NAME,
    }
}]

hw_iscsi_hpmctp = [
    {"hpmctpIp": hpmctp_credentials['ip'],
     "hpmctpUsername":hpmctp_credentials['username'],
     "hpmctpPassword":hpmctp_credentials['password'],
     "serverName":"SH:" + ENC3SHBAY1,
     "iloUsername":ilo_credentials['username'],
     "iloPassword":ilo_credentials['password'],
     "validatePrimary":
     """
                        <ISCSI-Boot-Cats>
    <flexfunc-index>2</flexfunc-index>
    <rdonly-categories>
        <capabilities-type>
            <iscsi-dhcp-proxy-cap><true/></iscsi-dhcp-proxy-cap>
        </capabilities-type>
        <status-type>
            <iscsi-boot-progress><none/></iscsi-boot-progress>
        </status-type>
    </rdonly-categories>
    <active-cfg-cats-RO>
        <config-nextDLR-type>
            <iscsi-ip-addr-type><iPv4/></iscsi-ip-addr-type>
            <iscsi-IP-Mask-DNS-via-DHCP><false/></iscsi-IP-Mask-DNS-via-DHCP>
            <iscsi-Target-Info-via-DHCP><false/></iscsi-Target-Info-via-DHCP>
            <iscsi-initiator-cfg>
                <iscsi-initiator-name>iqn.1986-03.hp:uefi-tbird8-bay3-iscsiboot</iscsi-initiator-name>
                <iscsi-initiator-ip-addr>C0 A8 16 3A</iscsi-initiator-ip-addr>
                <iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
                <iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
                <iscsi-primary-dns></iscsi-primary-dns>
                <iscsi-second-dns></iscsi-second-dns>
            </iscsi-initiator-cfg>
            <iscsi-target-params>
                <iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:613:tbird8-bay3-sles<nul/></iscsi-target-name>
                <iscsi-LUN>0</iscsi-LUN>
                <iscsi-target-ip>C0 A8 15 47</iscsi-target-ip>
                <iscsi-target-tcpport>3260</iscsi-target-tcpport>
                <iscsi-target-ip2></iscsi-target-ip2>
                <iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
                <iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
                <iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
            </iscsi-target-params>
            <iscsi-dhcp-vendor-id>none</iscsi-dhcp-vendor-id>
            <authentication>
                <iscsi-authentic-meth><mutual-chap/></iscsi-authentic-meth>
                <iscsi-chap-username>tbird8-bay3</iscsi-chap-username>
                <iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
                <iscsi-mutual-username>tbird8-bay3</iscsi-mutual-username>
                <iscsi-mutual-secret>68 70 76 73 65 31 32 33 77 70 73 74</iscsi-mutual-secret>
                <deprecated-b1><false/></deprecated-b1>
                <deprecated-b2><false/></deprecated-b2>
            </authentication>
        </config-nextDLR-type>
    </active-cfg-cats-RO>
    <pending-cfg-cats-RW>
    </pending-cfg-cats-RW>
</ISCSI-Boot-Cats>""",
     "validateSecondary":
     """
   <ISCSI-Boot-Cats>
    <flexfunc-index>3</flexfunc-index>
    <rdonly-categories>
        <capabilities-type>
            <iscsi-dhcp-proxy-cap><true/></iscsi-dhcp-proxy-cap>
        </capabilities-type>
        <status-type>
            <iscsi-boot-progress><none/></iscsi-boot-progress>
        </status-type>
    </rdonly-categories>
    <active-cfg-cats-RO>
        <config-nextDLR-type>
            <iscsi-ip-addr-type><iPv4/></iscsi-ip-addr-type>
            <iscsi-IP-Mask-DNS-via-DHCP><false/></iscsi-IP-Mask-DNS-via-DHCP>
            <iscsi-Target-Info-via-DHCP><false/></iscsi-Target-Info-via-DHCP>
            <iscsi-initiator-cfg>
                <iscsi-initiator-name>iqn.1986-03.hp:uefi-tbird8-bay3-iscsiboot</iscsi-initiator-name>
                <iscsi-initiator-ip-addr>C0 A8 16 3B</iscsi-initiator-ip-addr>
                <iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
                <iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
                <iscsi-primary-dns></iscsi-primary-dns>
                <iscsi-second-dns></iscsi-second-dns>
            </iscsi-initiator-cfg>
            <iscsi-target-params>
                <iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:613:tbird8-bay3-sles<nul/></iscsi-target-name>
                <iscsi-LUN>0</iscsi-LUN>
                <iscsi-target-ip>C0 A8 15 47</iscsi-target-ip>
                <iscsi-target-tcpport>3260</iscsi-target-tcpport>
                <iscsi-target-ip2></iscsi-target-ip2>
                <iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
                <iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
                <iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
            </iscsi-target-params>
            <iscsi-dhcp-vendor-id>none</iscsi-dhcp-vendor-id>
            <authentication>
                <iscsi-authentic-meth><mutual-chap/></iscsi-authentic-meth>
                <iscsi-chap-username>tbird8-bay3</iscsi-chap-username>
                <iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
                <iscsi-mutual-username>tbird8-bay3</iscsi-mutual-username>
                <iscsi-mutual-secret>68 70 76 73 65 31 32 33 77 70 73 74</iscsi-mutual-secret>
                <deprecated-b1><false/></deprecated-b1>
                <deprecated-b2><false/></deprecated-b2>
            </authentication>
        </config-nextDLR-type>
    </active-cfg-cats-RO>
    <pending-cfg-cats-RW>
    </pending-cfg-cats-RW>
</ISCSI-Boot-Cats>"""
     },
    {"hpmctpIp": hpmctp_credentials['ip'],
     "hpmctpUsername":hpmctp_credentials['username'],
     "hpmctpPassword":hpmctp_credentials['password'],
     "serverName":"SH:" + ENC1SHBAY5,
     "iloUsername":ilo_credentials['username'],
     "iloPassword":ilo_credentials['password'],
     "validatePrimary":
     """
                        <ISCSI-Boot-Cats>
    <flexfunc-index>2</flexfunc-index>
    <rdonly-categories>
        <capabilities-type>
            <iscsi-dhcp-proxy-cap><true/></iscsi-dhcp-proxy-cap>
        </capabilities-type>
        <status-type>
            <iscsi-boot-progress><none/></iscsi-boot-progress>
        </status-type>
    </rdonly-categories>
    <active-cfg-cats-RO>
        <config-nextDLR-type>
            <iscsi-ip-addr-type><iPv4/></iscsi-ip-addr-type>
            <iscsi-IP-Mask-DNS-via-DHCP><false/></iscsi-IP-Mask-DNS-via-DHCP>
            <iscsi-Target-Info-via-DHCP><false/></iscsi-Target-Info-via-DHCP>
            <iscsi-initiator-cfg>
                <iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-vcguhbt005</iscsi-initiator-name>
                <iscsi-initiator-ip-addr>C0 A8 3B 1E</iscsi-initiator-ip-addr>
                <iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
                <iscsi-initiator-route></iscsi-initiator-route>
                <iscsi-primary-dns></iscsi-primary-dns>
                <iscsi-second-dns></iscsi-second-dns>
            </iscsi-initiator-cfg>
            <iscsi-target-params>
                <iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-116:521:spt-hw-iscsi-managedvol-dhcp-newvol<nul/></iscsi-target-name>
                <iscsi-LUN>0</iscsi-LUN>
                <iscsi-target-ip>C0 A8 15 3B</iscsi-target-ip>
                <iscsi-target-tcpport>3260</iscsi-target-tcpport>
                <iscsi-target-ip2></iscsi-target-ip2>
                <iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
                <iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
                <iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
            </iscsi-target-params>
            <iscsi-dhcp-vendor-id>none</iscsi-dhcp-vendor-id>
            <authentication>
                <iscsi-authentic-meth><mutual-chap/></iscsi-authentic-meth>
                <iscsi-chap-username>iqn.2015-02.com.hpe:oneview-vcguhbt005</iscsi-chap-username>
                <iscsi-chap-secret>55 6A 24 4C 67 41 5A 33 57 48 4E 69 23 23 56 53</iscsi-chap-secret>
                <iscsi-mutual-username>iqn.2015-02.com.hpe:oneview-vcguhbt005</iscsi-mutual-username>
                <iscsi-mutual-secret>57 6F 47 37 58 29 31 77 24 5E 2D 21 33 63 5F 75</iscsi-mutual-secret>
                <deprecated-b1><false/></deprecated-b1>
                <deprecated-b2><false/></deprecated-b2>
            </authentication>
        </config-nextDLR-type>
    </active-cfg-cats-RO>
    <pending-cfg-cats-RW>
    </pending-cfg-cats-RW>
</ISCSI-Boot-Cats>""",
     "validateSecondary":
     """
    <ISCSI-Boot-Cats>
    <flexfunc-index>3</flexfunc-index>
    <rdonly-categories>
        <capabilities-type>
            <iscsi-dhcp-proxy-cap><true/></iscsi-dhcp-proxy-cap>
        </capabilities-type>
        <status-type>
            <iscsi-boot-progress><none/></iscsi-boot-progress>
        </status-type>
    </rdonly-categories>
    <active-cfg-cats-RO>
        <config-nextDLR-type>
            <iscsi-ip-addr-type><iPv4/></iscsi-ip-addr-type>
            <iscsi-IP-Mask-DNS-via-DHCP><false/></iscsi-IP-Mask-DNS-via-DHCP>
            <iscsi-Target-Info-via-DHCP><false/></iscsi-Target-Info-via-DHCP>
            <iscsi-initiator-cfg>
                <iscsi-initiator-name>none</iscsi-initiator-name>
                <iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
                <iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
                <iscsi-initiator-route></iscsi-initiator-route>
                <iscsi-primary-dns></iscsi-primary-dns>
                <iscsi-second-dns></iscsi-second-dns>
            </iscsi-initiator-cfg>
            <iscsi-target-params>
                <iscsi-target-name>enon<nul/></iscsi-target-name>
                <iscsi-LUN>0</iscsi-LUN>
                <iscsi-target-ip>00 00 00 00</iscsi-target-ip>
                <iscsi-target-tcpport>3260</iscsi-target-tcpport>
                <iscsi-target-ip2></iscsi-target-ip2>
                <iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
                <iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
                <iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
            </iscsi-target-params>
            <iscsi-dhcp-vendor-id>enon</iscsi-dhcp-vendor-id>
            <authentication>
                <iscsi-authentic-meth><none/></iscsi-authentic-meth>
                <iscsi-chap-username></iscsi-chap-username>
                <iscsi-chap-secret></iscsi-chap-secret>
                <iscsi-mutual-username></iscsi-mutual-username>
                <iscsi-mutual-secret></iscsi-mutual-secret>
                <deprecated-b1><false/></deprecated-b1>
                <deprecated-b2><false/></deprecated-b2>
            </authentication>
        </config-nextDLR-type>
    </active-cfg-cats-RO>
    <pending-cfg-cats-RW>
    </pending-cfg-cats-RW>
</ISCSI-Boot-Cats>"""
     }]

edit_profile_template = {
    "type": "ServerProfileTemplateV6",
    "uri": "SPT:SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
    "name": "SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
    "description": "SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
    "serverProfileDescription": "SPT-hw-iscsi-SpecifyBootTarget-UserSpecified",
    "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:EG1",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "UserDefined",
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "1",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "DHCP",
                    "subnetMask": "",
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": VSA_173_BOOT_TARGET_IP,
                        "firstBootTargetPort": VSA_173_BOOT_TARGET_PORT,
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap"
                    }
                }
            },
            {
                "id": 2,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "firstBootTargetIp": VSA_173_BOOT_TARGET_IP,
                        "firstBootTargetPort": VSA_173_BOOT_TARGET_PORT,
                        "secondBootTargetIp": "",
                        "chapLevel": "MutualChap"
                    }
                }
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [

        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [

        ],
        "controllers": [

        ]
    },
    "sanStorage": None,
    "category": "server-profile-templates",
    "status": "OK",
    "state": None,
}

edit_profile = {
    "type": "ServerProfileV10",
    "name": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
    "description": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": "SH:" + ENC1 + ", bay 5",
    "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:EG1",
    "enclosureUri": "ENC:" + ENC1,
    "enclosureBay": 5,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "wwpn": None,
                "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "UserDefined",
                    "subnetMask": "255.255.192.0",
                    "gateway": "",
                    "ipAddress": "192.168.22.50"
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": None,
                    #        "iscsi": {
                    #          "initiatorNameSource": "ProfileInitiatorName",
                    #          "initiatorVlanId": "",
                    #          "firstBootTargetIp": "",
                    #          "firstBootTargetPort": "",
                    #          "secondBootTargetIp": "",
                    #          "secondBootTargetPort": "",
                    #          "chapLevel": None,
                    #          "initiatorName": "",
                    #          "bootTargetName": "",
                    #          "bootTargetLun": "",
                    #          "chapName": "",
                    #          "chapSecret": None,
                    #          "mutualChapName": "",
                    #          "mutualChapSecret": None
                    #        }
                }
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [

        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [

        ],
        "controllers": [

        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": False,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE4_VOL1_TARGET
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-Vol",
        }, {
            "id": 2,
            "isBootVolume": True,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE4_VOL2_TARGET
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-NewVol",
        }],
    },
    "osDeploymentSettings": None,
}

edit_profile_back_to_dhcp = {
    "type": "ServerProfileV10",
    "name": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
    "description": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": "SH:" + ENC1 + ", bay 5",
    "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:EG1",
    "enclosureUri": "ENC:" + ENC1,
    "enclosureBay": 5,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "wwpn": None,
                "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                    "subnetMask": "",
                    "gateway": "",
                    "ipAddress": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": None,
                    #        "iscsi": {
                    #          "initiatorNameSource": "ProfileInitiatorName",
                    #          "initiatorVlanId": "",
                    #          "firstBootTargetIp": "",
                    #          "firstBootTargetPort": "",
                    #          "secondBootTargetIp": "",
                    #          "secondBootTargetPort": "",
                    #          "chapLevel": None,
                    #          "initiatorName": "",
                    #          "bootTargetName": "",
                    #          "bootTargetLun": "",
                    #          "chapName": "",
                    #          "chapSecret": None,
                    #          "mutualChapName": "",
                    #          "mutualChapSecret": None
                    #        }
                }
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [

        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [

        ],
        "controllers": [

        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": False,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE4_VOL1_TARGET
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-Vol",
        }, {
            "id": 2,
            "isBootVolume": True,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE4_VOL2_TARGET
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-NewVol",
        }]
    },
    "osDeploymentSettings": None,
}

move_bay5_to_bay7_profile_with_dhcp = {
    "type": "ServerProfileV10",
    "name": "tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP",
    "description": "moved-from-bay5-to-bay7-hw-iscsi-ManagedVol-DHCP",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "templateCompliance": "Unknown",
    "serverHardwareUri": 'SH:' + ENC1 + ', bay 7',
    "serverHardwareTypeUri": "SHT:SY 480 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:EG1",
    "enclosureUri": "ENC:" + ENC1,
    "enclosureBay": 7,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "status": "OK",
    "state": "Normal",
    "inProgress": False,
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": "ETH:network-untagged",
                "macType": "Virtual",
                "wwpnType": "Virtual",
                "wwpn": None,
                "wwnn": None,
                "ipv4": {
                    "ipAddressSource": "DHCP"
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": None,
                    #        "iscsi": {
                    #          "initiatorNameSource": "ProfileInitiatorName",
                    #          "initiatorVlanId": "",
                    #          "firstBootTargetIp": "",
                    #          "firstBootTargetPort": "",
                    #          "secondBootTargetIp": "",
                    #          "secondBootTargetPort": "",
                    #          "chapLevel": None,
                    #          "initiatorName": "",
                    #          "bootTargetName": "",
                    #          "bootTargetLun": "",
                    #          "chapName": "",
                    #          "chapSecret": None,
                    #          "mutualChapName": "",
                    #          "mutualChapSecret": None
                    #        }
                }
            }
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [

        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [

        ],
        "controllers": [

        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": False,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE4_VOL1_TARGET
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-Vol",
        }, {
            "id": 2,
            "isBootVolume": True,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE4_VOL2_TARGET
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:tbird14-bay5-SP-hw-iscsi-ManagedVol-DHCP-NewVol",
        }]
    },
    "osDeploymentSettings": None,
}

create_dhcp_profile_300 = [{
    "type": "ServerProfileV6",
    "serverHardwareUri": 'SH:' + ENC1 + ', bay 5',
    "serverHardwareTypeUri": "SHT:SY 660 Gen9:1:Smart Array P542D Controller:3:HP Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:EG1",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "macType": "Virtual",
    "wwnType": "Virtual",
    "name": "bay5-SP-sw-iscsi-SpecifyBootTarget-DHCP",
    "description": "bay5-sw-iscsi-SpecifyBootTarget-DHCP",
    "affinity": "Bay",
    "connections": [
        {
            "id": 1,
            "name": "1",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:network-untagged",
            "mac": None,
            "wwpn": None,
            "wwnn": None,
            "requestedVFs": "0",
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": "",
                "ipAddress": ""
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "UserDefined",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                    "initiatorVlanId": "",
                    "firstBootTargetIp": VSA_116_BOOT_TARGET_IP,
                    "firstBootTargetPort": VSA_116_BOOT_TARGET_PORT,
                    "secondBootTargetIp": "",
                    "secondBootTargetPort": "",
                    "chapLevel": "Chap",
                    "initiatorName": "",
                    "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                    "bootTargetLun": "0",
                    "chapName": PROFILE1_CHAP_NAME,
                    "chapSecret": CHAP_SECRET,
                    "mutualChapName": "",
                    "mutualChapSecret": None
                }
            }
        }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [

        ]
    },
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "",
    #    "serverProfileTemplateUri": "SPT:SPT-sw-iscsi-SpecifyBootTarget-DHCP",
    "osDeploymentSettings": None,
    "localStorage": {
        "sasLogicalJBODs": [

        ],
        "controllers": [

        ]
    },
    "sanStorage": None
}]


profile300_verify = {
    "type": "ServerProfileV6",
    "name": "bay2-SP-sw-iscsi-ManagedVol-DHCP",
    "description": "SPT-sw-iscsi-ManagedVol-DHCP",
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverProfileTemplateUri": None,
    "serverHardwareUri": "SH:" + ENC1 + ", bay 2",
    "enclosureGroupUri": "EG:EG1",
    "enclosureUri": "ENC:" + ENC1,
    "enclosureBay": 2,
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "firmware": {
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "manageFirmware": False,
        "firmwareBaselineUri": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connections": [],
    "bootMode": {
        "pxeBootPolicy": "Auto",
        "manageMode": True,
        "mode": "UEFIOptimized"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "volumeAttachments": [{
            "id": 1,
            "lun": "0",
            "lunType": "Auto",
            "state": "Attached",
            "status": "OK",
            "storagePaths": [
                {
                    "storageTargets": [
                        "tcpPort: 3260, ipAddress: " + VSA_116_BOOT_TARGET_IP + ", name: " + PROFILE2_BOOT_TARGET_NAME
                    ],
                    "storageTargetType": "Auto",
                    "connectionId": 1,
                    "isEnabled": True,
                    "status": "OK"
                }
            ],
            "volume": None,
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
            "volumeUri": "StorageVolumeV3:tbird8-bay2-dhcp",
        }],
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2"
    },
    "osDeploymentSettings": None,
}

profileTemplate300_verify = {
    "type": "ServerProfileTemplateV2",
    "name": "SPT-sw-iscsi-ManagedVol-DHCP",
    "description": "SPT-sw-iscsi-ManagedVol-DHCP",
    "serverProfileDescription": "SPT-sw-iscsi-ManagedVol-DHCP",
    "enclosureGroupUri": "EG:EG1",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "iscsiInitiatorNameType": "AutoGenerated",
    "firmware": {
        "manageFirmware": False,
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "firmwareBaselineUri": None
    },
    "connections": [],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "connectionId": 1,
                    "isEnabled": True,
                    "storageTargetType": "Auto",
                    "storageTargets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "tbird8-bay2-dhcp",
                    "description": "",
                    "storagePool": "StoragePoolV2:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "THIN",
                    "isShareable": False,
                },
                "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "StorageSystemV3:VSA_Cluster_116"
        }]
    },
    "category": "server-profile-templates",
    "status": "OK",
    "state": None,
}


edit_profile_tempalte300 = [{"type": "ServerProfileTemplateV2",
                             "serverProfileDescription": "SPT-sw-iscsi-SpecifyBootTarget-DHCP",
                             "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
                             "enclosureGroupUri": "EG:EG1",
                             "serialNumberType": "Virtual",
                             "macType": "Virtual",
                             "wwnType": "Virtual",
                             "name": "SPT-sw-iscsi-SpecifyBootTarget-DHCP",
                             "description": "SPT-sw-iscsi-SpecifyBootTarget-DHCP",
                             "affinity": "Bay",
                             "connections": [
                                 {
                                     "id": 1,
                                     "name": "1",
                                     "functionType": "Ethernet",
                                     "portId": "Auto",
                                     "requestedMbps": "2500",
                                     "networkUri": "ETH:unTagged",
                                     "requestedVFs": "0",
                                     "ipv4": {
                                         "ipAddressSource": "DHCP",
                                         "subnetMask": "",
                                         "gateway": ""
                                     },
                                     "boot": {
                                         "priority": "Primary",
                                         "ethernetBootType": "iSCSI",
                                         "bootVolumeSource": "UserDefined",
                                         "iscsi": {
                                             "initiatorNameSource": "ProfileInitiatorName",
                                             "initiatorVlanId": "",
                                             "firstBootTargetIp": VSA_116_BOOT_TARGET_IP,
                                             "firstBootTargetPort": VSA_116_BOOT_TARGET_PORT,
                                             "secondBootTargetIp": "",
                                             "secondBootTargetPort": "",
                                             "chapLevel": "Chap"
                                         }
                                     }
                                 },
                                 {
                                     "id": 2,
                                     "name": "2",
                                     "functionType": "Ethernet",
                                     "portId": "Auto",
                                     "requestedMbps": "2500",
                                     "networkUri": "ETH:unTagged",
                                     "requestedVFs": "0",
                                     "ipv4": {
                                         "ipAddressSource": "DHCP",
                                         "subnetMask": "",
                                         "gateway": ""
                                     },
                                     "boot": {
                                         "priority": "Secondary",
                                         "ethernetBootType": "iSCSI",
                                         "bootVolumeSource": "UserDefined",
                                         "iscsi": {
                                             "initiatorNameSource": "ProfileInitiatorName",
                                             "initiatorVlanId": "",
                                             "firstBootTargetIp": VSA_116_BOOT_TARGET_IP,
                                             "firstBootTargetPort": VSA_116_BOOT_TARGET_PORT,
                                             "secondBootTargetIp": "",
                                             "secondBootTargetPort": "",
                                             "chapLevel": "None"
                                         }
                                     }
                                 }
                             ],
                             "boot": {"manageBoot": True, "order": ["HardDisk"]},
                             "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                             "firmware": {"manageFirmware": False, "firmwareBaselineUri": "",
                                          "forceInstallFirmware": False, "firmwareInstallType": None},
                             "bios": {"manageBios": False, "overriddenSettings": []},
                             "hideUnusedFlexNics": True,
                             "iscsiInitiatorNameType": "AutoGenerated",
                             "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                             "sanStorage": None
                             }]


edit_profile300 = [{
    "type": "ServerProfileV400",
    "name": "bay2-SP-sw-iscsi-ManagedVol-DHCP",
    "description": "SPT-sw-iscsi-ManagedVol-DHCP",
    "serialNumber": "VCGPBWC00N",
    "iscsiInitiatorName": None,
    "iscsiInitiatorNameType": "AutoGenerated",
    "serverHardwareUri": "SH:" + ENC1 + ", bay 2",
    "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
    "enclosureGroupUri": "EG:EG1",
    "enclosureUri": "ENC:" + ENC1,
    "enclosureBay": 2,
    "affinity": "Bay",
    "associatedServer": None,
    "hideUnusedFlexNics": True,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": "",
        "forceInstallFirmware": False,
        "firmwareInstallType": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "connections": [
        {
            "id": 1,
            "name": "1",
            "functionType": "Ethernet",
            "portId": "Mezz 3:1-a",
            "requestedMbps": "2500",
            "networkUri": "ETH:unTagged",
            "macType": "Virtual",
            "mac": "52:81:C6:90:00:1E",
            "wwpnType": "Virtual",
            "wwpn": None,
            "wwnn": None,
            "requestedVFs": "0",
            "ipv4": {
                "ipAddressSource": "DHCP"
            },
            "boot": {
                "priority": "Primary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "ManagedVolume",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                    "firstBootTargetIp": "192.168.21.59",
                    "firstBootTargetPort": "3260",
                    "secondBootTargetIp": "",
                    "secondBootTargetPort": "",
                    "chapLevel": "MutualChap",
                    "initiatorName": PROFILE2_INITIATOR_NAME,
                    "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                    "bootTargetLun": "0",
                    "chapName": PROFILE2_CHAP_NAME,
                    "mutualChapName": PROFILE2_MCHAP_NAME
                }
            }
        },
        {
            "id": 2,
            "name": "2",
            "functionType": "Ethernet",
            "portId": "Auto",
            "requestedMbps": "2500",
            "networkUri": "ETH:unTagged",
            "mac": None,
            "wwpn": None,
            "wwnn": None,
            "requestedVFs": "0",
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": "",
                "ipAddress": ""
            },
            "boot": {
                "priority": "Secondary",
                "ethernetBootType": "iSCSI",
                "bootVolumeSource": "UserDefined",
                "iscsi": {
                    "initiatorNameSource": "ProfileInitiatorName",
                    "initiatorVlanId": "",
                    "firstBootTargetIp": "192.168.21.59",
                    "firstBootTargetPort": "3260",
                    "secondBootTargetIp": "",
                    "secondBootTargetPort": "",
                    "chapLevel": "None",
                    "initiatorName": "",
                    "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                    "bootTargetLun": "0",
                    "chapName": "",
                    "chapSecret": None,
                    "mutualChapName": "",
                    "mutualChapSecret": None
                }
            }
        }
    ],
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": [

        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [

        ],
        "controllers": [

        ]
    },
    "sanStorage": {
        "manageSanStorage": True,
        "hostOSType": "Windows 2012 / WS2012 R2",
        "volumeAttachments": [{
            "id": 1,
            "isBootVolume": True,
            "lun": 0,
            "lunType": "Auto",
            "storagePaths": [
                {
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                    "targets": [
                        PROFILE2_BOOT_TARGET_NAME
                    ]
                }
            ],
            "volume": None,
            "volumeUri": "StorageVolumeV3:" + PROFILE2_VOLUME_NAME,
        }]
    },
    "osDeploymentSettings": None,
}]

server_profiles_tunnel = [
    {
        "type": "ServerProfileV400",
        "serverHardwareUri": 'SH:' + ENC1 + ', bay 1',
        "serverHardwareTypeUri": "SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "bay1-SP-sw-iscsi-SpecifyBootTarget-DHCP",
        "description": "SPT-sw-iscsi-Tunnel-SpecifyBootTarget-DHCP",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "1",
                "functionType": "Ethernet",
                "portId": "Mezz 3:1-a",
                "requestedMbps": "2500",
                "networkUri": "ETH:Tunnel",
                "mac": None,
                "wwpn": None,
                "wwnn": None,
                "requestedVFs": "0",
                "ipv4": {
                    "ipAddressSource": "DHCP",
                    "subnetMask": "",
                    "gateway": "",
                    "ipAddress": ""
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorVlanId": "",
                        "firstBootTargetIp": VSA_116_BOOT_TARGET_IP,
                        "firstBootTargetPort": VSA_116_BOOT_TARGET_PORT,
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "initiatorName": PROFILE1_INITIATOR_NAME,
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }
                }
            }
        ],
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        #    "serverProfileTemplateUri": "SPT:SPT-sw-iscsi-SpecifyBootTarget-DHCP",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": None
    },
    {
        "type": "ServerProfileV400",
        "serverHardwareUri": "SH:" + ENC1 + ", bay 6",
        "serverHardwareTypeUri": "SHT:SY 660 Gen9:3:HP Synergy 3820C 10/20Gb CNA",
        "enclosureGroupUri": "EG:EG1",
        "serialNumberType": "Virtual",
        "iscsiInitiatorNameType": "AutoGenerated",
        "macType": "Virtual",
        "wwnType": "Virtual",
        "name": "bay6-SP-hw-iscsi-ManagedVol-DHCP",
        "description": "SPT-hw-iscsi-Tunnel-ManagedVol-DHCP",
        "affinity": "Bay",
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": "ETH:Tunnel",
                "ipv4": {
                    "ipAddressSource": "DHCP",
                    "subnetMask": "",
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "firstBootTargetIp": "",
                        "firstBootTargetPort": "",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": None,
                        "initiatorName": "",
                        "bootTargetName": "",
                        "bootTargetLun": "",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }
                }
            }
        ],
        "boot": {
            "manageBoot": True,
            "order": [
                "HardDisk"
            ]
        },
        "bootMode": {
            "manageMode": True,
            "mode": "UEFI",
            "pxeBootPolicy": "Auto"
        },
        "firmware": {
            "manageFirmware": False,
            "firmwareBaselineUri": "",
            "forceInstallFirmware": False,
            "firmwareInstallType": None
        },
        "bios": {
            "manageBios": False,
            "overriddenSettings": [

            ]
        },
        "hideUnusedFlexNics": True,
        "iscsiInitiatorName": "",
        "osDeploymentSettings": None,
        "localStorage": {
            "sasLogicalJBODs": [

            ],
            "controllers": [

            ]
        },
        "sanStorage": {
            "hostOSType": "Windows 2012 / WS2012 R2",
            "manageSanStorage": True,
            "volumeAttachments": [{
                "id": 1,
                "isBootVolume": False,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": None,
                "volumeUri": "StorageVolumeV3:SPT-hw-iscsi-ManagedVol-DHCP-Vol",
            }, {
                "id": 2,
                "isBootVolume": True,
                "lun": None,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                        "targets": [

                        ]
                    }
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "SPT-hw-iscsi-ManagedVol-DHCP-NewVol",
                        "storagePool": "StoragePoolV2:VSA_Cluster_116",
                        "size": 1073741824,
                        "provisioningType": "THIN",
                                "isShareable": False,
                                "dataProtectionLevel": "NetworkRaid0None"
                    },
                    "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:VSA_Cluster_116",
                },
                "volumeStorageSystemUri": "StorageSystemV3:VSA_Cluster_116",
                "volumeUri": None,
            }]
        }
    }]

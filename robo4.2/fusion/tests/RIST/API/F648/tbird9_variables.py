admin_credentials = {
    'userName': 'Administrator',
    'password': 'wpsthpvse1'}
hpmctp_credentials = {
    'ip': '16.114.218.103',
    'username': 'root',
    'password': 'hpvse1'}
ilo_credentials = {
    'username': 'Administrator',
    'password': 'hpvse123'}
# LIG, EG & LE
LIG_NAME = 'LIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'
# Enclosures
ENC1 = 'CN744502CG'
# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY2 = '%s, bay 2' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
FIRST_BOOT_TARGET_IP = "192.168.21.71"
SECOND_BOOT_TARGET_IP = "192.168.21.72"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"
# PROFILE1: profile on bay1, Blackbird
PROFILE1_NAME = "tbird9-bay1-profile"
PROFILE1_ILO = "16.114.219.242"
PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol'
PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird9-bay1"
PROFILE1_INITIATOR_IP_1 = "192.168.22.51"
PROFILE1_INITIATOR_IP_2 = "192.168.22.56"
PROFILE1_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol_attempt_1"
PROFILE1_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol_attempt_2"
PROFILE1_CHAP_NAME = 'tbird9-bay1'
PROFILE1_MCHAP_NAME = 'tbird9-bay1'
# PROFILE2: profile on bay6, Redbird
PROFILE2_NAME = "tbird9-bay6-profile"
PROFILE2_ILO = "16.114.219.197"
PROFILE2_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol"
PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird9-bay6"
PROFILE2_INITIATOR_IP_1 = "192.168.22.52"
PROFILE2_INITIATOR_IP_2 = "192.168.22.57"
PROFILE2_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol_attempt_1"
PROFILE2_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol_attempt_2"
PROFILE2_CHAP_NAME = 'tbird9-bay6'
PROFILE2_MCHAP_NAME = 'tbird9-bay6'
# PROFILE3: bay6 profile move to bay2
PROFILE3_ILO = "16.114.219.244"
PROFILE3_BOOT_TARGET_NAME = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol"
PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-tbird9-bay2"
PROFILE3_INITIATOR_IP_1 = "192.168.22.61"
PROFILE3_INITIATOR_IP_2 = "192.168.22.62"
PROFILE3_ISCSI_BOOT_ATTEMPT_1 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol_attempt_1"
PROFILE3_ISCSI_BOOT_ATTEMPT_2 = "iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol_attempt_2"
appliance = {
    "type": "ApplianceNetworkConfiguration",
    "applianceNetworks": [
        {
            "activeNode": 1,
            "unconfigure": False,
            "app1Ipv4Addr": "16.114.210.217",
            "app1Ipv6Addr": "",
            "app2Ipv4Addr": "16.114.210.218",
            "app2Ipv6Addr": "",
            "virtIpv4Addr": "16.114.211.88",
            "virtIpv6Addr": None,
            "app1Ipv4Alias": None,
            "app1Ipv6Alias": None,
            "app2Ipv4Alias": None,
            "app2Ipv6Alias": None,
            "hostname": "wpst-tbird-9-oneview.vse.rdlabs.hpecorp.net",
            "confOneNode": True,
            "interfaceName": "",
            "macAddress": None,
            "ipv4Type": "STATIC",
            "ipv6Type": "UNCONFIGURE",
            "overrideIpv4DhcpDnsServers": False,
            "ipv4Subnet": "255.255.240.0",
            "ipv4Gateway": "16.114.208.1",
            "ipv6Subnet": None,
            "ipv6Gateway": None,
            "domainName": "vse.rdlabs.hpecorp.net",
            "searchDomains": [
            ],
            "ipv4NameServers":[
                "16.125.25.81",
                "16.125.25.82"],
            "ipv6NameServers":[
                "16.125.25.81",
                "16.125.25.82"],
            "bondedTo":None,
            "aliasDisabled":True,
            "configureRabbitMqSslListener":False,
            "configurePostgresSslListener":False,
            "webServerCertificate":None,
            "webServerCertificateChain":None,
            "webServerCertificateKey":None}
    ],
    "serverCertificate": {
        "rabbitMQCertificate": None,
        "rabbitMQRootCACertificate": None,
        "rabbitMQCertificateKey": None,
        "postgresCertificate": None,
        "postgresRootCACertificate": None,
        "postgresCertificateKey": None}
}
timeandlocale = {
    'type': 'TimeAndLocale',
    'dateTime': None,
    'timezone': 'UTC',
    'ntpServers': [
        'ntp.hpecorp.net'],
    'locale': 'en_US.UTF-8'}
users = [
    {
        'userName': 'Serveradmin',
        'password': 'wpsthpvse1',
        'fullName': 'Serveradmin',
        'roles': [
            'Server administrator'],
        'emailAddress': 'sarah@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'},
    {
        'userName': 'Networkadmin',
        'password': 'wpsthpvse1',
        'fullName': 'Networkadmin',
        'roles': [
            'Network administrator'],
        'emailAddress': 'nat@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'},
    {
        'userName': 'Backupadmin',
        'password': 'wpsthpvse1',
        'fullName': 'Backupadmin',
        'roles': [
            'Backup administrator'],
        'emailAddress': 'backup@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'},
    {
        'userName': 'Noprivledge',
        'password': 'wpsthpvse1',
        'fullName': 'Noprivledge',
        'roles': [
            'Read only'],
        'emailAddress': 'rheid@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': 'UserAndPermissions'}
]
licenses = [{'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
            {'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
            {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            {'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'},
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]
enclosures = [
    {
        "type": "EnclosureV300",
        "name": ENC1,
    },
]
ics = [
    {
        "name": ENC1ICBAY3,
    },
    {
        "name": ENC1ICBAY6,
    },
]
ethernet_networks = [
    {
        'name': 'network-tunnel',
        'type': 'ethernet-networkV300',
        'vlanId': 0,
        'subnetUri': None,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tunnel'},
    {
        'name': 'network-untagged',
        'type': 'ethernet-networkV300',
        'vlanId': 0,
        'subnetUri': None,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Untagged'},
    {
        'name': 'net100',
        'type': 'ethernet-networkV300',
        'vlanId': 100,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'},
    {
        'name': 'net300',
        'type': 'ethernet-networkV300',
        'vlanId': 300,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tagged'},
]
network_sets = [
    {
        'name': 'NS1',
        'type': 'network-setV300',
        'networkUris': [
            'net100',
            'net300'],
        'nativeNetworkUri': 'net100'},
]
icmap = [
    {
        'bay': 3,
        'enclosure': 1,
        'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23',
        'enclosureIndex': 1},
    {
        'bay': 6,
        'enclosure': 1,
        'type': 'Virtual Connect SE 40Gb F8 Module for Synergy - 794502-B23',
        'enclosureIndex': 1},
]
uplink_sets = {
    'us_untagged': {
        'name': 'us-untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': [
            'network-untagged'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {
                'enclosure': '1',
                'bay': '3',
                'port': 'Q1.1',
                'speed': 'Auto'},
            {
                'enclosure': '1',
                'bay': '6',
                'port': 'Q1.1',
                'speed': 'Auto'},
        ]
    },
    'us_tunnel': {
        'name': 'us-tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': [
            'network-tunnel'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {
                'enclosure': '1',
                'bay': '3',
                'port': 'Q2.1',
                'speed': 'Auto'},
        ]
    },
    'us_tagged': {
        'name': 'us-tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': [
            'net300',
            'net100'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {
                'enclosure': '1',
                'bay': '6',
                'port': 'Q2.1',
                'speed': 'Auto'},
        ]
    },
}
ligs = [
    {
        'name': LIG_NAME,
        'type': 'logical-interconnect-groupV300',
        'enclosureType': 'SY12000',
        'interconnectMapTemplate': icmap,
        'enclosureIndexes': [
            1],
        'interconnectBaySet': 3,
        'redundancyType': 'Redundant',
        'ethernetSettings': None,
        'fcoeSettings': {
            'fcoeMode': 'FcfNpv'},
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None,
        'uplinkSets': [
            uplink_sets[
                'us_untagged']
            .copy(),
            uplink_sets[
                'us_tunnel']
            .copy(),
            uplink_sets[
                'us_tagged']
            .copy()],
    },
]
egs = [
    {
        'name': EG_NAME,
        'type': 'EnclosureGroupV300',
        'enclosureCount': 1,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 2,
        'configurationScript': None,
        'interconnectBayMappings':
        [
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [
        ],
        'powerMode': "RedundantPowerFeed"
    }
]
les = [
    {
        'name': LE_NAME,
        'enclosureUris': [
            'ENC:' + ENC1],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
    }
]
# Negative tests
# Invalid profile initiator name
negative_profile1 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    "enclosureUri": "",
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile1",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": "NAME",
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Invalid boot initiator name
negative_profile2 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile2",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": "NAME",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Invalid virtual function, only second flexNic is supported for hardware iSCSI boot
negative_profile3 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile3",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-a",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Define secondary boot without primary boot
negative_profile4 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile4",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Multiple Primary boot connections
negative_profile5 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile5",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-1",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}}},
            {
                "id": 2,
                "name": "iSCSI-boot-2",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorSubnetMask": INITIATOR_SUBNET_MASK,
                        "initiatorGateway": INITIATOR_GATEWAY,
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "initiatorName": "",
                        "initiatorIp": PROFILE1_INITIATOR_IP_2,
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Multiple Secondary boot connections
negative_profile6 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile6",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-1",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}}},
            {
                "id": 2,
                "name": "iSCSI-boot-2",
                "functionType": "iSCSI",
                "portId": "Auto",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None}
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Network set in iSCSI boot connection
negative_profile7 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile7",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'NS:NS1',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "initiatorName": "",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }}},
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "PXE"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Invalid bootVlanId in untagged network
negative_profile8 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile8",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "bootVlanId": "1",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": "tbird9-bay1",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Invalid bootVlanId for tunnel network
negative_profile9 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile9",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "bootVlanId": "8000",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": "tbird9-bay1",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Primary iSCSI boot connection on Mezz3:1b to tunnel network
# Primary PXE boot connection on Mezz3:2b
negative_profile10 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile10",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iscsi-boot",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }}},
            {
                "id": 2,
                "name": "pxe-boot",
                "functionType": "Ethernet",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE"}
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Primary iSCSI HW boot connection on Mezz3:1b to tunnel network
# Primary iSCSI SW boot connection on Mezz3:2a
negative_profile11 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": "negative-profile11",
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iscsi-hw-boot",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }}},
            {
                "id": 2,
                "name": "is-sw-boot",
                "functionType": "Ethernet",
                "portId": "Mezz 3:2-a",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "ethernetBootType": "iSCSI",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_profile_initiator_name'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_boot_initiator_name'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_functionType'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile5.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_iscsi'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Boot_VLAN_Id_Only_Tunnel'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile9.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invaid_initiator_vlan_id_for_tunnel_network'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile10.copy(),
        'taskState': 'Error',
        'errorMessage': 'Boot_VLAN_Id_Only_Tunnel'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_profile11.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot'}
]
# Positive tests
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2b to tunnel network
profile1_iscsi_one_connection_tunnel = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iscsi-boot",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile1: ENC1 bay 1, Blackbird
# Static with gateway unset. OV will set gateway to 0.0.0.0
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:1b to untagged network
# CHAP
profile1_one_connection_legacy_bios = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
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
            "CD",
            "USB",
            "PXE",
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile1: ENC1 bay 1, Blackbird
# Static with gateway unset. OV will set gateway to 0.0.0.0
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2b to untagged network
# CHAP
profile1_one_connection_ip1 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
profile1_one_connection_ip1_verify = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                    }
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Profile1: ENC1 bay 1, Blackbird
# Static with gateway unset. OV will set gateway to 0.0.0.0
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2b to tunnel network, initiator IP updated
# CHAP
profile1_one_connection_ip2 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile1: ENC1 bay 1, blackbird
# static with gateway unset. OV will set gateway to 0.0.0.0
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2b to untagged network and secondary on Mezz3:1b to tunnel network
# CHAP
profile1_two_connections = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }}},
            {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile1: ENC1 bay 6, Redbird
# Static with gateway unset. OV will set gateway to 0.0.0.0
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz3:2b to untagged network
# CHAP
profile2_one_connection_legacy_bios = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY6,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "Chap",
                        "chapName": PROFILE2_CHAP_NAME,
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
            "CD",
            "USB",
            "PXE",
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile2: ENC1 bay6, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary iSCSI boot connection on 3:1b using tunnel network
profile2_iscsi_one_connection_tunnel = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY6,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE2_INITIATOR_NAME,
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap",
                        "chapName": PROFILE2_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": PROFILE2_MCHAP_NAME,
                        "mutualChapSecret": MCHAP_SECRET
                    }
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile2: ENC1 bay6, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary iSCSI boot connection on 3:1b and secondary on  3:2b to untagged network
# MCHAP
profile2_two_connections = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY6,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE2_INITIATOR_NAME,
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap",
                        "chapName": PROFILE2_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": PROFILE2_MCHAP_NAME,
                        "mutualChapSecret": MCHAP_SECRET
                    }
                }
            },
            {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE2_INITIATOR_NAME,
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap",
                        "chapName": PROFILE2_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": PROFILE2_MCHAP_NAME,
                        "mutualChapSecret": MCHAP_SECRET
                    }
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile2: ENC1 bay6, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary boot connection on 3:1b on untagged network
# MCHAP
profile2_one_connection_ip1 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY6,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE2_INITIATOR_NAME,
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap",
                        "chapName": PROFILE2_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": PROFILE2_MCHAP_NAME,
                        "mutualChapSecret": MCHAP_SECRET
                    }
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
}
# Profile2: ENC1 bay6, Redbird
# Profile initiator name is user-defined
# Primary unbootable connection on 3:1b and secondary connection on 3:2b to untagged network=
profile2_two_unbootable_connections = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY6,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "boot": {
                    "priority": "NotBootable"}},
            {
                "id": 2,
                "name": "",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "boot": {
                    "priority": "NotBootable"}
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "PXE"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
}
# Profile2: ENC1 bay6, Redbird
# static with gateway set to 192.168.0.1
# Connection initiator name is user defined
# Profile initiator name is user-defined
# Primary boot connection on 3:1b to tunnel network
# MCHAP
profile2_one_connection_ip2 = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY6,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE2_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE2_INITIATOR_NAME,
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "MutualChap",
                        "chapName": PROFILE2_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": PROFILE2_MCHAP_NAME,
                        "mutualChapSecret": MCHAP_SECRET
                    }
                }
            }
        ]
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
}
# Profile3: profile2 moved from ECN1 bay6 to ENC1 bay2
# static with gateway set to 192.168.0.1
# Connection initiator name uses profile initiator name.
# Profile initiator name is user defined
# Primary boot connection on Mezz3:1b to tunnel network and secondary on Mezz3:2b to untagged network
# NO CHAP
profile3_two_connections = {
    "type": "ServerProfileV9",
    "serverHardwareUri": 'SH:' + ENC1SHBAY2,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE2_NAME,
    "description": "",
    "affinity": "Bay",
    "connectionSettings": {
        "connections": [
            {
                "id": 1,
                "name": "iSCSI-boot-primary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:1-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-tunnel',
                "ipv4": {
                    "ipAddress": PROFILE3_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
                        "mutualChapName": "",
                        "mutualChapSecret": None
                    }}},
            {
                "id": 2,
                "name": "iSCSI-boot-secondary",
                "functionType": "iSCSI",
                "portId": "Mezz 3:2-b",
                "requestedMbps": "2500",
                "networkUri": 'ETH:network-untagged',
                "ipv4": {
                    "ipAddress": PROFILE3_INITIATOR_IP_2,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE3_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                        "chapName": "",
                        "chapSecret": None,
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
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# hpMCTP Data
hpMCTP_profile1_iscsi_one_connection_tunnel = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 33</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
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
}
hpMCTP_profile2_iscsi_one_connection_tunnel = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY6,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay6</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 34</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol</iscsi-target-name>
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
<iscsi-chap-username>tbird9-bay6</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username>tbird9-bay6</iscsi-mutual-username>
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile1_two_connections = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 33</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username></iscsi-mutual-username>
<iscsi-mutual-secret></iscsi-mutual-secret>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 38</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
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
}
hpMCTP_profile2_two_connections = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY6,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay6</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 34</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol</iscsi-target-name>
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
<iscsi-chap-username>tbird9-bay6</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username>tbird9-bay6</iscsi-mutual-username>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay6</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 39</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol</iscsi-target-name>
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
<iscsi-chap-username>tbird9-bay6</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username>tbird9-bay6</iscsi-mutual-username>
<iscsi-mutual-secret>68 70 76 73 65 31 32 33 77 70 73 74</iscsi-mutual-secret>
<deprecated-b1><false/></deprecated-b1>
<deprecated-b2><false/></deprecated-b2>
</authentication>
</config-nextDLR-type>
</active-cfg-cats-RO>
<pending-cfg-cats-RW>
</pending-cfg-cats-RW>
</ISCSI-Boot-Cats>"""
}
hpMCTP_profile1_no_iscsi = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile2_no_iscsi = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY6,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile3_no_iscsi = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY2,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id>ASI</iscsi-dhcp-vendor-id>
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
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id>ASI</iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile1_iscsi_one_connection_legacy_bios = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 33</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username></iscsi-mutual-username>
<iscsi-mutual-secret></iscsi-mutual-secret>
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
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile1_one_connection_ip1 = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 33</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
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
}
hpMCTP_profile2_one_connection_ip1 = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY6,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay6</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 34</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol</iscsi-target-name>
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
<iscsi-chap-username>tbird9-bay6</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username>tbird9-bay6</iscsi-mutual-username>
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile1_one_connection_ip2 = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 38</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
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
}
hpMCTP_profile2_iscsi_one_connection_legacy_bios = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY6,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay6</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 34</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol</iscsi-target-name>
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
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay6</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
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
}
hpMCTP_profile2_one_connection_ip2 = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY6,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay6</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 39</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1061:tbird9-bay6-bootvol</iscsi-target-name>
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
<iscsi-chap-username>tbird9-bay6</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
<iscsi-mutual-username>tbird9-bay6</iscsi-mutual-username>
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
}
hpMCTP_profile3_two_connections = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY2,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay2</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 3D</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol</iscsi-target-name>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay2</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 3E</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1064:tbird9-bay2-bootvol</iscsi-target-name>
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
}
F1162_hpMCTP_after_create_sp_from_spt = {
    "hpmctpIp": hpmctp_credentials[
        'ip'],
    "hpmctpUsername": hpmctp_credentials[
        'username'],
    "hpmctpPassword": hpmctp_credentials[
        'password'],
    "serverName": "SH:" + ENC1SHBAY1,
    "iloUsername": ilo_credentials[
        'username'],
    "iloPassword": ilo_credentials[
        'password'],
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
<iscsi-initiator-name>none</iscsi-initiator-name>
<iscsi-initiator-ip-addr>00 00 00 00</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>00 00 00 00</iscsi-initiator-netmask>
<iscsi-initiator-route></iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>none</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>00 00 00 00</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2></iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id></iscsi-dhcp-vendor-id>
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
<iscsi-initiator-name>iqn.2015-02.com.hpe:oneview-tbird9-bay1</iscsi-initiator-name>
<iscsi-initiator-ip-addr>C0 A8 16 33</iscsi-initiator-ip-addr>
<iscsi-initiator-netmask>FF FF C0 00</iscsi-initiator-netmask>
<iscsi-initiator-route>C0 A8 00 01</iscsi-initiator-route>
<iscsi-primary-dns></iscsi-primary-dns>
<iscsi-second-dns></iscsi-second-dns>
</iscsi-initiator-cfg>
<iscsi-target-params>
<iscsi-target-name>iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:1058:tbird9-bay1-bootvol</iscsi-target-name>
<iscsi-LUN>0</iscsi-LUN>
<iscsi-target-ip>C0 A8 15 47</iscsi-target-ip>
<iscsi-target-tcpport>3260</iscsi-target-tcpport>
<iscsi-target-ip2>C0 A8 15 48</iscsi-target-ip2>
<iscsi-target-tcpport2>3260</iscsi-target-tcpport2>
<iscsi-LLMNR-enable><false/></iscsi-LLMNR-enable>
<iscsi-route-advertisement-enable><false/></iscsi-route-advertisement-enable>
</iscsi-target-params>
<iscsi-dhcp-vendor-id>none</iscsi-dhcp-vendor-id>
<authentication>
<iscsi-authentic-meth><chap/></iscsi-authentic-meth>
<iscsi-chap-username>tbird9-bay1</iscsi-chap-username>
<iscsi-chap-secret>77 70 73 74 68 70 76 73 65 31 32 33</iscsi-chap-secret>
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
}
# Sever Profile Template Data
# Verify Create Server Profile Template
# iSCSI primary only
spt_1 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt1_primary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'firstBootTargetIp': FIRST_BOOT_TARGET_IP,
                        'firstBootTargetPort': '3260',
                        'secondBootTargetIp': SECOND_BOOT_TARGET_IP,
                        'secondBootTargetPort': '3260',
                        'chapLevel': 'Chap'
                    }
                }
            }
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# iSCSI primary and secondary
spt_2 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt2_primary_secondary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'firstBootTargetIp': FIRST_BOOT_TARGET_IP,
                        'firstBootTargetPort': '3260',
                        'secondBootTargetIp': SECOND_BOOT_TARGET_IP,
                        'secondBootTargetPort': '3260',
                        'chapLevel': 'MutualChap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-tunnel',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'MutualChap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
spt_2_edit = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt2_primary_secondary',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-tunnel',
                "ipv4": {
                    "subnetMask": "255.255.255.0",
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'ProfileInitiatorName',
                        'firstBootTargetIp': SECOND_BOOT_TARGET_IP,
                        'firstBootTargetPort': '3261',
                        'secondBootTargetIp': "",
                        'secondBootTargetPort': '',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": "255.255.255.0",
                    "gateway": ""
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'ProfileInitiatorName',
                        'firstBootTargetIp': FIRST_BOOT_TARGET_IP,
                        'firstBootTargetPort': '3260',
                        'secondBootTargetIp': SECOND_BOOT_TARGET_IP,
                        'secondBootTargetPort': '3260',
                        'chapLevel': "None"
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# iSCSI primary only UEFI optimized
spt_3 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt3_primary_uefioptimized',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# iSCSI primary and secondary UEFI optimized
spt_4 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt4_primary_secondary_uefioptimized',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-tunnel',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# iSCSI primary and secondary UEFI optimized
spt_5 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt5_primary_secondary_no_chap',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'None'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'None'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# iSCSI primary only, Legacy Bios
spt_6_legacy_bios = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt6_primary_legacy_bios',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'firstBootTargetIp': FIRST_BOOT_TARGET_IP,
                        'firstBootTargetPort': '3260',
                        'secondBootTargetIp': SECOND_BOOT_TARGET_IP,
                        'secondBootTargetPort': '3260',
                        'chapLevel': 'Chap'
                    }
                }
            }
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# iSCSI primary and secondary, Legacy Bios
spt_7_legacy_bios = {
    'type': 'ServerProfileTemplateV5',
    'name': 'spt7_primary_secondary_legacy_bios',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'firstBootTargetIp': FIRST_BOOT_TARGET_IP,
                        'firstBootTargetPort': '3260',
                        'secondBootTargetIp': SECOND_BOOT_TARGET_IP,
                        'secondBootTargetPort': '3260',
                        'chapLevel': 'MutualChap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-tunnel',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'MutualChap'
                    }
                }
            },
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
sp_from_spt = [
    {
        'type': 'ServerProfileV9',
        'name': 'sp_from_spt1',
        'serverProfileTemplateUri': 'SPT:spt1_primary',
        "serverHardwareUri": 'SH:' + ENC1SHBAY1,
        'enclosureGroupUri': 'EG:%s' % EG_NAME,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE1_INITIATOR_NAME,
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": SECOND_BOOT_TARGET_IP,
                        "secondBootTargetPort": "3260",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET
                    }
                }
            },
        ],
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
            'overriddenSettings': [
            ]
        },
        'localStorage': {
            'sasLogicalJBODs': [
            ],
            'controllers': [
            ]
        },
        'sanStorage': {
            'manageSanStorage': False,
            'volumeAttachments': [
            ]
        }
    }
]
sp_from_spt_power = [
    {
        'type': 'ServerProfileV9',
        'name': 'sp_from_spt1',
        'serverProfileTemplateUri': 'SPT:spt1_primary',
        'serverHardwareUri': 'SH:' + ENC1SHBAY1,
        'enclosureGroupUri': 'EG:%s' % EG_NAME,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE1_INITIATOR_NAME,
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": SECOND_BOOT_TARGET_IP,
                        "secondBootTargetPort": "3260",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET
                    }
                }
            },
        ],
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
            'overriddenSettings': [
            ]
        },
        'localStorage': {
            'sasLogicalJBODs': [
            ],
            'controllers': [
            ]
        },
        'sanStorage': {
            'manageSanStorage': False,
            'volumeAttachments': [
            ]
        }
    }
]
delete_sp_from_spt = [
    {
        'type': 'ServerProfileV9',
        'name': 'sp_from_spt1',
        'serverProfileTemplateUri': 'SPT:spt1_primary',
        'serverHardwareUri': 'SH:' + ENC1SHBAY1,
        'enclosureGroupUri': 'EG:%s' % EG_NAME,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE1_INITIATOR_NAME,
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": SECOND_BOOT_TARGET_IP,
                        "secondBootTargetPort": "3260",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                        "chapSecret": CHAP_SECRET
                    }
                }
            },
        ],
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
            'overriddenSettings': [
            ]
        },
        'localStorage': {
            'sasLogicalJBODs': [
            ],
            'controllers': [
            ]
        },
        'sanStorage': {
            'manageSanStorage': False,
            'volumeAttachments': [
            ]
        }
    }
]
sp_from_spt_verify = [
    {
        'type': 'ServerProfileV9',
        'name': 'sp_from_spt1',
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "ipAddress": PROFILE1_INITIATOR_IP_1,
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "UserDefined",
                        "initiatorName": PROFILE1_INITIATOR_NAME,
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": SECOND_BOOT_TARGET_IP,
                        "secondBootTargetPort": "3260",
                        "chapLevel": "Chap",
                        "chapName": PROFILE1_CHAP_NAME,
                    }
                }
            },
        ],
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
            'overriddenSettings': [
            ]
        },
        'localStorage': {
            'sasLogicalJBODs': [
            ],
            'controllers': [
            ]
        },
        'sanStorage': {
            'manageSanStorage': False,
            'volumeAttachments': [
            ]
        }
    }
]
# Verify Network Sets are NOT Supported during Create Server Profile
# Template with iSCSI SW Boot
negative_spt1 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_1',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'NS:NS1',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Verify Network Sets are NOT Supported during Create Server Profile
# Template with iSCSI SW Boot
negative_spt2 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_2',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'NS:NS1',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Verify Cannot Create Server Profile Template with only iSCSI Secondary
# Boot Mode
negative_spt3 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_3',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Verify Cannot Create Server Profile Template with multiple primary or
# secondary
negative_spt4 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_4',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Verify Cannot Create Server Profile Template with multiple primary or
# secondary
negative_spt5 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_5',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Verify Required Fields
negative_spt6 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_6',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": "",
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                'functionType': 'iSCSI',
                'portId': 'Auto',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": INITIATOR_GATEWAY
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Primary iSCSI HW boot connection on Mezz3:1b to tunnel network
# Primary iSCSI SW boot connection on Mezz3:2a
negative_spt7 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_7',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                "name": "iscsi-hw-boot",
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net100',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                "name": "iscsi-sw-boot",
                'functionType': 'Ethernet',
                'portId': 'Mezz 3:2-a',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "UserDefined",
                    "ethernetBootType": "iSCSI",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Primary iSCSI boot connection on Mezz3:1b to tunnel network
# Primary PXE boot connection on Mezz3:2b
negative_spt8 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_8',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                "name": "iscsi-boot",
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:1-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-tunnel',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        'initiatorNameSource': 'UserDefined',
                        'chapLevel': 'Chap'
                    }
                }
            },
            {
                'id': 2,
                "name": "pxe-boot",
                'functionType': 'Ethernet',
                'portId': 'Mezz 3:2-b',
                'requestedMbps': 2500,
                'networkUri': 'ETH:net300',
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "PXE"}
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
# Invalid virtual function, only second flexNic is supported for hardware iSCSI boot
negative_spt9 = {
    'type': 'ServerProfileTemplateV5',
    'name': 'negative_spt_9',
    'serverHardwareTypeUri': 'SHT:SY 480 Gen9 1',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [
            {
                'id': 1,
                'functionType': 'iSCSI',
                'portId': 'Mezz 3:2-a',
                'requestedMbps': 2500,
                'networkUri': 'ETH:network-untagged',
                "ipv4": {
                    "subnetMask": INITIATOR_SUBNET_MASK,
                    "gateway": ""
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "secondBootTargetIp": "",
                        "secondBootTargetPort": "",
                        "chapLevel": "None",
                    }
                }
            },
        ],
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
        'overriddenSettings': [
        ]
    },
    'localStorage': {
        'sasLogicalJBODs': [
        ],
        'controllers': [
        ]
    },
    'sanStorage': {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_iscsi'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_iscsi'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt5.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt6.copy(),
        'taskState': 'Error',
        'errorMessage': 'Boot_initiator_subnet_required'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt7.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt8.copy(),
        'taskState': 'Error',
        'errorMessage': 'iSCSI_Ethernet_on_same_Virtual_Function'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt9.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_functionType'},
    {
        'keyword': 'Fusion Api Delete Server Profile Template',
        'argument': 'spt1_primary',
        'taskState': 'Error',
        'errorMessage': 'Referenced_by_server_profile'},
]
create_profile_templates = [
    spt_1.copy(),
    spt_2.copy(),
    spt_3.copy(),
    spt_4.copy(),
    spt_5.copy(),
    spt_6_legacy_bios.copy(),
    spt_7_legacy_bios.copy(),
]
delete_profile_templates = [
    'spt1_primary',
    'spt2_primary_secondary',
    'spt3_primary_uefioptimized',
    'spt4_primary_secondary_uefioptimized',
    'spt5_primary_secondary_no_chap',
    'spt6_primary_legacy_bios',
    'spt7_primary_secondary_legacy_bios',
]
delete_profile = [
    {
        'type': 'ServerProfileTemplateV5',
        'name': 'spt1_primary',
        'serverHardwareTypeUri': 'SHT:SY 660 Gen9 ',
        "serverHardwareUri": 'SH:' + ENC1SHBAY1,
        'enclosureGroupUri': 'EG:%s' % EG_NAME,
        "connectionSettings": {
            "manageConnections": True,
            'connections': [
                {
                    'id': 1,
                    'functionType': 'iSCSI',
                    'portId': 'Mezz 3:2-b',
                    'requestedMbps': 2500,
                    'networkUri': 'ETH:net100',
                    'boot': {
                        'priority': 'Primary',
                        'initiatorNameSource': 'UserDefined',
                        'initiatorSubnetMask': '255.255.192.0',
                        'initiatorGateway': '192.168.1.1',
                        'firstBootTargetIp': '192.168.21.72',
                        'firstBootTargetPort': '3260',
                        'secondBootTargetIp': '192.168.22.73',
                        'secondBootTargetPort': '3260',
                        'chapLevel': 'Chap'
                    }
                },
            ],
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
            'overriddenSettings': [
            ]
        },
        'localStorage': {
            'sasLogicalJBODs': [
            ],
            'controllers': [
            ]
        },
        'sanStorage': {
            'manageSanStorage': False,
            'volumeAttachments': [
            ]
        }
    }
]
# Profile with Version API V300 DTO
profile300 = {
    "type": "ServerProfileV6",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connections": [
        {
            "id": 1,
            "name": "iSCSI-boot-primary",
            "functionType": "iSCSI",
            "portId": "Mezz 3:2-b",
            "requestedMbps": "2500",
            "networkUri": 'ETH:network-untagged',
            "boot": {
                "priority": "Primary",
                "initiatorNameSource": "ProfileInitiatorName",
                "initiatorIp": PROFILE1_INITIATOR_IP_1,
                "initiatorSubnetMask": INITIATOR_SUBNET_MASK,
                "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                "bootTargetLun": "0",
                "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                "firstBootTargetPort": "3260",
                "secondBootTargetIp": "",
                "secondBootTargetPort": "",
                "chapLevel": "Chap",
                "chapName": PROFILE1_CHAP_NAME,
                "chapSecret": CHAP_SECRET,
            },
        }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]
    }
}
profile300_verify = {
    "type": "ServerProfileV6",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "iscsiInitiatorNameType": "UserDefined",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connections": [
        {
            "id": 1,
            "name": "iSCSI-boot-primary",
            "functionType": "iSCSI",
            "portId": "Mezz 3:2-b",
            "requestedMbps": "2500",
            "networkUri": 'ETH:network-untagged',
            "boot": {
                "priority": "Primary",
                "initiatorNameSource": "ProfileInitiatorName",
                "initiatorIp": PROFILE1_INITIATOR_IP_1,
                "initiatorSubnetMask": INITIATOR_SUBNET_MASK,
                "bootTargetName": PROFILE1_BOOT_TARGET_NAME,
                "bootTargetLun": "0",
                "firstBootTargetIp": FIRST_BOOT_TARGET_IP,
                "firstBootTargetPort": "3260",
                "secondBootTargetIp": "",
                "secondBootTargetPort": "",
                "chapLevel": "Chap",
                "chapName": PROFILE1_CHAP_NAME,
            },
        }
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
# Profile with Version API V200 DTO
profile200_verify = {
    "type": "ServerProfileV5",
    "serverHardwareUri": 'SH:' + ENC1SHBAY1,
    'enclosureUri': 'ENC:' + ENC1,
    "enclosureGroupUri": "EG:" + EG_NAME,
    "serialNumberType": "Physical",
    "macType": "Physical",
    "wwnType": "Physical",
    "name": PROFILE1_NAME,
    "description": "",
    "affinity": "Bay",
    "connections": [
    ],
    "boot": {
        "manageBoot": True,
        "order": [
            "HardDisk"]},
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"},
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None,
        "forceInstallFirmware": False,
        "firmwareInstallType": None},
    "bios": {
        "manageBios": False,
        "overriddenSettings": [
        ]},
    "hideUnusedFlexNics": True,
    "localStorage": {
        "sasLogicalJBODs": [
        ],
        "controllers": [
        ]},
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [
        ]}
}
ts1_create_profiles = [
    profile1_iscsi_one_connection_tunnel.copy(),
    profile2_iscsi_one_connection_tunnel.copy()
]
ts1_edit_profiles_1 = [
    profile1_two_connections.copy(),
    profile2_two_connections.copy()]
ts1_edit_profiles_2 = [
    profile1_iscsi_one_connection_tunnel.copy(),
    profile2_iscsi_one_connection_tunnel.copy()]
ts1_delete_profiles = [
    profile1_iscsi_one_connection_tunnel.copy(),
    profile2_iscsi_one_connection_tunnel.copy()]
ts1_all_profiles = [
    profile1_iscsi_one_connection_tunnel.copy(),
    profile2_iscsi_one_connection_tunnel.copy()]
ts2_create_profiles = [
    profile1_one_connection_legacy_bios.copy(),
    profile2_two_connections.copy()]
ts2_edit_profiles_1 = [
    profile1_one_connection_ip1.copy(),
    profile2_one_connection_ip1.copy()]
ts2_edit_profiles_2 = [
    profile1_one_connection_ip2.copy(),
    profile2_one_connection_legacy_bios.copy()]
ts2_edit_profiles_3 = [
    profile1_two_connections.copy(),
    profile2_one_connection_ip2.copy()]
ts2_move_profiles = [
    profile3_two_connections.copy()]
ts2_delete_profiles = [
    profile1_two_connections.copy(),
    profile3_two_connections.copy()]
ts2_all_profiles = [
    profile1_two_connections.copy(),
    profile2_two_connections.copy(),
    profile3_two_connections.copy()]
ts1_hpMCTP_after_create = [
    hpMCTP_profile1_iscsi_one_connection_tunnel.copy(),
    hpMCTP_profile2_iscsi_one_connection_tunnel.copy(),
]
ts1_hpMCTP_after_edit_1 = [
    hpMCTP_profile1_two_connections.copy(),
    hpMCTP_profile2_two_connections.copy(),
]
ts1_hpMCTP_after_edit_2 = [
    hpMCTP_profile1_iscsi_one_connection_tunnel.copy(),
    hpMCTP_profile2_iscsi_one_connection_tunnel.copy(),
]
ts1_hpMCTP_after_delete = [
    hpMCTP_profile1_no_iscsi.copy(),
    hpMCTP_profile2_no_iscsi.copy(),
]
ts2_hpMCTP_after_create = [
    hpMCTP_profile1_iscsi_one_connection_legacy_bios.copy(),
    hpMCTP_profile2_two_connections.copy(),
]
ts2_hpMCTP_after_edit_1 = [
    hpMCTP_profile1_one_connection_ip1.copy(),
    hpMCTP_profile2_one_connection_ip1.copy(),
]
ts2_hpMCTP_after_edit_2 = [
    hpMCTP_profile1_one_connection_ip2.copy(),
    hpMCTP_profile2_iscsi_one_connection_legacy_bios.copy(),
]
ts2_hpMCTP_after_edit_3 = [
    hpMCTP_profile1_two_connections.copy(),
    hpMCTP_profile2_one_connection_ip2.copy(),
]
ts2_hpMCTP_after_move = [
    hpMCTP_profile3_two_connections.copy(),
]
ts2_hpMCTP_after_delete = [
    hpMCTP_profile1_no_iscsi.copy(),
    hpMCTP_profile2_no_iscsi.copy(),
    hpMCTP_profile3_no_iscsi.copy(),
]
version400 = [
    profile1_one_connection_ip1.copy()]
version300 = [
    profile300.copy()]

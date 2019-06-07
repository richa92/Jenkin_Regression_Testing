from robot.libraries.BuiltIn import BuiltIn

admin_credentials = {'userName': 'Administrator',
                     'password': 'wpsthpvse1'
                     }

oa_credentials = {'username': 'Administrator',
                  'password': 'hpvse14'
                  }

ilo_credentials = {'username': 'Administrator',
                   'password': 'hpvse1-ilo'
                   }

cliq_credentials = {'mgmt_ip': '16.71.148.116',
                    'username': 'admin',
                    'password': 'admin'
                    }

user_specified_cliq_credentials = {'mgmt_ip': '16.71.149.173',
                                   'username': 'admin',
                                   'password': 'admin'
                                   }

dhcp_managed_cluster = {'ip': '16.71.148.116',
                        'username': 'admin',
                        'password': 'admin',
                        'network': 'network-untagged',
                        'clusterName': 'VSA_Cluster_116'
                        }

# LIGs and EGs
LIG_NAME = 'LIG1'
EG_NAME = 'EG1'

# Enclosures
ENC1 = 'wpst10'
ENC1_OA1 = "Wpst10-oa1.vse.rdlabs.hpecorp.net"

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC1ICBAY7 = '%s, interconnect 7' % ENC1
ENC1ICBAY8 = '%s, interconnect 8' % ENC1

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY2 = '%s, bay 2' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY8 = '%s, bay 8' % ENC1
ENC1SHBAY9 = '%s, bay 9' % ENC1

# MANAGED VOLUMES
BAY2_VOLUME_NAME = 'wpst10-bay2-dhcp-managed-volume'
BAY3_VOLUME_NAME = 'wpst10-bay3-dhcp-managed-volume'
BAY4_VOLUME_NAME = 'wpst10-bay4-dhcp-managed-volume'
BAY7_VOLUME_NAME = 'wpst10-bay7-dhcp-managed-volume'
BAY8_VOLUME_NAME = 'wpst10-bay8-dhcp-managed-volume'

# iSCSI
INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"
DHCP_BOOT_TARGET_IP = "192.168.21.59"
USER_SPECIFIED_BOOT_TARGET_IP = "192.168.21.71"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"


# BAY2_PROFILE1: profile on ENC1 bay2, BL460c Gen8 DHCP Initiator
BAY2_PROFILE1_NAME = "wpst10-bay2"
BAY2_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp'
BAY2_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

# BAY2_PROFILE2: profile on ENC1 bay2, BL460c Gen8 User Specified Initiator with MCHAP
BAY2_PROFILE2_NAME = "wpst10-bay2"
BAY2_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:816:wpst10-bay2-bootvol'
BAY2_PROFILE2_INITIATOR_IP_1 = "192.168.22.124"
BAY2_PROFILE2_INITIATOR_IP_2 = "192.168.22.125"
BAY2_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay2"
BAY2_PROFILE2_CHAP_NAME = 'wpst10-bay2'
BAY2_PROFILE2_MCHAP_NAME = 'wpst10-bay2'

# BAY2_PROFILE3: profile on ENC1 bay2, BL460c Gen8 DHCP managed volume
BAY2_PROFILE3_NAME = "wpst10-bay2"
BAY2_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp-managed-volume"


# BAY3_PROFILE1: profile on ENC1 bay3, BL460c Gen8 DHCP Initiator with CHAP
BAY3_PROFILE1_NAME = "wpst10-bay3"
BAY3_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp'
BAY3_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"
BAY3_PROFILE1_CHAP_NAME = 'wpst10-bay3'

# BAY3_PROFILE2: profile on ENC1 bay3, BL460c Gen8 User Specified Initiator
BAY3_PROFILE2_NAME = "wpst10-bay3"
BAY3_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:5675:wpst10-bay3-bootvol'
BAY3_PROFILE2_INITIATOR_IP_1 = "192.168.22.128"
BAY3_PROFILE2_INITIATOR_IP_2 = "192.168.22.129"
BAY3_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay3"

# BAY3_PROFILE3: profile on ENC1 bay3, BL460c Gen8 DHCP managed volume
BAY3_PROFILE3_NAME = "wpst10-bay3"
BAY3_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp-managed-volume"


# BAY4_PROFILE1: profile on ENC1 bay4, BL460c Gen9 DHCP Initiator
BAY4_PROFILE1_NAME = "wpst10-bay4"
BAY4_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:153:wpst10-bay4-dhcp'
BAY4_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp"

# BAY4_PROFILE2: profile on ENC1 bay4, BL460c Gen9 User Specified Initiator with CHAP
BAY4_PROFILE2_NAME = "wpst10-bay4"
BAY4_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:416:wpst10-bay4-vol1'
BAY4_PROFILE2_INITIATOR_IP_1 = "192.168.22.122"
BAY4_PROFILE2_INITIATOR_IP_2 = "192.168.22.123"
BAY4_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay4"
BAY4_PROFILE2_CHAP_NAME = 'wpst10-bay4'

# BAY4_PROFILE3: profile on ENC1 bay4, BL460c Gen9 DHCP managed volume
BAY4_PROFILE3_NAME = "wpst10-bay4"
BAY4_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume"


# BAY7_PROFILE1: profile on ENC1 bay7, BL660c Gen9 DHCP Initiator with CHAP
BAY7_PROFILE1_NAME = "wpst10-bay7"
BAY7_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp'
BAY7_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"
BAY7_PROFILE1_CHAP_NAME = 'wpst10-bay7'
BAY7_PROFILE1_MCHAP_NAME = 'wpst10-bay7'

# BAY7_PROFILE2: profile on ENC1 bay7, BL660c Gen9 User Specified Initiator
BAY7_PROFILE2_NAME = "wpst10-bay7"
BAY7_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol'
BAY7_PROFILE2_INITIATOR_IP_1 = "192.168.22.126"
BAY7_PROFILE2_INITIATOR_IP_2 = "192.168.22.127"
BAY7_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay7"

# BAY7_PROFILE3: profile on ENC1 bay7, BL660c Gen9 DHCP managed volume
BAY7_PROFILE3_NAME = "wpst10-bay7"
BAY7_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"


# BAY8_PROFILE1: profile on ENC1 bay8, BL460c Gen8 DHCP Initiator with CHAP
BAY8_PROFILE1_NAME = "wpst10-bay8"
BAY8_PROFILE1_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp'
BAY8_PROFILE1_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"
BAY8_PROFILE1_CHAP_NAME = 'wpst10-bay8'

# BAY8_PROFILE2: profile on ENC1 bay8, BL460c Gen8 User Specified Initiator
BAY8_PROFILE2_NAME = "wpst10-bay8"
BAY8_PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol'
BAY8_PROFILE2_INITIATOR_IP_1 = "192.168.22.130"
BAY8_PROFILE2_INITIATOR_IP_2 = "192.168.22.131"
BAY8_PROFILE2_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay8"

# BAY8_PROFILE3: profile on ENC1 bay8, BL460c Gen8 DHCP managed volume
BAY8_PROFILE3_NAME = "wpst10-bay8"
BAY8_PROFILE3_INITIATOR_NAME = "iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"


APP1_IPV4_ADDRESS = BuiltIn().get_variable_value("${APPLIANCE_IP}")
HOSTNAME = "wpst10"

appliance = {'type': 'ApplianceNetworkConfiguration',
             'applianceNetworks':
                 [{'device': 'eth0',
                   'macAddress': None,
                   'interfaceName': 'Appliance',
                   'activeNode': '1',
                   'unconfigure': False,
                   'ipv4Type': 'STATIC',
                   'app1Ipv4Addr': APP1_IPV4_ADDRESS,
                   'ipv6Type': 'UNCONFIGURE',
                   'ipv4Subnet': '255.255.240.0',
                   'ipv4Gateway': '16.114.208.1',
                   'hostname': HOSTNAME,
                   'confOneNode': True,
                   'domainName': 'vse.rdlabs.hpecorp.net',
                   'ipv4NameServers': ['16.125.25.81', '16.125.25.82', '16.125.24.20'],
                   'aliasDisabled': True}]}

timeandlocale = {'type': 'TimeAndLocale', 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

users = [{'userName': 'Serveradmin', 'password': 'Serveradmin', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]

licenses = [{'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
            {'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
            {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            {'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'},
            {'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
            {'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
            ]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': 'ethernet-networkV300',
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': 'ethernet-networkV300',
     'vlanId': 1,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
]

ligs = [{'name': LIG_NAME,
         'type': 'logical-interconnect-groupV3',
         'enclosureType': 'C7000',
         'interconnectMapTemplate': [{'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': 'HP VC 8Gb 24-Port FC Module'},
                                     ],
         'uplinkSets': [{'name': 'us-untagged',
                         'ethernetNetworkType': 'Untagged',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-untagged'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '1', 'port': 'X3', 'speed': 'Auto'}]},
                        {'name': 'us-tunnel',
                         'ethernetNetworkType': 'Tunnel',
                         'networkType': 'Ethernet',
                         'networkUris': ['network-tunnel'],
                         'nativeNetworkUri': None,
                         'mode': 'Auto',
                         'logicalPortConfigInfos': [{'bay': '2', 'port': 'X3', 'speed': 'Auto'}]},
                        ],
         'stackingMode': 'Enclosure',
         'ethernetSettings': None,
         'state': 'Active',
         'telemetryConfiguration': None,
         'snmpConfiguration': None},
        ]

enc_groups = [{'name': EG_NAME,
               'type': 'EnclosureGroupV300',
               'enclosureTypeUri': '/rest/enclosure-types/c7000',
               'stackingMode': 'Enclosure',
               'interconnectBayMappingCount': 8,
               'configurationScript': None,
               'interconnectBayMappings':
                   [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG_NAME},
                    {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG_NAME},
                    {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG_NAME},
                    {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG_NAME},
                    {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG_NAME},
                    {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG_NAME},
                    {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
                    {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}]
               },
              ]

encs = [{'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'], 'enclosureGroupUri': 'EG:' + EG_NAME,
         'force': True, 'licensingIntent': 'OneViewNoiLO'},
        ]


# Bay 2 Profile1 Two Connections: ENC1 bay 2, BL460c Gen8
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay2_profile1_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": BAY2_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "None",
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                             "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                             "iscsi": {
                                                 "initiatorNameSource": "ProfileInitiatorName",
                                                 "initiatorVlanId": "",
                                                 "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                 "firstBootTargetPort": "3260",
                                                 "bootTargetName": BAY2_PROFILE1_BOOT_TARGET_NAME,
                                                 "bootTargetLun": "0",
                                                 "chapLevel": "None",
                                                 "chapName": "",
                                                 "chapSecret": None,
                                                 "mutualChapName": "",
                                                 "mutualChapSecret": None
                                             }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY2_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Bay2 Profile1 One Connection Tunnel: ENC1 bay 2, BL460c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay2_profile1_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "DHCP",
                                                    "subnetMask": "",
                                                    "gateway": "",
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "UserDefined",
                                                        "initiatorName": BAY2_PROFILE1_INITIATOR_NAME,
                                                        "initiatorVlanId": "",
                                                        "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "bootTargetName": BAY2_PROFILE1_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "chapLevel": "None",
                                                        "chapName": "",
                                                        "chapSecret": None,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY2_PROFILE1_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }


# Bay2 Profile1 One Connection Untagged: ENC1 bay 2, BL460c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay2_profile1_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "UserDefined",
                                                          "initiatorName": BAY2_PROFILE1_INITIATOR_NAME,
                                                          "initiatorVlanId": "",
                                                          "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "bootTargetName": BAY2_PROFILE1_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "chapLevel": "None",
                                                          "chapName": "",
                                                          "chapSecret": None,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY2_PROFILE1_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 2 Profile2 Two Connections: ENC1 bay 2, BL460c Gen8
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay2_profile2_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY2_PROFILE2_INITIATOR_IP_1,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY2_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": "MutualChap",
                                                  "chapName": BAY2_PROFILE2_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": BAY2_PROFILE2_MCHAP_NAME,
                                                  "mutualChapSecret": MCHAP_SECRET
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY2_PROFILE2_INITIATOR_IP_2,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY2_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": "MutualChap",
                                                  "chapName": BAY2_PROFILE2_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": BAY2_PROFILE2_MCHAP_NAME,
                                                  "mutualChapSecret": MCHAP_SECRET
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY2_PROFILE2_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }

# Bay2 Profile2 One Connection Tunnel: ENC1 bay 2, BL460c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay2_profile2_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "UserDefined",
                                                    "ipAddress": BAY2_PROFILE2_INITIATOR_IP_1,
                                                    "subnetMask": INITIATOR_SUBNET_MASK,
                                                    "gateway": ""
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "ProfileInitiatorName",
                                                        "initiatorVlanId": "",
                                                        "bootTargetName": BAY2_PROFILE2_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "chapLevel": "MutualChap",
                                                        "chapName": BAY2_PROFILE2_CHAP_NAME,
                                                        "chapSecret": CHAP_SECRET,
                                                        "mutualChapName": BAY2_PROFILE2_MCHAP_NAME,
                                                        "mutualChapSecret": MCHAP_SECRET
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY2_PROFILE2_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }

# Bay2 Profile2 One Connection Untagged: ENC1 bay 2, BL460c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay2_profile2_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "UserDefined",
                                                      "ipAddress": BAY2_PROFILE2_INITIATOR_IP_1,
                                                      "subnetMask": INITIATOR_SUBNET_MASK,
                                                      "gateway": ""
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
                                                          "bootTargetName": BAY2_PROFILE2_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "chapLevel": "MutualChap",
                                                          "chapName": BAY2_PROFILE2_CHAP_NAME,
                                                          "chapSecret": CHAP_SECRET,
                                                          "mutualChapName": BAY2_PROFILE2_MCHAP_NAME,
                                                          "mutualChapSecret": MCHAP_SECRET
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY2_PROFILE2_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 2 Profile3 Two Connections: ENC1 bay 2, BL460c Gen8
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
bay2_profile3_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
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
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
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
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY2_PROFILE3_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                 "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                "volumeAttachments": [{
                                                    "id": 1,
                                                    "isBootVolume": True,
                                                    "lun": None,
                                                    "lunType": "Auto",
                                                    "storagePaths": [{
                                                        "isEnabled": True,
                                                        "connectionId": "1",
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }],
                                                    "volume": None,
                                                    "volumeUri": BAY2_VOLUME_NAME,
                                                }
                                                ]

                                                }}


# Bay2 Profile3 One Connection Untagged: ENC1 bay 2, BL460c Gen8
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
bay2_profile3_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY2_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                  "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
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
                                                      }}},
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY2_PROFILE3_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                         "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                        "volumeAttachments": [{
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lun": None,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": "1",
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeUri": BAY2_VOLUME_NAME,
                                                        }
                                                        ]

                                                        }}


# Bay 3 Profile1 Two Connections: ENC1 bay 3, BL460c Gen8
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay3_profile1_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "ipAddress": "",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY3_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY3_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "ipAddress": "",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY3_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY3_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Bay 3 Profile1 One Connection Tunnel: ENC1 bay 3, BL460c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay3_profile1_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "DHCP",
                                                    "subnetMask": "",
                                                    "gateway": "",
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "UserDefined",
                                                        "initiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                                                        "initiatorVlanId": "",
                                                        "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "bootTargetName": BAY3_PROFILE1_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "chapLevel": "Chap",
                                                        "chapName": BAY3_PROFILE1_CHAP_NAME,
                                                        "chapSecret": CHAP_SECRET,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }


# Bay 3 Profile1 One Connection Untagged: ENC1 bay 3, BL460c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay3_profile1_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "UserDefined",
                                                          "initiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                                                          "initiatorVlanId": "",
                                                          "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "bootTargetName": BAY3_PROFILE1_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "chapLevel": "Chap",
                                                          "chapName": BAY3_PROFILE1_CHAP_NAME,
                                                          "chapSecret": CHAP_SECRET,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 3 Profile2 Two Connections: ENC1 bay 3, BL460c Gen8
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay3_profile2_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY3_PROFILE2_INITIATOR_IP_1,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY3_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY3_PROFILE2_INITIATOR_IP_2,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY3_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY3_PROFILE2_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }

# Bay 3 Profile2 One Connection Tunnel: ENC1 bay 3, BL460c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay3_profile2_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "UserDefined",
                                                    "ipAddress": BAY3_PROFILE2_INITIATOR_IP_1,
                                                    "subnetMask": INITIATOR_SUBNET_MASK,
                                                    "gateway": ""
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "ProfileInitiatorName",
                                                        "initiatorVlanId": "",
                                                        "bootTargetName": BAY3_PROFILE2_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "chapLevel": None,
                                                        "chapName": "",
                                                        "chapSecret": None,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY3_PROFILE2_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }

# Bay 3 Profile2 One Connection Untagged: ENC1 bay 3, BL460c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay3_profile2_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "UserDefined",
                                                      "ipAddress": BAY3_PROFILE2_INITIATOR_IP_1,
                                                      "subnetMask": INITIATOR_SUBNET_MASK,
                                                      "gateway": ""
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
                                                          "bootTargetName": BAY3_PROFILE2_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "chapLevel": None,
                                                          "chapName": "",
                                                          "chapSecret": None,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY3_PROFILE2_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 3 Profile3 Two Connections: ENC1 bay 3, BL460c Gen8
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
bay3_profile3_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
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
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
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
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY3_PROFILE3_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                 "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                "volumeAttachments": [{
                                                    "id": 1,
                                                    "isBootVolume": True,
                                                    "lun": None,
                                                    "lunType": "Auto",
                                                    "storagePaths": [{
                                                        "isEnabled": True,
                                                        "connectionId": "1",
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }],
                                                    "volume": None,
                                                    "volumeUri": BAY3_VOLUME_NAME,
                                                }
                                                ]

                                                }}


# Bay 3 Profile3 One Connection Untagged: ENC1 bay 3, BL460c Gen8
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
bay3_profile3_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY3, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY3_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                  "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
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
                                                      }}},
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY3_PROFILE3_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                         "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                        "volumeAttachments": [{
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lun": None,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": "1",
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeUri": BAY3_VOLUME_NAME,
                                                        }
                                                        ]

                                                        }}


# Bay 4 Profile1 Two Connections: ENC1 bay 4, BL460c Gen9
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay4_profile1_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": BAY4_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY4_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY4_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Bay 4 Profile1 One Connection Tunnel: ENC1 bay 4, BL460c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay4_profile1_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "DHCP",
                                                    "subnetMask": "",
                                                    "gateway": "",
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "UserDefined",
                                                        "initiatorName": BAY4_PROFILE1_INITIATOR_NAME,
                                                        "initiatorVlanId": "",
                                                        "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "bootTargetName": BAY4_PROFILE1_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "chapLevel": None,
                                                        "chapName": "",
                                                        "chapSecret": None,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY4_PROFILE1_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }


# Bay 4 Profile1 One Connection Untagged: ENC1 bay 4, BL460c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay4_profile1_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "UserDefined",
                                                          "initiatorName": BAY4_PROFILE1_INITIATOR_NAME,
                                                          "initiatorVlanId": "",
                                                          "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "bootTargetName": BAY4_PROFILE1_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "chapLevel": None,
                                                          "chapName": "",
                                                          "chapSecret": None,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY4_PROFILE1_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 4 Profile2 Two Connections: ENC1 bay 4, BL460c Gen9
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay4_profile2_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY4_PROFILE2_INITIATOR_IP_1,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY4_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY4_PROFILE2_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY4_PROFILE2_INITIATOR_IP_2,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY4_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY4_PROFILE2_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY4_PROFILE2_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }

# Bay 4 Profile2 One Connection Tunnel: ENC1 bay 2, ENC1 bay 4, BL460c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay4_profile2_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "UserDefined",
                                                    "ipAddress": BAY4_PROFILE2_INITIATOR_IP_1,
                                                    "subnetMask": INITIATOR_SUBNET_MASK,
                                                    "gateway": ""
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "ProfileInitiatorName",
                                                        "initiatorVlanId": "",
                                                        "bootTargetName": BAY4_PROFILE2_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "chapLevel": "Chap",
                                                        "chapName": BAY4_PROFILE2_CHAP_NAME,
                                                        "chapSecret": CHAP_SECRET,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY4_PROFILE2_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }

# Bay 4 Profile2 One Connection Untagged: ENC1 bay 4, BL460c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay4_profile2_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "UserDefined",
                                                      "ipAddress": BAY4_PROFILE2_INITIATOR_IP_1,
                                                      "subnetMask": INITIATOR_SUBNET_MASK,
                                                      "gateway": ""
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
                                                          "bootTargetName": BAY4_PROFILE2_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "chapLevel": "Chap",
                                                          "chapName": BAY4_PROFILE2_CHAP_NAME,
                                                          "chapSecret": CHAP_SECRET,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY4_PROFILE2_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 4 Profile3 Two Connections: ENC1 bay 4, BL460c Gen9
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
bay4_profile3_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                          }},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                          }}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY4_PROFILE3_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                 "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                "volumeAttachments": [{
                                                    "id": 1,
                                                    "isBootVolume": True,
                                                    "lunType": "Auto",
                                                    "storagePaths": [{
                                                        "isEnabled": True,
                                                        "connectionId": 1,
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }, {
                                                        "isEnabled": True,
                                                        "connectionId": 2,
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }],
                                                    "volume": None,
                                                    "volumeUri": "SVOL:" + BAY4_VOLUME_NAME,
                                                }
                                                ]

                                                }}


# Bay 4 Profile3 One Connection Untagged: ENC1 bay 4, BL460c Gen9
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
bay4_profile3_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY4, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY4_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                  "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
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
                                                      }}},
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY4_PROFILE3_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                         "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                        "volumeAttachments": [{
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lun": None,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": "1",
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeUri": BAY4_VOLUME_NAME,
                                                        }
                                                        ]

                                                        }}


# Bay 7 Profile1 Two Connections: ENC1 bay 7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay7_profile1_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY7_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": BAY7_PROFILE1_MCHAP_NAME,
                                                  "mutualChapSecret": MCHAP_SECRET
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "MutualChap",
                                                  "chapName": BAY7_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": BAY7_PROFILE1_MCHAP_NAME,
                                                  "mutualChapSecret": MCHAP_SECRET
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Bay 7 Profile1 One Connection Tunnel: ENC1 bay 7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay7_profile1_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "DHCP",
                                                    "subnetMask": "",
                                                    "gateway": "",
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "UserDefined",
                                                        "initiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                                        "initiatorVlanId": "",
                                                        "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "chapLevel": "MutualChap",
                                                        "chapName": BAY7_PROFILE1_CHAP_NAME,
                                                        "chapSecret": CHAP_SECRET,
                                                        "mutualChapName": BAY7_PROFILE1_MCHAP_NAME,
                                                        "mutualChapSecret": MCHAP_SECRET
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }


# Bay 7 Profile1 One Connection Untagged: ENC1 bay 7, BL660c Gen9
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay7_profile1_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "UserDefined",
                                                          "initiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                                          "initiatorVlanId": "",
                                                          "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "chapLevel": "MutualChap",
                                                          "chapName": BAY7_PROFILE1_CHAP_NAME,
                                                          "chapSecret": CHAP_SECRET,
                                                          "mutualChapName": BAY7_PROFILE1_MCHAP_NAME,
                                                          "mutualChapSecret": MCHAP_SECRET
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 7 Profile2 Two Connections: ENC1 bay 7, BL660c Gen9
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay7_profile2_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY7_PROFILE2_INITIATOR_IP_1,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY7_PROFILE2_INITIATOR_IP_2,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY7_PROFILE2_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }

# Bay 7 Profile2 One Connection Tunnel: ENC1 bay 7, BL660c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay7_profile2_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "UserDefined",
                                                    "ipAddress": BAY7_PROFILE2_INITIATOR_IP_1,
                                                    "subnetMask": INITIATOR_SUBNET_MASK,
                                                    "gateway": ""
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "ProfileInitiatorName",
                                                        "initiatorVlanId": "",
                                                        "bootTargetName": BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "chapLevel": None,
                                                        "chapName": "",
                                                        "chapSecret": None,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY7_PROFILE2_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }

# Bay 7 Profile2 One Connection Untagged: ENC1 bay 7, BL660c Gen9
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay7_profile2_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "UserDefined",
                                                      "ipAddress": BAY7_PROFILE2_INITIATOR_IP_1,
                                                      "subnetMask": INITIATOR_SUBNET_MASK,
                                                      "gateway": ""
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
                                                          "bootTargetName": BAY7_PROFILE2_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "chapLevel": None,
                                                          "chapName": "",
                                                          "chapSecret": None,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY7_PROFILE2_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 7 Profile3 Two Connections: ENC1 bay 7, BL660c Gen9
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
bay7_profile3_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                          }},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Mezz 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                          }}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY7_PROFILE3_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                 "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                "volumeAttachments": [{
                                                    "id": 1,
                                                    "isBootVolume": True,
                                                    "lunType": "Auto",
                                                    "storagePaths": [{
                                                        "isEnabled": True,
                                                        "connectionId": 1,
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }, {
                                                        "isEnabled": True,
                                                        "connectionId": 2,
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }],
                                                    "volume": None,
                                                    "volumeUri": "SVOL:" + BAY7_VOLUME_NAME,
                                                }
                                                ]

                                                }}


# Bay 7 Profile3 One Connection Untagged: ENC1 bay 7, BL660c Gen9
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
bay7_profile3_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                  "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                  }},
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY7_PROFILE3_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                         "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                        "volumeAttachments": [{
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lunType": "Auto",
                                                            "storagePaths": [{
                                                                "isEnabled": True,
                                                                "connectionId": 1,
                                                                "targetSelector": "Auto",
                                                                "targets": []
                                                            }],
                                                            "volume": None,
                                                            "volumeUri": "SVOL:" + BAY7_VOLUME_NAME,
                                                        }
                                                        ]

                                                        }}


# Bay 8 Profile1 Two Connections: ENC1 bay 8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay8_profile1_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY8_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY8_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY8_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Bay 8 Profile1 One Connection Tunnel: ENC1 bay 8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay8_profile1_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "DHCP",
                                                    "subnetMask": "",
                                                    "gateway": "",
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "UserDefined",
                                                        "initiatorName": BAY8_PROFILE1_INITIATOR_NAME,
                                                        "initiatorVlanId": "",
                                                        "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "bootTargetName": BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "chapLevel": "Chap",
                                                        "chapName": BAY8_PROFILE1_CHAP_NAME,
                                                        "chapSecret": CHAP_SECRET,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY8_PROFILE1_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }


# Bay 8 Profile1 One Connection Untagged: ENC1 bay 8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay8_profile1_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "UserDefined",
                                                          "initiatorName": BAY8_PROFILE1_INITIATOR_NAME,
                                                          "initiatorVlanId": "",
                                                          "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "bootTargetName": BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "chapLevel": "Chap",
                                                          "chapName": BAY8_PROFILE1_CHAP_NAME,
                                                          "chapSecret": CHAP_SECRET,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY8_PROFILE1_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 8 Profile2 Two Connections: ENC1 bay 8, BL660c Gen8
# User Specified Initiator and Target
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
bay8_profile2_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY8_PROFILE2_INITIATOR_IP_1,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "UserDefined",
                                              "ipAddress": BAY8_PROFILE2_INITIATOR_IP_2,
                                              "subnetMask": INITIATOR_SUBNET_MASK,
                                              "gateway": ""
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "ProfileInitiatorName",
                                                  "initiatorVlanId": "",
                                                  "bootTargetName": BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "chapLevel": None,
                                                  "chapName": "",
                                                  "chapSecret": None,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY8_PROFILE2_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }

# Bay 8 Profile2 One Connection Tunnel: ENC1 bay 8, BL660c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to tunnel network
bay8_profile2_one_connection_tunnel = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                       "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                       "connectionSettings": {
                                           "connections": [
                                               {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                "networkUri": 'ETH:network-tunnel',
                                                "ipv4": {
                                                    "ipAddressSource": "UserDefined",
                                                    "ipAddress": BAY8_PROFILE2_INITIATOR_IP_1,
                                                    "subnetMask": INITIATOR_SUBNET_MASK,
                                                    "gateway": ""
                                                },
                                                   "boot": {
                                                    "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                    "iscsi": {
                                                        "initiatorNameSource": "ProfileInitiatorName",
                                                        "initiatorVlanId": "",
                                                        "bootTargetName": BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                        "bootTargetLun": "0",
                                                        "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                        "firstBootTargetPort": "3260",
                                                        "chapLevel": None,
                                                        "chapName": "",
                                                        "chapSecret": None,
                                                        "mutualChapName": "",
                                                        "mutualChapSecret": None
                                                    }}}
                                           ]
                                       }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                       "iscsiInitiatorName": BAY8_PROFILE2_INITIATOR_NAME,
                                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                       }

# Bay 8 Profile2 One Connection Untagged: ENC1 bay 8, BL660c Gen8
# User Specified Initiator and Target
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on Mezz1:1b to Untagged network
bay8_profile2_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE2_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Mezz 1:1-b", "requestedMbps": "2500",
                                                  "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "UserDefined",
                                                      "ipAddress": BAY8_PROFILE2_INITIATOR_IP_1,
                                                      "subnetMask": INITIATOR_SUBNET_MASK,
                                                      "gateway": ""
                                                  },
                                                     "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                      "iscsi": {
                                                          "initiatorNameSource": "ProfileInitiatorName",
                                                          "initiatorVlanId": "",
                                                          "bootTargetName": BAY8_PROFILE2_BOOT_TARGET_NAME,
                                                          "bootTargetLun": "0",
                                                          "firstBootTargetIp": USER_SPECIFIED_BOOT_TARGET_IP,
                                                          "firstBootTargetPort": "3260",
                                                          "chapLevel": None,
                                                          "chapName": "",
                                                          "chapSecret": None,
                                                          "mutualChapName": "",
                                                          "mutualChapSecret": None
                                                      }}}
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY8_PROFILE2_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                         }

# Bay 8 Profile3 Two Connections: ENC1 bay 8, BL660c Gen8
# DHCP Initiator
# Managed Volume
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to untagged network
bay8_profile3_two_connections = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                          "boot": {
                                              "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                          }},
                                         {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "subnetMask": "",
                                              "gateway": "",
                                          },
                                             "boot": {
                                              "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
                                          }}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY8_PROFILE3_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                 "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                "volumeAttachments": [{
                                                    "id": 1,
                                                    "isBootVolume": True,
                                                    "lunType": "Auto",
                                                    "storagePaths": [{
                                                        "isEnabled": True,
                                                        "connectionId": 1,
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }, {
                                                        "isEnabled": True,
                                                        "connectionId": 2,
                                                        "targetSelector": "Auto",
                                                        "targets": []
                                                    }],
                                                    "volume": None,
                                                    "volumeUri": "SVOL:" + BAY8_VOLUME_NAME,
                                                }
                                                ]

                                                }}


# Bay 8 Profile3 One Connection Untagged: ENC1 bay 8, BL660c Gen8
# DHCP Initiator
# Managed volume
# Connection initiator name uses user defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexibleLOM1:1b to Untagged network
bay8_profile3_one_connection_untagged = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY8, 'enclosureUri': 'ENC:' + ENC1,
                                         "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                         "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE3_NAME, "description": "", "affinity": "Bay",
                                         "connectionSettings": {
                                             "connections": [
                                                 {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                  "ipv4": {
                                                      "ipAddressSource": "DHCP",
                                                      "subnetMask": "",
                                                      "gateway": "",
                                                  },
                                                  "boot": {
                                                      "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                                                  }},
                                             ]
                                         }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                                         "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                         "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                         "iscsiInitiatorName": BAY8_PROFILE3_INITIATOR_NAME,
                                         "localStorage": {"sasLogicalJBODs": [], "controllers": []},
                                         "sanStorage": {'manageSanStorage': True, "hostOSType": "RHE Linux (5.x, 6.x)",
                                                        "volumeAttachments": [{
                                                            "id": 1,
                                                            "isBootVolume": True,
                                                            "lunType": "Auto",
                                                            "storagePaths": [
                                                                {
                                                                    "isEnabled": True,
                                                                    "connectionId": 1,
                                                                    "targetSelector": "Auto",
                                                                    "targets": []
                                                                }
                                                            ],
                                                            "volume": None,
                                                            "volumeUri": "SVOL:" + BAY8_VOLUME_NAME,
                                                        }
                                                        ]

                                                        }}


# Negative Profiles


# DHCP with IP address
negative_sp_dhcp_with_ip = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                            "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                            "macType": "Physical", "wwnType": "Physical", "name": "DHCP with IP", "description": "", "affinity": "Bay",
                            "connectionSettings": {
                                "connections": [
                                    {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                     "networkUri": 'ETH:network-tunnel',
                                     "ipv4": {
                                         "ipAddressSource": "DHCP",
                                         "ipAddress": BAY7_PROFILE2_INITIATOR_IP_1,
                                         "subnetMask": "",
                                         "gateway": "",
                                     },
                                        "boot": {
                                         "priority": "Primary", "bootVolumeSource": "UserDefined",
                                         "iscsi": {
                                             "initiatorNameSource": "UserDefined",
                                             "initiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                             "initiatorVlanId": "",
                                             "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                             "firstBootTargetPort": "3260",
                                             "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                             "bootTargetLun": "0",
                                             "chapLevel": "Chap",
                                             "chapName": BAY7_PROFILE1_CHAP_NAME,
                                             "chapSecret": CHAP_SECRET,
                                             "mutualChapName": "",
                                             "mutualChapSecret": None
                                         }}}
                                ]
                            }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                            "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                            "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                            "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                            "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                            }


# DHCP with Subnetmask
negative_sp_dhcp_with_subnetmask = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                    "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                    "macType": "Physical", "wwnType": "Physical", "name": "DHCP with Subnetmask", "description": "", "affinity": "Bay",
                                    "connectionSettings": {
                                        "connections": [
                                            {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                             "networkUri": 'ETH:network-tunnel',
                                             "ipv4": {
                                                 "ipAddressSource": "DHCP",
                                                 "ipAddress": "",
                                                 "subnetMask": INITIATOR_SUBNET_MASK,
                                                 "gateway": "",
                                             },
                                                "boot": {
                                                 "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                 "iscsi": {
                                                     "initiatorNameSource": "UserDefined",
                                                     "initiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                                     "initiatorVlanId": "",
                                                     "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                     "firstBootTargetPort": "3260",
                                                     "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                     "bootTargetLun": "0",
                                                     "chapLevel": "Chap",
                                                     "chapName": BAY7_PROFILE1_CHAP_NAME,
                                                     "chapSecret": CHAP_SECRET,
                                                     "mutualChapName": "",
                                                     "mutualChapSecret": None
                                                 }}}
                                        ]
                                    }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                    "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                    "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                    "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                    "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                    }

# DHCP with Gateway
negative_sp_dhcp_with_gateway = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                                 "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                 "macType": "Physical", "wwnType": "Physical", "name": "DHCP with Gateway", "description": "", "affinity": "Bay",
                                 "connectionSettings": {
                                     "connections": [
                                         {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                                          "networkUri": 'ETH:network-tunnel',
                                          "ipv4": {
                                              "ipAddressSource": "DHCP",
                                              "ipAddress": "",
                                              "subnetMask": "",
                                              "gateway": INITIATOR_GATEWAY,
                                          },
                                             "boot": {
                                              "priority": "Primary", "bootVolumeSource": "UserDefined",
                                              "iscsi": {
                                                  "initiatorNameSource": "UserDefined",
                                                  "initiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                                  "initiatorVlanId": "",
                                                  "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                  "firstBootTargetPort": "3260",
                                                  "bootTargetName": BAY7_PROFILE1_BOOT_TARGET_NAME,
                                                  "bootTargetLun": "0",
                                                  "chapLevel": "Chap",
                                                  "chapName": BAY7_PROFILE1_CHAP_NAME,
                                                  "chapSecret": CHAP_SECRET,
                                                  "mutualChapName": "",
                                                  "mutualChapSecret": None
                                              }}}
                                     ]
                                 }, "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                                 "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                 "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                 "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                                 "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                 }


# Move Test
# Bay 8 Profile1 Two Connections: ENC1 bay 8, BL660c Gen8
# DHCP Initiator
# Connection initiator name uses profile defined
# Profile initiator name is user defined
# Primary iSCSI boot connection on FlexLOM1:1b to untagged network and secondary on FlexLom1:2b to tunnel network
move_bay8_profile1_two_connections_to_bay2 = {"type": "ServerProfileV9", "serverHardwareUri": 'SH:' + ENC1SHBAY2, 'enclosureUri': 'ENC:' + ENC1,
                                              "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                                              "macType": "Physical", "wwnType": "Physical", "name": BAY8_PROFILE1_NAME, "description": "", "affinity": "Bay",
                                              "connectionSettings": {
                                                  "connections": [
                                                      {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500", "networkUri": 'ETH:network-untagged',
                                                       "ipv4": {
                                                           "ipAddressSource": "DHCP",
                                                           "subnetMask": "",
                                                           "gateway": "",
                                                       },
                                                       "boot": {
                                                           "priority": "Primary", "bootVolumeSource": "UserDefined",
                                                           "iscsi": {
                                                               "initiatorNameSource": "ProfileInitiatorName",
                                                               "initiatorVlanId": "",
                                                               "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                               "firstBootTargetPort": "3260",
                                                               "bootTargetName": BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                               "bootTargetLun": "0",
                                                               "chapLevel": "Chap",
                                                               "chapName": BAY8_PROFILE1_CHAP_NAME,
                                                               "chapSecret": CHAP_SECRET,
                                                               "mutualChapName": "",
                                                               "mutualChapSecret": None
                                                           }}},
                                                      {"id": 2, "name": "iSCSI-boot-secondary", "functionType": "iSCSI", "portId": "Flb 1:2-b", "requestedMbps": "2500", "networkUri": 'ETH:network-tunnel',
                                                       "ipv4": {
                                                           "ipAddressSource": "DHCP",
                                                           "subnetMask": "",
                                                           "gateway": "",
                                                       },
                                                          "boot": {
                                                           "priority": "Secondary", "bootVolumeSource": "UserDefined",
                                                           "iscsi": {
                                                               "initiatorNameSource": "ProfileInitiatorName",
                                                               "initiatorVlanId": "",
                                                               "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                                               "firstBootTargetPort": "3260",
                                                               "bootTargetName": BAY8_PROFILE1_BOOT_TARGET_NAME,
                                                               "bootTargetLun": "0",
                                                               "chapLevel": "Chap",
                                                               "chapName": BAY8_PROFILE1_CHAP_NAME,
                                                               "chapSecret": CHAP_SECRET,
                                                               "mutualChapName": "",
                                                               "mutualChapSecret": None
                                                           }}}
                                                  ]
                                              }, "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]}, "bootMode": {"manageMode": True, "mode": "BIOS"},
                                              "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                                              "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                                              "iscsiInitiatorName": BAY8_PROFILE1_INITIATOR_NAME,
                                              "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                                              }


# Create with API v300
create_v300_profile = {"type": "ServerProfileV6", "serverHardwareUri": 'SH:' + ENC1SHBAY1, 'enclosureUri': 'ENC:' + ENC1,
                       "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                       "macType": "Physical", "wwnType": "Physical", "name": "API v300 Profile", "description": "", "affinity": "Bay",
                       "connections": [
                           {"id": 1, "name": "iSCSI-boot-primary", "functionType": "iSCSI", "portId": "Flb 1:1-b", "requestedMbps": "2500",
                            "networkUri": 'ETH:network-untagged',
                            "ipv4": {
                                "ipAddressSource": "DHCP",
                                "subnetMask": "",
                                "gateway": "",
                            },
                               "boot": {
                                "priority": "Primary", "bootVolumeSource": "UserDefined",
                                "iscsi": {
                                    "initiatorNameSource": "UserDefined",
                                    "initiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                                    "initiatorVlanId": "",
                                    "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                                    "firstBootTargetPort": "3260",
                                    "bootTargetName": BAY3_PROFILE1_BOOT_TARGET_NAME,
                                    "bootTargetLun": "0",
                                    "chapLevel": "Chap",
                                    "chapName": BAY3_PROFILE1_CHAP_NAME,
                                    "chapSecret": CHAP_SECRET,
                                    "mutualChapName": "",
                                    "mutualChapSecret": None
                                }}}
                       ],
                       "boot": {"manageBoot": True, "order": ["HardDisk", "CD", "USB", "PXE"]},
                       "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                       "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                       "iscsiInitiatorName": BAY3_PROFILE1_INITIATOR_NAME,
                       "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                       }

# API v300 GET
get_300_profile = {"type": "ServerProfileV6", "serverHardwareUri": 'SH:' + ENC1SHBAY7, 'enclosureUri': 'ENC:' + ENC1,
                   "enclosureGroupUri": "EG:" + EG_NAME, "serialNumberType": "Physical", "iscsiInitiatorNameType": "UserDefined",
                   "macType": "Physical", "wwnType": "Physical", "name": BAY7_PROFILE1_NAME, "description": "", "affinity": "Bay",
                   "connections": [],
                   "boot": {"manageBoot": True, "order": ["HardDisk"]}, "bootMode": {"manageMode": True, "mode": "UEFI", "pxeBootPolicy": "Auto"},
                   "firmware": {"manageFirmware": False, "firmwareBaselineUri": None, "forceInstallFirmware": False, "firmwareInstallType": None},
                   "bios": {"manageBios": False, "overriddenSettings": []}, "hideUnusedFlexNics": True,
                   "iscsiInitiatorName": BAY7_PROFILE1_INITIATOR_NAME,
                   "localStorage": {"sasLogicalJBODs": [], "controllers": []}, "sanStorage": {'manageSanStorage': False, 'volumeAttachments': []}
                   }


# Blade CLPs

# Bay 1 no profile
clp_bay1_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "1",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Bay 2 no profile
clp_bay2_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "2",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 3 no profile
clp_bay3_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}


# Bay 4 no profile
clp_bay4_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "4",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1414"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}

# Bay 7 no profile
clp_bay7_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 no profile
clp_bay8_no_profile = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 2 profile 1 two connections
clp_bay2_profile1_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "2",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;AC162DAB6148;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;AC162DAB6149;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;AC162DAB614C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;AC162DAB614D;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport2 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport2 OEMHP_targetPort=3260"

     PID42: "set netport2 OEMHP_LUN=0"

     PID43: "set netport2 OEMHP_authenticationMethod=None"

     PID44: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Bay 3 profile 1 two connections
clp_bay3_profile1_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;10604B010400;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;10604B010401;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay3""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;10604B010404;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;10604B010405;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"

     PID39: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp"

     PID40: "set netport2 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport2 OEMHP_targetPort=3260"

     PID42: "set netport2 OEMHP_LUN=0"

     PID43: "set netport2 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport2 OEMHP_username="wpst10-bay3""

     PID45: "set netport2 OEMHP_secret=777073746870767365313233"

     PID46: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Bay 7 profile 1 two connections
clp_bay7_profile1_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 1 two connections
clp_bay8_profile1_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB416698;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB416699;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB41669C;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB41669D;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 2 profile 1 one connection untagged
clp_bay2_profile1_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "2",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;A0B3CC1C80C8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;A0B3CC1C80C9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;A0B3CC1C80CC;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;A0B3CC1C80CD;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Bay 3 profile 1 one connection untagged
clp_bay3_profile1_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;C4346BC8E468;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;C4346BC8E469;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay3""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;C4346BC8E46C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;C4346BC8E46D;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Bay 7 profile 1 one connection untagged
clp_bay7_profile1_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B70;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B71;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B78;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B79;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 1 one connection untagged
clp_bay8_profile1_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 2 profile 1 one connection tunnel
clp_bay2_profile1_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "2",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;A0B3CC1C80C8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;A0B3CC1C80C9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay2-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:158:wpst10-bay2-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=None"

     PID44: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID45: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=060Fh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;A0B3CC1C80CC;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;A0B3CC1C80CD;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Bay 3 profile 1 one connection tunnel
clp_bay3_profile1_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;10604B010400;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;10604B010401;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:150:wpst10-bay3-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay3""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;10604B010404;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;10604B010405;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"
"""
}

# Bay 7 profile 1 one connection tunnel
clp_bay7_profile1_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B70;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B71;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:161:wpst10-bay7-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay7""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_MutualUsername="wpst10-bay7""

     PID47: "set netport1 OEMHP_mutualSecret=687076736531323377707374"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=06E3h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B78;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B79;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 1 one connection tunnel
clp_bay8_profile1_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

"""
}


# Bay 3 profile 2 two connections
clp_bay3_profile2_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;10604B010400;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;10604B010401;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.128"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:829:wpst10-bay3-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;10604B010404;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;10604B010405;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;C4346BC8E468;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;C4346BC8E469;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=046Bh)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;C4346BC8E46C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;C4346BC8E46D;1001;2500;10000;enabled;enabled""

     PID36: "set netport2 OEMHP_IPVersion=IPv4"

     PID37: "set netport2 OEMHP_InitiatorIP=192.168.22.129"

     PID38: "set netport2 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport2 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3"

     PID40: "set netport2 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:829:wpst10-bay3-bootvol"

     PID41: "set netport2 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport2 OEMHP_targetPort=3260"

     PID43: "set netport2 OEMHP_LUN=0"

     PID44: "set netport2 OEMHP_authenticationMethod=None"

     PID45: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Bay 7 profile 2 two connections
clp_bay7_profile2_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.126"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.127"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 2 two connections
clp_bay8_profile2_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176F8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176F9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.130"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176FC;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176FD;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.131"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 7 profile 2 one connection tunnel
clp_bay7_profile2_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B70;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B71;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.126"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B78;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B79;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 2 one connection tunnel
clp_bay8_profile2_one_connection_tunnel = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.130"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 3 profile 2 one connection untagged
clp_bay3_profile2_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "3",
    "validate":
    """
Blade 3 mezz F: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

--------------------------------------

HP LPe1205A 8Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1411"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 554FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;C4346BC8E468;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;C4346BC8E469;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.128"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay3"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:829:wpst10-bay3-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;C4346BC8E46C;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;C4346BC8E46D;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}

# Bay 7 profile 2 one connection untagged
clp_bay7_profile2_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B70;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B71;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.126"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:821:wpst10-bay7-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;ECB1D7A95B78;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;ECB1D7A95B79;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 2 one connection untagged
clp_bay8_profile2_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3CA82AFEFF40;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3CA82AFEFF41;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_InitiatorIP=192.168.22.130"

     PID38: "set netport1 OEMHP_InitiatorNetmask=255.255.192.0"

     PID39: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8"

     PID40: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-173-2:879:wpst10-bay8-bootvol"

     PID41: "set netport1 OEMHP_targetIP=192.168.21.71"

     PID42: "set netport1 OEMHP_targetPort=3260"

     PID43: "set netport1 OEMHP_LUN=0"

     PID44: "set netport1 OEMHP_authenticationMethod=None"

     PID45: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID46: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0644h)

     PID01: "set netport2 default"

     PID32: "set netport2 OEMHP_CVNI=2001"

     PID33: "set netport2 OEMHP_FlowControl=function"

     PID34: "set netport2 OEMHP_LF0="E;1;3CA82AFEFF44;1000;0;0;disabled;disabled""

     PID35: "set netport2 OEMHP_LF1="I;1;3CA82AFEFF45;1001;0;0;disabled;disabled""

     PID36: "set netport2 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport2 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 4 profile 3 two connections
clp_bay4_profile3_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "4",
    "validate":
    """
Blade 4 mezz F: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

        --> status: 00000500h

     PID02: "exit"

        --> status: 00000500h

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1414"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

        --> status: 00000500h

     PID32: "set netport1 OEMHP_CVNI=2001"

        --> status: 00000500h

     PID33: "set netport1 OEMHP_FlowControl=function"

        --> status: 00000500h

     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173C0080;1000;0;0;disabled;disabled""

        --> status: 00000500h

     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173C0081;1001;2500;10000;enabled;enabled""

        --> status: 00000500h

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

        --> status: 00000500h

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

        --> status: 00000500h

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:539:wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

        --> status: 00000500h

     PID41: "set netport1 OEMHP_targetPort=3260"

1475707274:Wed Oct  5 22:41:14 2016:1245:nettray.c:2766:GetIOIPv6Info::SWM5: Read 1 addr from SWM IPV6_INFO
        --> status: 00000500h

     PID42: "set netport1 OEMHP_LUN=0"

        --> status: 00000500h

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

        --> status: 00000500h

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID45: "set netport1 OEMHP_secret=304f55724c61736b744f725724734a71"

        --> status: 00000500h

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID47: "set netport1 OEMHP_mutualSecret=725444644e3173763074646d496c6661"

1475707275:Wed Oct  5 22:41:15 2016:1245:nettray.c:2980:GetIOIPv6ProtoData::SWM5 doesn't form URL for the IPv6 address [1 of 1].
        --> status: 0000FF02h

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

        --> status: 00000500h

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

        --> status: 00000500h

     PID02: "exit"

        --> status: 00000500h

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

        --> status: 00000500h

     PID32: "set netport1 OEMHP_CVNI=2001"

        --> status: 00000500h

     PID33: "set netport1 OEMHP_FlowControl=function"

        --> status: 00000500h

     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173C0088;1000;0;0;disabled;disabled""

        --> status: 00000500h

     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173C0089;1001;2500;10000;enabled;enabled""

        --> status: 00000500h

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

        --> status: 00000500h

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

        --> status: 00000500h

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:539:wpst10-bay4-dhcp-managed-volume"

        --> status: 00000500h

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

        --> status: 00000500h

     PID41: "set netport1 OEMHP_targetPort=3260"

        --> status: 00000500h

     PID42: "set netport1 OEMHP_LUN=0"

        --> status: 00000500h

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

        --> status: 00000500h

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID45: "set netport1 OEMHP_secret=304f55724c61736b744f725724734a71"

        --> status: 00000500h

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay4-dhcp-managed-volume""

        --> status: 00000500h

     PID47: "set netport1 OEMHP_mutualSecret=725444644e3173763074646d496c6661"

        --> status: 0000FF02h

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

        --> status: 00000500h

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

        --> status: 00000500h

     PID02: "exit"

        --> status: 00000500h
"""
}

# Bay 7 profile 3 two connections
clp_bay7_profile3_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:334:wpst10-bay7-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=4d5839717546584a6143394e21476b38"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=77364f48592d5a292321674145434274"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:334:wpst10-bay7-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=4d5839717546584a6143394e21476b38"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=77364f48592d5a292321674145434274"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 3 two connections
clp_bay8_profile3_two_connections = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176F8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176F9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:337:wpst10-bay8-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=765e5276494278585462797736595a79"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=566e384941335733275f386b5e415072"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176FC;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176FD;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:337:wpst10-bay8-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=765e5276494278585462797736595a79"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=566e384941335733275f386b5e415072"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}


# Bay 7 profile 3 one connection untagged
clp_bay7_profile3_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "7",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71160;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71161;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:334:wpst10-bay7-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=55594e4f67402b3348384d614e54454c"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay7-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=496326306575616a4b62476e64555666"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;5CB901D71164;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;5CB901D71165;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1412"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1415"

     PID05: "exit"

Blade 7 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

Blade 7 mezz A: NOT FOUND
"""
}

# Bay 8 profile 3 one connection untagged
clp_bay8_profile3_one_connection_untagged = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "8",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 554M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport2 default"

     PID02: "exit"

Blade 8 mezz 2: NOT FOUND

Blade 8 mezz 3: NOT FOUND

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176F8;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176F9;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:337:wpst10-bay8-dhcp-managed-volume"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=MutualCHAP"

     PID44: "set netport1 OEMHP_username="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID45: "set netport1 OEMHP_secret=337172285f79742425314b2669257021"

     PID46: "set netport1 OEMHP_MutualUsername="iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp-managed-volume""

     PID47: "set netport1 OEMHP_mutualSecret=676d47726d274b6431246a6c21502379"

     PID48: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID49: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0771h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;3863BB4176FC;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;3863BB4176FD;1001;0;0;disabled;disabled""

     PID36: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID37: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-Port 534FLB Adapter

Mezz=A (FLB=2) DevID=41h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"
"""
}

# Bay 2 no profile
clp_bay2_move = {
    "oa": ENC1_OA1,
    "username": oa_credentials['username'],
    "password": oa_credentials['password'],
    "bay": "2",
    "validate":
    """
--------------------------------------

HP FlexFabric 10Gb 2-port 534M Adapter

Mezz=1 DevID=4Eh (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID02: "exit"

  FIP: 1 (off=033Ch)

     PID01: "set netport1 default"

     PID02: "exit"

--------------------------------------

HP LPe1605 16Gb FC HBA for BladeSystem c-Class

Mezz=2 DevID=4Ch (off=0200h)

--------------------------------------

  FIP: 0 (off=021Ch)

     PID01: "set netport0 default"

     PID02: "set netport0 OEMHP_hss=1416"

     PID03: "set netport1 default"

     PID04: "set netport1 OEMHP_hss=1412"

     PID05: "exit"

--------------------------------------

HP FlexFabric 10Gb 2-port 536FLB Adapter

Mezz=9 (FLB=1) DevID=40h (off=0300h)

--------------------------------------

  FIP: 0 (off=031Ch)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173C0080;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173C0081;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"

  FIP: 1 (off=0670h)

     PID01: "set netport1 default"

     PID32: "set netport1 OEMHP_CVNI=2001"

     PID33: "set netport1 OEMHP_FlowControl=function"

     PID34: "set netport1 OEMHP_LF0="E;1;6CC2173C0088;1000;0;0;disabled;disabled""

     PID35: "set netport1 OEMHP_LF1="I;1;6CC2173C0089;1001;2500;10000;enabled;enabled""

     PID36: "set netport1 OEMHP_IPVersion=IPv4"

     PID37: "set netport1 OEMHP_NetworkParamsDHCP=enabled"

     PID38: "set netport1 OEMHP_initiatorName=iqn.2015-02.com.hpe:oneview-wpst10-bay8-dhcp"

     PID39: "set netport1 OEMHP_targetName=iqn.2003-10.com.lefthandnetworks:vsa-mg-116:164:wpst10-bay8-dhcp"

     PID40: "set netport1 OEMHP_targetIP=192.168.21.59"

     PID41: "set netport1 OEMHP_targetPort=3260"

     PID42: "set netport1 OEMHP_LUN=0"

     PID43: "set netport1 OEMHP_authenticationMethod=CHAP"

     PID44: "set netport1 OEMHP_username="wpst10-bay8""

     PID45: "set netport1 OEMHP_secret=777073746870767365313233"

     PID46: "set netport1 OEMHP_LF2="D;;;;;;;disabled""

     PID47: "set netport1 OEMHP_LF3="D;;;;;;;disabled""

     PID02: "exit"
"""
}


# Server Profile Templates

# DHCP iSCSI primary only, Legacy Bios, untagged network
dhcp_primary_only_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# edit from DHCP to User Specified iSCSI primary only, Legacy Bios, untagged network
edit_dhcp_primary_only_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# DHCP iSCSI primary only, Legacy Bios, untagged network
dhcp_managed_volume_primary_only_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "template_dhcp_primary_only_legacy_bios",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# edit DHCP to User Specified iSCSI primary only, Legacy Bios, untagged network
edit_dhcp_managed_volume_primary_only_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "edit_template_dhcp_primary_only_legacy_bios",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# DHCP iSCSI primary only, Legacy Bios, tunnel network
dhcp_primary_only_legacy_bios_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# edit DHCP to User Specified iSCSI primary only, Legacy Bios, tunnel network
edit_dhcp_primary_only_legacy_bios_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# DHCP iSCSI primary & secondary, Legacy Bios, untagged network
dhcp_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# edit DHCP to User Specified iSCSI primary & secondary, Legacy Bios, untagged network
edit_dhcp_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# DHCP iSCSI with managed volume primary & secondary, Legacy Bios, untagged network
dhcp_managed_volume_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "connectionId": 2,
                    "isEnabled": True,
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "template_dhcp_legacy_bios",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# edit DHCP to User Specified iSCSI with managed volume primary & secondary, Legacy Bios, untagged network
edit_dhcp_managed_volume_legacy_bios_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_legacy_bios_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
    },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "connectionId": 2,
                    "isEnabled": True,
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "edit_template_dhcp_legacy_bios",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# DHCP iSCSI primary & secondary, Legacy BIOs, tunnel network
dhcp_legacy_bios_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# edit DHCP to User Specified iSCSI primary & secondary, Legacy BIOs, tunnel network
edit_dhcp_legacy_bios_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_legacy_bios_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# DHCP iSCSI primary only, UEFI, untagged network
dhcp_primary_only_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary only, UEFI, untagged network
edit_dhcp_primary_only_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI primary only, UEFI, untagged network
dhcp_managed_volume_primary_only_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "template_dhcp_primary_only_uefi",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI, untagged network
edit_dhcp_managed_volume_primary_only_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_primary_only_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "edit_template_dhcp_primary_only_uefi",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# DHCP iSCSI primary only, UEFI, tunnel network
dhcp_primary_only_UEFI_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary only, UEFI, tunnel network
edit_dhcp_primary_only_UEFI_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI primary & secondary, UEFI, untagged network
dhcp_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary & secondary, UEFI, untagged network
edit_dhcp_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI with managed volume primary & secondary, UEFI, untagged network
dhcp_managed_volume_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "connectionId": 2,
                    "isEnabled": True,
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "template_dhcp_uefi",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# edit DHCP to User Specified iSCSI with managed volume primary & secondary, UEFI, untagged network
edit_dhcp_managed_volume_UEFI_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_UEFI_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "connectionId": 2,
                    "isEnabled": True,
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "edit_template_dhcp_uefi",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# DHCP iSCSI primary & secondary, UEFI, tunnel network
dhcp_UEFI_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary & secondary, UEFI, tunnel network
edit_dhcp_UEFI_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFI",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI primary only, UEFI Optimized, untagged network
dhcp_primary_only_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary only, UEFI Optimized, untagged network
edit_dhcp_primary_only_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI primary only, UEFI Optimized, untagged network
dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "template_dhcp_primary_only_uefi_optimized",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# edit DHCP to User Specified iSCSI primary only, UEFI Optimized, untagged network
edit_dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "edit_template_dhcp_primary_only_uefi_optimized",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# DHCP iSCSI primary only, UEFI optimized, tunnel network
dhcp_primary_only_UEFI_optimized_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary only, UEFI optimized, tunnel network
edit_dhcp_primary_only_UEFI_optimized_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_primary_only_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI primary & secondary, UEFI optimized, untagged network
dhcp_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary & secondary, UEFI optimized, untagged network
edit_dhcp_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# DHCP iSCSI with managed volume primary & secondary, UEFI Optimized, untagged network
dhcp_managed_volume_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "connectionId": 2,
                    "isEnabled": True,
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "template_dhcp_uefi_optimized",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# edit DHCP to User Specified iSCSI with managed volume primary & secondary, UEFI Optimized, untagged network
edit_dhcp_managed_volume_UEFI_optimized_untagged_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_managed_volume_UEFI_optimized_untagged_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "ManagedVolume",
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "ManagedVolume",
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
                 },
    'bios': {
        'manageBios': False,
        'overriddenSettings': []
    },
    'localStorage': {
        'sasLogicalJBODs': [],
        'controllers': []
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
                    "targetSelector": "Auto",
                    "targets": []
                },
                {
                    "connectionId": 2,
                    "isEnabled": True,
                    "targetSelector": "Auto",
                    "targets": []
                }
            ],
            "volume": {
                "isPermanent": False,
                "properties": {
                    "name": "edit_template_dhcp_uefi_optimized",
                    "storagePool": "SPOOL:VSA_Cluster_116",
                    "size": 2147483648,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:VSA_Cluster_116",
            },
            "volumeStorageSystemUri": "SSYS:VSA_Cluster_116",
        }
        ]
    }
}

# DHCP iSCSI primary & secondary, UEFI optimized, tunnel network
dhcp_UEFI_optimized_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# edit DHCP to User Specified iSCSI primary & secondary, UEFI optimized, tunnel network
edit_dhcp_UEFI_optimized_tunnel_template = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_UEFI_optimized_tunnel_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }}},
            {
            'id': 2,
            'name': "iSCSI-secondary",
            'functionType': 'iSCSI',
            'portId': 'Flb 1:1-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-tunnel',
            "ipv4": {
                "ipAddressSource": "UserDefined",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Secondary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["HardDisk"]
    },
    "bootMode": {"manageMode": True,
                 "mode": "UEFIOptimized",
                 "pxeBootPolicy": "Auto"
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

# Negative Server Profile Templates

# DHCP with IP address
negative_spt_dhcp_with_ip = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_with_ip_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "ipAddress": BAY4_PROFILE2_INITIATOR_IP_1,
                "subnetMask": "",
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# DHCP with Subnetmask
negative_spt_dhcp_with_subnetmask = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_with_subnetmask_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "ipAddress": "",
                "subnetMask": INITIATOR_SUBNET_MASK,
                "gateway": ""
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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

# DHCP with gateway
negative_spt_dhcp_with_gateway = {
    'type': 'ServerProfileTemplateV5',
    'name': 'dhcp_with_gateway_template',
    'serverHardwareTypeUri': 'SHT:BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class',
    'enclosureGroupUri': 'EG:%s' % EG_NAME,
    "connectionSettings": {
        "manageConnections": True,
        'connections': [{
            'id': 1,
            'name': "iSCSI-primary",
            'functionType': 'iSCSI',
            'portId': 'Mezz 1:2-b',
            'requestedMbps': 2500,
            'networkUri': 'ETH:network-untagged',
            "ipv4": {
                "ipAddressSource": "DHCP",
                "ipAddress": "",
                "subnetMask": "",
                "gateway": INITIATOR_GATEWAY
            },
            "boot": {
                "priority": "Primary", "bootVolumeSource": "UserDefined",
                "iscsi": {
                    'initiatorNameSource': 'UserDefined',
                    'firstBootTargetIp': DHCP_BOOT_TARGET_IP,
                    'firstBootTargetPort': '3260',
                    'chapLevel': 'Chap'
                }
            }}
        ],
    },
    "boot": {
        "manageBoot": True,
        "order": ["CD", "USB", "PXE", "HardDisk"]
    },
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS"
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


all_profiles = [move_bay8_profile1_two_connections_to_bay2.copy(),
                bay7_profile2_one_connection_untagged.copy(),
                bay8_profile2_one_connection_untagged.copy(),
                ]

create_profiles = [bay8_profile3_two_connections.copy(),
                   bay7_profile1_one_connection_tunnel.copy(),
                   ]

edit_profiles = [bay8_profile2_one_connection_tunnel.copy(),
                 bay7_profile2_one_connection_untagged.copy(),
                 ]

edit_profiles2 = [bay8_profile1_two_connections.copy(),
                  bay7_profile3_one_connection_untagged.copy(),
                  ]

move_profiles = [move_bay8_profile1_two_connections_to_bay2.copy(),
                 ]

delete_profiles = [bay7_profile3_one_connection_untagged.copy(),
                   move_bay8_profile1_two_connections_to_bay2.copy(),
                   ]

clp_after_create = [clp_bay7_profile1_one_connection_tunnel.copy(),
                    ]

clp_after_edit = [clp_bay8_profile2_one_connection_tunnel.copy(),
                  clp_bay7_profile2_one_connection_untagged.copy(),
                  ]

clp_after_edit2 = [clp_bay8_profile1_two_connections.copy(),
                   ]

clp_after_move = [clp_bay2_move.copy(),
                  clp_bay8_no_profile.copy(),
                  ]

clp_after_delete = [clp_bay7_no_profile.copy(),
                    clp_bay8_no_profile.copy(),
                    clp_bay2_no_profile.copy(),
                    ]

negative_profile_tasks = [
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_dhcp_with_ip.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_with_ip_address'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_dhcp_with_subnetmask.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_with_ip_address'},
    {
        'keyword': 'Add Server Profile',
        'argument': negative_sp_dhcp_with_gateway.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_with_ip_address'},
]

create_profile_templates = [dhcp_primary_only_legacy_bios_untagged_template.copy(),
                            dhcp_primary_only_legacy_bios_tunnel_template.copy(),
                            dhcp_legacy_bios_untagged_template.copy(),
                            dhcp_legacy_bios_tunnel_template.copy(),
                            dhcp_primary_only_UEFI_untagged_template.copy(),
                            dhcp_primary_only_UEFI_tunnel_template.copy(),
                            dhcp_UEFI_untagged_template.copy(),
                            dhcp_UEFI_tunnel_template.copy(),
                            dhcp_primary_only_UEFI_optimized_untagged_template.copy(),
                            dhcp_primary_only_UEFI_optimized_tunnel_template.copy(),
                            dhcp_UEFI_optimized_untagged_template.copy(),
                            dhcp_UEFI_optimized_tunnel_template.copy(),
                            dhcp_managed_volume_primary_only_legacy_bios_untagged_template.copy(),
                            dhcp_managed_volume_legacy_bios_untagged_template.copy(),
                            dhcp_managed_volume_primary_only_UEFI_untagged_template.copy(),
                            dhcp_managed_volume_UEFI_untagged_template.copy(),
                            dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template.copy(),
                            dhcp_managed_volume_UEFI_optimized_untagged_template.copy(),
                            ]

edit_profile_templates = [edit_dhcp_primary_only_legacy_bios_untagged_template.copy(),
                          edit_dhcp_primary_only_legacy_bios_tunnel_template.copy(),
                          edit_dhcp_legacy_bios_untagged_template.copy(),
                          edit_dhcp_legacy_bios_tunnel_template.copy(),
                          edit_dhcp_primary_only_UEFI_untagged_template.copy(),
                          edit_dhcp_primary_only_UEFI_tunnel_template.copy(),
                          edit_dhcp_UEFI_untagged_template.copy(),
                          edit_dhcp_UEFI_tunnel_template.copy(),
                          edit_dhcp_primary_only_UEFI_optimized_untagged_template.copy(),
                          edit_dhcp_primary_only_UEFI_optimized_tunnel_template.copy(),
                          edit_dhcp_UEFI_optimized_untagged_template.copy(),
                          edit_dhcp_UEFI_optimized_tunnel_template.copy(),
                          # edit_dhcp_managed_volume_primary_only_legacy_bios_untagged_template.copy(),
                          # edit_dhcp_managed_volume_legacy_bios_untagged_template.copy(),
                          # edit_dhcp_managed_volume_primary_only_UEFI_untagged_template.copy(),
                          # edit_dhcp_managed_volume_UEFI_untagged_template.copy(),
                          # edit_dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template.copy(),
                          # edit_dhcp_managed_volume_UEFI_optimized_untagged_template.copy(),
                          ]

edit_profile_templates2 = [dhcp_primary_only_legacy_bios_untagged_template.copy(),
                           dhcp_primary_only_legacy_bios_tunnel_template.copy(),
                           dhcp_legacy_bios_untagged_template.copy(),
                           dhcp_legacy_bios_tunnel_template.copy(),
                           dhcp_primary_only_UEFI_untagged_template.copy(),
                           dhcp_primary_only_UEFI_tunnel_template.copy(),
                           dhcp_UEFI_untagged_template.copy(),
                           dhcp_UEFI_tunnel_template.copy(),
                           dhcp_primary_only_UEFI_optimized_untagged_template.copy(),
                           dhcp_primary_only_UEFI_optimized_tunnel_template.copy(),
                           dhcp_UEFI_optimized_untagged_template.copy(),
                           dhcp_UEFI_optimized_tunnel_template.copy(),
                           # dhcp_managed_volume_primary_only_legacy_bios_untagged_template.copy(),
                           # dhcp_managed_volume_legacy_bios_untagged_template.copy(),
                           # dhcp_managed_volume_primary_only_UEFI_untagged_template.copy(),
                           # dhcp_managed_volume_UEFI_untagged_template.copy(),
                           # dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template.copy(),
                           # dhcp_managed_volume_UEFI_optimized_untagged_template.copy(),
                           ]

negative_profile_template_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_dhcp_with_subnetmask.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_template_with_subnetmask_or_gateway'},
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_dhcp_with_gateway.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_dhcp_server_profile_template_with_subnetmask_or_gateway'},
]

delete_profile_templates = ['dhcp_primary_only_legacy_bios_untagged_template',
                            'dhcp_primary_only_legacy_bios_tunnel_template',
                            'dhcp_legacy_bios_untagged_template',
                            'dhcp_legacy_bios_tunnel_template',
                            'dhcp_primary_only_UEFI_untagged_template',
                            'dhcp_primary_only_UEFI_tunnel_template',
                            'dhcp_UEFI_untagged_template',
                            'dhcp_UEFI_tunnel_template',
                            'dhcp_primary_only_UEFI_optimized_untagged_template',
                            'dhcp_primary_only_UEFI_optimized_tunnel_template',
                            'dhcp_UEFI_optimized_untagged_template',
                            'dhcp_UEFI_optimized_tunnel_template',
                            'dhcp_managed_volume_primary_only_legacy_bios_untagged_template',
                            'dhcp_managed_volume_legacy_bios_untagged_template',
                            'dhcp_managed_volume_primary_only_UEFI_untagged_template',
                            'dhcp_managed_volume_UEFI_untagged_template',
                            'dhcp_managed_volume_primary_only_UEFI_optimized_untagged_template',
                            'dhcp_managed_volume_UEFI_optimized_untagged_template',
                            ]

negative_create_profile_with_v300 = [create_v300_profile.copy(), ]

create_profile_for_v300_verify = [bay7_profile1_one_connection_untagged.copy(), ]

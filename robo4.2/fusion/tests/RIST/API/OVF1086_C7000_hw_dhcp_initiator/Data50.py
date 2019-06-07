"""
OVF1086 C7000 HW DHCP initiator
"""
# pylint: disable=E0401,E0602
from copy import deepcopy
from dto import *
from env_variables_C7000 import *

admin_credentials = deepcopy(ADMIN_CREDENTIALS_COMMON)
oa_credentials = deepcopy(OA_CREDENTIALS_COMMON)
cliq_credentials = deepcopy(STOREVIRTUAL_SLPT_DHCP_CLIQ_CREDENTIALS)
ilo_credentials = deepcopy(ILO_CREDENTIALS_COMMON)
hpmctp_credentials = deepcopy(HPMCTP_CREDENTIALS_COMMON)

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY4 = '%s, interconnect 4' % ENC1
ENC1ICBAY5 = '%s, interconnect 5' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1
ENC2ICBAY1 = '%s, interconnect 1' % ENC2
ENC2ICBAY2 = '%s, interconnect 2' % ENC2
ENC2ICBAY3 = '%s, interconnect 3' % ENC2
ENC2ICBAY4 = '%s, interconnect 4' % ENC2
ENC2ICBAY5 = '%s, interconnect 5' % ENC2
ENC2ICBAY6 = '%s, interconnect 6' % ENC2
ENC3ICBAY1 = '%s, interconnect 1' % ENC3
ENC3ICBAY2 = '%s, interconnect 2' % ENC3
ENC3ICBAY3 = '%s, interconnect 3' % ENC3
ENC3ICBAY4 = '%s, interconnect 4' % ENC3
ENC3ICBAY5 = '%s, interconnect 5' % ENC3
ENC3ICBAY6 = '%s, interconnect 6' % ENC3

interconnects_expected = [
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY1, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY2, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY3, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY4, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY5, "productName": OCHO, },
    {"type": INTERCONNECT_TYPE, "name": ENC1ICBAY6, "productName": OCHO, },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY1, "productName": SUPERSHAW, },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY2, "productName": SUPERSHAW, },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY3, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY4, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY5, "productName": OCHO, },
    {"type": INTERCONNECT_TYPE, "name": ENC2ICBAY6, "productName": OCHO, },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY1, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY2, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY3, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY4, "productName": SHEPPARD, },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY5, "productName": UTAH, },
    {"type": INTERCONNECT_TYPE, "name": ENC3ICBAY6, "productName": UTAH, },
]
# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY2 = '%s, bay 2' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY4 = '%s, bay 4' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC1SHBAY14 = '%s, bay 14' % ENC1
ENC1SHBAY16 = '%s, bay 16' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC2SHBAY2 = '%s, bay 2' % ENC2
ENC2SHBAY3 = '%s, bay 3' % ENC2
ENC2SHBAY4 = '%s, bay 4' % ENC2
ENC2SHBAY5 = '%s, bay 5' % ENC2
ENC2SHBAY6 = '%s, bay 6' % ENC2
ENC2SHBAY7 = '%s, bay 7' % ENC2
ENC2SHBAY16 = '%s, bay 16' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3
ENC3SHBAY2 = '%s, bay 2' % ENC3
ENC3SHBAY3 = '%s, bay 3' % ENC3
ENC3SHBAY4 = '%s, bay 4' % ENC3
ENC3SHBAY5 = '%s, bay 5' % ENC3
ENC3SHBAY6 = '%s, bay 6' % ENC3
ENC3SHBAY7 = '%s, bay 7' % ENC3
ENC3SHBAY8 = '%s, bay 8' % ENC3
ENC3SHBAY9 = '%s, bay 9' % ENC3
ENC3SHBAY10 = '%s, bay 10' % ENC3

appliance = {
    'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    'applianceNetworks': [{
        'device': 'eth0',
        'macAddress': None,
        'interfaceName': 'Appliance',
        'activeNode': '1',
        'unconfigure': False,
        'ipv4Type': 'STATIC',
        'app1Ipv4Addr': APP1_IPV4_ADDRESS,
        'ipv6Type': 'UNCONFIGURE',
        'ipv4Subnet': IPV4_SUBNET,
        'ipv4Gateway': IPV4_GATEWAY,
        'hostname': HOSTNAME,
        'confOneNode': True,
        'domainName': 'DOMAIN_NAME',
        'ipv4NameServers': [IPV4_DNS1, IPV4_DNS2, IPV4_DNS3],
        'aliasDisabled': True
    }]
}

timeandlocale = {
    'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': TIME_ZONE, 'ntpServers': [NTP_SERVER_HOSTNAME],
    'locale': LOCALE_EN
}

users = [
    {
        "type": USER_AND_PERMISSION_TYPE,
        "userName": "Serveradmin",
        "fullName": "Serveradmin",
        "password": "Serveradmin",
        "emailAddress": "sarah@hp.com",
        "officePhone": "970-555-0003",
        "mobilePhone": "970-500-0003",
        "enabled": True,
        "permissions": [{
            "roleName": "Server administrator",
            "scopeUri": None
        }
        ]
    },
    {
        'userName': 'Networkadmin',
        'password': 'Networkadmin',
        'fullName': 'Networkadmin',
        "permissions": [{
            "roleName": "Network administrator",
            "scopeUri": None
        }
        ],
        'emailAddress': 'nat@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Backupadmin',
        'password': 'Backupadmin',
        'fullName': 'Backupadmin',
        "permissions": [{
            "roleName": "Backup administrator",
            "scopeUri": None
        }
        ],
        'emailAddress': 'backup@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    },
    {
        'userName': 'Noprivledge',
        'password': 'Noprivledge',
        'fullName': 'Noprivledge',
        "permissions": [{
            "roleName": "Read only",
            "scopeUri": None
        }
        ],
        'emailAddress': 'rheid@hp.com',
        'officePhone': '970-555-0003',
        'mobilePhone': '970-500-0003',
        'type': USER_AND_PERMISSION_TYPE
    }
]

licenses = [
    {
        'key':
            '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'
    },
    {
        'key':
            'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'
    },
]

ethernet_networks = [
    {
        'name': 'network-tunnel',
        'type': ETHERNET_NETWORK_TYPE,
        'vlanId': 1,
        'purpose': 'General',
        'smartLink': True,
        'privateNetwork': False,
        'connectionTemplateUri': None,
        'ethernetNetworkType': 'Tunnel'
    },
    {
        'name': 'network-untagged',
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
    },
]

network_sets = [
    {'name': 'NS1', 'type': NETWORK_SET_TYPE, 'networkUris': ['net100', 'net300'], 'nativeNetworkUri': 'net100'},
]

ligs = [
    {
        'name': LIG1_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': OCHO},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': OCHO},
        ],
        'uplinkSets': [
            {
                'name': 'us-untagged',
                'ethernetNetworkType': 'Untagged',
                'networkType': 'Ethernet',
                'networkUris': ['network-untagged'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '1', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
            {
                'name': 'us-tunnel',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['network-tunnel'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '2', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
            {
                'name': 'us-tagged',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['net100', 'net300'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                    {'bay': '4', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    {
        'name': LIG2_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': SUPERSHAW},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': SUPERSHAW},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': OCHO},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': OCHO},
        ],
        'uplinkSets': [
            {
                'name': 'us-untagged',
                'ethernetNetworkType': 'Untagged',
                'networkType': 'Ethernet',
                'networkUris': ['network-untagged'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '1', 'port': 'X1', 'speed': 'Auto'}
                ]
            },
            {
                'name': 'us-tunnel',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['network-tunnel'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '2', 'port': 'X1', 'speed': 'Auto'}
                ]
            },
            {
                'name': 'us-tagged',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['net100', 'net300'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                    {'bay': '4', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
    {
        'name': LIG3_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 3, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': SHEPPARD},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 5, 'type': UTAH},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 6, 'type': UTAH},
        ],
        'uplinkSets': [
            {
                'name': 'us-untagged',
                'ethernetNetworkType': 'Untagged',
                'networkType': 'Ethernet',
                'networkUris': ['network-untagged'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '1', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
            {
                'name': 'us-tunnel',
                'ethernetNetworkType': 'Tunnel',
                'networkType': 'Ethernet',
                'networkUris': ['network-tunnel'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '2', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
            {
                'name': 'us-tagged',
                'ethernetNetworkType': 'Tagged',
                'networkType': 'Ethernet',
                'networkUris': ['net100', 'net300'],
                'nativeNetworkUri': None,
                'mode': 'Auto',
                'logicalPortConfigInfos': [
                    {'bay': '3', 'port': 'X3', 'speed': 'Auto'},
                    {'bay': '4', 'port': 'X3', 'speed': 'Auto'}
                ]
            },
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None
    },
]

enc_groups = [
    {
        'name': EG1_NAME,
        'type': ENCLOSURE_GROUP_TYPE,
        'enclosureTypeUri': '/rest/enclosure-types/c7000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 8,
        'configurationScript': None,
        'interconnectBayMappings': [
            {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME},
            {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
        ]
    },
    {
        'name': EG2_NAME,
        'type': ENCLOSURE_GROUP_TYPE,
        'enclosureTypeUri': '/rest/enclosure-types/c7000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 8,
        'configurationScript': None,
        'interconnectBayMappings': [
            {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG2_NAME},
            {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
        ]
    },
    {
        'name': EG3_NAME,
        'type': ENCLOSURE_GROUP_TYPE,
        'enclosureTypeUri': '/rest/enclosure-types/c7000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 8,
        'configurationScript': None,
        'interconnectBayMappings': [
            {'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
            {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
            {'interconnectBay': 3, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
            {'interconnectBay': 4, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
            {'interconnectBay': 5, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
            {'interconnectBay': 6, 'logicalInterconnectGroupUri': 'LIG:' + LIG3_NAME},
            {'interconnectBay': 7, 'logicalInterconnectGroupUri': None},
            {'interconnectBay': 8, 'logicalInterconnectGroupUri': None}
        ]
    }
]

enclosures = [
    {
        'hostname': ENC1_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
        'enclosureGroupUri': 'EG:' + EG1_NAME,
        'force': True, 'licensingIntent': 'OneViewNoiLO'
    },
    {
        'hostname': ENC2_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
        'enclosureGroupUri': 'EG:' + EG2_NAME,
        'force': True, 'licensingIntent': 'OneViewNoiLO'
    },
    {
        'hostname': ENC3_OA1, 'username': oa_credentials['username'], 'password': oa_credentials['password'],
        'enclosureGroupUri': 'EG:' + EG3_NAME,
        'force': True, 'licensingIntent': 'OneViewNoiLO'
    },
]

enclosures_expected = [
    {"type": ENCLOSURE_TYPE, "name": "wpst22", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst23", "state": "Configured", },
    {"type": ENCLOSURE_TYPE, "name": "wpst26", "state": "Configured", },
]

STORAGE_POOL = 'VSA_Cluster_116'
DHCP_BOOT_TARGET_IP = "192.168.21.59"
CHAP_SECRET = "wpsthpvse123"
MCHAP_SECRET = "hpvse123wpst"

# VOLUME_TEMPLATE = 'Volume root template for StoreVirtual 1.2'

EXISTING_SHARED_VOLUME1 = "ovs3803-dhcp-shared-volume1"
NEW_PRIVATE_VOLUME1 = 'ovs3803-dhcp-private-volume1'
NEW_PRIVATE_VOLUME2 = 'ovs3803-dhcp-private-volume2'
NEW_PRIVATE_VOLUME3 = 'ovs3803-dhcp-private-volume3'
NEW_PRIVATE_VOLUME4 = 'ovs3803-dhcp-private-volume4'
Gen10_NEW_PRIVATE_VOLUME1 = 'ovs3803-gen10-dhcp-private-volume1'
Gen10_NEW_PRIVATE_VOLUME2 = 'ovs3803-gen10-dhcp-private-volume2'
Gen10_NEW_PRIVATE_VOLUME3 = 'ovs3803-gen10-dhcp-private-volume3'
Gen10_NEW_PRIVATE_VOLUME4 = 'ovs3803-gen10-dhcp-private-volume4'

INITIATOR_GATEWAY = "192.168.0.1"
INITIATOR_SUBNET_MASK = "255.255.192.0"

STORAGE_POOL_NETWORK = 'ETH:network-untagged'
NETWORK_SET = "NS1"

# PROFILE1 SETTINGS
PROFILE1_TEMPLATE_NAME = 'wpst22-bay1-DHCP-legacy-bios-hw-iSCSI-simplified-boot'
PROFILE1_EXISTING_VOLUME = 'wpst22-bay1-dhcp-managed-volume'
PROFILE1_SHT_NAME = 'BL465c Gen8:Flb1:HP FlexFabric 10Gb 2-port 554FLB Adapter'
PROFILE1_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-wpst22-bay1-dhcp-managed-volume'

# PROFILE2 SETTINGS
PROFILE2_TEMPLATE_NAME = 'wpst22-bay5-DHCP-uefi-hw-iSCSI-simplified-boot'
PROFILE2_EXISTING_VOLUME = 'wpst22-bay5-dhcp-managed-volume'
PROFILE2_SHT_NAME = 'BL460c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:1:HP FlexFabric 10Gb 2-port 534M Adapter:2:HP LPe1605 16Gb FC HBA for BladeSystem c-Class'
PROFILE2_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-wpst22-bay5-dhcp-managed-volume'
PROFILE2_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:769:wpst22-bay5-dhcp'
PROFILE2_CHAP_NAME = 'wpst22-bay5'
PROFILE2_MCHAP_NAME = 'wpst22-bay5'

# PROFILE3 SETTINGS
PROFILE3_TEMPLATE_NAME = 'wpst26-bay7-dhcp-uefi-optimized-hw-iSCSI-simplified-boot'
PROFILE3_EXISTING_VOLUME = 'wpst26-bay7-dhcp-managed-volume'
PROFILE3_SHT_NAME = 'BL660c Gen9:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter:Flb2:HP FlexFabric 10Gb 2-port 536FLB Adapter'
PROFILE3_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-wpst26-bay7-dhcp-managed-volume'

# PROFILE4 SETTINGS
PROFILE4_TEMPLATE_NAME = 'wpst22-bay14-dhcp-legacy-bios-hw-iSCSI-simplified-boot'
PROFILE4_EXISTING_VOLUME = 'wpst22-bay1-dhcp-managed-volume'
PROFILE4_SHT_NAME = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'
PROFILE4_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-wpst22-bay14-dhcp-managed-volume'

# PROFILE5 SETTINGS
PROFILE5_TEMPLATE_NAME = 'wpst22-bay16-dhcp-uefi-hw-iSCSI-simplified-boot'
PROFILE5_EXISTING_VOLUME = 'wpst22-bay5-dhcp-managed-volume'
PROFILE5_SHT_NAME = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'
PROFILE5_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-wpst22-bay16-dhcp-managed-volume'
PROFILE5_BOOT_TARGET_NAME = 'iqn.2003-10.com.lefthandnetworks:vsa-mg-116:769:wpst22-bay5-dhcp'
PROFILE5_CHAP_NAME = 'wpst22-bay5'
PROFILE5_MCHAP_NAME = 'wpst22-bay5'

# PROFILE6 SETTINGS
PROFILE6_TEMPLATE_NAME = 'wpst23-bay16-dhcp-uefi-optimized-hw-iSCSI-simplified-boot'
PROFILE6_EXISTING_VOLUME = 'wpst26-bay7-dhcp-managed-volume'
PROFILE6_SHT_NAME = 'BL460c Gen10:Flb1:HP FlexFabric 10Gb 2-port 536FLB Adapter'
PROFILE6_INITIATOR_NAME = 'iqn.2015-02.com.hpe:oneview-wpst23-bay16-dhcp-managed-volume'

existing_volumes = [
    {
        "storageSystemUri": STORAGE_POOL,
        "name": PROFILE1_EXISTING_VOLUME,
        "deviceVolumeName": PROFILE1_EXISTING_VOLUME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": PROFILE2_EXISTING_VOLUME,
        "deviceVolumeName": PROFILE2_EXISTING_VOLUME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": PROFILE3_EXISTING_VOLUME,
        "deviceVolumeName": PROFILE3_EXISTING_VOLUME,
        "isShareable": False,
    },
    {
        "storageSystemUri": STORAGE_POOL,
        "name": EXISTING_SHARED_VOLUME1,
        "deviceVolumeName": EXISTING_SHARED_VOLUME1,
        "isShareable": True,
    },
]

# UEFI
spt_hw_iscsi_managed_volume_uefi = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4":
                    {
                        "ipAddressSource": "DHCP",
                    },
                "boot":
                    {
                        "priority": "Primary",
                        "bootVolumeSource": "ManagedVolume",
                    },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# UEFI optimized
spt_hw_iscsi_managed_volume_uefi_optimized = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Legacy BIOS
spt_hw_iscsi_managed_volume_legacy_bios = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME3,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Gen10 UEFI
gen10_spt_hw_iscsi_dhcp_managed_volume_uefi = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE5_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE5_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary", "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": Gen10_NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    "templateVersion": STORAGE_VOLUME_TEMPLATE_TYPE,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# gen10 UEFI optimized
gen10_spt_hw_iscsi_dhcp_managed_volume_uefi_optimized = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE6_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG2_NAME,
    "name": PROFILE6_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": Gen10_NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    "templateVersion": STORAGE_VOLUME_TEMPLATE_TYPE,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Gen10 Legacy BIOS
gen10_spt_hw_iscsi_dhcp_managed_volume_legacy_bios = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE4_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE4_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "bootMode": {"manageMode": True, "mode": "BIOS"},
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }

                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": Gen10_NEW_PRIVATE_VOLUME3,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    "templateVersion": STORAGE_VOLUME_TEMPLATE_TYPE,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}
# edit UEFI template to change to a different boot volume
edit_spt_hw_iscsi_managed_volume_uefi = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME4,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# edit UEFI optimized to add a secondary boot volume
edit_spt_hw_iscsi_managed_volume_uefi_optimized = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# edit Legacy BIOS to disable simplified boot
edit_spt_hw_iscsi_managed_volume_legacy_bios = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [],
        "manageBoot": False
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    }
}

# UEFI edit 2 back to original
edit2_spt_hw_iscsi_managed_volume_uefi = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# UEFI optimized back to original
edit2_spt_hw_iscsi_managed_volume_uefi_optimized = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE3_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Legacy BIOS back to original
edit2_spt_hw_iscsi_managed_volume_legacy_bios = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [{
            "id": 1,
            "bootVolumePriority": "Primary",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": NEW_PRIVATE_VOLUME3,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                # "propertiesTemplateVersion": 1,
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# edit gen10 UEFI optimized to add a secondary boot volume
edit_gen10_spt_hw_iscsi_dhcp_managed_volume_uefi_optimized = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE6_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG2_NAME,
    "name": PROFILE6_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "sanSystemCredentials": [{"storageSystemUri": "SSYS:" + STORAGE_POOL, "chapLevel": "MutualChap"}],
        "volumeAttachments": [{
            "associatedTemplateAttachmentId": 'SPTVAID:1',
            "id": 1,
            "bootVolumePriority": "Primary",
            "lunType": "Auto",
            "storagePaths": [{
                "isEnabled": True,
                "connectionId": 1,
                "targetSelector": "Auto",
            }, {
                "isEnabled": True,
                "connectionId": 2,
                "targetSelector": "Auto",
            }],
            "volume": {
                "isPermanent": True,
                "properties": {
                    "name": Gen10_NEW_PRIVATE_VOLUME2,
                    "storagePool": "SPOOL:" + STORAGE_POOL,
                    "size": 21474836480,
                    "provisioningType": "Thin",
                    "isShareable": False,
                    "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                },
                "templateUri": "ROOT:" + STORAGE_POOL,
            },
            "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
            "volumeUri": None,
        }]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and UEFI
sp_from_spt_hw_uefi_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [{
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# verify DTO fro Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and UEFI
verify_sp_from_spt_hw_uefi_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + NEW_PRIVATE_VOLUME1,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and UEFI optimized
sp_from_spt_hw_iscsi_uefi_optimized_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC3SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Verify DTO for Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and UEFI optimized
verify_sp_from_spt_hw_iscsi_uefi_optimized_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC3SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + NEW_PRIVATE_VOLUME2,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and Legacy BIOS
sp_from_spt_hw_legacy_bios_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME3,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Verify DTO for Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and Legacy BIOS
verify_sp_from_spt_hw_legacy_bios_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + NEW_PRIVATE_VOLUME3,
            }
        ]

    }
}

# Gen10 Create SP from template with HW iSCSI boot from StoreVirtual managed volume using defined volume and UEFI optimized
gen10_sp_from_spt_hw_iscsi_dhcp_uefi_optimized_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC2SHBAY16,
    "serverProfileTemplateUri": 'SPT:' + PROFILE6_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG2_NAME,
    "name": PROFILE6_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE6_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": Gen10_NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Verify gen10 DTO for Create template with HW iSCSI boot from StoreVirtual managed volume using defined volume and UEFI optimized
verify_gen10_sp_from_spt_hw_iscsi_dhcp_uefi_optimized_defined_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC2SHBAY16,
    "serverProfileTemplateUri": 'SPT:' + PROFILE6_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG2_NAME,
    "name": PROFILE6_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE6_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }, {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + NEW_PRIVATE_VOLUME3,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}
# Create template with HW iSCSI boot from StoreVirtual managed volume using existing volume and UEFI
sp_from_spt_hw_uefi_existing_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 2,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    }, ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + PROFILE2_EXISTING_VOLUME,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume using existing volume and UEFI optimized
sp_from_spt_hw_iscsi_uefi_optimized_existing_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC3SHBAY7,
    "serverProfileTemplateUri": 'SPT:' + PROFILE3_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE3_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 2,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + PROFILE3_EXISTING_VOLUME,
            }
        ], "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Create template with HW iSCSI boot from StoreVirtual managed volume using existing volume and Legacy BIOS
sp_from_spt_hw_legacy_bios_existing_volume = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 2,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

sp_from_spt_hw_iscsi_uefi_compliant = {
    "name": PROFILE2_TEMPLATE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_from_spt_hw_iscsi_uefi_optimized_compliant = {
    "name": PROFILE3_TEMPLATE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_from_spt_hw_iscsi_legacy_bios_compliant = {
    "name": PROFILE1_TEMPLATE_NAME,
    "compliance-preview": {
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE,
        "automaticUpdates": [],
        "manualUpdates": []
    }
}

sp_from_spt_hw_iscsi_uefi_non_compliant = {
    "name": PROFILE2_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [
            "REGEX:Configure SAN storage to managed by profile\.",
            "REGEX:Change host OS type to RHE Linux \(5.x, 6.x, 7.x\)\.",
            "REGEX:Create an attachment to a new volume \"" + NEW_PRIVATE_VOLUME1 + "\"\.",
            "REGEX:Add a storage path using connection \"1\" to attachment for volume \"" + NEW_PRIVATE_VOLUME1 + "\"\.",
        ],
        "manualUpdates": [
            "REGEX:Change boot source of connection \d on port FlexibleLOM \(Flb\) \d:\d-b to Managed volume\.",
            "REGEX:Change boot setting of volume attachment for volume \"" + NEW_PRIVATE_VOLUME1 + "\" to primary\."
        ],
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE
    }
}

sp_from_spt_hw_iscsi_legacy_bios_non_compliant = {
    "name": PROFILE1_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to enabled\.",
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to enabled\.",
            "REGEX:Change boot setting for volume {\"name\":\".*\", \"uri\":\".*\"} attachment id \"\d\" to match the associated template setting\.",
        ],
        "manualUpdates": [],
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE

    }
}

sp_from_spt_hw_iscsi_legacy_bios_non_compliant2 = {
    "name": PROFILE1_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [
            "REGEX:Create an attachment to a new volume \"" + NEW_PRIVATE_VOLUME4 + "\"\.",
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to disabled\.",
            "REGEX:Change storage path using connection \"\d\" in volume attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} to disabled\.",
        ],
        "manualUpdates": [
            "REGEX:The boot setting for attachment id \"\d\" for volume {\"name\":\".*\", \"uri\":\".*\"} does not match the associated template setting\.  Change either the profile or the template setting accordingly\."
        ],
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE

    }
}

sp_from_spt_hw_iscsi_uefi_optimized_non_compliant = {
    "name": PROFILE3_TEMPLATE_NAME,
    "compliance-preview": {
        "automaticUpdates": [],
        "manualUpdates": [
            "REGEX:Change server hardware type to {\"name\":\".*\", \"uri\":\".*\"}."

        ],
        "type": SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE

    }
}

# Edit legacy bios SP to boot from a non-associated ATAI
compliance_legacy_bios_non_associated_atai = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY1,
    "serverProfileTemplateUri": 'SPT:' + PROFILE1_TEMPLATE_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE1_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 2,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "bootVolumePriority": "Primary",
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + PROFILE1_EXISTING_VOLUME,
            }, {
                "id": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": None,
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": "V:" + NEW_PRIVATE_VOLUME3,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Removing the bootable volume
comliance_uefi_no_simplified_boot = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareUri': 'SH:' + ENC1SHBAY5,
    "serverProfileTemplateUri": 'SPT:' + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "connections": [
            {
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "UserDefined",
                    "iscsi": {
                        "initiatorNameSource": "ProfileInitiatorName",
                        "bootTargetName": PROFILE2_BOOT_TARGET_NAME,
                        "bootTargetLun": "0",
                        "firstBootTargetIp": DHCP_BOOT_TARGET_IP,
                        "firstBootTargetPort": "3260",
                        "chapLevel": "MutualChap",
                        "chapName": PROFILE2_CHAP_NAME,
                        "chapSecret": CHAP_SECRET,
                        "mutualChapName": PROFILE2_MCHAP_NAME,
                        "mutualChapSecret": MCHAP_SECRET
                    }
                },
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ]
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
}

# Edit legacy bios SPT to boot from a non-associated ATAI
compliance_legacy_bios_non_associated_atai_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    "serverHardwareTypeUri": 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "localStorage": {
        "sasLogicalJBODs": [],
        "controllers": []
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": False,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "bootVolumePriority": "Primary",
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME3,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            },
            {
                "id": 2,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME4,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Removing the bootable volume
comliance_uefi_no_managed_boot_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [],
        "manageBoot": False
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': [],
    }
}

# edit UEFI optimized template to different SHT
comliance_uefi_optimized_different_sht_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG3_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [{
                    "isEnabled": True,
                    "connectionId": 1,
                    "targetSelector": "Auto",
                },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME2,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Legacy BIOS back to original
edit_compliance_legacy_bios_return_to_compliant_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE1_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE1_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "PXE",
            "HardDisk",
        ],
        "manageBoot": True
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                    {
                        "isEnabled": True,
                        "connectionId": 2,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME3,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# UEFI edit 2 back to original
edit_compliance_uefi_return_to_compliant_template = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorNameType": "UserDefined",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "chapLevel": "MutualChap",
                "storageSystemUri": "SSYS:" + STORAGE_POOL
            }
        ]
    }
}

# Multiple primary boot connections
negative_spt_1 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "wpst10-negative-1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Only secondary boot connection
negative_spt_2 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "wpst10-negative-2",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Multiple secondary boot connection
negative_spt_3 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "wpst10-negative-3",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Secondary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            },
            {
                "functionType": "iSCSI",
                "id": 2,
                "ipv4":
                    {
                        "ipAddressSource": "DHCP",
                    },
                "boot":
                    {
                        "priority": "Secondary",
                        "bootVolumeSource": "ManagedVolume",
                    },
                "name": "Connection 2",
                "networkUri": STORAGE_POOL_NETWORK,
            },
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# SW iSCSI on C7000
negative_spt_4 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative-spt-4",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "Ethernet",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "ethernetBootType": "iSCSI",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# iSCSI boot without managed storage
negative_spt_5 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative-spt-5",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        'manageSanStorage': False,
        'volumeAttachments': []
    }
}

# iSCSI boot with non-bootable volume
negative_spt_6 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_6",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Multiple boot volumes selected
negative_spt_7 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_7",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }, {
                "id": 2,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "volume 2",
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Existing shared volume
negative_spt_8 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_8",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + EXISTING_SHARED_VOLUME1,
            }
        ]
    }
}

# Existing private volume
negative_spt_9 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_9",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "connectionId": 1,
                        "isEnabled": True,
                        "targetSelector": "Auto",
                    }
                ],
                "volume": None,
                "volumeUri": "SVOL:" + PROFILE1_EXISTING_VOLUME,
            }
        ]
    }
}

# New shared volume
negative_spt_10 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_10",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "negative-volume",
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": True,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Disabled storage path
negative_spt_11 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_11",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": False,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "negative_spt_11",
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# Using network set
negative_spt_12 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_12",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": "NS:" + NETWORK_SET,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "negative_spt_12",
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# managed boot while specifying iscsi section
negative_spt_13 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_spt_13",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "boot": {
                    "bootVolumeSource": "ManagedVolume",
                    "priority": "Primary",
                    "iscsi": {
                        "chapLevel": "None",
                        "initiatorName": "iqn.2015-02.com.hpe:oneview-vcgs03t010",
                        "initiatorNameSource": "UserDefined"
                    }
                },
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "name": "Connection 131",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": "negative_spt_13",
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# edit to disable Boot Volume for managed volume
negative_spt_14 = {
    "type": SERVER_PROFILE_TEMPLATE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": PROFILE3_TEMPLATE_NAME,
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFIOptimized",
        "pxeBootPolicy": "Auto"
    },
    "connectionSettings": {
        "manageConnections": True,
        "connections": [
            {
                "functionType": "iSCSI",
                "id": 1,
                "ipv4": {
                    "ipAddressSource": "DHCP",
                },
                "boot": {
                    "priority": "Primary",
                    "bootVolumeSource": "ManagedVolume",
                },
                "name": "Connection 1",
                "networkUri": STORAGE_POOL_NETWORK,
            }
        ],
    },
    "sanStorage": {
        "hostOSType": "RHE Linux (5.x, 6.x, 7.x)",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "associatedTemplateAttachmentId": 'SPTVAID:1',
                "id": 1,
                "bootVolumePriority": "NotBootable",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": True,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 21474836480,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ],
        "sanSystemCredentials": [
            {
                "storageSystemUri": "SSYS:" + STORAGE_POOL,
                "chapLevel": "MutualChap"
            }
        ]
    }
}

# Create profile from template with simplified iSCSI boot without initiator IP
negative_sp_from_spt_1 = {
    "type": SERVER_PROFILE_TYPE,
    'serverHardwareTypeUri': 'SHT:' + PROFILE2_SHT_NAME,
    "serverProfileTemplateUri": "SPT:" + PROFILE2_TEMPLATE_NAME,
    "iscsiInitiatorName": PROFILE2_INITIATOR_NAME,
    "enclosureGroupUri": "EG:" + EG1_NAME,
    "name": "negative_sp_from_spt_1",
    "affinity": "Bay",
    "bios": {
        "manageBios": False
    },
    "boot": {
        "order": ['HardDisk'],
        "manageBoot": True
    },
    "bootMode": {
        "manageMode": True,
        "mode": "UEFI",
        "pxeBootPolicy": "Auto"
    },
    "connections": [
        {
            "functionType": "iSCSI",
            "id": 1,
            "ipv4": {
                "ipAddressSource": "DHCP",
            },
            "boot": {
                "priority": "Primary",
                "bootVolumeSource": "ManagedVolume",
            },
            "name": "Connection 1",
            "networkUri": STORAGE_POOL_NETWORK,
        }
    ],
    "sanStorage": {
        "hostOSType": "Windows 2012 / WS2012 R2",
        "manageSanStorage": True,
        "volumeAttachments": [
            {
                "id": 1,
                "bootVolumePriority": "Primary",
                "lunType": "Auto",
                "storagePaths": [
                    {
                        "isEnabled": True,
                        "connectionId": 1,
                        "targetSelector": "Auto",
                    },
                ],
                "volume": {
                    "isPermanent": False,
                    "properties": {
                        "name": NEW_PRIVATE_VOLUME1,
                        "storagePool": "SPOOL:" + STORAGE_POOL,
                        "size": 1073741824,
                        "provisioningType": "Thin",
                        "isShareable": False,
                        "dataProtectionLevel": "NetworkRaid10Mirror2Way",
                    },
                    # "propertiesTemplateVersion": 1,
                    "templateUri": "ROOT:" + STORAGE_POOL,
                },
                "volumeStorageSystemUri": "SSYS:" + STORAGE_POOL,
                "volumeUri": None,
            }
        ]
    }
}

# sp_power = [
#   {
#         'serverHardwareUri': 'SH:'+ETHERNET_BLADE,
#   },
#   {
#         'serverHardwareUri': 'SH:'+ISCSI_BLADE,
#   },
#   {
#         'serverHardwareUri': 'SH:'+NEG_ISCSI_BLADE,
#   },
#   {
#         'serverHardwareUri': 'SH:'+NEG_ETHERNET_BLADE,
#   },
# ]

create_templates = [
    spt_hw_iscsi_managed_volume_legacy_bios.copy(),
    spt_hw_iscsi_managed_volume_uefi.copy(),
    spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
]

create_gen10_templates = [
    gen10_spt_hw_iscsi_dhcp_managed_volume_legacy_bios.copy(),
    gen10_spt_hw_iscsi_dhcp_managed_volume_uefi.copy(),
    gen10_spt_hw_iscsi_dhcp_managed_volume_uefi_optimized.copy(),
]

edit_templates1 = [
    edit_spt_hw_iscsi_managed_volume_uefi.copy(),
    edit_spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
    edit_spt_hw_iscsi_managed_volume_legacy_bios.copy(),
]

edit_templates2 = [
    edit2_spt_hw_iscsi_managed_volume_legacy_bios.copy(),
    edit2_spt_hw_iscsi_managed_volume_uefi.copy(),
    edit2_spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
]

edit_gen10_templates = [edit_gen10_spt_hw_iscsi_dhcp_managed_volume_uefi_optimized.copy(), ]

negative_spt_tasks = [
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_1.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_primary_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_2.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_secondary_boot_connection'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_3.copy(),
        'taskState': 'Error',
        'errorMessage': 'Multiple_secondary_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_4.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_ethernet_with_iSCSI_boot'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_5.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_6.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_7.copy(),
        'taskState': 'Error',
        'errorMessage': 'DuplicateBootVolumePriority'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_8.copy(),
        'taskState': 'Error',
        'errorMessage': 'Only_private_boot_volume'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_9.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_attach_exist_private_volume'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_10.copy(),
        'taskState': 'Error',
        'errorMessage': 'ShareablePendingVolumeAttachmentNotSupported'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_11.copy(),
        'taskState': 'Error',
        'errorMessage': 'Managed_Volume_No_Bootable_Connections'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_12.copy(),
        'taskState': 'Error',
        'errorMessage': 'Profile_network_set_iscsi'
    },
    {
        'keyword': 'Add Server Profile Template',
        'argument': negative_spt_13.copy(),
        'taskState': 'Error',
        'errorMessage': 'Invalid_iSCSI_target_data_managed_volume'
    },
    {
        'keyword': 'Edit Server Profile Template',
        'argument': negative_spt_14.copy(),
        'taskState': 'Error',
        'errorMessage': 'SPT_Bootable_connection_nonbootable_volume'
    },
]

negative_sp_tasks = [
    # {
    #     'keyword': 'Add Server Profile',
    #     'argument': negative_sp_from_spt_1.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'iSCSI_initiator_IP_required'},
    # {
    #     'keyword': 'Add Server Profile',
    #     'argument': negative_sp_from_spt_2.copy(),
    #     'taskState': 'Error',
    #     'errorMessage': 'iSCSI_initiator_IP_required'},
]

create_sp_from_spt = [
    sp_from_spt_hw_uefi_defined_volume.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_defined_volume.copy(),
    sp_from_spt_hw_legacy_bios_defined_volume.copy(),
]

create_gen10_sp_from_spt = [gen10_sp_from_spt_hw_iscsi_dhcp_uefi_optimized_defined_volume.copy(), ]

verify_create_sp_from_spt = [
    verify_sp_from_spt_hw_uefi_defined_volume.copy(),
    verify_sp_from_spt_hw_iscsi_uefi_optimized_defined_volume.copy(),
    verify_sp_from_spt_hw_legacy_bios_defined_volume.copy(),
]

verify_create_gen10_sp_from_spt = [verify_gen10_sp_from_spt_hw_iscsi_dhcp_uefi_optimized_defined_volume.copy()]

edit_sp_from_spt = [
    sp_from_spt_hw_uefi_existing_volume.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_existing_volume.copy(),
    sp_from_spt_hw_legacy_bios_existing_volume.copy(),
]

edit_compliance1_sp_from_spt = [
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS compliance_legacy_bios_non_associated_atai.copy(),
    comliance_uefi_no_simplified_boot.copy(),
]

edit_compliance2_template = [
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS compliance_legacy_bios_non_associated_atai_template.copy(),
    comliance_uefi_no_managed_boot_template.copy(),
    comliance_uefi_optimized_different_sht_template.copy(),
]

edit_compliance3_template = [
    edit_compliance_legacy_bios_return_to_compliant_template.copy(),
    edit_compliance_uefi_return_to_compliant_template.copy(),
    edit2_spt_hw_iscsi_managed_volume_uefi_optimized.copy(),
]

sp_compliance = [
    sp_from_spt_hw_iscsi_uefi_compliant.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_compliant.copy(),
    sp_from_spt_hw_iscsi_legacy_bios_compliant.copy(),
]

verify_non_compliance_sp_from_spt = [
    sp_from_spt_hw_iscsi_uefi_non_compliant.copy(),
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS sp_from_spt_hw_iscsi_legacy_bios_non_compliant.copy(),
]

verify_non_compliance_sp_from_spt2 = [
    # sp_from_spt_hw_iscsi_uefi_non_compliant.copy(),
    # 4.20 6/15 RS, this edit now fails at the task.  Never gets to compliance check.  Create Negative tests?
    # RS sp_from_spt_hw_iscsi_legacy_bios_non_compliant2.copy(),
    sp_from_spt_hw_iscsi_uefi_optimized_non_compliant.copy(),
]

delete_profile_templates = [
    PROFILE1_TEMPLATE_NAME,
    PROFILE2_TEMPLATE_NAME,
    PROFILE3_TEMPLATE_NAME,
]

delete_gen10_profile_templates = [
    PROFILE4_TEMPLATE_NAME,
    PROFILE5_TEMPLATE_NAME,
    PROFILE6_TEMPLATE_NAME,
]

new_permanent_volumes = [
    {"properties": {"name": NEW_PRIVATE_VOLUME1}},
    {"properties": {"name": NEW_PRIVATE_VOLUME2}},
    {"properties": {"name": NEW_PRIVATE_VOLUME3}},
    {"properties": {"name": NEW_PRIVATE_VOLUME4}},
]

gen10_new_permanent_volumes = [
    {"properties": {"name": Gen10_NEW_PRIVATE_VOLUME2}},
]

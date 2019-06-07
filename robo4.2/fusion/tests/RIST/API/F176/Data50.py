from robot.libraries.BuiltIn import BuiltIn
from dto import *
from env_variables import *

try:
    TEST_RING = BuiltIn().get_variable_value("${X_TEST_RING}")
except:  # noqa
    TEST_RING = 'DCS'

# Potash interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC2ICBAY6 = '%s, interconnect 6' % ENC2

# Natasha SAS interconnects
ENC1SASICBAY1 = '%s, interconnect 1' % ENC1
ENC1SASICBAY4 = '%s, interconnect 4' % ENC1

# Drive Enclosures (Bigbird)
ENC1DEBAY1 = '%s, bay 1' % ENC1

# Server Hardware
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY5 = '%s, bay 5' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1
ENC1SHBAY7 = '%s, bay 7' % ENC1
ENC2SHBAY1 = '%s, bay 1' % ENC2
ENC3SHBAY1 = '%s, bay 1' % ENC3

appliance = {
    "type": APPLIANCE_NETWORK_CONFIGURATION_TYPE,
    "applianceNetworks": [
        {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": "16.114.210.227", "app1Ipv6Addr": "",
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
         "webServerCertificateChain": None, "webServerCertificateKey": None}
    ],
    "serverCertificate": {
        "rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
        "rabbitMQCertificateKey": None, "postgresCertificate": None,
        "postgresRootCACertificate": None, "postgresCertificateKey": None}
}

timeandlocale = {'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'],
                 'locale': 'en_US.UTF-8'}

users = [
    {'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'],
     'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin',
     'roles': ['Network administrator'],
     'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'],
     'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'],
     'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE}
]

licenses = [
    {
        'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
    {
        'key': 'AA9C AQAA H9PY CHVY V7B5 HWWB Y9JL KMPL 3JKH 5FVM DXAU 2CSM GHTG L762 MTK7 FYB9 KJVT D5KM EFVW DT5J 4BEM M2SC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZXJ-RDCJQ-55T3M-BP3H2'},
    {
        'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
    {
        'key': 'AAAE BQAA H9P9 CHW2 V7B5 HWWB Y9JL KMPL SRWE 8HJU DXAU 2CSM GHTG L762 LAB2 VRJA KJVT D5KM EFVW DT5J TF9K 54C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G7SK-QDGSY-LRT8D-PWPVP-QWRKW'},
    {
        'key': '9AQA BQAA H9PA GHWZ V7B5 HWWB Y9JL KMPL SR2G 7AZU DXAU 2CSM GHTG L762 69VZ USJA KJVT D5KM EFVW DT5J VFQM 85S8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3G8YL-HHGX3-6M6KH-DZ99V-BDXMM'},
    {
        'key': 'YAAE DQAA H9P9 GHV3 U7B5 HWW5 Y9JL KMPL CRKE 6AJU DXAU 2CSM GHTG L762 H9Z2 WUZY KJVT D5KM EFVW DT5J FFAK N5C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
]

enclosures = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, },
    {"type": ENCLOSURE_TYPE, "name": ENC2, },
    {"type": ENCLOSURE_TYPE, "name": ENC3, },
]

sasics = [
    {"name": ENC1SASICBAY1, "portCount": 12},
    {"name": ENC1SASICBAY4, "portCount": 12}
]

sasics_bay1 = [
    {"name": ENC1SASICBAY1, "portCount": 12}
]

sasics_bay4 = [
    {"name": ENC1SASICBAY4, "portCount": 12}
]

ics = [
    {"name": ENC1ICBAY3},
    {"name": ENC2ICBAY6}
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
     'type': ETHERNET_NETWORK_TYPE,
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100'],
                 'nativeNetworkUri': 'net100'}]

icmap = [
    {'bay': 3,
     'enclosure': 1,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
     'enclosureIndex': 1},
    {'bay': 6,
     'enclosure': 2,
     'type': 'Virtual Connect SE 40Gb F8 Module for Synergy',
     'enclosureIndex': 2},
    {'bay': 6,
     'enclosure': 1,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 1},
    {'bay': 3,
     'enclosure': 2,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 2},
    {'bay': 3,
     'enclosure': 3,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 3},
    {'bay': 6,
     'enclosure': 3,
     'type': 'Synergy 20Gb Interconnect Link Module',
     'enclosureIndex': 3},
]

uplink_sets = {'us_untagged': {'name': 'us-untagged',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['network-untagged'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3',
                                                           'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'enclosure': '2',
                                                           'bay': '6',
                                                           'port': 'Q1.1',
                                                           'speed': 'Auto'}]},
               'us_tagged': {'name': 'us-tagged',
                             'ethernetNetworkType': 'Tagged',
                             'networkType': 'Ethernet',
                             'networkUris': ['net100', 'net300'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3',
                                                         'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '2',
                                                         'bay': '6',
                                                         'port': 'Q2.1',
                                                         'speed': 'Auto'}]},
               'us_tunnel': {'name': 'us-tunnel',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['network-tunnel'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
                                                        {'enclosure': '2',
                                                         'bay': '6',
                                                         'port': 'Q3.1',
                                                         'speed': 'Auto'}]}, }

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
         'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tagged'].copy(),
                        uplink_sets['us_tunnel'].copy(), ], }]

sasligs = [{'name': SASLIG_NAME,  # Single SAS switch
            "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
            "enclosureType": "SY12000",
            "enclosureIndexes": [1],
            "interconnectBaySet": "1",
            'interconnectMapTemplate': [
                {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'Synergy 12Gb SAS Connection Module'}]}]

edit_sasligs = [{"name": SASLIG_NAME,  # Dual SAS switch
                 "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
                 "enclosureType": "SY12000",
                 "enclosureIndexes": [1],
                 "interconnectBaySet": "1",
                 'interconnectMapTemplate': [
                     {'enclosure': 1,
                      'enclosureIndex': 1,
                      'bay': 1,
                      'type': 'Synergy 12Gb SAS Connection Module'},
                     {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': 'Synergy 12Gb SAS Connection Module'}]}]

egs = [{'name': EG_NAME,
        'type': ENCLOSURE_GROUP_TYPE,
        'enclosureCount': 3,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'interconnectBayMappingCount': 2,
        'configurationScript': None,
        'interconnectBayMappings':
        [
            {"interconnectBay": 3,
             "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
            {"interconnectBay": 6,
             "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"}]

edit_egs = [{'name': EG_NAME,
             'type': ENCLOSURE_GROUP_TYPE,
             'enclosureCount': 3,
             'enclosureTypeUri': '/rest/enclosure-types/SY12000',
             'stackingMode': 'Enclosure',
             'interconnectBayMappingCount': 3,
             'configurationScript': None,
             'interconnectBayMappings':
             [{"enclosureIndex": 1, "interconnectBay": 1, "logicalInterconnectGroupUri": "SASLIG:" + SASLIG_NAME},
              {"interconnectBay": 3,
               "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
              {"interconnectBay": 6,
               "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}, ],
             'ipAddressingMode': "External",
             'ipRangeUris': [],
             'powerMode': "RedundantPowerFeed"}]

les = [{'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False}]

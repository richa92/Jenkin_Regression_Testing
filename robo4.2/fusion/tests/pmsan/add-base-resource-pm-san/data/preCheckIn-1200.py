from robot.libraries.BuiltIn import BuiltIn

APPLIANCE_ADMIN_PASSWORD = "hpvse123"
X_API_VERSION = 1200

# Credentials
ADMIN_CREDENTIALS = {'userName': 'Administrator', 'password': 'hpvse123'}
OA_CREDENTIALS = {'username': 'dcs', 'password': 'dcs'}

# Resource types for X-API-Version=800
APPLIANCE_NETWORK_CONFIGURATION_TYPE = 'ApplianceNetworkConfigurationV2'
TIME_AND_LOCALE_TYPE = 'TimeAndLocale'
USER_AND_PERMISSION_TYPE = 'UserAndPermissions'
ETHERNET_NETWORK_TYPE = 'ethernet-networkV4'
FC_NETWORK_TYPE = 'fc-networkV4'
LOGICAL_INTERCONNECT_GROUP_TYPE = 'logical-interconnect-groupV4'
INTERCONNECT_TYPE = 'InterconnectV4'
ENCLOSURE_TYPE = 'EnclosureV7'
ENCLOSURE_GROUP_TYPE = 'EnclosureGroupV7'
SERVER_HARDWARE_TYPE = 'server-hardware-8'
STORAGE_SYSTEM_TYPE = 'StorageSystemV4'
STORAGE_POOL_TYPE = 'StoragePoolV4'
STORAGE_VOLUME_TEMPLATE_TYPE = 'StorageTemplateV4'
STORAGE_VOLUME_TYPE = 'StorageVolumeV4'
SERVER_PROFILE_TEMPLATE_TYPE = 'ServerProfileTemplateV6'
SERVER_PROFILE_TYPE = 'ServerProfileV10'
SERVER_PROFILE_COMPLIANCE_PREVIEW_TYPE = 'ServerProfileCompliancePreviewV1'
SAS_LOGICAL_INTERCONNECT_GROUP_TYPE = 'sas-logical-interconnect-groupV2'

# FTS, users, and licenses
APP1_IPV4_ADDRESS = BuiltIn().get_variable_value("${APPLIANCE_IP}")
HOSTNAME = APP1_IPV4_ADDRESS
APPLIANCE = {'type': APPLIANCE_NETWORK_CONFIGURATION_TYPE,
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
                   'aliasDisabled': False}]}

TIMEANDLOCALE = {'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': 'UTC', 'ntpServers': ['ntp.hpecorp.net'], 'locale': 'en_US.UTF-8'}

USERS = [
    {"userName": "Serveradmin", 'password': 'Serveradmin', 'fullName': 'Serveradmin', "permissions": [{"roleName": "Server administrator", "scopeUri": None}], 'emailAddress': "sarah@hp.com", "officePhone": "970-555-0003", "mobilePhone": "970-500-0003", 'type': USER_AND_PERMISSION_TYPE, "enabled": True},
    {'userName': 'Networkadmin', 'password': 'Networkadmin', 'fullName': 'Networkadmin', "permissions": [{"roleName": "Network administrator", "scopeUri": None}], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Backupadmin', 'password': 'Backupadmin', 'fullName': 'Backupadmin', "permissions": [{"roleName": "Backup administrator", "scopeUri": None}], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Noprivledge', 'password': 'Noprivledge', 'fullName': 'Noprivledge', "permissions": [{"roleName": "Read only", "scopeUri": None}], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': USER_AND_PERMISSION_TYPE}
]

LICENSES = [
    {'key': '9A9C DQAA H9PY CHV2 V7B5 HWWB Y9JL KMPL DJKD 5FFM DXAU 2CSM GHTG L762 TT66 VZRY KJVT D5KM EFVW DT5J EBE9 M2CC SPS9 YG66 Z99R MWSN 6Z84 46XT WZJL HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTFG LS8T XU4E "EVAL-HPOV-NFR1 HPOV-NFR1 HP_OneView_16_Seat_NFR 7T36AEJG7JJ9"_3MBSY-CJZY2-LDVV4-92DQT-L6TTW'},
    {'key': 'AA9C DQAA H9PA GHX3 U7B5 HWW5 Y9JL KMPL SR6C MHJU DXAU 2CSM GHTG L762 9AVY WXJY KJVT D5KM EFVW DT5J TFQ9 74C8 SPS9 YG66 Z99R MWSN 6Z84 46XT WZJT HH4Q L975 SNJT ZWWC AADW NJ79 CEJC 5S86 FC4X EKSZ X4CP XZLU FMXS FKS6 KKCE 4NMU FGN5 F8CG Z2HX FRJ6 EPM2 2SJV VTVG LS8T XU4E "EVAL-HPOV-NFR2 HPOV-NFR2 HP_OneView_w/o_iLO_16_Seat_NFR 9G6UAEJGUA4U"'},
]
# SAN Manager and Managed SANs
SAN_MANAGERS = [
    {
        "connectionInfo": [
            {'name': 'Type', 'value': 'Brocade Network Advisor'},
            {"name": "Host", "displayName": "Host", "required": True, "value": "172.18.15.1", "valueFormat": "IPAddressOrHostname", "valueType": "String"},
            {"name": "Port", "displayName": "Port", "required": True, "value": 5989, "valueFormat": "None", "valueType": "Integer"},
            {"name": "Username", "displayName": "Username", "required": True, "value": "dcs", "valueFormat": "None", "valueType": "String"},
            {"name": "Password", "displayName": "Password", "required": True, "value": "dcs", "valueFormat": "SecuritySensitive", "valueType": "String"},
            {"name": "UseSsl", "displayName": "UseSsl", "required": True, "value": True, "valueFormat": "None", "valueType": "Boolean"},
        ],
    }
]
FA_SAN_A = 'SAN1_0'
FA_SAN_B = 'SAN1_1'

# Enclosures, Interconnects, Server Hardware, Networks, ULS, LIG, and EG
# Enclosures
ENC1 = 'Encl1'
ENC1_OA1 = "172.18.1.11"

# Interconnects
ENC1ICBAY1 = '%s, interconnect 1' % ENC1
ENC1ICBAY2 = '%s, interconnect 2' % ENC1

# LIGs and EGs
LIG1_NAME = 'dcs-eg LIG'
EG1_NAME = 'dcs-eg'

ETHERNET_NETWORKS = [
    {'name': 'eth100', 'type': ETHERNET_NETWORK_TYPE, 'vlanId': 100, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
    {'name': 'eth200', 'type': ETHERNET_NETWORK_TYPE, 'vlanId': 200, 'purpose': 'General', 'smartLink': True, 'privateNetwork': False, 'connectionTemplateUri': None, 'ethernetNetworkType': 'Tagged'},
]

FC_NETWORKS = [
    {'name': 'fa1', 'type': FC_NETWORK_TYPE, 'fabricType': 'FabricAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'managedSanUri': 'FCSan:' + FA_SAN_A, 'connectionTemplateUri': None},
    {'name': 'fa2', 'type': FC_NETWORK_TYPE, 'fabricType': 'FabricAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'managedSanUri': 'FCSan:' + FA_SAN_B, 'connectionTemplateUri': None},
    {'name': 'fa3', 'type': FC_NETWORK_TYPE, 'fabricType': 'FabricAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'managedSanUri': None},
    {'name': 'fa4', 'type': FC_NETWORK_TYPE, 'fabricType': 'FabricAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True, 'managedSanUri': None},
    {'name': 'da1', 'type': FC_NETWORK_TYPE, 'fabricType': 'DirectAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True},
    {'name': 'da2', 'type': FC_NETWORK_TYPE, 'fabricType': 'DirectAttach', 'linkStabilityTime': 30, 'autoLoginRedistribution': True}
]

LIGS = [
    {
        'name': LIG1_NAME,
        'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
        'enclosureType': 'C7000',
        'interconnectMapTemplate': [
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
            {'enclosure': 1, 'enclosureIndex': 1, 'bay': 2, 'type': 'HP VC FlexFabric 10Gb/24-Port Module'},
        ],
        'uplinkSets': [
            {'name': 'ul-eth100', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth100'], 'nativeNetworkUri': None, 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X5', 'speed': 'Auto'}, {'bay': '2', 'port': 'X5', 'speed': 'Auto'}]},
            {'name': 'ul-eth200', 'ethernetNetworkType': 'Tagged', 'networkType': 'Ethernet', 'networkUris': ['eth200'], 'nativeNetworkUri': None, 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X6', 'speed': 'Auto'}, {'bay': '2', 'port': 'X6', 'speed': 'Auto'}]},
            {'name': 'ul-da1', 'ethernetNetworkType': 'NotApplicable', 'networkType': 'FibreChannel', 'networkUris': ['da1'], 'nativeNetworkUri': None, 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X1', 'speed': 'Auto'}]},
            {'name': 'ul-da2', 'ethernetNetworkType': 'NotApplicable', 'networkType': 'FibreChannel', 'networkUris': ['da2'], 'nativeNetworkUri': None, 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X1', 'speed': 'Auto'}]},
            {'name': 'ul-fa1', 'ethernetNetworkType': 'NotApplicable', 'networkType': 'FibreChannel', 'networkUris': ['fa1'], 'nativeNetworkUri': None, 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '1', 'port': 'X2', 'speed': 'Auto'}]},
            {'name': 'ul-fa2', 'ethernetNetworkType': 'NotApplicable', 'networkType': 'FibreChannel', 'networkUris': ['fa2'], 'nativeNetworkUri': None, 'mode': 'Auto', 'logicalPortConfigInfos': [{'bay': '2', 'port': 'X2', 'speed': 'Auto'}]},
        ],
        'stackingMode': 'Enclosure',
        'ethernetSettings': None,
        'state': 'Active',
        'telemetryConfiguration': None,
        'snmpConfiguration': None},
]

ENC_GROUPS = [{'name': EG1_NAME, 'configurationScript': None, 'interconnectBayMappings': [{'interconnectBay': 1, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, {'interconnectBay': 2, 'logicalInterconnectGroupUri': 'LIG:' + LIG1_NAME}, ]}]

ENCLOSURES = [
    {'hostname': ENC1_OA1, 'username': OA_CREDENTIALS['username'], 'password': OA_CREDENTIALS['password'], 'enclosureGroupUri': 'EG:' + EG1_NAME, 'force': True, 'licensingIntent': 'OneView', "firmwareBaselineUri": None, },
]

# StoreServ
STORESERV1_NAME = 'ThreePAR-2'
STORESERV1_HOSTNAME = '172.18.11.12'
STORESERV1_POOL1 = 'FST_CPG1'
STORESERV1_POOL2 = 'FST_CPG2'

# StoreVirtual
STOREVIRTUAL1_NAME = 'Cluster-1'
STOREVIRTUAL1_HOSTNAME = '172.18.30.1'
STOREVIRTUAL1_VIP = '172.18.30.1'
STOREVIRTUAL1_POOL = 'Cluster-1'

STORAGE_SYSTEMS = [
    {"type": STORAGE_SYSTEM_TYPE, "name": STORESERV1_NAME, "family": "StoreServ", "hostname": STORESERV1_HOSTNAME, "credentials": {"username": "dcs", "password": "dcs"}, "deviceSpecificAttributes": {"discoveredDomains": ["NO DOMAIN", ], "managedDomain": "TestDomain", }, },
    {"type": STORAGE_SYSTEM_TYPE, "name": STOREVIRTUAL1_NAME, "family": "StoreVirtual", "hostname": STOREVIRTUAL1_HOSTNAME, "credentials": {"username": "dcs", "password": 'dcs'}, "ports": [{"name": STOREVIRTUAL1_VIP, "expectedNetworkUri": "ETH:eth100", "expectedNetworkName": "eth100", "mode": "Managed", }, ], },
]

STORAGE_POOLS = [
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL1, "isManaged": True, },
    {"storageSystemUri": STORESERV1_NAME, "name": STORESERV1_POOL2, "isManaged": True, },
]

from copy import deepcopy
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
        {"activeNode": 1, "unconfigure": False, "app1Ipv4Addr": APPLIANCE1_IP, "app1Ipv6Addr": "",
         "app2Ipv4Addr": APPLIANCE2_IP, "app2Ipv6Addr": "",
         "virtIpv4Addr": APPLIANCE_VIP, "virtIpv6Addr": None, "app1Ipv4Alias": None,
         "app1Ipv6Alias": None,
         "app2Ipv4Alias": None, "app2Ipv6Alias": None, "hostname": APPLIANCE_HOSTNAME,
         "confOneNode": True, "interfaceName": "", "macAddress": None,
         "ipv4Type": IPV4_TYPE, "ipv6Type": IPV6_TYPE, "overrideIpv4DhcpDnsServers": False,
         "ipv4Subnet": IPV4_SUBNET, "ipv4Gateway": IPV4_GATEWAY, "ipv6Subnet": IPV6_SUBNET,
         "ipv6Gateway": IPV6_GATEWAY,
         "domainName": DOMAIN_NAME, "searchDomains": [],
         "ipv4NameServers": [IPV4_DNS1, IPV4_DNS2],
         "ipv6NameServers": [IPV4_DNS1, IPV4_DNS2], "bondedTo": None, "aliasDisabled": True,
         "configureRabbitMqSslListener": False, "configurePostgresSslListener": False,
         "webServerCertificate": None,
         "webServerCertificateChain": None, "webServerCertificateKey": None}
    ],
    "serverCertificate": {
        "rabbitMQCertificate": None, "rabbitMQRootCACertificate": None,
        "rabbitMQCertificateKey": None, "postgresCertificate": None,
        "postgresRootCACertificate": None, "postgresCertificateKey": None}
}

Time_and_Locale = {'type': TIME_AND_LOCALE_TYPE,
                   'locale': 'en_US.UTF-8',
                   'timezone': TIME_ZONE,
                   'ntpServers': [NTP_SERVER]}

timeandlocale = {'type': TIME_AND_LOCALE_TYPE, 'dateTime': None, 'timezone': TIME_ZONE,
                 'ntpServers': [NTP_SERVER_HOSTNAME],
                 'locale': LOCALE_EN}

users = [
    {'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin',
     'roles': ['Server administrator'], 'emailAddress': 'sarah@hpe.com',
     'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin',
     'roles': ['Network administrator'],
     'emailAddress': 'nat@hpe.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin',
     'roles': ['Backup administrator'], 'emailAddress': 'backup@hpe.com',
     'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003',
     'type': USER_AND_PERMISSION_TYPE},
    {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge',
     'roles': ['Read only'], 'emailAddress': 'rheid@hpe.com', 'officePhone': '970-555-0003',
     'mobilePhone': '970-500-0003', 'type': USER_AND_PERMISSION_TYPE}
]

enclosures = [
    {"type": ENCLOSURE_TYPE, "name": ENC1, },
    {"type": ENCLOSURE_TYPE, "name": ENC2, },
    {"type": ENCLOSURE_TYPE, "name": ENC3, },
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

interconnects_linked_ports_expected = [
    {
        "name": ENC1 + ", interconnect 3",
        "linked_ports": ['d3', 'd5', 'd6', 'd7', 'd8', 'd13', 'd17',
                         'd19', 'd20', 'd25', 'd29', 'Q1:1', 'Q2:1', 'Q3:1',
                         'Q4:1', 'Q7', 'Q8', 'l1', 'l2', 'l3', 'l4']

    },
    {
        "name": ENC1 + ", interconnect 6",
        "linked_ports": ['d3', 'd5', 'd6', 'd7', 'd8', 'l1', 'l2']
    },
    {
        "name": ENC2 + ", interconnect 3",
        "linked_ports": ['d1', 'd5', 'd7', 'd8', 'l1', 'l2']
    },
    {
        "name": ENC2 + ", interconnect 6",
        "linked_ports": ['d1', 'd5', 'd7', 'd8', 'd15', 'd17', 'd18', 'd19',
                         'd20', 'd25', 'd29', 'Q1:1', 'Q2:1',
                         'Q3:1', 'Q4:1', 'Q7', 'Q8', 'l1', 'l2', 'l3', 'l4']
    },
    {
        "name": ENC3 + ", interconnect 3",
        "linked_ports": ['d1', 'd5', 'l1', 'l2']
    },
    {
        "name": ENC3 + ", interconnect 6",
        "linked_ports": ['d1', 'd5', 'l1', 'l2']
    },
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

fc_networks = [
    {'name': 'FA1',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
    {'name': 'FA2',
     'type': FC_NETWORK_TYPE,
     'fabricType': 'FabricAttach',
     'linkStabilityTime': 30,
     'autoLoginRedistribution': True,
     'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
]

fcoe_networks = [
    {'name': 'FCoE_350', 'type': FCOE_NETWORK_TYPE,
     'vlanId': 350, 'managedSanUri': 'FCSan:VSAN350'},
    {'name': 'FCoE_450', 'type': FCOE_NETWORK_TYPE,
     'vlanId': 450, 'managedSanUri': 'FCSan:VSAN450'}
]

san_managers = [
    {"connectionInfo": [
        {'name': 'Type',
         'value': SAN_MANAGER_BNA},
        {"name": "Host",
         "displayName": "Host",
         "required": True,
         "value": SAN_MANAGER_BNA_IP,
         "valueFormat": "IPAddressOrHostname",
         "valueType": "String"},
        {"name": "Port",
         "displayName": "Port",
         "required": True,
         "value": 5989,
         "valueFormat": "None",
         "valueType": "Integer"},
        {"name": "Username",
         "displayName": "Username",
         "required": True,
         "value": "Administrator",
         "valueFormat": "None",
         "valueType": "String"},
        {"name": "Password",
         "displayName": "Password",
         "required": True,
         "value": "password",
         "valueFormat": "SecuritySensitive",
         "valueType": "String"},
        {"name": "UseSsl",
         "displayName": "UseSsl",
         "required": True,
         "value": True,
         "valueFormat": "None",
         "valueType": "Boolean"},
    ], },
    {"connectionInfo": [
        {'name': 'Type', 'value': SAN_MANAGER_HPE},
        {"name": "Host", "value": SAN_MANAGER_HPE_IP},
        {"name": "SnmpPort", "value": 161},
        {"name": "SnmpUserName", "value": "UNoAuthNoPriv"},
        {"name": "SnmpAuthLevel", "value": "NOAUTHNOPRIV"},
        {"name": "SnmpAuthProtocol", "value": ""},
        {"name": "SnmpAuthString", "value": ""},
        {"name": "SnmpPrivProtocol", "value": ""},
        {"name": "SnmpPrivString", "value": ""}
    ], },
]

network_sets = [{'name': 'NS1',
                 'type': NETWORK_SET_TYPE,
                 'networkUris': ['net100'],
                 'nativeNetworkUri': 'net100'}]

icmap = [
    {'bay': 3,
     'enclosure': 1,
     'type': POTASH,
     'enclosureIndex': 1},
    {'bay': 6,
     'enclosure': 2,
     'type': POTASH,
     'enclosureIndex': 2},
    {'bay': 6,
     'enclosure': 1,
     'type': CHLORIDE20,
     'enclosureIndex': 1},
    {'bay': 3,
     'enclosure': 2,
     'type': CHLORIDE20,
     'enclosureIndex': 2},
    {'bay': 3,
     'enclosure': 3,
     'type': CHLORIDE20,
     'enclosureIndex': 3},
    {'bay': 6,
     'enclosure': 3,
     'type': CHLORIDE20,
     'enclosureIndex': 3},
]

icmap_carbon = [
    {'bay': 1,
     'enclosure': -1,
     'type': CARBON16,
     'enclosureIndex': -1},
    {'bay': 4,
     'enclosure': -1,
     'type': CARBON16,
     'enclosureIndex': -1}
]

uplink_sets = {
    'us_untagged': {
        'name': 'us-untagged',
        'ethernetNetworkType': 'Untagged',
        'networkType': 'Ethernet',
        'networkUris': ['network-untagged'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
        ]},
    'us_tagged': {
        'name': 'us-tagged',
        'ethernetNetworkType': 'Tagged',
        'networkType': 'Ethernet',
        'networkUris': ['net100', 'net300'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'},
        ]},
    'us_tunnel': {
        'name': 'us-tunnel',
        'ethernetNetworkType': 'Tunnel',
        'networkType': 'Ethernet',
        'networkUris': ['network-tunnel'],
        'nativeNetworkUri': None,
        'mode': 'Auto',
        'lacpTimer': 'Long',
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q3.1', 'speed': 'Auto'},
            {'enclosure': '2', 'bay': '6', 'port': 'Q3.1', 'speed': 'Auto'},
        ]},
    'FA-path1': {
        'name': 'FA-path1',
        'ethernetNetworkType': None,
        'networkType': 'FibreChannel',
        'networkUris': ['FA1'],
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '1', 'bay': '3', 'port': 'Q4:1', 'speed': 'Auto'}
        ]},
    'FA-path2': {
        'name': 'FA-path2',
        'ethernetNetworkType': None,
        'networkType': 'FibreChannel',
        'networkUris': ['FA2'],
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '2', 'bay': '6', 'port': 'Q4:1', 'speed': 'Auto'}
        ]}
}

uplink_sets2 = {
    'FCoE-path1': {'name': 'FCoE-path1',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': ['FCoE_350'],
                   'primaryPort': None,
                   'logicalPortConfigInfos': [
                       {'enclosure': '1', 'bay': '3', 'port': 'Q5:1', 'speed': 'Auto'}
                   ]},
    'FCoE-path2': {'name': 'FCoE-path2',
                   'ethernetNetworkType': 'Tagged',
                   'networkType': 'Ethernet',
                   'networkUris': ['FCoE_450'],
                   'primaryPort': None,
                   'logicalPortConfigInfos': [
                       {'enclosure': '2', 'bay': '6', 'port': 'Q5:1', 'speed': 'Auto'}
                   ]}
}

uplink_sets_carbons = [
    {
        'name': 'FA-path5',
        'ethernetNetworkType': None,
        'networkType': 'FibreChannel',
        'networkUris': ['FA5'],
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '-1', 'bay': '1', 'port': '4', 'speed': 'Auto'}
        ]
    },
    {
        'name': 'FA-path6',
        'ethernetNetworkType': None,
        'networkType': 'FibreChannel',
        'networkUris': ['FA6'],
        'primaryPort': None,
        'logicalPortConfigInfos': [
            {'enclosure': '-1', 'bay': '4', 'port': '4', 'speed': 'Auto'}
        ]
    }
]

ligs_carbon = [{
    'name': CARBON_LIG_NAME,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': 'SY12000',
    'interconnectMapTemplate': icmap_carbon,
    'enclosureIndexes': [-1],
    'interconnectBaySet': 1,
    'redundancyType': 'Redundant',
    'ethernetSettings': None,
    'snmpConfiguration': None,
    'uplinkSets': uplink_sets_carbons,
}]


def add_uplink_sets():
    upls = [
        uplink_sets['us_untagged'].copy(),
        uplink_sets['us_tagged'].copy(),
        uplink_sets['us_tunnel'].copy(),
        uplink_sets['FA-path1'].copy(),
        uplink_sets['FA-path2'].copy()
    ]
    if TEST_RING == 'Ring2':
        upls = deepcopy(upls)
        upls.extend([
            uplink_sets2['FCoE-path1'].copy(),
            uplink_sets2['FCoE-path2'].copy()
        ])
    return upls


ligs = [{
    'name': LIG_NAME,
    'type': LOGICAL_INTERCONNECT_GROUP_TYPE,
    'enclosureType': FRAME_TYPE,
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
    'uplinkSets': add_uplink_sets()
}]

sasligs = [{
    'name': SASLIG_NAME,  # Single SAS switch
    "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
    "enclosureType": FRAME_TYPE,
    "enclosureIndexes": [1],
    "interconnectBaySet": "1",
    'interconnectMapTemplate': [
        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': NATASHA}
    ]
}]

edit_sasligs = [{
    "name": SASLIG_NAME,  # Dual SAS switch
    "type": SAS_LOGICAL_INTERCONNECT_GROUP_TYPE,
    "enclosureType": FRAME_TYPE,
    "enclosureIndexes": [1],
    "interconnectBaySet": "1",
    'interconnectMapTemplate': [
        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 1, 'type': NATASHA},
        {'enclosure': 1, 'enclosureIndex': 1, 'bay': 4, 'type': NATASHA}
    ]
}]


def icbaymap():
    baymap = [
        {"interconnectBay": 3,
         "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
        {"interconnectBay": 6,
         "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
    ]
    if TEST_RING == 'Ring2':
        baymap = deepcopy(baymap)
        baymap.extend([
            {"interconnectBay": 1, "enclosureIndex": 2,
             "logicalInterconnectGroupUri": "LIG:" + CARBON_LIG_NAME},
            {"interconnectBay": 4, "enclosureIndex": 2,
             "logicalInterconnectGroupUri": "LIG:" + CARBON_LIG_NAME}
        ])
    return baymap


egs = [{
    'name': EG_NAME,
    'enclosureCount': 3,
    'configurationScript': None,
    'interconnectBayMappings': icbaymap(),
    'ipAddressingMode': "External",
    'ipRangeUris': [],
    'powerMode': "RedundantPowerFeed"
}]

edit_egs = [{
    'name': EG_NAME,
    'type': ENCLOSURE_GROUP_TYPE,
    'enclosureCount': 3,
    'enclosureTypeUri': '/rest/enclosure-types/SY12000',
    'stackingMode': 'Enclosure',
    'interconnectBayMappingCount': 3,
    'configurationScript': None,
    'interconnectBayMappings': [
        {"enclosureIndex": 1, "interconnectBay": 1,
         "logicalInterconnectGroupUri": "SASLIG:" + SASLIG_NAME},
        {"enclosureIndex": 2, "interconnectBay": 1,
         "logicalInterconnectGroupUri": "SASLIG:" + SASLIG_NAME},
        {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
        {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
    ],
    'ipAddressingMode': "External",
    'ipRangeUris': [],
    'powerMode': "RedundantPowerFeed"
}]

les = [{
    'name': LE_NAME,
    'enclosureUris': ['ENC:' + ENC1, 'ENC:' + ENC2, 'ENC:' + ENC3],
    'enclosureGroupUri': "EG:" + EG_NAME,
    'firmwareBaselineUri': None,
    'forceInstallFirmware': False
}]

storage_systems = [
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': STORESERV1_NAME,
        'family': 'StoreServ',
        "hostname": STORESERV1_HOSTNAME,
        'credentials': STORESERV1_CREDENTIALS,
        "deviceSpecificAttributes":
            {
                "discoveredDomains": ["NO DOMAIN"],
                "managedDomain": STORESERV1_MANAGED_DOMAIN,
            },
    },
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': STOREVIRTUAL_SLPT_STATIC_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL_SLPT_STATIC_HOSTNAME,
        "credentials": STOREVIRTUAL_SLPT_STATIC_CREDENTIALS,
        "ports": [
            {
                "name": STOREVIRTUAL_SLPT_STATIC_VIP,
                "expectedNetworkUri": "ETH:network-untagged",
                "expectedNetworkName": "network-untagged",
                "mode": "Managed",
            },
        ],
    },
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': STOREVIRTUAL_SLPT_DHCP_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL_SLPT_DHCP_HOSTNAME,
        "credentials": STOREVIRTUAL_SLPT_DHCP_CREDENTIALS,
        "ports": [
            {
                "name": STOREVIRTUAL_SLPT_DHCP_VIP,
                "expectedNetworkUri": "ETH:network-untagged",
                "expectedNetworkName": "network-untagged",
                "mode": "Managed",
            },
        ],
    },
    {
        'type': STORAGE_SYSTEM_TYPE,
        'name': STOREVIRTUAL_MLPT_NAME,
        "family": "StoreVirtual",
        "hostname": STOREVIRTUAL_MLPT_HOSTNAME,
        "credentials": STOREVIRTUAL_MLPT_CREDENTIALS,
        "ports": [
            {
                "name": STOREVIRTUAL_MLPT_VIP,
                "expectedNetworkUri": "ETH:network-tunnel",
                "expectedNetworkName": "network-tunnel",
                "mode": "Managed",
            },
        ],
    },
]

storage_pools = [
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL1,
        "isManaged": True,
    },
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL2,
        "isManaged": True,
    },
    {
        "storageSystemUri": STORESERV1_NAME,
        "name": STORESERV1_POOL3,
        "isManaged": True,
    },
]

if TEST_RING == 'Ring2':
    fc_networks = deepcopy(fc_networks)
    storage_systems = deepcopy(storage_systems)
    storage_pools = deepcopy(storage_pools)
    ligs = deepcopy(ligs)
    ligs_carbon = deepcopy(ligs_carbon)

    fc_networks.extend([
        {'name': 'FA5',
         'type': FC_NETWORK_TYPE,
         'fabricType': 'FabricAttach',
         'linkStabilityTime': 30,
         'autoLoginRedistribution': True,
         'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID100-10:00:00:27:f8:fe:0c:55'},
        {'name': 'FA6',
         'type': FC_NETWORK_TYPE,
         'fabricType': 'FabricAttach',
         'linkStabilityTime': 30,
         'autoLoginRedistribution': True,
         'managedSanUri': 'FCSan:wpstsan14.vse.rdlabs.hpecorp.net-FID101-10:00:00:27:f8:fe:0c:56'},
    ])

    storage_systems.append({
        'type': STORAGE_SYSTEM_TYPE,
        'name': 'fvt3par-8400-1-srv',
        'family': 'StoreServ',
        'hostname': 'fvt3par-8400-1-srv.vse.rdlabs.hpecorp.net',
        'credentials': {'username': '3paradm', 'password': '3pardata'},
        'deviceSpecificAttributes':
            {'discoveredDomains': ['NO DOMAIN'], 'managedDomain': FCOE_DOMAIN}
    })

    storage_pools.extend([
        {'storageSystemUri': STORESERV2_NAME, "name": STORESERV2_POOL1, "isManaged": True, },
        {'storageSystemUri': STORESERV2_NAME, "name": STORESERV2_POOL5, "isManaged": True, }
    ])

    ligs.extend(ligs_carbon)

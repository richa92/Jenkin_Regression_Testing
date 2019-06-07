FUSION_IP = '16.114.211.81'
FUSION_USERNAME = 'Administrator'    # Fusion Appliance Username
FUSION_PASSWORD = 'wpsthpvse1'         # Fusion Appliance Password
FUSION_SSH_USERNAME = 'root'             # Fusion SSH Username
FUSION_SSH_PASSWORD = 'hpvse1'        # Fusion SSH Password
FUSION_PROMPT = '#'               # Fusion Appliance Prompt
FUSION_TIMEOUT = 180              # Timeout.  Move this out???
FUSION_NIC = 'bond0'            # Fusion Appliance Primary NIC
FUSION_NIC_SUFFIX = '%' + FUSION_NIC

admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}

ilo_credentials = {'username': 'Administrator', 'password': 'hpvse123'}

LIG_NAME = 'LIG1'
EG_NAME = 'EG1'
LE_NAME = 'LE1'

# Enclosures
ENC1 = 'CN744502F0'
# Interconnects
ENC1ICBAY3 = '%s, interconnect 3' % ENC1
ENC1ICBAY6 = '%s, interconnect 6' % ENC1

# ports
DownLinkPort = 'd2'
UpLinkPort = 'Q1:1'

# Server Hardware
ENC1SHBAY1 = '%s, bay 1' % ENC1
ENC1SHBAY2 = '%s, bay 2' % ENC1
ENC1SHBAY3 = '%s, bay 3' % ENC1
ENC1SHBAY6 = '%s, bay 6' % ENC1

users = [{'userName': 'Serveradmin', 'password': 'wpsthpvse1', 'fullName': 'Serveradmin', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Networkadmin', 'password': 'wpsthpvse1', 'fullName': 'Networkadmin', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Backupadmin', 'password': 'wpsthpvse1', 'fullName': 'Backupadmin', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'},
         {'userName': 'Noprivledge', 'password': 'wpsthpvse1', 'fullName': 'Noprivledge', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndPermissions'}
         ]

enclosures = [
    {"type": "EnclosureV300", "name": ENC1, },
]

ics = [
    {"name": ENC1ICBAY3, },
    {"name": ENC1ICBAY6, },
]

ethernet_networks = [
    {'name': 'network-tunnel',
     'type': 'ethernet-networkV300',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tunnel'},
    {'name': 'network-untagged',
     'type': 'ethernet-networkV300',
     'vlanId': 0,
     'subnetUri': None,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Untagged'},
    {'name': 'net100',
     'type': 'ethernet-networkV300',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
    {'name': 'net300',
     'type': 'ethernet-networkV300',
     'vlanId': 300,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},
]

network_sets = [{'name': 'NS1', 'type': 'network-setV300', 'networkUris': ['net100', 'net300'], 'nativeNetworkUri': 'net100'}, ]

icmap = [
    {'bay': 3, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
    {'bay': 6, 'enclosure': 1, 'type': 'Virtual Connect SE 40Gb F8 Module for Synergy', 'enclosureIndex': 1},
]

uplink_sets = {'us_untagged': {'name': 'us-untagged',
                               'ethernetNetworkType': 'Untagged',
                               'networkType': 'Ethernet',
                               'networkUris': ['network-untagged'],
                               'nativeNetworkUri': None,
                               'mode': 'Auto',
                               'lacpTimer': 'Long',
                               'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          {'enclosure': '1', 'bay': '6', 'port': 'Q1.1', 'speed': 'Auto'},
                                                          ]
                               },
               'us_tunnel': {'name': 'us-tunnel',
                             'ethernetNetworkType': 'Tunnel',
                             'networkType': 'Ethernet',
                             'networkUris': ['network-tunnel'],
                             'nativeNetworkUri': None,
                             'mode': 'Auto',
                             'lacpTimer': 'Long',
                             'logicalPortConfigInfos': [{'enclosure': '1', 'bay': '3', 'port': 'Q2.1', 'speed': 'Auto'},
                                                        {'enclosure': '1', 'bay': '6', 'port': 'Q2.1', 'speed': 'Auto'}
                                                        ]
                             },
               }

ligs = [
    {'name': LIG_NAME,
     'type': 'logical-interconnect-groupV300',
     'enclosureType': 'SY12000',
     'interconnectMapTemplate': icmap,
     'enclosureIndexes': [1],
     'interconnectBaySet': 3,
     'redundancyType': 'Redundant',
     'ethernetSettings': None,
     'fcoeSettings': {'fcoeMode': 'FcfNpv'},
     'stackingMode': 'Enclosure',
     'state': 'Active',
     'telemetryConfiguration': None,
     'snmpConfiguration': None,
     'uplinkSets': [uplink_sets['us_untagged'].copy(), uplink_sets['us_tunnel'].copy()],
     },
]

egs = [{'name': EG_NAME,
        'type': 'EnclosureGroupV300',
        'enclosureCount': 1,
        'enclosureTypeUri': '/rest/enclosure-types/SY12000',
        'stackingMode': 'Enclosure',
        'interconnectBayMappingCount': 2,
        'configurationScript': None,
        'interconnectBayMappings':
        [
            {"interconnectBay": 3, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME},
            {"interconnectBay": 6, "logicalInterconnectGroupUri": "LIG:" + LIG_NAME}
        ],
        'ipAddressingMode': "External",
        'ipRangeUris': [],
        'powerMode': "RedundantPowerFeed"
        }
       ]


les = [{'name': LE_NAME,
        'enclosureUris': ['ENC:' + ENC1],
        'enclosureGroupUri': "EG:" + EG_NAME,
        'firmwareBaselineUri': None,
        'forceInstallFirmware': False
        }]

potash_on = [{"name": ENC1ICBAY3, "uri": "IC:" + ENC1ICBAY3, "powerState": "On"}]
potash_off = [{"name": ENC1ICBAY3, "uri": "IC:" + ENC1ICBAY3, "powerState": "Off"}]

disable_uplink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": ENC1ICBAY3,
    "portType": "Uplink",
    "portId": "Q1:1",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": UpLinkPort,
    "portStatus": "Linked",
    "type": "port"
}

disable_downlink = {
    "associatedUplinkSetUri": "us-unTagged",
    "interconnectName": ENC1ICBAY3,
    "portType": "Downlink",
    "portId": "d2",
    "portHealthStatus": "Normal",
    "capability": ["EnetFcoe", "Ethernet", "FibreChannel"],
    "configPortTypes": ["EnetFcoe", "Ethernet"],
    "enabled": False,
    "portName": DownLinkPort,
    "portStatus": "Linked",
    "type": "port"
}
server_profiles = [
    {
        'type': 'ServerProfileV7',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 1',
        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 1',
        'description': '',
        'affinity': 'Bay',
        'connections': [
            {
                'id': 1,
                'name': 'untagged',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:untagged',
                'mac': None,
                'wwpn': None,
                'wwnn': None,
                'requestedVFs': '0',
                'ipv4': {}
            },
            {
                'id': 2,
                'name': 'tunnel',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:tunnel',
                'mac': None,
                'wwpn': None,
                'wwnn': None,
                'requestedVFs': '0',
                'ipv4': {}
            }
        ],
        'boot': None,
        'bootMode': {'manageMode': False},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '',
                     'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': ''},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorName':'',
        'osDeploymentSettings': None,
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        #   'localStorage': {
        #   'sasLogicalJBODs': [ ],
        #   'controllers': [
        #       {
        #           'logicalDrives': [{
        #               'name':'rd0',
        #               'raidLevel':'RAID0',
        #               'bootable': False,
        #               'numPhysicalDrives': 1,
        #               'driveTechnology':'SasHdd',
        #               'sasLogicalJBODId': None,
        #               'driveNumber': None
        #               }
        #       ],
        #      'deviceSlot':'Embedded',
        #      'mode':'RAID',
        #       'initialize': False,
        #      'importConfiguration': False
        #     }
        #   ]
        # },
        'sanStorage': None
    },
    {
        'type': 'ServerProfileV7',
        'serverHardwareUri': 'SH:' + ENC1 + ', bay 2',
        'serverHardwareTypeUri': 'SHT:SY 480 Gen9:3:HP Synergy 3820C 10/20Gb CNA',
        'enclosureGroupUri': 'EG:EG1',
        'serialNumberType': 'Virtual',
        'iscsiInitiatorNameType': 'AutoGenerated',
        'macType': 'Virtual',
        'wwnType': 'Virtual',
        'name': ENC1 + ', bay 2',
        'description': '',
        'affinity': 'Bay',
        'connections': [
            {
                'id': 1,
                'name': 'untagged',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:untagged',
                'mac': None,
                'wwpn': None,
                'wwnn': None,
                'requestedVFs': '0',
                'ipv4': {}
            },
            {
                'id': 2,
                'name': 'tunnel',
                'functionType': 'Ethernet',
                'portId': 'Auto',
                'requestedMbps': '2500',
                'networkUri': 'ETH:tunnel',
                'mac': None,
                'wwpn': None,
                'wwnn': None,
                'requestedVFs': '0',
                'ipv4': {}
            }
        ],
        'boot': None,
        'bootMode': {'manageMode': False},
        'firmware': {'manageFirmware': False, 'firmwareBaselineUri': '',
                     'forceInstallFirmware': False, 'firmwareInstallType': None, 'firmwareScheduleDateTime': ''},
        'bios': {'manageBios': False, 'overriddenSettings': []},
        'hideUnusedFlexNics': True,
        'iscsiInitiatorName':'',
        'osDeploymentSettings': None,
        'localStorage': {'sasLogicalJBODs': [], 'controllers': []},
        #   'localStorage': {
        #   'sasLogicalJBODs': [ ],
        #   'controllers': [
        #       {
        #           'logicalDrives': [{
        #               'name':'rd0',
        #               'raidLevel':'RAID0',
        #               'bootable': False,
        #               'numPhysicalDrives': 1,
        #               'driveTechnology':'SasHdd',
        #               'sasLogicalJBODId': None,
        #               'driveNumber': None
        #               }
        #       ],
        #      'deviceSlot':'Embedded',
        #      'mode':'RAID',
        #       'initialize': False,
        #      'importConfiguration': False
        #     }
        #   ]
        # },
        'sanStorage': None
    },
]

from winnt import NULL
from requests.api import patch


def make_range_list(start, end, prefix='net_', suffix=''):
    rlist = []
    for x in xrange(start, end + 1):
        rlist.append(prefix + str(x) + suffix)
    return rlist

SSH_PASS = 'hpvse1'

admin_credentials = {'userName': 'Administrator', 'password': 'hpvse123'}

storage_admin = {'userName': 'storage', 'password': 'storageadmin'}

network_admin = {'userName': 'network', 'password': 'networkadmin'}

server_admin = {'userName': 'server', 'password': 'serveradmin'}

readonly_admin = {'userName': 'readonly', 'password': 'readonly'}

backup_admin = {'userName': 'backup', 'password': 'backupadmin'}

Testdata_ALLOCATE_2 = [
    {'type': 'Subnet',
     'gateway': '111.111.111.1',
     'networkId': '111.111.111.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet111.com'},

    {'type': 'Range',
     'startAddress': '111.111.111.5',
     'endAddress': '111.111.111.15',
     'name': 'RangeForSubnet111_1',
     'subnetUri': ' '},

    {'vlanId': '111',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'Network_111_1',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '111',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'Network_111_2',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'idList': ['111.111.111.5']},

]


Testdata_LE = [
    {'type': 'Subnet',
     'gateway': '222.222.222.1',
     'networkId': '222.222.222.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet222.com'},

    {'type': 'Range',
     'startAddress': '222.222.222.5',
                     'endAddress': '222.222.222.45',
     'name': 'RangeForSubnet222_1',
     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '222.222.222.50',
                     'endAddress': '222.222.222.65',
                     'name': 'RangeForSubnet222_2',
     'subnetUri': ' '},

    {'type': 'Subnet',
     'gateway': '223.223.223.1',
     'networkId': '223.223.223.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet223.com'},

    {'type': 'Range',
     'startAddress': '223.223.223.5',
                     'endAddress': '223.223.223.15',
                     'name': 'RangeForSubnet223_1',
                     'subnetUri': ' '},

    {'idList': ['222.222.222.5']},

    {"type": "logical-interconnect-groupV300",
     "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
     "description": None,
     "name": "LIG_2_ENCL_DCS",
     "interconnectMapTemplate":
     {"interconnectMapEntryTemplates": [
         {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
         {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 2},
         {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 20Gb Interconnect Link Module", "enclosureIndex": 1},
         {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 20Gb Interconnect Link Module", "enclosureIndex": 2}]},
     "enclosureType": "SY12000",
     "enclosureIndexes": [1, 2],
     "interconnectBaySet": "3",
     "redundancyType": "HighlyAvailable",
     "internalNetworkUris": [],
     "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
     "qosConfiguration": None,
     "uplinkSets": []
     },

    {'name': 'EG_2_ENCL_DCS',
     'type': 'EnclosureGroupV400',
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
                     'ipAddressingMode': 'IpPool',
                     'ipRangeUris': '',
                     'interconnectBayMappingCount': 0,
                     'enclosureCount': 2,
                     'configurationScript': None,
     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"}
      ]
     },

    {'name': 'EG_2_ENCL_DCS_2',
     'type': 'EnclosureGroupV400',
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
                     'ipAddressingMode': 'IpPool',
                     'ipRangeUris': '',
                     'interconnectBayMappingCount': 0,
                     'enclosureCount': 2,
                     'configurationScript': None,
                     'interconnectBayMappings':
     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"},
      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"}
      ]
     },

    {'name': 'EG_2_subnet_2_Range',
     'type': 'EnclosureGroupV400',
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
                     'ipAddressingMode': 'IpPool',
                     'ipRangeUris': '',
                     'interconnectBayMappingCount': 0,
                     'enclosureCount': 2,
                     'configurationScript': None,
                     'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"},
                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"}
                      ]
     },

    {'name': 'EG_1_Subnet_2_Range',
     'type': 'EnclosureGroupV400',
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
     'stackingMode': 'Enclosure',
                     'ipAddressingMode': 'IpPool',
                     'ipRangeUris': '',
                     'interconnectBayMappingCount': 0,
                     'enclosureCount': 2,
                     'configurationScript': None,
                     'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"},
                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:LIG_2_ENCL_DCS"}
                      ]
     },
    {'name': 'LE_2_ENCL_DCS',
     'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102'],  # REAL
     'enclosureGroupUri': 'EG:EG_2_ENCL_DCS',
     'firmwareBaselineUri': None,
     'forceInstallFirmware': False
     },

    {'vlanId': '222',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_222',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': ['Network_Edit']}

]


Testdata_Patch = [
    {'type': 'Subnet',
     'gateway': '180.180.180.1',
     'networkId': '180.180.180.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet180.com'},

    {'type': 'Range',
     'startAddress': '180.180.180.5',
     'endAddress': '180.180.180.15',
     'name': 'RangeForSubnet180_1',
     'subnetUri': ' '},

    {'vlanId': '180',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'Network_180',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': 'enc_groups_patch',
     'type': 'EnclosureGroupV400',
     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                         'stackingMode': 'Enclosure',
                         'ipAddressingMode': 'External',
                         'interconnectBayMappingCount': 0,
                         'enclosureCount': 3,
                         'configurationScript': None,
                         'interconnectBayMappings':
                         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
                          ]},

    {'operations': [
        {
            'op': 'add',
            'path': '/associatedResources/-',
            'value': {
                'resourceName': 'Network_180',
                                'resourceCategory': 'ethernet-networks',
                                'resourceUri': ''
            }
        }
    ],
        'eTag': ''
    },

    {'operations': [
        {
            'op': 'remove',
            'path': '/associatedResources/0'
        }
    ],
        'eTag': ''
    },

    {'idList': ['180.180.180.5']},

    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'WRONG',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                                    'resourceCategory': 'enclosure-groups',
                                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': ' ',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                                    'resourceCategory': 'enclosure-groups',
                                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [],
        'eTag':''
    },


    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                                    'resourceCategory': 'enclosure-groups',
                                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    }

]

Testdata_Allocate = [
    {'type': 'Subnet',
     'gateway': '200.200.200.1',
     'networkId': '200.200.200.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': ['200.200.200.2'],
     'domain': 'Subnet200.com'},

    {'type': 'Range',
     'startAddress': '200.200.200.5',
     'endAddress': '200.200.200.15',
     'name': 'RangeForSubnet200_1',
     'subnetUri': ' '},

    {'type': 'Subnet',
     'gateway': '201.201.201.1',
     'networkId': '201.201.201.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet201.com'},

    {'type': 'Range',
     'startAddress': '201.201.201.5',
                     'endAddress': '201.201.201.15',
     'name': 'Range201',
     'subnetUri': ' '},

    {'vlanId': '200',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_200',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '201',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_201',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'type': 'Range',
     'startAddress': '201.201.201.4',
                     'endAddress': '201.201.201.15',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '201.201.201.4',
                     'endAddress': '201.201.201.16',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '201.201.201.3',
                     'endAddress': '201.201.201.17',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '201.201.201.4',
                     'endAddress': '201.201.201.17',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '201.201.201.4',
                     'endAddress': '201.201.201.16',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '201.201.201.6',
                     'endAddress': '201.201.201.16',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '201.201.201.5',
                     'endAddress': '201.201.201.16',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'type': 'Subnet',
     'gateway': '',
     'networkId': '110.110.110.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet110.com'},

    {'type': 'Range',
     'startAddress': '110.110.110.1',
                     'endAddress': '110.110.110.254',
                     'name': 'Range110',
                     'subnetUri': ' '},

    {'vlanId': '110',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_110',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'type': 'Range',
     'startAddress': '201.201.201.5',
                     'endAddress': '201.201.201.25',
                     'name': 'Range201',
                     'subnetUri': ' '},

    {'vlanId': '202',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'Network_202',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}

]

Testdata_ip_allocate = [
    {'idList': ['201.201.201.5']},
    {'idList': ['201.201.201.5', '201.201.201.6', '201.201.201.7', '201.201.201.8', '201.201.201.9', '201.201.201.10', '201.201.201.11', '201.201.201.12', '201.201.201.13', '201.201.201.14', '201.201.201.15', '201.201.201.16']},
    {'idList': ['201.201.201.5', '201.201.201.6', '201.201.201.7', '201.201.201.8', '201.201.201.9', '201.201.201.10', '201.201.201.11', '201.201.201.12', '201.201.201.13', '201.201.201.14', '201.201.201.15']},
    {'count': 6},
    {'idList': ['200.200.200.5', '200.200.200.6', '200.200.200.7', '200.200.200.8', '200.200.200.9', '200.200.200.10', '200.200.200.11', '200.200.200.12', '200.200.200.13', '200.200.200.14', '200.200.200.15']},
    {'idList': ['200.200.200.1']},
    {'idList': ['200.200.200.2']},
    {'count': 254},
    {'idList': ['110.110.110.1', '110.110.110.2', '110.110.110.3', '110.110.110.4', '110.110.110.5', '110.110.110.6', '110.110.110.7', '110.110.110.8', '110.110.110.9', '110.110.110.10',
                '110.110.110.11', '110.110.110.12', '110.110.110.13', '110.110.110.14', '110.110.110.15', '110.110.110.16', '110.110.110.17', '110.110.110.18', '110.110.110.19', '110.110.110.20',
                '110.110.110.21', '110.110.110.22', '110.110.110.23', '110.110.110.24', '110.110.110.25', '110.110.110.26', '110.110.110.27', '110.110.110.28', '110.110.110.29', '110.110.110.30',
                '110.110.110.31', '110.110.110.32', '110.110.110.33', '110.110.110.34', '110.110.110.35', '110.110.110.36', '110.110.110.37', '110.110.110.38', '110.110.110.39', '110.110.110.40',
                '110.110.110.41', '110.110.110.42', '110.110.110.43', '110.110.110.44', '110.110.110.45', '110.110.110.46', '110.110.110.47', '110.110.110.48', '110.110.110.49', '110.110.110.50',
                '110.110.110.51', '110.110.110.52', '110.110.110.53', '110.110.110.54', '110.110.110.55', '110.110.110.56', '110.110.110.57', '110.110.110.58', '110.110.110.59', '110.110.110.60',
                '110.110.110.61', '110.110.110.62', '110.110.110.63', '110.110.110.64', '110.110.110.65', '110.110.110.66', '110.110.110.67', '110.110.110.68', '110.110.110.69', '110.110.110.70',
                '110.110.110.71', '110.110.110.72', '110.110.110.73', '110.110.110.74', '110.110.110.75', '110.110.110.76', '110.110.110.77', '110.110.110.78', '110.110.110.79', '110.110.110.80',
                '110.110.110.81', '110.110.110.82', '110.110.110.83', '110.110.110.84', '110.110.110.85', '110.110.110.86', '110.110.110.87', '110.110.110.88', '110.110.110.89', '110.110.110.90',
                '110.110.110.91', '110.110.110.92', '110.110.110.93', '110.110.110.94', '110.110.110.95', '110.110.110.96', '110.110.110.97', '110.110.110.98', '110.110.110.99', '110.110.110.100',
                '110.110.110.101', '110.110.110.102', '110.110.110.103', '110.110.110.104', '110.110.110.105', '110.110.110.106', '110.110.110.107', '110.110.110.108', '110.110.110.109', '110.110.110.110',
                '110.110.110.111', '110.110.110.112', '110.110.110.113', '110.110.110.114', '110.110.110.115', '110.110.110.116', '110.110.110.117', '110.110.110.118', '110.110.110.119', '110.110.110.120',
                '110.110.110.121', '110.110.110.122', '110.110.110.123', '110.110.110.124', '110.110.110.125', '110.110.110.126', '110.110.110.127', '110.110.110.128', '110.110.110.129', '110.110.110.130',
                '110.110.110.131', '110.110.110.132', '110.110.110.133', '110.110.110.134', '110.110.110.135', '110.110.110.136', '110.110.110.137', '110.110.110.138', '110.110.110.139', '110.110.110.140',
                '110.110.110.141', '110.110.110.142', '110.110.110.143', '110.110.110.144', '110.110.110.145', '110.110.110.146', '110.110.110.147', '110.110.110.148', '110.110.110.149', '110.110.110.150',
                '110.110.110.151', '110.110.110.152', '110.110.110.153', '110.110.110.154', '110.110.110.155', '110.110.110.156', '110.110.110.157', '110.110.110.158', '110.110.110.159', '110.110.110.160',
                '110.110.110.161', '110.110.110.162', '110.110.110.163', '110.110.110.164', '110.110.110.165', '110.110.110.166', '110.110.110.167', '110.110.110.168', '110.110.110.169', '110.110.110.170',
                '110.110.110.171', '110.110.110.172', '110.110.110.173', '110.110.110.174', '110.110.110.175', '110.110.110.176', '110.110.110.177', '110.110.110.178', '110.110.110.179', '110.110.110.180',
                '110.110.110.181', '110.110.110.182', '110.110.110.183', '110.110.110.184', '110.110.110.185', '110.110.110.186', '110.110.110.187', '110.110.110.188', '110.110.110.189', '110.110.110.190',
                '110.110.110.191', '110.110.110.192', '110.110.110.193', '110.110.110.194', '110.110.110.195', '110.110.110.196', '110.110.110.197', '110.110.110.198', '110.110.110.199', '110.110.110.200',
                '110.110.110.201', '110.110.110.202', '110.110.110.203', '110.110.110.204', '110.110.110.205', '110.110.110.206', '110.110.110.207', '110.110.110.208', '110.110.110.209', '110.110.110.210',
                '110.110.110.211', '110.110.110.212', '110.110.110.213', '110.110.110.214', '110.110.110.215', '110.110.110.216', '110.110.110.217', '110.110.110.218', '110.110.110.219', '110.110.110.220',
                '110.110.110.221', '110.110.110.222', '110.110.110.223', '110.110.110.224', '110.110.110.225', '110.110.110.226', '110.110.110.227', '110.110.110.228', '110.110.110.229', '110.110.110.230',
                '110.110.110.231', '110.110.110.232', '110.110.110.233', '110.110.110.234', '110.110.110.235', '110.110.110.236', '110.110.110.237', '110.110.110.238', '110.110.110.239', '110.110.110.240',
                '110.110.110.241', '110.110.110.242', '110.110.110.243', '110.110.110.244', '110.110.110.245', '110.110.110.246', '110.110.110.247', '110.110.110.248', '110.110.110.249', '110.110.110.250',
                '110.110.110.251', '110.110.110.252', '110.110.110.253', '110.110.110.254']},
    {'idList': ['110.110.110.250']},
    {'idList': ['110.110.110.11', '110.110.110.21', '110.110.110.31', '110.110.110.41', '110.110.110.51']}
]

Testdata_Collect = [
    {'type': 'Subnet',
     'gateway': '175.175.175.1',
     'networkId': '175.175.175.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': ['175.175.175.2'],
     'domain': 'Subnet175.com'},

    {'type': 'Range',
     'startAddress': '175.175.175.5',
     'endAddress': '175.175.175.15',
     'name': 'RangeForSubnet175_1',
     'subnetUri': ' '},

    {'type': 'Range',
     'startAddress': '175.175.175.25',
     'endAddress': '175.175.175.35',
     'name': 'RangeForSubnet175_2',
     'subnetUri': ' '},

    {'type': 'Subnet',
     'gateway': '176.176.176.1',
     'networkId': '176.176.176.0',
     'subnetmask': '255.255.255.0',
     'dnsServers': [],
     'domain': 'Subnet176.com'},

    {'type': 'Range',
     'startAddress': '176.176.176.5',
     'endAddress': '176.176.176.15',
     'name': 'Range176',
     'subnetUri': ' '},

    {'vlanId': '175',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_175',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '176',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_176',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '175',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'Network_175',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}
]

Testdata_ip_collect = [
    {'idList': ['176.176.176.5']},
    {'idList': ['175.175.175.15', '175.175.175.35']},
    {'idList': ['176.176.176.5', '176.176.176.6', '176.176.176.7']},
    {'idList': ['176.176.176.5', '176.176.176.6', '176.176.186.7']},
    {'idList': ['300.a. .@']},
    {'idList': ['201.201.201.5', '201.201.201.6', '201.201.201.7', '201.201.201.8', '201.201.201.9', '201.201.201.10', '201.201.201.11', '201.201.201.12', '201.201.201.13', '201.201.201.14', '201.201.201.15']},
    {'count': 6}
]

Testdata_Subnet = [{'type': 'Subnet',
                    'gateway': '20.20.20.1',
                    'networkId': '20.20.20.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '20.20.20.2',
                        '20.20.20.3',
                        '20.20.20.4'],
                    'domain': 'Subnet20.com'},

                   {'type': 'Subnet',
                    'gateway': '',
                    'networkId': '21.21.21.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [],
                    'domain': ''},

                   {'type': 'Subnet',
                    'gateway': '',
                    'networkId': '22.22.22.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '22.22.22.2',
                        '22.22.22.3',
                        '22.22.22.4'],
                    'domain': ''},

                   {'type': 'Subnet',
                    'gateway': '',
                    'networkId': '23.23.23.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '23.23.23.2',
                        '23.23.23.3',
                        '23.23.23.4'],
                    'domain': 'Subnet23.com'},

                   {'type': 'Subnet',
                    'gateway': '24.24.24.1',
                    'networkId': '24.24.24.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '24.24.24.2',
                        '24.24.24.3',
                        '24.24.24.4'],
                    'domain': ''},

                   {'type': 'Subnet',
                    'gateway': '25.25.25.1',
                    'networkId': '',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '25.25.25.2'],
                    'domain': 'Subnet25.com'},

                   {'type': 'Subnet',
                    'gateway': '25.25.25.1',
                    'networkId': '25.25.25.0',
                    'subnetmask': '',
                    'dnsServers': [
                        '25.25.25.2'],
                    'domain': 'Subnet25.com'},

                   {'type': 'Subnet',
                    'gateway': '25.25.25.1',
                    'networkId': '25.25.25.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '25.25.25.3',
                        '25.25.25.3',
                        '25.25.25.3'],
                    'domain': 'Subnet25.com'},

                   {'type': 'Subnet',
                    'gateway': '26.26.26.1',
                    'networkId': '26.26.26.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [],
                    'domain': 'Subnet26.com'},

                   {'type': 'Subnet',
                    'gateway': '26.26.26.1',
                    'networkId': '127.0.0.1',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [],
                    'domain': 'Subnet127.com'},

                   {'type': 'Subnet',
                    'gateway': '127.0.0.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [],
                    'domain': 'Gateway127.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '127.0.0.1',
                    'dnsServers': [],
                    'domain': 'SubnetMask127.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['127.0.0.1'],
                    'domain': 'DNS127.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '224.0.0.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [''],
                    'domain': 'subnetMulticast.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '224.0.0.0',
                    'dnsServers': [''],
                    'domain': 'SubnetMaskMulticast.com'},

                   {'type': 'Subnet',
                    'gateway': '224.0.0.0',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [],
                    'domain': 'Gateway224.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['224.0.0.0'],
                    'domain': 'DNS127.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': 'A.10. .#',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [''],
                    'domain': 'SubnetInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '100.200.300.400',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [''],
                    'domain': 'SubnetInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': 'A.10. .#',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [''],
                    'domain': 'GatewayInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '100.200.300.400',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [''],
                    'domain': 'GatewayInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': 'A.10. .#',
                    'dnsServers': [''],
                    'domain': 'SubnetMaskInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '100.200.300.400',
                    'dnsServers': [''],
                    'domain': 'SubnetMaskInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['A.10. .#'],
                    'domain': 'DNSInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['100.200.300.400'],
                    'domain': 'DNSInvalid.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['27.27.27.2'],
                    'domain': 'ABCD.2'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['27.27.27.2'],
                    'domain': 'ABCD.C'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['27.27.27.2'],
                    'domain': 'A ~`!@#$%^&*()_+{}|[]\-=:;<>?/,.com'},

                   {'type': 'Subnet',
                    'gateway': '27.27.27.1',
                    'networkId': '27.27.27.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['27.27.27.2'],
                    'domain': 'Domain-name.com'},

                   {'type': 'Subnet',
                    'gateway': '28.28.28.1',
                    'networkId': '28.28.28.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['28.28.28.2'],
                    'domain': 'abc.co.com.comc.comco.comcom'},

                   {'type': 'Subnet',
                    'gateway': '28.28.28.1',
                    'networkId': '28.28.28.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['28.28.28.2'],
                    'domain': 'abc.comcomm'},

                   {'type': 'Subnet',
                    'gateway': '29.29.29.1',
                    'networkId': '29.29.29.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['29.29.29.2'],
                    'domain': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefgh.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabc.abc.com'},

                   {'type': 'Subnet',
                    'gateway': '30.30.30.1',
                    'networkId': '30.30.30.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['30.30.30.2'],
                    'domain': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghij.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd.abc.com'},

                   {'type': 'Subnet',
                    'gateway': '30.30.30.1',
                    'networkId': '30.30.30.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['30.30.30.2'],
                    'domain': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk.com'},

                   {'type': 'Subnet',
                    'gateway': '30.30.30.1',
                    'networkId': '30.30.30.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['30.30.30.2'],
                    'domain': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl.com'},

                   {'type': 'Subnet',
                    'gateway': '31.31.31.1',
                    'networkId': '31.31.31.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': ['31.31.31.2'],
                    'domain': '-Domain-name.com'},

                   {'type': 'Subnet',
                    'gateway': '',
                    'networkId': '31.31.31.0',
                    'subnetmask': '255.255.255.0',
                    'dnsServers': [
                        '31.31.31.2',
                        '31.31.31.3',
                        '31.31.31.4'],
                    'domain': ''}
                   ]

Testdata_Subnet_Edit = [{'type': 'Subnet',
                         'gateway': '22.22.22.1',
                         'networkId': '22.22.22.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '22.22.22.2',
                                 '22.22.22.3',
                                 '22.22.22.4'],
                         'domain': 'Subnet22-Edit.com'},

                        {'type': 'Subnet',
                         'gateway': '',
                         'networkId': '21.21.21.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '21.21.21.2',
                                 '21.21.21.3',
                                 '21.21.21.4'],
                         'domain': 'Subnet21-Edit.com'},

                        {'type': 'Subnet',
                         'gateway': '24.24.24.1',
                         'networkId': '24.24.24.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '24.24.24.2',
                                 '24.24.24.3',
                                 '24.24.24.4'],
                         'domain': 'Subnet24-Edit.com'},

                        {'type': 'Subnet',
                         'gateway': '31.31.31.1',
                         'networkId': '31.31.31.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '31.31.31.2',
                                 '31.31.31.3',
                                 '31.31.31.4'],
                         'domain': ''},

                        {'type': 'Subnet',
                         'gateway': '23.23.23.1',
                         'networkId': '23.23.23.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '23.23.23.2',
                                 '23.23.23.3',
                                 '23.23.23.4'],
                         'domain': 'Subnet23.com'},

                        {'type': 'Subnet',
                         'gateway': '',
                         'networkId': '20.20.20.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '20.20.20.2',
                                 '20.20.20.3',
                                 '20.20.20.4'],
                         'domain': ''},

                        {'type': 'Subnet',
                         'gateway': '22.22.22.1',
                         'networkId': '22.22.22.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '22.22.22.2',
                                 '22.22.22.3',
                                 '22.22.22.4'],
                         'domain': ''},

                        {'type': 'Subnet',
                         'gateway': '',
                         'networkId': '21.21.21.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '21.21.21.2',
                                 '21.21.21.3',
                                 '21.21.21.4'],
                         'domain': ''},

                        {'type': 'Subnet',
                         'gateway': '',
                         'networkId': '23.23.23.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '23.23.23.2',
                                 '23.23.23.3',
                                 '23.23.23.4'],
                         'domain': 'Subnet23.com'},

                        {'type': 'Subnet',
                         'gateway': '',
                         'networkId': '22.22.22.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '22.22.22.2',
                                 '22.22.22.3',
                                 '22.22.22.4'],
                         'domain': ''},

                        {'type': 'Subnet',
                         'gateway': '24.24.24.5',
                         'networkId': '24.24.24.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '24.24.24.2',
                                 '24.24.24.3',
                                 '24.24.24.4'],
                         'domain': 'Subnet24-Edit.com'},

                        {'type': 'Subnet',
                         'gateway': '24.24.24.5',
                         'networkId': '24.24.24.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '24.24.24.2',
                                 '24.24.24.3',
                                 '24.24.24.4'],
                         'domain': 'Subnet24-EditDomainData.com'},

                        {'type': 'Subnet',
                         'gateway': '31.31.31.5',
                         'networkId': '31.31.31.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '31.31.31.2',
                                 '31.31.31.3',
                                 '31.31.31.4'],
                         'domain': ''},

                        {'type': 'Subnet',
                         'gateway': '',
                         'networkId': '23.23.23.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '23.23.23.2',
                                 '23.23.23.3',
                                 '23.23.23.4'],
                         'domain': 'Subnet23-EditDomain.com'},

                        {'type': 'Subnet',
                         'gateway': '24.24.24.A',
                         'networkId': '24.24.24.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '24.24.24.2',
                                 '24.24.24.3',
                                 '24.24.24.4'],
                         'domain': 'Subnet24-EditDomainData.com'},

                        {'type': 'Subnet',
                         'gateway': '24.24.24.5',
                         'networkId': '24.24.24.0',
                         'subnetmask': '255.255.255.0',
                         'dnsServers': [
                                 '24.24.24.2',
                                 '24.24.24.3',
                                 '24.24.24.4'],
                         'domain': '-Subnet24-EditDomainData.com'}

                        ]

Testdata_SubnetEdit_For_Range = [{'type': 'Subnet',
                                  'gateway': '20.20.20.1',
                                  'networkId': '20.20.20.0',
                                  'subnetmask': '255.255.255.0',
                                  'dnsServers': [
                                      '20.20.20.2',
                                      '20.20.20.3',
                                      '20.20.20.4'],
                                  'domain': ''},

                                 {'type': 'Subnet',
                                  'gateway': '',
                                  'networkId': '20.20.20.0',
                                  'subnetmask': '255.255.255.0',
                                  'dnsServers': [
                                      '20.20.20.2',
                                      '20.20.20.3',
                                      '20.20.20.4'],
                                  'domain': ''},

                                 {'type': 'Subnet',
                                  'gateway': '20.20.20.1',
                                  'networkId': '20.20.20.0',
                                  'subnetmask': '255.255.255.0',
                                  'dnsServers': [
                                      '20.20.20.2',
                                      '20.20.20.3',
                                      '20.20.20.4'],
                                  'domain': 'Subnet20.com'},

                                 {'type': 'Subnet',
                                  'gateway': '',
                                  'networkId': '192.168.1.192',
                                  'subnetmask': '255.255.255.224',
                                  'dnsServers': [],
                                  'domain': 'Subnet192.com'},

                                 {'type': 'Subnet',
                                  'gateway': '192.168.1.197',
                                  'networkId': '192.168.1.192',
                                  'subnetmask': '255.255.255.224',
                                  'dnsServers': [
                                      '192.168.1.195',
                                      '192.168.1.196',
                                      '192.168.1.198'],
                                  'domain': 'Subnet192.com'}


                                 ]


Testdata_Range = [{'type': 'Range',
                   'startAddress': '20.20.20.5',
                   'endAddress': '20.20.20.100',
                   'name': 'RangeForSubnet20_1',
                   'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.5',
                      'endAddress': '21.21.21.100',
                      'name': 'RangeForSubnet21_1',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.5',
                      'endAddress': '24.24.24.100',
                      'name': 'RangeForSubnet24_1',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '23.23.23.5',
                      'endAddress': '23.23.23.100',
                      'name': 'RangeForSubnet23_1',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.5',
                      'endAddress': '21.21.21.100',
                      'name': 'Subnet21_1_Duplicate',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.10',
                      'endAddress': '21.21.21.90',
                      'name': 'RangeForSubnet21_1_Edited',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.100',
                      'endAddress': '21.21.21.110',
                      'name': 'RangeForSubnet21_1_Edited',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '127.0.0.1',
                      'endAddress': '21.21.21.120',
                      'name': 'Range_Start__Loopback',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.120',
                      'endAddress': '127.0.0.1',
                      'name': 'Range_End__Loopback',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '224.0.0.0',
                      'endAddress': '21.21.21.120',
                      'name': 'Range_Start_Multicast',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.120',
                      'endAddress': '224.0.0.0',
                      'name': 'Range_End__Multicast',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '21.21.21.10',
                      'endAddress': '21.21.21.90',
                      'name': 'Range_Dup_IP',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.101',
                      'endAddress': '24.24.24.110',
                      'name': 'RangeForSubnet24_2',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.5',
                      'endAddress': '24.24.24.110',
                      'name': 'RangeForSubnet24_3',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '22.22.22.5',
                      'endAddress': '22.22.22.100',
                      'name': 'Subnet_out_scope',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.100',
                      'endAddress': '24.24.24.120',
                      'name': 'RangeForSubnet24_4',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.120',
                      'endAddress': '24.24.24.130',
                      'name': 'RangeForSubnet24_5',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '',
                      'endAddress': '',
                      'name': 'RangeForSubnet24_6',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.*.w.500',
                      'endAddress': '24.24.424.1A',
                      'name': 'RangeForSubnet24_7',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.0',
                      'endAddress': '24.24.24.120',
                      'name': 'RangeForSubnet24_8',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.120',
                      'endAddress': '24.24.24.119',
                      'name': 'RangeForSubnet24_9',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.120',
                      'endAddress': '24.24.24.121',
                      'name': 'RangeName33CharactersRangeName33Cha',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.120',
                      'endAddress': '24.24.24.121',
                      'name': 'RangeName32CharactersRangeName32',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '24.24.24.190',
                      'endAddress': '24.24.24.190',
                      'name': 'RangeSameIP',
                      'subnetUri': ' '},

                  {'type': 'Range',
                      'startAddress': '192.168.1.193',
                      'endAddress': '192.168.1.194',
                      'name': 'Range192',
                      'subnetUri': ' '}

                  ]

Testdata_NetworkSet = [
    {'name': 'NetSet_01', 'type': 'network-setV300', 'networkUris': ['Network_100_0', 'Network_For_NetworkSet_14'], 'nativeNetworkUri': None},
    {'name': 'NetSet_02', 'type': 'network-setV300', 'networkUris': ['Network_100_0', 'Network_103_3'], 'nativeNetworkUri': None},
    {'name': 'NetSet_03', 'type': 'network-setV300', 'networkUris': ['Network_For_NetworkSet_14'], 'nativeNetworkUri': None}
]


subnet = [{'type': 'Subnet',
           'gateway': '10.10.10.1',
           'networkId': '10.10.10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'testsub.com'},

          {'type': 'Subnet',
           'gateway': '20.20.20.1',
           'networkId': '20.20.20.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test20.com'},

          {'type': 'Subnet',
           'gateway': '30.30.30.1',
           'networkId': '30.30.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test30.com'},

          {'type': 'Subnet',
           'gateway': '40.40.40.1',
           'networkId': '40.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test40.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '50.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test540.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test543.com'},

          {'type': 'Subnet',
           'gateway': ' ',
           'networkId': '80.80.80.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'NoGateway.com'},

          {'type': 'Subnet',
           'gateway': '90.90.90.1 ',
           'networkId': '90.90.90.0',
           'subnetmask': ' ',
           'dnsServers': [],
           'domain': 'NoSubnet.com'},

          {'type': 'Subnet',
           'gateway': '91.91.91.1',
           'networkId': '91.91.91.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': ''},

          {'type': 'Subnet',
           'gateway': '80.80.80.0',
           'networkId': '127.0.0.1',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Loopback.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '258.890.1.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': 'a.b.c',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '1234.10.10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.40.1',
           'networkId': '10. .10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'InvalidNetwork.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'test543.com.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.255',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'test543.com.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.1',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'testsubEdit.com'},

          {'type': 'Subnet',
           'gateway': '50.40.30.2',
           'networkId': '50.40.30.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.40.2',
               '50.40.40.3',
               '50.40.40.4'],
           'domain': 'testsubEdit.com'},

          {'type': 'Subnet',
           'gateway': '10.10.10.2',
           'networkId': '10.10.10.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['10.10.10.254'],
           'domain': 'EditSubnetWithRange.com'},

          {'type': 'Subnet',
           'gateway': '224.0.0.2',
           'networkId': '224.0.0.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Multicast.com'},

          {'type': 'Subnet',
           'gateway': '1.1.1.1',
           'networkId': '1.1.1.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubnetMaskAllCheck.com'},

          {'type': 'Subnet',
           'gateway': '15.15.15.1',
           'networkId': '15.15.15.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet15.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.1',
           'networkId': '16.16.16.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet1516.com'},

          {'type': 'Subnet',
           'gateway': '127.0.0.1',
           'networkId': '17.17.17.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'GatewayLoopback.com'},

          {'type': 'Subnet',
           'gateway': '19.19.19.1',
           'networkId': '19.19.19.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['19.19.19.2'],
           'domain': 'OneDNS.com'},

          {'type': 'Subnet',
           'gateway': '18.18.18.1',
           'networkId': '18.18.18.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['127.0.0.1'],
           'domain': 'DNSLoopBack.com'},

          {'type': 'Subnet',
           'gateway': '21.21.21.1',
           'networkId': '21.21.21.0',
           'subnetmask': '127.0.0.1',
           'dnsServers': [],
           'domain': 'DNSLoopBack.com'},

          {'type': 'Subnet',
           'gateway': '224.0.0.0',
           'networkId': '24.24.24.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'GatewayMulticast.com'},

          {'type': 'Subnet',
           'gateway': '24.24.24.1',
           'networkId': '24.24.24.0',
           'subnetmask': '224.0.0.0',
           'dnsServers': [],
           'domain': 'SubnetmaskMulticast.com'},

          {'type': 'Subnet',
           'gateway': '24.24.24.1',
           'networkId': '24.24.24.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['224.0.0.0'],
           'domain': 'DNSMulticast.com'},

          {'type': 'Subnet',
           'gateway': '100.100.100.1',
           'networkId': '100.100.100.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['100.100.100.2'],
           'domain': 'AssociateTestCase.com'},

          {'type': 'Subnet',
           'gateway': '200.200.200.1',
           'networkId': '200.200.200.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['200.200.200.2'],
           'domain': 'SubnetAllocateTestCase.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.1',
           'networkId': '16.16.16.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet16.com'},

          {'type': 'Subnet',
           'gateway': '210.210.210.1',
           'networkId': '210.210.210.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['210.210.210.2'],
           'domain': 'Subnet210.com'},

          {'type': 'Subnet',
           'gateway': '125.125.125.1',
           'networkId': '125.125.125.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['125.125.125.2'],
           'domain': 'Subnet125.com'},

          {'type': 'Subnet',
           'gateway': '126.126.126.1',
           'networkId': '126.126.126.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['126.126.126.2'],
           'domain': 'Subnet126.com'},

          {'type': 'Subnet',
           'gateway': '5.5.5.1',
           'networkId': '5.5.5.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['5.5.5.2'],
           'domain': 'SubnetDiffUsers.com'},

          {'type': 'Subnet',
           'gateway': '40.40.40.3',
           'networkId': '40.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['40.40.40.4'],
           'domain': 'SubnetServerUsersEdit.com'},

          {'type': 'Subnet',
           'gateway': '40.40.40.7',
           'networkId': '40.40.40.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': ['40.40.40.8'],
           'domain': 'SubnetNetworkUsersEdit.com'},

          {'type': 'Subnet',
           'gateway': '50.40.50.1',
           'networkId': '50.40.50.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [
               '50.40.50.2',
               '50.40.50.3',
               '50.40.50.4'],
           'domain': 'TestEditSubAssociated.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.1',
           'networkId': '16.16.16.16.0',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'SubnetMismatch.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.65',
           'networkId': '16.16.16.64',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'SubnetMismatch.com'},

          {'type': 'Subnet',
           'gateway': '16.16.16.193',
           'networkId': '16.16.16.192',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'SubnetMismatch.com'},

          {'type': 'Subnet',
           'gateway': '50.40.41.1',
           'networkId': '50.40.41.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'test5041.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.193',
           'networkId': '192.168.1.192',
           'subnetmask': '255.255.255.224',
           'dnsServers': [],
           'domain': 'vlsm1.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.1',
           'networkId': '192.168.1.0',
           'subnetmask': '255.255.255.128',
           'dnsServers': [],
           'domain': 'vlsm2.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.129',
           'networkId': '192.168.1.128',
           'subnetmask': '255.255.255.192',
           'dnsServers': [],
           'domain': 'vlsm3.com'},

          {'type': 'Subnet',
           'gateway': '192.168.1.225',
           'networkId': '192.168.1.224',
           'subnetmask': '255.255.255.252',
           'dnsServers': [],
           'domain': 'vlsm4.com'},

          {'type': 'Subnet',
           'gateway': '150.150.150.1',
           'networkId': '150.150.150.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet150.com'},

          {'type': 'Subnet',
           'gateway': '60.60.60.1',
           'networkId': '60.60.60.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubAllocateLE.com'},

          {'type': 'Subnet',
           'gateway': '61.61.61.1',
           'networkId': '61.61.61.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubAllocateLE2.com'},

          {'type': 'Subnet',
           'gateway': '130.130.130.1',
           'networkId': '130.130.130.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Subnet130.com'},

          {'type': 'Subnet',
           'gateway': '131.131.131.1',
           'networkId': '131.131.131.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain':'`~!@#$%^&*()_+={}|[]\:";<>?,/'},

          {'type': 'Subnet',
           'gateway': '132.132.132.1',
           'networkId': '132.132.132.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'Check-name.com'},

          {'type': 'Subnet',
           'gateway': '175.175.175.1',
           'networkId': '175.175.175.0',
           'subnetmask': '255.255.255.0',
           'dnsServers': [],
           'domain': 'SubnetPatch.com'}

          ]

edit_subnet = [{'type': 'Subnet',
                'gateway': '50.40.30.1',
                'networkId': '50.40.30.0',
                'subnetmask': '255.255.255.0',
                'dnsServers': [
                    '50.40.40.2',
                        '50.40.40.3',
                        '50.40.40.4'],
                'domain': 'testsubEdit.com'},

               {'type': 'Subnet',
                'gateway': '20.20.20.1',
                'networkId': '20.20.20.0',
                'subnetmask': '255.255.255.0',
                'dnsServers': [],
                'domain': 'test20.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.128',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.224',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.240',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.248',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.252',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'},

               {'type': 'Subnet',
                'gateway': '1.1.1.1',
                'networkId': '1.1.1.0',
                'subnetmask': '255.255.255.192',
                'dnsServers': [],
                'domain': 'SubnetMaskAllCheck.com'}
               ]

range_enable = [{'type': 'Range',
                 'enabled': 'true'}
                ]
range_disable = [{'type': 'Range',
                  'enabled': 'false'}
                 ]

ipv4ranges = [{'type': 'Range',
               'startAddress': '10.10.11.2',
               'endAddress': '10.10.11.100',
               'name': 'test',
               'subnetUri': ' '},

              {'type': 'Range',
               'startAddress': '10.10.10.3',
               'endAddress': '10.10.10.252',
               'name': 'test1',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '10.10.11.101',
               'endAddress': '10.10.11.200',
               'name': 'test2',
               'subnetUri': ' '},

              {'type': 'Range',
               'endAddress': '30.30.30.200',
               'startAddress': '30.30.30.2',
               'name': 'test13',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.2',
               'startAddress': '30.30.30.254',
               'name': 'OverLapRange',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.5',
               'name': 'SameSubnetIdStartAddress',
               'startAddress': '30.30.30.0',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '300.3O..5',
               'name': 'InvalidEndAddress',
               'startAddress': '30.30.30.0',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '127.0.0.1',
               'name': 'LoopbackEndAddress',
               'startAddress': '30.30.30.0',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.2',
               'name': 'LoopbackStartAddress',
               'startAddress': '127.0.0.1',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': ' ',
               'name': 'EmptyAddress',
               'startAddress': ' ',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.2',
               'endAddress': '15.15.15.100',
               'name': 'test151',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.101',
               'endAddress': '15.15.15.200',
               'name': 'test152',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.201',
               'endAddress': '15.15.15.254',
               'name': 'test153',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.250',
               'startAddress': '30.30.30.2',
               'name': 'test1330',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.250',
               'startAddress': '30.30.30.2',
               'name': 'test1330',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '100.100.100.100',
               'startAddress': '100.100.100.5',
               'name': 'Range100AssiciateTestCase',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '200.200.200.100',
               'startAddress': '200.200.200.5',
               'name': 'RangeAllocateTestCase',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '15.15.15.201',
               'endAddress': '15.15.15.220',
               'name': 'test15R3',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '16.16.16.201',
               'endAddress': '16.16.16.220',
               'name': 'Range16',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '20.20.20.20',
               'endAddress': '20.20.20.30',
               'name': 'RangeSub20',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '210.210.210.10',
               'endAddress': '210.210.210.20',
               'name': 'RangeSub210',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '125.125.125.10',
               'endAddress': '125.125.125.20',
               'name': 'Range125A',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '40.40.40.40',
               'endAddress': '40.40.40.50',
               'name': 'Range40Users',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.30.30',
               'endAddress': '50.40.30.40',
               'name': 'Range1Sub504030',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.30.50',
               'endAddress': '50.40.30.60',
               'name': 'Range2Sub504030',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.40.10',
               'endAddress': '50.40.40.20',
               'name': 'Range1Sub504040',
               'subnetUri': ''},

              {'type': 'Range',
               'startAddress': '50.40.41.10',
               'endAddress': '50.40.41.20',
               'name': 'Range1Sub504041',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.250',
               'startAddress': '30.30.30.2',
               'name': 'test13Duplicate',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.222',
               'startAddress': '192.168.1.194',
               'name': 'RangeVlsm1',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.3',
               'startAddress': '192.168.1.2',
               'name': 'RangeVlsm2',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.190',
               'startAddress': '192.168.1.130',
               'name': 'RangeVlsm3',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '192.168.1.226',
               'startAddress': '192.168.1.226',
               'name': 'RangeVlsm4',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.252',
               'startAddress': '30.30.30.252',
               'name': 'RangeSameFirstEndIp',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '30.30.30.252',
               'startAddress': '30.30.30.250',
               'name': 'RangeReAssignIpAfterDelete',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '150.150.150.50',
               'startAddress': '150.150.150.40',
               'name': 'Range150Allocate',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '60.60.60.60',
               'startAddress': '60.60.60.10',
               'name': 'RangeAllocateLE',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '61.61.61.60',
               'startAddress': '61.61.61.10',
               'name': 'RangeAllocateLE2',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '130.130.130.10',
               'startAddress': '130.130.130.4',
               'name': '33character33character33character',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '130.130.130.10',
               'startAddress': '130.130.130.4',
               'name': '32character32character32characte',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '130.130.130.40',
               'startAddress': '224.130.130.30',
               'name': 'RangeFirstMulticast',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '224.130.130.50',
               'startAddress': '130.130.130.20',
               'name': 'RangeLastMulticast',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '1.1.1.20',
               'startAddress': '1.1.1.10',
               'name': 'Range1',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '1.1.1.30',
               'startAddress': '1.1.1.25',
               'name': 'Range2',
               'subnetUri': ''},

              {'type': 'Range',
               'endAddress': '175.175.175.20',
               'startAddress': '175.175.175.10',
               'name': 'RangePatch',
               'subnetUri': ''}

              ]

ipv4ranges_edit = [

    {'type': 'Range',
     'endAddress': '30.30.30.254',
     'startAddress': '30.30.30.251',
     'name': 'test13',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.50',
     'startAddress': '150.150.150.39',
     'name': 'Range150ExpandFirstIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.39',
     'name': 'Range150ExpandLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.52',
     'startAddress': '150.150.150.38',
     'name': 'Range150ExpandFirstLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.52',
     'startAddress': '150.150.150.39',
     'name': 'Range150ShrinkFirstIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.39',
     'name': 'Range150ShrinkLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.50',
     'startAddress': '150.150.150.40',
     'name': 'Range150ShrinkFirstLastIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.41',
     'name': 'Range150ShrinkExpandIp',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.50',
     'startAddress': '150.150.150.40',
     'name': 'Range150Allocate',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.40',
     'name': 'Range150ExpandLastIpAllocated',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.51',
     'startAddress': '150.150.150.41',
     'name': 'Range150ShrinkFirstIpAllocated',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '150.150.150.56',
     'startAddress': '150.150.150.40',
     'name': 'Range150DisExpLastIpAllocat',
     'subnetUri': ''},

    {'type': 'Range',
     'endAddress': '1.1.1.30',
     'startAddress': '1.1.1.10',
     'name': 'Range1',
     'subnetUri': ''}

]

Network_Subnet_Empty = None

Testdata_Subnet_For_Network = [{'type': 'Subnet',
                                'gateway': '100.100.100.1',
                                'networkId': '100.100.100.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Network-0.com'},

                               {'type': 'Subnet',
                                'gateway': '101.101.101.1',
                                'networkId': '101.101.101.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Network-1.com'},

                               {'type': 'Subnet',
                                'gateway': '102.102.102.1',
                                'networkId': '102.102.102.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Network-2.com'},

                               {'type': 'Subnet',
                                'gateway': '103.103.103.1',
                                'networkId': '103.103.103.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Network-3.com'},

                               {'type': 'Subnet',
                                'gateway': '104.104.104.1',
                                'networkId': '104.104.104.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Network-4.com'},

                               {'type': 'Subnet',
                                'gateway': '101.101.101.2',
                                'networkId': '101.101.101.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Network-Edit-1.com'},

                               {'type': 'Subnet',
                                'gateway': '150.150.150.2',
                                'networkId': '150.150.150.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Users-6.com'},

                               {'type': 'Subnet',
                                'gateway': '104.104.104.4',
                                'networkId': '104.104.104.0',
                                'subnetmask': '255.255.255.0',
                                'dnsServers': [],
                                'domain': 'Subnet-Users-Edit-7.com'}
                               ]

Testdata_Vlsm = [{'type': 'Subnet',
                  'gateway': '192.168.1.193',
                  'networkId': '192.168.1.192',
                  'subnetmask': '255.255.255.224',
                  'dnsServers': [],
                  'domain': 'vlsm1.com'},

                 {'type': 'Subnet',
                     'gateway': '192.168.1.1',
                     'networkId': '192.168.1.0',
                     'subnetmask': '255.255.255.128',
                     'dnsServers': [],
                     'domain': 'vlsm2.com'},

                 {'type': 'Subnet',
                     'gateway': '192.168.1.129',
                     'networkId': '192.168.1.128',
                     'subnetmask': '255.255.255.192',
                     'dnsServers': [],
                     'domain': 'vlsm3.com'},

                 {'type': 'Subnet',
                     'gateway': '192.168.1.225',
                     'networkId': '192.168.1.224',
                     'subnetmask': '255.255.255.252',
                     'dnsServers': [],
                     'domain': 'vlsm4.com'},

                 {'type': 'Range',
                     'endAddress': '192.168.1.222',
                     'startAddress': '192.168.1.194',
                     'name': 'RangeVlsm1',
                     'subnetUri': ''},

                 {'type': 'Range',
                     'endAddress': '192.168.1.3',
                     'startAddress': '192.168.1.2',
                     'name': 'RangeVlsm2',
                     'subnetUri': ''},

                 {'type': 'Range',
                     'endAddress': '192.168.1.190',
                     'startAddress': '192.168.1.130',
                     'name': 'RangeVlsm3',
                     'subnetUri': ''},

                 {'type': 'Range',
                     'endAddress': '192.168.1.226',
                     'startAddress': '192.168.1.226',
                     'name': 'RangeVlsm4',
                     'subnetUri': ''}
                 ]

Testdata_Range_For_Network = [{'type': 'Range',
                               'startAddress': '104.104.104.5',
                               'endAddress': '104.104.104.100',
                               'name': 'RangeForSubnet104_0',
                               'subnetUri': ' '},

                              {'type': 'Range',
                                  'startAddress': '103.103.103.5',
                               'endAddress': '103.103.103.100',
                               'name': 'RangeForSubnet103_1',
                               'subnetUri': ' '},

                              {'type': 'Range',
                                  'startAddress': '101.101.101.5',
                                  'endAddress': '101.101.101.100',
                               'name': 'RangeForSubnet101_2',
                               'subnetUri': ' '},

                              {'type': 'Range',
                                  'startAddress': '150.150.150.5',
                                  'endAddress': '150.150.150.100',
                                  'name': 'Range_Network_User_3',
                               'subnetUri': ' '}

                              ]

Testdata_Network = [
    {'vlanId': '100',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_100_0',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '101',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_101_1',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '102',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_101_2',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '103',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_103_3',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '100',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkNameEdited_100_4',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '105',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': '',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '106',
     'ethernetNetworkType': 'Untagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkUntagged',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '107',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_No_Uri',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '108',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_Already_Subnet',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '109',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_Disable_Range',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': 'Network_Fabric_Attach',
     'connectionTemplateUri': None,
     'linkStabilityTime': '30',
     'autoLoginRedistribution': True,
     'fabricType': 'FabricAttach',
     'managedSanUri': None,
     'type': 'fc-networkV300'
     },

    {'name': 'Network_FCOE',
     'vlanId': '11',
     'connectionTemplateUri': None,
     'managedSanUri': None,
     'type': 'fcoe-networkV300'
     },

    {'ethernetNetworkType': 'Tunnel',
     'subnetUri': None,
     'purpose': 'General',
     'name': 'Network_Tunnel',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'
     },

    {'vlanId': '104',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_For_Users',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '114',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'Network_For_NetworkSet_14',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '100',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_100_0',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '103',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'Network_103_3',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}



]


Ethernet_network_1 = [
    {'name': 'eth-100',
     'type': 'ethernet-networkV300',
     'vlanId': 100,
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},

    {'vlanId': '17',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NET30',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '10',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NET10',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '100',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NET100',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '200',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetAssociateSub200',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': 'Network16A',
     'type': 'ethernet-networkV300',
     'vlanId': '102',
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'BlankSubnetUri',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'NoSubnetSelection',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '15',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK15',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '40',
     'ethernetNetworkType': 'Tagged',
     'purpose': 'General',
     'name': 'NETWORK40',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '16',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK16',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '20',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK20',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NoUri',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '2',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': '',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '210',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK210',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '125',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK125',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '126',
     'ethernetNetworkType': 'Untagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK126Untagged',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '40',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub40',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '30',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub504030',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '40',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub504040',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '41',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NetworkSub504041',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'vlanId': '150',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK150',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'},

    {'name': 'NetworkPatch',
     'type': 'ethernet-networkV300',
     'vlanId': '75',
     'purpose': 'General',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'ethernetNetworkType': 'Tagged'}

]

edit_network = [
    {'vlanId': '125',
     'ethernetNetworkType': 'Tagged',
     'subnetUri': '',
     'purpose': 'General',
     'name': 'NETWORK125',
     'smartLink': True,
     'privateNetwork': False,
     'connectionTemplateUri': None,
     'type': 'ethernet-networkV300'}

]

bulk_networks_dict = {
    'vlanIdRange': '5,6,7,8',
    'namePrefix': 'bulk',
    'privateNetwork': False,
    'smartLink': True,
    'purpose': 'General',
    'type': 'bulk-ethernet-network',
    'bandwidth': {
        'maximumBandwidth': 20000,
        'typicalBandwidth': 2500}
}
network_sets = [
    {'name': 'NetSet100', 'type': 'network-setV300', 'networkUris': ['NET100'], 'nativeNetworkUri': None},
    {'name': 'NetSetHappy', 'type': 'network-setV300', 'networkUris': ['nethappy'], 'nativeNetworkUri': None},
    {'name': 'NetSet15', 'type': 'network-setV300', 'networkUris': ['NETWORK15'], 'nativeNetworkUri': None},
    {'name': 'NetSet4015', 'type': 'network-setV300', 'networkUris': ['NETWORK15', 'NETWORK40'], 'nativeNetworkUri': None},
    {'name': 'NetSet16', 'type': 'network-setV300', 'networkUris': ['NETWORK16'], 'nativeNetworkUri': None},
    {'name': 'NetSet16A', 'type': 'network-setV300', 'networkUris': [], 'nativeNetworkUri': None}
]

network_sets_working = [
    {'name': 'NetSet100', 'type': 'network-setV300', 'networkUris': ['NET100'], 'nativeNetworkUri': None},
    {'name': 'NetSetHappy', 'type': 'network-setV300', 'networkUris': ['nethappy'], 'nativeNetworkUri': None}
]
Ethernet_Network_Set = [{
                        'name': 'NetSet100',
                        'networkUris': ['/rest/ethernet-networks/43f49f6f-f31d-4ca1-b240-9ea0e0a25c3f'],
                        'connectionTemplateUri':None,
                        'type':'network-setV300',
                        'nativeNetworkUri':None},

                        {
                        'name': 'NetSet200',
                        'networkUris': '',
                        'connectionTemplateUri': None,
                        'type': 'network-setV300',
                        'nativeNetworkUri': None}
                        ]
subnet_allocate = [
    {'idList': ['200.200.200.11']},
    {'idList': ['20.20.20.20']},
    {'idList': ['210.210.210.10']},
    {'idList': ['210.210.210.200']},
    {'idList': ['210.210.210.10', '210.210.210.11']},
    {'idList': ['210.210.210.255']},
    {'idList': ['210.210.210.2']},
    {'idList': ['210.210.210.1']},
    {'idList': ['210.210.210.10', '210.210.210.12', '210.210.210.15', '210.210.210.19']},
    {'idList': ['50.40.30.30']},
    {'idList': ['50.40.40.15']},
    {'idList': ['50.40.41.15']},
    {'idList': ['50.40.40.16', '50.40.40.17', '50.40.40.19']},
    {'idList': ['50.40.40.12', '50.40.40.16', '50.40.40.17', '50.41.41.18', '50.40.40.19']},
    {'idList': ['550.A.30.30']},
    {'idList': ['50.40.40.10', '50.40.40.11', '50.40.40.12', '50.40.40.13', '50.40.40.14', '50.40.40.15', '50.40.40.16', '50.40.40.17', '50.40.40.18', '50.40.40.19', '50.40.40.20']},
    {'idList': ['50.40.41.10', '50.40.41.11', '50.40.41.12', '50.40.41.13', '50.40.41.14', '50.40.41.15', '50.40.41.16', '50.40.41.17', '50.40.41.18', '50.40.41.19', '50.40.41.20']},
    {'idList': ['150.150.150.40', '150.150.150.41', '150.150.150.42', '150.150.150.43', '150.150.150.44', '150.150.150.45']}
]

subnet_collect = [
    {'idList': ['200.200.200.11']},
    {'idList': ['20.20.20.20']},
    {'idList': ['210.210.210.10']},
    {'idList': ['210.210.210.10', '210.210.210.11', '210.210.210.12', '210.210.210.13', '210.210.210.14', '210.210.210.15', '210.210.210.16', '210.210.210.17', '210.210.210.18', '210.210.210.19', '210.210.210.20']}
]

subnet_allocate_count = [
    {'count': 6},
    {'count': 15},
    {'count': 1},
    {'idList': ['20.20.20.20']},
    {'idList': ['210.210.210.10']}

]

lig_tbird_2enc = {"type": "logical-interconnect-groupV300",
                  "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                  "description": None,
                  "name": "lig_tbird21",
                  "interconnectMapTemplate":
                  {"interconnectMapEntryTemplates": [
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 2},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 20Gb Interconnect Link Module", "enclosureIndex": 1},
                      {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 20Gb Interconnect Link Module", "enclosureIndex": 2}]},
                  "enclosureType": "SY12000",
                  "enclosureIndexes": [1, 2],
                  "interconnectBaySet": "3",
                  "redundancyType": "HighlyAvailable",
                  "internalNetworkUris": [],
                  "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                  "qosConfiguration": None,
                  "uplinkSets": []
                  }

lig_tbird_1enc_dcs = {"type": "logical-interconnect-groupV300",
                      "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                      "description": None,
                      "name": "lig_1_Encl_dcs",
                      "interconnectMapTemplate":
                      {"interconnectMapEntryTemplates": [
                          {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                          {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
                      "enclosureType": "SY12000",
                      "enclosureIndexes": [1],
                      "interconnectBaySet": "3",
                      "redundancyType": "Redundant",
                      "internalNetworkUris": [],
                      "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                      "qosConfiguration": None,
                      "uplinkSets": []
                      }


lig_demo_3enc = {"type": "logical-interconnect-groupV300",
                 "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                 "description": None,
                 "name": "lig_demo_pools",
                 "interconnectMapTemplate":
                 {"interconnectMapEntryTemplates": [
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 2},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 1},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 2}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 2},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 3}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 3},
                     {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 3}]}, "permittedInterconnectTypeUri": "Synergy 10Gb Interconnect Link Module", "enclosureIndex": 3}]},

                 "enclosureType": "SY12000",
                 "enclosureIndexes": [1, 2, 3],
                 "interconnectBaySet": "3",
                 "redundancyType": "HighlyAvailable",
                 "internalNetworkUris": [],
                 "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                 "qosConfiguration": None,
                 "uplinkSets": []
                 }


les_potash = {'name': 'LE_POTASH',
              # 'enclosureUris': ['ENC:HD345r'],   #REAL
              'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102', 'ENC:0000A66103'],  # DCS
              'enclosureGroupUri': 'EG:enc_groups_potash',
              'firmwareBaselineUri': None,
              'forceInstallFirmware': False
              }


les_potash_1enc = {'name': 'LE_POTASH',
                   # 'enclosureUris': ['ENC:HD345r'],   #REAL
                   'enclosureUris': ['ENC:0000A66101'],  # DCS
                   'enclosureGroupUri': 'EG:enc_groups_potash',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

les_potash_2enc = {'name': 'LE_POTASH',
                   'enclosureUris': ['ENC:0000A66101', 'ENC:0000A66102'],  # REAL
                   'enclosureGroupUri': 'EG:enc_groups_potash',
                   'firmwareBaselineUri': None,
                   'forceInstallFirmware': False
                   }

les_demo_3enc = {'name': 'LE_DEMO',
                 'enclosureUris': ['ENC:FVTCRMENC1', 'ENC:FVTCRMENC2', 'ENC:FVTCRMENC3'],  # DEMO REAL
                 'enclosureGroupUri': 'EG:enc_groups_demo',
                 'firmwareBaselineUri': None,
                 'forceInstallFirmware': False
                 }

les_1enc = {'name': 'LE_1_Encl',
            'enclosureUris': ['ENC:0000A66101'],  # 1 ENCL
            'enclosureGroupUri': 'EG:enc_groups_1_Encl',
            'firmwareBaselineUri': None,
            'forceInstallFirmware': False
            }

enc_groups_potash_1enc1 = [{'name': 'enc_groups_1_Encl',
                            'type': 'EnclosureGroupV300',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 1,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"}
                             ]}]

enc_groups_1enc_2 = [{'name': 'enc_groups_1_Encl_2',
                      'type': 'EnclosureGroupV300',
                      'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                      'stackingMode': 'Enclosure',
                      'ipAddressingMode': 'IpPool',
                      'ipRangeUris': '',
                      'interconnectBayMappingCount': 0,
                      'enclosureCount': 1,
                      'configurationScript': None,
                      'interconnectBayMappings':
                      [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                       {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"},
                          {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_dcs"}
                       ]}]

enc_groups_potash_2enc1 = [{'name': 'enc_groups_potash',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 2,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                             ]}]

enc_groups_potash_2enc2 = [{'name': 'enc_groups_potash_2',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 2,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                             ]}]

enc_groups_demo_3enc = [{'name': 'enc_groups_demo',
                         'type': 'EnclosureGroupV300',
                         'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                         'stackingMode': 'Enclosure',
                         'ipAddressingMode': 'IpPool',
                         'ipRangeUris': '',
                         'interconnectBayMappingCount': 0,
                         'enclosureCount': 3,
                         'configurationScript': None,
                         'interconnectBayMappings':
                         [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                          {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"}
                          ]}]

enc_groups_demo_3enc2 = [{'name': 'enc_groups_demo_temp',
                          'type': 'EnclosureGroupV300',
                          'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                          'stackingMode': 'Enclosure',
                          'ipAddressingMode': 'IpPool',
                          'ipRangeUris': '',
                          'interconnectBayMappingCount': 0,
                          'enclosureCount': 3,
                          'configurationScript': None,
                          'interconnectBayMappings':
                          [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"},
                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"}
                           ]}]

enc_groups_demo_3enc3 = [{'name': 'enc_groups_demo_temp2',
                          'type': 'EnclosureGroupV300',
                          'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                          'stackingMode': 'Enclosure',
                          'ipAddressingMode': 'IpPool',
                          'ipRangeUris': '',
                          'interconnectBayMappingCount': 0,
                          'enclosureCount': 3,
                          'configurationScript': None,
                          'interconnectBayMappings':
                          [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                           {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"},
                              {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                              {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_demo_pools"}
                           ]}]

enc_groups_potash_2enc3 = [{'name': 'enc_groups_potash_3',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 2,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"},
                                {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_tbird21"}
                             ]}]

enc_groups_patch = [{'name': 'enc_groups_patch',
                     'type': 'EnclosureGroupV400',
                     'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                     'stackingMode': 'Enclosure',
                     'ipAddressingMode': 'External',
                     'interconnectBayMappingCount': 0,
                     'enclosureCount': 3,
                     'configurationScript': None,
                     'interconnectBayMappings':
                     [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': None}
                      ]}]


lig_tbird_1enc_HW_2_potash = {"type": "logical-interconnect-groupV300",
                              "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": "lig_1_Encl_2_potash",
                              "interconnectMapTemplate":
                              {"interconnectMapEntryTemplates": [
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [1],
                              "interconnectBaySet": "3",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                              "qosConfiguration": None,
                              "uplinkSets": []
                              }

enc_groups_1enc_2potash = [{'name': 'enc_groups_2_Potash',
                            'type': 'EnclosureGroupV300',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 1,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                             ]}]

enc_groups_1enc_2potash_temp = [{'name': 'enc_groups_2_Potash_temp',
                                 'type': 'EnclosureGroupV300',
                                 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                 'stackingMode': 'Enclosure',
                                 'ipAddressingMode': 'IpPool',
                                 'ipRangeUris': '',
                                 'interconnectBayMappingCount': 0,
                                 'enclosureCount': 1,
                                 'configurationScript': None,
                                 'interconnectBayMappings':
                                 [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                  ]}]

enc_groups_1enc_2potash_temp2 = [{'name': 'enc_groups_2_Potash_temp2',
                                  'type': 'EnclosureGroupV300',
                                  'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                  'stackingMode': 'Enclosure',
                                  'ipAddressingMode': 'IpPool',
                                  'ipRangeUris': '',
                                  'interconnectBayMappingCount': 0,
                                  'enclosureCount': 1,
                                  'configurationScript': None,
                                  'interconnectBayMappings':
                                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                   ]}]

les_1enc_2potash = {'name': 'LE_2_Potash',
                    'enclosureUris': ['ENC:EM1FFFF600'],  # REAL
                    'enclosureGroupUri': 'EG:enc_groups_2_Potash',
                    'firmwareBaselineUri': None,
                    'forceInstallFirmware': False
                    }

patch_add = [
    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'NetworkPatch',
                    'resourceCategory': 'ethernet-networks',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },
    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [],
        'eTag':''
    },

    {
        'operations': [
            {
                'op': ' ',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'WRONG',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    },

    {
        'operations': [
            {
                'op': 'add',
                'path': '/associatedResources/-',
                'value': {
                    'resourceName': 'enc_groups_patch',
                    'resourceCategory': 'enclosure-groups',
                    'resourceUri': ''
                }
            }
        ],
        'eTag': ''
    }
]

patch_remove = [
    {
        'operations': [
            {
                'op': 'remove',
                'path': '/associatedResources/0'
            }
        ],
        'eTag': ''
    }
]

lig_tbird_1enc_HW_2_potash = {"type": "logical-interconnect-groupV300",
                              "ethernetSettings": {"type": "EthernetInterconnectSettingsV201", "enableIgmpSnooping": False, "igmpIdleTimeoutInterval": 260, "enableFastMacCacheFailover": True, "macRefreshInterval": 5, "enableNetworkLoopProtection": True, "enablePauseFloodProtection": True, "enableRichTLV": False, "interconnectType": "Ethernet", "dependentResourceUri": None, "name": "defaultEthernetSwitchSettings", "category": None, "uri": "/ethernetSettings"},
                              "description": None,
                              "name": "lig_1_Encl_2_potash",
                              "interconnectMapTemplate":
                              {"interconnectMapEntryTemplates": [
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 3}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1},
                                  {"logicalLocation": {"locationEntries": [{"type": "Bay", "relativeValue": 6}, {"type": "Enclosure", "relativeValue": 1}]}, "permittedInterconnectTypeUri": "Virtual Connect SE 40Gb F8 Module for Synergy", "enclosureIndex": 1}]},
                              "enclosureType": "SY12000",
                              "enclosureIndexes": [1],
                              "interconnectBaySet": "3",
                              "redundancyType": "Redundant",
                              "internalNetworkUris": [],
                              "snmpConfiguration": {"type": "snmp-configuration", "readCommunity": "public", "systemContact": "", "trapDestinations": None, "snmpAccess": None, "enabled": True, "description": None, "name": None, "state": None, "category": "snmp-configuration"},
                              "qosConfiguration": None,
                              "uplinkSets": []
                              }

enc_groups_1enc_2potash = [{'name': 'enc_groups_2_Potash',
                            'type': 'EnclosureGroupV400',
                            'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                            'stackingMode': 'Enclosure',
                            'ipAddressingMode': 'IpPool',
                            'ipRangeUris': '',
                            'interconnectBayMappingCount': 0,
                            'enclosureCount': 1,
                            'configurationScript': None,
                            'interconnectBayMappings':
                            [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                             {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                             {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                             ]}]

enc_groups_1enc_2potash_temp = [{'name': 'enc_groups_2_Potash_temp',
                                 'type': 'EnclosureGroupV400',
                                 'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                 'stackingMode': 'Enclosure',
                                 'ipAddressingMode': 'IpPool',
                                 'ipRangeUris': '',
                                 'interconnectBayMappingCount': 0,
                                 'enclosureCount': 1,
                                 'configurationScript': None,
                                 'interconnectBayMappings':
                                 [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                  {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                     {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                     {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                  ]}]

enc_groups_1enc_2potash_temp2 = [{'name': 'enc_groups_2_Potash_temp2',
                                  'type': 'EnclosureGroupV400',
                                  'enclosureTypeUri': '/rest/enclosure-types/SY12000',
                                  'stackingMode': 'Enclosure',
                                  'ipAddressingMode': 'IpPool',
                                  'ipRangeUris': '',
                                  'interconnectBayMappingCount': 0,
                                  'enclosureCount': 1,
                                  'configurationScript': None,
                                  'interconnectBayMappings':
                                  [{'interconnectBay': 1, 'logicalInterconnectGroupUri': None},
                                   {'interconnectBay': 2, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 3, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"},
                                      {'interconnectBay': 4, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 5, 'logicalInterconnectGroupUri': None},
                                      {'interconnectBay': 6, 'logicalInterconnectGroupUri': "LIG:lig_1_Encl_2_potash"}
                                   ]}]

les_1enc_2potash = {'name': 'LE_2_Potash',
                    'enclosureUris': ['ENC:EM1FFFF600'],  # REAL
                    'enclosureGroupUri': 'EG:enc_groups_2_Potash',
                    'firmwareBaselineUri': None,
                    'forceInstallFirmware': False
                    }


users = [{'userName': 'server', 'password': 'serveradmin', 'fullName': 'Sarah', 'roles': ['Server administrator'], 'emailAddress': 'sarah@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'network', 'password': 'networkadmin', 'fullName': 'Nat', 'roles': ['Network administrator'], 'emailAddress': 'nat@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'backup', 'password': 'backupadmin', 'fullName': 'Backup', 'roles': ['Backup administrator'], 'emailAddress': 'backup@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'readonly', 'password': 'readonly', 'fullName': 'Rheid', 'roles': ['Read only'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'storage', 'password': 'storageadmin', 'fullName': 'Rheid', 'roles': ['Storage administrator'], 'emailAddress': 'rheid@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'},
         {'userName': 'software', 'password': 'softwareadmin', 'fullName': 'Software', 'roles': ['Software administrator'], 'emailAddress': 'software@hp.com', 'officePhone': '970-555-0003', 'mobilePhone': '970-500-0003', 'type': 'UserAndRoles'}
         ]
